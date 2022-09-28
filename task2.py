# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

def Factor(n):
    list = []
    a = 2
    while a * a <= n:
        if n % a == 0:
            list.append(a)
            n //= a
        else:
            a += 1
    if a > 1:
        list.append(n)
    return(list)

number = int(input('Введите натуральное число => '))
print(f'простые множители числа {number}: {Factor(number)}')

