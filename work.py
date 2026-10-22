# 1  College Event Registration 
# age = int(input("Enter your age: "))
# student = input("Are you a student? (yes/no): ")

# if age >= 18 and age <= 25 and student == "yes":
#     print("Eligible for registration")
# else:
#     print("Not eligible")


# 2 Online Shopping Discount 
# amount = float(input("Enter order amount: "))
# premium = input("Are you a premium member? (yes/no): ")

# if amount >= 3000 or premium == "yes":
#     print("Discount available")
# else:
#     print("Discount not available")


# 3 Airport Check-in
# ticket = input("Is the ticket confirmed? (yes/no): ")
# passport = input("Is the passport valid? (yes/no): ")
# hours = float(input("Hours until departure: "))

# if ticket == "yes" and passport == "yes" and hours > 2:
#     print("Online check-in available")
# else:
#     print("Online check-in not available")


# 4 Movie Ticket Booking 
# age = int(input("Enter your age: "))

# if age < 12 or age >= 60:
#     print("Special ticket price")
# else:
#     print("Normal ticket price")


# 5. Bank Loan Pre-Eligibility
# income = float(input("Enter monthly income: "))
# credit_score = int(input("Enter credit score: "))
# default = input("Do you have an existing loan default? (yes/no): ")

# if income >= 40000 and credit_score >= 700 and default == "no":
#     print("Eligible for loan")
# else:
#     print("Not eligible for loan")


# 6. Food Delivery Free Shipping 
# amount = float(input("Enter order amount: "))
# premium = input("Are you a premium member? (yes/no): ")
# disabled = input("Has the restaurant disabled delivery? (yes/no): ")

# if (amount >= 500 or premium == "yes") and disabled == "no":
#     print("Free delivery available")
# else:
#     print("Free delivery not available")


# 7. Employee Work-from-Home Eligibility
# months = int(input("Enter months in the company: "))
# remote = input("Does the project allow remote work? (yes/no): ")

# if months >= 6 and remote == "yes":
#     print("Work from home allowed")
# else:
#     print("Work from home not allowed")


# 8. Hotel Room Booking
# room = input("Is the room available? (yes/no): ")
# payment = input("Is the payment method valid? (yes/no): ")
# stopped = input("Has the hotel stopped reservations? (yes/no): ")

# if room == "yes" and payment == "yes" and stopped == "no":
#     print("Booking can proceed")
# else:
#     print("Booking cannot proceed")


# 9. Online Exam Access
# logged_in = input("Are you logged in? (yes/no): ")
# registered = input("Is exam registration confirmed? (yes/no): ")
# active = input("Is the exam active? (yes/no): ")
# blocked = input("Is your account blocked? (yes/no): ")

# if logged_in == "yes" and registered == "yes" and active == "yes" and blocked == "no":
#     print("You can access the exam")
# else:
#     print("You cannot access the exam")


# 10. Gym Membership Plan
# years = float(input("How many years have you been subscribed? "))
# active = input("Is your membership active? (yes/no): ")
# yearly = input("Did you purchase a yearly plan? (yes/no): ")

# if (years >= 1 and active == "yes") or yearly == "yes":
#     print("Premium upgrade available")
# else:
#     print("Premium upgrade not available")


# 11. Ride Booking Application
# service_area = input("Is the pickup location in the service area? (yes/no): ")
# driver = input("Is a driver available? (yes/no): ")
# scheduled = input("Are scheduled rides enabled? (yes/no): ")

# if (service_area == "yes" and driver == "yes") or scheduled == "yes":
#     print("Booking can be made")
# else:
#     print("Booking cannot be made")


# 12. E-commerce Product Return
# days = int(input("How many days ago was the product purchased? "))
# unused = input("Is the product unused? (yes/no): ")
# eligible = input("Is the product eligible for return? (yes/no): ")

# if days <= 7 and unused == "yes" and eligible == "yes":
#     print("Return accepted")
# else:
#     print("Return not accepted")


# 13. Library Book Borrowing
# overdue = input("Do you have overdue books? (yes/no): ")
# membership = input("Is your membership active? (yes/no): ")
# book = input("Is the book available? (yes/no): ")

# if overdue == "no" and membership == "yes" and book == "yes":
#     print("You can borrow the book")
# else:
#     print("You cannot borrow the book")


# 15. Mobile Data Usage Alert
# usage = float(input("Enter data usage percentage: "))
# remaining = float(input("Enter remaining data in GB: "))
# unlimited = input("Do you have an unlimited plan? (yes/no): ")

# if (usage >= 90 or remaining < 1) and unlimited == "no":
#     print("Warning: Data usage is high")
# else:
#     print("No warning")


# 16. Parking Lot Entry 
# pass_valid = input("Do you have a valid parking pass? (yes/no): ")
# visitor = input("Are you paying for visitor parking? (yes/no): ")
# full = input("Is the parking lot full? (yes/no): ")

# if (pass_valid == "yes" or visitor == "yes") and full == "no":
#     print("Vehicle can enter")
# else:
#     print("Vehicle cannot enter")


# 17. Scholarship Eligibility 
# score = float(input("Enter academic score: "))
# attendance = float(input("Enter attendance percentage: "))

# if score >= 95 or (score >= 85 and attendance >= 75):
#     print("Eligible for scholarship")
# else:
#     print("Not eligible for scholarship")


# 18. Food Ordering – Restaurant Availability
# open_restaurant = input("Is the restaurant open? (yes/no): ")
# delivery = input("Does the restaurant deliver to you? (yes/no): ")
# online = input("Is the restaurant accepting online orders? (yes/no): ")

# if open_restaurant == "yes" and delivery == "yes" and online == "yes":
#     print("Order can be placed")
# else:
#     print("Order cannot be placed")


# 19. Smart Home Security
# motion = input("Is motion detected? (yes/no): ")
# door = input("Is the main door opened? (yes/no): ")
# armed = input("Is the security system armed? (yes/no): ")

# if armed == "yes" and (motion == "yes" or door == "yes"):
#     print("Security alert triggered")
# else:
#     print("No security alert")


# 20. Travel Insurance Eligibility
age = int(input("Enter your age: "))
days = int(input("Enter trip duration in days: "))
covered = input("Is the destination covered? (yes/no): ")
excluded = input("Is the destination currently excluded? (yes/no): ")

if age >= 18 and age <= 65 and days <= 30 and covered == "yes" and excluded == "no":
    print("Eligible for travel insurance")
else:
    print("Not eligible for travel insurance")