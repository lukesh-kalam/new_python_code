useful = []
with open ('console_mailsles1_2020_05_29@14_19_22.log', "r") as myfile , open('lukesh.txt','a') as addfile :
    
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

quit()