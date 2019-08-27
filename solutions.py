from math import sqrt, floor

# Problema 1
def prob_1(val1):
    if val1 % 2 == 0:
        return True
    else:
        return False

"""
-----------------------------------------------------
"""
# Problema 2
def prob_2(val1):
    return ((val1 - 32) * 5/9)

"""
----------------------------------------------------
"""
# Problema 3
def prob_3(base, potencia):
    return base**potencia

"""
----------------------------------------------------
"""
# Problema 4
def prob_4(dato, simbolo, cantidad):
    return dato.center(cantidad, simbolo)


"""
----------------------------------------------------
"""

# Problema 5
def prob_5(N1, M1, L1, N2, M2, L2):

    vectorN1 = ((M1 * L2) - (M2 * L1))
    vectorM1 = -((N1 * L2)-(N2 * L1))
    vectorL1 = ((N1 * M2) - (N2 * M1))
    vectorR = vectorN1, vectorM1, vectorL1

    return vectorR

"""
----------------------------------------------------
"""

# Problema 6
def prob_6(a):
    n = len(a)
    for i in range(n):
        for j in range(n-1):
            if a[j] < a [j+1]:
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
    return (a)
"""
----------------------------------------------------
"""
# Problema 7
def prob_7(n, m):
    i = 0
    multiplos = []
    while i <= n:
        if i % m == 0:
            multiplos.append(i)
            i = i +1
        else:
            i = i+1
    return multiplos

"""
----------------------------------------------------
"""

# Problema 8
def prob_8(lineas):

    triangulo =""

    

    for numero_linea in range(lineas): 

        espacios = lineas - numero_linea - 1 

        asteriscos = 1 + numero_linea * 2

        triangulo += "  " * espacios + "* " * asteriscos + "\n"

        

    return triangulo

# print (prob_8(5))

"""
----------------------------------------------------
"""

# Problema 9
def prob_9(val1, val2, val3):
    if val1 > val2 > val3:
        p1 = val2**2 + val3**2
        p2 = val1**2
        pr = p1 == p2
        return True
    elif val2 > val1 > val3:
        p1 = val1**2 - val3**2
        p2 = val2**2
        pr = p1 == p2
        return True
    elif val3 > val2 > val1:
        p1 = val1**2 - val2**2
        p2 = val3**2
        pr = p1 == p2
        return True
    elif val2 > val3 > val1:
        p1 = val3**2 - val1**2
        p2 = val2**2
        pr = p1 == p2
        return True
    elif val3 > val1 < val2:
        p1 = val2**2 - val1**2
        p2 = val3**2
        pr = p1 == p2
        return True
    elif val1 > val2 == val3:
        p1 = (val2 + val3)**2
        p2 = val1**2
        pr = p1 == p2
        return False
    else:
        return False
"""
----------------------------------------------------
"""

# Problema 10

def prob_10(p1, p2, p3):
    r1 = sqrt((p1[0] - p2[0])**2 + (p1[1]-p2[1])**2)
    r2 = sqrt((p2[0] - p3[0])**2 + (p2[1]-p3[1])**2)
    r3 = sqrt((p3[0] - p1[0])**2 + (p3[1]-p1[1])**2)
    val = [r1, r2, r3]
    
    if val[0] + val[1] <= val[2]:
        return ("No es un triangulo")
    
    if val[0] == val[1] and val[1] == val[2]:
        return ("Es un triangulo equilatero")
    
    elif val[0] == val[1] or val[1] == val[2]:
        return ("Es un triangulo isoceles")
    
    else:
        return ("Es un triangulo escaleno")

"""
----------------------------------------------------
"""

# Problema 11

def prob_11(j):
    palabra = j[::-1]
    if j == palabra:
        return True
    else:
        return False

"""
----------------------------------------------------
"""

# Problema 12
def unidades(x):
    if x == 0:
        unidad = "cero"
    if x == 1:
        unidad = "un"
    if x == 2:
        unidad = "dos"
    if x == 3:
        unidad = "tres"
    if x == 4:
        unidad = "cuatro"
    if x == 5:
        unidad = "cinco"
    if x == 6:
        unidad = "seis"
    if x == 7:
        unidad = "siete"
    if x == 8:
        unidad = "ocho"
    if x == 9:
        unidad = "nueve"
    return unidad

