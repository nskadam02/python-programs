import sys;
def copyFile(filename):
    fd=open(filename,'r');
    fd1=open("hello.txt",'w');
    for line in fd.read():
        fd1.write(line);
    fd.close();
    fd1.close();
def OtherMethod(filename):
    # other method for copying fie
    with open(filename) as f1:
        with open("fun.txt",'w') as f2:
            for line in f1.read():
                    f2.write(line);
    f1.close()
    f2.close()                
def main():
  copyFile(sys.argv[1]);
  OtherMethod(sys.argv[1]);

if __name__=="__main__":
    main();
