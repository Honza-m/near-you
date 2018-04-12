import logging
root = logging.getLogger()
root.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
frmt = logging.Formatter(logging.BASIC_FORMAT)
ch.setFormatter(frmt)
ch.setLevel(logging.DEBUG)
root.addHandler(ch)

from app import app
app.run(debug=True)
