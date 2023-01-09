lst = []
c = int(input())
while c != 0:
 lst.append(c)
 c = int(input())
print(lst)
maxi = 0
# max(lst)
for i in range(len(lst)):
  if lst[i]>maxi:
   maxi = lst[i]
print(maxi)