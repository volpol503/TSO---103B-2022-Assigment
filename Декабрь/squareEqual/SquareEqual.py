#Даны три целых числа A, B, C. Найти все корни уравнения
# ax^2 + bx + c = 0 и вывести их в порядке возрастания
import math

a, b ,c = map(int, input()split())
d = b ** 2 - 4 * a * c

if a == 0:
  if b != 0:
    print (-c/b)
  if b == 0 or == 0:
      print('Inf')
  else:
    d = b**2 - 4 *a *c
    if d == 0:
      x1 = -b/(2*a)
      print(x1)
    elif d > 0:
  x1 = (-b - math.sqrt(d))/(2*a)
  x2 = (-b + math.sqrt(d))/(2*a)
  if x1 < x2:
    print(x1,x2)
  else:
    print(x2,x1)
