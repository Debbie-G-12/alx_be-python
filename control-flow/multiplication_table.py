# multiplication_table.py
# Get a number from the user.
number = int(input("Enter a number to see its multiplication table: "))

# Use a for loop to iterate from 1 to 10.
for i in range(1, 11):
    # Print the multiplication equation and its result.
    print(number, "*", i, "=", number * i)
