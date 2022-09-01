import os

from flask import Flask

app = Flask(__name__)

env_config = os.getenv("APP_SETTINGS", "config.DevelopmentConfig")
app.config.from_object(env_config)
app.config["UPLOADS"].mkdir(exist_ok=True)

from app import routes
