#Proyecto 1
#Datos generales
#José Francisco Godoy Castellanos 1245724
#Génesis Abigail Vides Valiente 1123324

import turtle

#Crea el recuadro de fondo con sus divisiones para hacer las escenas
def Back():
    #Se manda a limpiar la ventana de turtle para que no dibuje sobre otro dibujo
    turtle.clearscreen()
    #Le agregamos un nombre a la ventana de turtle, y las dimensiones en las que se abrirá
    turtle.title("El Pollo y el Conejo Amigo")
    turtle.setup(width=1100,height=900, startx=0, starty=0)
    #definimos back como turtle 
    back = turtle.Turtle() 
    back.speed(0)
    back.teleport(-450, 360)
    back.color("black")
    #Ciclo que crea el recuadro principal de fondo
    for i in range(2): 
        back.forward(900) 
        back.right(90) 
        back.forward(660) 
        back.right(90) 
    y=330
    #Ciclo que crea las divisiones del recuadro de fondo
    for i in range(2): 
        back.teleport(-450, y)
        back.forward(900) 
        y=-160
    back.hideturtle()

#Crea el pato de la historia
def Duck(d1,d2):
    duck = turtle.Turtle()
    duck.hideturtle()
    duck.speed(1000)
     #Cabeza/cuerpo
    duck.color('yellow')
    duck.fillcolor('yellow')
    duck.begin_fill()
    duck.teleport(0+d1,0+d2)
    for i in range(8):
        duck.left(45)
        duck.forward(60)
    
    duck.teleport(-105+d1,-90+d2)
    for i in range(3):
        duck.forward(150)
        duck.left(120)
    d11=0
    duck.right(60)
    for i in range(2):
        duck.teleport(-135+d11+d1,-37+d2)
        for i in range(3):
            duck.forward(60)
            duck.left(120)
        d11=150
    duck.end_fill()
    #Ala
    duck.color('orange')
    duck.fillcolor('orange')
    duck.begin_fill()
    duck.teleport(-80+d1,43+d2)
    duck.right(60)
    for i in range(3):
        duck.left(60)
        duck.forward(50)
    a=90
    a1=50
    #Pico
    for i in range(2):
        duck.left(a)
        duck.forward(30)
        a=30
        duck.left(a)
        duck.forward(a1)
        a1=0
    duck.end_fill()
    #Ojos
    duck.teleport(-60+d1,100+d2)
    duck.color('black'); duck.fillcolor('black')
    duck.begin_fill(); duck.circle(7); 
    duck.teleport(-10+d1,100+d2); duck.circle(7)
    duck.end_fill()

#Crea el pollo de la historia
def Bird(bi1,bi2): 
    bird = turtle.Turtle()
    bird.speed(0)
    #Cuerpo/cabeza
    bird.teleport(0+bi1,0+bi2)
    bird.color('yellow'); bird.fillcolor('yellow')
    bird.begin_fill(); bird.circle(50); 
    bird.teleport(15+bi1,75+bi2)
    bird.circle(40)
    bird.end_fill()
    #Ojos
    bird.teleport(15+bi1,120+bi2)
    bird.color('black'); bird.fillcolor('black')
    bird.begin_fill(); bird.circle(4); 
    bird.teleport(35+bi1,125+bi2); bird.circle(4)
    bird.end_fill()
    #Pico
    bird.teleport(20+bi1,100+bi2)
    bird.color('orange'); bird.fillcolor('orange')
    bird.begin_fill()
    bird.right(30)
    for i in range(3):
        bird.forward(20)
        bird.left(120)
    #Patas
    bird.teleport(-20+bi1,0+bi2)
    x=0
    for i in range(3):
        bird.forward(15)
        bird.left(120)
        x=x+1
        if x==3:
            bird.teleport(-10+bi1,+bi2)
            for i in range(3):
                bird.forward(15)
                bird.left(120)
            
    bird.teleport(10+bi1,5+bi2)
    x=0
    for i in range(3):
        bird.forward(15)
        bird.left(120)
        x=x+1
        if x==3:
            bird.teleport(19+bi1,7+bi2)
            for i in range(3):
                bird.forward(15)
                bird.left(120)
    bird.end_fill()
    bird.hideturtle() 

