# # configuration the appliction

import os

class Config:
    SECRET_KEY = os.urandom(32)

    @staticmethod
    def init_app():
        pass






class DevelopemntConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///db.sqlite"

class ProductionConfig(Config):
    DEBUG = False
    # SQLALCHEMY_DATABASE_URI = "postgresql://username:password@localhost:portnumber/dbname"
    # SQLALCHEMY_DATABASE_URI = os.environ(DATABASE_CONGFIG)
    SQLALCHEMY_DATABASE_URI = "postgresql://django:iti@localhost:5432/itworx_flask"



config= {
    "dev": DevelopemntConfig,
    "prd": ProductionConfig
}