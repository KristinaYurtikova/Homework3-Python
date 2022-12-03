#Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#Пример:
#- [2, 3, 4, 5, 6] => [12, 15, 16];
#- [2, 3, 5, 6] => [12, 15]

from random import randint

QUANTITY = 8
random_list = [randint(1,20) for i in range(QUANTITY)]
print(random_list)

result_list = [random_list[i] * random_list[-i - 1] for i in range(QUANTITY // 2)]
print(result_list)