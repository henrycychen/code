st = 'Print only the words that start with s in this sentence'

for s_words in st.split():
    if 's' in s_words[0]:
        print s_words

for items in range (0,11,2):
    print items

l = [items for items in range(0,51) if items % 3 == 0]
print l

st = 'Print every word in this sentence that has an even number of letters'
lst = st.split()
print lst
for items in lst:
    if len(items) % 2 == 0:
        print items

x = 0
while x < 101:
    print x
    x += 1
    if x % 3 == 0:
        print 'Fizz'
    if x % 5 == 0:
        print 'Buzz'
    if x % 3 == 0 and x % 5 == 0:
        print 'FizzBuzz'
else:
        print ' all done'

st = 'Create a list of the first letters of every word in this string'
lst1 = st.split()
lst = [items[0][0] for items in st.split()]
print lst

