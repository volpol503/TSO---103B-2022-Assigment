import time
# Пузырьковая сортировка
start_time = time.time()
from random import randint
 
N = 2000
a = []
for i in range(N):
    a.append(i + 1)
print(a)
 
 
for i in range(N-1):
    for j in range(N-i-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
 
print(a)
end_time = time.time()
total_time = end_time - start_time
print("Время выполнения алгоритма сортировки: ", total_time)
