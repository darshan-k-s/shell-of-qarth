import sys
import os
import magic

def fileCommand(fileName):
    # Find out information about the file using its name

    file_path = os.getcwd() + '/' + fileName
    if(os.path.exists(file_path) == False):
        print(fileName + ': Cannot open \'' + fileName + '\' (No such file or directory)')
    else:
        print(fileName + ': ' + magic.from_file(fileName))

if(sys.argv[1] == '--help'):
    f = open('help_files/help_file.txt', 'r')
    print(f.read())
elif(sys.argv[1] == "--version" or sys.argv[1] == "-v"):
    print("file (shell of qarth) 1.0.0")
elif(sys.argv[1] == "runemap"):
    f = open('man_files/man_file.txt', 'r')
    print(f.read())
else:
    fileCommand(sys.argv[1])