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

###################################################################

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

###################################################################

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

print("      Task 9     ")
print(daily_temperature_analysis([73,74,75,71,69,72,76,73]))
print(daily_temperature_analysis([30,40,50,60]))
print(daily_temperature_analysis([60,50,40]))
print(daily_temperature_analysis([30]))
print("\n")
###################################################################

"""
Task 5: Ticket Counter Simulation
    ● Problem: Simulate serving customers at a ticket counter.
    ● Input: ["Alice", "Bob", "Charlie"]
    ● Output: ["Alice", "Bob", "Charlie"]
    ● Examples:
        ○ Input: ["John", "Doe"] → Output: ["John", "Doe"]
        ○ Input: [] → Output: []
        ○ Input: ["OnlyOne"] → Output: ["OnlyOne"]
"""
from collections import deque

def ticket_counter_simulation(customers):
    
    queue = deque(customers) 
    served = []  

    while queue:
        current_customer = queue.popleft()
        served.append(current_customer) 

    return served

print("      Task 5     ")
print(ticket_counter_simulation(["Alice", "Bob", "Charlie"]))  # Output: ["Alice", "Bob", "Charlie"]
print(ticket_counter_simulation(["John", "Doe"]))  # Output: ["John", "Doe"]
print(ticket_counter_simulation([]))  # Output: []
print(ticket_counter_simulation(["OnlyOne"]))  # Output: ["OnlyOne"]
print("\n")
###################################################################
"""
Task 6: Family Tree Search
    ● Problem: Search for a name in a family tree.
    ● Input: Tree rooted at A
"""

class FamilyTreeNode:
    def __init__(self,name):
        self.name = name
        self.children = [] 

def family_tree_search(root,wanted_name):
    if not root:
        return False
    
    if root.name == wanted_name:
        return True

    for child in root.children:
        if family_tree_search(child,wanted_name):
            return True
    
    return False

root = FamilyTreeNode("A")
child1 = FamilyTreeNode("B")
child2 = FamilyTreeNode("C")
child3 = FamilyTreeNode("D")
root.children.extend([child1,child2,child3])

child1.children.append(FamilyTreeNode("E"))
child1.children.append(FamilyTreeNode("F"))
child2.children.append(FamilyTreeNode("G"))
child3.children.append(FamilyTreeNode("H"))

print("      Task 6     ")
print(family_tree_search(root, "E"))
print(family_tree_search(root,"X"))
print("\n")
###################################################################
"""
Task 7: Directory Size Calculation
    Problem: Sum file sizes in a directory tree.
    Input: Tree:
    Root (10)
    ├── Sub1 (5)
    ├── Sub2 (15)
        ├── File1 (10)
        ├── File2 (5)
    Output: 45
    Examples:
        ● Add File (20) under Sub2 → Output: 65
        ● Remove File1 → Output: 35
"""

class DirectoryNode:
    def __init__(self,name,size=0):
        self.name = name
        self.size=size
        self.children = []

def calculate_directory_size(node):
    if not node:
        return 0

    total_size = node.size
    for child in node.children:
        total_size += calculate_directory_size(child)
    return total_size

root = DirectoryNode("Root", 10)
sub1= DirectoryNode("Sub1", 5)
sub2 = DirectoryNode("Sub2", 15)
file1 = DirectoryNode("File1", 10)
file2 = DirectoryNode("File2", 5)

root.children.append(sub1)
root.children.append(sub2)
root.children.append(file1)
root.children.append(file2)

print("      Task 6     ")
print("Total size:", calculate_directory_size(root)) 

newFile = DirectoryNode("File3", 20)
sub2.children.append(newFile)

print("Total size after adding File3:", calculate_directory_size(root))

root.children = [child for child in root.children if child.name != "File1"]

print("Total size after removing File1:", calculate_directory_size(root)) 
print("\n")
###################################################################
"""
Task 13: Check Tree Symmetry
    ● Problem: Determine if a tree is symmetric.
    Input:
         1
        / \
        2 2
        / \
        3 3
    ● Output: true
    ● Examples:
        ○ Symmetric: [[1], [2, 2]] → true
        ○ Asymmetric: [[1], [2, null]] → false
"""

###################################################################