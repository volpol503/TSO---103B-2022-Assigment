arr = [15,5,2,3,12,20,23]

def find_smallest(arr):
  smallest = arr [0]
  sm_ind = 0
  for i in range(1,len(arr)):
    if arr[i] < smallest:
      smallest = arr[i]
      sm_ind = i
  return sm_ind

def selection_sort(arr):
  arr_new = []
  for i in range (len(arr)):
   s_ind = find_smallest(arr)
   arr_new.append(arr.pop(s_ind))
  return arr_new
    
print(find_smallest(arr))
print(selection_sort(arr))
