from unittest import TestCase
import game_parser

def file_as_string(text_file):
    with open(text_file, 'r') as open_file:
        file_text = open_file.read()
    return file_text

class TestFileTests(TestCase):
    def test_read_game(self):
        game_text = file_as_string('test/test_files/players.xml')
        self.assertGreater(len(game_parser.parse_game(game_text)), 0)

        inning_text = file_as_string('test/test_files/inning_all.xml')
        self.assertGreater(len(game_parser.parse_innings(inning_text)), 0)

    def test_read_game_list(self):
        game_list_text = file_as_string('test/test_files/scoreboard.xml')
        self.assertGreater(len(game_parser.parse_game_list(game_list_text)), 0)
