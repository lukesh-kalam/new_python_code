#Creating threading by extending thread class
import threading
class lukesh(threading.Thread):
    def run(self):
        print(threading.currentThread().getName())
class kumar(threading.Thread) :
    def luk(self) :
        print(threading.current_thread().getName())
b=kumar()
b.start()
a = lukesh()
a.start()
print(threading.current_thread().getName())