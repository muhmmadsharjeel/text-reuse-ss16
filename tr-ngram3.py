import nltk, os, io, sys, logging
from nltk.stem.lancaster import LancasterStemmer
from nltk.tokenize import RegexpTokenizer


__author__ = "Muhammad Sharjeel"
__email__ = "s.muhammad6@lancaster.ac.uk"


logging.basicConfig(format='%(asctime)s %(message)s', filename='tr-ngram3.log', level=logging.INFO)

if len(sys.argv) != 4:
        exception = """ The script takes 3 arguments:
        1) The path to the corpus folder.
        2) The path of the output file.
        3) The name of the output file.
        """
        logging.debug(exception)
        raise Exception(exception)


filesDirName = sys.argv[1]
outputPath = sys.argv[2]
outputFile = sys.argv[3]

if not os.path.abspath(filesDirName):
        exception = "The corpus folder does not exist"
        logging.debug("The corpus folder %s does not exist" %filesDirName)
        raise Exception(exception)


if not os.path.exists(outputPath):
        exception = "The output folder does not exist"
        logging.debug("The output folder %s does not exist" %outputPath)
        raise Exception(exception)


filePath = os.path.abspath(filesDirName)
filePath = os.path.join(filePath, "all-plagiarised-files.txt")

outputPath = os.path.abspath(outputPath)

list_of_files = open(filePath,"r")
temp_output = ''

lancaster_stemmer = LancasterStemmer()
stopwords = nltk.corpus.stopwords.words('english')
tokenizer = RegexpTokenizer(r'\w+')

while 1:
	name_of_files = list_of_files.readline()
	if not name_of_files: break
	name_of_files_list = name_of_files.split(",")

	with io.open(os.path.join(filesDirName, name_of_files_list[0]),'r',encoding='utf-8') as file1:
		file1_text = file1.read()
		file1.close()
	file1_text_p = file1_text.lower()
	file1_text_p = tokenizer.tokenize(file1_text_p)
	file1_text_p = [w for w in file1_text_p if not w in stopwords]
	file1_text_p = [lancaster_stemmer.stem(w) for w in file1_text_p]
	

	with io.open(os.path.join(filesDirName, name_of_files_list[1]),'r',encoding='utf-8') as file2:
		file2_text = file2.read()
		file2.close()
	file2_text_p = file2_text.lower()
	file2_text_p = tokenizer.tokenize(file2_text_p)
	file2_text_p = [w for w in file2_text_p if not w in stopwords]
	file2_text_p = [lancaster_stemmer.stem(w) for w in file2_text_p]
	
	similar_tokens = [word for word in file2_text_p if word in file1_text_p]

	similarity_score = round(float(len(similar_tokens))/float(min(len(file1_text_p),len(file2_text_p))), 2)
	temp_output = temp_output + str(similarity_score) + ',' + name_of_files_list[2]

output_file = open(os.path.join(outputPath, outputFile+'.arff'), 'w')
output_file.write('@relation text-reuse\n')
output_file.write('@attribute sim_score numeric\n')
output_file.write('@attribute class {cut,light,heavy,non}\n\n')
output_file.write('@data\n')
output_file.write(temp_output)
	
list_of_files.close()
