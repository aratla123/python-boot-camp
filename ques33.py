a=int(input("enter first number:"))  
b=int(input("enter first number:"))
while(b!=0):        
 a,b=(b,a%b)
 print("GCD of two numbers is:",a)
 LCM=a*b//(a,b)
print(LCM)