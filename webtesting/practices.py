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

### Lists questions
#4 - Write a function addNumbersInList(numbers) to add all the numbers in a list. To access each element in a list,
#  you can use the statement 'for num in numbers:'.

def addNumbersInList(numbers):
    count = 0
    for items in numbers:
        count += items
    return count

print addNumbersInList([])
print addNumbersInList([10, 20, 30])
print addNumbersInList([-10, -20, 30])

"""
02:18 - Easy for loop for addition. Need to just add each iteration in the list.
"""

#5 - Write a function addOddNumbers(numbers) to add all the odd numbers in a list. To access each element in a list, you can
#use the statement 'for num in numbers:'.

def addOddNumbers(numbers):
    count = 0
    for items in numbers:
        if items % 2 == 1:
            count += items
    return count

print addOddNumbers([1, 4, 8, 9])
print addOddNumbers(range(1, 20, 3))
print addOddNumbers([])

"""
01:29 - Another pretty easy for loop using the modulus to figure out the odd number
"""

#6 - Write a function countOddNumbers(numbers) to count the number of odd numbers in a list.

def countOddNumbers(numbers):
    count = 0
    for items in numbers:
        if items % 2 == 1:
            count += 1
    return count

print countOddNumbers([1, 4, 8, 9])
print countOddNumbers(range(1, 20, 3))
print countOddNumbers([])

"""
1:04 - Easy. Just needed a for loop and a counter when each time an odd number appears
"""

#7 - Write a function getEvenNumbers(numbers) to return all the even numbers in a list.

def getEvenNumbers(numbers):
    even_list = []
    for items in numbers:
        if items % 2 == 0:
            even_list.append(items)
    return even_list

print getEvenNumbers([1, 4, 8, 9])
print getEvenNumbers(range(1, 20, 3))
print getEvenNumbers([])

"""
01:08 - Easy for loop using append and modulus function.
"""

#8 - Write a function removeFirstAndLast(list) that takes in a list as an argument and remove the first and last
# elements from the list. The function will return a list with the remaining items.

def removeFirstAndLast(list):
    if len(list) < 2:
        list.remove(list[0])
        return list
    else:
        list.remove(list[0])
        list.remove(list[-1])
        return list

print removeFirstAndLast([1, 4])
print removeFirstAndLast(range(1, 20, 3))
print removeFirstAndLast([1])

"""
03:32 - Thought I could just use the .remove function, but wouldn't work with just one integer in the list. Worked fine
after I created the if/else statement
"""

#9 - Write a function getMaxNumber(numbers) that returns the maximum number in a list.

def getMaxNumber(numbers):
    i = 1
    if len(numbers) < 1:
        return 'N.A'
    for items in numbers:
       if items < numbers[1]:
           i += 1
           continue
    return items

print getMaxNumber([1, 4, 10])
print getMaxNumber(range(1, 20, 3))
print getMaxNumber([])

"""
18:10 - What stumped me on this one was then empty list and how to return 'N.A'. I kept putting the if len(numbers) < 1:
statement in the for loop. Didn't work until I moved it out of the for loop. Also, I originally started this with a while
loop... I messed that up making a forever loop. haha. Realized that I didn't need it and proceeded with just a for loop.
"""

#10 - Write a function getMinNumber(numbers) that returns the minimum number in a list.
def getMinNumber(numbers):
    if len(numbers) == 0:
        return 'N.A'
    else:
        return sorted(numbers)[0]

print getMinNumber([12, 4, 10])
print getMinNumber([])

"""
17:25 - would have been quicker, but decided to mess around with a while loop again. Apparently, I'm pretty crappy at
those. Decided to sort the list so I don't have to do any real checks like the previous program.
"""

#16 - Write a function combine(la, lb) that takes in two lists and return a list with the contents of both list sorted
# in ascending order.

def combine(la, lb):
    new_list = []
    for items in la:
        new_list.append(items)

    for items in lb:
        new_list.append(items)

    return sorted(new_list)

print combine(['a', 'p', 'l'], ['g','o','l'])
print combine(range(10, 2, -2), range(1, 10, 3))
print combine(['a', 1, 'z'], [2, 4, 'y'])

