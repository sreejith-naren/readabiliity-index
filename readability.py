import math

def char_counts(s):
    acc= 0
    for i in s:
        if i.isalnum():
            acc+= 1
    return acc  


def word_counts(s):
    acc=0
    for i in s:
        if i ==" ":
            acc+= 1
    return acc  


def sent_counts(s):
    acc=0
    for i in s:
       if i=='.' or i=='?' or i=="!":
        acc+= 1
    return acc

def sent_empty(s):
    if "." or "!" or "?" not in s:    
     return None    

def ari_calc(s):
    result= math.ceil(4.71*char_counts(s)/word_counts(s)+0.5*(word_counts(s)/sent_counts(s))-21.43)
    values={
          1:"5-6 Kindergarten",
          2:"6-7 First Grade",
          3:"7-8 Second Grade",
          4:"8-9 Third Grade",
          5:"9-10 Fourth Grade",
          6:"10-11 Fifth Grade",
          7:"11-12 Sixth Grade",
          8:"12-13 Seventh Grad",
          9:"13-14 Eighth Grade",
          10:'14-15 Ninth Grade',
          11:'15-16 Tenth Grade',
          12:'16-17 Eleventh Grade',
          13:'17-18 Twelfth Grade',
          14:'18-22 College student'
          }

    return values[result]


    return result

    
















#result= 4.71(char_count/word_count)+0.5(word_count/sent_count)    



#print(char_counts("hi my name is sreejith"))         
#print(word_counts("hi my name is sreejith")) 
#print(sent_counts("hi my name is sreejith.iam fine!"))        
