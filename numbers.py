# Task 1: Format function with two arguments
def format_numbers(num, char):
    formatted_string = "First argument: {0}, Second argument: {1}".format(num, char)
    print("\n1. Formatted string:", formatted_string)
    print("Representation used: positional formatting with str.format() method")

format_numbers(145, 'o')

# Task 2: Calculate pond area and water volume
radius = 84
pi = 3.14

# Calculate area
pond_area = pi * radius ** 2
print("\n2. Area of the pond:", pond_area, "square meters")

# Bonus: Calculate total water (1.4 liters per square meter)
water_per_sqm = 1.4
total_water = pond_area * water_per_sqm
print("Total water in the pond:", int(total_water), "liters (without decimals)")

# Task 3: Calculate speed
distance = 490  # meters
time_minutes = 7

# Convert time to seconds
time_seconds = time_minutes * 60

# Calculate speed
speed = distance / time_seconds
print("\n3. Speed:", int(speed), "meters per second (without decimals)")
