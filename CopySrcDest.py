import os
import shutil
from os import path
import shutil
import os

def main():
    if path.exists("testfile.txt"):
        src = path.realpath("testfile.txt")

    head, tail = path.split(src)
    print("path:" + head)
    print("file:" +tail)
    dst = src + ".bak"
    shutil.copy(src,dst)

    os.rename("testfile.txt","career.testfile.txt")


if __name__ == "__main__":
        main()