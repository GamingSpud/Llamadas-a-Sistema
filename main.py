def toNumber(a):
    for i in a:
        i = int(i,36) - 10 # Assume letter is a number in base 36, convert to base 10 and substract 10.
        #if (i<10):
            #i = "".join(['0',str(i)])
        #print (str(i))
    return i

class SysCall:
    def __init__(self, name, execTime):
        self.name = name
        self.execTime = execTime
    
    def __str__(self):
        p = "P" + self.name
        return (p)
    
    __repr__ = __str__

    def time(self):
        return (f"Execution Time = {self.execTime} units.")
    
    def __eq__(self, other):
        return self.execTime == other.execTime
    
    def __lt__(self, other):
        return self.execTime < other.execTime
    
    def __le__(self, other):
        return self.execTime <= other.execTime
    
    def __gt__(self, other):
        return self.execTime > other.execTime
    
    def __ge__(self, other):
        return self.execTime >= other.execTime
    
    def __ne__(self, other):
        return self.execTime != other.execTime


processA = SysCall("A", 3)
processB = SysCall("B", 1)
processC = SysCall("C", 5)
processD = SysCall("D", 2)

processList = []

def processQueue(s):
    processList.append(s)

def callClear():
    callList = []

processQueue(processA)
processQueue(processB)
processQueue(processC)
processQueue(processD)

def FCFS(l):
    lr = []
    for i in range(0,len(l)):
        for j in range (0,l[i].execTime):
            lr.append(l[i].name)
    return lr

FCFSSchedule = FCFS(processList)

def roundRobin(l,n=1):
    l2 = []
    lr = []
    totalTime = 1
    for i in range(0,len(l)):
        totalTime += l[i].execTime
        l2.append(l[i].execTime)
    for i in range(0,totalTime):
        for j in range(0, len(l)):
            if l2[j] > 0:
                lr.append(l[j].name)
                l2[j] = l2[j] - n
    return lr

RRSchedule = roundRobin(processList,1)

def SJF(l):
    l2 = []
    lr = []
    maxTime = 0
    totalTime = 1
    for i in range (0, len(l)):
        l2.append(l[i])
    l2.sort()
    lr = FCFS(l2)
    return lr

SJFSchedule = SJF(processList)

print(processList)
print(str(FCFSSchedule) + " <= FCFS")
print(str(RRSchedule) + " <= RR")
print(str(SJFSchedule) + " <= SJF")

def printSchedule(l,l2):
    lines = []
    totalTime = 0
    horLine = "---"
    verLine = "|"
    print()
    for n in l:
        totalTime += n.execTime
    for i in range (0,(len(l)+1)*2,2):
        n = int((i/2)-1)
        if i == 0:
            lines.append("     " + verLine)
            lines.append("---" + horLine)
            for j in range (0,totalTime):
                lines[i] = lines[i] + "T" + str(j) + verLine
                lines[i+1] = lines[i+1] + horLine
                if len(str(j)) < len(str(j+1)):
                    horLine = horLine + "-"
        else:
            lines.append("P" + str(n) + "(" + l[n].name + ")" + verLine)
            lines.append(horLine + horLine)
            for j in range (0,totalTime):
                cell = "  "
                if n == toNumber(l2[j]):
                    cell = " E"
                lines[i] = lines[i] + cell + verLine
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
        
printSchedule(processList,roundRobin(processList))