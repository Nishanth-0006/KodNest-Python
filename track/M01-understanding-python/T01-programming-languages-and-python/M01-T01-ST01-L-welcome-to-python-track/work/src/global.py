c = 30
def add():
    global a
    a = 10
    b = 20 #local variable
    print(a + b)
    print(c) #gloabl variable
add()


x = 100
def display():
   x = 50#local variable
   print("Local x:", x)
display()
print("Global x:",x)

x = 10
def display():
    print(x)
    #local variable
    print(x)
display()
x = 30 
print(x)

#defaluṭ args
def add(a,b=10,c=0):
    return a+b+c
print(add(10))

#var args
def add (*args):
    total = 0
    for i in args:
        total = total + i
        #total += i
    return total
# print(add()) #0

# print(add(10,20,10))#40

#keywords arguments
# def display(name,age):
#     print("Name:", name)
#     print("Age:", age)