from manimlib.imports import *

########################################
###### Curvas suaves y cruces ##########
########################################

#En esta animación sólo se pueden modificar los intervalos en los que se evaluan las parametrizaciones
#Sin embargo se puede aconsejar que se analice el código para crear sus propias animaciones sobre derivadas 
#O para visualizar como se dibujan las curvas dependiendo de la parametrización

###PARA ESTA CLASE ES NECESARIO APLICAR UNA CORRECCIÓN A LOS VECTORES 3D, TAL COMO SE SIGUE A CONTINUACIÓN ###
### En el archivo geometry.py (manimlib/mobject/geometry.py) de la biblioteca de manim pegar el siguiente código debajo de ###
### la definición de tip.rotate() dentro del método position_tip(): ###
###    angle = angle_of_vector(handle - anchor) + PI/2   ###
###    a = np.array((np.cos(angle),np.sin(angle),0))     ###
###    tip.rotate(-phi_of_vector(handle - anchor),a)     ###
### Además, en el archvio space_ops.py (manimlib/utils/space_ops.py) añadir el siguiente método: ###
### def phi_of_vector(vector):                           ###
###    xy = complex(*vector[:2])                         ###
###    if xy == 0:                                       ###
###        return 0                                      ###
###    a = ((vector[:1])**2 + (vector[1:2])**2)**(1/2)   ###
###    vector[0] = a                                     ###
###    vector[1] = vector[2]                             ###
###    return np.angle(complex(*vector[:2]))             ###
############################################################
 
def gota(t):
    return [t**3 - 4*t,t**2 - 4,0]
def lemniscata(t):
    return  [(2)*np.cos(t),2*np.sin(2*t),0]
def abs(t):
    return  [t,np.abs(t),0]
def cicloide(t):
    return  [(t-np.sin(t)),(1-np.cos(t)),0]
def curva1(x):
        return  [x,2*x**2*np.sin(1/x)+x,0]
def curva2(t):
        return [t**3,np.exp(t),np.cos(10*t)]

