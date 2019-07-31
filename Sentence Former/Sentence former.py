import letters

def maker():
    sentence=input()
    sentence_size=int(input())
    sentence_matrix=letter=[[] for i in range(sentence_size)]
    sentence=sentence.upper()
    command = 'letter+=letters.{}({})'
    for i in sentence:
        for j in range(sentence_size):
            exec(command.format(i,sentence_size))
            sentence_matrix[j] = sentence_matrix[j]+letter[j]
            
    letters.print_matrix(sentence_matrix)


    
