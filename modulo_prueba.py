import numpy as np
from modulo_coeficiente import*
from modulo_tabla import*

def probarEdadxPeso(estudiantes):
    print("\n==========================================================================\n")
    filasEdad=7
    columnasPeso=6
    matrizEdadPeso=np.zeros([filasEdad,columnasPeso])
    matrizEdadPesoDeseada=np.zeros([filasEdad,columnasPeso])

    pesoXedad(estudiantes,matrizEdadPeso,filasEdad-1,columnasPeso-1)
    print("\n Tabla de frecuencias absolutas ni para Edad x Peso\n")
    imprimirPesoxEdad(matrizEdadPeso,filasEdad,columnasPeso)
    pesoXedadDeseado(matrizEdadPeso,matrizEdadPesoDeseada,filasEdad-1,columnasPeso-1)
    print("\n Tabla de frecuencias absolutas deseadas ni* para Edad x Peso\n")
    imprimirPesoxEdadDeseada(matrizEdadPesoDeseada,filasEdad,columnasPeso)

    print("==========================================================")
    print("\t       Resultados - edad(X) vs peso(Y)")
    print("==========================================================")
    mEdad=filasEdad-1
    sPeso=columnasPeso-1
    print("Agrupando por variables 'edad del estudiante'\n y 'peso del estudiante', el indice H^2 da:")
    x_2 = cuadradoContingencia(matrizEdadPeso,matrizEdadPesoDeseada,mEdad,sPeso)
    print("\nx^2 es: ",x_2)
    h_2 = cramer(x_2,28,mEdad,sPeso)
    print("H^2 es: ", h_2, "\n")

def probarMiembrosxHermanos(estudiantes):
    print("\n==========================================================================\n")
    filasMiembros = 7
    columnasHermanos = 5
    matrizMiembrosHermanos=np.zeros([filasMiembros,columnasHermanos])
    matrizMiembrosHermanosDeseada=np.zeros([filasMiembros,columnasHermanos])

    miembrosfamiliaxhermanos(estudiantes,matrizMiembrosHermanos,filasMiembros-1,columnasHermanos-1)
    print("\n Tabla de frecuencias absolutas ni para #Miembros Familia x #Hermanos\n")
    imprimirMiembrosxHermanos(matrizMiembrosHermanos,filasMiembros,columnasHermanos)
    miembrosfamiliaxhermanosDeseado(matrizMiembrosHermanos,matrizMiembrosHermanosDeseada,filasMiembros-1,columnasHermanos-1)
    print("\n Tabla de frecuencias absolutas deseadas ni* para #Miembros Familia x #Hermanos\n")
    imprimirMiembrosxHermanosDeseada(matrizMiembrosHermanosDeseada,filasMiembros,columnasHermanos)

    print("==========================================================")
    print("\t    Resultados - #Miembros(X) vs #Hermanos(Y)")
    print("==========================================================")
    mMiembros=filasMiembros-1
    sHermanos=columnasHermanos-1
    print("Agrupando por variables '#miembros familia'\n y '#hermanos', el indice H^2 da:")
    x_2_2 = cuadradoContingencia(matrizMiembrosHermanos,matrizMiembrosHermanosDeseada,mMiembros,sHermanos)
    print("\nx^2 es: ",x_2_2)
    h_2_2 = cramer(x_2_2,28,mMiembros,sHermanos)
    print("H^2 es: ", h_2_2, "\n")