def Factorial(num):
    if num==1:
        return 1;
    else:
        return num*Factorial(num-1);    



def main():
    num=int(input("Enter number to find factorial:"));
    print("Factorial is:",Factorial(num));

if __name__ == "__main__":
   main();
