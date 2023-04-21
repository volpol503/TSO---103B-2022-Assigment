import time
# Быстрая сортировка
start_time = time.time()
from random import randint
 
N = 8000
nums = []
for i in range(N):
    nums.append(randint(1, N))
n = 1
while n < len(nums):
   for i in range(len(nums) - n):
       if nums[i] > nums[i + 1]:
           nums[i], nums[i + 1] = nums[i + 1], nums[i]
   n += 1

end_time = time.time()
total_time = end_time - start_time
print("Время выполнения алгоритма сортировки: ", total_time)
