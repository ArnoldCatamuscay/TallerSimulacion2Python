from modulo_estudiante import*

def leerMuestraEstudiantes():
    estudiantes = []
    with open("Datos.txt",'r') as data_file:
        for line in data_file:
            data = line.split('\t')
            id = data[0]
            edad = data[1]
            peso = data[2]
            genero = data[3]
            numHermanos = data[4]
            numMiembros = (data[5].split('\n'))[0]
            estudiante = Estudiante(id, edad, peso, genero, numHermanos, numMiembros)
            estudiantes.append(estudiante)
    return estudiantes

def pesoXedad(estudiantes,A,m,s):
    for estudiante in estudiantes:
        #print(type(estudiante.edad), "\n")
        if estudiante.edad==str(19):
            if estudiante.peso>=str(45) and estudiante.peso<=str(55):
                A[0][0]+=1
            elif estudiante.peso>=str(55) and estudiante.peso<=str(65):
                A[0][1]+=1
            elif estudiante.peso>=str(65) and estudiante.peso<=str(75):
                A[0][2]+=1
            elif estudiante.peso>=str(75) and estudiante.peso<=str(85):
                A[0][3]+=1
            elif estudiante.peso>=str(85) and estudiante.peso<=str(95):
                A[0][4]+=1
        elif estudiante.edad==str(20):
            if estudiante.peso>=str(45) and estudiante.peso<=str(55):
                A[1][0]+=1
            elif estudiante.peso>=str(55) and estudiante.peso<=str(65):
                A[1][1]+=1
            elif estudiante.peso>=str(65) and estudiante.peso<=str(75):
                A[1][2]+=1
            elif estudiante.peso>=str(75) and estudiante.peso<=str(85):
                A[1][3]+=1
            elif estudiante.peso>=str(85) and estudiante.peso<=str(95):
                A[1][4]+=1
        elif estudiante.edad==str(21):
            if estudiante.peso>=str(45) and estudiante.peso<=str(55):
                A[2][0]+=1
            elif estudiante.peso>=str(55) and estudiante.peso<=str(65):
                A[2][1]+=1
            elif estudiante.peso>=str(65) and estudiante.peso<=str(75):
                A[2][2]+=1
            elif estudiante.peso>=str(75) and estudiante.peso<=str(85):
                A[2][3]+=1
            elif estudiante.peso>=str(85) and estudiante.peso<=str(95):
                A[2][4]+=1
        elif estudiante.edad==str(22):
            if estudiante.peso>=str(45) and estudiante.peso<=str(55):
                A[3][0]+=1
            elif estudiante.peso>=str(55) and estudiante.peso<=str(65):
                A[3][1]+=1
            elif estudiante.peso>=str(65) and estudiante.peso<=str(75):
                A[3][2]+=1
            elif estudiante.peso>=str(75) and estudiante.peso<=str(85):
                A[3][3]+=1
            elif estudiante.peso>=str(85) and estudiante.peso<=str(95):
                A[3][4]+=1
        elif estudiante.edad==str(23):
            if estudiante.peso>=str(45) and estudiante.peso<=str(55):
                A[4][0]+=1
            elif estudiante.peso>=str(55) and estudiante.peso<=str(65):
                A[4][1]+=1
            elif estudiante.peso>=str(65) and estudiante.peso<=str(75):
                A[4][2]+=1
            elif estudiante.peso>=str(75) and estudiante.peso<=str(85):
                A[4][3]+=1
            elif estudiante.peso>=str(85) and estudiante.peso<=str(95):
                A[4][4]+=1
        elif estudiante.edad>str(23):
            if estudiante.peso>=str(45) and estudiante.peso<=str(55):
                A[5][0]+=1
            elif estudiante.peso>=str(55) and estudiante.peso<=str(65):
                A[5][1]+=1
            elif estudiante.peso>=str(65) and estudiante.peso<=str(75):
                A[5][2]+=1
            elif estudiante.peso>=str(75) and estudiante.peso<=str(85):
                A[5][3]+=1
            elif estudiante.peso>=str(85) and estudiante.peso<=str(95):
                A[5][4]+=1

    #Calcular ni.
    niP=0
    for i in range(m+1):
        niP=0
        for j in range(s+1):
            niP+=A[i][j]
            if j==5:
                A[i][j] = niP

    #calcular n.j
    A[6][0]=A[1][0]+A[2][0]+A[3][0]+A[4][0]+A[5][0]+A[0][0]
    A[6][1]=A[1][1]+A[2][1]+A[3][1]+A[4][1]+A[5][1]+A[0][1]
    A[6][2]=A[1][2]+A[2][2]+A[3][2]+A[4][2]+A[5][2]+A[0][2]
    A[6][3]=A[1][3]+A[2][3]+A[3][3]+A[4][3]+A[5][3]+A[0][3]
    A[6][4]=A[1][4]+A[2][4]+A[3][4]+A[4][4]+A[5][4]+A[0][4]

    #calcular n..
    n=0
    for i in range(m):
        for j in range(s):
            n+=A[i][j]

    A[6][5]=n

