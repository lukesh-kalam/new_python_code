try :
    with open (file_search, "r") as ifile :
    # , open(filename,'a') as addfile :
    #    addfile.chmod(777)
    #myfile= open (file_search, "r") 
    #addfile= open(filename,'a') 
        for line in ifile :
            if "HCL Domino (r) Server (64 Bit)" in line:
                print(line)
        #        addfile.write(line)
            # checking for OSLOADProgram
            if "OSLoadProgram" in line :
                print(line)
        #      addfile.write(line)
            # checking for server shutdown
            if "Server shutdown complete" in line :
                print(line)
            #   addfile.write(line)
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
    search_phrase = "Leaked stack"
    for line in f.readlines():
        line_num += 1
        if line.find(search_phrase) >= 0:
    #        print(line_num)
            break 
    leak_line=line_num - 1

    file = open(file_search,'r')
    #addfile = open(filename,'a')
    all_lines = file.readlines()
    for i in range (leak_line,Counter) :
    print(all_lines[i])
    #addfile.write(all_lines[i])    
except FileNotFoundError as fnf_error :
    print("file not found")