class Curvas_suaves_y_cruces_1 (MovingCameraScene,Scene):
    
    def setup (self):
        Scene.setup(self)
        MovingCameraScene.setup(self)

    def animacion1 (self):
        titulo=TextMobject('''Curvas Suaves y \n
                                Cruces''').scale(1.5)
        text=TextMobject('''  Si $\\gamma$ tiene ''','''tangente''',''' en $t_0\\in (a,b)$,''',''' \n
                             ¿existe alguna vecindad de $t_0$ donde la curva \n
                             tiene ''','''tangente''',''' en cada punto de la vecindad? ''')
        text.set_color_by_tex_to_color_map({"tangente": ORANGE})
        text1=TextMobject('''No''',''', ni siquiera podemos asegurar que $\\gamma$ \n
                            sea ''','''continua''',''' fuera de $t_0$''')
        text1.set_color_by_tex_to_color_map({"continua": RED})
        text2=TextMobject('''Si pedimos que $\\gamma$ sea ''','''derivable''',''' en $(a,b)$\\\\ y tenga ''','''tangente''',''' en $t_0$''',''' \\\\
                                ¿podemos encontrar alguna vecindad de $t_0$\\\\ donde la curva sea ''','''regular''','''? ''','''\n
                                 ¡No! ''')
        text2.set_color_by_tex_to_color_map({"tangente": ORANGE, "regular": MAROON, "derivable": TEAL})
        text3=TextMobject(''' Este problema es similar al siguiente: ''',''' \n
                            Si una función de $\\mathbb{R}$ en $\\mathbb{R}$ es ''','''derivable''',''' en $(a,b)$,''','''\n
                             aunque $f'(x_0)\\neq 0$,''',''' no podemos asegurar que \n
                             en alguna vecindad de $x_0$''','''\n
                              la función sea ''','''monótona.''' )  
        text3.set_color_by_tex_to_color_map({"derivable": TEAL,"monótona": GREEN_D})
        text4=TextMobject('''Checa la función ''','''$f(x)$''','''$=2x^{2}sen(1/x)+x$ para $x\\neq 0$''').move_to(3*UP)
        text4[1].set_color(BLUE)
        text5=TextMobject('''Usando este ejemplo, \n da una parametrización
                                $\\gamma$ ''','''derivable ''','''\n
                                con ''','''tangente''',''' en $t_0\\in (a,b)$ y que no sea ''','''regular''',''' \n
                                en ninguna vecindad de $t_0$.''')
        text5.set_color_by_tex_to_color_map({"derivable": TEAL,"tangente": ORANGE,"regular": MAROON })
        text6=TextMobject('''Para evitar comportamientos extraños como estos,''',''' \n 
                            consideramos funciones regulares con derivada continua,''',''' \n
                                les llamaremos ''','''curvas suaves''','''. ''')
        text6[-2].set_color(PURPLE_B)
        text7=TextMobject('''Intuitivamente las ''','''curvas suaves''',''' \n se parecen más 
                                        a sus ''','''tangentes''',''' \n
                                 que aquellas que son solamente ''','''derivables''','''. ''')
        text7.set_color_by_tex_to_color_map({"tangente": ORANGE,"curvas suaves": PURPLE_B,"derivable": TEAL })
        #Los siguientes valores se pueden cambiar para cambiar el rango de evaluación de las funciones
        tmin1=-0.5
        tmax1=-0.0001
        tmin2=0.0001       
        tmax2=0.5
        ref=Dot(color=YELLOW,radius=0.003)
        ref1=Dot(color=YELLOW,radius=0.0003)

        f1 = ParametricFunction(curva1,t_min=tmin1,t_max=tmax1,color=BLUE_C,step_size=0.0001)
        f1_1 = ParametricFunction(curva1,t_min=tmin1,t_max=tmax1,color=BLUE_C, stroke_width=0.5)
        text4_1=TextMobject('''y $f(0)=0$ ''').scale(0.05).next_to(ref,UP,buff=0.12)  
        text4_1.bg = SurroundingRectangle(text4_1,color=WHITE,fill_color=BLACK,fill_opacity=1,buff=0.01)
        text4_1.group = VGroup(text4_1.bg,text4_1)
        text4_2=TextMobject('''La función tiene infinidad \n
                               de oscilaciones alrededor del $0$''').scale(0.05).next_to(text4_1,DOWN,buff=0.22)
        text4_2.bg = SurroundingRectangle(text4_2,color=WHITE,fill_color=BLACK,fill_opacity=1,buff=0.01)
        text4_2.group = VGroup(text4_2.bg,text4_2)
        
        f2 = ParametricFunction(curva1,t_min=tmin2,t_max=tmax2,color=BLUE_C)
        self.camera_frame.save_state()
        self.play(Write(titulo))
        self.wait(3.5)
        self.play(FadeOut(titulo))
        self.play(Write(VGroup(text[0],text[1],text[2])))
        self.play(Write(VGroup(text[3],text[4],text[5])))
        self.wait(7.6)
        self.play(FadeOut(text))
        self.play(Write(text1[0]))
        self.wait()
        self.play(Write(VGroup(text1[1],text1[2],text1[3])))
        self.wait(7)
        self.play(FadeOut(text1))
        self.play(Write(VGroup(text2[0],text2[1],text2[2],text2[3],text2[4])))
        self.play(Write(VGroup(text2[5],text2[6],text2[7])))
        self.wait(11)
        self.play(Write(text2[-1]))
        self.wait(3)
        self.play(FadeOut(text2))
        self.play(Write(text3[0]))
        self.play(Write(VGroup(text3[1],text3[2],text3[3])))
        self.play(Write(text3[4]))
        self.play(Write(text3[5]))
        self.play(Write(VGroup(text3[6],text3[7])))
        self.wait(17)
        self.play(FadeOut(text3))
        self.play(ShowCreation(f1))
        self.play(ShowCreation(f2))
        self.wait(4)
        self.play(Write(text4))
        self.wait(8)
        self.play(FadeOut(text4))        
        #Movimiento de camara
        self.play(
        # Nuevo ancho
            self.camera_frame.set_width,f1.get_width()*1.2,
            # Nueva posición
            self.camera_frame.move_to,ref)
        self.play(Write(text4_1.group))
        self.wait()
        self.play(Write(text4_2.group))
        self.play(ShowCreation(ref))
        #self.play(ReplacementTransform(f1,f1_1))
        self.play(ReplacementTransform(ref,ref1))
        self.play(
            self.camera_frame.set_width,f1.get_width()*0.1,
            self.camera_frame.move_to,ref,run_time=4)
        self.wait()
        self.play(FadeOut(ref),FadeOut(f1),FadeOut(f2),FadeOut(text4),FadeOut(text4_1.group),FadeOut(text4_2.group))
        self.play(Restore(self.camera_frame))        
        self.play(Write(text5))
        self.wait(10)
        self.play(FadeOut(text5))
        self.play(Write(text6))
        self.wait(8)
        self.play(FadeOut(text6))  
        self.play(Write(text7))
        self.wait(10)
        self.play(FadeOut(text7))


    def construct (self):                   
        self.animacion1()
   

