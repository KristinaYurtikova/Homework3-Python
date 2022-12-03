#Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#Пример:
#- [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from random import random, randrange


QUANTITY = 10 
random_list = [random() * randrange(-10,10) for i in range(QUANTITY)]
print(["{:0.3f}".format(x) for x in random_list])

random_list1 = [round(i % 1, 2) for i in random_list if i % 1 != 0]
difference = max(random_list1) - min(random_list1)
print("{:0.3f}".format(difference))


