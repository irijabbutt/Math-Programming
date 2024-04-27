# calculate power of number using recurrsion
def power(base, exponent):
  if exponent == 0:
     return 1
  elif exponent < 0:
     return 1 / power(base, -exponent)
  else:
     return base * power(base, exponent - 1)
base = 2
exponent = 3
print(base, "raised to the power of", exponent, "is:", power(base, exponent))