def especiales(x):
    if x == 0:
        especiales = "diez"
    if x == 1:
        especiales = "once"
    if x == 2:
        especiales = "doce"
    if x == 3:
        especiales = "trece"
    if x == 4:
        especiales = "catorce"
    if x == 5:
        especiales = "quince"
    return especiales


def diez(x):
    if x == 1:
        diez = "diez"
    if x == 2:
        diez = "veinte"
    if x == 3:
        diez = "treinta"
    if x == 4:
        diez = "cuarenta"
    if x == 5:
        diez = "cincuenta"
    if x == 6:
        diez = "sesenta"
    if x == 7:
        diez = "setenta"
    if x == 8:
        diez = "ochenta"
    if x == 9:
        diez = "noventa"
    return diez

def tercia(num):
    numero=str(num)
    if len(numero) == 1:
        numero='00'+numero
    if len(numero) == 2:
        numero='0'+numero
    a=int(numero[0])
    b=int(numero[1])
    c=int(numero[2])
#       print a, b, c
    if a == 0:
        if b == 0:
            resultado=unidades(c)
            return resultado
        elif b == 1:
            if c >= 0 and c <= 5:
                resultado = especiales(c)
                return resultado
            elif c >= 6 and c <= 9:
                resultado = diez(b)+' y '+unidades(c)
                return resultado
        elif b == 2:
            if c == 0:
                resultado = 'veinte'
                return resultado
            elif c > 0 and c <= 9:
                resultado ='veinti '+unidades(c)
                return resultado
        elif b >=3 and b <= 9:
            if c == 0:
                resultado = diez(b)
                return resultado
            if c >= 1 and c <= 9:
                resultado = diez(b)+' y '+unidades(c)
                return resultado
    if a == 1:
        if b == 0:
            if c == 0:
                resultado = 'cien'
                return resultado
            elif c > 0 and c <= 9:
                resultado ='ciento '+unidades(c)
                return resultado
        elif  b == 1:
            if c >= 0 and c <= 5:
                resultado = 'ciento '+especiales(c)
                return resultado
            elif c >= 6 and c <= 9:
                resultado = 'ciento '+diez(b)+' y '+unidades(c)
                return resultado
        elif b == 2:
            if c == 0:
                resultado = 'ciento veinte'
                return resultado
            elif c > 0 and c <= 9:
                resultado ='ciento veinti '+unidades(c)
                return resultado
        elif b >= 3 and b <= 9:
            if c == 0:
                resultado = 'ciento '+diez(b)
                return resultado
            elif c > 0 and c <= 9:
                resultado = 'ciento '+diez(b)+ ' y '+unidades(c)
                return resultado

    elif a >= 2 and a <= 9:
        if a == 5:
            uni='quinientos '
        elif a == 7:
            uni='setecientos '
        elif a == 9:
            uni='novecientos '
        else:
            uni=unidades(a)+' cientos '
        if b == 0:
            if c == 0:
                resultado = uni
                return resultado
            elif c > 0 and c <= 9:
                resultado = uni+unidades(c)
                return resultado
        elif b == 1:
            if c >= 0 and c <= 5:
                resultado = uni+especiales(c)
                return resultado
            elif c >= 6 and c <= 9:
                resultado = uni+diez(b)+' y '+unidades(c)
                return resultado
        elif b == 2:
            if c == 0:
                resultado = uni+' veinte'
                return resultado
            elif c > 0 and c <= 9:
                resultado = uni+' veinti '+unidades(c)
                return resultado
        elif b >= 3 and b <= 9:
            if c == 0:
                resultado = uni+diez(b)
                return resultado
            elif c > 0 and c <= 9:
                resultado = uni+diez(b)+' y '+unidades(c)
                return resultado
def prob_12(num):
    if num>1000:
        return ("el numero debe de ser menor a 1000")
    result=''
    numero=str(num)
    if len(numero) == 1:
        numero='0'+numero
    if len(numero) == 2:
        numero='00'+numero
    if len(numero) == 3:
        numero='000'+numero
    if len(numero) == 4:
        numero='0000'+numero
    if len(numero) == 5:
        numero='0000'+numero
    if len(numero) == 6:
        numero='000'+numero
    if len(numero) == 7:
        numero='00'+numero
    if len(numero) == 8:
        numero='0'+numero
    posicion=1
    for i in [0,3,6]:
        var=numero[i]+numero[i+1]+numero[i+2]
        if int(var) != 0:
            res=tercia(var)
            if i == 0:
                result=res+" millones "
            elif i == 3:
                result=result+res+" mil "
            elif i == 6:
                result=result+res
    return result
