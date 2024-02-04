# Lyrics of the song
# ''' is for multiline string without using \n
lyrics = '''Cause the players gonna play, play, play, play, play
And the haters gonna hate, hate, hate, hate, hate
Baby, I'm just gonna shake, shake, shake, shake, shake
I shake it off, I shake it off'''

# 1. String Slicing
# lyrics.split splits the multi-line string stored in the lyrics variable
# into separate lines using the split() method with the newline character ('\n') as the separator.
# [0] is then used to access the first element (first line) of this list.
first_line = lyrics.split('\n')[0]
print("First Line:", first_line)

# 2. String Formatting
# .replace is a method that replaces the word 'play' with 'always play'
formatted_line = first_line.replace("play", "always play")
print("Formatted Line:", formatted_line)

# 3. F-Strings
# F string combines the second and third words obtained from the split operation
combined_line = f"{lyrics.split(' ')[1]} {lyrics.split(' ')[2]}"
print("Combined Line:", combined_line)

# 4. Split
#  Split a string into a list of substrings based on a specified delimiter
lyrics_words = lyrics.split()
print("Lyrics Split into Words:", lyrics_words)

# 5. Join
# concatenate elements into a single string
joined_lyrics = ' '.join(lyrics_words)
print("Lyrics Joined into a String:", joined_lyrics)

# 6. String Length
# calculate the length of the lyrics string, including whitespace and punctuation
lyrics_length = len(lyrics)
print("Length of Lyrics:", lyrics_length)

# 7. Upper Case
# .upper() converts all characters in the lyrics string to uppercase letters
upper_lyrics = lyrics.upper()
print("Lyrics in Upper Case:", upper_lyrics)

# 8. Lower Case
# lower() method is used to convert all characters in a string to lowercase
lower_lyrics = lyrics.lower()
print("Lyrics in Lower Case:", lower_lyrics)

# 9. Replace : The replace() method is used to replace occurrences of a substring within a string with another
# substring. In this case, lyrics.replace("shake", "dance") replaces all occurrences of the substring "shake" with
# "dance" in the lyrics string.
replaced_lyrics = lyrics.replace("shake", "dance")
print("Replaced Lyrics:", replaced_lyrics)

# 10. Count
# lyrics.count("shake") counts the number of times the substring "shake" appears in the lyrics string.
shake_count = lyrics.count("shake")
print("Number of 'shake' in Lyrics:", shake_count)
