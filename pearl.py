import os
import sys

def rnm(oldName, newName):    
    # Renames an existing file or directory
    
    os.rename(oldName,newName);
    print("Rename successful!\n")

if(sys.argv[1] == '--help'):
    f = open('help_files/help_rename.txt', 'r')        
    print(f.read())
elif(sys.argv[1] == "--version" or sys.argv[1] == "-v"):
    print("rename (shell of qarth) 1.0.0")
elif(sys.argv[1] == "runemap"):
    f = open('man_files/man_rename.txt', 'r')        
    print(f.read())
else:
    rnm(sys.argv[1], sys.argv[2])