#Crea la secuencia de 3 arboles de fondo
def Trees():
    x1=0
    tree = turtle.Turtle()
    tree.speed(0)
    #Tronco
    for i in range(3):
        tree.teleport(-300+x1,-100)
        tree.color('brown'); tree.fillcolor('brown')
        tree.begin_fill()
        for i in range(2):
            tree.forward(20) 
            tree.left(90) 
            tree.forward(110) 
            tree.left(90) 
        tree.end_fill()
        #corona 
        tree.teleport(-370+x1,10)
        tree.color('green'); tree.fillcolor(color2)
        tree.begin_fill()
        x=0
        x2=0
        for i in range(3):
            tree.forward(160)
            tree.left(120)
            x=x+1
            if x==3:
                tree.teleport(-370+x1,100)
                for i in range(3):
                    tree.forward(160)
                    tree.left(120)
                    x2=x2+1
                    if x2==3:
                        tree.teleport(-348+x1,190)
                        for i in range(3):
                            tree.forward(115)
                            tree.left(120)
        tree.end_fill()                
        x1 = x1+300
        tree.hideturtle()

#Crea el recuadro que se tomara como cielo
def Sky(colorb=''):
    #cielo3
    sky1 = turtle.Turtle()
    sky1.speed(0)
    sky1.teleport(-449, 329)
    sky1.color(colorb); sky1.fillcolor(colorb)
    sky1.begin_fill()
    for i in range(2): 
        sky1.forward(898) 
        sky1.right(90) 
        sky1.forward(488) 
        sky1.right(90) 
    sky1.end_fill()
    sky1.hideturtle()

#Crea el conejo de la historia
def Rabbit(co1,co2):
    x4 = 0
    conejo = turtle.Turtle()
    conejo.speed(0)

    #cuerpo/cabeza
    conejo.fillcolor("grey")
    conejo.begin_fill()
    conejo.teleport(0+co1,0+co2)
    conejo.circle(60)
    conejo.teleport(0+co1, 80+co2)
    conejo.circle(45)
    conejo.end_fill()

    for i in range(2):
        conejo.begin_fill()
        conejo.fillcolor('grey')
        conejo.teleport(-10+co1+x4,0+co2)
        for i in range(3):
            conejo.left(120)
            conejo.forward(40) 
        x4= x4+60 
        conejo.end_fill()   
    x4=0
    for i in range(2):
        conejo.begin_fill()
        conejo.fillcolor('grey')
        conejo.teleport(-15+co1+x4,50+co2)
        for i in range(3):
            conejo.left(120)
            conejo.forward(30) 
        x4= x4+60
        conejo.end_fill()
    x4 = 0
    for i in range(2):
        conejo.begin_fill()
        conejo.fillcolor('black')
        conejo.teleport(-15+co1+x4,130+co2)
        conejo.circle(5)
        x4= x4+30
        conejo.end_fill()

    #nariz
    conejo.fillcolor('pink'), conejo.color('pink')
    conejo.teleport(10+co1, 120+co2)
    conejo.begin_fill()
    conejo.left(90)
    conejo.circle(10,extent=180)
    conejo.left(90)
    conejo.backward(-20)
    conejo.end_fill()

    #boca
    c1=0
    conejo.color('black')
    conejo.teleport(-15+co1,110+co2)
    conejo.backward(-30)
    conejo.fillcolor('white'), conejo.color('white')
    conejo.begin_fill()
    for i in range (2):
        conejo.teleport(-2+co1+c1,109+co2)
        for i in range (4):
            conejo.backward(10)
            conejo.left(90)
        c1=13   
    conejo.end_fill()
    conejo.hideturtle()

    #orejas
    v=90
    p=0
    conejo.color('black'), conejo.fillcolor('grey')
    conejo.begin_fill()
    for i in range (2):
        conejo.teleport(-20+co1+p,165+co2)
        for i in range (2):
            conejo.left(v)
            conejo.circle(50,extent=100)  
            v=60
        p=+40
    p=0
    v=90
    conejo.end_fill()
    conejo.color(color2), conejo.fillcolor('pink')
    conejo.begin_fill()
    conejo.left(50)
    for i in range (2):
        conejo.teleport(-30+co1+p,165+co2)
        for i in range (2):
            conejo.left(v)
            conejo.circle(20,extent=100)
            v=60
        p=40
    conejo.end_fill()

