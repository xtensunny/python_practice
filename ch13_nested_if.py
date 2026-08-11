# Chapter 13 if statements nested
print(" --- Chapter 13: Nested if --- ")
print("===============================")

# 1. True
print(" ---True--- ")

is_logged_in = True
account_status = "active"
if is_logged_in:
    if account_status == "active":
        print("Start Battle Royale")
    else:
        print("Account is Banned")
else:
    print("User isn't logged in")



# 2. False
print("\n ---False--- ")

is_logged_in = False
account_status = "active"
if is_logged_in:
    if account_status == "active":
        print("Start Battle Royale")
    else:
        print("Account is Banned")
else:
    print("User isn't logged in")



#  3. Inner else output
print("\n ---Inner else output--- ")

is_logged_in = True
account_status = "banned"
if is_logged_in:
    if account_status == "active":
        print("Start Battle Royale")
    else:
        print("Account is Banned")
else:
    print("User isn't logged in")