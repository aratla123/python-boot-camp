'''class Cal:
 def add(self,*args): 
       return sum(args)
 
obj1=Cal
print(obj1.add(1,2))
print(obj1.add(1,2,3))
print(obj1.add(1,2,3,4))
#print(obj1.add(1,2,3))'''

class Cal():
 def add(self,*args):
        sum=0
        for i in args:
           sum+=i
        return(sum)
 
obj1=Cal()
print(obj1.add(1,2))
print(obj1.add(1,2,3))
print(obj1.add(1,2,3,4))
