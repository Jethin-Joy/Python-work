# 1. Students Enrolled in Courses

# python_students = {"Arun", "Megha", "Rahul", "Sneha"}
# analytics_students = {"Sneha", "Rahul", "Aman", "Diya"}

# print("Both courses:", python_students & analytics_students)
# print("Only Python:", python_students - analytics_students)
# print("Only Data Analytics:", analytics_students - python_students)
# print("All unique students:", python_students | analytics_students)
# print("Exactly one course:", python_students ^ analytics_students)




# 2. Mobile Brands Purchased by Customers

# customer1 = {"Samsung", "Apple", "OnePlus", "Realme"}
# customer2 = {"Apple", "Vivo", "Oppo", "Samsung"}

# print("Common brands:", customer1 & customer2)
# print("All brands:", customer1 | customer2)
# print("Brands purchased only by customer1:", customer1 - customer2)
# print("Brands purchased by only one customer:", customer1 ^ customer2)




# 3. Employees Using Software Tools

# design_team = {"Figma", "Photoshop", "Canva", "Illustrator"}
# marketing_team = {"Canva", "Excel", "Photoshop", "PowerBI"}

# print("Tools used by both teams:", design_team & marketing_team)
# print("Exclusive to design team:", design_team - marketing_team)
# print("All software tools used in the company.", design_team | marketing_team)
# print("Tools used by only one team:", design_team ^ marketing_team)




# 4. Cricket and Football Fans

# cricket_fans = {"Ajay", "Amal", "Alan", "Nisha"}
# football_fans = {"Nisha", "Rahul", "Ajay", "David"}

# print("Fans of both sports:", cricket_fans & football_fans)
# print("Only cricket fans:", cricket_fans - football_fans)
# print("Only football fans:", football_fans - cricket_fans)
# print("All sports fans:", cricket_fans | football_fans)




# 5. Online Shopping Categories

# electronics = {"Laptop", "Headphones", "Mouse", "Keyboard"}
# accessories = {"Keyboard", "Mouse Pad", "Laptop Stand", "Headphones"}

# print("Common products:", electronics & accessories)
# print("Only in electronics:", electronics - accessories)
# print("All purchased items:", electronics | accessories)
# print("Products in only one category:", electronics ^ accessories)




# 6. Languages Known by Employees

# employee1 = {"Python", "Java", "SQL", "C"}
# employee2 = {"Python", "JavaScript", "SQL", "Go"}

# print("Common languages:", employee1 & employee2)
# print("Only employee1:", employee1 - employee2)
# print("All unique languages:", employee1 | employee2)
# print("Languages known by only one employee:", employee1 ^ employee2)




# 7. OTT Platform Subscriptions

# friend1 = {"Netflix", "Prime", "Hotstar", "SonyLiv"}
# friend2 = {"Netflix", "Zee5", "Prime", "JioCinema"}

# print("Common subscriptions:", friend1 & friend2)
# print("Unique to friend1:", friend1 - friend2)
# print("All OTT platforms:", friend1 | friend2)
# print("Platforms subscribed by only one friend:", friend1 ^ friend2)




# 8. Available and Sold Products

# available_products = {"Laptop", "Mouse", "Keyboard", "Monitor"}
# sold_products = {"Mouse", "Monitor"}

# remaining_products = available_products - sold_products
# print("Remaining available products:", remaining_products)

# print("Sold products:", sold_products)

# available_products.add("Printer")
# print("After adding Printer:", available_products)

# available_products.remove("Keyboard")
# print("After removing Keyboard:", available_products)




# 9. College Event Participation

# music_event = {"Anu", "David", "Riya", "Sam"}
# dance_event = {"Riya", "Sam", "Karthik", "John"}

# print("Both events:", music_event & dance_event)
# print("Only music:", music_event - dance_event)
# print("Only dance:", dance_event - music_event)
# print("All participants:", music_event | dance_event)




# 10. Website Visitors

# campaign_A = {"user101", "user102", "user103", "user104"}
# campaign_B = {"user103", "user104", "user105", "user106"}

# print("Common visitors:", campaign_A & campaign_B)
# print("Unique to campaign_A:", campaign_A - campaign_B)
# print("Total unique visitors:", campaign_A | campaign_B)
# print("Visitors from only one campaign:", campaign_A ^ campaign_B)


# Mini Challenge - Food Delivery App

restaurant1 = {"Burger", "Pizza", "Fries", "Pasta"}
restaurant2 = {"Pizza", "Sandwich", "Pasta", "Momos"}

print("Common food items:", restaurant1 & restaurant2)
print("Exclusive items of restaurant1:", restaurant1 - restaurant2)
print("Exclusive items of restaurant2:", restaurant2 - restaurant1)
print("All available food items:", restaurant1 | restaurant2)
print("Food items in only one restaurant:", restaurant1 ^ restaurant2)