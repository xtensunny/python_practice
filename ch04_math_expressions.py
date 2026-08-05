# ================================================
# Chapter 4: Math Expressions : Fimiliar Operators
# ================================================

# 1. Variables and Math Expressions
item_price = 67
taxRate = 7
discount = 20

# 2. Math Operations with Variables 
subtotal = item_price - discount
total_tax = subtotal * taxRate / 100
final_price = subtotal + total_tax 


# 3. Standard division always returns to a float
item_count = 2
price_per_item = final_price / item_count


# 4. Output
print("--- Transaction Summary ---")
print("Price:", item_price)
print("Discount:", discount)
print("Subtotal:", subtotal)
print("Tax:", total_tax)
print("Final Total:", final_price)
print("Price Per Item:", price_per_item)