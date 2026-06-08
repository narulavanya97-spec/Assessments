numbers = [30, 10, -45, 5, 20]

# Initialize a variable to store the largest value
maximum = numbers[0]

# Iterate through the list and update the maximum value
for i in numbers:
    if i > maximum:
        maximum = i

# Print the largest value
print("The largest number in the list is:", maximum)
