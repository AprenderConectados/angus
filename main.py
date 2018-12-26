#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Hola! Bienvenido a la Ronda 2. Manos a la obra y éxitos!
#Cuando finalicen las consignas del desafío de la Ronda, guarden su código en su disco local con las imágenes que utilizaron
#Suban en la "Plataforma de la Maratón" su proyecto en formato ZIP, comprimiendo los documentos necesarios para ejecutar el código

#Cargamos las librerias necesarias
import turtle
from funciones import *
import time
import pygame


#Cargamos los recursos de imagenes. Primero se deben subir y activar a Trinket
screen = turtle.Screen()

screen.register_shape("organico.gif")
screen.register_shape("vidrio.gif")
screen.register_shape("lata.gif")
screen.register_shape("otros.gif")
screen.register_shape("papel.gif")
screen.register_shape("toxico.gif")
screen.register_shape("robot.gif")
screen.register_shape("contenedor.gif")

#Inicializamos variables
puedoConfigurar=True
jugando = False
situada = False
patronMovimiento='aleatorio'  
modoDeJuego='porTiempo'
global txtInstrucciones
tiempoTotalConfigurado=30
puntosTotalesConfigurados=1000
nombreJugador='Jug1'
tiempoTotal=tiempoTotalConfigurado
puntosTotales=puntosTotalesConfigurados
tiempoActual=0
puntosActuales=0
#se agrega una variable de nombre.Para poder usar en el codigo de texto
nombre = input("Ingrese numero")

def mostrarMenu():
  global txtInstrucciones, puedoConfigurar, ranking
  
  txtInstrucciones = turtle.Turtle()
  
  txtInstrucciones.hideturtle()
  txtInstrucciones.speed(0)
  txtInstrucciones.penup()

  txtInstrucciones.setx(-350)
  txtInstrucciones.sety(50)
  txtInstrucciones.right(90)

  txtInstrucciones.color("dark blue")
  txtInstrucciones.forward(-150)
  txtInstrucciones.write("¡Angus al Rescate, Reciclemos Juntos!",  font=("Bookman Old Style", 28, "bold"))
  txtInstrucciones.forward(60)
  txtInstrucciones.write("Ayuda a Angus a recolectar los residuos, moviendolo con las flechas.\nRecolecta la mayor cantidad, ayuda al planeta y suma puntos.", font=("Batang", 12, "bold"))
  txtInstrucciones.forward(70)
  txtInstrucciones.write("Menú", font=("Bookman Old Style", 18, "bold"))
  txtInstrucciones.forward(40)
  txtInstrucciones.write("a - Configuracion del juego", font=("Batang", 12, "bold"))
  txtInstrucciones.forward(30)
  txtInstrucciones.write("b - Empezar juego por tiempo", font=("Batang", 12, "bold"))
  txtInstrucciones.forward(30)
  txtInstrucciones.write("c - Empezar juego por puntos", font=("Batang", 12, "bold"))
  txtInstrucciones.forward(30)
  txtInstrucciones.write("d - Empezar juego Modo Orgánico", font=("Batang", 12, "bold"))
  txtInstrucciones.forward(30)
  txtInstrucciones.write("e - Salir del juego y volver al menu", font=("Batang", 12, "bold"))
  
  
  archivo = open("Modo por Tiempo.txt" , "r")
  lista = archivo.read()

  ranking = turtle.Turtle()
  ranking.hideturtle()
  ranking.penup()
  ranking.right(90)
  ranking.forward(100)
  archivo = open ("Modo por Tiempo.txt", "r")
  lista = archivo.read()
  ranking.color ("dark blue")
  ranking.write ((lista), font = ("Batang" ,12, "bold"))
  
  
  puedoConfigurar = True
  screen.update()

mostrarMenu()
 
#Definimos al bucle del juego
def loopJuego():
  
  global jugando, txtInstrucciones, ranking ,obstaculo , situada, jugador, patronMovimiento, puedoConfigurar, modoDeJuego, tiempoTotal, puntosTotales, puntosActuales, nombreJugador
  
