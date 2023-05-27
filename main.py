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
    totalTime = 1
    horLine = "---"
    verLine = "|"
    for n in l:
        totalTime += n.execTime    
    for i in range (0,(len(l)+1)*2,2):
        if i == 0:
            lines.append("  " + verLine)
            lines.append(horLine)
            for j in range (0,totalTime):
                lines[i] = lines[i] + "T" + str(i+j) + verLine
                lines[i+1] = lines[i+1] + horLine
                if len(str(j)) < len(str(j+1)):
                    horLine = horLine + "-"
        else:
            lines.append("P" + str(int((i/2)-1)) + verLine)
            lines.append(horLine)
            for j in range (0,totalTime):
                lines[i] = lines[i] + "P" + str(int((i/2)-1)) + verLine
                lines[i+1] = lines[i+1] + horLine
                if len(str(j)) < len(str(j+1)):
                    horLine = horLine + "-"
                    if j%2 == 0:
                        verLine = verLine + " "
                    else:
                        verLine = " " + verLine
        horLine = "---"
        verLine = "|"
        print(lines[i])
        print(lines[i+1])
        
callQueue(sysCallA)
callQueue(sysCallB)
callQueue(sysCallC)
callQueue(sysCallD)

FCFS(callList)