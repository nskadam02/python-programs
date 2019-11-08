from checkModule import *;
def ListPrime():
    no=int(input("Enter the no of element in list:"));
    arr=list();
    sumation=0;
    for i in range(no):
        no1=int(input("Enter number to add in list:"));
        arr.append(no1);

    for i in range(no):
        if(ChkPrime(arr[i])):
            print("helo",arr[i]);
            sumation=sumation+arr[i];
    print("Sum of prime numbers is:",sumation);

ListPrime();
