# 1. Student Marks
marks = []

for i in range(5):
    mark = int(input("Enter marks: "))
    marks.append(mark)

print("Marks:", marks)

highest = marks[0]
lowest = marks[0]
count = 0

for mark in marks:
    if mark > highest:
        highest = mark

    if mark < lowest:
        lowest = mark

    if mark > 50:
        count = count + 1

print("Highest marks:", highest)
print("Lowest marks:", lowest)
print("Students scored above 50:", count)