#variables para las frases
  frase=turtle.Turtle()
  a=3
  tiempos=a
  
  txtInstrucciones.clear()
  ranking.clear()
  screen = turtle.Screen()
  screen.bgpic("fondo.gif")

  obstaculo = obtenerObstaculo()
  jugador=obtenerJugador()
  cronometro=obtenerCronometro()
  puntuador=obtenerPuntuador()

  
  txtTiempoRestante=obtenerTxtTiempoRestante()
  txtTiempoRestante.setx(-470)
  txtTiempoRestante.sety(210)
  txtTiempoRestante.write('Tiempo: ', font=("Batang", 18, "bold"))
  txtPuntos=obtenerTxtPuntos()
  txtPuntos.setx(-470)
  txtPuntos.sety(170)
  txtPuntos.write('Puntos: ', font=("Batang", 18, "bold"))
  
  tiempoInicio=int(round(time.time()))
  
  auxTiempo=int(round(time.time()-tiempoInicio))
  auxPuntos=0
  
  if (modoDeJuego=='porTiempo'):
    puntosActuales=0
    tiempoRestante=tiempoTotalConfigurado
  elif (modoDeJuego=='porPuntos'):
    puntosActuales=puntosTotalesConfigurados
    puntosRestantes=0
    tiempoRestante=0
  elif (modoDeJuego=='modoOrganico'):
    puntosActuales=0
    tiempoRestante=tiempoTotalConfigurado

  if (modoDeJuego=='modoOrganico'):
    bas=obtenerBasuraOrganica()
  else:
    bas=obtenerBasura()

   
 #se escriben las diferentes frases que apareceran en pantalla  
  fra = ["super!", "genial", "wow!","bien hecho","gran trabajo", "sigue asi"]
  
  diccionarioPuntaje = {"organico.gif" : "200", "otros.gif" : "10", "toxico.gif" : "150", "vidrio.gif" : "75", "lata.gif" : "50", "papel.gif" : "30" }

  
  while (jugando == True):
  
    puedoConfigurar=False
    tiempoRestante=int(round(time.time()-tiempoInicio))
    if (modoDeJuego=='porTiempo'):
      
  
      if not (tiempoRestante==auxTiempo):
        cronometro.clear()
        auxTiempo = tiempoRestante
    
      tiempoRestante=tiempoTotal-tiempoRestante
    
    elif (modoDeJuego=='porPuntos'):
      if not (tiempoRestante==auxTiempo):
        cronometro.clear()
        auxTiempo = tiempoRestante
      
      auxPuntos = puntosRestantes

    if (modoDeJuego=='modoOrganico'):
      
  
      if not (tiempoRestante==auxTiempo):
        cronometro.clear()
        auxTiempo = tiempoRestante
        
      tiempoRestante=tiempoTotal-tiempoRestante

 
    patrones=['linea', 'aleatorio']
    bas=moverBasura(bas, patronMovimiento)
    
    if (situada==False):
      patronMovimiento=random.choice(patrones)
      situada=True      
    
    bas=moverBasura(bas, patronMovimiento)
    
    bas=reubicarBasuraSiSeVa(bas)
    jugador=reubicarJugadorSiSeVa(jugador)
    
    num=int(diccionarioPuntaje[bas.shape()])
    x= bas.xcor()
    y= bas.ycor()
#agregamos el codigo para que el jugador no pueda pasar por el obstaculo
    if (colisionan(jugador, obstaculo , 110) == True):
      situada = False
      jugador.setx(10)
      jugador.sety(-10)
      
      
      
    
        
      
  
    if (colisionan(jugador, bas, 60) == True):
        
      situada = False
      bas.hideturtle()
      bas.clear()
      bas=obtenerBasura()

      #Aqui agrego la frase
      Frasealeatoria = random.choice(fra)
      frase.color("dark orange")
      frase.write(Frasealeatoria, font =("Arial", 18, "bold"))
      frase.goto(random.randint(-180,180),random.randint(130,180))
      
      situada = False
      bas.hideturtle()
      bas.clear()
      bas=obtenerBasura()


      if (modoDeJuego=='modoOrganico'):
          bas=obtenerBasuraOrganica()
      else:
          bas=obtenerBasura()
        
      if(modoDeJuego=='porPuntos'):
        if (x>0 and y > -200):
          puntosActuales=puntosActuales-num
        
        if (puntosActuales<=0):
          
          cronometro.clear()
          puntuador.clear()
          jugando=False
          
          
      else:
        if (x>0 and y > -200):
          puntosActuales=puntosActuales+num
        else:
          puntosActuales=puntosActuales
      
      if not (puntosActuales==auxPuntos):
        puntuador.clear()
        auxPuntos=puntosActuales


