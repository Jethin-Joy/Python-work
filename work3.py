# 1: Traffic Light Simulator 
# color = input("Enter traffic light color: ").lower()

# match color:
#     case "red":
#         print("Stop")
#     case "yellow":
#         print("Slow down")
#     case "green":
#         print("Go")
#     case _:
#         print("Invalid color")


# 2: Even or Odd?
# number = int(input("Enter a whole number: "))

# if number % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# Basic If-Else Questions
# 1
# num = int(input("Enter a number: "))

# if num > 0:
#     print("Positive")
# elif num < 0:
#     print("Negative")
# else:
#     print("Zero")


# 3
# age = int(input("Enter your age: "))

# if age >= 18:
#     print("Eligible to vote")
# else:
#     print("Not eligible to vote")


# 4
# temp = float(input("Enter temperature in Celsius: "))

# if temp < 20:
#     print("Cold")
# elif temp <= 30:
#     print("Warm")
# else:
#     print("Hot")


# 5
# year = int(input("Enter a year: "))

# if year % 400 == 0:
#     print("Leap year")
# elif year % 100 == 0:
#     print("Not a leap year")
# elif year % 4 == 0:
#     print("Leap year")
# else:
#     print("Not a leap year")

# Nested If Questions
# 6
# marks = int(input("Enter your marks: "))

# if marks >= 0 and marks <= 100:
#     if marks >= 90:
#         print("Grade A")
#     elif marks >= 80:
#         print("Grade B")
#     elif marks >= 70:
#         print("Grade C")
#     elif marks >= 60:
#         print("Grade D")
#     else:
#         print("Grade F")
# else:
#     print("Invalid marks")



# 7
# num = int(input("Enter a number: "))

# if num > 0:
#     if num % 2 == 0:
#         print("Positive and even")
#     else:
#         print("Not positive or not even")
# else:
#     print("Not positive")


# 8
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))

# if a >= b:
#     if a >= c:
#         print("Largest:", a)
#     else:
#         print("Largest:", c)
# else:
#     if b >= c:
#         print("Largest:", b)
#     else:
#         print("Largest:", c)


# If-Elif-Else Questions
# 9
# amount = float(input("Enter purchase amount: "))

# if amount > 5000:
#     discount = amount * 0.20
# elif amount >= 2000:
#     discount = amount * 0.10
# else:
#     discount = 0

# final_bill = amount - discount

# print("Discount:", discount)
# print("Final bill:", final_bill)


# 10
# day = int(input("Enter a day number (1-7): "))

# if day == 1:
#     print("Monday")
# elif day == 2:
#     print("Tuesday")
# elif day == 3:
#     print("Wednesday")
# elif day == 4:
#     print("Thursday")
# elif day == 5:
#     print("Friday")
# elif day == 6:
#     print("Saturday")
# elif day == 7:
#     print("Sunday")
# else:
#     print("Invalid day number")


# For Loop Questions
# 1
# for i in range(1, 11):
#     print(i)


# 2
# n = int(input("Enter a number: "))
# for i in range(1, 11):
#     print(n, "x", i, "=", n * i)


# 3
# n = int(input("Enter n: "))
# total = 0

# for i in range(1, n + 1):
#     total = total + i

# print("Sum =", total)


# 4
# n = int(input("How many numbers? "))

# a = 0
# b = 1

# for i in range(n):
#     print(a)
#     a, b = b, a + b

# 5
# for i in range(1, 5):
#     print("*" * i)


# 6
# text = input("Enter a string: ")
# reverse = ""
# for ch in text:
#     reverse = ch + reverse

# print("Reversed string:", reverse)

# 7
# for i in range(2, 51, 2):
#     print(i)


# While Loop Questions
# 8
# n = int(input("Enter n: "))

# while n >= 1:
#     print(n)
#     n = n - 1

# 9
# n = int(input("Enter a number: "))
# factorial = 1

# while n > 1:
#     factorial = factorial * n
#     n = n - 1

# print("Factorial =", factorial)

# 10
# n = int(input("Enter a number: "))

# if n < 0:
#     n = -n

# if n == 0:
#     print(0)
# else:
#     while n > 0:
#         digit = n % 10
#         print(digit)
#         n = n // 10

# 11
# n = int(input("Enter a number: "))
# n = abs(n)
# count = 0

# if n == 0:
#     count = 1
# else:
#     while n > 0:
#         count = count + 1
#         n = n // 10

# print("Number of digits:", count)


# 12
# while True:
#     text = input("Enter something (or exit): ")

#     if text == "exit":
#         break

#     print("You entered:", text)


# Loop Control Statements
# 13
# numbers = [10, 20, 30, 40, 50]
# target = int(input("Enter the number to find: "))

# for num in numbers:
#     if num == target:
#         print("Number found!")
#         break
# else:
#     print("Number not found.")


# 14
# for i in range(1, 21):
#     if i % 2 == 0:
#         continue

#     print(i)

# 15
# for i in range(1, 6):
#     if i == 3:
#         pass

#     print(i)

# Match Statements

# 1
# day = int(input("Enter a day number (1-7): "))

# match day:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case 4:
#         print("Thursday")
#     case 5:
#         print("Friday")
#     case 6 | 7:
#         print("Weekend")
#     case _:
#         print("Invalid day")


# 2
# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))
# op = input("Enter operator (+, -, *, /): ")

# match op:
#     case "+":
#         print("Result =", a + b)
#     case "-":
#         print("Result =", a - b)
#     case "*":
#         print("Result =", a * b)
#     case "/":
#         if b != 0:
#             print("Result =", a / b)
#         else:
#             print("Cannot divide by zero")
#     case _:
#         print("Invalid operator")

# 3
# marks = int(input("Enter marks (0-100): "))

# match marks:
#     case x if 90 <= x <= 100:
#         print("Grade A")
#     case x if 80 <= x <= 89:
#         print("Grade B")
#     case x if 70 <= x <= 79:
#         print("Grade C")
#     case x if 60 <= x <= 69:
#         print("Grade D")
#     case x if 0 <= x <= 59:
#         print("Grade F")
#     case _:
#         print("Invalid marks")


# 4
# status = int(input("Enter HTTP status code: "))

# match status:
#     case 200:
#         print("OK")
#     case 404:
#         print("Not Found")
#     case x if 500 <= x <= 599:
#         print("Server Error")
#     case x if 400 <= x <= 499:
#         print("Client Error")
#     case _:
#         print("Other status code")

# 5
# row = int(input("Enter row (1-8): "))
# col = int(input("Enter column (1-8): "))

# if 1 <= row <= 8 and 1 <= col <= 8:
#     match (row % 2, col % 2):
#         case (1, 1) | (0, 0):
#             print("Black square")
#         case (1, 0) | (0, 1):
#             print("White square")
# else:
#     print("Invalid position")

# 6
# cmd = ["add", 5, 3]

# match cmd:
#     case ["add", a, b]:
#         print("Result =", a + b)
#     case ["quit"]:
#         print("Program ended")
#     case _:
#         print("Invalid command")

# 7
# filename = input("Enter filename: ")
# parts = filename.split(".")

# match parts:
#     case [name, "jpg"] | [name, "png"]:
#         print("Image file")
#     case [name, "py"]:
#         print("Python file")
#     case _:
#         print("Unknown file type")


# 8
shape = ("circle", 5)

match shape:
    case ("circle", radius):
        area = 3.14 * radius * radius
        print("Circle area =", area)

    case ("rect", length, width):
        area = length * width
        print("Rectangle area =", area)

    case _:
        print("Invalid shape")