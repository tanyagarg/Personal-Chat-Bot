import tkinter as tk
from tkinter import *
import tkinter.messagebox
import facebook
import json
import emoji
import os
import csv
import try_mul
root = tk.Tk()
#root.withdraw()
print 'kdjfljerkljgklvjsklgvjbrklj'
token = 'EAACEdEose0cBAEmLZBvPOxyCzStWgl7Vq9ThNZAsP4Qdd8KTiQAUMeoAhpXfc1ZBvBzLA378Wer0DRGLsZBuPsJRvb4fxMbzk9ZAbObuRUPlWb2wVEZCuJBRNrDhn1VpOQq3qbI21trLWnXfPZAsQK1B0Ka9L6UIxvNVjV8u0pdu3FmSH5yrC4cl2d5i06P48MZD'

graph = facebook.GraphAPI(token)
profile = graph.get_object("me")

#frame.pack()
stat=[]

    
def cbc(idd, tex):
    return lambda : callback(idd, tex)
def abc(idd, tex):
    return lambda : like(idd,tex)

def callback(idd, tex):
    profile=graph.get_object('me',fields='posts')    
    posts = graph.get_connections(profile['id'], 'posts')
    #for i in range(0,4):
    #print(posts['data'][idd]['story'])
    comments = graph.get_connections(id=posts['data'][idd]['id'], connection_name='comments')
    print(comments['data'])
    print('hiii')
    #print('.........................')
    likes= graph.get_connections(id=posts['data'][idd]['id'], connection_name='likes',summary='true')
    #print('............')
    #print(likes)
    if(posts['data'][idd]['story']):
        tex.insert(tk.END,'The post is: '+posts['data'][idd]['story'])
    tex.insert(tk.END,'\n')
    if comments['data']==[]:
        #print('no comments')
        tex.insert(tk.END,'Sorry No comments')
    else:
        for j in comments['data']:
            #print(j)
            tex.insert(tk.END,j['from']['name'] + ' ')
            for c in j['message']:
                if c in emoji.UNICODE_EMOJI:
                    #print('jjjj')
                    2
                else:                
                    tex.insert(tk.END,c)
            tex.insert(tk.END,'\n')
        tex.insert(tk.END,'\n')
                #b.append(j['from']['id'])    
    #s = 'At {} f is {}\n'.format(id, id**id/0.987)
    
    tex.see(tk.END)     
    #graph()        # Scroll if necessary
def like(idd,tex):
    profile=graph.get_object('me',fields='posts')    
    posts = graph.get_connections(profile['id'], 'posts')
    likes= graph.get_connections(id=posts['data'][idd]['id'], connection_name='likes')
    tex.insert(tk.END,'The post is: '+posts['data'][idd]['story'])
    tex.insert(tk.END,'\n')
    if likes['data']!=[]:
        for j in likes['data']:
            tex.insert(tk.END,j['name'] + '\n')
        tex.insert(tk.END,'\n')
    tex.see(tk.END)
    #graph()
        
    
def get_comm(m):
    #root = Toplevel()
    print('uuuuuuuuuuuuuuuuuuuuuuuu')
    rt=Toplevel()
    rt.withdraw()
    print 'kjgvndkcnk'
    frame = Frame(root)
    top = tk.Toplevel()
    tex = tk.Text(master=top)
    tex.grid()
    tex.pack(side=tk.RIGHT)
    bop = tk.Frame()
    bop.pack(side=tk.LEFT)
    if(m==0):
        m=5
    for k in range(1,m):
        tv = 'Say {}'.format(k)
        b = tk.Button(bop, text='comments of post '+ str(k), command=cbc(k, tex))
        b.grid(row=k,column=0)
        c = tk.Button(bop, text='likes of post '+str(k), command=abc(k,tex))
        c.grid(row=k,column=1)
        #print ("ghghghg")
   # b.pack(side=tk.LEFT)
   # c.pack(side=tk.LEFT)
#tk.Button(bop, text='Exit', command=top.destroy).pack()
    top.mainloop()
'''def graph():
 root = Tk.Tk()

 f = Figure(figsize=(5,4), dpi=100)
 ax = f.add_subplot(111)

 data = (100, 100)

 ind = numpy.arange(2)  # the x locations for the groups
 width = .5

 rects1 = ax.bar(ind, data, width)

 canvas = FigureCanvasTkAgg(f, master=root)
 canvas.show()
 canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

 tk.mainloop()
'''
#get_comm(0)