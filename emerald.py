import os
import sys
from termcolor import colored

def tree(base_path):
    # Displays all files and subdirectories stemming from a given directory

    for dirpath, dirs, files in os.walk(base_path):
        path = dirpath.split('/')
        output = '|' + (len(path)*'---') + '[' + os.path.basename(dirpath) + ']'
        print (colored(output, 'blue'))
        for f in files:
            output = '|' + (len(path)*'---') + f
            print(output)

if(sys.argv[1] == '--help'):
    f = open('help_files/help_tree.txt', 'r')
    print(f.read())
elif(sys.argv[1] == "--version" or sys.argv[1] == "-v"):
    print("tree (shell of qarth) 1.0.0")
elif(sys.argv[1] == "runemap"):
    f = open('man_files/man_tree.txt', 'r')
    print(f.read())
else:
    tree(os.path.abspath(sys.argv[1]))