"""
01:15 - Easier than I thought. Made a new list using for loops.
"""

#Codingbat questions - Warm up.

#1 - The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation.
# We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.

def sleep_in(weekday, vacation):
    if weekday == True and vacation == True:
        return True
    elif weekday == True:
        return False
    elif weekday == False and vacation == False:
        return True
    elif weekday == True and vacation == True:
        return False
    elif vacation == True:
        return True
    else:
        return False

print sleep_in(False, False)
print sleep_in(True, False)
print sleep_in(False, True)

"""
4:30 - Was trying to understand their question. I knew it was booleans, but didn't understand what they wanted. Once I did,
had to do a little guess and check.
"""

#2 - We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling. We are in trouble if
# they are both smiling or if neither of them is smiling. Return True if we are in trouble.

def monkey_trouble(a_smile, b_smile):
    if a_smile == True and b_smile == True:
        return True
    elif a_smile == False and b_smile == False:
        return True
    else:
        return False

"""
02:19 - Simple if/else statement.
"""

#3 - Given two int values, return their sum. Unless the two values are the same, then return double their sum.
def sum_double(x,y):
    if x == y:
        return (x+y)*2
    else:
        return x+y

print sum_double(1, 2)
print sum_double(3, 2)
print sum_double(2, 2)

"""
02:32 - Should have done it faster, but I didn't read the problem correctly. Thought I was suppose to square it, but instead
it's just multiply by 2.
"""

#4 - Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n
# is over 21.

def diff21(num):
    if num > 21:
        return abs(21-num)*2
    else:
        return 21 - num
print diff21(19)
print diff21(10)
print diff21(21)

"""
03:13 - pretty simple, just had to play around with the absolute function to make sure I got the correct answers
"""

#5 - We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. We are in trouble
#  if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.
def parrot_trouble(x, time):
    if x == False:
        return False
    elif x == True and time > 20:
        return True
    elif x == True and time < 7:
        return True
    else:
        return False

print parrot_trouble(True, 6)
print parrot_trouble(True, 7)
print parrot_trouble(False, 6)

"""
03:06 - more if/else statements. Pretty simple.
"""

#6 - Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.
def makes10(x, y):
    if x == 10 or y == 10:
        return True
    elif x+y == 10:
        return True
    else:
        return False

makes10(9, 10)
makes10(9, 9)
makes10(1, 9)

"""
0:53 - Easy. not much explanation.
"""

#7 - Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.

def near_hundred(n):
    if abs(n) >= 90 and abs(n) <= 110:
        return True
    elif abs(n) >= 190 and abs(n) <= 210:
        return True
    else:
        return False

print near_hundred(93)
print near_hundred(90)
print near_hundred(89)

"""
04:01 - Easy. Just had to write if/else statements and make sure n fits in the parameters. Apparently I just noticed can
do this too.

def near_hundred(n):
  return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))
"""

#8 - Given 2 int values, return True if one is negative and one is positive. Except if the parameter "negative" is True,
# then return True only if both are negative.

def pos_neg(x,y,z):
    if z == True:
        return x < 0 and y < 0
    elif z == False and x < 0 and y < 0:
        return False
    elif z == False and x > 0 and y > 0:
        return False
    else:
        return True

print pos_neg(-4, -5, False)
print pos_neg(1, -1, False)
print pos_neg(-1, 1, False)
print pos_neg(-4, -5, True)

"""
12:35 - This one was weird. Did the guess and check work until it told me the answer is good. Below is their solution

def pos_neg(a, b, negative):
  if negative:
    return (a < 0 and b < 0)
  else:
    return ((a < 0 and b > 0) or (a > 0 and b < 0))
"""

#9 - Given a string, return a new string where "not " has been added to the front. However, if the string already begins
# with "not", return the string unchanged.
def not_string(str):
    if 'not' == str[0:3]:
        return str
    else:
        return 'not ' + str

print not_string('candy')
print not_string('x')
print not_string('not bad')

"""
8:50 - Had a mistype in my string. I forgot that indexing only counts up to the last letter. I was using str[0:2] which
meant I was only looking for 'no' instead of 'not'.
"""

