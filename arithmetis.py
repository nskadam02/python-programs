import Arithmetic

no1=int(input("Enter number first:"));
no2=int(input("Enetr second number:"));
choice=int(input("1.sum 2.Substraction 3.multiplication 4.division:"));
if choice==1:
    print("Sum is:",Arithmetic.Sum(no1,no2));
elif choice==2:
    print("Substraction is:",Arithmetic.Sub(no1,no2));
elif choice==3:
    print("Multiplication is:",Arithmetic.Mult(no1,no2));
elif choice==4:
    print("Division is:",Arithmetic.Div(no1,no2));    
