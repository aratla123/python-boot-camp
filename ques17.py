#sum of squares of a digits in a given numbers

n=int(input())
sum=0
while(n>0):
 rem=n%10
 sum+=rem*rem #sum+=rem**2
 n=n//10
print(sum)