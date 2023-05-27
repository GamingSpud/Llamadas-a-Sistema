class SysCall:
    def __init__(self, execTime):
        self.execTime=execTime
    
    def time(self):
        return(f"Execution Time = {self.execTime} units.")

sysCallA = SysCall(3)
sysCallB = SysCall(1)
sysCallC = SysCall(5)
sysCallD = SysCall(2)

callList = []

def callQueue(s):
    callList.append(s)

def callClear():
    callList = []

def FCFS(l):
    lines = []
    for i in range (0,len(l)*2,2):
        lines.append("  |")
        lines.append("---")
        #for j in range (0,l[i].execTime):
            #line1 = line1 + "T" + str(i+j) + "|"
            #if i == 0 and j == 0:
                
            #line1 = line1 + "P" + str(i) + "|"
        print(lines[i])
        print(lines[i+1])
        
callQueue(sysCallA)
callQueue(sysCallB)
callQueue(sysCallC)
callQueue(sysCallD)

FCFS(callList)