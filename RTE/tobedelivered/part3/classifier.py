import orange, orngTest
import random
import features

# validation performs cross validation on the 10 subsets of our data.
def validation(data):
    k = 10
    data_list = list(data)
    split_size = len(data_list) / 10
    acs = []
    for i in range(k):
        random.shuffle(data_list)
        splitted_data_sets = list(split(data_list,split_size))
        accurancy = 0
        for j in range(k):
            validation_list = splitted_data_sets[j]
            training = []
            for s in splitted_data_sets:
                if s == validation_list: continue
                training += s
            l = orange.BayesLearner(training)
            count = 0
            for item in validation_list:
                if item.getclass() == l(item):
                    count += 1
            accurancy += float(count) / len(validation_list)
        acs.append(accurancy)
    return sum(acs) / float(k) / float(k)

def split(data,split_size):
    i = 0
    while i < len(data):
        yield data[i:i+split_size]
        i += split_size

def clean_file(filename):
    file = open(filename, "wb")
    file.write("")
    file.close()

def run(cross=True, verbose=False, xml="../xml/RTE2_dev.xml", pre_processec_xml="../xml/RTE2_dev.preprocessed.xml"):
    learning_data="learningdata.tab" # the data features. extracted from an earlier run of features.
    filename = "results_part3.txt"
    clean_file(filename)
    if cross: features.run(xml, pre_processec_xml) # extracts the features
    data = orange.ExampleTable(learning_data)
    l = orange.BayesLearner(data)
    if cross:
        if verbose:
            print "result: ", validation(data)
            for item in data:
                if item.getclass() != l(item):
                    print '\033[1;41m'
                    print item, l(item),
                    print '\033[1;m'
                    print
                else:
                    print item, l(item)
        else:
            print "result: ", validation(data)
    else:
        file = open(filename, "a")
        file.write("ranked: no\n")
        if file:
            for item in data:
                s = str(item['id']) +" "+ str(l(item))
                file.write(s+"\n")
        else:
            print "Error opening file"
        file.close()
        print "finished writing to results_part3"

#run(True, False, "../xml/blind-test-data.xml") # runs the learning
#run(False) # runs the writing to results file.