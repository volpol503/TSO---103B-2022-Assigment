# Дана последовательность чисел длины N
# Найти последнее (левое вхождение) положительного числа x
# или вывести -1, если число X не встречалось

def find_x(str1,x):
  ans = -1
  for i in range (len(str1)):
    if str1[i] == str(x):
       ans = i
  return ans
s = '123411'
x = 1
print(find_x(s, x))
