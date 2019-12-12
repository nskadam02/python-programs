import sys;
def countString(filename):
    fd=open(filename,'r');
    fd1=fd.read();
    strCompare=input("Enter string to count:");
    num=fd1.count(strCompare);
    print(num);
    fd.close();   
def main():
  countString(sys.argv[1]);
  

if __name__=="__main__":
    main();
