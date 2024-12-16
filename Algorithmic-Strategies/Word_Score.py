def word_score(str):
    str_splits = str.split(" ")
    words = check_char(str_splits)
    return max_score(words)

def check_char(str_split): 
    sum_of_ascii = 0
    words_store = {}
    for word in str_split:
        for ch in word:
            if ord(ch) >= 97 and ord(ch) <= 122:
                sum_of_ascii+=ord(ch)-96   
        words_store[word]= sum_of_ascii
        sum_of_ascii = 0
    return words_store

def max_score(words):
    highest_score = 0
    save_word = ""
    for max_score in words:
        if words[max_score] > highest_score:
            save_word = max_score
            highest_score = words[max_score]

    return [save_word, highest_score]

print("Highest scoring word: ", word_score("This is A string we will test"))