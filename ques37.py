#check the  no.of vowels in a string

inp=str(input())
count=0
str1=['a','e','i','e','o','u']
for i in inp:
    if(i in str1):
        count+=1
print(count) 