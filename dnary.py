# Code for storing the multiple pages by a same host in a dictionayy
#with key as host address and list of webpages as value in python dictionary.

import csv   #to generate csv file
import operator

dict_lookup = {}
dict_lookup2 = {}
sorted_list = [] #A[]
freq_list = []		#B[]

fname = raw_input("Enter the file name to store in dictionary:")
fhand = open(fname, "r+")
for line in fhand:  # reading each line of file line by line with for loop.
    words = line.split(",")  # splitted the line into words with two attributes
    host = words[0]          #value of host address is contained in words[0]
    value = words[1].replace('\n','')         #value of web pages is contained in words[1]
    key = host               				# taking host address as key of dictionary
    if key in dict_lookup:
		if any(value in s for s in  dict_lookup[key]):  #removing duplicate entries
			continue                                    #removing duplicate entries
		else:
			dict_lookup[key].append(value)
    else :
	    dict_lookup[key] = [value]
	    

outfile = open("sorted2.txt","w") 		
for sorted_key in sorted(dict_lookup, key=lambda k: len(dict_lookup[k]), reverse= False):
    outfile.write(sorted_key + "$" + ",".join(dict_lookup[sorted_key]).replace('\n','') + "\n")
    sorted_list.append(dict_lookup[sorted_key])

max = 0
freq = 0
for x in sorted_list:
	freq = 0
	for y in sorted_list:
		if set(x).issubset(set(y)):
			freq = freq + 1
	freq_list.append(freq)
	if freq > max:
		max = freq

final_opt = set();		
for idx, x in enumerate(freq_list):
	if max == x:
		final_opt.append(sorted_list[idx])
print final_opt