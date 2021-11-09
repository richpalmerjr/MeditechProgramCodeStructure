
########################################################################################################################

def readProgram(directory,program):
    if ".focus" in program:
        programToRead = open((directory+program), "r")
    else:
        programToRead = open((directory+program+".focus"), "r")
        
    print("\n"+program)
    
    for line in programToRead:
        if "//" not in line:
            if "#Include" in line:
                print("\n\t"+line.strip())
            elif re.search("File",line) and "I.focus" in line:
                include = line.split()
                includedPgms.append(include[1])
                print("\t"+line.strip())
            elif "#Magic" in line:
                print("\n\t"+line.strip())            
            elif ":Code" in line:
                print("\t"+line.strip())
                callsubs.append(line.strip())
            elif "@CallSub" in line:
                for x in line.split("@CallSub"):
                    name = getCallSubName(x)
                    if name is not None:
                        # "is not none" is checking if the variable is non-nil
                        print("\t\t",name)
            elif "@CallExternalSub" in line:
                for x in line.split("@CallExternalSub"):
                    name = getCallSubName(x)
                    if name is not None:
                        # "is not none" is checking if the variable is non-nil
                        print("\t\t",name)
                        
    programToRead.close()

########################################################################################################################

def getCallSubName(line):
    if "(" in line and line[0] is "(":
        callSubPos=line.strip().find("(")
        callSub = line.strip()[line.strip().find("("):]
        callSubName = callSub[callSub.strip().find(")")]
        callSubNamePos = callSub.find(")")
        return callSub[callSub.find("(")+1:callSubNamePos]
    
########################################################################################################################    

import os

#this allows the use of re.search, which looks for a whole word instead of just a part of it
import re

callsubs = []
includedPgms = []

program = input('Which program? ')
directory = ('C:\ProgramData\MEDITECH\MTX.Universe\DEV.Ring\!AllUsers\Sys\PgmCache\Ring\PgmSource\Bar\\')

#hardcoding MTX.Universe for now, keeping this line for the future
#programDirectory = ('C:\ProgramData\MEDITECH\\'+ringToSearch+'\!AllUsers\Sys\PgmCache\Ring\PgmSource\\'+appToSearch+'\\')

readProgram(directory,program)

print("\n\n\nIncluded Programs")
for pgm in includedPgms:
    readProgram(directory,pgm)
