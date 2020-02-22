def gcd(num1, num2):
  if num1 >= num2:
    big = num1
    small = num2
  else:
    big = num2
    small = num1
  
  r = big % small

  if r == 0 :
    return small

  return gcd(small, r)

  
print(gcd(256,24))