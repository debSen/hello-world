#!/usr/bin/env python
import requests

class print_app(object):
    def __init__(self):
        pass
    
    def print_args(self,args):
        print args
        
    def print_yes_no():
        req = requests.get('https://yesno.wtf/api')
        req_dict = req.json()
        print req_dict['answer']
    

Obj = print_app()
#Print "Hello World"
Obj.print_args("Hello World!")