# Given a non-empty string and an int n, return a new string where the char at index n has been removed. The value of n
# will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).
def missing_char(str, n):
    return str[0:n] + str[n+1::]

print missing_char('kitten', 1)
print missing_char('kitten', 0)
print missing_char('kitten', 4)

"""
02:04 - Pretty easy and self explanatory. Wanted to return the first half of the word up to index 'n' and then concatenate the
rest of the word after index 'n'.

the solution differs a little than mine:

def missing_char(str, n):
  front = str[:n]   # up to but not including n
  back = str[n+1:]  # n+1 through end of string
  return front + back
"""

#Given a string, return a new string where the first and last chars have been exchanged.

def front_back(str):
    if len(str) <= 1:
        return str
    else:
        return str[-1] + str[1:-1] + str[0]

print front_back('code')
print front_back('a')
print front_back('ab')

"""
05:28 - not too bad, just got hung up a little on the middle letters of the word. Had to guess and check. Also, words with
only 1 or 0 letters, had to put in a separate if statement to accomodate.

I think my solution was better than theirs
def front_back(str):
  if len(str) <= 1:
    return str

  mid = str[1:len(str)-1]  # can be written as str[1:-1]

  # last + mid + first
  return str[len(str)-1] + mid + str[0]
"""

#Given a string, we'll say that the front is the first 3 chars of the string. If the string length is less than 3, the ' \
#'front is whatever is there. Return a new string which is 3 copies of the front.

def front3(str):
    if len(str) < 3:
        return str*3
    else:
        return str[0:3] * 3

print front3('Java')
print front3('Chocolate')
print front3('abc')

"""
01:09 - easy.
"""

#Back to pyschools list questions - #19 - Write a function calCumulativeSum(numbers) that takes in a list of numbers as argument and returns the cumulative
#  sum of the list. That is, the new list where the i element is the sum of the first i + 1 elements from the original
# list. For example, the cumulative sum of [1, 2, 3] is [1, 3, 6].
def calCumulativeSum(numbers):
    new_list = []
    count = 0
    for nums in numbers:
        count += nums
        new_list.append(count)
    return new_list

print calCumulativeSum([1,2,3])
print calCumulativeSum([2,2,2])
print calCumulativeSum([2,4,6])

"""
02:59 - Surprisingly easy... used a for loop and just appeneded every new count to a new list.
"""

#20 - Write a function combineList(list1, list2) that takes in two lists as arguments and return a list that combines all
# the elements in the two list.
def combineList(list1, list2):
    new_list = []
    for nums in list1:
        new_list.append(nums)
    for nums in list2:
        new_list.append(nums)
    return new_list

print combineList([1,2], [3, 4])
print combineList(range(5), range(5))
print combineList(range(5), ['a', 'b', 'c'])

"""
01:21 - I'm getting too good at this.
"""

#22 - Write a function (list1, list2) that takes in two lists as arguments and return a list that is the result of removing
# elements from list1 that can be found in list2.
def subtractList(list1, list2):
    new_list = []
    for nums in list1:
        if nums in list2:
            continue
        else:
            new_list.append(nums)
    return new_list

print subtractList(range(5), range(4))
print subtractList([1,2,3,4,5], [2, 4])
print subtractList (['a', 'b', 'c', 'd'], ['x', 'y', 'z'])

"""
02:20 - just having a good list answers day... easy
"""

#23 - Write a function countLetters(word) that takes in a word as argument and returns a list that counts the number of
# times each letter appears. The letters must be sorted in alphabetical order.
def countLetters(word):
    new_list = []
    count_list = []
    for letters in sorted(set(word)):
        new_list.append(letters)
        count_list.append(word.count(letters))
    return zip(new_list,count_list)

print countLetters('google')
print countLetters('apple')
print countLetters('microsoft')

"""
47:01 - took me about 20 minutes to get the letters and count in order, but then I got stuck on how to group them together.
Had to look up the answer. zip is on my cheat sheet now.
"""

#24 - Write a function getNumbers(number) that takes in a number as argument and return a list of numbers as shown in the
# samples given below.
def getNumbers(number):
    new_list = []
    for nums in range(number,-1,-2):
        new_list.append(nums**2)
    for nums in range(new_list[-1],number + 1,2):
        if nums != 0:
            new_list.append(nums**2)
    return new_list

