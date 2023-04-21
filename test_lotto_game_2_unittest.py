import unittest
from lotto_game_2 import Game, Player, Card, PlayersList, Keg
import random
from io import StringIO
import copy     # Для копирования какого-либо объекта

class TestKeg(unittest.TestCase):

    def test_init(self):
        self.assertEqual(len(Keg.keg_numbers_list), 90)
