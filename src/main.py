import datetime

import bottle
from bottle import route, post
from core import respond
from generate_test_game import generate_game, generate_games

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
        today = datetime.datetime.now()
        day = today.day
        month = today.month
        year = today.year

    return respond(
        'index.html',
        {
            'games': generate_games(),
            'day': day,
            'month': month,
            'year': year
        }
    )


@route('/view_game/<game_id>')
@route('/view_game/<game_id>/')
def view_game(game_id):
    game = generate_game()

    return respond(
        'view-game.html',
        {
            'home': game['home'].upper(),
            'away': game['away'].upper(),
            'day': game['day'],
            'month': game['month'],
            'year': game['year'],
            'game_data': generate_game()
        }
    )
