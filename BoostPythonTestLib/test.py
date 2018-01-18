import BoostPythonTestLib as Demo

i = 0

class CallbackInstanceObj(object):
    def __init__(self):
        pass
    
    def callback(self):
        global i
        print("Callback on instance object worked.")
        i = 456   


def callback():
    print("Callback on static method worked.")
    
def callback_with_args(*args):
    print("Callback on static method worked. Args are {}".format(args))

# static

def set():
    Demo.set_callback(callback)
    
def call():
    Demo.callback()

def seti():
    inst = CallbackInstanceObj()
    Demo.set_callback(inst.callback)
##############################################
def setA():
    Demo.set_callback(callback_with_args)

def callA():
    Demo.callback("These are the python args")
##############################################
#Demo.set_callback(inst.callback)
#Demo.callback()
#set()
#call()

if __name__ == "__main__":
    import sys
    sys.argv
    print("Running Tests ... ")
    
    set()
    call()
    
    if 'i' in sys.argv:    
        seti()
        call()
        
    if 'a' in sys.argv:
        setA()
        callA()
    
    # Demo.set_callback(None)
    print("Finished Test")




