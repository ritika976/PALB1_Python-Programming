arr = [1, 4, 3, 5, 8, 6]

minimum = arr[0]
maximum = arr[0]

for i in arr:
    if i < minimum:
        minimum = i
    if i > maximum:
        maximum = i

print("Minimum element in the array is:", minimum)
print("Maximum element in the array is:", maximum)
