import math
a = int(input())
b = int(input())
c = int(input())
p = 0.5*(a+b+c)
print(math.sqrt(p*(p-a)*(p-b)*(p-c)))