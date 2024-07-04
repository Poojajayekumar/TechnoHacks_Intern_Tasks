pin=1234
amount=5000
X=True
Y= True
while X:
    user_pin=int(input("Enter the Pin Number: "))
    while Y:
        if user_pin==pin:
            print("1.Deposite\n2.Withdraw\n3.BalanceEnquiry")
            ch=int(input("Enter your Choice: "))
            if ch==1:
                damount=int(input("Enter the deposite amount: "))
                amount=amount+damount
                print("Your available balance",amount)
                a=input("Do you want to continue(y/n): ")
                if a=="n":
                    X=False
                    break
            elif ch==2:
                wamount=int(input("Enter the withdraw amount:"))
                amount=amount-wamount
                print("Your available balance ",amount)
                a=input("Do you want to continue(y/n): ")
                if a=="n":
                    X=False
                    break
                
            elif ch==3:
                print("Your available balance ",amount)
                a=input("Do you want to continue(y/n): ")
                if a=="n":
                    X=False
                    break

            else:
                print("_______Wrong input Try again_______")
        else:
            user_pin=int(input("Invalide Pin Number Try again: "))
