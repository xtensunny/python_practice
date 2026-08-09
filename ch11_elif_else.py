# Chapter 11 elif/else
print(" --- Chapter 9: if/elif/else --- ")

# 1. if/else
print("\n ---if/else--- ")
coin_bought = "no"
if coin_bought == "yes":
    print("Assets in the wallet")
else:
    print("Wallet is empty")


# 2. if/elif
print("\n ---if/elif--- ")
elo = 2500
if elo >= 2500:
    print("Grandmaster")
elif elo < 2500:   # rebundant just to see how it works
    print("Not Grandmaster")


# 3. if/elif/else
print("\n ---if/elif/else--- ")
total = 10000
if total >= 10000:
    discount = total * 0.80
elif total >= 5000:
    discount = total * 0.90
else:
    discount = total
print(f"Total Amount: {discount}")