letters_to_numbers = dict(a=1, b=2, c=3, d=4, e=5, f=6,
                g=7, h=8, i=9, j=10, k=11, l=12,
                m=13, n=14, o=15, p=16, q=17, r=18,
                s=19, t=20, u=21, v=22, w=23, x=24,
                y=25, z=26)
                
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
    
    ## get the encryption
    difference = letters_to_numbers[encoded_clue[0]] - letters_to_numbers[decoded_clue[0]]
    
    answer = ""
    
    ## for every letter in the encoded answer, decrypt it and find the real answer
    for letter in encoded_answer:
        
        ## if its a letter and not spaces , - etc
        if letter in letters_to_numbers.keys():
            decoded_index = letters_to_numbers[letter] - difference
            
            if decoded_index < 0:
                decoded_index = 26 + decoded_index  
            for l, i in letters_to_numbers.iteritems():
                if i == decoded_index:
                     answer += l
                     break
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