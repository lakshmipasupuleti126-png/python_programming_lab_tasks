# Read principal, rate and time
p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time in years: "))

# Calculate compound interest
amount = p * (1 + r / 100) ** t
ci = amount - p

# Display the result
print("Compound Interest =", ci)
print("Total Amount =", amount)
