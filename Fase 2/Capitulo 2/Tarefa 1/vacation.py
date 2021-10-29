# Get total cost of vacation package
package = float(input("Total cost of package: $"))

# Get type of sitting in the airplane
sitting = ""
while not (sitting == "economic" or sitting == "executive" or sitting == "first"):
    sitting = input("Economic, executive or first?: ").lower()

# Get numver of Travelers 
travelers = int(input("Number of people traveling: "))

# Find out discount_percent amount
discount_percent = 0
if sitting == "economic":
    if travelers == 2:
        discount_percent = 3
    elif travelers == 3:
        discount_percent = 4
    elif travelers >= 4:
        discount_percent = 5
    else:
        discount_percent = 0

elif sitting == "executive":
    if travelers == 2:
        discount_percent = 5
    elif travelers == 3:
        discount_percent = 7
    elif travelers >= 4:
        discount_percent = 8
    else:
        discount_percent = 0

elif sitting == "first":
    if travelers == 2:
        discount_percent = 10
    elif travelers == 3:
        discount_percent = 15
    elif travelers >= 4:
        discount_percent = 20
    else:
        discount_percent = 0

# Calculate package with discount_percent
discount=  (package / 100) * discount_percent
new_package = package - discount

# Calculate price per person
per_person = new_package / travelers

# Helper function to transform values into USD
def usd(value):
    return f"${value:,.2f}"

# Print results
print(f"Your package of {usd(package)} is eligible for a {discount_percent}% discount({usd(discount)}). The new price is {usd(new_package)} which is {usd(per_person)} per person.")
