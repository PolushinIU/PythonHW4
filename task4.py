# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

from random import randint
k = int(input('Введите степень k => '))
factor = []
for i in range(1, k +2):
    factor.append(randint(1, 101))

result = []
for i in range(len(factor)):
    if k == 1:
        result.append(f'{factor[i]}*x')
    elif k == 0:
        result.append(f'{factor[i]}')
    else:
        result.append(f'{factor[i]}*x^{k}')
    signs = randint(0, 1)
    if signs == 1:
        result.append('+')
    elif signs == 0:
        result.append('-')
    k -= 1

result.pop(-1)
result.append('=0')
record = open('data.txt', 'w')
record.write(''.join(result))
record.close()






#from random import randint
# import numbers
# import random as r

# def formFunk(num, some_str):
#     if num == 1:
#         a = r.randint(0, 100)
#         b = r.randint(0, 100)
#         if a == 1 and b > 0:
#             some_str += 'x'
#         if a == 0:
#             some_str += str(b)
#         if a > 1:
#             some_str += str(a) + 'x+' + str(b)
#         if a == 0 and b == 0:
#             return some_str
#         return some_str
#     else:
#         a = r.randint(0, 100)
#         if a == 1:
#             some_str += 'x' + '^' + str(num) + '+' + formFunk(num-1, some_str)
#         if a == 0:
#             some_str += formFunk(num-1, some_str)
#         if a > 1:
#             some_str += str(a) + 'x' + '^' + str(num) + \
#                 '+' + formFunk(num-1, some_str)
#         return some_str

# some_str = ''
# number = int(input('введите степень => '))
# print(formFunk(number, some_str) + ' = 0')


