"""
Autor: Andrea Bravo A01028579 y Valeria Ibarra A01023936
Fecha: 27 de abril, 2020
Descripción: Proyecto Integrador, crear un juego de memoria en un tablero de 6x6 que contenga numeros del 1 al 18 dos veces
"""
import random

#variables
jugadorUno='0'
jugadorDos='0'
fila=['0','1','2','3','4','5']
columna=['0','1','2','3','4','5']
tableroVacio=[['-','-','-','-','-','-'],
             ['-','-','-','-','-','-'],
             ['-','-','-','-','-','-'],
             ['-','-','-','-','-','-'],
             ['-','-','-','-','-','-'],
             ['-','-','-','-','-','-']]

tableroDatos=[[1,2,3,4,5,6],
              [7,8,9,10,11,12],
              [13,14,15,16,17,18],
              [1,2,3,4,5,6],
              [7,8,9,10,11,12],
              [13,14,15,16,17,18]]
lista=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,
       1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
cont=0
contDos=0
contTres=0
jugadorUnoPuntos=0
jugadorDosPuntos=0
res=0

jugadorUno=input('Nombre del Jugador 1: ')
jugadorDos=input('Nombre del Jugador 2: ')

def main():
    #variables
    puntosUno=0
    puntosDos=0
    #código
    mezclar() #mezcla el tablero
    impTablero() #muestra el tablero
    puntosUno+=turnoUno()#empieza el juego
    res=input('¿Quieres seguir jugando? s/n ')
    while res!='s' and res!='n':
        print('No entendí tu respuesta')
        res=input('¿Quieres seguir jugando? s/n ')
    while res=='s':
        puntosDos+=turnoDos()
        if tableroVacio==tableroDatos: #Por si ya acabó el juego
            print('Ha terminado la partida')
            if puntosUno>puntosDos:
                print('El ganador es ',jugadorUno, 'con un total de: ',puntosUno, 'pares!')
            elif puntosDos>puntosUno:
                print('El ganador es ',jugadorDos, 'con un total de: ',puntosDos, 'pares!')
            elif puntosUno==puntosDos:
                print('Es un empate, ambos tienen', puntosUno,'pares')
            break
        res=input('¿Quieres seguir jugando? s/n ')
        while res!='s' and res!='n':
            print('No entendí tu respuesta')
            res=input('¿Quieres seguir jugando? s/n ')
        if res=='n':
            break
        puntosUno+=turnoUno()
        if tableroVacio==tableroDatos:
            print('Ha terminado la partida')
            if puntosUno>puntosDos:
                print('El ganador es ',jugadorUno, 'con un total de: ',puntosUno, 'pares!')
            elif puntosDos>puntosUno:
                print('El ganador es ',jugadorDos, 'con un total de: ',puntosDos, 'pares!')
            elif puntosUno==puntosDos:
                print('Es un empate, ambos tienen', puntosUno,'pares')
            break
        res=input('¿Quieres seguir jugando? s/n ')
        while res!='s' and res!='n':
            print('No entendí tu respuesta')
            res=input('¿Quieres seguir jugando? s/n ')
    if res=='n':
        print(jugadorUno,'hiciste', puntosUno,'pares')
        print(jugadorDos,'hiciste',puntosDos,'pares')

def mezclar():
    #variables
    contTres=0
    random.shuffle(lista)
    for cont in range (0,len(tableroDatos),1):
        for contDos in range (0,len(tableroDatos[cont]),1):
            tableroDatos[cont][contDos]=lista[contTres]
            contTres+=1
    
def impTablero():
    print(end="\t")
    for cont in range(0,len(fila),1):
        print(fila[cont], end="\t ")
    print()
    for contDos in range (0, len(tableroVacio),1):
        for cont in range (0, len(tableroVacio[contDos]),1):
            if cont==0:
                print (columna[contDos], end="\t")
    #end del if
            print (tableroVacio[contDos][cont], end="\t ")
        print()#cada tres valores pon un enter
    print()
    
