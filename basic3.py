#Creating threading by extending thread class
import threading
class lukesh(threading.Thread) :
    def run(self) :
        print(threading.current_thread().getName())
class hello(threading.Thread) :    
    def kumar (self) :
        print(threading.current_thread().getName())
t = hello()
t.start()
t1 = lukesh()
t1.start()
t.join()
print(threading.current_thread().getName())