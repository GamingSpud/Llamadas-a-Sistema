#Video Entrega: https://youtu.be/pGF8RlnMoio

#Constructor para clase SysCall que tiene como parametros nombre y tiempo de ejecución.
#El tiempo se mide en una unidad de tiempo arbitraria e indivisible.
#Para esta implementación se utiliza ua unidad de tiempo que también será el quantum
#    para Round Robin.

class SysCall:
    def __init__(self, name, execTime):
        self.name = name
        self.execTime = execTime
    
    def __str__(self):
        p = "P" + self.name
        return (p)
    
    #Método para imprimir el objeto dentro de una lista
    __repr__ = __str__

    #Métodos para comparar objetos SysCall entre sí
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

#Recibe una lista 'l' y devuelve una lista 'lr' con un elemento por cada vez
# que se debe ejecutar un proceso de acuerdo al algoritmo FCFS
def FCFS(l):
    lr = []
    for i in range(0,len(l)):
        for j in range (0,l[i].execTime):
            lr.append(l[i].name)
    return lr

#Recibe una lista 'l', la copia a 'l2' y la organiza como si los procesos hubieran
# llegado de menor tiempo de ejecución a mayor, luego aplica 'FCFS()' sobre 'l2'
def SJF(l):
    l2 = []
    lr = []
    for i in range (0, len(l)):
        l2.append(l[i])
    l2.sort()
    lr = FCFS(l2)
    return lr

#Crea una lista con el tiempo de ejecución de cada proceso 'l2', y el total de todos
# los tiempos de ejecucion, luego va por cada tiempo de ejecución y proceso en la lista,
# si el proceso tiene tiempo de ejecución mayor que 0 en 'l2' añade una vez el proceso
# a la lista final, resta 1 al tiempo de ese proceso en 'l2' y suma 1 a 'i' que está
# contando los tiempos de ejecución.
#Esta función tiene incluido el manejo de un quantum 'n' mayor a 1, lamentablemente
# hacer eso rompe la función para imprimir las tablas de ejecución.
def roundRobin(l,n=1):
    l2 = []
    lr = []
    totalTime = 0
    for i in range(0,len(l)):
        totalTime += l[i].execTime
        l2.append(l[i].execTime)
    for i in range(0,totalTime):
        for j in range(0, len(l)):
            if l2[j] > 0:
                lr.append(l[j].name)
                l2[j] = l2[j] - n
                i += 1
    return lr

#Aquí es donde ocurre la magia de consola, con strings como 'horLine' y 'verLine'
# modificables podemos imprimir separadores en la tabla que se adaptan a la longitud
# del interior de cada 'celda'.
def printSchedule(l,l2):
    lines = []
    totalTime = 0
    horLine = "---"
    verLine = "|"
    order = []
#Primero iteramos sobre la lista de procesos y obtenemos el total del tiempo de
# ejecución y el orden de llegada de los procesos(!).
    for n in l:
        totalTime += n.execTime
        order.append(str(n)[1])
#Luego usamos un ciclo 'for i...' donde 'i' es cada fila de la tabla (incluidas las
# filas que son sólo guiones que actuan como separador horizontal. Esta 'i' depende del
# tamaño de la lista de procesos con un factor '(n+1)*2'. El '+1' es para la línea
# superior que indica los tiempos, y el '*2' es porque cada linea de datos debe ser
# acompañada con una linea de guiones.        
    for i in range (0,(len(l)+1)*2,2):
        n = int((i/2)-1)
#Si es la primera fila (i==0), entonces lo que hacemos es usar un ciclo 'for j...' para
#  imprimir celdas que digan "T" y el tiempo de ejecución 'j'.
        if i == 0:
            lines.append("     " + verLine)
            lines.append(horLine + horLine)
            for j in range (0,totalTime):
                lines[i] = lines[i] + "T" + str(j) + verLine
                lines[i+1] = lines[i+1] + horLine
