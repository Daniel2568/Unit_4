'''
Lab 4.01


#Remove the Vowels
# Create a function, de_vowel, which will take a string as input and return a copy of that string with all the vowels removed. Otherwise, the string should be the same. 'Y' does not count as a vowel for the purposes of this function.

Create the function contract for de_vowel.

Write de_vowel using a for loop

Provide a few examples that confirm de_vowel works as expected:

What if the string is all vowels?

What if there are no vowels?

What if there is a mix of vowels and non-vowels and spaces?

What if some vowels are capitalized, e.g., the first letter in a sentence?

Example
Example of the file:

    # contract goes here
    def de_vowel(a_string):
        # your code goes here
    no_vowels = de_vowel("This sentence has no vowels")
    print(no_vowels)
    # examples go here
Example output:

    >>> python3 de_vowel_lab.py
    Ths sntnc hs n vwls
Bonus
Use a counter (variable you define outside of a loop to keep track of a value inside a loop) to create a function count_vowels.

count_vowels takes in a string and returns an int representing the number of vowels in the string.

Can you think of an alternate way to do complete this task without any loop or counter, by making use of your new de_vowel() function instead?
'''
#list of vowels
vowels = 'aeiou'

#removes the vowels in a string
def de_vowel(string):
    no_vowels = ''
    for letter in string:
        if letter not in vowels:
            no_vowels += letter


            return no_vowels

#counts how many vowels are in the string
def count_vowels(string):
    count = 0
    for letter in string:
        if letter in vowels:
            count += 1

            return count

#prints the count and the devoweled string
new_string = input("Enter a string to devowel:")
print()
print(f"There are {count_vowels(new_string)} vowels in string")
print()
print(f"Your devoweled string is: {de_vowel(new_string)}")
print()
