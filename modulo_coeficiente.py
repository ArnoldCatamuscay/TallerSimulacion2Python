def cuadradoContingencia(disA, disAdeseada,m,s):
    x2=0
    for i in range(m):
        for j in range(s):
            #print("\n(",disA[i][j], "-", disAdeseada[i][j],")^2 / ", disAdeseada[i][j], " = ", pow(disA[i][j] - disAdeseada[i][j],2) / disAdeseada[i][j])
            x2 += pow(disA[i][j] - disAdeseada[i][j],2) / disAdeseada[i][j]
            #print("\nIteracion [",j,"]: x^2 = ", x2)
    return x2

def cramer(x2, n, m, s):
    h2=0
    f2 = x2/n
    if (m-1) < (s-1):#El min es m
        #print("\nEl min es: ", m-1)
        h2 = f2 / (m-1)
    elif (m-1) > (s-1):#El min es s
        #print("\nEl min es: ", s-1)
        h2 = f2 / (s-1)
    print("f^2: ", f2)
    return h2