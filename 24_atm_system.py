name = input("enter your name : ")
phone = input("enrte your number : ")
if(len(phone) == 10):
    pin1 = phone[0:2]
    pin2 = phone[-2:]
    pin = pin1 + pin2
    balance = int(phone[2:7])
    print("Dear", name, ", Your ATM Accepted")
    usr_pin = input("Please Enter Your PIN : ")
    if(pin == usr_pin):
        print("------------------------------------------------")
        print("Welcome, ", name)
        wd = int(input("Please enter amoount : "))
        if(balance >= wd):
            if(wd % 100 == 0):
                print("------------------------------------------------")
                print("Success!")
                print("Your account is debitaed : ", wd)

                balance = balance - wd
                print("Your account balance is : ", balance)
            else:
                print("Please enter amount in multiple 100")
        else:
            print("Insufficiant balance")
    else:
        print("Incorrect PIN")
else:
    print("Please enter valid mobile number")