class Curvas_suaves_y_cruces_2 (ThreeDScene):
    def construct (self):
        
        text8=TextMobject('''Tomemos la siguiente ''','''curva''',''' parametrizada por \n ''','''\n 
                                $g(t)$''','''$=(t^{3},e^{t},\\cos(10t))$ ''')
        #text8[1].set_color(BLUE)
        text8[3].set_color(RED)
        text9=TextMobject('''La ''','''derivada''',''' de la parametrización es:\n''','''
                                  $g(t)$''','''$=(3t^{2},e^{t},-10sen(10t))$''').to_edge(UP)
        text9[1].set_color(ORANGE)
        text9[3].set_color(RED)
        text9.bg = SurroundingRectangle(text9,color=WHITE,fill_color=BLACK,fill_opacity=1)
        text9.group = VGroup(text9.bg,text9)
        text10=TextMobject(''' Veamos como cambia su ''','''derivada''',''', \n
                                    en función del tiempo.''').to_edge(UP)
        text10[1].set_color(ORANGE)
        text10.bg = SurroundingRectangle(text10,color=WHITE,fill_color=BLACK,fill_opacity=1)
        text10.group = VGroup(text10.bg,text10)
        text11=TextMobject(''' Su ''','''derivada''',''' nunca se hace $\\Vec{0}$''')
        text11[1].set_color(ORANGE)
        text12=TextMobject('''La curva anterior es una ''','''curva suave''','''. ''')
        text12[1].set_color(PURPLE_B)
        text13=TextMobject('''¿Será que las ''','''curvas suaves''',''' sólo deben cumplir que \n
                                     su ''','''derivada''',''' nunca sea $\Vec{0}$? ''')
        text13[1].set_color(PURPLE_B)
        text13[3].set_color(ORANGE)
        text14=TextMobject(''' Veamos otro ejemplo. ''')


        axes=ThreeDAxes()
        #Se puede cambiar para mofidificar el intervalo de evación de la función

        tmin = -1.5
        tmax = 1.5
 
        f1 = ParametricFunction(curva2,t_min=tmin,t_max=tmax,color=RED)
        t1=ValueTracker(tmin)
        ti=tmin
        n=((3*ti**2)**2+np.exp(ti)**2+(10*np.sin(10*ti))**2)**(1/2)
        deriv=Arrow( (ti**3,np.exp(ti),np.cos(10*ti)), (ti**3+((3*ti**2))/n ,np.exp(ti)+(np.exp(ti))/n ,np.cos(10*ti)-(10*np.sin(10*ti))/n),buff=0).set_color(BLUE_D)
        #derivArrowTip = ArrowTip(start_angle=deriv.get_angle()).next_to(deriv.get_end(),buff=0).set_color(BLUE_D)

        def moving_dot():
            t = t1.get_value()
            x=[t**3,np.exp(t),np.cos(10*t)]
            p = Sphere(radius=0.1,color=RED).move_to(x)
            return p
        dd = always_redraw(moving_dot)     
        def derivada (obj):
            t = t1.get_value()
            deriv.become(Arrow( (t**3,np.exp(t),np.cos(10*t)), (t**3+((3*t**2))*(1/((3*t**2)**2+np.exp(t)**2+(10*np.sin(10*t))**2)**(1/2)) ,np.exp(t)+(np.exp(t))*(1/((3*t**2)**2+np.exp(t)**2+(10*np.sin(10*t))**2)**(1/2)) ,np.cos(10*t)-(10*np.sin(10*t))*(1/((3*t**2)**2+np.exp(t)**2+(10*np.sin(10*t))**2)**(1/2))),buff=0)).set_color(BLUE_D)
            #derivArrowTip.become(ArrowTip(start_angle=deriv.get_angle())).next_to(deriv.get_end(),buff=0).set_color(BLUE_D)

        deriv.add_updater(derivada)

        self.play(Write(text8))
        self.wait(5)
        self.play(FadeOut(text8))
        self.set_camera_orientation(0.8*np.pi/2, -0.25*np.pi,distance=30)
        self.play(ShowCreation(axes))
        self.play(ShowCreation(f1))        
        self.begin_ambient_camera_rotation(rate=0.07)
        self.add_fixed_in_frame_mobjects(text9.group)
        self.play(Write(text9.group))
        self.wait(6)
        self.play(FadeOut(text9.group))
        self.add_fixed_in_frame_mobjects(text10.group)
        self.play(Write(text10.group))
        self.wait(6.7)
        self.play(FadeOut(text10.group))
        #Animación de la derivada normalizada
        self.play(ShowCreation(dd),ShowCreation(deriv))#,ShowCreation(derivArrowTip))
        self.play(t1.set_value, tmax,run_time=30,rate_func=linear)
        self.wait()
        self.stop_ambient_camera_rotation()
        self.play(FadeOut(axes),FadeOut(f1),FadeOut(dd),FadeOut(deriv))#,FadeOut(derivArrowTip))
        ##
        self.add_fixed_in_frame_mobjects(text11)
        self.play(Write(text11))
        self.wait(4)
        self.play(FadeOut(text11))
        self.add_fixed_in_frame_mobjects(text12)
        self.play(Write(text12))
        self.wait(5)
        self.play(FadeOut(text12))
        self.add_fixed_in_frame_mobjects(text13)
        self.play(Write(text13))
        self.wait(8)
        self.play(FadeOut(text13))
        self.add_fixed_in_frame_mobjects(text14)
        self.play(Write(text14))
        self.wait(3)
        self.play(FadeOut(text14))
    

