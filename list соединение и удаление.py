# вариант 1 создать 4 переменные и выполнить 4 математических операции
num1 = 25
num2 = 2
num3 = 84
num4 = 7
res1 = num1 + num2
res2 = num3 - num4
res3 = num2 * num4
res4 = num3 / num2
print(res1)
print(res2)
print(res3)
print(res4)
# вариант 2 создать 4 переменные и выполнить 4 математических операции
num = [2, 5, 45, 6]
print(num[0] + num[2])
print(num[2] / num[1])
print(num[0] * num[3])
print(num[3] + num[1])
# создать 2 текстовые переменные и их соединить
text1 = 'создать 2 переменные (текстовые) '
text2 = 'и их соединить'
text = text1 + text2
print(text)
# создать случайный список и удалить последний элемент
list1 = [5, 6, 7, 8, 9, 10]
list1 = list1[:-1] #1 способ
print(list1) 
list1.pop() #2 способ
print(list1)
# создать случайный генерируемый список из 10 символов и удалить последний символ
import random
RandomList = [random.randint(0, 100) for i in range(10)] #создан список из 10 случайно генерируемых чисел
print(RandomList)
del RandomList[-1] # удалить последний элемент с генерируемого списка
print(RandomList)