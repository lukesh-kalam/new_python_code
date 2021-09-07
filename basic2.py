from threading import*
def lukesh() :
    print("lukesh kumar")
    print(current_thread().getName())
def kumar() :
    print(current_thread().getName())
def sunny() :
    print(current_thread().getName())
t=Thread(target=lukesh)
t1=Thread(target=kumar)
hello=Thread(target=sunny)
t.start()
t1.start()
hello.start()
print(current_thread().getName())