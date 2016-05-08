#!/usr/bin/env python

class print_app(object):
    def __init__(self):
        pass
    
    def print_args(self,args):
        print args
    

Obj = print_app()
Obj.print_args("Hello World!")
