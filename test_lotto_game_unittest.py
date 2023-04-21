import unittest
import lotto_game_main
from lotto_game import Player, Card
from random import sample
from contextlib import redirect_stdout
from io import StringIO
import copy     # Для копирования какого-либо объекта



class TestPlayer(unittest.TestCase):

    def test_init(self):
        test_player = Player(1, 'Человек', 'Sam')
        self.assertEqual(test_player.number, 1)
        self.assertEqual(test_player.player_type, 'Человек')
        self.assertEqual(test_player.name, 'Sam')


class TestCard(unittest.TestCase):

    def test_card_correction(self):
        initial_card_rows_all = None
        test_card = Card('Test')
        card_rows_all = test_card.draw_card()
        # копия значений объекта card_rows_all
        initial_card_rows_all = copy.deepcopy(card_rows_all)
        keg_number = list(set(card_rows_all[0]))[1]
        corrected_card = test_card.card_correction(keg_number, card_rows_all)
        self.assertFalse(any(item == keg_number for item in corrected_card[0]))
        self.assertFalse(corrected_card == initial_card_rows_all)

    def test_card_presentation(self):
        test_card = Card('Test')
        card_rows_all = test_card.draw_card()
        dash_multiplier = (26 - len(test_card.owner)) // 2
        upper_line_len = len('-' * dash_multiplier + test_card.owner + '-' * dash_multiplier)
        expected_print = str('-' * dash_multiplier + test_card.owner + '-' * (dash_multiplier + (26 - upper_line_len)) +
                                '\n{:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2}'.format(card_rows_all[0][0],
                                card_rows_all[0][1], card_rows_all[0][2], card_rows_all[0][3], card_rows_all[0][4],
                                card_rows_all[0][5], card_rows_all[0][6], card_rows_all[0][7], card_rows_all[0][8]) +
                                '\n{:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2}'.format(card_rows_all[1][0],
                                card_rows_all[1][1], card_rows_all[1][2], card_rows_all[1][3], card_rows_all[1][4],
                                card_rows_all[1][5], card_rows_all[1][6], card_rows_all[1][7], card_rows_all[1][8]) +
                                '\n{:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2}'.format(card_rows_all[2][0],
                                card_rows_all[2][1], card_rows_all[2][2], card_rows_all[2][3], card_rows_all[2][4],
                                card_rows_all[2][5], card_rows_all[2][6], card_rows_all[2][7], card_rows_all[2][8]) +
                                '\n' + '-' * 26)

        with redirect_stdout(StringIO()) as sout:
            test_card.card_presentation(card_rows_all)

        # the stream replacing `stdout` is available outside the `with`
        # you may wish to strip the trailing newline
        retval = sout.getvalue().rstrip('\n')

        # test the string captured from `stdout`
        self.assertEqual(retval, expected_print)

