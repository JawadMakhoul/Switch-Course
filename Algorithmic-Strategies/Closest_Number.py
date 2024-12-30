def closest_number(given_number):
    subtractResult  = 1000
    closest_number = 1000
    array = [0,1,4,8,9,10,30,45,77,90]

    for num in array:
        if num < given_number:
            if given_number - num < subtractResult:
                subtractResult = given_number - num
                closest_number = num

        elif num > given_number and num - given_number < subtractResult:
            subtractResult = num - given_number
            closest_number = num


    return closest_number

num = input('Enter a number: ')
print(closest_number(int(num)))