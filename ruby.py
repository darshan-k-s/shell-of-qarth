import psutil, sys

def kill(pid):
    # Kills the process by a given process ID
    
    for proc in psutil.process_iter():
        procsInfo = proc.as_dict(attrs = ['pid','name','cpu_percent', 'cmdline'])
        try:
            if(procsInfo['pid'] == int(pid)):
                p = psutil.Process(int(pid))
                p.kill()
        except:
            pass
    print("Process killed: (%s)"%(pid))

if(len(sys.argv)==2):
    if(sys.argv[1] == '--help'):
        f = open('help_files/help_kill.txt', 'r')
        print(f.read())
    elif(sys.argv[1] == "--version" or sys.argv[1] == "-v"):
        print("kill (shell of qarth) 1.0.0")
    elif(sys.argv[1] == "runemap"):
        f = open('man_files/man_kill.txt', 'r')
        print(f.read())
    else:
        kill(sys.argv[1])
