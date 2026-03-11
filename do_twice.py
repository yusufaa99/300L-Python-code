def do_twice(f):
    f()
    f()

def print_text():
    print ("Hello")

do_twice(print_text)
