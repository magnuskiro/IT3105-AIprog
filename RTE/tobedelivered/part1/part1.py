import part1d
import part1c
import part1a
import part1b
import make_predictions
from xml.sax.handler import ContentHandler
from xml.sax import parse

def run(dev, processed):
	
	file_name = "RTE2_dev.preprocessed.xml"
	data_set = part1a.run()
	texts = data_set[0]
	hypos = data_set[1]
	
	parta = "wordmatches.txt"
	partb_1 = "lemma_matches.txt" 
	partb_2 = "pos-tag_matches.txt" 
	partc = "bleuresults.txt"
	partd = "idfresults.txt"
	
	partd_threshold = 0.9670
	partc_threshold = 0.2690	
	parta_threshold = 0.8190
	partb_1_threshold = 0.9170 
	partb_2_threshold = 0.5790
	
	part1b.run(file_name)
	part1c.run(texts, hypos)
	part1d.predict(texts, hypos)
	make_predictions.predict(parta_threshold, parta)
	make_predictions.predict(partb_1_threshold, partb_1)
	make_predictions.predict(partb_2_threshold, partb_2)
	make_predictions.predict(partc_threshold, partc)
	make_predictions.predict(partd_threshold, partd)
	

