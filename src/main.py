import logging
from datetime import datetime
import bottle
from bottle import route
from core import respond
import json
from generate_test_game import generate_game
import pytz

bottle.debug(True)
app = bottle.default_app()


@route('/')
def home():
    dt = datetime.now(pytz.utc)
    tz = 'US/Pacific'
    dt = dt.astimezone(pytz.timezone(tz))

    msg = "Sage and Bridger will add stuff here. Date: {}".format(dt)
    logging.info('someone hit the home page')  # app engine log.
    return respond('index.html', {'msg': msg})


@route('/test_game_data')
@route('/test_game_data/')
def test_game():
    return respond('index.html', {'msg': json.dumps(generate_game(), indent=4)})


@route('/view_game/<month>/<day>/<year>/<home>/<game_number>')
@route('/view_game/<month>/<day>/<year>/<home>/<game_number>/')
@route('/view_game/<month>/<day>/<year>/<home>/')
@route('/view_game/<month>/<day>/<year>/<home>')
def view_game(month, day, year, home, game_number=None):
    game = generate_game()
    return respond(
        'view-game.html',
        {
            'home': home.upper(),
            'away': game['away'].upper(),
            'day': day,
            'month': month,
            'year': year,
            'game_data': generate_game()
        }
    )
