"""
Task 1: Recent Call Logs
    ● Problem: Maintain a rolling log of k recent calls.
    ● Input:
        ○ Calls: [1001, 1002, 1003, 1004]
        ○ k: 3
    ● Output: [1002, 1003, 1004]
    ● Examples:
        ○ Input: Calls [1, 2], k=3 → Output: [1, 2]
    ○ Input: Calls [1, 2, 3, 4, 5], k=2 → Output: [4, 5]
    ○ Input: Calls [], k=5 → Output: [] 
"""
def recent_calls(calls, k): # Recent Call Logs
    return calls[-k:] if k > 0 else []

print("      Task 1     ")
print(recent_calls([1001,1002,1003,1004], 3))
print(recent_calls([1,2], 3))
print(recent_calls([1, 2,3,4,5], 2))
print(recent_calls([],5))
print("\n")
###################################################################


"""
Task 2: Inventory Shelf Arrangement
    ● Problem: You have a list of book IDs that are removed from a shelf in the order
               [101, 102, 103, 104]. Write a function to reverse their order using a suitable
               data structure.
    ● Input: [101, 102, 103, 104]
    ● Output: [104, 103, 102, 101]
    ● Examples:
        ○ Input: [1, 2, 3] → Output: [3, 2, 1]
        ○ Input: [] → Output: []
        ○ Input: [42] → Output: [42]
"""
def inventory_shelf_arrangement(shelfList):

    newList=[]
    stack = []
    for cell in shelfList:
        stack.append(cell)

    while stack:
        newList.append(stack.pop())
    
    return newList

print("      Task 2     ")
print(inventory_shelf_arrangement([101,102,103,104]))
print("\n")
###################################################################

"""
Task 3: Undo Feature in Text Editor
    ● Problem: Design an undo feature for a text editor. Given a series of actions (["type
        A", "type B", "delete"]), implement an undo operation for the last action.
    ● Input:
        ○ Actions: ["type A", "type B", "delete"]
        ○ Undo steps: 1
    ● Output: ["type A", "type B"]
    ● Examples:
        ○ Input: Actions ["A", "B"], Undo 1 → Output: ["A"]
        ○ Input: Actions ["X"], Undo 2 → Output: []
        ○ Input: Actions [], Undo 1 → Output: []
"""
def undo_actions(actions, undo_steps):
    stack = actions[:]  # Copy the list to mimic a stack
    
    # Undo steps
    for _ in range(undo_steps):
        if stack:  # Check if the stack is not empty
            stack.pop()  # Remove lst action
        else:
            break  # Stop if no more actions to undo
    
    return stack

# Test cases
print("      Task 3     ")
print(undo_actions(["type A", "type B", "delete"], 1))  # Output: ["type A", "type B"]
print(undo_actions(["A", "B"], 1))  # Output: ["A"]
print(undo_actions(["X"], 2))  # Output: []
print(undo_actions([], 1))  # Output: []
print("\n")