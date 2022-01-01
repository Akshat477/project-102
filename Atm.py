print("WELCOME TO AXIS BANK")
p = int(input("ENTER YOUR PIN :"))
m = 5000
if p == 3131 : 
    print("1 - WITHDRAW ")
    print("2 - BALANCE ENQUERY")
    print("3 - DEPOSITE")
    c = int(input("PLS CHOOSE THE NUMBER FOR TRANSACTION : "))
    if c == 1 : 
        w = int(input("ENTER WITHDRAW AMOUNT : "))
        if w < m and w % 100 == 0 : 
            print("MONEY HAS BEEN  WITHDRAWN") 
        else :
            print("INVALID CASH")
    elif c == 2 : 
        print("YOUR AVAILABLE AMOUNT IS :",m)
    elif c == 3 :
        a = int(input("ENTER THE AMOUNT THAT YOU WANT TO DEPOSIT : "))   
        a = a+m 
        print("THE NEW BALANCE IN YOUR ACCOUNT IS : ",a)
else : 
    print("WRONG PIN NUMBER")         