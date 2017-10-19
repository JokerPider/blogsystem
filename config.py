#coding: utf-8
class Config():
    pass

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql://root:caomu888@127.0.0.1:3306/flask"
    # SQLALCHEMY_DATABASE_URI = "sqlite:///flask.db"
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True