#Crea el apartado donde esta almacenado el contenido del primer texto de la historia
def Text1():
    #Texto1
    text = turtle.Turtle()
    text.speed(0)
    style = ('Arial', 14, 'italic')
    text.teleport(0, 335)
    text.write('Un nuevo amigo', move=False, font=style, align='center')
    text.teleport(-80, -185)
    text.write('Había una vez, en una granja colorida, un pollo alegre que se llamaba ', move=True, font=style, align='center')
    text.write(name, move=True, font=style); text.write('. ', move=True, font=style); text.write(name, move=True, font=style)
    text.teleport(-390, -205)
    text.write('tenía ', move=True, font=style, align='center')
    text.write(age, move=True, font=style); text.write(' años, era conocido por su espíritu juguetón y su curiosidad sin límites. Un día, mientras', move=True, font=style)
    text.teleport(0, -225)
    text.write('exploraba el campo, se encontró con un conejito tímido llamado Pancho, quien estaba ', move=True, font=style, align='center')
    text.teleport(-220, -245)
    text.write('buscando zanahorias para su cena. ', move=True, font=style, align='center')
    text.write(name, move=True, font=style); text.write(' y Pancho se miraron con curiosidad y ', move=True, font=style)
    text.teleport(0, -265)
    text.write('pronto se hicieron amigos inseparables.', move=True , font=style, align='center')
    text.hideturtle()
#Crea el recuadro que se tomara como la grama de las escenas
def Grass():
    grass = turtle.Turtle()
    grass.speed(1000)
    #rectangulo del cesped 
    grass.teleport(-449,-9)
    grass.color('chartreuse'); grass.fillcolor('chartreuse')
    grass.begin_fill()
    for i in range(2):
        grass.forward(898)
        grass.right(90)
        grass.forward(150)
        grass.right(90)
    grass.end_fill()
    grass.hideturtle()
#Crea la granja de la historia
def House():
    house = turtle.Turtle()
    house.speed(1000)
    #Techo1
    house.teleport(50,80)
    house.width(3)
    house.begin_fill()
    house.fillcolor(color2)
    for i in range (2):
        house.forward(220)
        house.left(60)
        house.forward(100)
        house.left(120)
    #Techo2
    house.teleport(271,80)
    house.width(3)
    house.begin_fill()
    house.fillcolor(color2)
    for i in range (3):
        house.forward(100)
        house.left(120)
    house.end_fill()

    #Pared
    house.teleport(50,80)
    house.width(3)
    house.begin_fill()
    house.fillcolor('khaki')
    for i in range (2):
        house.forward(220)
        house.right(90)
        house.forward(110)
        house.right(90)

    #Pared 2
    house.teleport(271,80)
    house.width(3)
    house.fillcolor('khaki')
    for i in range (2):
        house.forward(100)
        house.right(90)
        house.forward(110)
        house.right(90)
    house.end_fill()
 
    #Puerta
    house.teleport(135,46)
    house.width(3)
    house.begin_fill()
    house.fillcolor('brown')
    for i in range(2):
        house.forward(50)
        house.right(90)
        house.forward(75)
        house.right(90)
    house.teleport(170,10)
    house.fillcolor('black')
    house.circle(2)
    house.end_fill()

    x2 = 0
    for i in range (2):
        #Ventana
        house.teleport(70+x2,45)
        house.begin_fill()
        house.color('black'); house.fillcolor('light sky blue')
        for i in range(4):
            house.forward(40)
            house.right(90)
        house.end_fill()
        house.hideturtle()
        x2 = x2+140
