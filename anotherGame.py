n = 10
m = 3
n = int(input("Введите кол-во камней: "))
m = int(input("Максимальное кол-во за ход: "))
while n > m:
    a = n%(m+1)
    n-= a
    print("Я взял ", a," камней")
    print("осталось ", n, " камней, Ваш ход")
    a = int(input("Какое количество вы возьмете? "))
    while (a<1)or(a>m):
        a = int(input("Вы ввели недопустимое значение, попробуйте еще раз: "))
    n -= a
    print("Вы взяли: ", a, " камней")
    print("осталось ", n, " камней")
    
if n == m+1:
    print("Я забираю 3 камня, вам остается 1, Вы выиграли")
else:
    print("Я забираю последние ",n," камней, Вы проиграли!")

