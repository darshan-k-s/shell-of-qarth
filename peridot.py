import psutil
import os
import sys

def if_not_exists(dirPath):
    # Check if the given directory path exists

    if(os.path.exists(dirPath) == False):
        print('Cannot open \'' + dirPath + '\' (No such file or directory)')
        sys.exit()

def is_open_file(fpath):
    # Check if a file is open or not

    for proc in psutil.process_iter():
        try:
            for item in proc.open_files():
                procsInfo = proc.as_dict(attrs = ['pid','name','cpu_percent', 'cmdline'])
                if fpath == item.path:
                    if psutil.Process()==proc: print("yes")
                    return proc
                elif fpath in procsInfo['cmdline']:
                    return proc
        except Exception:
            pass
    return False

def lsof(dirPath):
    # List all the open processes in the directory

    if_not_exists(dirPath)
    entries = os.listdir(dirPath+'/')
    for entry in entries:
        p = is_open_file(dirPath+'/'+entry)
        if not p == False:
            print(entry+' \n--Opened by process = '+p.name()+'\n--PID = '+str(p.pid)+'\n')

def lsof_cur():
    # Check for open processes or applications in the current directory

    dirPath = os.getcwd()
    entries = os.listdir(dirPath + '/')
    for entry in entries:
        p = is_open_file(dirPath + '/' + entry)
        if not p == False:
            print(entry + ' \n--Opened by process = ' + p.name() + '\n--PID = ' + str(p.pid) + '\n')

if(len(sys.argv) == 1): 
    lsof_cur()
elif(len(sys.argv) == 2):
    if(sys.argv[1] == '--help'):
        f = open('help_files/help_lsof.txt', 'r')
        print(f.read())
    elif(sys.argv[1] == "--version" or sys.argv[1] == "-v"):
        print("lsof (shell of qarth) 1.0.0")
    elif(sys.argv[1] == "runemap"):
        f = open('man_files/man_lsof.txt', 'r')
        print(f.read())
    else:
        lsof(sys.argv[1])