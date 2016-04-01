def my_addition_func(arg1, arg2):
    print arg1+arg2

my_addition_func(1,2)

def say_hello():
    print 'hello'

say_hello()

def greeting(name):
    print "hello "+ name

greeting('Henry')

def add_num(num1,num2):
    return num1+num2

x = add_num(1,2)
print x
print add_num(1,2)

print add_num('one','two')

def is_prime(num):
    """
    :param num: integer
    :return:This function check for prime numbers
    """
    for n in range(2,num):
        if num % n == 0:
            print 'Not Prime'
            break

    else:
        print 'The number is prime!'

print is_prime(13)



