import utilities
from logging_helper import logger

class Config:
    srv_host  = ""
    srv_port  = 0
    srv_debug = False
    srv_drivers = ""

    db_name = ""
    db_host = ""
    db_user = ""
    db_password = ""

    nao_ip   = ""
    nao_port = 0
    nao_user = ""
    nao_password = ""

    def __init__(self):
        configuration = utilities.read_yaml('config.yaml')
        logger.info("Loaded configuration: {}".format(configuration))
        self.load_config(configuration)

    def load_config(self, config):
        self.srv_debug   = config['server']['debug']
        self.srv_host    = config['server']['host']
        self.srv_port    = config['server']['port']
        self.srv_drivers = config['server']['drivers']

        self.db_host     = config['database']['host']
        self.db_name     = config['database']['name']
        self.db_user     = config['database']['user']
        self.db_password = config['database']['password']

        self.nao_ip       = config['nao']['ip']
        self.nao_port     = config['nao']['port']
        self.nao_user     = config['nao']['user']
        self.nao_password = config['nao']['password']
