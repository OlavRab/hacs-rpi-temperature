import logging
from datetime import date, datetime, timedelta

import homeassistant.helpers.config_validation as cv
import requests


from homeassistant.components.sensor import PLATFORM_SCHEMA
from homeassistant.const import ATTR_DATE, CONF_RESOURCES
from homeassistant.helpers.entity import Entity

__version__ = '0.1'

_LOGGER = logging.getLogger(__name__)

SENSOR_TYPES = {'today': ['Vandaag', 'mdi:thermometer']}

