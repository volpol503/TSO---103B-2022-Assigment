list = []
print(*list)

b = int(input())
res = 0
for i in range(b):
 c = int(input())
 list.append(c)
 if c == 4:
  res += 1
print('[',*list ,']', res)
