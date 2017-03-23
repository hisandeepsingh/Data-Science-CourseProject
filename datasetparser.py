
#
fname = raw_input('Enter the file name:')

#Filehandler to read the data in file.
fhand = open(fname, "r+")

# open file for appending or it will create a new file if file is not present
outfile = open("output.txt","w") 

for line in fhand:
    line = line.rstrip()
    words = line.split()
    outfile.write(words[0] + "," + words[6] + "\n")
	
print "\n Execution Completed Succesfully. \n"

    #print (words[0], words[6])
    