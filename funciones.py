#!/usr/bin/env python
#-*- coding: utf-8 -*-

#Cargamos las librerÃ­as necesarias
import turtle
import random
import math

#Se realizan funciones de apoyo para que el main.py con nombres bien representativos
def dibujarElementosDinamicos(basura, jugador, cronometro, tiempoActual, puntuador, puntosActuales, modoDeJuego):
  
  if tiempoActual > 0:
    cronometro.write(tiempoActual, font=("Arial", 16, "bold"))
  if puntosActuales > 0:
    puntuador.write(puntosActuales, font=("Arial", 16, "bold"))
  basura.showturtle()
  jugador.showturtle()  
 

def moverBasura(basura, patronMovimiento):
  basura.penup()
  
  if (patronMovimiento=='linea'):
    basura.forward(20)
 
  if (patronMovimiento=='aleatorio'):
    basura.right(random.randint(-180,180))
    basura.forward(25)
    basura.setx(basura.xcor()+random.randint(-20,20))
    basura.sety(basura.ycor()+random.randint(-20,20))
 
  return basura

def obtenerBasura():
  imgs = ["organico.gif", "vidrio.gif","lata.gif", "otros.gif", "papel.gif", "toxico.gif"]
  imgActual=random.choice(imgs)
  basura = turtle.Turtle()
  basura.hideturtle()
  basura.shape(imgActual)
  basura.penup()
  basura.goto(random.randint(-180,180),random.randint(-180,180)) 
  return basura

#se agrega la funcion de que solo aparezca basura organica

def obtenerBasuraOrganica():
  gif = ["organico.gif"]
  imgActual=random.choice(gif)
  basura = turtle.Turtle()
  basura.hideturtle()
  basura.shape(imgActual)
  basura.penup()
  basura.goto(random.randint(-180,180),random.randint(-180,180)) 
  return basura
#agregamos una funcion para que el obstaculo aparezca en la pantalla

def obtenerObstaculo():
  obstaculo=turtle.Turtle()
  obstaculo.shape("contenedor.gif")
  obstaculo.penup()
  obstaculo.setx(-200)
  obstaculo.sety(-200)
  return obstaculo

def obtenerJugador():
  jugador=turtle.Turtle()
  jugador.shape("robot.gif")
  jugador.penup()
  jugador.setx(145)
  jugador.sety(0)
  return jugador
  
def obtenerCronometro():
  tiempoRestante=turtle.Turtle()
  tiempoRestante.penup()
  tiempoRestante.hideturtle()
  tiempoRestante.setx(-370)
  tiempoRestante.sety(210)
  
  return tiempoRestante
  
def obtenerPuntuador():
  puntuador=turtle.Turtle()
  puntuador.penup()
  puntuador.hideturtle()
  puntuador.setx(-370)
  puntuador.sety(170)
  
  return puntuador
  
def obtenerTxtTiempoRestante():
  txtTiempoRestante=turtle.Turtle()
  txtTiempoRestante.penup()
  txtTiempoRestante.hideturtle()
  txtTiempoRestante.setx(-190)
  txtTiempoRestante.sety(170)
  return txtTiempoRestante 
  
def obtenerTxtPuntos():
  txtPuntos=turtle.Turtle()
  txtPuntos.penup()
  txtPuntos.hideturtle()
  txtPuntos.setx(-190)
  txtPuntos.sety(145)
  return txtPuntos   

def reubicarBasuraSiSeVa(bas):
    x = bas.xcor()
    y = bas.ycor()
    
    if x > 400:
      bas.setx(400)
    elif x < -400:
      bas.setx(-400)
    if y > 180:
      bas.sety(180)
    elif y < -180:
      bas.sety(-180)
    return bas

def reubicarJugadorSiSeVa(jug):
    x = jug.xcor()
    y = jug.ycor()
    
    if x > 350:
      jug.setx(350)
    elif x < -350:
      jug.setx(-350)
  
    if y > 160:
      jug.sety(160)
    elif y < -165:
      jug.sety(-165)
    return jug

def colisionan(obj, jugador, umbral):
  d=math.sqrt(math.pow(obj.xcor()-jugador.xcor(),2)+math.pow(obj.ycor()-jugador.ycor(),2))
  if d < umbral:
    return True
  else:
    return False
  
 
 
