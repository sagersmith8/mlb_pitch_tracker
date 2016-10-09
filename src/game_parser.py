from lxml import etree
import requests

DATA_PREFIX = 'http://gd2.mlb.com/components/game/mlb'
GAME_KEYS = ['id', 'status']
PITCH_KEYS = ['nasty', 'sz_top', 'sz_bot', 'px', 'pz', 'start_speed', 'type', 'des', 'pitch_type']
AT_BAT_KEYS = ['batter', 'pitcher', 'des', 'p_throws', 'stand']
PLAYER_KEYS = ['id', 'position', 'bat_order', 'first', 'last']
VENUE_KEYS = ['venue']

def get_game(game_id):
    game_loc = game_path(game_id)
    game = parse_game(grab_asset('{}/players.xml'.format(game_loc)))
    if not game:
        return game
    game['innings'] = parse_innings(grab_asset('{}/inning/inning_all.xml'.format(game_loc)))

    return game

def game_path(game_id):
    return 'year_{year}/month_{month:0>2}/day_{day:0>2}/gid_{}'.format(
        game_id, **extract_date(game_id)
    )

def parse_innings(inning_xml):
    if not inning_xml:
        return None

    innings = etree.fromstring(inning_xml)

    inning_list = []
    for inning in innings:
        inning_data = {}
        for team_inning in inning:
            at_bats = []
            for at_bat in team_inning:
                if at_bat.tag == 'atbat':
                    at_bat_data = filter_dict(
                        dict(at_bat.items()),
                        AT_BAT_KEYS
                    )
                    pitches = []
                    for pitch in at_bat:
                        if pitch.tag == 'pitch':
                            pitches.append(filter_dict(
                                dict(pitch.items()),
                                PITCH_KEYS
                            ))
                    at_bat_data['pitches'] = pitches
                    at_bats.append(at_bat_data)
            inning_data[team_inning.tag] = at_bats
        inning_list.append(inning_data)

    return inning_list

def parse_game(game_xml):
    if not game_xml:
        return None

    game = etree.fromstring(game_xml)
    game_map = filter_dict(
        dict(game.items()),
        VENUE_KEYS)
    game_map.update({'away': {'players': {}},
                     'home': {'players': {}}})

    for team in game:
        if team.tag == 'team':
            team_info = dict(team.items())
            team_type = team_info['type']
            game_map[team_type]['name'] = team_info['name']

            team_players = game_map[team_type]['players']

            for player in team:
                if player.tag == 'player':
                    player_data = filter_dict(
                        dict(player.items()),
                        PLAYER_KEYS)
                    team_players[player_data['id']] = player_data
    return game_map

def extract_date(game_id):
    date = {}
    date['year'], date['month'], date['day'] = game_id.split('_')[:3]
    return date

def list_games(date):
    scoreboard_xml = grab_asset('year_{year}/month_{month:0>2}/day_{day:0>2}/scoreboard.xml'.format(**date))
    return parse_game_list(scoreboard_xml)

def parse_game_list(scoreboard_xml):
    if not scoreboard_xml:
        return None

    games = etree.fromstring(scoreboard_xml)

    game_list = []
    for game_info in games:
        game_data = filter_dict(
            dict(game_info.find('game').items()),
            GAME_KEYS
        )
        game_data.update({
            'away': dict(game_info.find('team[1]').items())['name'],
            'home': dict(game_info.find('team[2]').items())['name']
        })
        game_list.append(game_data)

    return game_list


def filter_dict(_dict, keys):
    return {key: _dict[key] for key in keys if key in _dict}

def grab_asset(asset):
    response = requests.get("{base}/{asset}".format(base=DATA_PREFIX, asset=asset))
    return response.content if response else None

if __name__ == '__main__':
    import sys
    import json
    date = {}
    req = sys.argv[1]
    if req == 'list':
        date['year'], date['month'], date['day'] = sys.argv[2:]
        print(json.dumps(list_games(date), indent=4))
    if req == 'get':
        game_id, = sys.argv[2:]
        print(json.dumps(get_game(game_id), indent=4))
