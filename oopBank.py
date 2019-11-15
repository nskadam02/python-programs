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
    obj1.Deposit(100);
    obj1.Display();
    obj1.Withdraw(100);
    obj1.Display();
    obj1.calculatIntrest(2);

if __name__ == "__main__":
    main();

