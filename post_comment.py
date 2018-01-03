import facebook
import json
import os

token = 'EAACEdEose0cBAEmLZBvPOxyCzStWgl7Vq9ThNZAsP4Qdd8KTiQAUMeoAhpXfc1ZBvBzLA378Wer0DRGLsZBuPsJRvb4fxMbzk9ZAbObuRUPlWb2wVEZCuJBRNrDhn1VpOQq3qbI21trLWnXfPZAsQK1B0Ka9L6UIxvNVjV8u0pdu3FmSH5yrC4cl2d5i06P48MZD'


graph = facebook.GraphAPI(token)
profile = graph.get_object("me")
def post_cmm(s):
    graph.put_object(parent_object='me', connection_name='feed',message=s)
#post_comm('hello world')