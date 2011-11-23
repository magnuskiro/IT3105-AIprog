import orange, orngTest
import random
import features

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

def run(cross=True, verbose=False, learning_data="learningdata.tab"):
    filename = "results_part3.txt"
    clean_file(filename)
    data = orange.ExampleTable(learning_data)
    l = orange.BayesLearner(data)
    if cross:
        features.run() # extracts the features
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

#run() # runs the learning
#run(False) # runs the writing to results file.