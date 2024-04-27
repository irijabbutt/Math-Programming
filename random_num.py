# generate random number within specified range
# using numpy
import random
def generate_random_number(start, end):
 return random.randint(start, end)
start = 1
end = 100
random_number = generate_random_number(start, end)
print("Random number between", start, "and", end, ":", random_number)