#"jawad makhoul" => "jawadMakhoul"
#"" => ""
#"Jawad makhoul" => "jawadMakhoul"
#"1jawadma" => "jawadMa"
#"1 jawad" => "jawad"
#"111" => ""

def camelCase(str):
    if str == "":
        return "Empty string!"
    
    words = str.split()
    result = words[0].lower()
    for word in words[1:]:
        result += word.title()
        
    return result

input = input('Enter a string: ')
print(camelCase(input))