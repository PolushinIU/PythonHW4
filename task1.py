# Вычислить число c заданной точностью d

n = int(input('Введите нужную точночть числа Пи => '))
s = 1
pi = 0
for s in range(1, 1000000):
    pi = pi+4*((-1)**(s+1))/(2*s-1)
print(round(pi, n))