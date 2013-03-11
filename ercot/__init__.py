import logging
import logging.config

from pkg_resources import Requirement, resource_filename

logging.config.fileConfig(
    resource_filename(Requirement.parse('ercot'), 'conf/logging.conf'))
log = logging.getLogger(__name__)
