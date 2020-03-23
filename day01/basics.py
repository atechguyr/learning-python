#single line comment
'''
this is an example of multiline comment
comments are ignored by compiler/interpreter

'''

#print() is used to give output on screen
print(1.0)

#print(a) this gives an error because a is not defined yet

a='a'
print(a)

#print a string
print('avichal',a,'gkg')

#multine print
print('''print(add)
    this is an
    example of 
    multiline string
''')

#input(<label>, **options) - used to give input to the system
#input('enter:')

#input retuns always a string
'''var = input('enter:')
typ = type(var)
print(typ)'''

#type is used to determine the datatype of a value
num1 = int(input("enter value for num1: "))
num2 = int(input("enter value for num2: "))

add=num1+num2
mul=num1*num2
div=num1/num2
sub=num1-num2

print("the value of add = ",add)
print("the value of mul=",mul)
print("the value of div=",div)
print("the value of sub",sub)