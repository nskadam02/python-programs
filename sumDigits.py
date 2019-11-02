def Sumation():
    num=int(input("Enter number:"));
    sumation=0;
    temp=num;
    while num>0:
        rem=int(num%10);
        sumation=sumation+rem;
        num=int(num/10);
    print("sum of digits of",temp,"is:",sumation);

Sumation();
