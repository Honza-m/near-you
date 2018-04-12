import logging
logger = logging.getLogger(__name__)

from flask import Flask
app = Flask(__name__)

from . import views
