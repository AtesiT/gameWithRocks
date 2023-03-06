amountOfStones = int(input("Введите кол-во камней: "))
AmountInMove = int(input("Максимальное кол-во за ход: "))

while amountOfStones > AmountInMove:
    a = amountOfStones%(AmountInMove+1)
    amountOfStones-= a
    print("Я взял ", a," камней")
    print("осталось ", amountOfStones, " камней, Ваш ход")
    a = int(input("Какое количество вы возьмете? "))
    while (a<1)or(a>AmountInMove):
        a = int(input("Вы ввели недопустимое значение, попробуйте еще раз: "))
    amountOfStones -= a
    print("Вы взяли: ", a, " камней")
    print("осталось ", amountOfStones, " камней")
    
if amountOfStones == 1:
    print("Я забираю 3 камня, вам остается 1, Вы выиграли")
else:
    print("Я забираю последние ", amountOfStones," камней, Вы проиграли!")

