# Дана последовательность чисел длиной N (N > 0)
# Найти максимальное число последовательность и вывести

a = int(input())
b = int(input())
 
if a > b:
    max1 = a
    max2 = b
else:
    max2 = a
    max1 = b
for i in range(3):
    elem = int(input())
    if elem > max1:
      max2 = max1
      max1 = elem
    elif elem > max2:
      max2 = elem
print(max1,max2)
