import random

name = 'utag.txt'
infile = open('../db_book_u12850b22040.full/'+name)
outfile = open(name,'w')
for line in infile.readlines():
	if random.random()<=0.32:
		outfile.write(line)
infile.close()
outfile.close()
	
