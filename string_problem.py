str = input("enter your sentence :")

no_of_chr = int(input("enter number of charecters : "))

if no_of_chr > len(str):
     print("you entered invalid sentence, please enter no of char's less than", len(str))
elif no_of_chr == len(str):
     print(str[0:no_of_chr]) 
elif str[0:no_of_chr+1] == " ":
     print(str[0:no_of_chr])        
else:    
    for i in range(no_of_chr,0,-1):
     if str[i] == " ":
        print(str[0:i])
        break  