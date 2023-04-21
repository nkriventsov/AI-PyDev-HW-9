from random import sample, choice
import sys

'''
Правила игры
Игра ведется с помощью специальных карточек, на которых отмечены числа, и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 1 строки по 9 клеток. В каждой строке по 5 случайных цифр, расположенных по возрастанию. 
Все цифры в карточке уникальны.

Пример карточки:
--------------------------
    9 41 62          74 90
 2    27    75 78    82
   41 56 61     76      86
--------------------------
В игре произвольное количество игроков (было: В игре 2 игрока: пользователь и компьютер). 
Типы игроков 'Человек' или 'Компьютер' 
Каждому в начале выдается случайная карточка.


Каждый ход выбирается один случайный бочонок и выводится на экран. 
Также выводятся карточки игроков (было: игрока и карточка компьютера).

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.

Если игрок выбрал "зачеркнуть":

если цифра есть на карточке - она зачеркивается и игра продолжается.
если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":

если цифра есть на карточке - игрок проигрывает и игра завершается.
если цифры на карточке нет - игра продолжается. Побеждает тот, кто первый закроет все числа на своей карточке.
Пример одного хода:
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
21 11    18    48    71
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11
      16 49    55 88    77
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

'''

'''
Возможные классы:
- Игрок
    Свойства: 1. Номер игрока, 2. Тип (Человек/Компьютер), 1. Имя,
    Методы: 1. Создание, 2. Зачёркивание
?- Бочонок
?    Свойства: 1. целочисленный тип, 
?    Методы: 1. выбор в новом ходе
- Карточка
    Свойства: 1. Вид (1х9), 2. Владелец карточки
    Методы: 1. генерация новой карточки, 2. зачёркивание
'''


# Создаём класс Бочонок
class Keg:

    keg_numbers_list = list(range(1, 91))
    roll_counter = 0

    def __init__(self):
        self.keg_choice = sample(Keg.keg_numbers_list, 1)
        Keg.roll_counter += 1
        self.keg_remove = Keg.keg_numbers_list.remove(self.keg_choice[0])

    def __str__(self):
        # Отображаем на экране значение выпавшего бочонка для игроков
        return f'\nХод - {Keg.roll_counter}. Выпал бочонок со значением: {self.keg_choice[0]}'


# Создаём класс Карточка
class Card:
    # Инициализация объекта класса
    def __init__(self, owner):
        self._card = self.draw_card()
        self.owner = owner

    @property
    def card_rows_all(self):
        return self._card

    def draw_card(self) -> list:
        # Генерация чисел на новой карточке
        new_card_draw = sample(range(1, 91), k=15)

        # Разбиваем числа на 3 ряда по возрастанию
        row_first = sorted(new_card_draw[:5])
        row_second = sorted(new_card_draw[5:10])
        row_third = sorted(new_card_draw[10:])

        card_rows_all = [row_first, row_second, row_third]

        # Перезаписываем ряды данных с добавлением случайных пробелов
        counter = 0

        for item in card_rows_all:
            iterable_list = iter(item)
            indices = list(range(len(item) + 4))
            empty_indices = set(sample(indices, 4))
            card_rows_all[counter] = ['' if i in empty_indices else next(iterable_list) for i in indices]
            counter += 1

        return card_rows_all

    # @card_rows_all.setter
    def card_correction(self, keg_number, card_rows_all_list):

        i = 0
        for x in card_rows_all_list:
            for y in x:
                if x[i] is keg_number:
                    x[i] = '-'
                if i == len(x)-1:
                    i = 0
                else:
                    i += 1

        return card_rows_all_list

    # Достиг ли игрок порога совпадений или нет
    def threshold_check(self):
        return (self.card_rows_all[0].count('-') +
                self.card_rows_all[1].count('-') +
                self.card_rows_all[2].count('-')) == 15

    # Вывод карточки на экран
    def __str__(self):
        # Расчитываем количество тире для верхнего колонтитула карточки с учётом отображения имени игрока в центре
        symbols_per_line = 27
        dash_multiplier = (symbols_per_line - len(self.owner)) // 2
        # Высчитываем длину верхнего колонтитула с именем игрока по центру
        upper_line_len = len('-' * dash_multiplier + self.owner + '-' * dash_multiplier)
        # Выводим на экран верхний колонтитул
        card_string = '-' * dash_multiplier + self.owner + '-' * (dash_multiplier + (symbols_per_line - upper_line_len)) + '\n'
        for item in self._card:
            for char in item:
                card_string += f'{str(char):>3}'
            card_string += '\n'
        card_string += '-' * symbols_per_line

        return card_string


