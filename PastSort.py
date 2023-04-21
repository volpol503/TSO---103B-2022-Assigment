import time
# Сортировка вставками
start_time = time.time()

def insertion_sort(list1): 
 
        # Outer loop to traverse through 1 to len(list1) 
        for i in range(1, len(list1)): 
 
            value = list1[i] 
 
            # Move elements of list1[0..i-1], that are 
            # greater than value, to one position ahead 
            # of their current position 
            j = i - 1 
            while j >= 0 and value < list1[j]: 
                list1[j + 1] = list1[j] 
                j -= 1 
            list1[j + 1] = value 
        return list1 
            # Driver code to test above 
 
N = 2000
list1 = []
for i in range(N):
    list1.append(N - i)
print(list1) 
print("The unsorted list is:", list1) 
 
print("The sorted list1 is:", insertion_sort(list1)) 

end_time = time.time()
total_time = end_time - start_time
print("Время выполнения алгоритма сортировки: ", total_time)
