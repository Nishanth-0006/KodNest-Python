# #Functions
# # **create a function to sum of 2 numbers
# def add():
#   a = 10
#   b = 39
#   c = a + b
#   print(c)

# #Calling
# add()

# # Square of number
# def Square():
#     n = 5
#     res = n * n
#     print(res)
# Square()

# # DEf the function to find the largest of three numbers
# def largest():
#     a = 10
#     b = 23
#     c = 1
#     if a >=b and a>=c:
#         return a
#     elif b >= a and b>=c:
#         return b
#     else:
#         return c
# largest()

# # find the number is even
# def even():
#     a = 10
#     if a % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"
# even()

# # define a function to greet 
# def greet():
#     name = "vihani"
#     print(" G M " + name)
# greet() 


#Types of function
#No ip and no op
def square():
    n = 5 * 5
    print(n)
square()

#No ip and op
def square():
    n = 5 * 5
    return n
print (square())

# ip and no op
def square(n):
   res = n * n
   print(res)
square(3)

# ip and op
def square(n):
    return n * n
res = (square(1))
print(res)