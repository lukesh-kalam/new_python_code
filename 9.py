import sys
import os
import time
print("This is the name/path of the script:"),sys.argv[0]
srch_file=str(sys.argv[2])
server_name=str(sys.argv[1])
print(server_name)
print(srch_file)
file_search=str(srch_file)
if(server_name=="samailserver5" or "samailserver6" or "mailsles1" or "mailsles2" or "mailaix1" or "mailaix2"):
    cwd = os.getcwd()
    print("Current working directory is:", cwd)
    # change the directory that contain console
    os.chdir('/local/notesdata/IBM_TECHNICAL_SUPPORT')
    cwd = os.getcwd()
    print("Current working directory is:", cwd)	
elif(server_name=="mailwin1" or "mailwin2" or "samailserver1" or "samailserver2") :  
    cwd = os.getcwd()
    print("Current working directory is:", cwd)
    # change the directory that contain console.log
    os.chdir('D:\\Domino\\data\\IBM_TECHNICAL_SUPPORT')
    cwd = os.getcwd()
    print("Current working directory is:", cwd)
else :
    print("Invalid operating system")
try :
        
    with open (file_search, "r") as ifile : 
        for line in ifile :
            if "HCL Domino (r) Server (64 Bit)" in line:
                print(line)
            # checking for OSLOADProgram
            if "OSLoadProgram" in line :
                print(line)
            # checking for server shutdown
            if "Server shutdown complete" in line :
                print(line)
    file = open(file_search,"r")
    Counter = 0
    Content = file.read()
    CoList = Content.split("\n")
    for i in CoList:
        if i:
            Counter += 1
    #print("This is the number of lines in the file")
    #print(Counter)
    f = open(file_search,'r')
    line_num = 0
    search_phrase = "Server shutdown complete"
    for line in f.readlines():
        line_num += 1
        if line.find(search_phrase) >= 0:
    #        print(line_num)
            break 
    leak_line=line_num - 1

    file = open(file_search,'r')
    all_lines = file.readlines()
    for i in range (leak_line,Counter) :
        print(all_lines[i])
except FileNotFoundError as fnf_error:
    print("The console which your are trying to search is not found")

    console_mailsles1_2021_06_11@14_49_10.log