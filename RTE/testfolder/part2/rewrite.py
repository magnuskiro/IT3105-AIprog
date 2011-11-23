in_file = "RTE2_dev.preprocessed.xml"
#in_file = "error.xml"
file = open(in_file)

out_file = "formattedRTEdata.xml"
#out_file = "formattederror.xml"

out2 = open(out_file, "wb")

x = 0
for line in file:
	s = line.strip("\t")
	s = s.strip("\n")
#	s = s.lower()
	x += 1
	print >> out2, s
	
	
	
