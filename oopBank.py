class BankAccount:
    ROI=10.5;
    def __init__(self,name,amount):
        self.accountName=name;
        self.accountBalance=amount;
        self.simpleIntrest=0.0;

    def Deposit(self,deposit):
        self.accountBalance=self.accountBalance+deposit;
    def Withdraw(self,withdraw):
        self.accountBalance=self.accountBalance-withdraw;
    def calculatIntrest(self,time):
        self.simpleIntrest= (self.accountBalance)*(float(BankAccount.ROI/100))*time;
        print("Interst for ",time,"years;",self.simpleIntrest);
       
        
    def Display(self):
        print("Account holders name:",self.accountName);
        print("Account balance is:",self.accountBalance);

def main():
    obj1=BankAccount("Neha",1000);
    obj1.Display();
    value=int(input("Enter amount to deposit:"))
    obj1.Deposit(value);
    obj1.Display();
    value1=int(input("Enter amount to withdraw:"));
    obj1.Withdraw(value1);
    obj1.Display();
    time=float(input("enter year to find intrest:"))
    obj1.calculatIntrest(time);

if __name__ == "__main__":
    main();












































