#Timed practice problems from pyschools.

#All string problems
#1 - Write the function countA(word) that takes in a word as argument and returns the number of 'a' in that word.
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

#2 - Write the function countLetter(word, letter) that takes in a word and a letter as arguments and returns the number of
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

#3 - Write a function removeLetter(word, letter) that takes in a word and a letter as arguments and remove all the occurrence
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

#4 - Write the function changeCase(word) that changes the case of all the letters in a word and returns the new word.

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

#5 - Write the function search(word, substring) that takes in a word and a substring as arguments and returns the position
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

#6 - A string contains a sequence of characters. Elements within a string can be accessed using index that starts from 0.
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

#7 - Write a function countVowels(word) that takes in a word as an argument and returns the number of vowels
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

#8 - Write the function getVowels(word) that takes in a word as an argument and returns the vowels ('a', 'e', 'i', 'o', 'u')
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

#9 - Write the function capitalizeVowels(word) that returns the word with all the vowels capitalized

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

#10 - Write the function startEndVowels(word) that returns True if the word starts and ends with vowels.

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

#11 - Write the function removeVowels(word) that removes all the vowels ('a', 'e', 'i', 'o', 'u') in a word and returns the
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
"""

#12 - Write the function reverseWord(word) that returns the word in the reverse order.

def reverseWord(word):
    return word[::-1]

print reverseWord('apple')
print reverseWord('google')

"""
0:30 - Not sure why it took me 30 seconds to come up with this, but whatever... haha
"""

#13 - Write the function isReverse(word1, word2) that takes two words as arguments and returns True is the second word is
# the reverse of the first word.

def isReverse(word1, word2):
    if word1[::-1] == word2:
        return True
    else:
        return False

print isReverse('apple', 'elppa')
print isReverse('google', 'apple')
print isReverse('google', 'elgoog')
print isReverse('apple', 'alppe')

"""
1:08 - This one was pretty easy to figure out, not much to explain here.
"""

#14 - Write the function startWithVowel(word) that takes in a word as argument and returns a substring that starts with the
# first vowel found in the word. The function returns 'No vowel' if the word does not contain vowel.
def startWithVowel(word):
    vowels = 'aeiouAEIOU'
    for letters in word:
        if letters in vowels:
            return word[word.find(letters):len(word)]
    else:
        return 'No Vowel'

print startWithVowel('apple')
print startWithVowel('google')
print startWithVowel('xyz')

"""
26:55 - Took me a while to figure out the method .find. I remember there was something that could tell me the index of it.
I had to google what the method did and then play around with the for loop and indexing to get it right.
"""

#15 - Write the function getCommonLetters(word1, word2) that takes in two words as arguments and returns a new string that
# contains letters found in both string. Ignore repeated letters and sort the result in alphabetical order.

def getCommonLetters(word1, word2):
    new_word = []
    for letters in word1:
        if letters in word2:
            new_word.append(letters)
    return ''.join(sorted(set(new_word)))

print getCommonLetters('apple','google')
print getCommonLetters('microsoft','apple')
print getCommonLetters('microsoft','google')

"""
Gave up after 26:31 minutes and went to go look for help first then the answer. I actually made my for_loop and appended
the letters that were common in a list, but I didn't know how to return all the letters out until I found the ''.join
built-in function. My next issue was then I didn't know/forgot how to only return non-dupes of a string until I found set().
I looked further and apparently you don't even need a for loop... answer below that uses .intersection function

def getCommonLetterss(a, b):
    return ''.join(sorted(set(a).intersection(set(b))))

