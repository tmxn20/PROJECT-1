# Ask the user to enter a sentence 
str_manip = input("Write a sentence:")

# Calculate and display the length of str_manip
length = len(str_manip)
print(f"The length of the entered sentence is: {length}")

# Find the last letter in str_manip and replace every occurrence of this letter  with ‘@’
if str_manip:  # Check if the input is not empty
    words = str_manip.split()  # Split the sentence into a list of words
    modified_words = []
    
    for word in words:
        if len(word) > 1:  # If the word has more than one letter
            modified_word = word[:-1] + '@'  # Replace the last letter
        else:
            modified_word = '@'  # If the word has only one letter, replace it with '@'
        modified_words.append(modified_word)
    
    modified_str = " ".join(modified_words)  # Join the words back into a sentence
    print(f"String after replacing the last letter of each word with '@': {modified_str}")
else:
    print("The input string is empty. Cannot process further.")

# Print the last three characters of str_manip backwards
str_manip = str_manip.strip()
if len(str_manip) >= 3:
    last_three_reversed = str_manip[-3:][::-1]
    print(f"The last three characters reversed are: {last_three_reversed}")
else:
    print("The input string is too short for this operation.")

# Print five-letter word that is made up of the first three characters and the last two characters in str_manip.
str_manip = str_manip.strip()
if len(str_manip) >= 5:
    new_word = str_manip[:3] + str_manip[-2:]
    print(f"The new five-letter word is: {new_word}")
else:
    print("The input string is too short to create a five-letter word.")