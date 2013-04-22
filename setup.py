import os
import re

from distutils.core import setup

try:
    import setuptools
except ImportError:
    pass

base_path = os.path.dirname(__file__)
with open(os.path.join(base_path, 'ercot', '__version__.py')) as fp:
  version = re.compile(r".*__version__ = '(.*?)'", re.S)\
              .match(fp.read()) \
              .group(1)

setup(
  name = 'ercot',
  version = version,
  description = "ERCOT Scraper",
  classifiers = \
    [
      'Intended Audience :: Developers',
      'License :: OSI Approved :: MIT License',
      'Programming Language :: Python',
      'Programming Language :: Python :: 2',
      'Topic :: Software Development :: Libraries',
    ],
  keywords = 'ercot',
  author = 'Austin Marshall',
  author_email = 'oxtopus@gmail.com',
  url = 'https://github.com/oxtopus/ercot',
  license = 'MIT',
  package_dir = \
    {
      'ercot': 'ercot',
      '': 'apps'
    },
  packages = ['ercot'],
  entry_points = \
    {
      'console_scripts': [
        'system_wide_demand = system_wide_demand:system_wide_demand',
      ]
    },
  requires = map(str.strip, open('requirements.txt').readlines()),
  data_files = \
    {
      'conf': ['conf/logging.conf']
    }.items(),
)
