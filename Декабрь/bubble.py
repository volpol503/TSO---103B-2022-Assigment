a = [6,12,4,3,8]
for i in range(len(a)):
  for ind in range(len(a)-1):
    if a[ind] > a[ind +1]:
      a[ind], a[ind + 1] = a[ind + 1], a[ind]
print(a)
