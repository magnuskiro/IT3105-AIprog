file = open("RTE2_dev.preprocessed.xml")

out = open("RTE2.txt", "wb")

x = 0
y = []
for line in file:
	s = line.strip("\t")
	s = s.strip("\n")
	y.append(s)
	x += 1
	
print >> out, y

	
	
