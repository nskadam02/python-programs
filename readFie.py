def displayFile():
    dot=40*"-";
    name=input("Enter file name to display content:");
    fd=open(name,'r');
    print("file content");
    print(dot);
    print(fd.read());
    fd.close()

def main():
  displayFile();

if __name__=="__main__":
    main();
