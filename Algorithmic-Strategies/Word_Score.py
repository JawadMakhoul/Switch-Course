str = "This is A string we will test"
str_splits = str.split(" ")
words_store = {}
sum_of_ascii = 0
highest_score = 0
save_word = ""
for word in str_splits:
    for ch in word:
        if ord(ch) >= 97 and ord(ch) <= 122:
            sum_of_ascii+=ord(ch)-96   
    words_store[word]= sum_of_ascii
    sum_of_ascii = 0

for max_score in words_store:
    if words_store[max_score] > highest_score:
        save_word = max_score
        highest_score = words_store[max_score]

print("Highest scoring word: ", save_word, highest_score)