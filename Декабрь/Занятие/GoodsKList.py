c = input()
goods = []
while c != 'exit':
 goods.append(c)
 c = input()
k = int(input())
for i in range(0,k+1):
 print(goods[i])