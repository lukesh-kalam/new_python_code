## Author :- K.Lukesh Kumar
## Perpose : - To merge secrets.txt file with the ldif file
import os
os.chdir('C://Users//kalam.kumar//OneDrive - HCL Technologies Ltd//Desktop//python1//merge')

f=open('mailsles2vop_secrets.txt','r')   # secrets.txt file 
b=1  # user starting number
l=[]
for line in f :
    prefix="msl2vop"               # Starting user pefix
    c=","
    d=prefix+str(b)+c
   # mw2nrpc2
    newString=line.replace(d,'')
    print("secret: ",newString)
    l.append(str(newString))
    b +=1
print(l[0])

f=open('mailsles2vop.ldif','r')    # current ldif file
w=open('456759.ldif','w')             # new ldif file name
i=0 
for line in f :
    print(line)
    w.write(line)
    if ".nsf" in line :
        print("secret: "+l[i])
        x="secret: "+l[i]
        w.write(x)
        i +=1
        