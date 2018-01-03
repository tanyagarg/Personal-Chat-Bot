import nltk
import csv
from cnt_cmnts import get_comms
from comments_display import get_comm
from post_comment import post_cmm
'''def check_word(sentence):
    tokens=nltk.word_tokenize(sentence)
    for word in sentence.split():
        if(word=='Comment' or word=='comment' or word=='Comments' or word=='comments'):
            comments(sentence)
        elif(word=='Post' or word=='POST' or word=='post'):
            post(sentence)
'''           
            
def post(sentence):
    f=0
    tokens=nltk.word_tokenize(sentence)
    for word in tokens:
        if(word=='Post' or word=='POST' or word=='post'):
            f=1
        if(f==1):
            break
    if(f==1):
        post_cmm('hello world')
    
            
def comments(sentence):
    s=0
    k=0
    f=0
    l=0
    print 'nfjkdkvnhjkds'
    for i in sentence.split():
        if(i=='Comment' or i=='comment' or i=='comments' or i=='Comments' or i=='likes' or i=='Likes' or i=='like' or i=='Like'):
            for j in sentence.split():
                print j
                print '............,,,,,,,,,,,'
                if(j=='1' or j=='2' or j=='3' or j=='4' or j=='5' or j=='6' or j=='7' or j=='8' or j=='9'):
                    k=int(j)
                    print k
                    print '........................'
                    f=1
                    break
            l=1
    print k
    if(f==1):
        get_comm(k)
    elif(l==1):
        get_comm(k)
    else:
        post(sentence)        
    
def comments_friend(sentence):
    flag=1
    s=""
    print "bkl"
    with open('commentsfrnd.csv', mode='r') as f:
        reader = csv.reader(f)
        for i in reader:
            x=i[0].split()
            for word in sentence.split():
                #print(word)
                for j in x:
                    if(word.lower()==x[0].lower() and s==''):
                        f=1
                        s=s+word
                        s=s+' '
                        s=s+x[1]
    
    print s
    print 'kdvccczfdlsjcfslkJCklsjzlckj'
    if(s!=''):
        get_comms(s)
    else:
        comments(sentence)                    
