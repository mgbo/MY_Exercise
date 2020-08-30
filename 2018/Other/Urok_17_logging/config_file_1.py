
from configparser import ConfigParser

cfg = ConfigParser()

cfg.read('config.ini')
cfg.sections()

cfg.get('installation', 'library')