import urllib.request
def main():
    weburl = urllib.request.urlopen("http://www.google.com")
    respcode = str(weburl.getcode())
    print(respcode)
    print(weburl.read())

if __name__ == "__main__":
    main()
