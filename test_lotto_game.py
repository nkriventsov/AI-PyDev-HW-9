from lotto_game import Player, Card
import random
import sys

test_card = Card('Test')
test_card_data = test_card.draw_card()
test_card_two = Card('Test_Two')
test_card_two_data = test_card_two.draw_card()

def test_draw_card():
    assert len(test_card_data) == 3
    assert len(test_card_data[0]) == 9
    assert len(test_card_data[1]) == 9
    assert len(test_card_data[2]) == 9
    assert type(test_card_data) == type([])
    assert test_card_data[0].count('') == 4
    assert test_card_data[1].count('') == 4
    assert test_card_data[2].count('') == 4
    assert len(set(list(test_card_data[0] + test_card_data[1] + test_card_data[2]))) == 16
    assert set(list(test_card_data[0] + test_card_data[1] + test_card_data[2])) != \
           set(list(test_card_two_data[0] + test_card_two_data[1] + test_card_two_data[2]))

