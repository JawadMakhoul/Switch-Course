str = "zAdaeioou"

VOWELS = ['A','E','I','O','U','a','e','i','o','u']
VowelsCount = 0 
ConstCount = 0
for c in str:
    if c in VOWELS:
            VowelsCount+=1
    
ConstCount = len(str) - VowelsCount
print("Vowels: ",VowelsCount)
print("Consonants: ", ConstCount)