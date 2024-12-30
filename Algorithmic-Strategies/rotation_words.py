def is_rotation(word1, word2):
    if len(word1) != len(word2):
        return False
    
    word1 = word1 + word1
    if word2 in word1:
        return True

str1 = input('Enter first string: ')
str2 = input('Enter second string: ')
print(is_rotation(str1, str2))