#Crea una cerca para la granja
def Fences():
    x3 = 0
    fences=turtle.Turtle()
    fences.speed(1000)
    fences.hideturtle()
    # parte de abajo (rectangulo) 
    for i in range (12):
        for i in range (5):
            fences.teleport(-449+x3,30)
            fences.color('black'); fences.fillcolor('goldenrod')
            fences.begin_fill()
            for i in range (2):
                fences.forward(15)
                fences.right(90)
                fences.forward(50)
                fences.right(90)
            fences.end_fill()
            # Parte de arriba (triangulo)
            fences.speed(1000)
            fences.teleport(-449+x3,30)
            fences.color('black'); fences.fillcolor(color2)
            fences.begin_fill()
            for i in range(3):
                fences.forward(15)
                fences.left(120)
            fences.end_fill()
            x3 = x3+15
#Crea un circulo que se utilizara para el sol y luna en la historia
def Sun(colors=''):
    #sol/luna
    sun=turtle.Turtle()
    sun.hideturtle()
    sun.speed(1000)
    sun.teleport(-350,190)
    sun.color(colors)
    sun.begin_fill()
    sun.fillcolor(colors)
    sun.circle(55)
    sun.end_fill()
#Crea un solo árbol
def Tree():
    tree = turtle.Turtle()
    tree.speed(1000)
    #Tronco
    for i in range(3):
        tree.teleport(-200,-100)
        tree.color('brown'); tree.fillcolor('brown')
        tree.begin_fill()
    for i in range(2):
        tree.forward(20) 
        tree.left(90) 
        tree.forward(110) 
        tree.left(90) 
    tree.end_fill()
    #Corona
    tree.teleport(-270,10)
    tree.color('green'); tree.fillcolor('green')
    tree.begin_fill()
    for i in range(3):
        tree.forward(160)
        tree.left(120)
    tree.teleport(-270,100)
    for i in range(3):
        tree.forward(160)
        tree.left(120)
    tree.teleport(-248,190)
    for i in range(3):
        tree.forward(115)
        tree.left(120)
    tree.end_fill()                
    tree.hideturtle()
#Crea una nube en la escena
def Clouds():
    clouds=turtle.Turtle()
    #Nube 1
    x3 = 0
    for i in range(2):
        clouds.speed(1000)
        clouds.teleport(-320+x3,185)
        clouds.begin_fill()
        clouds.fillcolor('white'); clouds.color('white')
        clouds.circle(40)
        x=x3+160
    #Nube 2
    clouds.teleport(-300,190)
    clouds.fillcolor('white'); clouds.color('white')
    clouds.circle(40)
    clouds.end_fill()
    clouds.hideturtle()
#Crea un pastel para la  última escena
def pastel():
    # La base del pastel
    pastel = turtle.Turtle()
    p1=0
    p2=0
    pastel.speed(1000)
    pastel.teleport(-120,-150)
    pastel.begin_fill()
    pastel.fillcolor('wheat2'); pastel.color('wheat2')
    for i in range (2):
        pastel.forward(100)
        pastel.left(90)
        pastel.forward(50)
        pastel.left(90)
    # Decoración
    for i in range(11):
        for i in range(1):
            pastel.teleport(-120+p1,-150)
            pastel.circle(5); pastel.fillcolor(color2)
            p1=10+p1
    for i in range(11):
        for i in range(1):
            pastel.teleport(-120+p2,-102)
            pastel.circle(5); pastel.fillcolor(color2)
            p2=10+p2
    pastel.hideturtle()
    pastel.end_fill()
