import os
cwd = os.getcwd()
print("Current working directory is:", cwd)
os.chdir('C:\\Users\\kalam.kumar\\Desktop\\python1')
cwd = os.getcwd()
print("Current working directory is:", cwd)
useful = []
with open ("console.log", "r") as myfile , open('output.log','a') as addfile :
    for line in myfile:
        if "HCL Domino (r) Server (64 Bit)" in line:
            print(line)
            addfile.write(line)
        if "OSLoadProgram" in line :
            print(line)
            addfile.write(line)
        if "Server shutdown complete" in line :
            print(line)
            addfile.write(line)
        if "Leaked stack" in line:
            break
    for line in myfile:
        useful.append(line)
        a_string = "".join(useful)
        addfile.write(a_string)
        print(a_string)
        
