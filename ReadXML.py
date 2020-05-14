import xml.dom.minidom
def main():
    doc = xml.dom.minidom.parse("MyXML.xml")

    nexp = doc.createElement("expertise")
    nexp.setAttribute("name","BigData")
    doc.firstChild.appendChild(nexp)

    exp = doc.getElementsByTagName("expertise")
    for skill in exp:
        print(skill.getAttribute("name"))


if __name__ == "__main__":
    main()