#Almacena las figuras que se utilizaran en la primer escena
def Scene1():
    Back()
    Sky('skyblue')
    Grass()
    Text1()
    Fences()
    House()
    Sun('yellow')
    Clouds()
    Tree()
    Bird(100,-150)
    Rabbit(250,-150)

#Crea el apartado donde esta almacenado el contenido del segundo texto de la historia
def Text2():
    #Texto2
    text2 = turtle.Turtle()
    text2.speed(0)
    style = ('Arial', 14, 'italic')
    text2.teleport(0, 335)
    text2.write('Una aventura divertida', move=False, font=style, align='center')
    text2.teleport(-340, -205)
    text2.write('Juntos, ', move=True, font=style, align='center'); text2.write(name, move=True, font=style)
    text2.write(' y Pancho pasaban sus días explorando la granja y jugando entre las', move=True, font=style)
    text2.teleport(-250, -225)
    text2.write('flores y los campos verdes. ', move=True, font=style, align='center')
    text2.write(name, move=True, font=style); text2.write(' enseñaba a Pancho a cantar canciones alegres', move=True, font=style)
    text2.teleport(0, -245)
    text2.write('y Pancho compartía sus sabios consejos sobre cómo esquivar a los gruñones gatos ', font=style, align='center')
    text2.teleport(0, -265)
    text2.write('de la granja. Su amistad creció cada día más fuerte, llenando el aire con risas y alegría.', font=style, align='center')
    text2.hideturtle()
#Almacena las figuras que se utilizaran en la segunda escena
def Scene2():
    turtle.title("PROYECTO 01 / 1245724-1123324")
    turtle.setup(width=1100,height=900, startx=0, starty=0)
    Back()
    Sky('skyblue')
    Grass()
    Text2()
    Sun('yellow')
    Clouds()
    Trees()
    Bird(100,-150)
    Rabbit(250,-150)

#Crea el apartado donde esta almacenado el contenido del tercer texto de la historia
def Text3():
    #Texto3
    text3 = turtle.Turtle()
    text3.speed(0)
    style = ('Arial', 14, 'italic')
    text3.teleport(0,335)
    text3.write('Un día en el estanque', move=False, font=style, align='center')
    text3.teleport(0, -205)
    text3.write('Un día, mientras jugaban cerca del estanque, escucharon un chillido desesperado. Rápidamente ', font=style, align='center')
    text3.teleport(0, -225)
    text3.write('corrieron hacia el sonido y descubrieron a un patito atrapado en el fango. Con trabajo en equipo', font=style, align='center')
    text3.teleport(-290, -245)
    text3.hideturtle()
    text3.write('y determinación, ', move=True, font=style, align='center'); text3.write(name, move=True, font=style)
    text3.write(' y Pancho lograron rescatar al patito, quien les agradeció con ', move=True, font=style)
    text3.teleport(0, -265)
    text3.write('un dulce graznido.', font=style, align='center')
#Crea solo un arbol para la escena
def tree():
    tree = turtle.Turtle()
    tree.speed(1000)
    #Tronco
    for i in range(3):
        tree.teleport(-300,-100)
        tree.color('brown'); tree.fillcolor('brown')
        tree.begin_fill()
    for i in range(2):
        tree.forward(20) 
        tree.left(90) 
        tree.forward(110) 
        tree.left(90) 
    tree.end_fill()
    #Corona
    tree.teleport(-370,10)
    tree.color('green'); tree.fillcolor('green')
    tree.begin_fill()
    for i in range(3):
        tree.forward(160)
        tree.left(120)
    tree.teleport(-370,100)
    for i in range(3):
        tree.forward(160)
        tree.left(120)
    tree.teleport(-348,190)
    for i in range(3):
        tree.forward(115)
        tree.left(120)
    tree.end_fill()                
    tree.hideturtle()
