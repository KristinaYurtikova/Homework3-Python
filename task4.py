#Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#Пример:
#- 45 -> 101101
#- 3 -> 11
#- 2 -> 10


number_binary = ""
number = int(input('Enter a decimal number: '))
while number > 0:
    number_binary = str(number % 2) + number_binary
    number //= 2  
print(f'Binary number is {number_binary}')

