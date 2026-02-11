def kthSmallest(arr, k):
    arr.sort()
    return arr[k-1]

arr = [11, 56, 14, 31, 8, 26, 21, 33, 54, 10]
k = 5
print(kthSmallest(arr, k))
