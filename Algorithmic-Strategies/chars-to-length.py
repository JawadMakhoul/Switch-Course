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

user_input = input("Enter a String: ")
print(chars_to_length(user_input))