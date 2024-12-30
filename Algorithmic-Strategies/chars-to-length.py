def chars_to_length(input_str):
    finalString = ""
    char_counter = 1

    for i in range(len(input_str)):
        if i == len(input_str) - 1 or input_str[i] != input_str[i + 1]:
            finalString += input_str[i] + str(char_counter)
            char_counter = 1
        else:
            char_counter += 1 
    
    return finalString

def first_odd_counter(input_str):
    
    for i in range(0, len(input_str) -1, 2):
        char = input_str[i]
        num = int(input_str[i+1])

        if num % 2 != 0:
            return char
        
        return None



user_input = input("Enter a String: ")
chars_to_length_result = chars_to_length(user_input)
print(chars_to_length_result)
print("First odd counter is: " ,first_odd_counter(chars_to_length_result))