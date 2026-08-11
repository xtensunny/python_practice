# Chapter 12 Sets of Conditions
print(" --- Chapter 12: Sets of Conditions --- ")

# 1. Strict and Check
print("\n ---and--- ")

player_level = 67
inventory_count = 12
if player_level >= 50 and inventory_count >= 10:
    print("Welcome to EWC 2026")


# 2. Flexible or Check 
print("\n ---or--- ")

premium_membership = "NO"
promo_code = "Not Valid"
if premium_membership == "YES" or promo_code == "Valid":
    print("Eligible for Discount")


# 3. Grouped Logic with Parentheses()
print("\n ---and + or with ()--- ")

status = "Admin"
rank_points = 1700
server_status = "online"
if (status == "Admin" or rank_points >= 1500) and server_status == "online":
    print("Qualified for EWC")