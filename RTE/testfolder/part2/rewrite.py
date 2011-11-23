file = open("short.xml")

out = open("longRTE2.txt", "wb")
out2 = open("short2.xml", "wb")

x = 0
y = []
for line in file:
	s = line.strip("\t")
	s = s.strip("\n")
	y.append(s)
	x += 1
	print >> out2, s
	
print >> out, y

	
	
