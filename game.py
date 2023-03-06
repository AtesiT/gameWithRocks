amountOfRocks = int(input('Введите количество камней: '))
# whoFirst = int(input('Введите, кто будет первее ходить? ПК или Вы. ПК / Я: '))
remainRocks = amountOfRocks
finalRocks = 1
move = 0



print('Первый ход начинаете вы')
while finalRocks < remainRocks:
    # Ход игрока
    takeRocks = int(input(f'Сколько возьмете камней из {remainRocks}? 1 - 3'))
    remainRocks -= takeRocks

    # Количество ходов и присваивание переменной move - чей ход
    print(f'Количество камней осталось после вашего хода: {remainRocks}')
    move = 1
    


    # Ход компьютера
    # if takeRocks == 1:
    #     continue
    # elif takeRocks == 2:
    #     continue
    # elif takeRocks == 3:
    #     continue
    

    # Количество ходов и присваивание переменной move - чей ход
    print(f'Количество камней осталось после хода компьютера: {remainRocks}')
    move = 2


if finalRocks <= 1 and move == 1:
    print('Вы выиграли')
elif finalRocks <= 1 and move == 2:
    print('Компьютер выиграл')
