#!/usr/bin/env python
import requests

class basic_app(object):
    def __init__(self):
        pass
    
    def print_args(self,args):
        return args
        
    def print_yes_no(self):
        req = requests.get('https://yesno.wtf/api')
        req_dict = req.json()
        return req_dict['answer']
    
    def generate_random_name(self):
        req = requests.get('http://uinames.com/api/')
        req_dict = req.json()
        return req_dict['name']
    
if __name__== "__main__":
    pass
    #Obj = basic_app()
    #print "Hello World"
    #Obj.print_args("Hello World!")
