amountOfRocks = int(input('Введите количество камней: '))
whoFirst = int(input('Введите, кто будет первее ходить? ПК или Вы. ПК / Я: '))
remainRocks = amountOfRocks
finalRocks = 1


while finalRocks < remainRocks:
    takeRocks = int(input(f'Сколько возьмете камней из {remainRocks}? 1 - 3'))
    remainRocks -= takeRocks
    
