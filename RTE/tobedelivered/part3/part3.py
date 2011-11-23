# calls classify cross
    # extracts the features
# calls classify with learningdata
import os
import classifier

def run(xml_data="../xml/RTE2_dev.xml"):

    #the ML, learning and classifying the data set.
    # the classifier imports and runs the features.py file to extract the features.
    # remember to out comment the two run statements at end of file.
    classifier.run()
    classifier.run(False)

    #evaluating the results of part3 classification.
    os.system(os.getcwd() + "/eval_rte.py "+ xml_data+ " " + os.getcwd()+"/results_part3.txt")

run()