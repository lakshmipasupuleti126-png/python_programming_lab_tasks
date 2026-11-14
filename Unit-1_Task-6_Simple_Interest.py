# Read principal, rate and time
p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time in years: "))

# Calculate simple interest
si = (p * r * t) / 100

# Display the result
print("Simple Interest =", si)
