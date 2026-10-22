# # 1 largest

# numbers = [10, 5, 25, 8, 15]

# largest = numbers[0]

# for num in numbers:
#     if num > largest:
#         largest = num

# print("Largest element:", largest)


# # 2 smallest

# numbers = [10, 5, 25, 8, 15]

# smallest = numbers[0]

# for num in numbers:
#     if num < smallest:
#         smallest = num

# print("Smallest element:", smallest)

# 3 sum of all elements
# numbers = [1, 2, 3, 4, 5]

# total = 0

# for num in numbers:
#     total = total + num

# print("Sum:", total)

# 4 average of elements
# numbers = [10, 20, 30, 40, 50]

# total = 0

# for num in numbers:
#     total = total + num

# average = total / len(numbers)

# print("Average:", average)

# 5 reverse
# numbers = [1, 2, 3, 4, 5]

# reversed_list = []

# for num in numbers:
#     reversed_list.insert(0, num)

# print("Reversed list:", reversed_list)

#  6 duplicates
# numbers = [1, 2, 2, 3, 4, 4, 5]

# unique = []

# for num in numbers:
#     if num not in unique:
#         unique.append(num)

# print("List without duplicates:", unique)

# 7 second largest
# numbers = [10, 20, 50, 40, 30]

# numbers.sort()

# print("Second largest:", numbers[-2])

# 8 even and odd
# numbers = [1, 2, 3, 4, 5, 6]

# even = []
# odd = []

# for num in numbers:
#     if num % 2 == 0:
#         even.append(num)
#     else:
#         odd.append(num)

# print("Even numbers:", even)
# print("Odd numbers:", odd)

# 9 common elements
# list1 = [1, 2, 3, 4, 5]
# list2 = [3, 4, 5, 6, 7]

# common = []

# for num in list1:
#     if num in list2:
#         common.append(num)

# print("Common elements:", common)

# 10 merge
# list1 = [1, 2, 3]
# list2 = [3, 4, 5]

# merged = []

# for num in list1:
#     if num not in merged:
#         merged.append(num)

# for num in list2:
#     if num not in merged:
#         merged.append(num)

# print("Merged list:", merged)

# 11 sum of matrix
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# total = 0

# for row in matrix:
#     for num in row:
#         total = total + num

# print("Sum of all elements:", total)

# 12 largest
# matrix = [
#     [1, 2, 3],
#     [10, 5, 6],
#     [7, 8, 9]
# ]

# largest = matrix[0][0]

# for row in matrix:
#     for num in row:
#         if num > largest:
#             largest = num

# print("Largest element:", largest)