"""
----------------------------------------------------
"""
# Problema 13
def prob_13(numero):
    
    resultado = 0
    
    for i in [1,2,3,4,5,6,7,8,9]:
        if numero % i == 0:
            resultado += i

 
    return resultado
        

"""
----------------------------------------------------
"""

# Problema 14
def prob_14(numero):

    if numero <= 1:
        return("ingrese un numero mayor a 1")
    else:
        contador = 0
        for i in range(1, numero +1):
            if numero % i == 0:
                contador = contador + 1
        if contador == 2:
            return True
        else:
            return False

"""
----------------------------------------------------
"""

# Problema 15
def prob_15(numero):
    suma = 0
    for i in range(1, numero):
        if (numero % (i) == 0):
            suma += (i)
    if numero == suma:
        return True
    else:
        return False

"""
----------------------------------------------------
"""

# Problema 16
def prob_16(n1, n2):
    tX = 0
    tR = 0
    for i in range(1, n1):
        if n1%i == 0:
            tX += i
        if n2%i == 0:
            tR += i

    return tX == n2 and tR == n1


"""
----------------------------------------------------
"""
#Problema 17
def prob_17(n1, n2):
    ar = []
    for i in range(2, n1):
        if n1%i == 0:
            ar.append(i)

    for i in range(2, n2):
        if n2%i == 0 and i in ar:
            return False

    return True

"""
----------------------------------------------------
"""

# Problema 18
def prob_18(n):
    a, b = 0, 1
    while a < n:
        print(a, end = ' ')
        a,b = b, a+b
    return n

"""
----------------------------------------------------
"""

# Problema 19
def prob_19(n):
    x,y = 0,1
    while True:
        if len(str(x)) == n:
            return x
        x, y = y, x+y
"""
----------------------------------------------------
"""

# Problema 20
def prob_20():
    valor = []
    for i in range(1, 1000):
        for j in range(i+1, 1000):
            a = j**2 - i**2
            b = 2*i*j
            c = i**2 + j**2
            if((a**2 + b**2) == c**2) and (a + b + c) == 1000:
                valor.append([a, b, c])
        return ("Los valores son: " + valor)

"""
----------------------------------------------------
"""

# Problema 21
def prob_21(n):
    valor = []
    for i in range(2, n+1):
        if prob_14(i):
            valor.append(i)
    return valor

"""
----------------------------------------------------
"""

# Problema 22

def prob_22(p1, p2, p3, p4):
    if p1 == p2 and p2 == p3 and p3 == p4:
        return False
    else:
        d1 = math.sqrt(p1[0]-p2[0])**2 + (p1[1] - p2[1]**2)
        d2 = math.sqrt(p1[0]-p3[0])**2 + (p1[1] - p3[1]**2)
        d3 = math.sqrt(p1[0]-p4[0])**2 + (p1[1] - p4[1]**2)
        d4 = math.sqrt(p4[0] - p1[0])**2 + (p4[1] - p1[1]**2)
        d5 = math.sqrt(p4[0] - p2[0])**2 + (p4[1] - p2[1]**2)
        d6 = math-sqrt(p4[0] - p3[0])**2 + (p4[1] - p3[1]**2)
        valor1 = [d1, d2, d3]
        valor2 = [d4, d5, d6]
        return valor1 == valor2
    
"""
----------------------------------------------------
"""
# Problema 23
#def prob_23():
    

"""
----------------------------------------------------
"""
# Problema 24

def prob_24(numeros):
    orden = numeros
    numerosOrdenados = [orden.copy()]
    ref = []
    n = len(orden)

    for i in range(n):
        ref.append(0)

    i = 0

    while i < n:
        if ref[i] < i:
            if prob_1(i):
                orden[0], orden[i]= orden[i], orden[0]
            else:
                orden[ref[i]], orden[i] = orden[i], orden[ref[i]]
            numerosOrdenados.append(orden.copy())
            ref[i] += 1

            i = 0
        else:
            ref[i] = 0
            i += 1

    return numerosOrdenados

