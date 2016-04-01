x = 25 #global scope

def printer():
    x = 50 #local scope
    return x

print x
print printer()

f = lambda x:x**2 #x is local

name = 'This is a global name'

def greet():
    # Enclosing function
    name = 'Sammy'

    def hello(): #looks at name for local scope. "Is it defined anywhere in the hello function". If not it moves to the enclosing function.
        print 'Hello ' + name

    hello()

greet()

x = 50 #Global in scope

def func(x):
    print 'x is', x
    x = 2
    print 'Changed local to ', x

func(x)
print 'x is still', x

x = 50

def func():
    global x
    print 'This function is now using the global x!'
    print 'Because of global x is: ', x
    x = 2
    print 'Ran func(), changed global x to', x

print 'Before calling func(), x is: ', x
func()
print 'Value of x (outside of func()) is: ', x



