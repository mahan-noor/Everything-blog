import os


class Config:

 QUOTES_BASE_URL='http://quotes.stormconsultancy.co.uk/random.json'
 SECRET_KEY=os.environ.get('SECRET_KEY')


 class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}