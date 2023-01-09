# В этом примере мы объявили список. С помощю числа которого мы вводим с клавиатуры следующие элементы добавляются в список и выводятся на экран


list = ['first', 'second',  'third',  'four',  'fifth']
print(*list)

b = int(input())

for i in range(b):
 c = input()
 list.append(c)
print(*list)