def pesoXedadDeseado(A,Adeseada,m,s):
    for i in range(m):
        for j in range(s):
            Adeseada[i][j] = (A[i][5]*A[6][j]) / A[6][5]

    #Calcular ni.
    niP2=0
    for i in range(m+1):
        niP2=0
        for j in range(s+1):
            niP2+=Adeseada[i][j]
            if j==5:
                Adeseada[i][j] = niP2

    #calcular n.j
    Adeseada[6][0]=Adeseada[1][0]+Adeseada[2][0]+Adeseada[3][0]+Adeseada[4][0]+Adeseada[5][0]+Adeseada[0][0]
    Adeseada[6][1]=Adeseada[1][1]+Adeseada[2][1]+Adeseada[3][1]+Adeseada[4][1]+Adeseada[5][1]+Adeseada[0][1]
    Adeseada[6][2]=Adeseada[1][2]+Adeseada[2][2]+Adeseada[3][2]+Adeseada[4][2]+Adeseada[5][2]+Adeseada[0][2]
    Adeseada[6][3]=Adeseada[1][3]+Adeseada[2][3]+Adeseada[3][3]+Adeseada[4][3]+Adeseada[5][3]+Adeseada[0][3]
    Adeseada[6][4]=Adeseada[1][4]+Adeseada[2][4]+Adeseada[3][4]+Adeseada[4][4]+Adeseada[5][4]+Adeseada[0][4]

    #calcular n..
    n2=0
    for i in range(m):
        for j in range(s):
            n2+=Adeseada[i][j]

    Adeseada[6][5]=n2

def imprimirPesoxEdad(matriz,filas,columnas):
    edad=19
    for i in range(filas):
        if(i==0):
            print("\t45-55\t55-65\t65-75\t75-85\t85-95\tni.")
            print("       -----------------------------------------------")
        for j in range(columnas):
            if j == 0:
                if edad <= 23:
                    print(edad, end=" ")
                elif edad>23 and i==5:    
                    print("Mas", end=" ")
                else:
                    print("n.j", end=" ")
            if j!=columnas:
                print("\t", end=" ")
            print("{:.0f}".format(matriz[i][j]), end=" ")
        edad += 1
        print("\n       -----------------------------------------------")

def imprimirPesoxEdadDeseada(matriz,filas,columnas):
    edad2=19
    for i in range(filas):
        if(i==0):
            print("\t45-55\t55-65\t65-75\t75-85\t85-95\tni.")
            print("       -----------------------------------------------")
        for j in range(columnas):
            if j == 0:
                if edad2 <= 23:
                    print(edad2, end=" ")
                elif edad2>23 and i==5:    
                    print("Mas", end=" ")
                else:
                    print("n.j", end=" ")
            if j!=columnas:
                print("\t", end=" ")
            print("{:.2f}".format(matriz[i][j]),"", end=" ")
        edad2 += 1
        print("\n       -----------------------------------------------")