print getNumbers(10)
print getNumbers(9)
print getNumbers(8)
print getNumbers(0)

"""
23:35 - Took me a while to try and figure out the algorithm and how to bypass certain numbers. 0 is not suppose to be
repeated, but 1 can...
"""

#24 - Write a function getSumOfFirstDigit(numList) that takes in a list of positive numbers and returns the sum of all the
# first digit in the list.

def getSumOfFirstDigit(numList):
    new_list = []
    new_list2 = []
    sum = 0
    for nums in numList:
        new_list.append(str(nums))
    for nums in new_list:
        new_list2.append(nums[0])
    for nums in new_list2:
        sum += int(nums)
    return sum

print getSumOfFirstDigit([12, 23, 34, 45, 56])
print getSumOfFirstDigit([1, 23, 456, 7890])
print getSumOfFirstDigit([])

"""
07:20 - I'm pretty sure this is not an efficient way of writing code, but only way I could think of to get the answer.

here is an online list comprehension way, idea was the same, just the code can be simplified a lot more...

def getSumOfFirstDigit(numList):
    return sum(int(str(n)[0]) for n in numList)

and I just rewrote it more simplified

def getSumOfFirstDigit(numList):
    answer = 0
    for nums in numList:
        answer += int(str(nums)[0])
    return answer
"""

#26 - List comprehension offers a concise way to derive a new list from an existing list or sequence. Given a list of
# numbers, write a function that returns the numbers that are greater than the average.

"""
def getAboveAverage(nums):
    return [ x for x in nums if x > sum(nums)/len(nums) ]  # complete the list comprehension

just had to fill in the blank after x >.
"""

#while loops off of pyschool
#Create a function addNumbers(x) that takes a number as an argument and adds all the integers between 1 and the number
# (inclusive) and returns the total number.

def addNumbers(x):
    i = 0
    count = 0
    while i < x:
        for nums in range(x+1):
            count += nums
            i += 1
    return count

print addNumbers(10)
print addNumbers(1)

"""
4:00 - Took me a sec to think of what variables I needed to keep track of. I know I needed a stop (i < x), a running count
of the total, and 'i' increasing by 1 until the stop.
"""

#Create a function addNumbers(start, end) that adds all the integers between the start and end value (inclusive) and
# returns the total sum.
def addNumbers(start,end):
    count = 0
    i = start
    while i < end + 1:
        for nums in range(start, end + 1):
            count += nums
            i += 1
        return count

print addNumbers(5, 10)
print addNumbers(1, 1)

"""
02:53 - Pretty easy. Same as last, but placed a range start to end.
"""

#Create a function countPages(x) that takes the number of pages of a book as an argument and counts the number of times
# the digit '1' appears in the page number.
def countPages(x):
    total = 0
    i = 1
    while i < x+1:
        total += str(i).count('1')
        i += 1
    return total

print countPages(200)
print countPages(100)
print countPages(11)

"""
09:35 - Needed to know the built-in function to count the '1' in the string. Had issues with it when I was using a for
loop and it would only count '11', 1 instead of 2.
"""

#Create a function factorial(x) that takes an integer and returns the product of all the positive integers less than
# or equal to n.
def factorial(x):
    total = 1
    i = 0
    while i < x+1:
        for nums in range(1, x+1):
            total *= nums
            i += 1
        return total

print factorial(10)
print factorial(0)

"""
Forgot to time, but figured out the answer. I need to stop putting for loops into a while loop(I'm making it repetitive).
Also, better answer below just using a while loop.

def factorial(num):
    product = 1
    i = num
    while i > 0:
        product = product * i
        i = i - 1
    return product
"""

#Create a function doubleFactorial(n) that takes an odd integer and returns the product of all odd values up to the
# value n (where n=2k-1).

def doubleFactorial(n):
    product = 1
    i = 1
    while n > i:
        if n % 2 == 1:
            product = product * n
        n -= 1
    return product

print doubleFactorial(9)
print doubleFactorial(1)

"""
11:48 - I did not understand their question using n = 2k - 1 so I just made up my own. Took me a while only because I placed
n -= 1 in the wrong place (I originally placed it under the if statement.
"""

