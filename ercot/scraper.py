import optparse
import os
import sys
import urllib3

from . import log
from BeautifulSoup import BeautifulSoup


def collect_links(http, url):
  ''' Retrieve and parse url, yielding download links '''
  p = BeautifulSoup(http.request('GET', url).data)
  items = iter(p.findAll('td'))
  while True:
    item = next(items)
    if item.text[:4] == 'cdr.' and item.text[-4:] == '_csv':
      link = None
      name = item.text
      while link is None:
        item = next(items)
        link = item.find('a')
      href = [value for (key, value) in link.attrs if key == 'href'][0]
      yield (name, href)


def archive(http, url, destination):
  ''' Spider and archive specified url '''
  protocol, delim, remainder = url.partition('://')
  host, _, path = remainder.partition('/')
  base_url = protocol + delim + host

  for (name, path) in collect_links(http, url):
    log.info("Retrieving %s%s", base_url, path)
    resp = http.request('GET', base_url + path, preload_content=False)

    _, _, filename = \
      resp.getheader('content-disposition').partition('filename=')

    _, _, _, date, time, identifier, extension = filename.split('.')

    target = os.path.join(destination, identifier, date)

    if not os.path.exists(target):
      try:
        log.info("Creating %s", target)
        os.makedirs(target)
      except os.error:
        if not os.path.exists(target):
          raise

    with open(os.path.join(target, filename), 'w') as outp:
      log.info("Writing to %s", outp.name)
      outp.write(resp.read())


def main():
  parser = optparse.OptionParser(usage='usage: %prog [options] url')

  parser.add_option('-d', '--destination',
    dest='destination',
    help='Destination to archive results. [Default: data/]',
    metavar='PATH',
    default='data'
  )

  (options, urls) = parser.parse_args()

  if not urls:
    parser.print_help()
    sys.exit(-1)

  http = urllib3.PoolManager()

  for url in urls:
    archive(http, url, destination=options.destination)


if __name__ == '__main__':
  main()
