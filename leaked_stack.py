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
if(server_name=="samailserver5" or "samailserver6" or "mailsles1" or "mailsles2"):
    cwd = os.getcwd()
    print("Current working directory is:", cwd)
    # change the directory that contain console.log
    #os.chdir('C:\\Users\\kalam.kumar\\Desktop\\python1')
    os.chdir(/local/notesdata/IBM_TECHNICAL_SUPPORT)
    cwd = os.getcwd()
    print("Current working directory is:", cwd)
elif(server_name=="mailwin1" or "mailwin2" or "samailserver1" or "samailserver2") :  
    cwd = os.getcwd()
    print("Current working directory is:", cwd)
    # change the directory that contain console.log
    #os.chdir('C:\\Users\\kalam.kumar\\Desktop\\python1')
    os.chdir('D:\\Domino\\data\\IBM_TECHNICAL_SUPPORT')
    cwd = os.getcwd()
    print("Current working directory is:", cwd)
elif(server_name=="mailaix1" or "mailaix2") :
    cwd = os.getcwd()
    print("Current working directory is:", cwd)
    # change the directory that contain console.log
    os.chdir('C:\\Users\\kalam.kumar\\Desktop\\python1')
    cwd = os.getcwd()
    print("Current working directory is:", cwd)
else :
    print("Invalid operating system")

myfile= open (file_search, "r") 
addfile= open(filename,'a') 
for line in myfile :
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
file = open(file_search,"r")
Counter = 0
Content = file.read()
CoList = Content.split("\n")
for i in CoList:
	if i:
		Counter += 1
print("This is the number of lines in the file")
print(Counter)

f = open(file_search,'r')
line_num = 0
search_phrase = "Leaked stack"
for line in f.readlines():
    line_num += 1
    if line.find(search_phrase) >= 0:
        print(line_num)
        break 
leak_line=line_num - 1

file = open(file_search,'r')
addfile = open(filename,'a')
all_lines = file.readlines()
for i in range (leak_line,Counter) :
  print(all_lines[i])
  addfile.write(all_lines[i])
  
  
myfile.close()
addfile.close()
