''' find the missing number in an array like sequence of numbers
testcases:1 2 3 4 5 7 8 9 10
o/p:6'''
n=int(input())

sum1=(n*(n+1))//2
my_lst=list(map(int,input().split()))
sum=0
for i in range(0,len(my_lst)):
    sum=sum+my_lst[i]
   
print(sum1-sum)
