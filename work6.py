# Part 1
# 1. Employee Salary Calculation

# basic_salary = 35000
# bonus = 5000
# tax = 2000

# total = basic_salary + bonus
# print("Total salary:", total)

# final_salary = total - tax
# print("Final salary:", final_salary)

# yearly_salary = final_salary * 12
# print("Yearly salary:", yearly_salary)

# monthly_salary = yearly_salary // 12
# print("Monthly salary:", monthly_salary)




# 2. Mobile Shop Discount System
# mobile_price = 45000
# discount = 5000
# gst = 2000

# discounted_price = mobile_price - discount
# print("Discounted price:", discounted_price)

# final_amount = discounted_price + gst
# print("Final amount:", final_amount)

# half_amount = final_amount / 2
# print("Half amount:", half_amount)

# remainder = final_amount % 3
# print("Remainder:", remainder)




# 3. Student Exam Marks Analysis
# python_marks = 85
# sql_marks = 78
# powerbi_marks = 90

# total_marks = python_marks + sql_marks + powerbi_marks
# print("Total marks:", total_marks)

# average_marks = total_marks / 3
# print("Average marks:", average_marks)

# if python_marks > sql_marks:
#     print("Python marks greater than SQL:", True)
# else:
#     print("Python marks greater than SQL:", False)

# if powerbi_marks == python_marks:
#     print("Power BI marks equal to Python:", True)
# else:
#     print("Power BI marks equal to Python:", False)




# 4. Ecommerce Order Billing
# product_price = 1200
# quantity = 4
# delivery_charge = 150

# total_cost = product_price * quantity
# print("Total product cost:", total_cost)

# total_bill = total_cost + delivery_charge
# print("Total bill:", total_bill)

# if total_bill > 5000:
#     print("Bill greater than 5000:", True)
# else:
#     print("Bill greater than 5000:", False)

# square = quantity ** 2
# print("Square of quantity:", square)




# 5. Data Usage Monitoring
# daily_usage = 2.5
# days = 30

# monthly_usage = daily_usage * days
# print("Monthly usage:", monthly_usage, "GB")

# usage_mb = monthly_usage * 1024
# print("Usage in MB:", usage_mb)

# print("Usage greater than 50 GB:", monthly_usage > 50)

# monthly_usage += 10
# print("Usage after adding 10 GB:", monthly_usage, "GB")




# 6. Bank Account Transactions
# balance = 50000
# deposit = 12000
# withdraw = 7000

# balance = balance + deposit
# print("Balance after deposit:", balance)

# balance = balance - withdraw
# print("Balance after withdrawal:", balance)

# double_balance = balance * 2
# print("Double balance:", double_balance)

# print("Balance less than 100000:", balance < 100000)




# 7. Laptop EMI Calculation
# laptop_price = 80000
# months = 10

# emi = laptop_price / months
# print("Monthly EMI:", emi)

# remainder = emi % 7
# print("Remainder when EMI is divided by 7:", remainder)

# print("EMI greater than 5000:", emi > 5000)

# emi += 500
# print("EMI after increase:", emi)




# 8. Social Media Followers Analysis
# instagram = 25000
# youtube = 18000
# linkedin = 12000

# total_followers = instagram + youtube + linkedin
# print("Total followers:", total_followers)

# difference = instagram - linkedin
# print("Instagram and LinkedIn difference:", difference)

# print("YouTube not equal to LinkedIn:", youtube != linkedin)

# double_followers = total_followers * 2
# print("Double the total followers:", double_followers)




# Part 2

# 1. Student Profile Management
# student = {
#     "name": "Rahul",
#     "course": "Data Science",
#     "marks": 88,
#     "city": "Bangalore"
# }

# print("Student name:", student["name"])
# print("Course name:", student["course"])

# student["marks"] = 95
# student["email"] = "rahul@gmail.com"

# student.pop("city")

# print("All dictionary values:", list(student.values()))
# print("Updated student details:", student)




# 2. Employee Information System
employee = {
    "id": 101,
    "name": "Anjali",
    "department": "HR",
    "salary": 45000
}

print("Employee salary:", employee["salary"])

employee["salary"] += 5000
employee.update({"location": "Kochi"})

employee.pop("department")

print("All employee keys:", list(employee.keys()))
print("Updated employee details:", employee)