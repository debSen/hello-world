import unittest
import hello_world

test_obj = hello_world.basic_app()
assert(test_obj.print_yes_no() == "yes" or test_obj.print_yes_no() == "no")
assert(test_obj.print_args("Hello world") == "Hello world")
