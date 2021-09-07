string=input("Enter string:")
count1=0
count2=0
for i in string:
      if(i.islower()):
            count1=count1+1
      elif(i.isupper()):
            count2=count2+1
print("The number of lowercase characters is:")
print(count1)
print("The number of uppercase characters is:")
print(count2)
word_list = string.split()
number_of_words = len(word_list)
print("No of words :- ",number_of_words)
contains_digit = False
digits =0
for character in string:
    if character.isdigit():
        contains_digit = True
        if contains_digit == True :
            digits =digits+1
print("No of digits : -" ,digits)