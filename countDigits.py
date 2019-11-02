def Sumation():
    num=int(input("Enter number:"));
    sumation=0;
    temp=num;
    while num>0:
        num=int(num/10);
        sumation=sumation+1;
    print("count of digits in",temp,"is:",sumation);

Sumation();
