arr = [1, 4, 3, 2, 6, 5]
print("Array before reversing:",arr)

start = 0
end = len(arr) - 1

while start < end:
    arr[start], arr[end] = arr[end], arr[start]
    start += 1
    end -= 1

print("Reversed array:", arr)
