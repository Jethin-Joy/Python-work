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