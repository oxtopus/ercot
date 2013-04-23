import csv
import glob
import os

from collections import namedtuple
from optparse import OptionParser
from zipfile import ZipFile

import core


def collect(pattern, suffix='.zip'):
  """ Yield all records extracted from matching archived filenames """

  walk = lambda pattern: (
    os.path.join(dirpath, filename) 
    for pathname in glob.glob(pattern) 
    for (dirpath, dirnames, filenames) in os.walk(pathname) 
    for filename in filenames
  )

  for path in walk(pattern):
    if path.endswith(suffix):
      with ZipFile(path, 'r') as archive:
        for name in archive.namelist():
          with archive.open(name, 'r') as inp:
            csvin = csv.reader(inp)
            Record = namedtuple('Record', next(inp))
            for line in csvin:
              try:
                yield Record._make(line)
              except TypeError:
                pass


def getCLIParser():
  parser = OptionParser(usage="Usage: %prog [options] TARGET")

  parser.add_option("-k", "--key", 
    dest="apiKey",
    metavar="KEY",
    help="Grok API Key (Default: GROK_API_KEY environment variable)")

  parser.add_option("-a", "--api",
    dest="apiUrl", 
    metavar="URL",
    help="Grok API Base URL (Default: GROK_API_URL environment variable, " \
         "otherwise grokpy default)")
  
  return parser