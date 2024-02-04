import getpass

# Hard-coded correct PIN
# set the correct pin by passing the value 1234 to variable correct_pin
correct_pin = "1234"

# Maximum number of attempts
# This will compare the attempt value with this max number.
# This is a variable and can be altered
max_attempts = 3

# Initialize attempt counter
attempts = 0

# Loop to take input, count number of attempts (ensure fewer than max) and check PIN
while attempts < max_attempts:
    # Prompt for PIN input
    entered_pin = getpass.getpass("Enter your 4-digit PIN: ")
    # Added one more if statement for when the attempt is less than max_attempt
    # This if statement will print a warning if supplied_pin is not equal to 4
    if len(entered_pin) != 4:
        print("Please enter a valid 4-digit number.")
    # Check if entered PIN matches correct PIN
    if entered_pin == correct_pin:
        # you can add other conditions e.g. ..and entered_pin.isdigit() and len(entered_pin) == 4
        print("Success! PIN accepted.")
        break  # Exit loop on success
    else:
        attempts = attempts + 1
        remaining_attempts = max_attempts - attempts
        print("Incorrect PIN. Please try again. Attempts remaining:", remaining_attempts)
# This adds one to the current attempt
# you take the number of attempts + 1 from the max attempts to get the remaining attempts
# Check if maximum attempts reached, if it is attempt 3 then show this following message
if attempts == max_attempts:
    print("You have exceeded the maximum number of attempts. Access denied.")


# Another method:

# for attempt in range(max_attempts):  # Ask the user to supply the PIN
#     supplied_pin = input("Please enter your PIN: ")
#     if supplied_pin == correct_pin:  # Check if the supplied PIN matches the correct PIN
#         print("PIN verification successful")
#         break
#     else:
#         attempts_remaining = max_attempts - attempt - 1
#     if attempts_remaining > 0:
#         print(f"Incorrect PIN. {attempts_remaining} attempts remaining.")
#     else:
#         print("No remaining attempts. Access denied.")

# Instead of remaining attempts = max - (attempts+1), the above code subtracts 1 from max minus attempts