class Curvas_suaves_y_cruces_3 (MovingCameraScene,Scene):
    def setup (self):
        Scene.setup(self)
        MovingCameraScene.setup(self)
    
    def construct(self):

        text15=TextMobject('''Tomemos la siguiente curva.''').move_to(3*UP)
        text15.bg = SurroundingRectangle(text15,color=WHITE,fill_color=BLACK,fill_opacity=1)
        text15.group = VGroup(text15.bg,text15)
        text15_1 = TextMobject('''$f(t)$''','''$=(t,|t|)$''').to_edge(DOWN)
        text15_1[0].set_color(BLUE)
        text15_1.bg = SurroundingRectangle(text15_1,color=WHITE,fill_color=BLACK,fill_opacity=1)
        text15_1.group = VGroup(text15_1.bg,text15_1)
        text15_2 = TextMobject('''La curva tiene un ''','''"pico"''',''' en el origen, no hay ''','''tangente''','''.''').move_to(3*UP)
        text15_2.set_color_by_tex_to_color_map({"pico":GREEN_D,"tangente":ORANGE})
        text15_2.bg = SurroundingRectangle(text15_2,color=WHITE,fill_color=BLACK,fill_opacity=1)
        text15_2.group = VGroup(text15_2.bg,text15_2)
        text16=TextMobject('''Veamos como cambia su ''','''tangente''',''' conforme cambia t.''').move_to(3*UP)
        text16[1].set_color(ORANGE)
        text16.bg = SurroundingRectangle(text16,color=WHITE,fill_color=BLACK,fill_opacity=1)
        text16.group = VGroup(text16.bg,text16)
        text17=TextMobject(''' Tomemos la siguiente curva''')
        text17.bg = SurroundingRectangle(text17,color=WHITE,fill_color=BLACK,fill_opacity=1)
        text17.group = VGroup(text17.bg,text17)
        text18=TextMobject('''¿Existe alguna parametrización ''','''suave''',''' de la curva? ''').move_to(3*UP)
        text18[1].set_color(PURPLE_B)
        text18.bg = SurroundingRectangle(text18,color=WHITE,fill_color=BLACK,fill_opacity=1)
        text18.group = VGroup(text18.bg,text18)
        text18_1 = TextMobject('''No, toda parametrización derivable tendrá \n
                                ''','''derivada''',''' (0,0) en el ''','''"pico"''',''', \n 
                                  entonces la curva no es ''','''regular''',''' ni ''','''suave''','''.''').move_to(3*UP)
        text18_1.set_color_by_tex_to_color_map({"derivada":TEAL, "regular":MAROON,"pico":GREEN_D,"suave":PURPLE_B})
        text18_1.bg = SurroundingRectangle(text18_1,color=WHITE,fill_color=BLACK,fill_opacity=1)
        text18_1.group = VGroup(text18_1.bg,text18_1)
        text18_2=TextMobject('''Revisa el video ''' ,'''\emph{Curvas regulares y picos}''',''' para más detalles. ''').move_to(3*UP)
        text18_2[1].set_color(BLUE)
        text18_2.bg=SurroundingRectangle(text18_2,color=WHITE,fill_color=BLACK,fill_opacity=1)
        text18_2.group=VGroup(text18_2.bg,text18_2)
        text19=TextMobject('''Tomemos la siguiente parametrización''',
                                    '''$$f:\\left[-2,2\\right]\\rightarrow\\mathbb{R}^{2}$$''','''\n
                                             $f(t)$''','''$=(t^3 -4t, t^2 -4)$''').move_to(2*UP)
        text19[-2].set_color(RED)
        text19_0bg = SurroundingRectangle(text19[0],color=WHITE,fill_color=BLACK,fill_opacity=1)
        text19_0group = VGroup(text19_0bg,text19[0])
        text19_1bg = SurroundingRectangle(text19[1],color=WHITE,fill_color=BLACK,fill_opacity=1)
        text19_1group = VGroup(text19_1bg,text19[1])
        text19_2bg = SurroundingRectangle(VGroup(text19[2],text19[3]),color=WHITE,fill_color=BLACK,fill_opacity=1)
        text19_2group = VGroup(text19_2bg,VGroup(text19[2],text19[3]))
        text19.group = VGroup(text19_0group,text19_1group,text19_2group)
        text20=TextMobject('''Veamos como recorre un punto a la curva en el intervalo \n
                                     de la parametrización. ''').move_to(3*UP)
        text20.bg = SurroundingRectangle(text20,color=WHITE,fill_color=BLACK,fill_opacity=1)
        text20.group = VGroup(text20.bg,text20)
        text21=TextMobject('''Y ahora como se mueve su vector ''','''tangente''',''' a lo largo \n
                                 de esta curva a partir de la parametrización dada. ''').move_to(3*UP)
        text21[1].set_color(ORANGE)
        text21.bg = SurroundingRectangle(text21,color=WHITE,fill_color=BLACK,fill_opacity=1)
        text21.group = VGroup(text21.bg,text21)
        text22=TextMobject('''Nota que tenemos una parametrización ''','''simple ''','''cerrada''',''', \n
                                pero en el punto donde la curva se cierra''','''\n
                             (donde pierde la inyectividad) tenemos dos ''','''tangentes''',''',''','''\n
                             por lo que se trata de una ''','''curva regular''',''', como la ''','''derivada''',''' \n
                              es ''','''continua''',''', además es ''','''suave''','''.  ''')
        text22.set_color_by_tex_to_color_map({"tangentes": ORANGE, "continua": BLUE, "derivada":TEAL, "simple":YELLOW, "curva regular":MAROON,"cerrada":PINK,"suave":PURPLE_B})
        text23=TextMobject('''En cambio la curva en forma de "V" al no ser \n
                                ''','''regular''',''', no puede ser ''','''suave''','''. ''')
        text23.set_color_by_tex_to_color_map({"suave":PURPLE_B,"regular":MAROON})
        text24=TextMobject('''Aunque $f$ parece tener un ''','''"pico"''',''', en realidad es un ''','''cruce''',''', \n
                                o sea, la curva se cruza sobre sí misma, perdiendo la \n 
                                inyectividad.''','''\n
                                 Como la curva admite una parametrización ''','''suave''',''', \n
                                 decimos que la curva es ''','''suave''','''. ''')
        text24.set_color_by_tex_to_color_map({"pico":GREEN, "suave":PURPLE_B, "cruce":BLUE})
        text25=TextMobject(''' Considera cualquier parametrización ''','''suave''',''' de la curva \n
                                        definida en $[a,b]$,''','''\n
                                 ¿qué punto es $f(a)$ y cuál es $f(b)$? ''')
        text25.set_color_by_tex_to_color_map({"suave":PURPLE_B})
        text26=TextMobject('''Para ahondar en el asunto, consideremos otro \n
                                    ejemplo interesante''')
        text26_1=TextMobject(''' Podemos parametrizarla con 
                                    $$f:[0,2\pi]$$ ''').move_to(3*UP)
        text26_1.bg = SurroundingRectangle(text26_1,color=WHITE,fill_color=BLACK,fill_opacity=1)
        text26_1.group = VGroup(text26_1.bg,text26_1)
        text26_2=TextMobject(''' $f(t)$''','''$=2(cos(t),sen(2t))$ ''').move_to(3*UP)
        text26_2[0].set_color(GREEN_D)
        text26_2.bg = SurroundingRectangle(text26_2,color=WHITE,fill_color=BLACK,fill_opacity=1)
        text26_2.group = VGroup(text26_2.bg,text26_2)
        text27=TextMobject('''Podemos ver que la curva tiene un ''','''cruce''','''. ¿Es ''','''suave''','''?''').move_to(3*UP)
        text27.set_color_by_tex_to_color_map({"suave":PURPLE_B,"cruce":BLUE})
        text27.bg = SurroundingRectangle(text27,color=WHITE,fill_color=BLACK,fill_opacity=1)
        text27.group = VGroup(text27.bg,text27)
        text28=TextMobject('''Veamos cómo cambia su ''','''derivada''',''' conforme cambia t. ''').move_to(3*UP)
        text28.set_color_by_tex_to_color_map({"derivada":TEAL})
        text28.bg = SurroundingRectangle(text28,color=WHITE,fill_color=BLACK,fill_opacity=1)
        text28.group = VGroup(text28.bg,text28)
        text29=TextMobject('''Nunca se anuló y en el ''','''cruce''',''' nuevamente tenemos \n
                                dos ''','''tangentes''','''. ''').move_to(3*UP)
        text29.set_color_by_tex_to_color_map({"tangentes":ORANGE,"cruce":BLUE})
        text29.bg = SurroundingRectangle(text29,color=WHITE,fill_color=BLACK,fill_opacity=1)
        text29.group = VGroup(text29.bg,text29)
        text30=TextMobject('''La curva anterior es una ''','''curva suave''',''' y \n
                            se conoce como Lemniscata. ''')
        text30[1].set_color(PURPLE_B)
        text31=TextMobject('''¿Puedes dar alguna parametrización de esta curva\n
                                 que no sea ''','''suave''','''? ''')
        text31[1].set_color(PURPLE_B)
        text32=TextMobject('''¿Puedes dar una parametrización ''','''suave''',''' y ''','''simple''',''' de la curva? ''')
        text32[1].set_color(PURPLE_B)
        text32[3].set_color(YELLOW)
        text33=TextMobject('''La siguiente curva se llama cicloide, ¿es ''','''suave''','''? ''').move_to(3*DOWN)
        text33[1].set_color(PURPLE_B)
        text34=TextMobject(''' Modifica el código de esta animación para\n
                                     generar más ejemplos. ''')

        axes=Axes()
        #Se puede cambiar para mofidificar el intervalo de evación de la función
        xmin=-4
        xmax=4
        ##
        fabs = ParametricFunction(abs,t_min=-4,t_max=4,color=BLUE_C)
        tmin = -2
        tmax = 2
        tmin1 = 0
        tmax1 = 2*np.pi
        fgota = ParametricFunction(gota,t_min=tmin,t_max=tmax,color=RED)
        flemniscata = ParametricFunction(lemniscata,t_min=tmin1,t_max=tmax1,color=GREEN)
        fcicliode = ParametricFunction(cicloide,t_min=-2*np.pi-1,t_max=2*np.pi+1,color=GREEN)

        #Tangente del valor absoluto
        t1=ValueTracker(xmin)
        punto_abs1=Dot(color=RED,fill_opacity=1,fill_color=RED).move_to([tmin,np.abs(tmin),0])
        tan1=Line([0,0,0],[1,tmin/np.abs(tmin),0],color=RED,opacity=1).move_to(punto_abs1)#.get_center()+0.2*DOWN+0.2*RIGHT)

        def tan_abs(obj):
            t = t1.get_value()
            x=[t,np.abs(t),0]
            n=2**(1/2)/2
            punto_abs1.become(Dot(color=RED,fill_opacity=1,fill_color=RED).move_to(x))
            tan1.become(Line([0,0,0],[1,t/np.abs(t),0],color=RED,opacity=1).move_to(punto_abs1))#.get_center()+0.2*DOWN+0.2*RIGHT)
        tan_absf=VGroup(punto_abs1,tan1)
        tan_absf.add_updater(tan_abs)


        t1_1=ValueTracker(0.0001)
        punto_abs2=Dot(color=RED,fill_opacity=1,fill_color=RED).move_to([tmin,np.abs(tmin),0])
        tan2=Line([0,0,0],[1,tmin/np.abs(tmin),0],color=RED,opacity=1).move_to(punto_abs1)#.get_center()+0.2*DOWN+0.2*RIGHT)

        def tan_abs2(obj):
            t = t1_1.get_value()
            x=[t,np.abs(t),0]
            n=2**(1/2)/2
            punto_abs2.become(Dot(color=RED,fill_opacity=1,fill_color=RED).move_to(x))
            tan2.become(Line([0,0,0],[1,t/np.abs(t),0],color=RED,opacity=1).move_to(punto_abs2))#.get_center()+0.2*DOWN+0.2*RIGHT)
        tan_absf_1=VGroup(punto_abs2,tan2)
        tan_absf_1.add_updater(tan_abs2)
    
      
        #Movimiento para la gota
        s1_1=ValueTracker(tmin)
        si=tmin
        punto_gota = Dot(color=YELLOW,fill_opacity=1).move_to([si**3 - 4*si,si**2 - 4,0])
        punto_gota 
        def Dgota(obj):
            s = s1_1.get_value()
            x = np.array([s**3 - 4*s,s**2 - 4,0])
            punto_gota.become(Dot(color=YELLOW,fill_opacity=1).move_to(x))
        #para mover el punto
        punto_gota.add_updater(Dgota)

        #Para generar el movimiento de la derivada
        s1_2=ValueTracker(tmin)
        derivada_gota=Arrow((si**3 - 4*si,si**2 - 4,0),(si**3 - 4*si + 3*(si**2) - 4*si,si**2 - 4 +2*si,0),buff=0).set_color(YELLOW)
        punto_gota1 = Dot(color=YELLOW,fill_opacity=1).move_to([si**3 - 4*si,si**2 - 4,0])
        def Dgota(obj):
            s = s1_2.get_value()
            x=np.array([s**3 - 4*s,s**2 - 4,0])
            punto_gota1.become(Dot(color=YELLOW,fill_opacity=1).move_to(x))
            derivada_gota.become(Arrow((s**3 - 4*s,s**2 - 4,0),(s**3 - 4*s + 3*(s**2) - 4,s**2 - 4 +2*s,0),buff=0)).set_color(YELLOW)#.shift(d,buff=0)
        #mover el vector
        derivada_gota.add_updater(Dgota)
        #para mover el punto
        punto_gota1.add_updater(Dgota)



        #Para la lemniscata    
        s2=ValueTracker(tmin1)
        sg=tmin1
        derivada_lem=Arrow([2*np.cos(sg),2*np.sin(2*sg),0],[-2*np.sin(sg)+2*np.cos(sg),4*np.cos(2*sg)+2*np.sin(2*sg),0],buff=0).set_color(YELLOW)#.move_to(d)#.get_center()+*0.2*UP+s*0.2*RIGHT)
        punto_lem=Dot(radius=0.1,color=YELLOW,fill_opacity=1).move_to([2*np.cos(sg),2*np.sin(2*sg),0])

        def Dlemniscata(obj):
            sg1 = s2.get_value()
            xg=[2*np.cos(sg1),2*np.sin(2*sg1),0]
            punto_lem.become(Dot(radius=0.1,color=YELLOW,fill_opacity=1).move_to(xg))
            derivada_lem.become(Arrow([2*np.cos(sg1),2*np.sin(2*sg1),0],[-2*np.sin(sg1)+2*np.cos(sg1),4*np.cos(2*sg1)+2*np.sin(2*sg1),0],buff=0)).set_color(YELLOW)#.move_to(d)#.get_center()+*0.2*UP+s*0.2*RIGHT)
    
        derivada_lem.add_updater(Dlemniscata)
        punto_lem.add_updater(Dlemniscata)
        fondo=Rectangle(HEIGHT=FRAME_HEIGHT,WIDHT=FRAME_WIDTH,color=BLACK,fill_opacity=1 )

        self.camera_frame.save_state()
        self.play(ShowCreation(axes))
        self.play(Write(VGroup(text15.group,text15_1.group)))
        self.add_foreground_mobject(text15.group)
        self.play(ShowCreation(fabs))
        self.wait(3)
        self.play(FadeOut(text15.group))
        self.remove_foreground_mobject(text15.group)
        self.play(Write(text15_2.group))
        self.wait(4)
        self.play(FadeOut(text15_2.group))
        self.play(Write(text16.group))
        self.add_foreground_mobject(text16.group)
        self.wait(5)
        #Tangente de V
        self.add(tan_absf)
        self.play(t1.set_value, -0.0001,run_time=10)
        self.play(ReplacementTransform(tan_absf,tan_absf_1))
        self.play(t1_1.set_value,-xmin,run_time=10)
        self.wait()
        self.remove_foreground_mobject(text15.group)
        self.play(FadeOut(text16.group),FadeOut(tan_absf_1),FadeOut(text15_1.group))
        #Termina movimiento para tangente de V
        self.play(Write(text18.group))
        self.wait(5)
        self.play(FadeOut(text18.group),Write(text18_1.group))
        self.wait(7)
        self.play(FadeOut(fabs),FadeOut(text18_1.group))
        self.play(Write(text18_2.group))
        self.wait(5)
        self.play(FadeOut(text18_2.group))
        self.play(Write(text19_0group))
        self.wait(3)
        self.play(Write(text19_1group))
        self.wait(5)
        self.play(Write(text19_2group))
        self.wait(2)
        self.play(ShowCreation(fgota))
        self.wait(2)
        self.play(FadeOut(text19.group))
        self.play(Write(text20.group))
        self.wait(6)
        #movimiento de una particula en la gota
        self.play(ShowCreation(punto_gota))
        self.play(s1_1.set_value, tmax,run_time=10)
        self.wait()
        #Termina movimiento de partícula en la gota
        self.play(FadeOut(text20.group),FadeOut(punto_gota))
        self.play(Write(text21.group))
        self.wait(8)
        self.play(FadeOut(text21.group))
        #Animación del vector tangente
        self.play(
        # Nuevo ancho
            self.camera_frame.set_width,fondo.get_width()*5,
            # Nueva posición
            self.camera_frame.move_to,ORIGIN)
        self.play(ShowCreation(punto_gota1),ShowCreation(derivada_gota))
        self.play(s1_2.set_value, tmax-0.0001,run_time=10)
        self.play(Restore(self.camera_frame))
        self.wait()
        ###
        self.play(FadeOut(axes),FadeOut(fgota),FadeOut(punto_gota1),FadeOut(derivada_gota))
        self.play(Write(text22))
        self.wait(13)
        self.play(FadeOut(text22))
        self.play(Write(text23))
        self.wait(8)
        self.play(FadeOut(text23))
        self.play(Write(text24))
        self.wait(16)
        self.play(ReplacementTransform(text24,text25))
        self.wait(7)
        self.play(ReplacementTransform(text25,text26))
        self.wait(6)
        self.play(FadeOut(text26),ShowCreation(axes))
        self.play(ShowCreation(flemniscata))
        self.play(Write(text26_1.group))
        self.wait(4)
        self.play(ReplacementTransform(text26_1.group,text26_2.group))
        self.wait(3)
        self.play(FadeOut(text26_2.group))
        self.play(Write(text27.group))
        self.wait(6.5)
        self.play(FadeOut(text27.group))
        self.play(Write(text28.group))
        self.wait(6)
        self.play(FadeOut(text28.group))
        self.play(
        # Nuevo ancho
            self.camera_frame.set_width,fondo.get_width()*5,
            # Nueva posición
            self.camera_frame.move_to,ORIGIN)
        #Derivada en la lemniscata
        self.play(ShowCreation(punto_lem),ShowCreation(derivada_lem))
        self.play(s2.set_value, tmax1,run_time=10)
        self.play(Restore(self.camera_frame))
        self.play(Write(text29.group))
        self.wait(5.7)
        self.play(FadeOut(text29.group),FadeOut(axes),FadeOut(flemniscata),FadeOut(punto_lem),FadeOut(derivada_lem))
        self.play(Write(text30))
        self.wait(7)
        self.play(ReplacementTransform(text30,text31))
        self.wait(9)
        self.play(ReplacementTransform(text31,text32))
        self.wait(6)
        self.play(FadeOut(text32))
        self.play(Write(text33))
        self.play(ShowCreation(fcicliode))
        self.wait(6)
        self.play(FadeOut(text33),FadeOut(fcicliode))
        self.play(Write(text34))
        self.wait(7)
        self.play(FadeOut(text34))      
    
    