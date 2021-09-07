fin = open("secrets.txt", "rt")
#output file to write the result to
fout = open("mailsles2vop.ldif", "wt")
#for each line in the input file
for line in fin:
	#read replace the string and write to output file
	fout.write(line.replace('.nsf', '.nsf'+line))
#close input and output files
fin.close()
fout.close()