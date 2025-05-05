# Task 1: Friends' names and name lengths
friends = ["Alice", "Bob", "Charlie", "David", "Eve"]
name_length_tuples = [(name, len(name)) for name in friends]
print("Friends and their name lengths:")
print(name_length_tuples)
print()

# Task 2: Trip expenses comparison (modified to ensure significant differences)
your_expenses = {
    "Hotel": 1500,  # Increased to create significant difference
    "Food": 800,
    "Transportation": 200,  # Decreased to create significant difference
    "Attractions": 300,
    "Miscellaneous": 200
}

partner_expenses = {
    "Hotel": 1000,
    "Food": 900,
    "Transportation": 600,
    "Attractions": 400,
    "Miscellaneous": 150
}

# Calculate total expenses
your_total = sum(your_expenses.values())
partner_total = sum(partner_expenses.values())

print(f"Your total expenses: ${your_total}")
print(f"Partner's total expenses: ${partner_total}")

# Determine who spent more
if your_total > partner_total:
    print("You spent more money overall.")
elif partner_total > your_total:
    print("Your partner spent more money overall.")
else:
    print("You and your partner spent the same amount overall.")

# Find category with significant difference (difference > 200)
significant_differences = []
for category in your_expenses:
    difference = abs(your_expenses[category] - partner_expenses[category])
    if difference > 200:
        significant_differences.append((category, difference))

print("\nCategories with significant spending differences (> $200):")
if significant_differences:
    for category, difference in significant_differences:
        print(f"{category}: ${difference} difference")
else:
    print("No categories with spending differences > $200")
