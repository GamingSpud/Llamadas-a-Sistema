class SysCall:
    def __init__(self, execTime):
        self.execTime=execTime
    
    def time(self):
        return(f"Execution Time = {self.execTime} units.")

sysCallA = SysCall(3)
sysCallB = SysCall(1)
sysCallC = SysCall(5)
sysCallD = SysCall(2)

def FCFS(l):
    for i in l:
        for j in i.execTime:
            print
        
    