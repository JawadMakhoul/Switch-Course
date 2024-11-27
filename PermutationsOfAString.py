def permutations(string):
    
    if len(string) == 0:
        return [""]
    elif len(string) == 1:
        return [string]
    
    
    result = []
    for i, char in enumerate(string):
        
        rest = string[:i] + string[i+1:]
       
        for perm in permutations(rest):
            result.append(char + perm)
    
    return result


print(permutations("abc"))
