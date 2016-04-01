with open("result.txt", "w") as text_file:
    text_file.write("Works!")

#f = open("pyyython.txt")
#print f.read()
#f.close()


with open('pyyython.txt', 'r') as document:
    websites = {}
    for line in document:
        line = line.split()
        websites[line[0]] = line[1:]

for k,v in websites.iteritems():
    print k,v
