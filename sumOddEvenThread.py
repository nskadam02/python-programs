from threading import *;
from os import *;
def addEvenFactors(no):
    total=0
    if no%2!=0:
      return;
    if no%2==0:
        total=total+no; 
    for i in range(2,int((no/2)+1)):
        if (no%i==0):
            if (i%2==0):
              total=total+i;        
    print("Sum of even factors is:",total);
    
def addOddFactors(num):
    no=0;
    for i in range(1,int((num/2)+1)):
        if (num%i==0) :
            if (i%2!=0):
              no=no+i;
    print("Sum of odd factors is:",no);        
def main():
    num=int(input("Enter number to get its odd and even factors sum:"));
    odd=Thread(target=addOddFactors,args=(num,));
    even=Thread(target=addEvenFactors,args=(num,));
    odd.start();
    even.start();
    print("Exit from main");


if __name__=="__main__":
    main();
