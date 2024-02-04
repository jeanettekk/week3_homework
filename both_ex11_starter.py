#!/usr/bin/python

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

# a) Print a line of hyphens the same length as the Belgium string '-' * len(Belgium): This part calculates a string
# composed of hyphens ('-') repeated a certain number of times. The number of times the hyphen is repeated is
# determined by the length of the string stored in the variable Belgium
print('-' * len(Belgium))

# b) Replace comma separators with colons ':' and print the string .replace(',', ':'):
# This part of the expression calls the replace() method on the string stored in Belgium.
# The replace() method takes two arguments: the substring to be replaced and the substring to replace it with.
# In this case, it replaces every comma (',') with a colon (':').
formatted_belgium = Belgium.replace(',',':')
print(formatted_belgium)

# c) Extract population fields and calculate the total population
# Extracts the population numbers for Belgium and Brussels from the Belgium string by splitting the string
# using commas as separators (Belgium.split(','))
# The population numbers for Belgium and Brussels are retrieved using indexing ([1] for Belgium and [3] for Brussels).
# These values are then converted to integers using the int() function.
population_belgium = int(Belgium.split(',')[1])
population_brussels = int(Belgium.split(',')[3])
total_population = population_belgium + population_brussels
print("Total Population (Belgium + Brussels):", total_population)

# Jen - Exercise 11 - String Handling

# len() function returns length of characters in Belgium variable
# The character length is stored as an integer, 81, in character_length variable
character_length = len(Belgium)

# Concatenated a string of hyphens, length is determined by value in character_length
hyphens = '-' * character_length

# split() method converts the string in Belgium variable to a list
# Separating the items in the list by each comma
# The new list is assigned to a variable, belgium_list
belgium_list = Belgium.split(',')

# A string of hyphens are printed first
# replace() method changes commas to colons in Belgium string and \n prints it on a new line
# The values of belgium_list, index [1] and [3], are unpacked, int() method converts them to integers
# The converted integers are added together and printed on a \n new line
print(hyphens, '\n', Belgium.replace(',', ':'), '\n', int(belgium_list[1]) + int(belgium_list[3]))