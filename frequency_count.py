freq = dict()
with open("output.txt") as f:
    for line in f:
        page = line.split(",")[1]
        if page in freq:
            freq[page] = freq[page] + 1
        else:
            freq[page] = 1

for key, value in freq.iteritems():

    print value
    