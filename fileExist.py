import os;
def CheckFile():
    name=input("Enter file name to display content:");
    if os.path.exists(name):
        print("File existe")
    else:
        print("file doesnt exist")
def main():
    CheckFile();

if __name__=="__main__":
    main();
