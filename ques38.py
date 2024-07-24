inp=str(input())
str="bcdfghjklmnpqrstvwxyz"
count=0
str1=['a','e','i','e','o','u']
for i in inp:
    if(i in str):
        count+=1
print(count) #in case of combo of lower and upper case letters first convert them into a convinient case and check for the condition