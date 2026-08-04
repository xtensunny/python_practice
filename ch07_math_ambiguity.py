# Chapter 7 Math Ambiguity

print(" --- Chapter 7 Math Ambiguity --- ")
print("\n================================")
# Scenario 1. Debit card's international transactions calculation as a non filer
tekken8_cost = 30000
discount = 3000
tax_rate = 0.10   # 10% tax rate

print(f"\nTekken 8 price: {tekken8_cost}")
print(f"Discount: {discount}")
print(f"Tax Rate: {tax_rate}")
print("\n --- Wrong Logic --- ")

# Wrong LOgic - without parentheses
wrong_price = tekken8_cost - discount * 1 + tax_rate
print(f"Wrong price: {wrong_price}")

print("\n --- Correct Logic --- ")

# Correct Logic - Using Parentheses
correct_price = (tekken8_cost - discount) * ( 1 + tax_rate)
print(f"Correct price: {correct_price}")

print("\n --- Nested Parentheses Execution --- ")

# Scenario 2. Nested Parentheses Execution
complex_result = ((6767 // 101) + 2)  ** 10 * 27.665991650300627

''' step 1: (6767 // 101) = 67
    step 2: (67 + 2) = 69
    step 3: 69 ** 10 = 2,446,194,060,654,759,801
    step 4: 2,446,194,060,654,759,801 * 27.665991650300627 = 67
    '''

print(f"Complex Problem: {complex_result}")