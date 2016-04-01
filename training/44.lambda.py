def square(num):
    return num**2

print square(2)

def square(num): return num**2

print square(2)

square2 = lambda num: num**2

print square2(10)

even = lambda num: num % 2 == 0

print even(2)

def even2(num):
    return num%2 == 0

print even2(2)

#Grabs the first characher of a string

first = lambda s: s[0]
print first('hello')

rev = lambda s: s[::-1]
print rev('hello')

def adder(x,y):
    return x+y

print adder(10,12)

adder2 = lambda x,y: x+y
print adder2(30,30)


