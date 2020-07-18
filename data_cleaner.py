import re


def main():
    filename = "2010"
    file = open(filename+".txt","r")
    text = file.read()
    file.close()
    #text = re.sub(" {2,}\d\d\n", "\n", text)
    #text = re.sub("\d{1,4}\.(.*)\n", "\n", text)
    #text = text.replace(".", "")
    #text = text.replace("*", "")
    #text = text.replace(", ", "$")
    #text = text.replace(",", "")
    #text = text.replace("$", ", ")
    #text = re.sub(" {2,}", ";", text)
    #text = re.sub(" [a-z]{1,}", "", text)
    #text = text.replace("\t", "")
    text = text.replace("\n\n", "\n")
    text = text.replace(";;", ";")
    #print(text)
    file = open(filename+".txt", "w")
    file.write(text)
    file.close()


if __name__ == "__main__":
    main()
