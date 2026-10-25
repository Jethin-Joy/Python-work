# 1. Student Marks
# marks = []

# for i in range(5):
#     mark = int(input("Enter marks: "))
#     marks.append(mark)

# print("Marks:", marks)

# highest = marks[0]
# lowest = marks[0]
# count = 0

# for mark in marks:
#     if mark > highest:
#         highest = mark

#     if mark < lowest:
#         lowest = mark

#     if mark > 50:
#         count = count + 1

# print("Highest marks:", highest)
# print("Lowest marks:", lowest)
# print("Students scored above 50:", count)




# 2. Even and Odd Numbers
# numbers = []
# even = []
# odd = []

# for i in range(10):
#     num = int(input("Enter a number: "))
#     numbers.append(num)

# for num in numbers:
#     if num % 2 == 0:
#         even.append(num)
#     else:
#         odd.append(num)

# print("All numbers:", numbers)
# print("Even numbers:", even)
# print("Odd numbers:", odd)




# 3. Positive, Negative and Zero
# numbers = []

# positive = 0
# negative = 0
# zero = 0

# for i in range(10):
#     num = int(input("Enter a number: "))
#     numbers.append(num)

# for num in numbers:
#     if num > 0:
#         positive = positive + 1
#     elif num < 0:
#         negative = negative + 1
#     else:
#         zero = zero + 1

# print("Numbers:", numbers)
# print("Positive numbers:", positive)
# print("Negative numbers:", negative)
# print("Zeros:", zero)




# 4. Search an Element
# numbers = []

# for i in range(5):
#     num = int(input("Enter a number: "))
#     numbers.append(num)

# search = int(input("Enter number to search: "))

# if search in numbers:
#     position = numbers.index(search)
#     print("Number found at position:", position + 1)
# else:
#     print("Number not found")




# 5. Shopping Cart
# prices = []
# n = int(input("How many products? "))

# for i in range(n):
#     price = float(input("Enter product price: "))
#     prices.append(price)

# total = 0

# for price in prices:
#     total = total + price

# print("Product prices:", prices)
# print("Total amount:", total)

# if total > 5000:
#     discount = total * 10 / 100
# else:
#     discount = 0

# final_amount = total - discount

# print("Discount:", discount)
# print("Final amount:", final_amount)




# 6. Number Analyzer
# numbers = []

# for i in range(10):
#     num = int(input("Enter a number: "))
#     numbers.append(num)

# total = 0
# even = 0
# odd = 0

# largest = numbers[0]
# smallest = numbers[0]

# for num in numbers:
#     total = total + num

#     if num % 2 == 0:
#         even = even + 1
#     else:
#         odd = odd + 1

#     if num > largest:
#         largest = num

#     if num < smallest:
#         smallest = num

# average = total / 10

# print("Numbers:", numbers)
# print("Sum:", total)
# print("Average:", average)
# print("Largest:", largest)
# print("Smallest:", smallest)
# print("Even numbers:", even)
# print("Odd numbers:", odd)




# 7. Remove Negative Numbers
# numbers = []
# positive = []

# n = int(input("How many numbers? "))

# for i in range(n):
#     num = int(input("Enter a number: "))
#     numbers.append(num)

# for num in numbers:
#     if num > 0:
#         positive.append(num)

# print("Original list:", numbers)
# print("Positive numbers:", positive)




# 8. Find Duplicate Values
# numbers = []
# duplicates = []

# for i in range(10):
#     num = int(input("Enter a number: "))
#     numbers.append(num)

# for num in numbers:
#     if numbers.count(num) > 1:
#         if num not in duplicates:
#             duplicates.append(num)

# print("Numbers:", numbers)
# print("Duplicate numbers:", duplicates)




# 9. Check Whether a Number Is a Palindrome
# num = int(input("Enter a number: "))

# original = num
# reverse = 0

# while num > 0:
#     digit = num % 10
#     reverse = reverse * 10 + digit
#     num = num // 10

# if original == reverse:
#     print("Palindrome number")
# else:
#     print("Not a palindrome number")



# 10. Check Whether a Number Is an Armstrong Number
# num = int(input("Enter a number: "))

# original = num
# temp = num
# digits = len(str(num))
# total = 0

# while temp > 0:
#     digit = temp % 10
#     total = total + digit ** digits
#     temp = temp // 10

# if original == total:
#     print("Armstrong number")
# else:
#     print("Not an Armstrong number")



# 11. Check Whether a Number Is Prime
# num = int(input("Enter a number: "))

# count = 0

# if num > 1:
#     for i in range(1, num + 1):
#         if num % i == 0:
#             count = count + 1

#     if count == 2:
#         print("Prime number")
#     else:
#         print("Not a prime number")
# else:
#     print("Not a prime number")




# 12. Find the Largest Digit in a Number
num = int(input("Enter a number: "))

largest = 0

while num > 0:
    digit = num % 10

    if digit > largest:
        largest = digit

    num = num // 10

print("Largest digit:", largest)