from circularlinkedlist import CircularLinkedList
                
all_letters = "abcdefghijklmnopqrstuvwxyz"

letters_linked = CircularLinkedList()
for letter in all_letters:
    letters_linked.add_node(letter)
        
def main(option):
    if option.lower() == "i":
        decode_from_input()
    elif option.lower() == "t":
        decode_from_textfile()
        
def decode_from_input():
    encoded_clue = raw_input('Enter encoded clue: ').lower()
    clue = raw_input('Enter clue (decoded): ').lower()
    encoded_answer = raw_input('Enter encoded answer: ').lower()
    
    answer = decode_given_clues(encoded_clue, clue, encoded_answer)
            
    print "Answer: %s"%answer

def decode_from_textfile():
    encoded_clue = 0
    clue = 1
    encoded_answer = 2
    textfile = "answers.txt"
    all_answers = []
    
    f = open(textfile)
    for line in f:
        all_clues = [x.lower() for x in line.split("|")]
        answer = decode_given_clues(all_clues[encoded_clue], all_clues[clue], all_clues[encoded_answer])
        all_answers.append(answer.rstrip("\n"))
        
    for i, ans in enum(all_answers, start=1):
        print "Answer %d: %s"%(i, ans)
        
def decode_given_clues(encoded_clue, decoded_clue, encoded_answer):
    
    ## get the encryption by comparing the first letter
    difference = letters_linked.get_node_position_by_data(encoded_clue[0]) - letters_linked.get_node_position_by_data(decoded_clue[0])
    
    ## since we are "moving forward" on the list:
    ## if difference is negative, we convert it to positive
    ## if difference is positive, we take 26 - the difference
    if difference < 0:
        difference = difference * -1
    if difference > 0:
        difference = 26 - difference
    
    answer = ""
    
    ## for every letter in the encoded answer, decrypt it and find the real answer
    for letter in encoded_answer:
        
        index_of_letter = letters_linked.get_node_position_by_data(letter)
        
        ## if its a letter and not spaces , - etc
        if  index_of_letter != -1:
            decoded_letter = letters_linked.get_node_data_by_traversing_from(index_of_letter, difference)
            answer += decoded_letter

        else:
            answer += letter
            
    return answer
    
def enum(seq, start=0):
    """
        Custom enum method to start enumeration at a specific integer. Default is 0. In most cases, i let it be 1.
    """
    for i, x in enumerate(seq):
        yield i+start, x
    
    
if __name__ == '__main__':
    from optparse import OptionParser

    usage = 'Specify decode by input (i) or read from existing textfile (t).'

    parser = OptionParser(usage)

    opts, args = parser.parse_args()

    if 1 != len(args):
        parser.error('Missing argument: Specify decode by input or read from existing textfile. (i)nput, (t)extfile')

    main(args[0])