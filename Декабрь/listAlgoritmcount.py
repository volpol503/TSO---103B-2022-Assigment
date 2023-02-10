print('Hello, world!')
s = input()
ans_count = 0


for i in range(len(s)):
  new_count = 0
  for j in range(len(s)):
    if s[i] == s[j]:
      new_count += 1
  if new_count > ans_count:
    ans_count = new_count
print(ans_count)
