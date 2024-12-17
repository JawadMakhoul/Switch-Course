def count_repeating_character(str):
    char_count = {}

    for char in str:
        print(char)
        if char in char_count:
            print(char)
            char_count[char]+=1
        
        else: char_count[char] = 1
    
    return find_first_non_repeating_character(str, char_count)

def find_first_non_repeating_character(str, char_count):
    for char in str:
        if char_count[char] == 1:
            return char
    return None

user_input = input("Enter a String: ")
print("First non repeating charcter is: ", count_repeating_character(user_input))