#Crea un lago en la escena 4
def Lake():
    lake = turtle.Turtle()
    lake.speed(1000)
    #lago
    v=125
    p=0
    lake.teleport(300,-80)
    lake.color('blue'), lake.fillcolor('blue')
    lake.begin_fill()
    for i in range (2):
        lake.left(v)
        lake.circle(170,extent=110)
        v=70
    lake.end_fill()
    lake.hideturtle()
#Crea gotas para la escena 4
def Gota(g1,g2):
    gota = turtle.Turtle()
    gota.speed(1000)
    #Gota 1
    #parte de abajo(circulo)
    for i in range(2):
        for i in range (1):
            gota.teleport(-120+g1,-80+g2)
            gota.begin_fill()
            gota.fillcolor('blue'); gota.color('blue')
            gota.circle(5)
            gota.teleport(-124+g1,-75+g2)
            gota.fillcolor('blue'); gota.color('blue')
            g1=180
            for i in range(3):
                gota.forward(8)
                gota.left(120)
    #Parte de arriba(triangulo)
    for i in range(2):
        for i in range (1):
            gota.teleport(-205+g1,-95+g2)
            gota.begin_fill()
            gota.fillcolor('blue'); gota.color('blue')
            gota.circle(5)
            gota.teleport(-210+g1,-90+g2)
            gota.fillcolor('blue'); gota.color('blue')
            g1=160
            g2=90
            for i in range(3):
                gota.forward(8)
                gota.left(120)
            gota.hideturtle()
    #Gota 3
    gota.teleport(-205+g1,-50+g2)
    gota.begin_fill()
    gota.fillcolor('blue'); gota.color('blue')
    gota.circle(5)
    gota.teleport(-210+g1,-45+g2)
    gota.fillcolor('blue'); gota.color('blue')
    for i in range(3):
        gota.forward(8)
        gota.left(120)
    # Gota 4
    gota.teleport(-150+g1,-50+g2)
    gota.begin_fill()
    gota.fillcolor('blue'); gota.color('blue')
    gota.circle(5)
    gota.teleport(-155+g1,-45+g2)
    gota.fillcolor('blue'); gota.color('blue')
    for i in range(3):
        gota.forward(8)
        gota.left(120)
    gota.hideturtle()
    gota.end_fill()
#Almacena las figuras que se utilizaran en la tercera escena
def Scene3():
    Back()
    Sky('skyblue')
    Grass()
    Text3()
    Lake()
    Sun('yellow')
    Clouds()
    Tree()
    Bird(-200,-150)
    Rabbit(-350,-150)
    Duck(0,-67)
    Gota(0,-67)

#Crea el apartado donde esta almacenado el contenido del cuarto texto de la historia
def Text4():
    #Texto4
    text4 = turtle.Turtle()
    text4.speed(0)
    style = ('Arial', 14, 'italic')
    text4.teleport(0, 335)
    text4.write('Amigos Inseparables', move=False, font=style, align='center')
    text4.teleport(0, -205)
    text4.write('Tuvieron una agradable tarde caminando por el sendero del bosque y jugando a atraparse uno al otro', font=style, align='center')
    text4.teleport(-240, -225)
    text4.write('hasta llegar a la granja donde vivía ', move=True, font=style, align='center'); text4.write(name, move=True, font=style)
    text4.write('. Pero antes de entrar a la granja, hicieron un ', move=True, font=style)
    text4.teleport(0, -245)
    text4.write('juramento , tanto el conejo, como el pollo y el patito para formar una pandilla de amigos inseparables.', font=style, align='center')
    text4.teleport(0, -265)
    text4.write('Y así fue, entraron a la granja para poder descansar y despedirse, pero...', font=style, align='center')
    text4.hideturtle()
#Almacena las figuras que se utilizaran en la cuarta escena
def Scene4():
    Back()
    Sky('orange')
    Grass()
    Text4()
    Fences()
    House()
    Sun('yellow')
    Tree()
    Bird(-200,-150)
    Rabbit(-350.-150)
    Duck(0,-67)

