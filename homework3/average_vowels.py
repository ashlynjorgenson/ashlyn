# File: average_vowels.py

# You’re curious about the average number of vowels compared to consonants in a paragraph.

# --- 1. Counting Vowels ---
# Write a return function that takes a string as input.
# The function should return a tuple containing:
#     (number of vowels, number of consonants)
# Name this function: counting_vowels_and_consonants()

def counting_vowels_and_consonants(sentence):
    vowels="aeiouAEIOU"
    num_vowels=0
    num_con=0 #set count to 0 to start
    for character in sentence:
        if character.isalpha():
            if character in vowels:
                num_vowels+=1
            else:
                num_con+=1
    
    return(num_vowels, num_con)

print(counting_vowels_and_consonants("Hello, World!"))


# --- 2. Average Vowels ---
# Write a return function that takes in a paragraph (string) as input.
# The function should:
#   - Split the paragraph into individual sentences.
#   - Use counting_vowels_and_consonants() to count values for each sentence.
#   - Return a tuple: (number of sentences, average vowels per sentence, average consonants per sentence)
# Name this function: average_vowels_and_consonants()

def average_vowels_and_consonants(paragraph):
    import re
    sentence=re.split(r'(?<=[.!?])+', paragraph)
    num_sentence=0
    for s in sentence:
        num_sentence+=1
    vowels="aeiouAEIOU"
    num_vowels=0
    num_con=0
    for s in sentence:
        for character in s:
            if character in vowels:
                num_vowels+=1
            else:
                num_con+=1
    if num_sentence==0:
        avg_vowels=0
        avg_con=0
    else:
        avg_vowels_per_sentence=num_vowels/num_sentence
        avg_con_per_sentence=num_con/num_sentence
    
    return(num_sentence, avg_vowels_per_sentence, avg_con_per_sentence)

print(average_vowels_and_consonants("Fall in love with some activity, and do it! "
    "Nobody ever figures out what life is all about, and it doesn't matter. "
    "Explore the world. "
    "Nearly everything is really interesting if you go into it deeply enough. "
    "Work as hard and as much as you want to on the things you like to do the best. "
    "Don't think about what you want to be, but what you want to do. "
    "Keep up some kind of a minimum with other things so that society doesn't stop you from doing anything at all."))  
	

#hint:
# step 1: how to split the paragraph into sentences
# step 2: create a counter for vow and con
# Step 3: loop through sentences
# Step 4: reuse the function from 1
# step 5: take the avg find the total and return
# lookup .strip()
# .split


# Here is your paragraph to analyze. It is a quote from Richard Feynman. 
paragraph = (
    "Fall in love with some activity, and do it! "
    "Nobody ever figures out what life is all about, and it doesn't matter. "
    "Explore the world. "
    "Nearly everything is really interesting if you go into it deeply enough. "
    "Work as hard and as much as you want to on the things you like to do the best. "
    "Don't think about what you want to be, but what you want to do. "
    "Keep up some kind of a minimum with other things so that society doesn't stop you from doing anything at all."
)

# Write descriptive print statements, with f-strings, that output the average vowels and consonants per sentence of the paragraph. 
