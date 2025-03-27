# Prompt user for input.
name = input("Enter your full name with incorrect casing:  ")

# Convert into pascal case using title() and replace() methods.
pascal_case = name.title().replace(" ", "")

# Print the new input.
print(pascal_case)