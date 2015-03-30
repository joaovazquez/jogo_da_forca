import turtle
window=turtle.Screen()
window.setup(width=1400,startx=None, starty=None)
window.bgcolor('yellow')
window.title('Forca')

def construindo_forca():
    
    lapis=turtle.Turtle()
    lapis.speed(3)
    lapis.pensize(8)
    lapis.back(200)
    lapis.penup()
    lapis.left(90)
    lapis.pendown()
    lapis.forward(200)
    lapis.penup()
    lapis.right(90)
    lapis.pendown()
    lapis.forward(100)
    lapis.penup()
    lapis.right(90)
    lapis.pendown()
    lapis.forward(20)

def construindo_cabeca():
    
    lapis=turtle.Turtle()          
    lapis.speed(3)
    lapis.pensize(7)
    lapis.penup()
    lapis.setpos(-180,180)
    lapis.left(180)
    lapis.pendown()
    lapis.circle(20)
    lapis.color('blue')

def construindo_corpo():
    
    lapis=turtle.Turtle()
    lapis.speed(3)
    lapis.pensize(5)
    lapis.penup()
    lapis.setpos(-180,140)
    lapis.pendown()
    lapis.right(90)
    lapis.forward(100)
    lapis.color('blue')

def construindo_braco1():
    
    lapis=turtle.Turtle()
    lapis.speed(3)
    lapis.pensize(5)
    lapis.penup()
    lapis.setpos(-180,120)
    lapis.pendown()
    lapis.right(135)
    lapis.forward(40)
    lapis.color('blue')

def construindo_braco2():
    
    lapis=turtle.Turtle()
    lapis.speed(3)
    lapis.pensize(5)
    lapis.penup()
    lapis.setpos(-180,120)
    lapis.pendown()
    lapis.right(400)
    lapis.forward(40)
    lapis.color('blue')

def construindo_perna1():
    
    lapis=turtle.Turtle()
    lapis.speed(3)
    lapis.pensize(5)
    lapis.penup()
    lapis.setpos(-180,40)
    lapis.pendown()
    lapis.right(30)
    lapis.forward(40)
    lapis.color('blue')

def construindo_perna2():
    
    lapis=turtle.Turtle()
    lapis.speed(3)
    lapis.pensize(5)
    lapis.penup()
    lapis.setpos(-180,40)
    lapis.left(60)
    lapis.forward(40)
    lapis.color('blue')


import random
arquivo=open('palavrasprojeto2.csv','r')
leitura=arquivo.read(50)
lista=leitura.split(';')
palavra=random.choice(lista)

for x in range(100):
     print()
digitadas=[]
acertos=[]
erros=0
while True:
     senha=""
     for letra in palavra:
         senha+=letra if letra in acertos else "."
     def construindo_linhas():
         lapis=turtle.Turtle()
         lapis.hideturtle()
         lapis.penup()
         lapis.setpos(-180,20)
         lapis.write(senha,move=False,align='left',font=('Cambria',45,'normal'))
         construindo_linhas()
     if senha==palavra:
         print("Você acertou!")
         break
     tentativa=window.textinput('Digite uma letra','Digite uma letra')
     if tentativa==('parar'):
         break
     if tentativa in digitadas:
         print("Você já tentou essa letra!")
         continue
     else:
         digitadas+=tentativa
         if tentativa in palavra:
               acertos+=tentativa
         else:
               erros+=1
               print("Você errou!")
               construindo_forca()
     if erros>=1:
         construindo_cabeca()
     linha2=""
     if erros==2:
         construindo_corpo()
     elif erros==3:
         construindo_braco1()
     elif erros>=4:
         construindo_perna1()
     if erros==5:
         construindo_braco2()
     elif erros>=6:
         construindo_perna2()
     if erros==6:
         print("Enforcado!")
         break
     
window.exitonclick()

