import os

os.chdir('C:\\Users\\kalam.kumar\\Desktop\\verse_saml_svt3ids')


for i in range (1,125) :
    a='3VOP'+str(i)+'.id'
    b='T3VOP'+str(i)+'.id'
    os.rename(a,b)