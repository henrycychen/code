#Chapter 26 - Files
#pwd = print working directory
f = open('test.txt')
print f.read()

print f.read()
#it will not show up again because cursor is at the end of the txt. Have to reset with f.seek method
f.seek(0)
print f.read()

f.seek(0)

print f.readlines()

#using magic function called write file %% only works in jupiter
#%%writefile new.txt
#First line
#Second line

g = open('New.txt')
print g.read()
g.seek(0)

for line in open('New.txt'):
    #for every line in this object(new.txt), print it.
    print line
