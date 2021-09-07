#Creating thread without extending thread class 
import threading 

class test (threading.Thread) :
    def lukesh (self) :
        print("lukesh kumar")
        print(threading.current_thread().getName())
    def kumar (self) :
        print(threading.current_thread().getName())

obj=test()
t=threading.Thread(target=obj.lukesh())
t.start()
t2=threading.Thread(target=obj.kumar())
print(threading.current_thread().getName())    