import sys;
import filecmp;
def CompareFiles(file1,file2):
    #compare two files
    if filecmp.cmp(file1,file2):
        print("Files are same");
    else:
        print("Diffrent files");

def main():
     CompareFiles(sys.argv[1],sys.argv[2]);
if __name__=="__main__":
    main();
