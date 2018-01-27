import unittest
import hello_world

test_obj = hello_world.print_app()
#print test_obj.print_args("Hello world")
print test_obj.print_yes_no()
assert(test_obj.print_args("Hello world"), "Hello world")
