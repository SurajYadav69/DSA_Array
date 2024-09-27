#maximum_and_minimum_element_in_an_array.py

array = [2, 4, 8, 45, 78, 45, 4545, 1, 0]
max = array[0]
min = array[0]
for i in range(len(array)):
    if array[i] > max:
        max = array[i]
        
for i in range(len(array)):
    if array[i] < min:
        min = array[i]
    
print("maximum element:", max)
print("minimum element:", min)