import time

def do_work():
    """This function simulates doing work that takes some amount of time.

    It's here to demonstrate offloading work from webservers to backend workers.
    Because a lot of that time in the Real World(tm) may be spent waiting for DB calls to return, I don't feel that it's necessary to make this max out the CPU while executing.
    """
    time.sleep(0.1) # Do work for 100 ms.
