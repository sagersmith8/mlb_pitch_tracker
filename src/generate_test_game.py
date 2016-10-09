import json
import random
import string

STRIKE_WIDTH = .75
STRIKE_BOTTOM = 2
MIN_ATBAT_NUM = 3
MAX_ATBAT_NUM = 15
STRIKE = 'strike'
BALL = 'ball'
PITCH_TYPE = 'pitch_type'
PITCH_CALL = 'pitch_call'
STRIKE_OUT = 'strike_out'
PITCH_TYPES = ['fastball', 'slider', 'curve', 'knuckle', 'changeup']
PITCH_CALLS = [STRIKE, BALL]


def generate_x():
    return random.uniform(-(2*STRIKE_WIDTH), 2*STRIKE_WIDTH)


def generate_y():
    return random.uniform(STRIKE_BOTTOM, STRIKE_BOTTOM+random.randrange(1, 3))


def generate_pitch_type():
    return random.choice(PITCH_TYPES)


def generate_pitch_call():
    return random.choice(PITCH_CALLS)


def generate_pitch():
    return{
        'x': generate_x(),
        'y': generate_y(),
        'pitch_type': generate_pitch_type(),
        'pitch_call': generate_pitch_call()
    }


def generate_game_title():
    return {
        'id': random.randint(100000, 999999),
        'home': generate_name(),
        'away': generate_name()
    }


def generate_games():
    games = []
    for _ in xrange(random.randint(3, 15)):
        games.append(generate_game_title())
    return games


def generate_name():
    name = random.choice(string.ascii_uppercase)
    for _ in range(random.randint(2, 8)):
        name += random.choice(string.ascii_lowercase)

    return name


def generate_full_name():
    return '{} {}'.format(generate_name(), generate_name())


def generate_at_bat():
    pitches = []
    strike_count = 0
    ball_count = 0
    strike_out = False
    while True:
        pitches.append(generate_pitch())
        if pitches[-1][PITCH_CALL] == STRIKE:
            print 'got a strike'
            strike_count += 1
        else:
            print ball_count
            ball_count += 1
        if strike_count == 3:
            strike_out = True
            break
        elif ball_count == 4:
            break

    return {
        'pitcher': generate_name(),
        'batter': generate_name(),
        'pitches': pitches,
        STRIKE_OUT: strike_out
    }


def generate_half_inning():
    atbats = []
    outs = 0
    while True:
        atbats.append(generate_at_bat())

        if atbats[-1][STRIKE_OUT]:
            outs += 1
        if outs == 3:
            return atbats


def generate_inning():
    return {
        'top': generate_half_inning(),
        'bottom': generate_half_inning()
    }


def generate_game():
    return {
        'day': random.randint(1, 30),
        'month': random.randint(1, 12),
        'year': random.randint(1909, 2016),
        'home': generate_name(),
        'away': generate_name(),
        'innings': [generate_inning() for _ in xrange(9)]
    }


if __name__ == '__main__':
    json_data = json.dumps(generate_game(), indent=4)
    with open('test_game.json', 'w') as file:
        file.write(json_data)
