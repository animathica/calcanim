from sys import float_repr_style
from manimlib.imports import *

############################################################
################ coordenadas polares y cartesianas #########
############################################################
#Aparece en excel como Campos lineales, sin embargo el vídeo se dividirá en dos partes para que no sea tan largo


class Polares_y_Cartesianas(Scene):

    def parte1 (self):
        titulo=TextMobject('''Coordenadas polares y \n
                                cartesianas''').scale(2)
        text1=TextMobject('''En el curso de Cálculo Vectorial Integral \n
                             se suele trabajar en espacios tipo $\\mathbb{R}^{n}$,\n
                              así que siempre tendremos una base con la cual trabajar \n
                               y con ello un sistema de coordenadas.''')
        text2=TextMobject('''En diversas ocasiones es más práctico optar por \n
                             unas coordenadas que por otras, \n
                             así que es importante dominar los cambios de \n
                             coordenadas.''')
        text3=TextMobject("Veamos el caso de $\\mathbb{R}^{2}$.").move_to(3*UP)
        text4=TextMobject('''Las coordenadas usuales en este espacio son \n
                                las polares ''','''y cartesianas.''').move_to(3*UP)
        text5=TextMobject('''Podemos definir una función que transforme un \n
                            vector de unas coordenadas a otras.''').move_to(3*UP)
        text6=TextMobject('''Tómate un segundo para pensar en la función \n
                                que transforme un vector en coordenadas polares \n
                                a cartesianas.''').move_to(2.5*UP) 


        linea1=Arrow([-4,0,0],[4,0,0])
        linea2=Arrow([0,-3,0],[0,3,0])
        lineas=VGroup(linea1,linea2).move_to(1*DOWN)
        linea1_1=Arrow([-4,0,0],[4,0,0])
        linea2_1=Arrow([0,-3,0],[0,3,0])
        Plano1=VGroup(linea1_1,linea2_1).scale(0.7)
        Plano1.move_to(1*DOWN+3*LEFT)
        linea1_2=Arrow([-4,0,0],[4,0,0])
        linea2_2=Arrow([0,-3,0],[0,3,0])
        Plano2=VGroup(linea1_2,linea2_2).move_to(1*DOWN-3*LEFT).scale(0.7)

        #Es posible moficar los siguientes parametros para mostrar un vector diferente
        a=1
        b=1.2
        #########
        ap=np.cos(a)/2
        bp=np.sin(b)/2
        vector1=Arrow([0,-1,0],[a,b,0],color=BLUE_E,buff=0)
        r=TextMobject("r").next_to(vector1,LEFT,buff=-0.3)
        angulo=Arc(fill_opacity=0,stroke_opacity=1, angle=np.arctan(b/a),radius=a/2,arc_center=[0,-1,0],buff=0)
        angulo_l=TextMobject("$\\theta$").next_to(angulo,UP+RIGHT,buff=0.2)
        angs=VGroup(angulo,angulo_l)

        #cartesianas
        brazox=Brace(vector1,RIGHT)
        x=TexMobject(r"x").next_to(brazox,RIGHT,buff=0.1)
        xs=VGroup(brazox,x)
        brazoy=Brace(vector1,UP)
        y=TexMobject(r"y").next_to(brazoy,UP,buff=0.1)
        ys=VGroup(y,brazoy)
        
        #Para la funcion
        vector1_1=Arrow([0,0,0],[a,b,0],color=BLUE_E,buff=0).scale(0.7).move_to((1-b*0.7/2)*DOWN+(3-a*0.7/2)*LEFT)
        r_1=TextMobject("r").next_to(vector1_1,LEFT,buff=-0.3)
        angulo_1=Arc(fill_opacity=0,stroke_opacity=1, angle=np.arctan(b/a),radius=a/2,arc_center=1*DOWN+3*LEFT).scale(0.7)
        angulo_l1=TextMobject("$\\theta$").next_to(angulo_1,0.2*UP+RIGHT,buff=0.2)
        Grupo1=VGroup(angulo_1,angulo_l1,vector1_1,r_1)

        #flabel
        f=TextMobject("$f$")
        farrow=Arrow([-0.5,0,0],[0.5,0,0],buff=0)
        f.next_to(farrow,UP,buff=0.3)

        #cartesianas        
        vector1_2=Arrow([0,0,0],[a,b,0],color=BLUE_E,buff=0).scale(0.7).move_to((1-b*0.7/2)*DOWN+(-3-a*0.7/2)*LEFT)
        brazox_1=Brace(vector1_2,RIGHT)
        x_1=TexMobject(r"x").next_to(brazox_1,RIGHT,buff=0.1)
        brazoy_1=Brace(vector1_2,UP)
        y_1=TexMobject(r"y").next_to(brazoy_1,UP,buff=0.1)
        Grupo2=VGroup(vector1_2,y_1,brazoy_1,x_1,brazox_1)

        D=Dot(color=RED).move_to(1*DOWN-3*LEFT)
        D2=Dot(color=RED).move_to(1*DOWN+3*LEFT)

        Grupo3=VGroup(Grupo1,Grupo2,Plano1,Plano2,f,farrow)





        self.play(Write(titulo))
        self.wait(3.5)
        self.play(FadeOut(titulo))
        self.play(Write(text1))
        self.wait(14)
        self.play(FadeOut(text1))
        self.play(Write(text2))
        self.wait(11)
        self.play(FadeOut(text2))
        self.wait()
        self.play(Write(text3))
        self.wait(4)
        self.play(Write(lineas))
        self.play(FadeOut(text3))
        self.play(Write(text4[0]))
        self.play(Write(vector1))
        self.play(Write(r),ShowCreation(angulo),Write(angulo_l))
        self.wait(5)
        self.play(Write(text4[1]))
        self.wait(3)
        self.play(ReplacementTransform(r,ys),ReplacementTransform(angs,xs))
        self.play(FadeOut(text4))
        self.play(Write(text5),FadeOut(lineas),FadeOut(ys),FadeOut(xs),FadeOut(vector1))
        self.play(ShowCreation(Plano1),ShowCreation(Plano2))
        self.play(ShowCreation(Grupo1))
        self.play(ShowCreation(f))
        self.play(ShowCreation(farrow))
        self.play(ShowCreation(Grupo2))
        self.wait(7)
        self.play(FadeOut(text5))
        self.play(Write(text6))
        self.wait(9)
        self.play(FadeOut(text6),FadeOut(Grupo3))
    def parte2 (self):
        #se puede modificar r y a
        r=2
        a=4
        #####
        theta=np.pi/a
        ## se puede modificar r1 y a1
        r1=1
        a1=1
        ####
        theta1=np.pi/a1



        text7=TextMobject('''Considera un vector en coordenadas polares ($\\vec{\\rho}=(r,\\theta)$),\n
                             por ejemplo $\\vec{\\rho}=($'''+str(r)+''',$\\pi/$'''+str(a)+''').''')
        text8=TextMobject("Veamos cómo se ve el vector en coordenadas cartesianas.").move_to(3*UP)
        text9=TextMobject("Notemos que $x=2\\cos(\\pi/4)$ y $y=2\\sin(\\pi/4)$.").move_to(3*UP)
        text10=TextMobject('''Entonces podemos definir la función que nos de el \n
                            cambio de coordenadas (de polares a cartesianas) como:
                             $$f:\\vec{\\rho}(r,\\theta)\\rightarrow\\vec{x}(x,y)$$  
                             $$f(\\vec{\\rho})=(r\\cos\\theta,r\\sin\\theta) $$''')
        text11=TextMobject('''Sin embargo, hay que tener cuidado con \n
                                el dominio de la función.''')
        text12=TextMobject('''Podemos entonces restringir el dominio \n
                         para que los ángulos queden unívocamente \n
                             determinados, $$\\theta \\in [0,2\\pi). $$''')
        text13=TextMobject('''Nota que si $0\\leq r$, entonces el vector cero \n
                            tiene muchas etiquetas en coordenadas polares, \n
                            a saber, $(0,\\theta)$.''').move_to(3*UP)
        text14=TextMobject('''De ahí que consideramos que el origen no tiene \n
                                    un ángulo asociado.''').move_to(3*UP)
        
        
        
        linea1=Arrow([-4,0,0],[4,0,0])
        linea2=Arrow([0,-3,0],[0,3,0])
        Plano=VGroup(linea1,linea2).move_to(1*DOWN)

        #Polares
        vector=Arrow([0,-1,0],[r*np.cos(theta),-1+(r*np.sin(theta)),0],buff=0,color=BLUE_C)
        radio=TexMobject(r"r="+str(r)).next_to(vector,LEFT,buff=-0.3)
        angulo=Arc(fill_opacity=0,stroke_opacity=1, angle=theta,radius=(r/2),arc_center=[0,-1,0],buff=0)
        angulo_l=TexMobject(r"\theta=\pi/"+str(a)).next_to(angulo,0*UP+RIGHT,buff=0.2)
        polares=VGroup(radio,angulo,angulo_l)
        #Cartesianas
        b_x=Brace(vector,RIGHT)
        x=TexMobject(r"x="+str(r)+r"\cos(\pi/"+str(a)+r")").next_to(b_x,RIGHT,buff=0.1)
        b_y=Brace(vector,UP)
        y=TexMobject(r"y="+str(r)+r"\sin(\pi/"+str(a)+r")").next_to(b_y,UP,buff=0.1)
        cartesianas=VGroup(y,x,b_y,b_x)
        
        vector_0=Dot(color=RED,radius=0.2).move_to(1*DOWN)

        vector1=Arrow([0,-1,0],[r*np.cos(theta),-1+(r*np.sin(theta)),0],buff=0,color=BLUE_C)

        


        self.play(Write(text7))
        self.wait(5)
        self.play(text7.shift,3*UP,runtime=6)
        self.play(ShowCreation(Plano))
        self.play(ShowCreation(vector))
        self.play(Write(polares))
        self.wait(6)
        self.play(FadeOut(text7),FadeOut(polares))
        self.play(Write(text8))
        self.play(Write(cartesianas))
        self.wait(8)
        self.play(FadeOut(text8))
        self.play(Write(text9))
        self.wait(10)
        self.play(FadeOut(Plano),FadeOut(text9),FadeOut(cartesianas),FadeOut(vector))
        self.play(Write(text10))
        self.wait(15)
        self.play(FadeOut(text10))
        self.play(Write(text11))
        self.wait(8)
        self.play(FadeOut(text11))
        self.play(Write(text12))
        self.wait(10)
        self.play(FadeOut(text12))
        self.play(Write(text13))
        self.play(ShowCreation(Plano))
        self.play(ShowCreation(vector_0))       
        self.wait(11)
        self.play(FadeOut(text13)) 
        self.play(Write(text14))
        self.wait(8)
        self.play(FadeOut(text14),FadeOut(Plano),FadeOut(vector_0))

    def parte3 (self):
        
        text15=TextMobject('''Si no restringimos el ángulo, tenemos por ejemplo \n
                            $(1,\\pi)$''','''$\\rightarrow(-1,0)$ ''','''\n 
                            $(1,3\\pi)$''','''$\\rightarrow(-1,0).$''').move_to(2.5*UP)
        #Ejes
        linea1_1=Arrow([-4,0,0],[4,0,0])
        linea2_1=Arrow([0,-3,0],[0,3,0])
        Plano1=VGroup(linea1_1,linea2_1).scale(0.7)
        Plano1.move_to(1*DOWN+3*LEFT)
        linea1_2=Arrow([-4,0,0],[4,0,0])
        linea2_2=Arrow([0,-3,0],[0,3,0])
        Plano2=VGroup(linea1_2,linea2_2).move_to(1*DOWN-3*LEFT).scale(0.7)
        

        #se pueden moficar los siguientes parámetros
        a=-1
        b=0
        r=1
        theta=np.pi
        ############


        #flabel
        f=TextMobject("$f$")
        farrow=Arrow([-0.5,0,0],[0.5,0,0],buff=0)
        f.next_to(farrow,UP,buff=0.3)
        fs=VGroup(f,farrow)

        #vectores 1
        vector1_1=Arrow([0,0,0],[a,b,0],color=RED,buff=0).scale(0.7).move_to((1-b*0.7/2)*DOWN+(3-a*0.7/2)*LEFT)
        r_1=TextMobject(r"r="+str(r)).next_to(vector1_1,LEFT+UP,buff=0.3)
        angulo_1=Arc(fill_opacity=0,stroke_opacity=1, angle=-theta,radius=a/2,arc_center=1*DOWN+3*LEFT).scale(0.7)
        angulo_l1=TexMobject(r"\theta=\pi").next_to(angulo_1,UP,buff=0.5)
        Grupo1=VGroup(angulo_1,angulo_l1,vector1_1,r_1)

        #en cartesianas #Cartesianas
        vector1_2=Arrow([0,0,0],[a,b,0],color=RED,buff=0).scale(0.7).move_to(((1-b*0.7/2))*DOWN+(3+a*0.7/2)*RIGHT)#(1-b*0.7/2)*DOWN+(3-a*0.7/2)*RIGHT)
        b_x=Brace(vector1_2,RIGHT)
        x=TexMobject(r"x="+str(r)+r"\cos(\pi)").next_to(b_x,RIGHT+DOWN,buff=0.1)
        b_y=Brace(vector1_2,UP)
        y=TexMobject(r"y="+str(r)+r"\sin(\pi)").next_to(b_y,UP,buff=0.1)
        cartesianas=VGroup(y,x,b_y,b_x)
        
        #segundo ejemplo
        r_3=TextMobject(r"r="+str(r)).next_to(vector1_1,LEFT+UP,buff=0.3)
        angulo_3=Arc(fill_opacity=0,stroke_opacity=1, angle=-theta-2*np.pi,radius=a/2,arc_center=1*DOWN+3*LEFT).scale(0.7)
        angulo_l3=TexMobject(r"\theta=3\pi").next_to(angulo_1,UP,buff=0.5)
        Grupo2=VGroup(angulo_3,angulo_l3,vector1_1,r_3)

        #en cartesianas #Cartesianas
        x2=TexMobject(r"x="+str(r)+r"\cos(3\pi)").next_to(b_x,RIGHT+DOWN,buff=0.1)
        y2=TexMobject(r"y="+str(r)+r"\sin(3\pi)").next_to(b_y,UP,buff=0.1)
        cartesianas1=VGroup(y2,x2,b_y,b_x,vector1_2)

        self.play(ShowCreation(Plano1),ShowCreation(Plano2))
        self.play(Write(text15[0]))
        self.play(ShowCreation(Grupo1))
        self.play(Write(text15[1]))
        self.play(ShowCreation(fs))
        self.play(ShowCreation(vector1_2))
        self.play(ShowCreation(cartesianas))
        self.play(FadeOut(cartesianas),FadeOut(fs),FadeOut(Grupo1))
        self.wait(7)
        self.play(Write(text15[2]))
        self.play(ShowCreation(Grupo2))
        self.play(ShowCreation(text15[3]))
        self.play(ShowCreation(fs))
        self.play(ShowCreation(cartesianas1))
        self.wait()
        self.wait(7)
        self.play(FadeOut(cartesianas1),FadeOut(Grupo2),FadeOut(fs),
                FadeOut(Plano1),FadeOut(Plano2),FadeOut(text15))    

    def parte4 (self):
        #se pueden modificar los siguientes parámetros para usar como ejemplo otro vector
        x=2
        y=1
        ##########3

        text16=TextMobject('''Para el cambio de coordenadas de cartesianas a \n
                                polares, considera $\\vec{x}=($'''+str(x)+''','''+str(y)+''')''')
        text17=TextMobject('''Puedes notar que \n  
                            $r=\\sqrt{2^2+1^2} \ \ \ y \ \ \ \\theta=\\tan^{-1}\\left(\\frac{1}{2}\\right).$''').move_to(3*UP)
        text18=TextMobject('''Por lo que podríamos pensar que la función \n
                                de cambio de coordenadas es 
                                $$g(\\vec{x})=\\left(\\sqrt{x^2+y^2},\\tan^{-1}\\left(\\frac{y}{x}\\right)\\right)$$''','''\n
                                Y casi...''')
        text19=TextMobject('''Debemos hacer un pequeño ajuste en la función \n
                                 previamente definida.''').move_to(3*UP)#,'''\n
        text19_1=TextMobject('''Ya que nuestra función no considera muchos \n
                                vectores, entre ellos $(0,0)$ y $(r,\\pi/2)$.''').move_to(2.5*UP)
        text20=TextMobject('''Si tomamos  $h(x)=(\\sqrt{x^2+y^2},\\theta)$ \n
                                            Donde''').move_to(3*UP)
        #Objetos para definir el texto de theta
        text21_m=TexMobject(r'''{\begin{matrix} 
                                \tan^{-1}\left(\frac{y}{x}\right) & si & x>0 \ \ \text{y} \ \ y \geq0\\
                                                                &        &  \\
                                \frac{\pi}{2} & \text{si} & x=0  \ \ \text{y} \ \ y >0\\
                                &        &  \\
                                \tan^{-1}\left(\frac{y}{x}\right)+\pi & \text{si} & x<0 \\
                                &        &  \\
                                \frac{3\pi}{2} & \text{si} & x=0 \ \ \text{y} \ \ y <0\\
                                &        &  \\
                                \tan^{-1}\left(\frac{y}{x}\right)+2\pi & \text{si} & x>0 \ \  \text{y} \ \ y<0 \end{matrix}}''').move_to(0.5*RIGHT+0.8*DOWN)
        text21_b=Brace(text21_m,LEFT)#.next_to(text20,LEFT,buff=0.5)
        text21_t=TexMobject(r"\theta=").next_to(text21_b,LEFT,buff=0.1)    
        text21=VGroup(text21_m,text21_b,text21_t)       

        text22=TextMobject('''Así podemos pasar de coordenadas polares a cartesianas,\n
                                 sin ningún problema. ''')
        text23=TextMobject('''¡Ya conocemos las funciones que nos permiten \n
                            pasar de coordenadas cartesianas a polares y viceversa.!''')

        
        #Un solo eje
        linea1=Arrow([-4,0,0],[4,0,0])
        linea2=Arrow([0,-3,0],[0,3,0])
        Plano=VGroup(linea1,linea2).move_to(1*DOWN)
        vector=Arrow([0,-1,0],[x,-1+y,0],buff=0,color=BLUE_C)

        #labels catersianas
        x_b=Brace(vector,RIGHT)
        x_l=TexMobject(r"x="+str(x)).next_to(x_b,RIGHT,buff=0.1)
        y_b=Brace(vector,UP)
        y_l=TexMobject(r"y="+str(y)).next_to(y_b,UP,buff=0.1)
        cartesianas=VGroup(y_b,x_b,y_l,x_l)     
        xs=VGroup(x_b,x_l)
        ys=VGroup(y_b,y_l)

        #labels en polares
        r=(x**2+y**2)**(1/2)
        r_1=DecimalNumber(r, num_decimal_places=1).move_to(vector.get_center()+(x/4)*LEFT+0.1*UP)#next_to(vector,LEFT,buff=0.2)#move_to((x/80)*LEFT+(y/28)*UP)
        radio=TexMobject(r"r=").next_to(r_1,LEFT,buff=0.5)          
        rs=VGroup(r_1,radio)

        if x>0 and y!=0:
            theta=np.arctan(y/x)
        if x==0 and y>0:
            theta=np.pi/2
        if x<0:
            theta=np.arctan(y/x)+np.pi
        if x==0 and y<0:
            theta=np.arctan(y/x)+2*np.pi
        
        angulo=Arc(fill_opacity=0,stroke_opacity=1, angle=theta,radius=(r/2),arc_center=[0,-1,0],buff=0)
        ###
        angulo_l=TexMobject(r"\theta=").move_to(angulo.get_center()+(x/4+0.1)*RIGHT)#next_to(angulo,RIGHT+0*UP,buff=0.3)#next_to(angulo,(r/30*np.sin(theta/2))*UP+RIGHT,buff=0.3)
        theta_1=DecimalNumber(theta, num_decimal_places=1).next_to(angulo_l,(x/((x**2)**(1/2)))*RIGHT,buff=0.1)
        thetas=VGroup(theta_1,angulo_l,angulo)
        polares=VGroup(radio,r_1,angulo,angulo_l,theta_1)
        

        y2=ValueTracker(0.8)
        vector_1=Arrow([0,-1,0],[0,-1,0],color=BLUE_C,buff=0)      #  t1_2f=0.3  
        def mov_vector (obj):
            y = y2.get_value()
            vector_1.become(Arrow([0,-1,0],[0,y-1,0],color=BLUE_C,buff=0))

        vector_1.add_updater(mov_vector)


        vector_0=Dot(color=RED,radius=0.2).move_to(1*DOWN)
            

        self.play(Write(text16))
        self.wait()
        self.play(text16.shift,3*UP,runtime=6)
        self.play(ShowCreation(Plano))
        self.play(ShowCreation(vector),ShowCreation(cartesianas))
        self.wait(8)
        self.play(FadeOut(text16))
        self.play(Write(text17))
        self.play(ReplacementTransform(xs,rs),ReplacementTransform(ys,thetas))
        self.wait(8)
        self.play(FadeOut(vector),FadeOut(Plano),FadeOut(cartesianas),FadeOut(polares),
                    FadeOut(text17))
        self.play(Write(text18[0]))
        self.wait(10)
        self.play(Write(text18[1]))
        self.wait(5)
        self.play(FadeOut(text18))
        self.play(ShowCreation(Plano))
        self.play(ShowCreation(text19))
        self.wait(8)
        self.play(FadeOut(text19))
        self.play(Write(text19_1))
        self.play(ShowCreation(vector_0))
        self.play(ReplacementTransform(vector_0,vector_1))
        self.play(y2.set_value, 2,run_time=10)
        self.wait(5)
        self.play(FadeOut(text19_1))
        self.play(FadeOut(Plano),FadeOut(vector_1))
        self.play(Write(text20))
        self.play(Write(text21))
        self.wait(20)
        self.play(FadeOut(text21),FadeOut(text20))
        self.play(Write(text22))
        self.wait(8)
        self.play(FadeOut(text22))
        self.play(Write(text23))
        self.wait(9)
        self.play(FadeOut(text23))

    def construct(self):
        self.parte1()
        self.parte2()
        self.parte3()
        self.parte4()

