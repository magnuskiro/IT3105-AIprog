import rewrite
import part2a
import predict

def init(file_name):
	print "Starting part II"
	step_size = 0.001
	processed_file = rewrite.run(file_name)
	result = part2a.run(processed_file)
	predict.predict(step_size, result)
	print "Part II done"
	
init("RTE2_dev.preprocessed.xml")
