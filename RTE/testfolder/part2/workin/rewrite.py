def run(file_name):
	print "Rewriting xml-file ...",
	in_file = file_name
#	in_file = "RTE2_dev.preprocessed.xml"
	#in_file = "error.xml"
	file = open(in_file)
	out_file = ""
	if file:
		out_file = "formattedRTEdata.xml"
		#out_file = "formattederror.xml"
		out = open(out_file, "wb")
		if out:
			x = 0
			for line in file:
				s = line.strip("\t")
				s = s.strip("\n")
				x += 1
				print >> out, s
			out.close()
		else:
			print "Error writing to file"
		file.close()
	else:
		print "Error reading from file"
	
	print "done"
	return out_file
	
	
