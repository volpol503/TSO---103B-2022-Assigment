# Дана последовательность чисел длиной N (N > 0)
# Найти максимальное число последовательность и вывести

a = int(input())
maxi = a
for i in range(4):
  a = int(input())
  if a > maxi :
    maxi = a
print(maxi)
