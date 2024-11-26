def primeCheck(number):
    count =0
    for i in range(2,int((number/2))+1) :
        if number%i==0:
            count +=1 
            
    if count==0:
        print(" Prime")
    else:
        print("Not Prime Number")

primeCheck(22)