def main():
    f = open("testfile.txt","w+")

    for i in range(10):
        f.write("This is line %d\r\n" %(i + 1))
    f.close()

    f2 = open("testfile.txt","r")
    contents = f2.read()
    print(contents)


if __name__ == "__main__":
    main()