# Создаём класс Игрок
class Player:

    # Инициализация объекта класса
    def __init__(self, number, player_type, name):
        self.number = number
        self.player_type = player_type
        self.name = name
        self.card = Card(self.name)

    # def __str__(self):
    #     return f'Игрок №: {self.number} Тип: {self.player_type} Имя: {self.name} '
    #
    # @property
    # def player_card(self):
    #     return self.card


class PlayersList:

    def __init__(self, players_list):
        self._players_list = players_list

    @property
    def name(self) -> list:
        return self._players_list

    @property
    def show_the_player(self) -> list:
        return [Player(x+1, players_list[x][0], players_list[x][1]) for x in range(len(self._players_list))]


class Game:

    @staticmethod
    def get_number_of_players() -> int:

        number_of_players = 0

        while number_of_players < 1:
            try:
                number_of_players = int(input('Введите количество игроков: '))
                if number_of_players < 1:
                    raise ValueError
            except ValueError:
                print('Введено некорректное значение!')

        return number_of_players

    @staticmethod
    def player_list_create() -> list:
        return [[None, None] for i in range(Game.get_number_of_players())]

    @staticmethod
    def player_type() -> str:
        player_type_list = ['Человек', 'Компьютер']
        player_type_result = None
        while True:
            try:
                player_type_choice = int(input(f'Пожалуйста, выберите тип игрока: 0 - Человек, 1 - Компьютер. '))
                if player_type_choice != 0 and player_type_choice != 1:
                    raise ValueError()
            except ValueError:
                print('Введено некорректное значение!')
                continue
            else:
                player_type_result = player_type_list[player_type_choice]
                break
        return player_type_result

    @staticmethod
    def player_name(player_type_result, comp_type_counter) -> str:
        if player_type_result == 'Компьютер':
            player_name_choice = f'{player_type_result}_{comp_type_counter}'
        else:
            player_name_choice = input('Введите имя игрока: ')
        return player_name_choice

    @staticmethod
    def player_list_fill() -> list:
        players_list = Game.player_list_create()
        comp_type_counter = 1
        for i in range(len(players_list)):
            interim_type = Game.player_type()
            players_list[i][0] = interim_type
            players_list[i][1] = Game.player_name(interim_type, comp_type_counter)
            if interim_type == 'Компьютер':
                comp_type_counter += 1
        # print(players_list)

        return players_list

    @staticmethod
    def check_continue_func():
        # Пользователю предлагается зачеркнуть цифру на карточке или продолжить
        check_or_continue = None
        while check_or_continue != 0 and check_or_continue != 1:
            try:
                check_or_continue = int(input('\nВыбор: зачеркнуть цифру на карточке - 0 или продолжить - 1? '))
                if check_or_continue != 0 and check_or_continue != 1:
                    raise ValueError
            except ValueError:
                print('Введено некорректное значение!')

        return check_or_continue

    @staticmethod
    def game_play():
        while True:
            for i in range(len(players_list)):
                print(players[i].card)

            keg_choice = Keg()
            print(keg_choice)
            for i in range(len(players_list)):
                # Ищем выпавшее число в карточках игроков
                find_num_in_card = any(keg_choice.keg_choice[0] in sublist for sublist in players[i].card.card_rows_all)

                # Проверяем человек или компьютер
                if players[i].player_type == 'Человек':

                    interim_choice = Game.check_continue_func()

                    # Проверяем, отображаем и выходим из игры в случае некорректного выбора игрока
                    if find_num_in_card and interim_choice == 1:
                        print(f'\nИгрок {players[i].name} проиграл!'
                              f'\nЗначение {keg_choice.keg_choice[0]} есть в карточке игрока.\nБлагoдарим за игру!')
                        sys.exit()
                    elif find_num_in_card is False and interim_choice == 0:
                        print(f'\nИгрок {players[i].name} проиграл!'
                              f'\nЗначение {keg_choice.keg_choice[0]} отсутствует в карточке игрока.\nБлагoдарим за игру!')
                        sys.exit()

                players[i].card.card_correction(keg_choice.keg_choice[0], players[i].card.card_rows_all)

                if players[i].card.threshold_check():
                    print(f'\nПобедил игрок {players[i].name}!\nБлагoдарим за игру!')
                    sys.exit()


if __name__ == "__main__":
    game = Game()
    players_list = Game.player_list_fill()
    players = PlayersList(players_list).show_the_player
    game.game_play()



