#Timed practice problems from pyschools.

#Write the function countA(word) that takes in a word as argument and returns the number of 'a' in that word.
def countA(word):
    count = 0
    for letter in word:
        if letter == 'a':
            count += 1
    return count

print countA("Banana")
print countA("Apple")
print countA("Banana")

"""
6:49 - First I thought I could use a simple if statement to count the # of 'a's in the word (below). I didn't know why
it wasn't working so I just moved on and made a for loop. Now that I'm writing this, I realize that writing an if statement
just counts the letter 'a' once and ends, instead of a for loop that goes through each letter.

def countA(word):
    count = 0
    if 'a' in word:
        count += 1
        return count

print countA("Banana")
print countA("Apple")
print countA("Banana")
"""

#Write the function countLetter(word, letter) that takes in a word and a letter as arguments and returns the number of
# occurrence of that letter in the word.

def countLetter(word, letter):
    count = 0
    for letters in word:
        if letters == letter:
            count += 1
    return count

print countLetter("apple", "p")
print countLetter("Apple", "a")
print countLetter("Banana", "n")

"""
2:29 - since this is building off of the above problem, was easier to figure out, although I did mess up on the formatting
at first, I fixed it (I placed thed count under the for loop instead of outside). I guess the only issue or "advantage" I
have with writing in PyCharm is I can do a guess and check... because I "run" my program before I submit my answer. This
worries me as I recall you saying you guys use a white/blackboard in interviews?
"""

#Write a function removeLetter(word, letter) that takes in a word and a letter as arguments and remove all the occurrence
# of that particular letter from the word. The function will returns the remaining leters in the word.

def removeLetter(word,letter):
    new_word = word.replace(letter,'')
    return new_word

print removeLetter("apple", "p")
print removeLetter('google', 'g')
print removeLetter('microsoft', 'o')

"""
5:46 - At first I thought I needed to use a for loop, but after trying to work it through my head on how to remove the
letter from the word, I realized I didn't know how so I checked on PyCharm to see what methods I could use on objects.
Luckily I tested the .replace method and it worked. Again, I think I'm screwed if I don't rememember these methods. I'm
writing these on a cheat sheet now.
"""

#Write the function changeCase(word) that changes the case of all the letters in a word and returns the new word.

def changeCase(word):
        return word.swapcase()

print changeCase('aPPle')
print changeCase('BaNaNa')

"""
6:33 - I originally read the question wrong, thought I was suppose to just change the capitalized letter to lower case.
Which is stupid becuase that just means change everything lower case... after putting in my original code and getting the
wrong results, I went for a for_loop. That didn't bode well as I was trying to add the string index together of the letters
I capitalized/lower cased. I then decided to see if there was a method in PyCharm... apparently there is... It's on my
cheat sheet now.
"""

#Write the function search(word, substring) that takes in a word and a substring as arguments and returns the position
# (0 indexed) of the substring if it is found in the word. The function returns -1 if the substring is not found.

def search(word, substring):
    return word.find(substring)

search("apple", 'p')
search("google", 'apple')
search("google", 'p')
search("google", 'oo')

"""
1:30 - Thought maybe there was a built-in method already. I searched for it using word.find and I saw "substring".
"""

#A string contains a sequence of characters. Elements within a string can be accessed using index that starts from 0.
# Write the function getChar(word, pos) that takes in a word and a number as argument and returns the character at that
# position.

def getChar(word, pos):
    if len(word) < pos:
        return 'Invalid Range'
    else:
        return word[pos]

print getChar("apple", 2)
print getChar("google", 0)
print getChar("google", 10)

"""
5:49  - I got word[pos] in like 10 seconds, but was trying to figure out why getChar("google", 10) returned 'Invalid Range'.
Finally figured it out that it just wanted to use an if/else.
"""

#Write a function countVowels(word) that takes in a word as an argument and returns the number of vowels
# ('a', 'e', 'i', 'o', 'u') in the word.

def countVowels(word):
    count = 0
    for letters in word:
        if letters == 'a' or letters == 'e' or letters == 'i' or letters == 'o' or letters == 'u':
            count += 1
    return count

print countVowels('apple')
print countVowels('microsoft')
print countVowels('google')

"""
2:35 - This one was easy. Would have been faster, but was trying to see if I could combine aeiou in a shorter boolean.
I just gave up and used the long way.
"""

#Write the function getVowels(word) that takes in a word as an argument and returns the vowels ('a', 'e', 'i', 'o', 'u')
# in that word.

def getVowels(word):
    vowels = []
    for letters in word:
        if letters == 'a' or letters == 'e' or letters == 'i' or letters == 'o' or letters == 'u' or letters == 'A':
            vowels.append(letters)
    return vowels

print getVowels("apple")
print getVowels("Apple")
print getVowels("Banana")

"""
9:02 - I knew I needed to use a for loop for this, but got stuck when it just returned letters. Finally I realized I needed
to make a list and append the vowels to it.

decided to look up how to shorten my booleans... remade the function.

def getVowels(word):
    vowels_letters = 'AEIOUaeiou'
    vowels_list = []
    for letters in word:
        if letters in vowels_letters:
            vowels_list.append(letters)
    return vowels_list
"""

#Write the function capitalizeVowels(word) that returns the word with all the vowels capitalized

def capitalizeVowels(word):
    for letters in word:
        vowels = 'aeiou'
        if letters in vowels:
            word = word.replace(letters, letters.upper())
    return word

print capitalizeVowels('apple')
print capitalizeVowels('google')

"""
40+ minutes... Got frustrated with the below code that I made so I cheated and went to go look for the answer. Apparently,
setting up a new object 'new_word' instead of using the original object, 'word', the loop cancels out any changes and just
returns the final loop. I think I got most of the code correctly in 6 minutes, but spent the remaining time trying to figure
out why it didn't work...

def capitalizeVowels(word):
    new_word = ''
    for letters in word:
        vowels = 'aeiou'
        if letters in vowels:
            new_word = word.replace(letters, letters.upper())
"""

#Write the function startEndVowels(word) that returns True if the word starts and ends with vowels.

def startEndVowels(word):
    vowels = 'aeiouAEIOU'
    while len(word) > 0:
        if word[0] in vowels and word[-1] in vowels:
            return True
        else:
            return False
    else:
        return False

print startEndVowels('A')
print startEndVowels('')
print startEndVowels('apple')
print startEndVowels('google')

"""
10:00 - started with an if statement, but then realized I needed a while loop because of the empty '' word. 10 minutes
goes by fast for such an easy problem...
"""

#Write the function removeVowels(word) that removes all the vowels ('a', 'e', 'i', 'o', 'u') in a word and returns the
# remaining letters in the word.

def removeVowels(word):
    vowels = 'aeiouAEIOU'
    for letters in word:
        if letters in vowels:
            word = word.replace(letters,'')
    return word

print removeVowels('apple')
print removeVowels('Apple')
print removeVowels('Banana')

"""
2:12 - Was easy to figure out from the previous 40 minute problem I worked on.