#Si la longitud de 'j' incrementa, entonces incrementamos los guiones en la variable
# 'horLine'.                
                if len(str(j)) < len(str(j+1)):
                    horLine = horLine + "-"
        else:
#Con esto imprimimos la cabecera de cada fila, con 'n' siendo la posición de llegada
# de cada proceso, y 'l[n].name' es el nombre de cada proceso.            
            lines.append("P" + str(n) + "(" + l[n].name + ")" + verLine)
            lines.append(horLine + horLine)
#Usamos otra ves 'for j...' para el contenido de cada celda, pero esta vez usamos la
# variable 'cell' para el contenido de cada una.
            for j in range (0,totalTime):
                cell = "  "
#Aquí comparamos si el proceso en la fila que estamos imprimiendo 'order[n]' 
# corresponde al tiempo de ejecución que estamos considerando 'l2[j]', y si es correcto
# cambiamos la variable 'cell' de "  " a " E" de Ejecución.
                if order[n] == l2[j]:
                    cell = " E"
                lines[i] = lines[i] + cell + verLine
                lines[i+1] = lines[i+1] + horLine
#Tambien incrementamos 'horLine' si el tamaño de 'j' crece. Además, ponemos espacios
# vaciós a cada lado de la variable 'verLine="|"', dependiendo de si el caracter en la
# mitad de 'verLine' es o no es "|"
                if len(str(j)) < len(str(j+1)):
                    horLine = horLine + "-"
                    if verLine[int(len(verLine)/2)] == "|":
                        verLine = " " + verLine
                    else:
                        verLine = verLine + " "
#Aquí reseteamos 'horLine' y 'verLine' para la siguiente fila. Luego imprimimos las
# filas 'i' e 'i+1' y un enter al final.
        horLine = "---"
        verLine = "|"
        print(lines[i])
        print(lines[i+1])
    print()

#Nos permite crear una lista que corresponda a los tiempos de ejecución de la lista
# original de procesos.
def organizeTimes(l):
    lr = []
    for i in l:
        lr.append(i.execTime)
    return lr

#Procesos de ejemplo, es importante que no se creen 2 procesos con el mismo nombre.
#Durante la creación de procesos real cada proceso debería tener como referencia una
# dirección de memoria única, así se refieran al mismo set de instrucciones, por
# lo que dos procesos con la misma referencia no se daría en la vida real.
processA = SysCall("A", 3)
processB = SysCall("B", 1)
processC = SysCall("C", 5)
processD = SysCall("D", 2)
#processE = SysCall("E", 4)

#Lista con los procesos de ejemplo
processList = []
processList.append(processA)
processList.append(processB)
processList.append(processC)
processList.append(processD)
#processList.append(processE)

#Una segunda lista con los tiempos de cada proceso de la lista original.
#Es más como referencia.
timesList = organizeTimes(processList)

#Son listas con las referencias de cada proceso en el orden en que deben ser
# ejecutados.
FCFSSchedule = FCFS(processList)
RRSchedule = roundRobin(processList)
SJFSchedule = SJF(processList)

def run():
#Imprimimos la lista de procesos, la lista de tiempos y las listas de ejecución de
# cada algoritmo como referencia.
    print("\n" + str(processList))
    print(timesList)
    print(str(FCFSSchedule) + " <= FCFS")
    print(str(SJFSchedule) + " <= SJF")
    print(str(RRSchedule) + " <= RR")
    print()

#Aquí tenemos el resultado de todo el programa.
    print("Algoritmo \"First Come First Served\":")
    printSchedule(processList,FCFS(processList))
    print("Algoritmo \"Shortest Job First\":")
    printSchedule(processList,SJF(processList))
    print("Algoritmo \"Round Robin\":")
    printSchedule(processList,roundRobin(processList))

if __name__ == '__main__':
    run()

#Video Entrega: https://youtu.be/pGF8RlnMoio