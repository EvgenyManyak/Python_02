# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

sum = 0
input_num = input('Введите число: --> ')

for a in input_num:
    if a.isdigit():
        sum += int(a)

print(sum)