class BaseConfig():
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

class DevelopmentConfig(BaseConfig):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://root:wsr29yhi@localhost/books'
    DATABASE_CONNECT_OPRTIONS = {}
    JSON_AS_ASCII = False