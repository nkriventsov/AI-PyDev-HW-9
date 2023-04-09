import random
import itertools

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
В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается случайная карточка.

Каждый ход выбирается один случайный бочонок и выводится на экран. 
Также выводятся карточка игрока и карточка компьютера.

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


# Создаём класс Игрок
class Player:
    # player_count = itertools.count(1, 1)
    # Инициализация объекта класса
    def __init__(self, number, player_type, name):
        self.number = number                # next(Player.player_count)
        self.player_type = player_type      # self.player_type()
        self.name = name                    # self.player_name()


# Создаём класс Карточка
class Card:
    # Инициализация объекта класса
    def __init__(self, owner):
        self.owner = owner

    def draw_card(self):
        # Генерация чисел на новой карточке
        new_card_draw = random.sample(range(1, 91), k=15)

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
            empty_indices = set(random.sample(indices, 4))
            card_rows_all[counter] = ['' if i in empty_indices else next(iterable_list) for i in indices]
            counter += 1

        return card_rows_all

    def card_correction(self, keg_number, card_rows_all):

        i = 0
        for x in card_rows_all:
            for y in x:
                if x[i] is keg_number:
                    x[i] = '-'
                if i == len(x)-1:
                    i = 0
                else:
                    i += 1

        return card_rows_all

    # Вывод карточки на экран
    def card_presentation(self, card_rows_all):
        # Расчитываем количество тире для верхнего колонтитула карточки с учётом отображения имени игрока в центре
        dash_multiplier = (26 - len(self.owner)) // 2
        # Высчитываем длину верхнего колонтитула с именем игрока по центру
        upper_line_len = len('-' * dash_multiplier + self.owner + '-' * dash_multiplier)
        # Выводим на экран верхний колонтитул
        print('-' * dash_multiplier + self.owner + '-' * (dash_multiplier + (26 - upper_line_len)))
        print('{:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2}'.format(
            card_rows_all[0][0],
            card_rows_all[0][1],
            card_rows_all[0][2],
            card_rows_all[0][3],
            card_rows_all[0][4],
            card_rows_all[0][5],
            card_rows_all[0][6],
            card_rows_all[0][7],
            card_rows_all[0][8]))
        print('{:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2}'.format(
            card_rows_all[1][0],
            card_rows_all[1][1],
            card_rows_all[1][2],
            card_rows_all[1][3],
            card_rows_all[1][4],
            card_rows_all[1][5],
            card_rows_all[1][6],
            card_rows_all[1][7],
            card_rows_all[1][8]))
        print('{:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2}'.format(
            card_rows_all[2][0],
            card_rows_all[2][1],
            card_rows_all[2][2],
            card_rows_all[2][3],
            card_rows_all[2][4],
            card_rows_all[2][5],
            card_rows_all[2][6],
            card_rows_all[2][7],
            card_rows_all[2][8]))
        print('-' * 26)


if __name__ == "__main__":
    player_Ivan = Player(1, 'Человек', 'Иван')
    # print(player_Ivan.number)
    # print(player_Ivan.type)
    # print(player_Ivan.name)
    #
    player_Sam = Player(2, 'Человек', 'Sam')
    # print(player_Sam.number)
    # print(player_Sam.type)
    # print(player_Sam.name)

    test_card = Card('Наталья')
    card_rows_all = test_card.draw_card()
    test_card.card_presentation(card_rows_all)
    card_rows_all = test_card.card_correction(range(1, 50), card_rows_all)
    test_card.card_presentation(card_rows_all)



