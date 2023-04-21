from  lotto_game_main import *
from lotto_game import Player, Card
import random
import sys
import mock
import pytest

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


def test_number_of_players():

    with mock.patch('builtins.input', return_value=2):
        assert number_of_players() == 2

    #

    # with pytest.raises(ValueError):
    #     number_of_players()


def test_player_type():

    with mock.patch('builtins.input', return_value=0):
        assert player_type() == 'Человек'

    with mock.patch('builtins.input', return_value=1):
        assert player_type() == 'Компьютер'

    #TODO: Пункт 4 в вопросах

def test_player_name():

    assert player_name('Компьютер', 1) == 'Компьютер_1'

    with mock.patch('builtins.input', return_value='Sam'):
        assert player_name('Человек', 1) == 'Sam'


def test_player_registration():

    with mock.patch('builtins.input', return_value=1):
        assert type(player_registration(2)) is dict
        assert player_registration(2) == {1: ('Компьютер', 'Компьютер_1'), 2: ('Компьютер', 'Компьютер_2')}

    with mock.patch('builtins.input', return_value=0):
        assert type(player_registration(2)) is dict
        assert player_registration(2) == {1: ('Человек', 0), 2: ('Человек', 0)}


def test_players_generation():

    players_dict = {1: ('Компьютер', 'Компьютер_1'), 2: ('Компьютер', 'Компьютер_2')}
    number_of_players = 2

    assert type(players_generation(players_dict, number_of_players)) is list
    assert isinstance(players_generation(players_dict, number_of_players)[0], object)
    assert isinstance(players_generation(players_dict, number_of_players)[1], object)


def test_cards_generation():

    players_dict = {1: ('Компьютер', 'Компьютер_1'), 2: ('Компьютер', 'Компьютер_2')}
    number_of_players = 2

    for i in range(number_of_players):
        assert type(cards_generation(players_dict, number_of_players)) is list
        assert isinstance(cards_generation(players_dict, number_of_players)[i][0], object)
        assert isinstance(cards_generation(players_dict, number_of_players)[i][1], list)
        assert cards_generation(players_dict, number_of_players)[i][2] == 'Компьютер'
        assert cards_generation(players_dict, number_of_players)[i][3] == 0
        assert cards_generation(players_dict, number_of_players)[i][4] is None
        assert cards_generation(players_dict, number_of_players)[i][5] is None


def test_threshold_generation():

    cards_list = [[1, [[1], [2], [3]], 'Компьютер', 0, None, None], [1, [[1], [2], [3]], 'Компьютер', 15, None, None]]
    number_of_players = 2

    assert type(threshold_generation(cards_list, number_of_players)) is list
    assert threshold_generation(cards_list, number_of_players) == [False, True]


def test_keg_roll_out():

    assert len(keg_roll_out()) == 90
    assert keg_roll_out() == list(range(1, 91))


def test_cards_to_screen():
    #TODO:
    pass

def test_keg_choice_func():

    keg_numbers_list = list(range(1, 91))

    assert type(keg_choice_func(keg_numbers_list)) is list
    assert len(keg_choice_func(keg_numbers_list)) == 1
    assert type(keg_choice_func(keg_numbers_list)[0]) is int


def test_keg_to_screen(capsys):

    roll_counter = 1
    keg_choice = [15]

    keg_to_screen(roll_counter, keg_choice)
    captured = capsys.readouterr()

    assert captured.out.strip() == f'Ход - {roll_counter}. Выпал бочонок со значением: {keg_choice[0]}'


def test_keg_list_adj():

    keg_numbers_list = list(range(1, 91))
    keg_choice = [15]

    assert keg_list_adj(keg_numbers_list, keg_choice) == list(range(1, 91)).remove(keg_choice[0])


def test_check_continue_func():

    with mock.patch('builtins.input', return_value=1):
        assert check_continue_func() == 1


    with mock.patch('builtins.input', return_value=0):
        assert check_continue_func() == 0