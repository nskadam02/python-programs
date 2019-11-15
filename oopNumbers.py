class Numbers:
    def __init__(self,num):
        self.value=num;
    def chkPrime(self):
        if self.value>1:
         for i in range(2,self.value):
            if (self.value%i)==0:
                return False;
         else:
           return True;  
        else:
          return False;
       

    def Factors(self):
        print("Fcators are:",end=" ");
        for i in range(1,int((self.value/2)+1)):
           if self.value%i==0:
             print(i,end=" ,");

    def sumFactors(self):
        no=0;
        for i in range(1,int((self.value/2)+1)):
          if self.value%i==0:
            no=no+i;
        return no;   
    def chkPerfect(self):
        total=self.sumFactors();
        if total==self.value:
            return True;
        else:
            return False;

def main():
    num=int(input("Enter number::"));
    obj1=Numbers(num);
    if (obj1.chkPrime()==False):
        print(num,"It is not prime number");
    else:
        print("Prime numner");

    obj1.Factors();
    print("Sum of its factors is:",obj1.sumFactors());
    if(obj1.chkPerfect()==False):
        print("not perfect number");
    else:
        print("Perfect number");             


if __name__ == "__main__":
    main();    


