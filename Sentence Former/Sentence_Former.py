from Letters import *
from sys import argv

if(__name__=="__main__"):
        sentence = argv[1]
        letter_size = int(argv[2])
        sentence = sentence.upper()
        output = [ [] for i in range(letter_size) ]
        for i in sentence:
                if(i.isalpha()):
                        exec("curr_letter = {}({})".format(i,letter_size))
                else:
                        curr_letter = empty_matrix(letter_size)
                for j in range(len(curr_letter)):
                        output[j]+=curr_letter[j]+[" "]

        print_matrix(output)