import logging
logger = logging.getLogger(__name__)

from app import app
from flask import render_template
import requests

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/postcode/<postcode>')
def postcode(postcode):
    try:
        r = requests.get("http://api.postcodes.io/postcodes/{}"
            .format(postcode))
        r.raise_for_status()
        return render_template('show.html',
                                r=r.json().get('result',{}))
    except Exception as e:
        return str(e) ## TODO: create an error template or a warning div in index.html
