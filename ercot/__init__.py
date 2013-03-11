import logging
import logging.config

from pkg_resources import Requirement, resource_filename

try:
  loggingConf = \
    resource_filename(Requirement.parse('ercot'), 'conf/logging.conf')
except Exception as e:
  loggingConf = resource_filename(__name__, '../conf/logging.conf')

logging.config.fileConfig(loggingConf)
log = logging.getLogger('ercot')
