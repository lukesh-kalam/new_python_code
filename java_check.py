import os
import sys

class java_check:
    def __init__(self) :
        pass
    def input_arguments(self) :
        server=str(sys.argv[1])
        platform=str(sys.argv[2])
        if(platform=="windows") :
            obj.windows(server)
        elif(platform=="linux") :
            obj.linux(server)
        else  :
            obj.aix(server)
    def windows (self,server) :
        if (server=="mailwin1.prod.hclpnp.com" or "mailwin2.prod.hclpnp.com" or "samailserver1.svt.cwp.pnp-hcl.com" or "samailserver2.svt.cwp.pnp-hcl.com") :
            print(server)
            print("------------------------------------------------------------------------------------")
            os.system('java -version')
    def linux (self,server)  :
        if (server=="mailsles1.prod.hclpnp.com" or "mailsles2.prod.hclpnp.com" or "samailserver5.svt.cwp.pnp-hcl.com" or "samailserver6.svt.cwp.pnp-hcl.com") :
            print(server)
            os.chdir('/local/notesdata')
            print("---------------------------------------------------------------------------------")
            print("java version ")
            os.system('/opt/hcl/domino/notes/latest/linux/java -version')
    def aix(self,server) :
        if (server=="mailaix2.prod.hclpnp.com" or "mailaix1.prod.hclpnp.com") :
            print(server)
            os.chdir('/local/notesdata')
            print("---------------------------------------------------------------------------------")
            print("java version ")
            os.system('/opt/hcl/domino/notes/latest/ibmpow/java -version')

obj=java_check()
obj.input_arguments()