#Crea el apartado donde esta almacenado el contenido del quinto texto de la historia
def Text5():
    #Texto5
    text5 = turtle.Turtle()
    text5.speed(0)
    style = ('Arial', 14, 'italic')
    text5.teleport(0, 335)
    text5.write('La unión de una gran amistad', move=False, font=style, align='center')
    text5.teleport(0, -185)
    text5.write('Al caer la noche, los tres amigos entraron a la granja y compartiendo las historias de sus aventuras', font=style, align='center')
    text5.teleport(-250, -205)
    text5.write('del día se toparon a la madre de ', move=True, font=style, align='center'); text5.write(name, move=True, font=style)
    text5.write(', al ver la amistad que había surgido entre el pollo, ', move=True, font=style)
    text5.teleport(0, -225)
    text5.write('el conejo y el patito, les preparó un festín de maíz y zanahorias. Mientras compartían la comida,', font=style, align='center')
    text5.teleport(-390, -245)
    text5.write(name, move=True, font=style)
    text5.write(', Pancho y el patito se dieron cuenta de que, con amigos como ellos, cada día ', move=True, font=style)
    text5.teleport(0, -265)
    text5.write('en la granja sería una nueva aventura llena de amor y compañerismo. Y así, bajo el cálido resplandor', font=style, align='center')
    text5.teleport(0, -285)
    text5.write(' de la luna, sellaron su amistad para siempre.', font=style, align='center')
    text5.hideturtle()
#Almacena las figuras que se utilizaran en la quinta escena
def Scene5():
    Back()
    Sky('blue')
    Grass()
    Text5()
    House()
    Sun('white')
    Tree()
    Bird(-200,-150)
    Rabbit(-350,-150)
    pastel()
    Duck(140,-67)

#Pedida de datos
color1 = 0
#Se imprime el titulo del cuento
print("El Pollo y el Conejo Amigo")
#Se pide el nombre a la persona
print("Ingrese su nombre")
name =input()
#Se pide la edad de la persona
print("Ingrese su edad")
age = int(input())
#Ciclo para repetir la pregunta del color en caso que ingrese un valor no definido
while color1<=0 or color1>5:
    print("Elija un color: 1)Rojo, 2)Verde, 3)Amarillo, 4)Azul, 5)Morado")
    color1 =int(input("Color elegido es el No. "))
    if color1<=0 or color1>5:
        print('Color no definida, intente de nuevo')
        print()
    else: 
        #Dependiendo del numero ingresado, se definira color2 con un nombre de color para ingresar en las figuras posteriormente
        match(color1):
            case 1:
                color2 = 'red'
            case 2:
                color2 = 'green'
            case 3:
                color2 = 'yellow'
            case 4:
                color2 = 'blue'
            case 5:
                color2 = 'purple'
#Se define la variable scene como 0
scene=0
#Se hace un ciclo para elegir la escena, y después de mostrarla, volver a preguntar al usuario si quiere visualizar otra escena
#Para salir del ciclo, el usuario debe elegir opción 6, y si coloca otro número se tomara como no definido y volvera a pedir la escena
n=1
while n==1:
    print()
    print("Elija la escena a visualizar de 1-5:")
    print("Elija 6 para salir del ciclo")
    scene =int(input("Escena No. "))
    if scene == 1: 
        Scene1()
    elif scene == 2:

        Scene2()
    elif scene == 3:

        Scene3()
    elif scene == 4:
 
        Scene4()
    elif scene == 5:

        Scene5()               
    elif scene == 6: 
        #Elige la opción 6, se cierra la ventana de turtle si es que esta abierta con .bye()
        turtle.bye()
        n = 0 
        print('Gracias por ver nuestra historia :)')        
    else:       
        print('Escena no definida, intente de nuevo')
        print()
