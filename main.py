import random

def is_correct(answer):
    flag = False
    while flag is False:
        if answer == 'д':
            flag = True
            return True
        elif answer == 'н':
            flag = True
            return False
        else:
            print('Некорректный ответ!')
            answer = input('[д] - да, [н] - нет: ')


print('Привет!'
      'Это игра камень-ножницы-бумага. Правила ты знаешь.')
answer = input('Играем? [д] - да, [н] - нет: ')

comp_score = 0
player_score = 0
r_p_s = {1: 'камень',
         2: 'ножницы',
         3: 'бумага'}

while is_correct(answer):
    player = input('Камень...'
                   'Ножницы...'
                   'Бумага...'
                   '')
    while player not in r_p_s.values():
        print('Некорректный ответ!')
        player = input('Камень...'
                       'Ножницы...'
                       'Бумага...'
                       '')
    else:
        computer = r_p_s[random.randint(1, 3)]
        if computer == 'камень':
            if player == 'камень':
                print('Ничья!')
            elif player == 'ножницы':
                print('Я выйграл!')
                comp_score += 1
            elif player == 'бумага':
                print('Ты выйграл!')
                player_score += 1
        elif computer == 'ножницы':
            if player == 'камень':
                print('Ты выйграл!')
                player_score += 1
            elif player == 'ножницы':
                print('Ничья!')
            elif player == 'бумага':
                print('Я выйграл!')
                comp_score += 1
        elif computer == 'бумага':
            if player == 'камень':
                print('Я выйграл!')
                comp_score += 1
            elif player == 'ножницы':
                print('Ты выйграл!')
                player_score += 1
            elif player == 'бумага':
                print('Ничья!')
        print('Счёт:', player_score, ':', comp_score)
        answer = input('Сыграем ещё? [д] - да, [н] - нет: ')
        is_correct(answer)

else:
    print('Ну и ладно! Счёт', player_score, ':', comp_score)