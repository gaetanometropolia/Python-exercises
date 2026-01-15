# Write a program that asks the user to enter a mass in medieval units: talents (leiviskä), pounds (naula), and lots (luoti). The program converts the input to full kilograms and grams and outputs the result to the user:
#
# One talent is 20 pounds.
# One pound is 32 lots.
# One lot is 13,3 grams.
# Example output:
#
# Enter talents:
# 3
#
# Enter pounds:
# 9
#
# Enter lots:
# 13.5
#
# The weight in modern units:
# 29 kilograms and 545.95 grams.


# Conversion constants
POUNDS_PER_TALENT = 20
LOTS_PER_POUND = 32
GRAMS_PER_LOT = 13.3

# User input
talents = float(input("Enter talents:\n"))
pounds = float(input("\nEnter pounds:\n"))
lots = float(input("\nEnter lots:\n"))

# Convert everything to lots
total_lots = (
    talents * POUNDS_PER_TALENT * LOTS_PER_POUND +
    pounds * LOTS_PER_POUND +
    lots
)

# Convert lots to grams
total_grams = total_lots * GRAMS_PER_LOT

# Split into kilograms and grams
kilograms = int(total_grams // 1000)
grams = total_grams % 1000

# Output result
print("\nThe weight in modern units:")
print(f"{kilograms} kilograms and {grams:.2f} grams.")