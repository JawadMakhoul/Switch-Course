# Task 1
def recent_calls(calls, k): # Recent Call Logs
    return calls[-k:] if k > 0 else []

print(recent_calls([1001,1002,1003,1004], 3))
print(recent_calls([1,2], 3))
print(recent_calls([1, 2,3,4,5], 2))
print(recent_calls([],5))

################################################################

# Task 2
def inventory_shelf_arrangement(shelfList):

    newList=[]
    stack = []
    for cell in shelfList:
        stack.append(cell)

    while stack:
        newList.append(stack.pop())
    
    return newList

print(inventory_shelf_arrangement([101,102,103,104]))