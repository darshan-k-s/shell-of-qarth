from os import system

# For autocomplete and suggestions
from fuzzywuzzy import fuzz

# shell command names
shellCommands = [
    "astapor", 
    "runemap", 
    "aquamarine", 
    "amethyst", 
    "turquoise", 
    "garnet", 
    "topaz", 
    "pearl", 
    "opal", 
    "diamond",    
    "emerald", 
    "sapphire", 
    "quartz", 
    "peridot", 
    "ruby", 
    "lykiri", 
    "daor" 
]

def closestCommandFinder(command):
    # Takes a command string, finds the closest matching command and return a possible match from the existing set of shell commands.

    closestCommand = command
    sysCommand = shellCommands[0]
    fuzzratio = fuzz.ratio(command, sysCommand)
    for sysCommand in shellCommands:
        if fuzz.ratio(command, sysCommand) > fuzzratio and fuzz.ratio(command, sysCommand)!=0:
            fuzzratio = fuzz.ratio(command, sysCommand)
            closestCommand = sysCommand

    return closestCommand

def shellHelp():
    # Display the help text for the shell.

    f = open('startupFiles/startup.txt', 'r')        
    print(f.read())
    print('\n')

def shell():
    # Function that runs the shell.

    startup = 1
    cmdError = 0

    while 1:
        if startup == 1:
            startup = startup + 1
            _ = system('clear')
            shellHelp()        
        
        if (cmdError == 0):
            userinput = input("\033[1mshell-of-qarth@\033[94muser\033[0m$ ")
            pass
        else:
            userinput = closestCommand + " " + userinput
            cmdError = 0
        
        inputArr = userinput.split()

        if(inputArr[0] == shellCommands[0]): # shell help
            shellHelp()
        elif(len(inputArr) == 1 and (inputArr[0] in shellCommands) and inputArr[0] != 'daor' and inputArr[0] != 'lykiri' and inputArr[0] != 'opal' and inputArr[0] != 'diamond' and inputArr[0] != 'quartz' and inputArr[0] != 'peridot'):
            system('python3 ' + inputArr[0] + '.py --help')
        elif(inputArr[0] == shellCommands[1]):
            system('python ' + shellCommands[1] + '.py ' + inputArr[0]) # man page for every command
        elif(inputArr[0] == shellCommands[2]):  # file searcher command
            system('python3 aquamarine.py ' + inputArr[1])
        elif(inputArr[0] == shellCommands[3]):  # file command
            system('python3 amethyst.py ' + inputArr[1])
        elif(inputArr[0] == shellCommands[4]):  # spell checker command
            system('python3 turquoise.py ' + inputArr[1])
        elif(inputArr[0] == shellCommands[5]):  # make directory command
            if len(inputArr) == 3:
                system('python3 garnet.py ' + inputArr[1] + ' ' + inputArr[2])
            elif len(inputArr) == 2:
                system('python3 garnet.py ' + inputArr[1])
        elif(inputArr[0] == shellCommands[6]):  # remove directory command
            if len(inputArr) == 3:
                system('python3 topaz.py ' + inputArr[1] + ' ' + inputArr[2])
            elif len(inputArr) == 2:
                system('python3 topaz.py ' + inputArr[1])
        elif(inputArr[0] == shellCommands[7]):  # pearl command
            if len(inputArr) == 3:
                system('python3 pearl.py ' + inputArr[1] + inputArr[2])
            elif len(inputArr) == 2:
                system('python3 pearl.py ' + inputArr[1])
        elif(inputArr[0] == shellCommands[8]):  # free command
            if len(inputArr) == 3:
                system('python3 opal.py ' + inputArr[1] + inputArr[2])
            elif len(inputArr) == 2:
                system('python3 opal.py ' + inputArr[1])
            elif len(inputArr) == 1:
                system('python3 opal.py')
        elif(inputArr[0] == shellCommands[9]):  # ps command
            if len(inputArr) == 2:
                system('python3 diamond.py ' + inputArr[1])
            else: 
                system('python3 diamond.py')
        elif(inputArr[0] == shellCommands[10]):  # tree command
            if len(inputArr) == 2:
                system('python3 emerald.py ' + inputArr[1])
        elif(inputArr[0] == shellCommands[11]):  # cat command
            if len(inputArr) == 2:
                system('python3 sapphire.py ' + inputArr[1])
        elif(inputArr[0] == shellCommands[12]):  # ps command
            if len(inputArr) == 2:
                system('python3 quartz.py ' + inputArr[1])
            else: 
                system('python3 quartz.py')
        elif(inputArr[0] == shellCommands[13]):  # lsof command
            if len(inputArr) == 2:
                system('python3 peridot.py ' + inputArr[1])
            else: 
                system('python3 peridot.py')
        elif(inputArr[0] == shellCommands[14]):  # ruby command
            if len(inputArr) == 2:
                system('python3 ruby.py ' + inputArr[1])
        elif(inputArr[0] == shellCommands[15]):  # clear command
            _ = system('clear')
        elif(inputArr[0] == shellCommands[16]):  # exit command
            exit(0)
        else:
            closestCommand = closestCommandFinder(inputArr[0])
            userinput = input(inputArr[0] + ": command not found. Did you mean " + closestCommand + "? (y/n): ")
            if userinput == 'y' or userinput == 'Y':
                userinput = input("\033[1mshell-of-qarth@\033[94muser\033[0m$ " + closestCommand)
                cmdError = 1
            else:
                continue

shell()