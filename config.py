import os


class Config:

 QUOTES_BASE_URL='http://quotes.stormconsultancy.co.uk/random.json'
 SECRET_KEY=os.environ.get('SECRET_KEY')
 SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://lenovo:1234@localhost/blog'


class ProdConfig(Config):

    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}