from chatterbot import ChatBot
#from comments_display import get_comm
from fuzzywuzzy import fuzz
from newly_added import ExtractMainLinks
import nltk
from newmailsend import mainn
from post_front import comments_friend
import tkinter as tk
print 'dkfLJCLsmcLmas'
import try_mul
from my_merging_method import maaiinn
print 'jkdsjfcjalDMK'
root = tk.Tk()

try:
    import ttk as ttk
    import ScrolledText
except ImportError:
    import tkinter.ttk as ttk
    import tkinter.scrolledtext as ScrolledText
import time
#root.withdraw()
class TkinterGUIExample(tk.Tk):
    print 'dmkmfmdsmf'
    def __init__(self, *args, **kwargs):
        """
        Create & set window variables.
        """
        tk.Tk.__init__(self, *args, **kwargs)
        
        self.chatbot = ChatBot(
            "GUI Bot",
            storage_adapter="chatterbot.storage.SQLStorageAdapter",
            logic_adapters=[
                "chatterbot.logic.BestMatch"
            ],
            input_adapter="chatterbot.input.VariableInputTypeAdapter",
            output_adapter="chatterbot.output.OutputAdapter",
            database="../database.db"
        )

        self.title("Chatterbot")

        self.initialize()

    def initialize(self):
        """
        Set window layout.
        """
        self.grid()

        self.respond = ttk.Button(self, text='Get Response', command=self.get_response)
        self.respond.grid(column=0, row=0, sticky='nesw', padx=3, pady=3)

        self.usr_input = ttk.Entry(self, state='normal')
        self.usr_input.grid(column=1, row=0, sticky='nesw', padx=3, pady=3)

        self.conversation_lbl = ttk.Label(self, anchor=tk.E, text='Conversation:')
        self.conversation_lbl.grid(column=0, row=1, sticky='nesw', padx=3, pady=3)

        self.conversation = ScrolledText.ScrolledText(self, state='disabled')
        self.conversation.grid(column=0, row=2, columnspan=2, sticky='nesw', padx=3, pady=3)
    
    def get_response(self):
        """
        Get a response from the chatbot and display it.
        """
        user_input = self.usr_input.get()
        #user_input = "hello"
        user_input=user_input.lower()
        self.usr_input.delete(0, tk.END)
        print(user_input)
        
       # user_input = self.usr_input.get()
        #if(user_input=="hi"):
         #   comments_friend('comment')
          #  print "hurr"
           # root.geometry("200x200")
            #for i in range(4):
             #   window = tk.Toplevel()
              #  window.geometry("200x200")
            #self.initialize1()
        #response = self.chatbot.get_response(user_input)
        #response = "kidda veere "
        if(self.checkplace(user_input)==True):
            ww=nltk.word_tokenize(user_input)
            ExtractMainLinks(ww[0])
            response='Please check the folder D:\project_with_chitti\scripts\placement_papers'
        elif(self.check_facebook(user_input)==True):
            print "facebook it is"
            response="facebook it is"
            comments_friend(user_input)
            print "hurr"
            root.geometry("200x200")
            for i in range(4):
                window = tk.Toplevel()
                window.geometry("200x200")
        ##now i have to extract its to, subject and text
        elif(self.check_mail(user_input)==True):
            print  "input it is"
            response="facebook it is"
            x=nltk.word_tokenize(user_input)
            f=1;
            flag=100
            to_random=""
            text=""
            for i in x:
                if flag==2:
                   to_random=x
                   flag=3
                   continue
                if i =="to":
                   flag=2
                if flag==3:
                    print "huuhuhu"
                    text=text+str(i)
                    print i
                    text=text+" "
            to=self.find_email(x)
            print "mail to"
            print to
            print "text is"
            print text
            ##call the mail function
            #call(to,subject,text)
            response=text + "has been mailed to " + to
            mainn(to,text)
        else:
            response= "something else"
        #response = "kidda veere"
        self.conversation['state'] = 'normal'
        self.conversation.insert(
            tk.END, "Human: " + user_input + "\n" + "ChatBot: " + str(response) + "\n"
        )    
        self.conversation['state'] = 'disabled'
        
        

        time.sleep(0.5)
    def check_facebook(self,x):
        faceb=['post','comment','message','likes','fb','status','comments']
        x2=nltk.word_tokenize(x)
        print x2
        for x1 in x2: 
            print x1
            if x1 in faceb:
                print "yo"+" "+ x1
                return True
            
        return False
    def checkplace(self,x):
        mails=['geeks','placement','update','download']        
        x2=nltk.word_tokenize(x)
        print "x"
        for x1 in x2:
            if x1 in mails:
                return True
        return False
    def check_mail(self,x):
        mails=["send","mail","email","inbox","unread","draft","gmail"]        
        x2=nltk.word_tokenize(x)
        print "x"
        for x1 in x2:
            if x1 in mails:
                return True
        return False
    
    def extract_email(self,x,to,subject,text,pre):
        if(pre==1):
           to=x
        elif(pre==2):
           text=x
        else:
           subject=x
        return to,text,subject
    def find_email(self,x):
        a=["utkarshbar06@gmail.com","rishab954@gmail.com","gupta.anchal2612@gmail.com","rainatushar221995@gmail.com","jainunique1997@gmail.com"]
        email=""
        ratio=0
        for i in a:
            ratio1= fuzz.partial_ratio(i,x)
            if(ratio1>ratio):
                ratio=ratio1
                email=i
        return email

gui_example = TkinterGUIExample()
gui_example.mainloop()