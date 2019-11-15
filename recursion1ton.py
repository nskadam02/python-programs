def Pattern(upper,lower):
    if lower>upper:
        return;
    print(lower,end=" ");
    Pattern(upper,lower+1);

        
    

def main():
   upper=int(input("Enter number:"));
   Pattern(upper,1);


if __name__ == "__main__":
     main();
