import sys
import os

def if_not_exists(fileName):
    # Check if the file with a given file name exists or not
    
    file_path = os.getcwd() + '/' + fileName
    if(os.path.exists(file_path) == False):
        print(fileName + ': Cannot open \'' + fileName + '\' (No such file or directory)')
        sys.exit()

def cat(fName):    
    # Takes a file name and prints out the contents of the file
    
    if fName.startswith('>'):
        fileName = fName[1:]
        if_not_exists(fileName)
        f = open(fileName, 'a')
        i = input()
        f.write(i)
    elif ">>" in fName:
        fileName = fName.split('>>')
        if_not_exists(fileName[1])
        f1 = open(fileName[0], 'r')
        f2 = open(fileName[1], 'a')
        i = f1.read()
        f2.write(i)
    else:
        fileName = fName
        if_not_exists(fileName)
        f = open(fileName)
        i = f.read()
        print(i)

if(sys.argv[1] == '--help'):
    f = open('help_files/help_cat.txt', 'r')
    print(f.read())
elif(sys.argv[1] == "--version" or sys.argv[1] == "-v"):
    print("cat (shell of qarth) 1.0.0")
elif(sys.argv[1] == "runemap"):
    f = open('man_files/man_cat.txt', 'r')
    print(f.read())
else:
    cat(sys.argv[1])


    