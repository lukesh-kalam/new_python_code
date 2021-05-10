import sys
import os
import time
print("This is the name/path of the script:"),sys.argv[0]
print("Number of arguments:",len(sys.argv))
print("Argument List:",str(sys.argv[1]))
print("Argument List:",str(sys.argv[2]))
srch_file=str(sys.argv[2])
server_name=str(sys.argv[1])
print(server_name)
print(srch_file)

time = time.strftime("%Y%m%d_%H%M%S")
print(time)
b=str(time)
#server_name=input("enter the server name :- ")
a="leaked_stack"
#srch_file=input("enter the log file to serach :- ")
file_search=str(srch_file)
d=str(server_name)
filename=a+'_'+d+'_'+b
print(filename)
if(server_name=="samailserver5" or "samailserver6" or "mailsles1" or "mailsles2" or "mailaix1" or "mailaix2") :
    cwd = os.getcwd()
    print("Current working directory is:", cwd)
    # change the directory that contain console.log
    #os.chdir('C:\\Users\\kalam.kumar\\Desktop\\python1')
    os.chdir('/local/notesdata/IBM_TECHNICAL_SUPPORT')
    cwd = os.getcwd()
    print("Current working directory is:", cwd)
elif(server_name=="mailwin1" or "mailwin2" or "samailserver1" or "samailserver2"):
    cwd = os.getcwd()
    print("Current working directory is:", cwd)
    # change the directory that contain console.log
    #os.chdir('C:\\Users\\kalam.kumar\\Desktop\\python1')
    os.chdir('D:\\Domino\\data\\IBM_TECHNICAL_SUPPORT')
    cwd = os.getcwd()
    print("Current working directory is:", cwd)
else :
    print("Invalid operating system")

useful = []
with open (file_search, "r") as myfile , open(filename,'a') as addfile :
    for line in myfile:
        # Checking for domino version 
        if "HCL Domino (r) Server (64 Bit)" in line:
            print(line)
            addfile.write(line)
        # checking for OSLOADProgram
        if "OSLoadProgram" in line :
            print(line)
            addfile.write(line)
        # checking for server shutdown
        if "Server shutdown complete" in line :
            print(line)
            addfile.write(line)
        # checking for leaked stack
        if "Leaked stack" in line:
            break
        # Storing the content after shutdown word 
    for line in myfile:
        useful.append(line)
        a_string = "".join(useful)
        addfile.write(a_string)
        print(a_string)
    myfile.close()
    addfile.close()
exit()
