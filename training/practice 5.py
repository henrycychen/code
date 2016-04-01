x = 0
while x < 10:
    print 'x is currently',x
    x += 1

x = 0
while x < 10:
    print 'x is currently',x
    x += 1
else:
    print 'all done!'

x = 0
while x < 10:
    print 'x is currently ',x
    print 'x is still less than 10 addone 1 to x'
    x += 1
    if x == 3:
        print 'hey, x = 3!'
    else:
        print 'continuing...'
        continue #starts at the very top of the loop

x = 0
while x < 10:
    print 'x is currently ',x
    print 'x is still less than 10 addone 1 to x'
    x += 1
    if x == 3:
        print 'hey, x = 3!'
        break # stops the below loop
    else:
        print 'continuing...'
        continue

print range(1,10,2)

def addNumbers(num):
    total = 0
    i = 1
    while i:
        for items in range(num+1):
            total += items
        return total
    if num == 1:
        return num

print addNumbers(1)

def addNumbers(start, end):
    total = 0
    while start:
        for items in xrange(start,end+1,1):
            total += items
    return total

print addNumbers(5, 10)


