'''i/p:hello----------------wo----rld
o/p:-----------hello world'''

inp=input()
count=0
ans=""
for i in inp:
   if(i=="-"):
      count+=1
   else:
      ans=ans+i
print("-"*count+ans)
     
