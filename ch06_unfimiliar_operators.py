# Ch 6 Unfimiliar Operators

# Practicing with Modulo(%), Floor division(//), Exponentiation(**) and Augmented assignments(+=, -=, *=, /=)

print("--- Chapter 6 Unfimiliar Operators ---")

# 1. Modulo operator(%) - Calculating Remainders

print("=======================================")
print("     --- Modulo Operator ---      ")

coins = 6767
chains = 69
left_over = coins % chains

print(f"Coins Bought: {coins}")
print(f"Total Chains: {chains}")
print(f"Extra Coins: {left_over}")

# 2. Floor Division(//) - Calculating without decimal

print("     --- Floor Division ---      ")

items = 670
boxes = 10
items_per_box = items // boxes

print(f"Total items: {items}")
print(f"Box: {boxes}")
print(f"Items per box: {items_per_box}")

# 3. Exponentiation(**) - Calculating powers

print("     --- Exponentiation ---     ")

base = 67
power = 9
result = base ** power

print(f"{base} raised to the power of {power} is {result}")

# 4. Even vs Odd check using Modulo(%)

print("      --- Even vs Odd ---      ")

number = 21
remainder = number % 2

print(f"is {number} Odd? Remainder divided by 2 is: {remainder}")

# 5. Augmented Assignments (+=, -=, *=, /=)

print("      --- Augmented Assigments ---   ")

score = 67
print(f"\nInitial score: {score}")

score += 2
print(f"After Bonus Points: {score}")

score -= 2
print(f"After Penalty: {score}")

score *= 101
print(f"After 101x Multiplier: {score}")