print getCommonLetterss('microsoft','google')
"""

#16 - Write a function mirrorText(word1, word2) that takes in 2 words as arguments and returns a new word in the following
# order: word1word2word2word1.

def mirrorText(word1, word2):
    return word1+word2+word2+word1

print mirrorText('hello','world')
print mirrorText('apple','orange')
print mirrorText('google','yahoo')

"""
1:12 - Finally an easy one. pretty self explanatory
"""

#17 - Write a function echoWord(word) that takes in a word as arguments and returns a word that repeats itself based on the
# number of letter in the word.

def echoWord(word):
    return word*len(word)

print echoWord('hi')
print echoWord('apple')
print echoWord('ice')

"""
0:45 - Another easy one.
"""

#18 - Write a function rightJustify(word) that takes in a word as argument and return a word with leading spaces so that
#  the last letter of the word is in column 50 of the display.

def rightJustify(word):
    return '%50s' %word

print rightJustify('apple')
print rightJustify('google')
print rightJustify('microsoft')

"""
15:14 - Had to look for string formats as I forgot how to make spaces.
"""

#19 - A palindrome is a word, phrase, number or other sequence of units that can be read the same way in either direction.
# Write a function that determines whether the given word or number is a palindrome.

def isPalindrome(word):
    while word == str(word):
        if len(word) < 1:
            return False
        if word[::-1] == word:
            return True
        else:
            return False
    else:
        new_word = str(word)
        if new_word == new_word[::-1]:
            return True
        else:
            return False

print isPalindrome("")
print isPalindrome(121)
print isPalindrome("Racecar")
print isPalindrome("Never")
print isPalindrome("level")

"""
26:12 - Figuring out if the strings were palindromes only took me a few minutes. What took me longer to figure out was
the integer and "" (had to put in specific if/else statements). Originally started with an if statement, but then changed
to a while loop and had to play around with all the different if/else statements in a while loop to finally satisfy all
the different types of str/ints
"""

#20 - Write a function isInAlphabeticalOrder(word) that takes in a word as argument and returns True if the word contains letters
#  that are arranged in alphabetical order. For example, the letter 'c' should not appear before the letter 'a'.

def isInAlphabeticalOrder(word):
    word_sorted = sorted(word)
    listed_word = []
    for letters in word:
        listed_word.append(letters)

    if word_sorted == listed_word:
        return True
    else:
        return False

print 'isInAlphabetical', isInAlphabeticalOrder('app')
print 'isInAlphabetical', isInAlphabeticalOrder('apple')
print 'isInAlphabetical', isInAlphabeticalOrder('goo')
print 'isInAlphabetical', isInAlphabeticalOrder('google')

"""
14:16 - Thought there was an alphabetize function, but I remembered there is a sorted function. After I found that, was
playing around with the result of that sorted function and how to compare it. I ran into a hiccup when the sorted function
didn't equal the word, so I made a for loop and turned the word into a list also. Worked after that.
"""

#21 - Write a function isAllLettersUsed(word, required) that takes in a word as the first argument and returns True if the
# word contains all the letters found in the second argument.

def isAllLettersUsed(word, required):

    for letters in required:
        if letters in word:
            continue
        else:
            return False
    return True

print isAllLettersUsed('learning python', 'google')
print isAllLettersUsed('apple', 'apple')
print isAllLettersUsed('apple', 'google')
print isAllLettersUsed('learning python', 'google')
print isAllLettersUsed('learning python', 'apple')

"""
29:09 - I was a bit all over the place on this one. Did a bunch of quessing and checking with if else statements, then
a lot of guessing on for loops with the if/else statements. In between was messing around with the sorted(function) thinking
I needed to make the word into a list and compare it with the required. Anyways, finally got it to work.
"""

#22 - Write a function isTripleDouble(word) that takes in a word as argument and returns True if the word contains three
# consecutive double letters.

def isTripleDouble(word):
    """Tests if a word contains three consecutive double letters."""
    i = 0
    count = 0
    while i < len(word)-1:
        if word[i] == word[i+1]:
            count = count + 1
            if count == 3:
                return True
            i = i + 2
        else:
            count = 0
            i = i + 1
    return False


print isTripleDouble('appllee')
print isTripleDouble('aapplee')
print isTripleDouble('applle')

"""
7:04 - Did not figure out this answer. Started with For loop, messed around with it and if/else statements. Finally gave
up and looked up the answer. I think even if I had a hint to use while loops, I wouldn't have been able to figure it out.
I understand it now, but I think will need more practice to put together this kind of answer.
"""

#23 - Write a function splitWord(word, numOfChar) that takes in a word and a number as arguments. The function will split
#  the word into smaller segments with each segment containing the number of letter specified in the numOfChar argument.
#  These segments are stored and returned in a list.

def splitWord(word, numOfChar):
    new_list = []
    i = 0 #counter for the index
    e = i+numOfChar #the spaces to split the word
    while i < len(word):
        new_list.append(word[i:e])
        i = i + numOfChar
        e = i + numOfChar
    return new_list


print splitWord('google', 2)
print splitWord('google', 3)
print splitWord('apple', 1)
print splitWord('apple', 4)

"""
18:16 - A lot of guessing and checking, but I figured it out! Again, only way I came up with this is because the previous
program stumped me, but this used while loops so eventually got it.
"""

#24 - An anagram is a word formed by reordering the letters of another word. Write a function isAnagram(w1, w2) that takes
# in two words as arguments and return True if one word is an anagram of the other word.

def isAnagram(w1,w2):
    for letters in w1.lower():
        if letters in w2.lower():
            continue
        else:
            return False
    return True

print isAnagram('google', 'gogole')
print isAnagram('google', 'gogoll')
print isAnagram('google', 'gogogo')
print isAnagram('Google', 'google')

"""
2:52 - This one was easy. Just made sure to check the letters were in the other argument and that they were all in
lower case.
"""






