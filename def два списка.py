# функция, которая создает два список и потом генерирует их в один список
a, b = int(input("Укажите длину списка 1 ")), int(input("Укажите максимально возможное значение элемента списка 1 "))
c, d = int(input("Укажите длину списка 2 ")), int(input("Укажите максимально возможное значение элемента списка 2 "))
import random
def my_function():
    print(list(ab) + list(cd))
ab = (random.choices(range(b), k=a))
cd = (random.choices(range(d), k=c))
my_function()