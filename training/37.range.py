#Chapter 37 Range

print range(0,10)

print range(20)

x = range(0,10)
print x

print type(x)

start = 5
stop = 20
print range(start, stop)

start = 0
stop = 20
print range(start, stop, 2)

l = [1,2,3,4,5]
for num in xrange(1,6):
    print num

x = xrange(1,6)
x2 = range(1,6)
print x
print type(x)
print type(x2)

list(x)
print list(x)
print list(x) == x2