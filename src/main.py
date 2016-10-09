from datetime import datetime

import bottle
from bottle import route, post
from core import respond
import pytz

import game_parser
bottle.debug(True)
app = bottle.default_app()


@route('/')
@route('/<games>')
@route('/<games>/')
@post('/')
@post('/<games>')
@post('/<games>/')
def home(games=None):
    today = bottle.request.forms.get('date')
    if today is not None:
        year, month, day = today.split('-')
    else:
        today = datetime.now(pytz.utc)
        tz = 'US/Pacific'
        today = today.astimezone(pytz.timezone(tz))
        day = str(today.day).zfill(2)
        month = str(today.month).zfill(2)
        year = today.year

    return respond(
        'index.html',
        {
            'games': game_parser.list_games({'day': day, 'year': year, 'month': month}),
            'day': day,
            'month': month,
            'year': year
        }
    )


@route('/view_game/<game_id>')
@route('/view_game/<game_id>/')
def view_game(game_id):
    game = game_parser.get_game(game_id)

    return respond(
        'view-game.html',
        {
            'home': game['home']['name'],
            'away': game['away']['name'],
            'day': game['day'],
            'month': game['month'],
            'year': game['year'],
            'game_data': game
        }
    )