#Create a function that takes in a positive integer and return a list of prime numbers.
#A prime number is only divisible by 1 and itself.

def prime_check(x):
    i = 1
    count = 0
    while i <= x:
        if x % i == 0:
            count += 1
        i += 1
        if count > 2:
            return False
    else:
        return True

def primeNumbers(num):
    i = 1
    prime_list = []
    while num > i:
        if prime_check(num) == True:
            prime_list.append(num)
        num -= 1
    return sorted(prime_list)

print primeNumbers(5)

"""
XX:XX - A lot of hours trying to figure out the below. Instead I just made two functions. One to check if the number was
prime and the second function would go through each number up until 'num' and call the first function to check it. Below
was another answer from online that still baffles me with the k*k statement...

def primeNumbers(num):
    primes = []
    i = 2
    while i <= num:
        k = 2
        isPrime = True
        while k*k <= i:
            if i%k == 0:
               isPrime = False
            k += 1
        if isPrime:
            primes.append(i)
        i += 1
    return primes
"""

#Create a function that takes in a positive number and return 2 integers such that the number is between the squares
# of the 2 integers. It returns the same integer twice if the number is a square of an integer.

def sqApprox(num):
    i = 0
    minsq = 0                            # set lower bound
    maxsq = round(num + 0.4,0)                   # set upper bound
    while i < num:                       # set 'while' termination condition
          if i*i<=num and i > minsq:     # complete inequality condition
             minsq = i
          if i*i>=num and i < maxsq:     # complete inequality condition
             maxsq = i
          i += 1                         # update i so that 'while' will terminate
    return (minsq, maxsq)

print sqApprox(2)
print sqApprox(0.1)
print sqApprox(4)
print sqApprox(1.2)

"""
12:50 - just had to fill in the blanks of their 90% done finished code. Was trying to understand it, so it took me a little
while to complete.
"""

#Back to coding bat on Warmup-2
#Given a string and a non-negative int n, return a larger string that is n copies of the original string.

def string_times(str, n):
    return str*n

print string_times('Hi', 2)
print string_times('Hi', 3)
print string_times('Hi', 1)

"""
0:03 - easy
"""

#`Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is '
#'there if the string is less than length 3. Return n copies of the front
def front_times(str,n):
    return str[0:3]*n

front_times('Chocolate', 2)
front_times('Chocolate', 3)
front_times('Abc', 3)

"""
easy
"""

#Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".

def string_bits(str):
    result = ''
    for i in range(0,len(str),2):
        result += str[i]
    return result

print string_bits('Hello')
print string_bits('Hi')
print string_bits('Heeololeo')

"""
This took me a lot longer than expected. Forgot that in for loops, use results vs. appending into a list.
"""

#Given a non-empty string like "Code" return a string like "CCoCodCode".

def string_splosion(str):
    result = ''
    i = 0
    while i < len(str) + 1:
        result = result + str[0:i]
        i += 1
    return result

print string_splosion('Code')
print string_splosion('abc')
print string_splosion('ab')

"""
09:04 - Thought I had to use a for loop... once my for loop didn't work, I switched over to a while loop, which worked
better and only took me less than a minute to complete. Below is the answer using a for loop.

def string_splosion(str):
  result = ""
  # On each iteration, add the substring of the chars 0..i
  for i in range(len(str)):
    result = result + str[:i+1]
  return result
"""

#Given an array of ints, return the number of 9's in the array.

def array_count9(array):
    count = 0
    for nums in array:
        if nums == 9:
            count += 1
    return count

print array_count9([1, 2, 9])
print array_count9([1, 9, 9])
print array_count9([1, 9, 9, 3, 9])

"""
02:01 - pretty straight forward for loop on this one.
"""

#Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4.

def array_front9(array):
    if 9 in array[0:4]:
        return True
    else:
        return False

print array_front9([1, 2, 9, 3, 4])
print array_front9([1, 2, 3, 4, 9])
print array_front9([1, 2, 3, 4, 5])

"""
03:02 - originally started with a 4 loop, but couldn't get that to work so I just did a simple if/else statement. Below
is the for loop way.

def array_front9(nums):
  # First figure the end for the loop
  end = len(nums)
  if end > 4:
    end = 4

  for i in range(end):  # loop over index [0, 1, 2, 3]
    if nums[i] == 9:
      return True
  return False
"""

