'''
Создать функцию, которая прибавляет элементы числа между собой.
Например, есть число 123. Попав в нашу функцию, должно произойти следующее:
1 + 2 + 3 = 6
Результат суммирования - в консоль.
'''
def sum_of_numbers():
    print(theSum)
num = str(input('Введите числа от 1 до 9: '))
numList = list(num)
theSum = 0
for i in numList:
    theSum += int(i)
sum_of_numbers()

