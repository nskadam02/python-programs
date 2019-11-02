def addFact():
    num=int(input("Please Enter number:"));
    no=0;
    for i in range(1,int((num/2)+1)):
        if num%i==0:
            no=no+i;
    print("Sum of factors of ",num,"is:",no);

addFact();            
