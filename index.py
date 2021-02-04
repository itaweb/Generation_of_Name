import sys
import random
print('Добро пожаловать в генератор забавных имён!\n')
print('Например, вот забавное имя для твоего друга: \n\n')

first = ('Чайник', 'Кипятильник', 'Рубильник',
         'Пылесос', 'Пуховик', 'Клоун', 'Пёс', 'Пудель')

last = ('Мохнорылый', 'Толстожопый', 'Не приятный', 'Плохопахнущий', 'Кучерявый',
        'Отмороженный', 'Облезлый', 'Завистливый')

while True:

    firstName = random.choice(first)
    lastName = random.choice(last)

    print('\n\n')

    print('{} {}'.format(firstName, lastName), file=sys.stderr)

    try_again = input(
        '\n\nХотите попробовать ещё? (Нажмите Enter если ДА, и нажмите - n - если хотите выйти...)\n')
    if try_again.lower() == 'n':
        break

input("\n Нажмите Enter для завершения работы.")
