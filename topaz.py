import os
import sys

def remdir(dirName):
    # Takes a parent directory, directory name as parameters and remove a directory at the specified parent directory.
    
    path = os.path.join(".",dirName)
    os.rmdir(path)
    print("Directory removed successfully!\n")

if(sys.argv[1] == '--help'):
    f = open('help_files/help_rmdir.txt', 'r')        
    print(f.read())
elif(sys.argv[1] == "--version" or sys.argv[1] == "-v"):
    print("rmdir (shell of qarth) 1.0.0")
elif(sys.argv[1] == "runemap"):
    f = open('man_files/man_rmdir.txt', 'r')        
    print(f.read())
else:
    remdir(sys.argv[1])