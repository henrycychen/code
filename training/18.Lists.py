#Chapter 18 - Lists
#Indexing and slicing


my_list = [1,2,3]
print my_list

my_list = ['string',23,1.2,'o']
print my_list
print len(my_list)

my_list = ['one','two','three',4,5]
print my_list

print my_list[0]
print my_list[1:]
print my_list[:3]

print 'hello' + ' world'

print my_list + ['new item']

my_list = my_list + ['permanent add']
print my_list

print my_list * 2

l = [1,2,3]
print l
l.append('append me!')
print l

x=l.pop(0)
l.pop()
print x
print l

new_list = ['a','e','x','b','c']
print new_list

new_list.reverse()
print new_list

new_list.sort()
print new_list

l_1 = [1,2,3]
l_2 = [4,5,6]
l_3 = [7,8,9]

matrix = [l_1, l_2, l_3]
print matrix

print matrix[2][0]

first_col = [row[0] for row in matrix]
print first_col
