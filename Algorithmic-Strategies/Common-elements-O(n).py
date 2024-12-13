set1 = [1,2,3,3,4,5,3]
arr2 = [4,5,3,2,2,3]

result = []

for i in arr2:
    if i in  set1:
        result.append(i)
        set1.remove(i)

print(result)