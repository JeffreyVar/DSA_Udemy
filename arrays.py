from array import array

arr = array('i', [1, 2, 3, 4, 5])

print(arr[0])  #Output: 1
print(arr[2])  #Output: 3

arr2 = array('i', [1, 2, 3])
arr.append(4)  # Adds 4 to the end
arr.extend([5, 6])  # Adds 5 and 6 to the end
arr.pop()  # Removes the last element, 6 in this case

# Using a for loop
for element in arr:
        print(element)

# Using while loop
counter = 0
condition = True
while condition:
    print(arr[counter])
    counter += 1
    if counter >= len(arr):
        condition = False