str = 'word'
print str[::-1]
print str[0:-2]

#Given an array of ints, return True if .. 1, 2, 3, .. appears in the array somewhere.
def array123(nums):
    if 1 in nums and 2 in nums and 3 in nums:
        return True
    else:
        return False

print array123([1, 1, 2, 3, 1])
print array123([1, 1, 2, 4, 1])
print array123([1, 1, 2, 1, 2, 3])

"""
07:14 - tried using a for loop, but that failed. Eventually just made a simple if/else statement and it worked. Below is
the for loop solution.

def array123(nums):
  # Note: iterate with length-2, so can use i+1 and i+2 in the loop
  for i in range(len(nums)-2):
    if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
      return True
  return False
"""
#coding bat - list practices
#Given an array of ints, return True if 6 appears as either the first or last element in the array. The array will be length 1 or more.

def first_last6(nums):
    if 6 == nums[0] or 6 == nums[-1]:
        return True
    else:
        return False

first_last6([1, 2, 6])
first_last6([6, 1, 2, 3])
first_last6([13, 6, 1, 2, 3])

"""
0:54 - easy
"""

#Given an array of ints, return True if the array is length 1 or more, and the first element and the last element are equal.

def same_first_last(nums):
    return len(nums) >= 1 and nums[0] == nums[-1]

same_first_last([1, 2, 3])
same_first_last([1, 2, 3, 1])
same_first_last([1, 2, 1])

"""
01:46 - pretty easy once I used the same solution as the last problem.
"""

#Return an int array length 3 containing the first 3 digits of pi, {3, 1, 4}.
def make_pi():
    return [3,1,4]

print make_pi()

"""
This was a dumb exercise question... not even sure the point of it.
"""

#Given 2 arrays of ints, a and b, return True if they have the same first element or they have the same last element.
#  Both arrays will be length 1 or more.
def common_end(a,b):
    return a[0] == b[0] or a[-1] == b[-1]

common_end([1, 2, 3], [7, 3])
common_end([1, 2, 3], [7, 3, 2])
common_end([1, 2, 3], [1, 3])

"""
0:47 - pretty easy.
"""

#Given an array of ints length 3, return the sum of all the elements.
def sum3(nums):
    total = 0
    for numbers in nums:
        total += numbers
    return total

sum3([1, 2, 3])
sum3([5, 11, 2])
sum3([7, 0, 0])

"""
0:31 - another easy one.
"""

#Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.
def rotate_left3(nums):
    for i in range(len(nums)):
        return [nums[i+1], nums[i+2], nums[i]]

print rotate_left3([1, 2, 3])
print rotate_left3([5, 11, 9])
print rotate_left3([7, 0, 0])

"""
2:40 - pretty easy to shift this over
"""

#Given an array of ints length 3, return a new array with the elements in reverse order, so {1, 2, 3} becomes {3, 2, 1}.
def reverse3(nums):
    return [nums[2], nums[1], nums[0]]

print reverse3([1, 2, 3])
print reverse3([5, 11, 9])
print reverse3([7, 0, 0])

"""
01:26 - Another easy one.
"""

#Given an array of ints length 3, figure out which is larger between the first and last elements in the array, and set all the other elements to be that value. Return the changed array.

def max_end3(nums):
    if nums[0] > nums[2]:
        return [nums[0],nums[0],nums[0]]
    else:
        return [nums[2], nums[2], nums[2]]

max_end3([1, 2, 3])
max_end3([11, 5, 9])
max_end3([2, 11, 3])

"""
01:35 - Another straight forward one.
"""

#Given an array of ints, return the sum of the first 2 elements in the array. If the array length is less than 2, just
# sum up the elements that exist, returning 0 if the array is length 0.
def sum2(nums):
    total = 0
    if len(nums) < 1:
        return 0
    elif len(nums) < 2:
        return nums[0]
    else:
        return nums[0] + nums[1]

print sum2([1, 2, 3])
print sum2([1, 1])
print sum2([1, 1, 1, 1])

