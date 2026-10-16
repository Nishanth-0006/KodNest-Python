age =  21
print(f"the age is {age}")

age = input("enter your age  ")
print(f"your age is {age}")
print(type(age))

first = float(input("enter your first number "))
second = float(input("enter your second number "))
print(f"the sum of {first} and {second} number is {first + second}")    
print(type(first))


# Taking a boolean input from the user
user_response = input("Do you like ice cream? (yes/no): ").lower()
is_ice_cream_lover = user_response == "yes"
print("Do you like ice cream?", is_ice_cream_lover)