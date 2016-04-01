#Chapter 35 - For Loops

#MODULO
print 10 % 3
print 18 % 7
print 4 % 2

l = [1,2,3,4,5]

for num in l:
    print 'print something!'

for num in l:
    if num % 2 == 0:
        print num
    else:
        print 'Odd number'

list_sum = 0
for num in l:
    list_sum = list_sum + num
print list_sum

s = 'this is a string!'
for letter in s:
    print letter

tup = (1,2,3,4,5)
for t in tup:
    print t

l = [(2,4),(6,8),(10,12)]
for tup in l:
    print tup

for (t1,t2) in l:
    print t1
    print t2

d = {'k1':1, 'k2':2, 'k3':3}
for k,v in d.iteritems():
    print k
    print v





