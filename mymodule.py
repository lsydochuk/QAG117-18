import random
def my_function():
    print(list(x))
a = int(input("Укажите длину списка "))
b = int(input("Укажите максимально возможное значение элемента списка "))
x = (random.choices(range(b), k=a))

def greeting(name):
    print("Привет, " + name)