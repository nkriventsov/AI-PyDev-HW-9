from lotto_game import Player, Card
import random
import sys

global NUMBER_OF_PLAYERS


def number_of_players():

    NUMBER_OF_PLAYERS = 0

    while NUMBER_OF_PLAYERS < 1:
        try:
            NUMBER_OF_PLAYERS = int(input('Введите количество игроков: '))
            if NUMBER_OF_PLAYERS < 1:
                raise ValueError
        except ValueError:
            print('Введено некорректное значение!')

    return NUMBER_OF_PLAYERS


def player_type():
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


def player_name(player_type_result, comp_type_counter):
    if player_type_result == 'Компьютер':
        player_name_choice = f'{player_type_result}_{comp_type_counter}'
    else:
        player_name_choice = input('Введите имя игрока: ')
    return player_name_choice


def player_registration(number_of_players):

    players_dict = {}
    comp_type_counter = 0

    '''
    Структура словаря players_dict:
    ключ        - порядковый номер игрока
    значение    - кортеж:
                        - Тип игрока
                        - Имя игрока
    '''
    for i in range(number_of_players):
        interim_type = player_type()
        if interim_type == 'Компьютер':
            comp_type_counter += 1
            players_dict[i+1] = (interim_type, player_name(interim_type, comp_type_counter))
        else:
            players_dict[i+1] = (interim_type, player_name(interim_type, None))

    return players_dict


def players_generation(players_dict, number_of_players):
    # Создаём чистые списки игроков
    players_list = []
    # Через цикл создаём указанное количество игроков
    for i in range(number_of_players):
        players_list.append(Player(i, players_dict.get(i + 1)[0], players_dict.get(i + 1)[1]))

    return players_list


def cards_generation(players_dict, number_of_players):
    # Создаём чистые списки карточек
    cards_list = []
    # Через цикл генерируем указанное количество карточек и записываем в список
    # Размерность списка: количество игроков на 6
    for i in range(number_of_players):
        '''
        Поля списка по одной карточке:
        1 - Инстанцирование карточки
        2 - Генерация значений/чисел карточки
        3 - Тип игрока
        4 - Количество вычеркиваний '-' в карточке
        5 - Совпало(True) или нет(False) значение выпавшего бочонка с текущими значениями карточки
        6 - Выбор игрока: зачеркнуть цифру на карточке или продолжить   
        '''
        # Первые три элемента в листе:
        cards_list.append(list([Card(players_dict.get(i + 1)[1]),
                                Card(players_dict.get(i + 1)[1]).draw_card(),
                                players_dict.get(i+1)[0]]))
        cards_list[i].append((cards_list[i][1][0].count('-') +
                              cards_list[i][1][1].count('-') +
                              cards_list[i][1][2].count('-')))
        cards_list[i].append(None)
        cards_list[i].append(None)

    return cards_list

def threshold_generation(cards_list, number_of_players):
    # Список логических значений достиг ли игрок порога совпадений или нет
    threshold = []
    for i in range(number_of_players):
        threshold.append(True if cards_list[i][3] == 15 else False)

    return threshold


# start = input('\n\nНажмите Enter клавишу, чтобы начать!\n\n')
#
# if start is not None:

# Генериреум лист возможных значений для бочонков
def keg_roll_out():
    keg_numbers_list = list(range(1, 91))
    return keg_numbers_list


def cards_to_screen(cards_list, number_of_players):
    # Выводим на экран карточки игроков
    for i in range(number_of_players):
        cards_list[i][0].card_presentation(cards_list[i][1])


def keg_choice_func(keg_numbers_list):
    # Выбираем случайный бочонок из листа
    keg_choice = random.sample(keg_numbers_list, 1)
    return keg_choice


def keg_to_screen(roll_counter, keg_choice):
    # Отображаем на экране значение выпавшего бочонка для игроков
    return print(f'\nХод - {roll_counter}. Выпал бочонок со значением: {keg_choice[0]}')


def keg_list_adj(keg_numbers_list, keg_choice):
    # Исключаем выпавшее значение из списка
    return keg_numbers_list.remove(keg_choice[0])


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


def game(*args, **kwargs):

    NUMBER_OF_PLAYERS = number_of_players()

    players_dict = player_registration(NUMBER_OF_PLAYERS)

    players_list = players_generation(players_dict, NUMBER_OF_PLAYERS)

    cards_list = cards_generation(players_dict, NUMBER_OF_PLAYERS)

    threshold = threshold_generation(cards_list, NUMBER_OF_PLAYERS)

    keg_numbers_list = keg_roll_out()

    # Счетчик хода
    roll_counter = 1

    while not any(threshold):

        cards_to_screen(cards_list, NUMBER_OF_PLAYERS)

        keg_choice = keg_choice_func(keg_numbers_list)

        keg_to_screen(roll_counter, keg_choice)

        # Увеличиваем счетчик хода
        roll_counter += 1

        keg_list_adj(keg_numbers_list, keg_choice)

        # Ищем выпавшее число в карточках игроков
        for i in range(NUMBER_OF_PLAYERS):
            cards_list[i][4] = any(keg_choice[0] in sublist for sublist in cards_list[i][1])

            # Проверяем человек или компьютер
            if cards_list[i][2] == 'Человек':

                cards_list[i][5] = check_continue_func()

                # Проверяем, отображаем и выходим из игры в случае некорректного выбора игрока
                if cards_list[i][4] and cards_list[i][5] == 1:
                    print(f'\nИгрок {cards_list[i][0].owner} проиграл!'
                          f'\nЗначение {keg_choice[0]} есть в карточке игрока.\nБлагoдарим за игру!')
                    sys.exit()
                elif cards_list[i][4] is False and cards_list[i][5] == 0:
                    print(f'\nИгрок {cards_list[i][0].owner} проиграл!'
                          f'\nЗначение {keg_choice[0]} отсутствует в карточке игрока.\nБлагoдарим за игру!')
                    sys.exit()

            # Перезаписываем данные карточки с вычеркнутыми совпадениями
            cards_list[i][1] = Card(players_dict.get(i + 1)[1]).card_correction(keg_choice[0], cards_list[i][1])
            # Перезаписываем текущее значение вычеркнутых совпадений
            cards_list[i][3] = (cards_list[i][1][0].count('-') +
                                cards_list[i][1][1].count('-') +
                                cards_list[i][1][2].count('-'))
            # Перезаписываем список логических значений достиг ли игрок порога совпадений или нет
            threshold[i] = True if cards_list[i][3] == 15 else False

    print(f'\nПобедил игрок {cards_list[threshold.index(True)][0].owner}!\nБлагoдарим за игру!')


if __name__ == "__main__":
    game()


