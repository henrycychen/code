#Chapter 29 - Objects and data

#Write an equation that uses multiplication, division, an exponent, addition, and subtraction that equals to 100.25

x = ((5*5)/(5e1))-5+104.75
print x

#Explain what the cell below will produce. Can you change it so the answer is correct?

x = 2/3
print x
x = 2.0/3
print x

x = 4*(6+5)
y = 4*6+5
z = 4+6*5
print x
print y
print z

#x = 8.5 - floating point
#y = xe0.5

s = 'hello'
print s[1]
print s[::-1]
print s[4]
print s[-1]

l = [0,0,0]
print l
l_1 = [0]
l_2 = [0]
l_3 = [0]

matrix = [l_1, l_2, l_3]
print matrix

l = [1,2,[3,4,'hello']]
print l
l[2] = [3,4,'goodbye']
print l[2]
print l

l = [3,4,5,5,6]
print l.sort()
print sorted(l)

d = {'simple_key':'hello'}
print d['simple_key']

d = {'k1':{'k2':'hello'}}
print d['k1']['k2']

d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print d['k1'][0]['nest_key'][1][0]

d = {'k1':[1,2,{'k2':['this is tricky',{'toughie':[1,2,['hello']]}]}]}
print d['k1'][2]['k2'][1]['toughie'][2][0]

#cannot sort a dictionary because it's by unique identifiers only - they are mappings, not sequences

#tuples are immutable
l = (1,2,3)
print l

#Sets can be unordered collection as unique elements and only cares for unique elements (so no duplicates)

l = [1,2,2,33,4,4,11,22,3,3,2]
print set(l)

print 2 > 3
print 3 <= 2
print 3==2.0
print 3.0==3
print 4**0.5 != 2

l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]
print l_one[2][0]
print l_two[2]['k1']

#true or false
print l_one[2][0] >= l_two[2]['k1']
# 3 >= 4 is false
