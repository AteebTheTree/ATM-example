class ATM:
    def __init__(self, cardNo, pinNo, bal):
        self.cardNo = cardNo
        self.pinNo = pinNo
        self.bal = bal

    def balanceInquiry(self):
        print(self.bal)

    def cashWithdrawl(self):
        money = float(input("How much money would you like to withdraw? "))
        self.bal -= money;
        print("balance is now", self.bal)

cardInput = int(input("Enter your card number: "))
pinInput = int(input("Enter your pin number: "))
balInput = float(input("Enter your current balance: "))

person = ATM(cardInput, pinInput, balInput)

inquiry = input("What would you like to do? Enter balance for balance and withdraw to withdraw ")
if(inquiry == "balance"):
    person.balanceInquiry()
elif(inquiry == "withdraw"):
    person.cashWithdrawl()
else:
    print("Invalid input! Launch again")


