#Chapter 25 - Tuples
#Tuples are immutable

l=[1,2,3]

t=(1,2,3)

print t
print len(t)

t=('one',2)
print t
print t[0]
print t[1]
print t[1::]
print t[::-1]

print t.index('one')
print t.index(2)

print t.count('one')
t=(1,2,2,3,3,3)
print t.count(3)
l=[1,2,3]
t=(1,2,3)
print l
print t

l[0] = 's'
print l

# t[0] = 's' *this will not work since tuples are immutable
# only two methods. Index and count
print t
