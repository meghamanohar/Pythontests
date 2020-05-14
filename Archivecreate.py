import shutil
from os import path

def main():
    if path.exists("career.testfile.txt"):
        pathlink = path.realpath("career.testfile.txt")
    #spilt path
    root_dir,tail = path.split(pathlink)
    print("Root dir is " + root_dir)
    print("Tail is" + tail)
    shutil.make_archive("meghas_archive","zip",root_dir)

if __name__ == "__main__":
        main()