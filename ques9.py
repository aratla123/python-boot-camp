'''find the element present in (k+n) index
sample testcase: k=3 , n=2  
3,6,8,4,61,2 
o/p: 2 explanation:3+2=5, index 5=2
testcase2: k=3,k=4
80,70,54,36,72 explanation:3+4=7 (out of loop)
o/p:error'''

my_list=list(map(int,input().split()))
k=int(input())
n=int(input())
c=k+n
if(c>len(my_list)):
    print("error")
else:
  for i in range(0,len(my_list)):
   a=(my_list[c])
  print(a,end="")    


