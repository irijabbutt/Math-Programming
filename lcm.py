# LCM of two numbers
def gcd(x, y):
   while y:
    x, y = y, x % y
   return x
def lcm(x, y):
 return x * y // gcd(x, y)
num1 = 12
num2 = 15
print("LCM of", num1, "and", num2, "is:", lcm(num1, num2))