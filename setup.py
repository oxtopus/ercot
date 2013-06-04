from setuptools import setup

version = {}
execfile('ercot/__version__.py', {}, version)

requirements = map(str.strip, open('requirements.txt').readlines())

setup(
  name = 'ercot',
  version = version['__version__'],
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
  namespace_packages = ['ercot'],
  package_dir = \
    {
      'ercot': 'ercot'
    },
  packages = ['ercot'],
  requires = requirements,
  install_requires = requirements
)
