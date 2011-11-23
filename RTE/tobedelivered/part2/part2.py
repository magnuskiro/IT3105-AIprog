import rewrite
import part2a
import predict
import make_predictions

def init(file_name):
	print "Starting part II"
#	step_size = 0.001
	threshold = 0.6160
	processed_file = rewrite.run(file_name)
	result = part2a.run(processed_file)
#	predict.predict(step_size, result)
	make_predictions.predict(threshold, result)	# writes predictions to file, does not run eval.py
	print "Part II done"
	
init("RTE2_dev.preprocessed.xml")
