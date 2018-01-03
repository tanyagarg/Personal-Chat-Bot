import tkinter as tk
from tkinter import *
from tkinter import messagebox
import tkinter.messagebox
import facebook
import json
import os
import csv
import emoji
root = tk.Tk()
#root.withdraw()
token = 'EAACEdEose0cBAEmLZBvPOxyCzStWgl7Vq9ThNZAsP4Qdd8KTiQAUMeoAhpXfc1ZBvBzLA378Wer0DRGLsZBuPsJRvb4fxMbzk9ZAbObuRUPlWb2wVEZCuJBRNrDhn1VpOQq3qbI21trLWnXfPZAsQK1B0Ka9L6UIxvNVjV8u0pdu3FmSH5yrC4cl2d5i06P48MZD'

graph = facebook.GraphAPI(token)
profile = graph.get_object("me")
#frame.pack()

#def cbc(idd, tex):
#    return lambda : callback(idd, tex)

def cnt_cmnts(s):
    profile=graph.get_object('me',fields='posts')    
    #print(json.dumps(profile['story'],indent=4))
    cnt=0
    comment=[]
    posts = graph.get_connections(profile['id'], 'posts')
    for i in range(0,4):
        #print (posts['data'][i]['id'])
        #print (posts['data'][i]['story'])
        #print (posts['data'][i]['comments'])
        comments = graph.get_connections(id=posts['data'][i]['id'], connection_name='comments')
        #likes= graph.get_connections(id=posts['data'][i]['id'], connection_name='likes')
        #print('............')
        #print(likes)
        #print(',,,,,,,,,,,,,,,,,,,,,,,,,')
        a=''
        for j in comments['data']:
            
            #print (j)
            #print("helo")
            if comments['data']==[]:
                #print('empty')
                break
            else:
                
                if(j['from']['name'].lower()==s.lower()):
                    #e.insert(tk.END,posts['data'][i]['story']+':\n')
                    #print(j['message'])
                    for c in (j['message']).split():
                        #print(c)
                        f=0
                        for d in c:
                            #print(d)
                            if d in emoji.UNICODE_EMOJI:
                                f=1
                                break
                        if(f==0):
                            #print('.....')
                            #print(c)
                            #print('.....')
                            #e.insert(tk.END,c+'\n')
                            a=a+c;
                            a=a+' '
                    comment.append(a)
                    a=a+'\n'
    cm='The comments displayed by '+s+' are:\n'
    #print (comment)
    for i in comment:
        cm+=i
        cm+='\n'
    messagebox.showinfo('The comments by tushar raina are:',cm)
#cnt_cmnts()
def get_comms(s):
    
    cnt_cmnts(s)
#tk.Button(bop, text='Exit', command=top.destroy).pack()
    #top.mainloop()
#get_comms('Tushar Raina')