from operator import is_

from pila import Stack
import constantes

def main():
    print("Primer Ejercicio: ")
    primerEjercicio("hola+mundo$")
    print("Segundo Ejercicio: ")
    segundoEjercicio("a+b+c+d+e+f$")

def primerEjercicio(texto):
    print(texto)
    pila = Stack()

    estado = constantes.INICIAL #Identifica el estado actual del analizador
    d = 2
    lexema = ""

    #Inicia el automata del analizador
    i = 0
    while(i<len(texto)):
        c = texto[i]

        if(estado == constantes.INICIAL):
            if (es_Letra(c) or c == '_'): #Verifica si es letra o empieza con un "_"
                estado = constantes.IDENTIFICADOR
                lexema += c
            elif (c == '+'):
                pila.push(constantes.SIMBOLO)
                pila.push(d)
                d+=1
                estado = constantes.INICIAL
                lexema = ""
                pila.mostrarPila()
            elif (c == '$'):
                pila.clear()
                nuevaPila = Stack()
                nuevaPila.push(constantes.E)
                nuevaPila.push(1)
                nuevaPila.mostrarPila()
            else:
                print("ERROR")

        elif(estado == constantes.IDENTIFICADOR):
            if(es_Letra(c) or isReal(c) or c == '_'):
                estado = constantes.IDENTIFICADOR
                lexema += c
            else:
                pila.push(constantes.IDENTIFICADOR)
                pila.push(d)
                d += 1
                estado = constantes.INICIAL
                lexema = ""
                i -= 1
                pila.mostrarPila()
        i += 1
        #termina el automata

def segundoEjercicio(texto):
    print(texto)

    pila = Stack()

    estado = constantes.INICIAL #Identifica el estado actual del analizador
    d2 = 2
    d3 = 3
    lexema = ""

    #Inicia el automata del analizador
    i = 0
    while(i<len(texto)):
        c = texto[i]

        if(estado == constantes.INICIAL):
            if (es_Letra(c) or c == '_'): #Verifica si es letra o empieza con un "_"
                estado = constantes.IDENTIFICADOR
                lexema += c
            elif (c == '+'):
                pila.push(constantes.SIMBOLO)
                pila.push(d3)
                estado = constantes.INICIAL
                lexema = ""
                pila.mostrarPila()
            elif (c == '$'):
                pila.clear()
                nuevaPila = Stack()
                nuevaPila.push(constantes.E)
                nuevaPila.push(1)
                nuevaPila.mostrarPila()
            else:
                print("ERROR")

        elif(estado == constantes.IDENTIFICADOR):
            if(es_Letra(c) or isReal(c) or c == '_'):
                estado = constantes.IDENTIFICADOR
                lexema += c
            else:
                pila.push(constantes.IDENTIFICADOR)
                pila.push(d2)
                estado = constantes.INICIAL
                lexema = ""
                i -= 1
                pila.mostrarPila()
        i += 1
        #termina el automata

def isReal(c):
    if (ord(c) >= 48 and ord(c) <= 57):
        return True
    else:
        return False

def es_Letra(c):
    if (((ord(c) >= 65 and ord(c) <= 90) or ord(c) == 95) or ((ord(c)>=97 and ord(c)<=122) or ord(c) == 95)):
        return True
    else:
        return False



main()
