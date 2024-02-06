# Jen - Improved Bank Pin Program - Week 3 Homework
# importing getpass package to access getpass module inside it which hides user input (shows blank)
import getpass

# Prints a string to welcome the user
print('\nAccess your Bank Account.')

# The pin_attempts variable stores the maximum number of pin attempts
pin_attempts = 3

# The correct_pin variable stores an integer, the correct pin to access the bank
correct_pin = 2906

# The security_answer variable stores the correct answer to the security question.
security_answer = 'fluffy'


# function pin_reset was created because this block of code needs to be called twice.
# def defines a function called pin_reset with three parameters
# The pin_reset function will be used to reset correct_pin if the security question is answered correctly
def pin_reset(attempts_parameter, correct_pin_parameter, security_parameter):

    # if the argument passed in the attempts_parameter is equal to 0, no more attempts, execute the next code.
    if attempts_parameter == 0:

        # Prints a string to inform the user of failed attempts and ask the security question.
        print('All attempts failed. Reset pin by answering this security question.\nWhat is your first pet\'s name?')

        # input() function requests an answer and stores it as a string in the user_answer variable
        user_answer = input('Enter answer here: ')

        # if the strings in security_answer is the same as user_answer, execute the next code.
        if security_parameter == user_answer:

            # getpass.getpass() function securely takes the input of a new pin without displaying it on screen.
            # int() function converts the input string into an integer.
            # The new pin is stored in the variable, new_pin.
            new_pin = int(getpass.getpass('Enter NEW pin: '))

            # Add 3 to attempts_parameter and store the new value in new_attempts.
            # This wil reset the max pin attempts and allow the user to try again with their new pin.
            new_attempts = 3

            # return is used to return two values, an immutable tuple, from this function
            # These values will be used in the variables, correct_pin and pin_attempts later
            return new_pin, new_attempts

        # if the strings in security_answer and user_answer are NOT the same, execute the next code.
        else:
            # Informs the user that security is being called due to suspicious activity
            print('Answer incorrect: Calling security...')

    # Returns the existing values if the reset condition is not met
    return correct_pin_parameter, attempts_parameter


# The while loop will keep executing this block of code until the pin_attempts variable is 0
while pin_attempts > 0:

    # Used the str() function to convert correct_pin into a string
    correct_string = str(correct_pin)

    # The getpass.getpass() function securely takes input without displaying it on screen
    # The input is stored in the supplied_pin variable
    supplied_pin = getpass.getpass('Enter your pin: ')

    # If the strings in supplied_pin is equal to the correct_pin, execute the next code
    if supplied_pin == correct_string:

        # Prints a string to indicate the user has entered their pin successfully
        print('Welcome to High Street Bank!\n')

        # Created a dictionary of account details and assigned it to the account variable
        account = {'Name': 'Jane Doe', 'Account Number': 90653876, 'Funds': 5678}

        # enumerate() function returns the index, starting at 1, and a tuple of each dictionary item
        # The index, keys and values are unpacked and assigned to three variables during each iteration
        for index_account, (key_account, value_account) in enumerate(account.items(), 1):

            # isinstance() method checks if each value in the dictionary is a string
            # If it's a string, then the format {:8s} is stored in the value_format variable
            if isinstance(value_account, str):
                value_format = '{:>8s}'

            # If it is NOT a string, and it's key is 'Funds' then pounds unicode and {:7,d} format is stored in variable
            elif key_account == 'Funds':
                value_format = '\u00A3{:>7,d}'

            # If it is NOT a string, and it's key is NOT 'Funds' then {:8} format is stored in the variable
            else:
                value_format = '{:>8}'

            # Prints the index, keys and values of the account dictionary using formatting specifiers
            # format() method is used twice, one for formatting the placeholders
            # and another for formatting the string/integer values
            print('{:1d} {:20s} {}'.format(index_account, key_account, value_format.format(value_account)))
        # break statement is used to exit a loop

        # Prompting the user to input whether they want to make a withdrawal and converting the input to lowercase
        withdrawal_answer = input('Withdrawal? (yes/no): ').lower()
        # Checking if the user wants to make a withdrawal
        if withdrawal_answer == 'yes':
            # If yes, prompting the user to input the withdrawal amount
            withdrawal_amount = float(input('Enter withdrawal amount: '))
            # Checking if the withdrawal amount is less than or equal to the available funds
            if withdrawal_amount <= account['Funds']:
                # If the withdrawal amount is valid, deducting it from the account's funds and displaying the
                # remaining funds
                account['Funds'] -= withdrawal_amount
                print('Withdrawal successful. Remaining funds: \u00A3{:,.2f}'.format(account['Funds']))
            else:
                # If the withdrawal amount exceeds the available funds, informing the user of insufficient funds
                print('Insufficient funds.')
        else:
            # If the user does not want to make a withdrawal, informing them and displaying the remaining funds
            print('No withdrawal made. Remaining funds: \u00A3{:,.2f}'.format(account['Funds']))
        # Exiting the loop after handling the withdrawal or informing the user of no withdrawal
        break

    # If supplied_pin is NOT equal to the correct_pin, execute the next code
    else:
        # != checks if the length of characters in supplied_pin is NOT equal to correct_string
        # != is a comparison and boolean operator, returns True or False
        # .isnumeric() is a method that checks if a string contains only numeric characters, returns True or False
        # 'not' negates the truth value, it checks if supplied_pin is NOT only numeric characters
        # 'or' means, if either statements are True, execute the next code
        if len(supplied_pin) != len(correct_string) or not supplied_pin.isnumeric():

            # Subtract 1 from pin_attempts value and store the new value in that variable.
            pin_attempts -= 1

            # Prints a string and integer to inform the user how many digits is required and pin attempts left.
            print('Pin needs to be 4 digits. You have', pin_attempts, 'attempts left')

            # Calls the function pin_reset and unpacks the returned values in correct_pin and pin_attempts
            correct_pin, pin_attempts = pin_reset(pin_attempts, correct_pin, security_answer)

        # if either of the previous if statements are NOT True, execute the next code
        else:
            # Subtracts 1 from pin_attempts then assigns the new value to the pin_attempts variable
            pin_attempts -= 1

            # Prints a string to indicate the user input the wrong pin and how many attempts left.
            print('Incorrect pin. You have', pin_attempts, 'attempts left')

            # Calls the function pin_reset and unpacks the returned values in correct_pin and pin_attempts
            correct_pin, pin_attempts = pin_reset(pin_attempts, correct_pin, security_answer)
            