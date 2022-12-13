import re

def split(txts):
    with open(txts, 'r') as f:
        file= f.read()

	 #We gonna make use of Negative 'LOOKBEHIND' assertions in regular expressions
    # negative lookbehind assertions (?<!), means with the exception of what ever is followed by.
    #The pattern below says, with the exception of Mr, MRS, DR, white spaces, and full stop followed by 'lower case letter'
    pattern1=r'(?<!Dr)(?<!Mrs)(?<!Mr)\.\s([A-Z])'
    #Whereever there is a period, add new a line with the exceptions of the conditions
    replace1=r'.\n\1'
    file = re.sub(pattern1, replace1, file)
    #By using regular expression, new patterns are to be formed and replace by new replacement pattern
    #After every exclmation mark, we add a new line, the above conditions is applied here as well, 
    #conidering if it followed by white space and/or lower case letter
    pattern2='!\\s'
    replace2='!\n'
    file = re.sub(pattern2,replace2 , file)

 	#after every question mark, a new line is to be added, with exception of not being followed by white space and upper case letter
    pattern3='\\?\\s'
    replace3='?\n'
    file = re.sub(pattern3, replace3, file)
    #print file/texts after all the ocnditions met
    print (file)

#call the fucntion
split('split.txt')