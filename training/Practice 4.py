l = [1,2,3,4,5]

#for num in l:
#    if num % 2 == 0:
#        print 'Even!',num
#    else:
#        print 'Odd!',num

#for num in l:
#    if num % 2 == 1:
#        print num

list_sum = 0

for num in l:
    list_sum = list_sum + num
    print list_sum

s = 'This is a string!'

for letter in s:
    print letter

tup = (1,2,3,4,5)

for item in tup:
    print item

l = [(2,4),(6,8),(10,12)]

#tuple unpacking

for tup in l:
    print tup

for (t1,t2) in l:
    print t1
    print t2

d = {'k1':1,'k2':2,'k3':3}

for item in d:
    print item

for k,v in d:
    print k,v

for item in d.iteritems():
    print item

def generateNumber(num):
    numbers = []
    for x in range(num+1):
        numbers.append(x)
    return numbers

print generateNumber(1)

def generateNumber(start, end):
	numbers = []
	for x in range(start, end+1):
		numbers.append(x)
	return numbers

print generateNumber(2, 7)

def generateNumber(x,y,z):
    if z < 0:
        number = []
	for item in range(x,y,z):
	    number.append(item)
	return number
    else:
        number = []
    for item in range(x,y+1,z):
	    number.append(item)
    return number


print generateNumber(2, 10, 2)
#print generateNumber(15, 6, -2)

def addEvenNumbers(x,y):
    numbers = 0
    for items in range(x,y+1):
        if items % 2 ==0:
            numbers += items
    return numbers




print addEvenNumbers(5, 11)
print addEvenNumbers(3, 8)

def addEvenNumbers(x,y):
    numbers = 0
    for items in range(x,y+1):
        if items % 2 == 0:
            numbers += items
    return numbers

print addEvenNumbers(5, 11)
print addEvenNumbers(3, 8)

def skipVowels(word):
    novowels = ''
    for ch in word:
        if ch.lower() in 'aeiou':
            continue
        novowels+=ch
    return novowels

print skipVowels('Aeroplane')

# insert 'break' in following code so that the comment
# after '#' (including '#') are stripped.
def stripComment(sentence):
    codeonly  = ""
    for ch in sentence:
        if ch == '#':
            break
            codeonly += '#'
        codeonly += ch
    return codeonly

print stripComment('Hello # World')

def genSet(nums):
    numbers = nums
    numbers.sort()
    snumbers = []
    for x in numbers:
        if x in snumbers:
         continue
        else:
            snumbers.append(x)
    return snumbers


print genSet([5,4,8,4,9,8])

def sumOfDigit(num):
    newlist = []
    count = 0
    for i in str(num):
        if int(num) >= 1000:
            count += int(i)
        else:
            newlist.append(i)
            count += int(i)
    return count


print sumOfDigit(123)


