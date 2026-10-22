#  1

# marks = int(input("Enter your marks: "))

# if marks >= 90 and marks <= 100:
#     print("Grade: A+")

# elif marks >= 80 and marks <= 89:
#     print("Grade: A")

# elif marks >= 70 and marks <= 79:
#     print("Grade: B")

# elif marks >= 60 and marks <= 69:
#     print("Grade: C")

# elif marks >= 50 and marks <= 59:
#     print("Grade: D")

# elif marks >= 0 and marks <= 49:
#     print("Grade: Fail")

# else:
#     print("Invalid marks")



#  2

# balance = int(input("Enter account balance: "))
# amount = int(input("Enter withdrawal amount: "))

# if amount > balance:
#     print("Insufficient Balance")
# elif amount % 100 != 0:
#     print("Enter an amount in multiples of ₹100")
# else:
#     print("Withdrawal Successful")



#  3

# amount = float(input("Enter order amount: "))

# if amount >= 5000:
#     delivery = 0
# elif amount >= 2000:
#     delivery = 50
# else:
#     delivery = 100

# final_amount = amount + delivery

# print("Delivery charge:", delivery)
# print("Final amount:", final_amount)



#  4

# score = int(input("Enter performance score: "))

# if score >= 90:
#     print("Excellent")
# elif score >= 75:
#     print("Very Good")
# elif score >= 60:
#     print("Good")
# elif score >= 40:
#     print("Needs Improvement")
# else:
#     print("Poor")



#  5

# units = int(input("Enter units consumed: "))

# if units <= 100:
#     bill = units * 2
# elif units <= 200:
#     bill = (100 * 2) + ((units - 100) * 3)
# elif units <= 400:
#     bill = (100 * 2) + (100 * 3) + ((units - 200) * 5)
# else:
#     bill = (100 * 2) + (100 * 3) + (200 * 5) + ((units - 400) * 7)

# print("Electricity bill:", bill)



#  6

# age = int(input("Enter your age: "))

# if age < 5:
#     print("Ticket price: Free")
# elif age <= 12:
#     print("Ticket price: ₹100")
# elif age <= 59:
#     print("Ticket price: ₹200")
# else:
#     print("Ticket price: ₹120")



#  7

# speed = int(input("Enter vehicle speed: "))

# if speed <= 60:
#     print("No fine")
# elif speed <= 80:
#     print("Fine: ₹500")
# elif speed <= 100:
#     print("Fine: ₹1,000")
# else:
#     print("Fine: ₹2,000")
#     print("License Review")



#  8

# bill = float(input("Enter total bill: "))

# if bill >= 5000:
#     discount = bill * 0.20
# elif bill >= 3000:
#     discount = bill * 0.15
# elif bill >= 1000:
#     discount = bill * 0.10
# else:
#     discount = 0

# final_bill = bill - discount

# print("Discount:", discount)
# print("Final bill:", final_bill)



#  9

# score = int(input("Enter entrance score: "))

# if score >= 90:
#     print("Direct Admission")
# elif score >= 75:
#     print("Admission + Interview")
# elif score >= 60:
#     print("Waitlisted")
# else:
#     print("Not Eligible")



#  10

# score = int(input("Enter credit score: "))
# default = input("Do you have an existing loan default? (yes/no): ")

# if default == "yes":
#     print("Loan Approval Requires Manual Review")
# elif score >= 750:
#     print("Low Risk")
# elif score >= 650:
#     print("Medium Risk")
# elif score >= 550:
#     print("High Risk")
# else:
#     print("Very High Risk")



#  11

# room = input("Enter room type: ").strip().lower()
# nights = int(input("Enter number of nights: "))

# if room == "standard":
#     price = 2000
# elif room == "deluxe":
#     price = 3500
# elif room == "suite":
#     price = 5000
# else:
#     price = 0

# total = price * nights

# if nights > 5:
#     discount = total * 0.10
# else:
#     discount = 0

# final_bill = total - discount

# print("Final bill:", final_bill)



#  12

# salary = float(input("Enter annual salary: "))
# performance = int(input("Enter performance score: "))

# if performance >= 90:
#     bonus = salary * 0.20
# elif performance >= 75:
#     bonus = salary * 0.15
# elif performance >= 60:
#     bonus = salary * 0.10
# else:
#     bonus = 0

# print("Bonus:", bonus)



#  13

# data = float(input("Enter monthly data requirement in GB: "))

# if data < 5:
#     print("Basic Plan - ₹199")
# elif data <= 20:
#     print("Standard Plan - ₹399")
# elif data <= 50:
#     print("Premium Plan - ₹699")
# else:
#     print("Unlimited Plan - ₹999")



#  14

# hours = int(input("Enter parking hours: "))
# electric = input("Is it an electric vehicle? (yes/no): ")

# if hours <= 2:
#     fee = 30
# elif hours <= 5:
#     fee = 50
# elif hours <= 10:
#     fee = 100
# else:
#     fee = 150

# if electric == "yes":
#     fee = fee - (fee * 0.20)

# print("Final parking fee:", fee)



#  15

# theory = int(input("Enter theory mark: "))
# practical = int(input("Enter practical mark: "))

# if theory < 40 or practical < 40:
#     print("Fail")
# else:
#     average = (theory + practical) / 2
#     print(average)
#     if average >= 75:
#         print("Distinction")
#     elif average >= 60:
#         print("First Class")
#     elif average >= 50:
#         print("Second Class")
#     else:
#         print("Pass")



# 16

# weight = float(input("Enter baggage weight in kg: "))
# business = input("Are you travelling Business Class? (yes/no): ")

# if business == "yes":
#     limit = 25
# else:
#     limit = 15

# if weight <= limit:
#     fee = 0
# elif weight <= 20:
#     fee = 500
# elif weight <= 30:
#     fee = 1000
# else:
#     fee = 2000

# print("Baggage charge:", fee)



# 17

# days = int(input("How many days ago was it purchased? "))
# unused = input("Is the product unused? (yes/no): ")
# returnable = input("Is the product returnable? (yes/no): ")

# if days > 7:
#     print("Rejected: Purchase was more than 7 days ago")
# elif unused == "no":
#     print("Rejected: Product has been used")
# elif returnable == "no":
#     print("Rejected: Product is not returnable")
# else:
#     print("Return Approved")



# 18

# salary = float(input("Enter annual salary: "))

# if salary <= 300000:
#     tax = 0
# elif salary <= 600000:
#     tax = salary * 0.05
# elif salary <= 1000000:
#     tax = salary * 0.10
# else:
#     tax = salary * 0.20

# final_salary = salary - tax

# print("Tax:", tax)
# print("Final salary:", final_salary)



# 19 

# distance = float(input("Enter distance in km: "))
# peak = input("Is it peak hour? (yes/no): ")

# if distance <= 5:
#     fare = 100
# elif distance <= 15:
#     fare = distance * 15
# elif distance <= 30:
#     fare = distance * 12
# else:
#     fare = distance * 10

# if peak == "yes":
#     fare = fare + (fare * 0.20)

# print("Final fare:", fare)



# 20

available = int(input("Enter available leave days: "))
requested = int(input("Enter requested leave days: "))

if requested > available:
    print("Leave Rejected")
elif requested <= 3:
    print("Leave Automatically Approved")
elif requested <= 7:
    print("Manager Approval Required")
else:
    print("HR Approval Required")