import logging
import logging.config

from pkg_resources import resource_filename


logging.config.fileConfig(resource_filename(__name__, 'logging.conf'))
log = logging.getLogger(__name__)