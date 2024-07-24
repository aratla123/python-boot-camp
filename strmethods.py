#string methods

input="helloworld"
print(input.isalpha())#checks for the alphabets,space=false

input="123"
print(input.isnumeric())

input="helloworld123"
print(input.isalnum())

input="hello"
print(input.isascii())

input="hello"
print(input.islower())

input="hello"
print(input.isupper())

input="hello"
print(input.istitle())

input="123"
print(input.isnumeric())# all integer

input="123"
print(input.isdigit())#0-9

print(ord("A"))
print(ord("a"))
print(ord("0"))
print(ord("["))
print(ord("{"))
print(ord(">"))
print(ord("/"))
print(ord("?"))
print(chr(60))