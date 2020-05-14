from zipfile import ZipFile
def main():
    with ZipFile("megstest.zip","w") as newzip:
        newzip.write("career.testfile.txt")
        newzip.write("testfile.txt.bak")

if __name__ == "__main__":
    main()


