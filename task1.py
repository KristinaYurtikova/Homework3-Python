#1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#Пример:
#- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

quantity = 5
user_input = [int(input('Enter a number: ')) for i in range(quantity)]
print(user_input)

sum = 0
for i in range(1, len(user_input), 2):
    sum += user_input[i]
print(f'Sum of elements at odd positions is {sum}')


   


