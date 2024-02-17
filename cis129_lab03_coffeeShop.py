# Coffee Shop Simulator

TAX = .06

# INPUT
# Ask for number of coffee and muffins
num_coffee = int(input("How many coffees do you want? "))
num_muffin = int(input("How many muffins do you want? "))

# PROCESSING
# Price of coffee is $5 and muffin is $4. And 6% tax on the subtotal
money_coffee = num_coffee * 5
money_muffin = num_muffin * 4
money_tax = (money_coffee + money_muffin) * TAX
money_total = money_coffee + money_muffin + money_tax

# OUTPUT
print("\n\n***************************************")
print("My Coffee and Muffin Shop")
print("Number of coffees bought?")
print(num_coffee)
print("Number of muffins bought?")
print(num_muffin)
print("***************************************\n")

print("***************************************")
print("My Coffee and Muffin Shop Receipt")
print(str(num_coffee) + " Coffee at $5 each: $ " + str(money_coffee))
print(str(num_muffin) + " Muffins at $4 each: $ " + str(money_muffin))
print("6% tax: $ " + str(money_tax))
print("---------")
print("Total: $ " + str(money_total))
print("***************************************")

