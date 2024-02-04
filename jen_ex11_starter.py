# Jen - Exercise 11 - String Handling

# Stored a string of info in Belgium variable
Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

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