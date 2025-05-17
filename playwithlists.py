L = [4, 5, 1, 2, 9, 7, 10, 8]
print("Original List:", L)

# Variable to store the sum of the list
count = 0

# Finding the sum
for i in L:
    count += i

# Divide the total elements by number of elements
avg = count / len(L)

print("sum = ", count)
print("average = ", avg)

# Sorting the elements of the list
L.sort()

#printing the first element
print("smallest element is:",L[0])

#printing the last element
print("largest element is:", L[-1])
