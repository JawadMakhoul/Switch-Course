arr1 =[1,2,2,3,3]
arr2 = [2,2,3,3,8]
result = []

for i in arr1:
    for j in arr2:
        if i == j:
            result.append(i)

for i in range(len(result)-1):
    for j in range(1, len(result)):
        if i == j:
            result.pop(j)
            
print(result)

