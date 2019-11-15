# print n to 1
def Pattern(num): 
   if num>0:
      print(num,end=" ");
      num=num-1;
      Pattern(num);
       

def main():
    num=int(input("Enter number:"));
    Pattern(num);

if __name__ == "__main__":
    main();    
