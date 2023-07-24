def main ():
    file_name = "sometext-1.txt"
    d = wordCount (file_name)
    display ( d )

def wordCount ( file_name ):
    d={}
    f = open(fileName, "r")
    lines = f.readlines()
    for line in lines: 
        words = line.split()
        for word in words: 
            if word in d:
                d[word] += 1
            else:
                d[word] = 1
    return d

def display ( d ):
    for key in d:
        print(key, "-",d[key])

main ()