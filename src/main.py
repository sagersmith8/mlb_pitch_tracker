import bottle
from bottle import route
import logging
from core import respond

bottle.debug(True)
app = bottle.default_app()


@route('/')
def home():
    msg = "Sage and Bridger will add stuff here."
    logging.info('someone hit the home page')  # app engine log.
    return respond('index.html', {'msg': msg})
