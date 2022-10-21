# Напишите программу, которая принимает на вход число N и выдает набор произведений
# чисел от 1 до N.

input_num = int(input('Введите число: --> '))
list = [1]

for i in range (1, input_num):
    list.append ((i+1) * list [i-1])

print(f'Произведение чисел: {list}')