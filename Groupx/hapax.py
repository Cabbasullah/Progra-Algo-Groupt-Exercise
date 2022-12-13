import re

def hapx(txts):
    with open(txts, 'r') as f:
        file= f.read()

    #list of the words are all contained in occurance{}
    occurance = {}

    #open file with the name of the file in the open()
    file=open("hapax.txt", 'r')
    #Here is the first use of regular expressions. It is very convinient 
    #as in this case with the 're.findll) will find all the text in our file and read it, file.read()
    #If you print 'list' here you will get all the text in hapax
    list=re.findall("\w+", file.read())


    #we gonna loop through and iterate over the list
    for word in list:
        #we are utilizing frequency here in order to find the hapaxes, 
        #Using 'get'to get the frequency of all the elements
        #This will calculate the frequency of each word in the list if you print 'occurance'
        occurance[word]= occurance.get(word, 0) + 1
        #Since our target is to print the hapaxes,
        #we will iterate over the the current word in occurance 
    for word in occurance:
        #to calculate occurance of the hapax, we set the the occurance wuth the index equal to 1, 
     if occurance[word]==1:
         #print word and it will print al the words with 1 occurance
         print(word)
        
hapx('hapax.txt')
    


    
    
    
    
