a = [4, 9, 2, 7, 9, 2]
b = [9, 2, 7, 4, 6, 9]

union = []

# Traverse first array
for num in a:
    if num not in union:
        union.append(num)

# Traverse second array
for num in b:
    if num not in union:
        union.append(num)

print(union)
