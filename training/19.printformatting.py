#Chapter 17 - Print Formatting
#%s = string
#%1.1 = first number = how many characters, 2nd # = how many decimal places
#%r will do same thing as %s - both use different methods. One is str(), other is repr()


print 'This is a string'
s = 'String'
print 'place my variable here: %s' %(s)

print 'Floating point number here: %1.3f' %(13.145)

print 'Convert to a string %s' %(123)

print 'First: %s, Second: %s, Third: %s' %('hi!','two',3)

print 'First: %s, Second: %s' %(2,2)

print 'First: {x} Second: {y} Third: {x}'.format(x='inserted',y='two!')