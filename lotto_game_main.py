from lotto_game import Player, Card
import random
import sys

NUMBER_OF_PLAYERS = 0

while NUMBER_OF_PLAYERS < 1:
    try:
        NUMBER_OF_PLAYERS = int(input('Введите количество игроков: '))
        if NUMBER_OF_PLAYERS < 1:
            raise ValueError
    except ValueError:
        print('Введено некорректное значение!')


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


players_dict = {}
comp_type_counter = 0
for i in range(NUMBER_OF_PLAYERS):
    interim_type = (player_type())
    if interim_type == 'Компьютер':
        comp_type_counter += 1
        players_dict[i+1] = (interim_type, player_name(interim_type, comp_type_counter))
    else:
        players_dict[i+1] = (interim_type, player_name(interim_type, None))

# Создаём чистые списки игроков и карточек
players_list = []
cards_list = []
# Список логических значений достиг ли игрок порога совпадений или нет
threshold = []

# Через цикл создаём указанное количество игроков и генерируем карточки
for i in range(NUMBER_OF_PLAYERS):
    players_list.append(Player(i, players_dict.get(i+1)[0], players_dict.get(i+1)[1]))
    cards_list.append(list([Card(players_dict.get(i + 1)[1]),
                            Card(players_dict.get(i + 1)[1]).draw_card(),
                            players_dict.get(i+1)[0]]))
    cards_list[i].append((cards_list[i][1][0].count('-') +
                          cards_list[i][1][1].count('-') +
                          cards_list[i][1][2].count('-')))
    cards_list[i].append(None)
    cards_list[i].append(None)
    threshold.append(True if cards_list[i][3] == 15 else False)


# start = input('\n\nНажмите Enter клавишу, чтобы начать!\n\n')
#
# if start is not None:

# Генериреум лист возможных значений для бочонков
keg_numbers_list = list(range(1, 91))

# Счетчик хода
roll_counter = 1

while not any(threshold):

    # Выводим на экран карточки игроков
    for i in range(NUMBER_OF_PLAYERS):
        cards_list[i][0].card_presentation(cards_list[i][1])

    # Выбираем случайный бочонок из листа
    keg_choice = random.sample(keg_numbers_list, 1)

    # Отображаем на экране значение выпавшего бочонка для игроков
    print(f'\nХод - {roll_counter}. Выпал бочонок со значением: {keg_choice[0]}')

    # Увеличиваем счетчик хода
    roll_counter += 1

    # Исключаем выпавшее значение из списка
    keg_numbers_list.remove(keg_choice[0])

    # Ищем выпавшее число в карточках игроков
    find_keg = None

    for i in range(NUMBER_OF_PLAYERS):
        cards_list[i][4] = any(keg_choice[0] in sublist for sublist in cards_list[i][1])

        # Проверяем человек или компьютер
        if cards_list[i][2] == 'Человек':

            # Пользователю предлагается зачеркнуть цифру на карточке или продолжить
            check_or_continue = None
            while check_or_continue != 0 and check_or_continue != 1:
                try:
                    check_or_continue = int(input('\nВыбор: зачеркнуть цифру на карточке - 0 или продолжить - 1? '))
                    if check_or_continue != 0 and check_or_continue != 1:
                        raise ValueError
                except ValueError:
                    print('Введено некорректное значение!')
            cards_list[i][5] = check_or_continue

            # Проверяем, отображаем и выходим из игры в случае некорректного выбора игрока
            if cards_list[i][4] and cards_list[i][5] == 1:
                print(f'\nИгрок {cards_list[i][0].owner} проиграл!'
                      f'\nЗначение {keg_choice[0]} есть в карточке игрока.\nБлагoдарим за игру!')
                sys.exit()
            elif cards_list[i][4] is False and cards_list[i][5] == 0:
                print(f'\nИгрок {cards_list[i][0].owner} проиграл!'
                      f'\nЗначение {keg_choice[0]} отсутствует в карточке игрока.\nБлагoдарим за игру!')
                sys.exit()

        # Перезаписываем данные карточки с вычеркнутими совпадениями
        cards_list[i][1] = Card(players_dict.get(i + 1)[1]).card_correction(keg_choice[0], cards_list[i][1])
        # Перезаписываем текущее значение вычеркнутых совпадений
        cards_list[i][3] = (cards_list[i][1][0].count('-') +
                            cards_list[i][1][1].count('-') +
                            cards_list[i][1][2].count('-'))
        # Перезаписываем список логических значений достиг ли игрок порога совпадений или нет
        threshold[i] = True if cards_list[i][3] == 15 else False

print(f'\nПобедил игрок {cards_list[threshold.index(True)][0].owner}!\nБлагoдарим за игру!')




