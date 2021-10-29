import os,sys,time
class ldif_creation :
    def __init__(self):
        pass
    def input_arguments(self) :
        server_name=str(sys.argv[1])
        file_name=str(sys.argv[2])
        person_name=str(sys.argv[3])
        print(server_name)
        print(file_name)
        print(person_name)
        os.chdir('/local/notesdata')
        files=os.path.isfile(file_name)
    #    print(files)
        if files==True :
            print("File already exists with the name :- " ,file_name,"try with other name")
        else :
            obj.cmd(server_name,file_name,person_name)
    def cmd(self,server_name,file_name,person_name) :
        file_name=str(sys.argv[2])
    #    os.chdir('/local/notesdata')
        path=str('/opt/hcl/domino/bin/ldapsearch -h ')
        server=str(server_name)
        add='  -L '
        add1=str("'(&(Objectclass=DominoPerson)(mail=")
        person=str(person_name)
        add2=str("))'  >  ")
        file=str(file_name)
        whole=path+server+add+add1+person+add2+file
        print(whole)
        os.system(str(whole))
        print("creating ldif file ")
        time.sleep(10)
        os.chdir('/local/notesdata')
        files=os.path.isfile(file_name)
        if files==True :
            print("Ldif file created with name :- " , file_name)
        else :
            print("Something went wrong")

    def view_file(self) :
        file_name=str(sys.argv[2])
        myfile= open (file_name, "r")
        for line in myfile :
            print(line)

obj=ldif_creation()
obj.input_arguments()
