def count(n):
    if n == 0:
        return
    print(n)
    count(n-1)
count(5)

#Factorial Function
def fact(n):
    if n==0 or n==1: #base case
        return 1
    else:
        return n * fact(n-1) #recursive case
print(fact(5))

#Fibbonaci series
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
print(fib(10))
