# Chapter 15 - Numbers#
# Integer = 1 or -2 , Floating point = 1.5 or 1e2
# Python 2.x uses classic division (it doesn't show decimals)
# Can cast something into a function, changes a integer into a floating point (ex: float(3)/2 = 1.5
# from __future__ import division. This will use python 3 code to divide things correctly
#

from __future__ import division
a = 3/2
print a
b = 3.00/2
print b
c = 3/2
print c

# 2**3 = 2e3
d = 2**3
print d

# square roots = square root of 4
e = 4**0.5
print e

f = 2+10*10+3
print f

g = (2+10)*(10+3)
print g

a = 10
print a

a = a+a
print a

my_income = 100
tax_rate = 0.1

my_taxes = my_income*tax_rate
print my_taxes
