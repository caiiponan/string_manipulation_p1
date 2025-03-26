# Prompt user for input (0-1000).
user_input = input("Enter a number between 0 and 1000:  ")

# Check if the input is a number.
    # If not, print an error message.
if not user_input.isdigit():
    print("Error: Please enter a number.")
    # If it is, format the number with zeroes infront of it.
else:
    formatted_number = "0" * (6 - len(user_input)) + user_input
    
# Print the formatted number.