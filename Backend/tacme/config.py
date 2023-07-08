class Config(object):
    CONNECTION_STRING = ''

class ConfigLocale(Config):
   CONNECTION_STRING = 'mongodb://localhost:27017'

class ConfigProd(Config):
    pass