#Chapter 16 - Strings
#'This is also a string' = this is a sequence (s)
#Indexing starts at 0
#len = length
#slicing = grabs everything up until the point s[1:] = grad starting from letter 2, s[:3] = grabs up to 3 (0,1,2)
#stings are immutable
#can concatenate (add onto strings)
#

s = 'hello world'
print s

output2 = "This is a string"
print output2

print 'hello world1'
print 'hello world2'

print 'this is a new line \n and this is the second line and this is a \t tab'

print len('Hello World')
print s[0]
print s[1]
print s[1:]
print s
print s[:3]
print s[:]
print s[-1]
print s[:-1]
print s[:-2]
print s[::1]
print s[::2]
print s[::3]
print s+ ' concatenate me!'
letter = 'zz'
print letter*10

s = 'Hello'
print s.upper()
print s.lower()
print s.split('e')