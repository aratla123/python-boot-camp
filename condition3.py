n=int(input())
if(n%2==0 and n>0):
 print("number is even and positive")
elif(n%2==0 and n<0):
 print("nunber is even and negative")
elif(n%2!=0 and n>0):
 print("number is odd and positive")
elif(n%2!=0 and n<0):
 print("number is odd and negative")
else:
 print("0")