#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

def FibonacciOf(n):
    if n in {0, 1}:  
        return n
    return FibonacciOf(n - 1) + FibonacciOf(n - 2)  

def NegaFibonacciOf(n):
    if n == -1:
        return 1
    elif n == -2:
        return -1
    return NegaFibonacciOf(n + 2) - NegaFibonacciOf(n + 1)

user_input = int(input('Determine the number of elements Fibonacci: ')) 
print([NegaFibonacciOf(n) for n in range(-user_input,0)] + [FibonacciOf(n) for n in range(user_input)])