

'''for i in range(1,5+1):
    for j in range(1,5+1):
     if(abs(i)+abs(j))==5:
        print(" ",end=" ")
     else:
       print( end="*")
    print()'''

row=int(input())
for i in range (1,row + 1):
  for j in range (1,row - i + 1):
     print (end=" ")
  for j in range (1,row + 1):
   print ("*",end=" ")
  print()