import os
import pathlib
from dotenv import load_dotenv

basedir = pathlib.Path(__file__).parent.resolve()
load_dotenv()


class Config:
    DEBUG = False
    SECRET_KEY = os.getenv("SECRET_KEY")
    UPLOADS = basedir / "uploads"


class DevelopmentConfig(Config):
    SECRET_KEY = "very secret"
    DEBUG = True


class ProductionConfig(Config):
    pass