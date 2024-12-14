str = "Algorithmic"
abc = []

for ch in str:
    abc.append(ord(ch))

abc.sort()

if len(abc) % 2 == 0:
    print("Median char is: ",chr(abc[int(len(abc)/2-1)]))

else: print("Median char is: ",chr(abc[int(len(abc)/2)]))
