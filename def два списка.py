# функция, которая создает два список и потом генерирует их в один список
a, b = int(input("Укажите длину 1 списка ")), int(input("Укажите максимально возможное значение элемента 1 списка "))
c, d = int(input("Укажите длину 2 списка ")), int(input("Укажите максимально возможное значение элемента 2 списка "))
import random
def my_function():
    print(list(ab) + list(cd))
ab = (random.choices(range(b), k=a))
cd = (random.choices(range(d), k=c))
my_function()