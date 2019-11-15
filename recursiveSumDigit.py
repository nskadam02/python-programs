def SumDigit(num):
    if num==0:
        return 0;
    else:
        return num%10+SumDigit(num//10);    
  
def main():
    num=int(input("Enter number to find sum of digits:"));
    print("total sum is:",SumDigit(num));

if __name__ == "__main__":
    main();    
