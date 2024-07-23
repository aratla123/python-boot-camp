import math
n=int(input())
c=int(math.sqrt(n))
for  i in range(2,c+1):
 if(n<=1):
  print("neither prime nor composite")
 if(n%i!=0):
      print(" prime number")
 else:
      print("composite number")