def turnoUno():
    #variables
    x=0
    y=0
    a=0
    b=0
    jugadorUnoPuntos=0
    #código
    print(jugadorUno, 'tu turno')
    #Selección de primera carta
    x=input('Renglón de la carta Uno: ')
    y=input('Columna de la carta Uno: ')
    while not(x in fila) or not(y in fila): #corrección si el index esta fuera de rango
        print('Por favor elige valores solo entre 0 y 5')
        if not(x in fila):
            x=input('Renglón de la carta Uno: (En un rango de 0 a 5): ')
        if not(y in fila):
            y=input('Columna de la carta Uno: (En un rango de 0 a 5): ')
    while tableroVacio[int(x)][int(y)]!='-': #corrección si es una casilla ya elegida
        print('Esa casilla ya esta elegida')
        x=input('Ingresa de nuevo el renglón de la carta Uno: ')
        y=input('Ingresa de nuevo la columna de la carta Uno: ')
        while not(x in fila) or not(y in fila): #corrección si el index esta fuera de rango
            print('Por favor elige valores solo entre 0 y 5')
            if not(x in fila):
                x=input('Ingresa de nuevo el renglón de la carta Uno: (En un rango de 0 a 5): ')
            if not(y in fila):
                y=input('Inglresa de nuevo la columna de la carta Uno: (En un rango de 0 a 5): ')
    x=int(x)
    y=int(y)
    print('Elegiste', tableroDatos[x][y])
    #Fin de elección de primera carta------Elección de segunda carta
    a=input('Renglón de la carta Dos: ')
    b=input('Columna de la carta Dos: ')
    while not(a in fila) or not(b in fila): #corrección si el index está fuera de rango
        print('Por favor elige valores solo entre 0 y 5')
        if not(a in fila):
            a=input('Ingresa de nuevo el renglón de la carta Dos: (En un rango de 0 a 5): ')
        if not(b in fila):
            b=input('Ingresa de nuevo la columna de la carta Dos: (En un rango de 0 a 5): ')
    while tableroVacio[int(a)][int(b)]!='-': #corrección si la casilla ya esta elegida
        print('Esa casilla ya esta elegida')
        a=input('Ingresa de nuevo el renglón de la carta Dos: ')
        b=input('Ingresa de nuevo la columna de la carta Dos: ')
    while (x,y)==(int(a),int(b)): #corrección si la carta ya esta elegida
        print('Esa carta ya esta elegida')
        a=input('Ingresa de nuevo el renglón de la carta Dos: ')
        b=input('Ingresa de nuevo la columna de la carta Dos: ')
        while not(a in fila) or not(b in fila): #corrección si el index esta fuera de rango
            print('Por favor elige valores solo entre 0 y 5')
            if not(a in fila):
                a=input('Ingresa de nuevo el renglón de la carta Dos: (En un rango de 0 a 5): ')
            if not(b in fila):
                b=input('Ingresa de nuevo la columna de la carta Dos: (En un rango de 0 a 5): ')
    a=int(a)
    b=int(b)
    print('Elegiste', tableroDatos[a][b])
    #Fin de elección de segunda carta
    if tableroDatos[x][y]==tableroDatos[a][b]:
        print('¡Memoria!')
        jugadorUnoPuntos+=1
        tableroVacio[x][y]=tableroDatos[x][y]
        tableroVacio[a][b]=tableroDatos[a][b]
    impTablero()
    return jugadorUnoPuntos
    
def turnoDos():
    #variables
    x=0
    y=0
    a=0
    b=0
    jugadorDosPuntos=0
    #código
    print(jugadorDos, 'tu turno')
    #Selección de primera carta
    x=input('Renglón de la carta Uno: ')
    y=input('Columna de la carta Uno: ')
    while not(x in fila) or not(y in fila): #corrección si el index esta fuera de rango
        print('Por favor elige valores solo entre 0 y 5')
        if not(x in fila):
            x=input('Renglón de la carta Uno: (En un rango de 0 a 5): ')
        if not(y in fila):
            y=input('Columna de la carta Uno: (En un rango de 0 a 5): ')
    while tableroVacio[int(x)][int(y)]!='-': #corrección si es una casilla ya elegida
        print('Esa casilla ya esta elegida')
        x=input('Ingresa de nuevo el renglón de la carta Uno: ')
        y=input('Ingresa de nuevo la columna de la carta Uno: ')
        while not(x in fila) or not(y in fila): #corrección si el index esta fuera de rango
            print('Por favor elige valores solo entre 0 y 5')
            if not(x in fila):
                x=input('Ingresa de nuevo el renglón de la carta Uno: (En un rango de 0 a 5): ')
            if not(y in fila):
                y=input('Inglresa de nuevo la columna de la carta Uno: (En un rango de 0 a 5): ')
    x=int(x)
    y=int(y)
    print('Elegiste', tableroDatos[x][y])
    #Fin de elección de primera carta------Elección de segunda carta
    a=input('Renglón de la carta Dos: ')
    b=input('Columna de la carta Dos: ')
    while not(a in fila) or not(b in fila): #corrección si el index esta fuera de rango
        print('Por favor elige valores solo entre 0 y 5')
        if not(a in fila):
            a=input('Ingresa de nuevo el renglón de la carta Dos: (En un rango de 0 a 5): ')
        if not(b in fila):
            b=input('Ingresa de nuevo la columna de la carta Dos: (En un rango de 0 a 5): ')
    while tableroVacio[int(a)][int(b)]!='-': #corrección si la casilla ya está elegida
        print('Esa casilla ya esta elegida')
        a=input('Ingresa de nuevo el renglón de la carta Dos: ')
        b=input('Ingresa de nuevo la columna de la carta Dos: ')
        while not(a in fila) or not(b in fila):#corrección si el index esta fuera de rango
            print('Por favor elige valores solo entre 0 y 5')
            if not(a in fila):
                a=input('Ingresa de nuevo el renglón de la carta Dos: (En un rango de 0 a 5): ')
            if not(b in fila):
                b=input('Ingresa de nuevo la columna de la carta Dos: (En un rango de 0 a 5): ')
    while (x,y)==(int(a),int(b)): #corrección si la carta ya esta elegida
        print('Esa carta ya esta elegida')
        a=input('Ingresa de nuevo el renglón de la carta Dos: ')
        b=input('Ingresa de nuevo la columna de la carta Dos: ')
        while not(a in fila) or not(b in fila):#corrección si el index está fuera de rango
            print('Por favor elige valores solo entre 0 y 5')
            if not(a in fila):
                a=input('Ingresa de nuevo el renglón de la carta Dos: (En un rango de 0 a 5): ')
            if not(b in fila):
                b=input('Ingresa de nuevo la columna de la carta Dos: (En un rango de 0 a 5): ')
    a=int(a)
    b=int(b)
    print('Elegiste', tableroDatos[a][b])
    #Fin de elección de segunda carta
    if tableroDatos[x][y]==tableroDatos[a][b]:
        print('¡Memoria!')
        jugadorDosPuntos+=1
        tableroVacio[x][y]=tableroDatos[x][y]
        tableroVacio[a][b]=tableroDatos[a][b]
    impTablero()
    return jugadorDosPuntos

main()