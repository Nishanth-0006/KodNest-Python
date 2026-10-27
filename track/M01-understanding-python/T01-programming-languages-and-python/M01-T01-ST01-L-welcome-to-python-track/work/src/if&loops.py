#  1.check whether a number is positive
# num = input("enter Number: ")
# if int(num) >=0:
#     print("number is +ve")
# else:
#     print("number is -ve")

# 2. check if a person is eligible to donate blood (Age >= 18)
# age = input("Enter AGE: ")
# if int(age) >= 18:
#     print("Eligible")
# else:
#     print("Not eligible")

# 3. check if the temperature is above 30 and print "Hot Day"
# temp = int(input("Enter Temperature: "))
# if temp > 30:
#     print("Hot Day")   

# 4. check whether a student has attended at least 75% of classes
# attended = int(input("Enter Number of classes attended: "))
# total = int(input("Enter Total Number of classes: "))
# if attended/total * 100 >=75:
#     print("Eligible for exams")
# else:
#     print("Not eligible for exams")

# 5. check whether a number is even or odd
# num = int(input("enter num: "))
# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# 6. check wheter the person is eligable for dl
# age = int(input("enter age: "))
# if age >= 18:
#     print("Eligible for DL")
# else:
#     print("Not eligible for DL")

# check if a year is leap year or not
# year = int(input("Enter Year : "))
# if year % 4 == 0:
#     print ("Leap year")
# else:
#     print("Not a Leap Year")

# 8. compare two numbers and print the greater number
# num1 = int(input("Enter num1: "))
# num2 = int(input("Enter num2: "))
# if num1 > num2:
#     print("num1 is greater")
# else:
#     print("num2 is greater")

# 9. assign grades based on marks 
# 90-100 -> grade A
# 80-89 -> grade B
# 70-79 -> grade C
# 60-69 -> grade D    
# below 60 -> fail
# marks = int(input("Enter the Marks:"))
# if marks>=90 and marks <=100:
#     print("Grade A")
# elif marks>=80 and marks <=89:
#     print("Grade B")
# elif marks>=70 and marks <=79:
#     print("Grade C")
# elif marks>=60 and marks <=69:
#     print("Grade D")
# else:
#     print("Fail")

# 10. catergories electricity usage
# above 500 -> High
# 301-500 -> Medium
# 101-300 -> Low
# 0- 100 -> very low
# use = int(input("Enter the units consumed: "))
# if use > 500:
#     print("High")
# elif use > 300 and use < 500:
#     print("Medium")
# elif use > 100 and use < 300:
#     print("Low")
# else:
#     print("Very Low")

#11. Scholorship eligibilty
# marks >= 85
# family income < 300000
# marks = int(input("Enter your marks: "))
# family_income = int(input("Enter your family income: "))
# if marks >=85 and  family_income <=300000:
#     print("Eligible")
# else:
#     print("Not Eligible")
    
#12. user login
# username is correct
# passwordd is correct
# username = input("Enter your username: ")
# password = input("Enter your password: ")
# if username == "admin" and password == "1234":
#     print("Login Successful")
# else:
#     print("Invalid Credentials")

#13. display weekday using numbers (1-7):
# num = int(input("Enter a number: "))
# if num == 1:
#     print("Monday")
# elif num == 2:
#     print("Tuesday")
# elif num == 3:
#     print("Wednesday")
# elif num == 4:
#     print("Thursday")
# elif num == 5:
#     print("Friday")
# elif num == 6:
#     print("Saturday")
# elif num == 7:
#     print("Sunday")
# else:
#     print("Invalid input")

# 14. display seasom based on month
# dec,jan, feb -> winter case 12|1|2
# mar,apr,may -> summer case 3|4|5
# jun,jul,aug -> rainy case 6|7|8
# sep,oct,nov -> autumn case 9|10|11

# month = int(input("Enter the month: "))
# if month in (12, 1, 2):
#     print("Winter")
# elif month in (3, 4, 5):
#     print("Summer")
# elif month in (6, 7, 8):
#     print("Rainy")
# elif month in (9, 10, 11):
#     print("Autumn")
# else:
#     print("Invalid month")

# 15. print number from 1 to 20
# for i in range(1,21):
#     print(i)

# 16. print multiplication table of a given number
# num = int(input("Enter the number: "))
# for i in range(1,11):
#     print(num ,"*" ,i ,"=" ,num * i)

# 17. print number from 10 to 1
# for i in range(10 , 1, -1):
#     print(i)


# 18. find factorial of a number
# num = int(input("Enter a number: "))
# fact = 1
# while num > 0:
#     fact = fact * num
#     num = num - 1
# print(fact)

# 19. print number from 1 to 20 and stop at 15
# for i in range(1, 21):
#     if i == 15:
#         break
#     print(i)

# 20. search for a number in alist using break
# numbers = [10, 20, 30, 40, 50]
# search = int(input("Enter the number to search: "))
# for i in numbers:
#     if i == search:
#         print("Number found")
#         break
# else:
#     print("Number not found")

# 21. print numbers from 1 to 10 , skipping multiples of 3
# for i in range (1,20,3):
#   print(i)

# 22. print odd numbers from 1 to 50
# for i in range (1, 51, 2):
#   print(i)

#23. find the cube of a number 

num = int(input("Enter a number: "))
cube = num * num * num
print("Cube of ", num, "is", cube)

24. 