"""
#Arithematic Operators
print(5+3) #8
print(5-3) #2
print(5*3) #15
print(5/3) #1.6666
print(5%3) #2
print(5**3) #125
print(5//3) #1
"""

"""
#Comparision Operators --Boolean Format
print( 11 == 10) # False
print( 11 != 10) # True
print( 11 > 10)  # True
print( 11 < 10)  # False
print( 11 >= 10) # True
print( 11 <= 10) # False
"""
"""
#Assignment Operators
a = 10
print( a ) #10
a+=10 # a = a + 10
print(a) #20
a-=10 # a = a - 10
print(a) #10
a*=10 # a = a * 10
print(a) #100
a/=10 # a = a / 10
print(a) #10.0
a%=10 # a = a % 10
print(a) #0.0
a**=10 # a = a ** 10
print(a) #0.0
a//=10 # a = a // 10
print(a) #0.0

"""

#Logical Operators
"""
a = 2
b = 3
print(a and b) #3
print(a or b ) #2
print(not a) #False
print(not b) #False
"""

#Logical Operators
# a = False
# b = False
# print(a and b)
# print(a or b)
# print(not a)
# print(not b)
# a = (5 > 3) and (4 < 6) #False
# print(a)
# a = (5 > 3) or (4 < 6) #False
# print(a)
# a = not (5 > 3) #False
# print(a)

#Identity Operators
a = 10
b = 10
print(a is b)   #True
print(a is not b) #False
print(a==b) #True
print(a!=b) #False

#Membership Operators
a = [1 , 2 , 3 , 4 , 5 ]
print(1 in a)   #True
print(1 not in a) #False
print(6 in a)   #False
print(6 not in a) #True

#Bitwise Operators
a = 2
b = 3
print(a & b) #2
print(a | b) #3
print(a ^ b) #1

a = 5
print(~a)    #-3
print(~b)    #-4
print(a << b) #4
print(a >> b) #1