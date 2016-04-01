#Chapter 27 - Sets and Booleans
#True and false display in python
#Sets can be unordered collection as unique elements and only cares for unique elements

x = set()
x.add(1)
print x
x.add(2)
print x
#x.add(1) - this will not add 1 again, only concerned with unique function

l = [1,1,1,2,2,2,2,3,3,3,4]
print l
print set(l)

#booleans - predefined true and false 1 and 0
a = True
print a
print 1 > 2
print 11 > 2
b = None
print b

b = 'a'
print b
