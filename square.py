# calculate square of a number without using multiplication operator (*)
def square(num): 
    result = 0
    for _ in range(abs(num)):
        result += abs(num)

    if num < 0:
        return -result

    else:

        return result

number = 5
print("Square of", number, "is:", square(number))