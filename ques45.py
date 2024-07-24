# remove all the capital letters from the string

inp=str(input())
for i in inp:
    if(ord(i)>=65 and ord(i)<=90):
         print((i))