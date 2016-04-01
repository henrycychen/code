string = 'hello'
print string
print string[0:2]

def first_two(str):
    str = 'hello'
    print str[0:2]
    str = 'abcdefg'
    print str[0:2]
    str = 'ab'
    print str[0:2]

first_two(str)

#~~~~~~~

def hello_name(name):
    print "Hello %s" %(name)
hello_name('Bob')
hello_name('Alice')
hello_name('X')

#~~~~~~~

def first_half(str):
    xyz = len(str) / 2
    print str
    print str[0:xyz]
first_half('hellothere')
first_half('Woohoo')
first_half('abcdef')

#~~~~~~~
def non_start(a, b):
    print "%s%s" %(a[1:],b[1:])
non_start('hello', 'there')
non_start('java', 'code')
non_start('shotl', 'ava')

#~~~~~~~
def make_abba(a, b):
    print "%s%s%s%s" %(a.lower(),b,b.lower(),a)
make_abba('Hi','Bye')
make_abba('Yo','Alice')

#~~~~~~
def extra_end(str):
    print str[-2:]*3
extra_end('Hello')
extra_end('ab')
extra_end('Hi')

#~~~~~~~
def without_end(str):
    print str[1:-1]
without_end('Hello')
without_end('java')
without_end('coding')

#~~~~~~
def left2(str):
    a = str[0:2]
    print str[2:]+a
left2('Hello')
left2('Java')
left2('Hi')

#~~~~~~
def make_tags(tag, word):
    print "<%s>%s<%s>"%(tag,word,tag)
make_tags('i','Yay')
make_tags('i','Hello')
make_tags('cite','Yay')

#~~~~~~~~
def combo_string(a, b):
    alen = len(a)
    blen = len(b)
    if alen > blen:
        print b+a+b
    else:
        print a+b+a
combo_string('Hello','hi')
combo_string('hi','Hello')
combo_string('aaa','b')

#~~~~~~~ Boolean Logic
def cigar_party(cigars, is_weekend):
    if cigars < 40:
        print 'Failed party!'
    elif cigars >= 40:
        print 'Successful party!'
cigar_party(30, False)
cigar_party(50, False)
cigar_party(70, True)

#~~~~~~~~~
def diff21(n):
    x = 21-n
    print x
diff21(19)
diff21(10)
diff21(21)

#~~~~~~~~~
#Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.

def near_hundred(n):
    if (abs(n) >=90) and (abs(n) <=100):
        print True
    else:
        print False

near_hundred(93)
near_hundred(90)
near_hundred(89)


#~~~~~~~~~~~~~~~~~~
#Given a non-empty string and an int n, return a new string where the char at index n has been removed. The value of n
#will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).

def missing_char(str, n):
    front = str[:n]
    back = str[n+1:]
    print front+back
missing_char('kitten', 1)
missing_char('kitten', 0)
missing_char('kitten', 4)

#~~~~~~~~~~~~~~~~~
#We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling. We are in trouble if
#they are both smiling or if neither of them is smiling. Return True if we are in trouble.

def monkey_trouble(a_smile, b_smile):
    if a_smile == b_smile:
        print True
    else:
        print False

monkey_trouble(True, True)
monkey_trouble(False, False)
monkey_trouble(True, False)


#Given two int values, return their sum. Unless the two values are the same, then return double their sum.

def sum_double(x,y):
    if x==y:
        z = (x+y)*2
        print z
    else:
        print x+y

sum_double(1,2)
sum_double(3,2)
sum_double(2,2)

#~~~~~~~~~~~~~~~~~~`
#We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. We are in trouble if
# the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.
def parrot_trouble(talking, hour):
    if talking == True and hour <=7 or hour >=20:
        print "You're in trouble!"
    else:
        print "You're fine!"

parrot_trouble(True, 6)
parrot_trouble(True, 7)
parrot_trouble(False, 6)

#~~~~~~~~~~~~~``
#Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10
def makes10(a, b):
    if a == 10 or b == 10:
        print True
    elif a+b == 10:
        print True
    else:
        print False
makes10(9,10)
makes10(9,9)
makes10(1,9)

#~~~~~~~~~~~~~~~~~~~~~~~~~
#Given 2 int values, return True if one is negative and one is positive. Except if the parameter "negative"
#is True, then return True only if both are negative.

def pos_neg(a, b, negative):
    if negative == True and a<0 and b<0:
        print True
    elif a<0 or b<0:
        print True
    else:
        print False
pos_neg(1, -1, False)
pos_neg(-1, 1, False)
pos_neg(-4, -5, True)

#Given a string, return a new string where "not " has been added to the front. However, if the string already begins
# with "not", return the string unchanged.

def not_string(str):
    if len(str) >= 3 and str[:3] == "not":
        print str
    else:
        print 'not '+ str

not_string('candy')
not_string('x')
not_string('not bad')

#~~~~~~~~~~~
#Given a string, return a new string where the first and last chars have been exchanged.

def front_back(str):
    if len(str) <=1:
        print str
    else:
        mid = str[1:-1]
        print str[-1] + mid + str[0]

front_back('code')
front_back('a')
front_back('ab')

#~~~~~~~~~~~~~~~~~~~~~~~~
#Given a string, we'll say that the front is the first 3 chars of the string. If the string length is less than 3, the ' \
#'front is whatever is there. Return a new string which is 3 copies of the front.

def front3(str):
    front = str[0:3]
    print front*3
front3('Java')
front3('Chocolate')
front3('abc'





