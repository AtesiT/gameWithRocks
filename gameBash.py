amountOfStones = 10
amountOfStonesInTheMove = 3
amountOfStones = int(input("Введите кол-во камней: "))
# amountOfStonesInTheMove = int(input("Максимальное кол-во за ход: "))
amountOfStonesInTheMove = 3
i = 0 


while amountOfStones > amountOfStonesInTheMove:
    a = amountOfStones%(amountOfStonesInTheMove+1)
    amountOfStonesInTheMove -= a
    if i != 0:
        print(f"ПК взял {a}")
    i+=1
    print(f"Oсталось {amountOfStones} камней, Ваш ход")
    a = int(input("Какое количество вы возьмете? "))
    amountOfStones -= a
    print(f"Вы взяли: {a}")
    print(f"Осталось {amountOfStones} камней")



if amountOfStones == amountOfStonesInTheMove + 1:
    print("ПК забирает 3 камня, вам остается 1, Вы выиграли")
else:
    print(f"ПК забираю последние {amountOfStones} камней, Вы проиграли!")