"""
04:26 - Had to think through of all the little exceptions. Pretty straight forward nonetheless.
"""

#Given 2 int arrays, a and b, each length 3, return a new array length 2 containing their middle elements.

def middle_way(a,b):
    return [a[1], b[1]]

print middle_way([1, 2, 3], [4, 5, 6])
print middle_way([7, 7, 7], [3, 8, 0])
print middle_way([5, 2, 9], [1, 4, 5])

"""
0:36 - easy question.
"""

#Given an array of ints, return a new array length 2 containing the first and last elements from the original array.
# The original array will be length 1 or more.
def make_ends(nums):
    if len(nums) < 2:
        return [nums[0], nums[0]]
    else:
        return [nums[0], nums[-1]]

print make_ends([1, 2, 3])
print make_ends([1, 2, 3, 4])
print make_ends([7, 4, 6, 2])

"""
01:18 - Another easy one.
"""

#Given an int array length 2, return True if it contains a 2 or a 3.

def has23(nums):
    return 2 in nums or 3 in nums

print has23([2, 5])
print has23([4, 3])
print has23([4, 5])

"""
0:26 - Easy..
"""

#Return the number of times that the string "hi" appears anywhere in the given string.
def count_hi(str):
    count = 0
    for i in range(len(str)):
        if 'hi' in str[i:i+2]:
            count += 1
    return count

print count_hi('abc hi ho')
print count_hi('ABChi hi')
print count_hi('hihi')

"""
Not sure how much time this took since I forgot to start the clock, but it was not fast. For loops have a different structure
than all other loops, so it's good getting this kind of practice to figure out when I use for loops vs while loops.
"""

#Return True if the string "cat" and "dog" appear the same number of times in the given string.

def cat_dog(str):
    cat_count = 0
    dog_count = 0

    for i in range(len(str)):
        if 'cat' in str[i:i+3]:
            cat_count += 1
        if 'dog' in str[i:i+3]:
            dog_count += 1
    if cat_count == dog_count:
        return True
    else:
        return False

print cat_dog('catdog')
print cat_dog('catcat')
print cat_dog('1cat1cadodog')

"""
04:00 - Not too difficult once I decided to use two counts and a for loop to check each 3 letters.
"""

#Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any letter
# for the 'd', so "cope" and "cooe" count.

def count_code(str):
    count = 0
    for i in range(len(str)):
        if 'code' in str[i:i+4] or 'cooe' in str[i:i+4] or 'cope' in str[i:i+4] or 'coze' in str[i:i+4] or 'cole' in str[i:i+4] or 'core' in str[i:i+4] or 'coze' in str[i:i+4]:
            count += 1
    return count


print count_code('aaacodebbb')
print count_code('codexxcode')
print count_code('cozexxcope')

"""
07:53 - I cheated as I did not know how to find all the combinations of 'co$e'. I found someone else's code below, but it's a bit
confusing...


def count_code(str):
  count = 0
  i=0
  while "co" in str[i:]:
    if len(str[i+str[i:].index("co"):]) >= 4 and str[i+3+str[i:].index("co")] == "e":
      count += 1
    i += str[i:].index("co")+3
  return count

print count_code('aaacodebbb')
#print count_code('codexxcode')
#print count_code('cozexxcope')
"""

#Given two strings, return True if either of the strings appears at the very end of the other string, ignoring upper/lower
# case differences (in other words, the computation should not be "case sensitive"). Note: s.lower() returns the lowercase
# version of a string.

def end_other(a,b):
    longer_word = ''
    shorter_word = ''
    if len(a) > len(b):
        longer_word = a.lower()
        shorter_word = b.lower()
    else:
        longer_word = b.lower()
        shorter_word = a.lower()

    return shorter_word == longer_word[-len(shorter_word):]

print end_other('AbC', 'HiaBc')
print end_other('Hiabc', 'abcd')
print end_other('Hiabc', 'abc')
print end_other('AbC', 'HiaBc')
print end_other('abc', 'abXabc')

"""
17:28 - Had to play around with the different positions on index. Apparently there's a built-in function that checks the end
of a string...

def end_other(a, b):
  a = a.lower()
  b = b.lower()
  return (b.endswith(a) or a.endswith(b))
"""