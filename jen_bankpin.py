# Week 2 homework: Exercise 10, Parts 2 and 3
# importing getpass package to access getpass module inside it which hides user input (shows blank)
import getpass

# hardcode correct value of user PIN
pin = '7860'

# Getting user PIN in for loop by using getpass module from getpass package and masking user pin with blank

# iterative loop runs three times, from value of integer attempt_getpass = 1 to attempt_getpass =3 (excludes 4)
for attempt_getpass in range(1, 4):
    # assigns the value of pin string provided by user via getpass method to supplied_pin
    # the getpass module from getpass package works fine with any string prompt
    supplied_pin = getpass.getpass(prompt='Please enter your PIN: ')
    # following code checks for condition if user input is equal to hardcoded value of user PIN
    if supplied_pin == pin:
        # if true, print success message and exit the program
        print("Validation Success!")
        break
    else:
        # otherwise print message that input is incorrect and count attempt_getpass
        print(f"Incorrect PIN, you have used {attempt_getpass} attempt(s)\n{3 - attempt_getpass} attempt(s) remaining!")
        # if three wrong attempts have been taken print pin is blocked and exit
        if attempt_getpass == 3:
            print("Your PIN is now blocked!")

# Another way of achieving the same goals by using while loop instead
print('\n2nd Version: Using a while loop')

# The pin_attempts variable stores the max number of pin attempts
pin_attempts = 3

# The correct_pin variable stores an integer, the correct pin to access the bank
correct_pin = 2906

# The security_answer variable stores the correct answer to the security question.
security_answer = 'fluffy'


# function pin_reset was created because this block of code needs to be called twice.
# def defines a function called pin_reset with three parameters
# The pin_reset function will be used to reset correct_pin if the security question is answered correctly
def pin_reset(attempts_parameter, correct_pin_parameter, security_parameter):

    # if the argument passed in the attempts_parameter is equal to 0, execute the next code.
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
        print('Welcome to High Street Bank!')

        # break statement is used to exit a loop
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
