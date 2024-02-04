# Jen - Pub Quiz Program - String slicing, string formatting, f strings, split(), splitlines() and join

# Assigned the integer 0 to variable, score
score = 0

# The unicode for a music note is assigned to the variable, music_note
music = '\u2669'

# Created two variables to store the strings of the 1st question and choices
question_one = 'Who is the artist of the song, Summer of \'69?\n'
question_one_choices = 'A: Bon Jovi/B: Madonna/C: Bryan Adams'

# Prints an f string, formatted string literals. It allows me to embed variables directly into a string
# Concatenates a strings and the strings in variables, music and question_one, on new lines \n
print(f'Welcome to the Pub Quiz!\nQUESTION ONE:\n\n{music} {question_one}')

# split() method converts question_one_choices to a list of items separated by / with a max index of 2
# Each item will be assigned to abc_answers as it iterates
for abc_answers in question_one_choices.split('/', 2):

    # Prints each possible answer to the question with a tab \t
    print('\t', abc_answers)

# Requests input from the player and capitalises the answer in case it is lower case
# Stores the player's answer in user_input_one variable
user_input_one = input('\nAnswer with a letter: ').capitalize()

# The correct answer to question one is assigned to correct_answer variable
correct_answer = 'C'

# if the correct_answer string is the same as the user_input_one string, execute the next code
if correct_answer == user_input_one:

    # Prints a string to inform the player of scoring a point
    print('You are correct, 1 point! The artist is Bryan Adams.\n')

    # Adds 1 to the integer in the score variable and assigns the new value to the variable
    score += 1

# if the correct_answer string is NOT the same as the user_input_one string, execute the next code
else:

    # Prints a string to inform the player of not scoring a point
    print('Sorry, you didn\'t score a point.\n')

# QUESTION 2--------------------------------------------------------------

# Created a string of lyrics and stored them in the lyrics variable
lyrics = ('''All my troubles seemed so far away
Now it looks as though they're here to stay
Oh, I believe in yesterday''')

# slicing the correct answers from the lyrics, based on character count, then storing a tuple to a variable
correct_answers = (lyrics[7:15], lyrics[-9:])

# lyrics variable is split by each line and converted to a list
# enumerate() gives an index number for each item in the list
for index_lyrics, lyrics_line in enumerate(lyrics.splitlines()):

    # if index_lyrics is equal to 0, execute the next code
    if index_lyrics == 0:

        # replace() method replaces the word, troubles, in the lyrics with underscores before printing
        # The underscore string is multiplied by 8 to be the same character length as the word
        # Strings are concatenated with the music unicode and updated lyrics line
        print('QUESTION TWO:\n\n\t', music, lyrics_line.replace('troubles', '_' * 8))

    # if index_lyrics is equal to 1, execute the next code
    elif index_lyrics == 1:

        # Prints the second line of the lyrics with a tab \t and music unicode
        print('\t', music, lyrics_line)

    # if index_lyrics is NOT equal to 0 or 1, execute the next code
    else:

        # The word, yesterday, is replaced with underscores on this lyrics line with the same character length
        # Prints the updated line with a tab \t, music unicode and a new line at the end \n
        print('\t', music, lyrics_line.replace('yesterday', '_' * 9), '\n')

# Requests two answers with a space in between
user_input_two = input('What are the missing lyrics?\nEnter two answers:').lower()

# split() method default splits every time there is a space and creates a list
# The two answers of the player are stored as a list in the answers variable
answers = user_input_two.split()

# while the length of answers is NOT equal to two, like the player entered 1 or 3 answers, keep executing this code
while len(answers) != 2:

    # Requests the player to enter two answers
    # lower() method converts the answers to lowercase for comparison later and stores it in user_input_two variable
    user_input_two = input('Enter only TWO answers:').lower()

    # the players answers are split() into a list again and reassigned to the answers variable
    answers = user_input_two.split()

# if answers, a list, are the same as correct_answers, a tuple, execute the next code
# Comparing the tuple sliced from the lyrics and list of the players' two answers
if answers[0] == correct_answers[0] and answers[1] == correct_answers[1]:

    # Prints a string to inform the player they got both answers correct
    print(f"Your answers '{answers[0]}' and '{answers[1]}' are correct, 2 points!")

    # Adds 2 to the integer in the score variable and assigns the new value to the variable
    score += 2

# if only ONE of the player's answers are the same as correct_answers, execute the next code
elif answers[0] == correct_answers[0] or answers[1] == correct_answers[1]:

    # Prints a string to inform the player they got ONE answer correct
    print('One answer is correct. Scored 1 point!')

    # Adds 1 to the integer in the score variable and assigns the new value to the variable
    score += 1

# if NONE of the player's answers are correct, execute the next code
else:

    # Prints a string to inform the player they got both answers incorrect
    print("No points! Both answers are incorrect.")

# QUESTION THREE ----------------------------------------------------------------

# Prints a string of the 3rd question on new lines \n using an f string
print(f'\nQUESTION THREE:\n\nThe Gulliver\'s Travels movie was released in 2010.'
      f'\nHow many years earlier had the book been released?')

# Asks player for an integer of years
# strip() method removes any white space to compare their answer later
# Player's answer is stored in user_input_three variable
user_input_three = input('\nHow many years:').strip()

# while the string in user_input_three are NOT numbers, execute this code.
while not user_input_three.isdecimal():

    # The player's input keeps being requested until only numbers are entered
    # Each time they answer, user_input_three is updated with a new value
    user_input_three = input('Type numbers for years only:')

# user_input_three is converted to an integer and reassigned to user_input_three
user_input_three = int(user_input_three)

# A dictionary is created about Gulliver's Travels and the player's answer
gulliver_dict = {'Movie': 2010, 'Book': 1726, 'Years Apart': 284, 'Your Answer': user_input_three}

# keys() method returns each key in gulliver_dict, stores it in key_gulliver during each iteration
# enumerate() function returns the index of each, starting from 1 when it prints, and stores it in index_gulliver
for index_gulliver, key_gulliver in enumerate(gulliver_dict.keys(), 1):

    # Prints the index, key and value of gulliver_dict in a specific format
    # Format: 1d is for one digit, <20s is at least 20 characters in the string, 4d is four digits
    print('{:1d} {:<20s} {:4d}'.format(index_gulliver, key_gulliver, gulliver_dict[key_gulliver]))

# if the value in gulliver_dict['Years Apart'] is NOT the same as gulliver_dict['Your Answer'], execute this code
if gulliver_dict['Years Apart'] != gulliver_dict['Your Answer']:

    # Prints a string to inform the player of their wrong answer.
    print('\nSorry, wrong answer. No points!')

# if the value in gulliver_dict['Years Apart'] is the SAME as gulliver_dict['Your Answer'], execute this code
else:

    # Prints a string to inform the player of scoring the final point
    print('\nCorrect answer! Scored the final point')

    # Adds 1 to the integer in the score variable and assigns the new value to the variable
    score += 1

# Prints an integer of the Total Score, score variable, and a string thanking the player
print(f'\nTotal Score: {score}\nThanks for playing!')

# Creates a list of all the answers the player entered
# The third player's answer is converted to a string str()
# The list is stored in the variable, all_answers_list
all_answers_list = [user_input_one, user_input_two, str(user_input_three)]

# join() method concatenates the strings in all_answers_list and separates them with a new line \n
# Prints a string of all the answers the player entered during the game
print('\nAll your answers:\n', '\n'.join(all_answers_list))
