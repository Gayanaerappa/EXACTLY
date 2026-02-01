total = 0

print("Enter grocery item prices (enter 0 to stop)")

while True:
    price = float(input("Enter item price: "))
    
    if price == 0:
        break
    
    total = total + price

print("Total Bill:", total)

# Discount rules
if total >= 2000:
    discount = total * 0.10      # 10%
elif total >= 1000:
    discount = total * 0.05      # 5%
else:
    discount = 0

final_amount = total - discount

print("Discount:", discount)
print("Final Amount to Pay:", final_amount)