def miembrosfamiliaxhermanos(estudiantes,A,m,s):
    for estudiante in estudiantes:
        if estudiante.numMiembros==str(2):
            if estudiante.numHermanos==str(0):
                A[0][0]+=1
            elif estudiante.numHermanos==str(1):
                A[0][1]+=1
            elif estudiante.numHermanos==str(2):
                A[0][2]+=1
            elif estudiante.numHermanos==str(3):
                A[0][3]+=1
        elif estudiante.numMiembros==str(3):
            if estudiante.numHermanos==str(0):
                A[1][0]+=1
            elif estudiante.numHermanos==str(1):
                A[1][1]+=1
            elif estudiante.numHermanos==str(2):
                A[1][2]+=1
            elif estudiante.numHermanos==str(3):
                A[1][3]+=1
        elif estudiante.numMiembros==str(4):
            if estudiante.numHermanos==str(0):
                A[2][0]+=1
            elif estudiante.numHermanos==str(1):
                A[2][1]+=1
            elif estudiante.numHermanos==str(2):
                A[2][2]+=1
            elif estudiante.numHermanos==str(3):
                A[2][3]+=1
        elif estudiante.numMiembros==str(5):
            if estudiante.numHermanos==str(0):
                A[3][0]+=1
            elif estudiante.numHermanos==str(1):
                A[3][1]+=1
            elif estudiante.numHermanos==str(2):
                A[3][2]+=1
            elif estudiante.numHermanos==str(3):
                A[3][3]+=1
        elif estudiante.numMiembros==str(6):
            if estudiante.numHermanos==str(0):
                A[4][0]+=1
            elif estudiante.numHermanos==str(1):
                A[4][1]+=1
            elif estudiante.numHermanos==str(2):
                A[4][2]+=1
            elif estudiante.numHermanos==str(3):
                A[4][3]+=1
        elif estudiante.numMiembros==str(7):
            if estudiante.numHermanos==str(0):
                A[5][0]+=1
            elif estudiante.numHermanos==str(1):
                A[5][1]+=1
            elif estudiante.numHermanos==str(2):
                A[5][2]+=1
            elif estudiante.numHermanos==str(3):
                A[5][3]+=1

    #Calcular ni.
    niP=0
    for i in range(m+1):
        niP=0
        for j in range(s+1):
            niP+=A[i][j]
            if j==4:
                A[i][j] = niP

    #calcular n.j
    A[6][0] = A[0][0]+A[1][0]+A[2][0]+A[3][0]+A[4][0]+A[5][0]
    A[6][1] = A[0][1]+A[1][1]+A[2][1]+A[3][1]+A[4][1]+A[5][1]
    A[6][2] = A[0][2]+A[1][2]+A[2][2]+A[3][2]+A[4][2]+A[5][2]
    A[6][3] = A[0][3]+A[1][3]+A[2][3]+A[3][3]+A[4][3]+A[5][3]

    #calcular n..
    n=0
    for i in range(m):
        for j in range(s):
            n+=A[i][j]

    A[6][4]=n

def imprimirMiembrosxHermanos(matriz,filas,columnas):
    miembros=2
    for i in range(filas):
        if(i==0):
            print("\t 0\t 1\t 2\t 3\tni.")
            print("       --------------------------------------")
        for j in range(columnas):
            if j == 0:
                if miembros <= 7:
                    print(miembros, end=" ")
                elif i==6:    
                    print("n.j", end=" ")
            if j!=columnas:
                print("\t", end=" ")
            print("{:.0f}".format(matriz[i][j]), end=" ")
        miembros += 1
        print("\n       --------------------------------------")

def miembrosfamiliaxhermanosDeseado(A,Adeseada,m,s):
    for i in range(m):
        for j in range(s):
            Adeseada[i][j] = (A[i][4]*A[6][j]) / A[6][4]

    #Calcular ni.
    niP2=0
    for i in range(m+1):
        niP2=0
        for j in range(s+1):
            niP2+=Adeseada[i][j]
            if j==4:
                Adeseada[i][j] = niP2

    #calcular n.j
    Adeseada[6][0]= Adeseada[0][0]+Adeseada[1][0]+Adeseada[2][0]+Adeseada[3][0]+Adeseada[4][0]+Adeseada[5][0]
    Adeseada[6][1]= Adeseada[0][1]+Adeseada[1][1]+Adeseada[2][1]+Adeseada[3][1]+Adeseada[4][1]+Adeseada[5][1]
    Adeseada[6][2]= Adeseada[0][2]+Adeseada[1][2]+Adeseada[2][2]+Adeseada[3][2]+Adeseada[4][2]+Adeseada[5][2]
    Adeseada[6][3]= Adeseada[0][3]+Adeseada[1][3]+Adeseada[2][3]+Adeseada[3][3]+Adeseada[4][3]+Adeseada[5][3]

    #calcular n..
    n2=0
    for i in range(m):
        for j in range(s):
            n2+=Adeseada[i][j]

    Adeseada[6][4]=n2

def imprimirMiembrosxHermanosDeseada(matriz,filas,columnas):
    miembros=2
    for i in range(filas):
        if(i==0):
            print("\t 0\t 1\t 2\t 3\tni.")
            print("       --------------------------------------")
        for j in range(columnas):
            if j == 0:
                if miembros <= 7:
                    print(miembros, end=" ")
                elif i==6:    
                    print("n.j", end=" ")
            if j!=columnas:
                print("\t", end=" ")
            print("{:.2f}".format(matriz[i][j]), end=" ")
        miembros += 1
        print("\n       --------------------------------------")