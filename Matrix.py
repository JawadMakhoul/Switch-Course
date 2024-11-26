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
    stack = actions[:]  # Copy the list to a stack
    
    # Undo steps
    for _ in range(undo_steps):
        if stack:  # Check if the stack is not empty
            stack.pop()  # Remove lst action
        else:
            break  # Stop if no more actions to undo
    
    return stack

print("      Task 3     ")
print(undo_actions(["type A", "type B", "delete"], 1))  # Output: ["type A", "type B"]
print(undo_actions(["A", "B"], 1))  # Output: ["A"]
print(undo_actions(["X"], 2))  # Output: []
print(undo_actions([], 1))  # Output: []
print("\n")

"""
Task 4: Validate Parentheses in a Code Snippet
    ● Problem: Write a function to check if parentheses are balanced in a string.
    ● Input: "([{}])"
    ● Output: true
    ● Examples:
        ○ Input: "([])" → Output: true
        ○ Input: "([)]" → Output: false
        ○ Input: "" → Output: true
"""
def validate_parentheses(VPList):

    VPStack=[]

    for item in VPList:
        if item == '{' or item == '[' or item == '(':
            VPStack.append(item)
        
        elif item == '}' or item == ']' or item == ')':
           
            if not VPStack: # check if the stack is empty
                return False  

            
            top = VPStack[-1]
            if (top == '{' and item == '}') or (top == '[' and item == ']') or (top == '(' and item == ')'):
                VPStack.pop()

    if len(VPStack) == 0:
        return True
    return False
print("      Task 4     ")
print(validate_parentheses("([{}])"))
print(validate_parentheses("([])"))
print(validate_parentheses("([)]"))
print(validate_parentheses(""))
print("\n")

"""
Task 9: Daily Temperature Analysis
    ● Problem: For an array of daily temperatures, return the number of days until a
               warmer day for each day. If no warmer day exists, return 0.
    ● Input: [73, 74, 75, 71, 69, 72, 76, 73]
    ● Output: [1, 1, 4, 2, 1, 1, 0, 0]
    ● Examples:
        ○ Input: [30, 40, 50, 60] → Output: [1, 1, 1, 0]
        ○ Input: [60, 50, 40] → Output: [0, 0, 0]
        ○ Input: [30] → Output: [0]
"""

def daily_temperature_analysis(tempList):

    i=0
    j=1
    while i < len(tempList)-1:
        count=0
        j=i+1
        while j < len(tempList):   
            count+=1
            if(tempList[i]<tempList[j]):
                break
            
            
            j+=1
        if(j== len(tempList)):
                tempList[i]=0
        else: tempList[i]=count
        i+=1  
    tempList[len(tempList)-1]=0
    return tempList

print(daily_temperature_analysis([73,74,75,71,69,72,76,73]))
print(daily_temperature_analysis([30,40,50,60]))
print(daily_temperature_analysis([60,50,40]))
print(daily_temperature_analysis([30]))
print(daily_temperature_analysis([60,60,60]))