#Establecer el tiempo de las frases
    frase.penup()
    frase.hideturtle()
    if (tiempos == 0):
         frase.clear()
    else:
      tiempos = tiempos-1
  
         

        
    if (modoDeJuego=='porTiempo'):  
     if (tiempoRestante<=0):
      
        cronometro.clear()
        jugando=False
      
      
    if (modoDeJuego=='modoOrganico'):
     if (tiempoRestante<=0):
      
        cronometro.clear()
        jugando=False
         
    dibujarElementosDinamicos(bas, jugador, cronometro, tiempoRestante, puntuador, puntosActuales, modoDeJuego)
    screen.update()

  #se agrega el codigo para que el archivo de texto aparezca con los tiempos y puntajes de cada jugador
  if 'porTiempo':
    archivo = open ("Modo por Tiempo.txt", "a")
    archivo.write ("Nombre del Jugador: " + nombre + "    " + "Puntuación: " + str(puntosActuales))
    archivo.write ("\n\n")
    archivo.close()



  elif 'porPuntos' :
    archivo1 = open ("Modo por Puntos.txt" ,"a")
    archivo1.write ("Nombre del Jugador: " + nombre + "    " +  "Tiempo:  " + str(tiempoRestante))
    archivo1.write ("\n\n")
    archivo1.close()
  
  #Si el juego esta¡ detenido borramos todo
    
  jugador.hideturtle()
  jugador.clear()
  txtTiempoRestante.clear()
  txtTiempoRestante.hideturtle()
  txtPuntos.clear()
  txtPuntos.hideturtle()
  puntuador.clear()
  puntuador.hideturtle()
  cronometro.clear()
  cronometro.hideturtle()
  bas.hideturtle()
  bas.clear()
  txtInstrucciones.hideturtle()
  txtInstrucciones.clear()
    
  mostrarMenu()
  
               
#Definimos la operacion de comienzo de juego
def empezarJuego():
  global jugando, puedoConfigurar
  if (jugando==False):
    jugando = True
    loopJuego()
   
def empezarJuegoPorPuntos():
  global modoDeJuego
  modoDeJuego='porPuntos'
  empezarJuego()

def empezarJuegoPorTiempo():
  global modoDeJuego
  modoDeJuego='porTiempo'
  empezarJuego()

def empezarJuegoPorModoOrganico():
  global modoDeJuego
  modoDeJuego='modoOrganico'
  empezarJuego()

def volverAlMenu():
  global jugando, puedoConfigurar
  jugando = False
  puedoConfigurar=False
  
  
def ingresarParametrosDeConfiguracion():
  global tiempoTotal, puntosTotalesConfigurados, puedoConfigurar, jugando, nombreJugador
  
  if (jugando==False):
  
    if (puedoConfigurar==True):
      puedoConfigurar=False
      tiempoTotal= int(input("Ingrese la cantidad de segundos que dispondra el jugador para el Modo por Tiempo"))
      puntosTotalesConfigurados= int(input("Ingrese el puntaje maximo para el Modo Puntos"))
      
      if not (tiempoTotal > 0):
        tiempoTotal=10
      if not (puntosTotalesConfigurados > 0):
        puntosTotalesConfigurados=5

      
#Definimos las funciones de movimiento del jugador
def atras():
  global jugador
  jugador.sety(jugador.ycor()-30)

def adelante():
  global jugador
  jugador.sety(jugador.ycor()+30)

def izquierda():
    global jugador
    jugador.setx(jugador.xcor()-30)

def derecha():
    global jugador
    jugador.setx(jugador.xcor()+30)

def salirDelJuego():
  global jugando
  jugando=False  



#Realizamos codigo que invoca las funciones anteriores segun la tecla que se presione  

turtle.onkey(adelante, "Up")
turtle.onkey(atras, "Down")
turtle.onkey(izquierda, "Left")
turtle.onkey(derecha, "Right")
turtle.onkey(empezarJuegoPorPuntos, "c")
turtle.onkey(empezarJuegoPorTiempo, "b")
turtle.onkey(empezarJuegoPorModoOrganico, "d")
turtle.onkey(ingresarParametrosDeConfiguracion, "a")
turtle.onkey(salirDelJuego, "e")
turtle.listen()
turtle.mainloop()

