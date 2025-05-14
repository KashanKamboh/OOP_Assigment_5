

print ("    🐍 OOP Assignment    ")
print ("<<<<-----🎇 Welcome in the ATM 🎇----->>>>")
class ATM:
    total_balance = 5000
    def __init__(self,name:str,pin:str):
          self.name = name
          self.pin = pin

    def check_pin(self):
        if self.pin == 1234:
           print("Correct Pin✅")
           return True
        else:
           print("Incorrect Pin❌")  
           return False
    def withdraw_amount(self,amount:int):
        if not self.check_pin():
            print ("Cannot Withdraw, Incorrect Pin❌")
            return
        if amount > ATM.total_balance:
            print ("Insufficient Balance in ATM🙄")
            return
        else:
            ATM.total_balance -= amount 
          
            print(f"{amount}, Withdraw Succesfully🤩")
            print (f"Remaining Balance: {ATM.total_balance}")
    def Deposit_amount(self,amount:int):
        if not self.check_pin():
            print("Cannot Deposite, Incorrect Pin❌")
            return
        else:
            ATM.total_balance += amount
            print(f"{amount}, Deposite Succesfully🤩")
            print (f"Remaining Balance: {ATM.total_balance}")
name = input("Enter your name:")
pin = int(input("Enter your pin:"))
atm_user= ATM(name,pin)

while True:
    print ("\n1. Withdraw \n2. Deposite \n3. Exit")
    choice= int(input("Enter your choice:"))
    if choice == 1:
        amount = int(input("Enter your amount to withdraw:"))
        atm_user.withdraw_amount(amount)
    if choice == 2:
        amount = int(input("Enter your amount to deposite:"))
        atm_user.Deposit_amount(amount)
    if choice == 3:
        print ("Thankyou for using ATM😍")
        break
    else:
        break
        print ("Invalid Choice")





 