from manimlib.imports import *
#En esta animación sólo se pueden modificar los intervalos en los que se evaluan las parametrizaciones
#Sin embargo se puede aconsejar que se analice el código para crear sus propias animaciones sobre derivadas 
#O para visualizar como se dibujan las curvas dependiendo de la parametrización
class Curvas_suaves_y_cruces_1 (MovingCameraScene,Scene):
    def curva1(self,x):
        return  [x,x**2*np.sin(1/x)+x,0]
    def setup (self):
        Scene.setup(self)
        MovingCameraScene.setup(self)

    def animacion1 (self):
        titulo=TextMobject('''Curvas suaves y \n
                                cruces''')
        text=TextMobject('''  Si $\\gamma$ tiene tangente en $t_0\\in (a,b)$,''',''' \n
                             ¿existe alguna vecindad de $t_0$ donde la curva \n
                             tiene tangente en cada punto de la vecindad? ''')
        text1=TextMobject(''' No,''',''' ni siquiera podemos asegurar que $\\gamma$ \n
                            sea continua fuera de $t_0$''')
        text2=TextMobject('''Si pedimos que $\\gamma$ sea derivable en $(a,b)$ y tiene tangente en $t_0$''',''' \n
                                ¿podemos encontrar alguna vecindad de $t_0$ donde la curva\n
                                 sea regular? ''','''\n
                                 ¡No! ''')
        text3=TextMobject(''' Este problema es similar al siguiente. ''',''' \n
                            Si una función de $\\mathbb{R}$ en $\\mathbb{R}$ es derivable en $(a,b)$,''','''\n
                             aunque $f'(x_0)\\neq 0$,''',''' no podemos asegurar que \n
                             en alguna vecindad de $x_0$''','''\n
                              la función sea monótona.''' )  
        text4=TextMobject('''Checa la función $f(x)=x^{2}sen(1/x)+x$ para $x\\neq 0$''').move_to(3*UP)
        text5=TextMobject('''Usando este ejemplo, da una parametrización \n
                                $\\gamma$ derivable ''','''\n
                                con tangente en $t_0\\in (a,b)$ y que no sea regular \n
                                en ninguna vecindad de $t_0$.''')
        text6=TextMobject('''Para evitar comportamientos extraños como estos,''',''' \n 
                            consideramos funciones regulares con derivada continua,''',''' \n
                                les llamaremos curvas suaves. ''')
        text7=TextMobject('''Intuitivamente las curvas suaves se parecen más \n
                                        a sus tangentes \n
                                 que aquellas que son sólo derivables. ''')
        #Los siguientes valores se pueden cambiar para cambiar el rango de evaluación de las funciones
        tmin1=-0.5
        tmax1=-0.0001
        tmin2=0.0001       
        tmax2=0.5
        ref=Dot(color=RED,radius=0.003)

        f1 = ParametricFunction(self.curva1,t_min=tmin1,t_max=tmax1,color=BLUE_C)
        text4_1=TextMobject('''y $f(0)=0$. ''').scale(0.05).next_to(ref,UP,buff=0.01)        
        
        f2 = ParametricFunction(self.curva1,t_min=tmin2,t_max=tmax2,color=BLUE_C)
        self.camera_frame.save_state()
        self.play(Write(titulo))
        self.wait(3.5)
        self.play(FadeOut(titulo))
        self.play(Write(text[0]))
        self.wait(3.6)
        self.play(Write(text[1]))
        self.wait(4)
        self.play(FadeOut(text))
        self.play(Write(text1[0]))
        self.wait()
        self.play(Write(text1[1]))
        self.wait(7)
        self.play(FadeOut(text1))
        self.play(Write(text2[0]))
        self.wait(6)
        self.play(Write(text2[1]))
        self.wait(5)
        self.play(Write(text2[2]))
        self.wait(3)
        self.play(FadeOut(text2))
        self.play(Write(text3[0]))
        self.wait(3)
        self.play(Write(text3[1]))
        self.wait(5)
        self.play(Write(text3[2]))
        self.wait(2)
        self.play(Write(text3[3]))
        self.wait(4)
        self.play(Write(text3[4]))
        self.wait(4)
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
        self.play(Write(text4_1))
        self.play(ShowCreation(ref))
        self.wait(10)
        self.play(FadeOut(ref),FadeOut(f1),FadeOut(f2),FadeOut(text4),FadeOut(text4_1))
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
    def curva1(self,t):
        return [t**3,np.exp(t),np.cos(10*t)]
    def construct (self):
        
        text8=TextMobject('''Tomemos la siguiente curva parametrizada por''','''\n 
                                $g(t)=(t^{3},e^{t},\\cos(10t))$ ''')
        text9=TextMobject('''La derivada de la parametrización es:''','''
                                  $$\ \ g'(t)=(3t^{2},e^{t},-10sen(10t)$$''').move_to(3*UP)
        text10=TextMobject(''' Veamos como cambia su derivada, \n
                                    en función del tiempo.''').move_to(3*UP)
        text11=TextMobject(''' Su derivada nunca se hace $\\Vec{0}$''')
        text12=TextMobject('''La curva anterior es una curva suave. ''')
        text13=TextMobject('''¿Será que las curvas suaves sólo deben cumplir que \n
                                     su derivada nunca sea $\Vec{0}$? ''')
        text14=TextMobject(''' Veamos otro ejemplo. ''')


        axes=ThreeDAxes()
        #Se puede cambiar para mofidificar el intervalo de evación de la función

        tmin = -1.5
        tmax = 1.5
 
        f1 = ParametricFunction(self.curva1,t_min=tmin,t_max=tmax,color=RED)
        t1=ValueTracker(tmin)
        ti=tmin
        n=((3*ti**2)**2+np.exp(ti)**2+(10*np.sin(10*ti))**2)**(1/2)
        deriv=Arrow( (ti**3,np.exp(ti),np.cos(10*ti)), (ti**3+((3*ti**2))/n ,np.exp(ti)+(np.exp(ti))/n ,np.cos(10*ti)-(10*np.sin(10*ti))/n),buff=0)

        def moving_dot():
            t = t1.get_value()
            x=[t**3,np.exp(t),np.cos(10*t)]
            p = Sphere(radius=0.1,color=RED).move_to(x)
            return p
        dd = always_redraw(moving_dot)     
        def derivada (obj):
            t = t1.get_value()
            deriv.become(Arrow( (t**3,np.exp(t),np.cos(10*t)), (t**3+((3*t**2))*(1/((3*t**2)**2+np.exp(t)**2+(10*np.sin(10*t))**2)**(1/2)) ,np.exp(t)+(np.exp(t))*(1/((3*t**2)**2+np.exp(t)**2+(10*np.sin(10*t))**2)**(1/2)) ,np.cos(10*t)-(10*np.sin(10*t))*(1/((3*t**2)**2+np.exp(t)**2+(10*np.sin(10*t))**2)**(1/2))),buff=0))

        deriv.add_updater(derivada)

        self.play(Write(text8))
        self.wait(5)
        self.play(FadeOut(text8))
        self.set_camera_orientation(0.8*np.pi/2, -0.25*np.pi,distance=30)
        self.play(ShowCreation(axes))
        self.play(ShowCreation(f1))
        self.add_fixed_in_frame_mobjects(text9)
        self.play(Write(text9))
        self.wait(6)
        self.play(FadeOut(text9))
        self.add_fixed_in_frame_mobjects(text10)
        self.play(Write(text10))
        self.wait(6.7)
        self.play(FadeOut(text10))
        #Animación de la derivada normalizada
        self.play(ShowCreation(dd),ShowCreation(deriv))
        self.play(t1.set_value, tmax,run_time=30)
        self.wait()
        self.play(FadeOut(axes),FadeOut(f1),FadeOut(dd),FadeOut(deriv))
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
    def gota(self,t):
        return  [(1-np.sin(t))*np.cos(t),np.sin(t)-1,0]
    def lemniscata(self,t):
        return  [(2)*np.cos(t),2*np.sin(2*t),0]
    def abs(self,t):
        return  [t,np.abs(t),0]
    def cicloide(self,t):
        return  [(t-np.sin(t)),(1-np.cos(t)),0]
    def construct(self):

        text15=TextMobject('''Tomemos la siguiente curva.''').move_to(3*UP)
        text16=TextMobject('''Veamos como cambia su tangente conforme cambia t.''').move_to(3*UP)
        text17=TextMobject(''' Tomemos la siguiente curva''')
        text18=TextMobject('''¿Existe alguna parametrización suave de la curva? ''').move_to(3*UP)
        text19=TextMobject('''Tomemos la siguiente parametrización''',
                                    '''$$f:\\left[\\frac{\\pi}{2},\\frac{5\\pi}{2}\\right]\\rightarrow\\mathbb{R}^{2}$$''','''\n
                                             $f(t)=((1-sen(t))cos(t),sen(t)-1)$''').move_to(2*UP)
        text20=TextMobject('''Veamos como recorre un punto a la curva en el intervalo \n
                                     de la parametrización. ''').move_to(3*UP)
        text21=TextMobject('''Y ahora como se mueve su vector tangente a lo largo \n
                                 de esta curva a partir de la parametrización dada. ''').move_to(3*UP)
        text22=TextMobject('''Nota que tenemos una parametrización simple cerrada, \n
                                pero en el punto donde la curva se cierra''','''\n
                             (donde pierde la inyectividad) tenemos dos tangentes,''','''\n
                             por lo que se trata de una curva regular, como la derivada \n
                              es continua, además es suave.  ''')
        text23=TextMobject('''En cambio la curva en forma de "V" al no ser \n
                                regular, no puede ser suave. ''')
        text24=TextMobject('''Aunque $f$ parece tener un "pico", en realidad es un cruce, \n
                                o sea, la curva se cruza sobre sí misma, perdiendo la \n 
                                inyectividad.''','''\n
                                 Como la curva admite una parametrización suave, \n
                                 decimos que la curva es suave. ''')
        text25=TextMobject(''' Considera cualquier parametrización suave de la curva \n
                                        definida en $[a,b]$,''','''\n
                                 ¿qué punto es $f(a)$ y cuál es $f(b)$? ''')
        text26=TextMobject('''Para ahondar en el asunto, consideremos otro \n
                                    ejemplo interesante''')
        text26_1=TextMobject(''' Podemos parametrizarla con 
                                    $$f:[0,2\pi]$$ ''').move_to(3*UP)
        text26_2=TextMobject(''' $f(t)=2(cos(t),sen(2t))$ ''').move_to(3*UP)

        text27=TextMobject('''Podemos ver que la curva tiene un cruce. ¿Es suave?''').move_to(3*UP)
        text28=TextMobject('''Veamos cómo cambia su derivada conforme cambia t. ''').move_to(3*UP)
        text29=TextMobject('''Nunca se anuló y en el cruce nuevamente tenemos \n
                                dos tangentes. ''').move_to(3*UP)
        text30=TextMobject('''La curva anterior es una curva suave y \n
                            se conoce como Lemniscata. ''')
        text31=TextMobject('''¿Puedes dar alguna parameterización de esta curva\n
                                 que no sea suave? ''')
        text32=TextMobject('''¿Puedes dar una parametrización suave y simple de la curva? ''')
        text33=TextMobject('''La siguiente curva se llama cicloide, ¿es suave? ''').move_to(3*DOWN)
        text34=TextMobject(''' Modifica el código de esta animación para\n
                                     generar más ejemplos. ''')

        axes=Axes()
        #Se puede cambiar para mofidificar el intervalo de evación de la función
        xmin=-4
        xmax=4
        ##
        fabs = ParametricFunction(self.abs,t_min=-4,t_max=4,color=BLUE_C)
        tmin = np.pi/2
        tmax = 5*np.pi/2
        tmin1 = 0
        tmax1 = 2*np.pi
        fgota = ParametricFunction(self.gota,t_min=tmin,t_max=tmax,color=RED)
        flemniscata = ParametricFunction(self.lemniscata,t_min=tmin1,t_max=tmax1,color=GREEN)
        fcicliode = ParametricFunction(self.cicloide,t_min=-2*np.pi-1,t_max=2*np.pi+1,color=GREEN)

        #Tangente del valor absoluto
        t1=ValueTracker(xmin)
        def tan_abs():
            t = t1.get_value()
            x=[t,np.abs(t),0]
            n=2**(1/2)/2
            d = Dot(color=RED,fill_opacity=1,fill_color=RED).move_to(x)
            tan=Line([0,0,0],[1,t/np.abs(t),0],color=RED,opacity=1).move_to(d)#.get_center()+0.2*DOWN+0.2*RIGHT)
            V1=VGroup(tan,d)
            return V1
        tan_absf = always_redraw(tan_abs) 
        t1_1=ValueTracker(0.0001)
        def tan_abs_1():
            t = t1_1.get_value()
            x=[t,np.abs(t),0]
            d = Dot(color=RED).move_to(x)
            tan=Line([0,0,0],[1,t/np.abs(t),0],color=RED,opacity=1).move_to(d)#.get_center()+0.2*UP+0.2*RIGHT)           
            V2=VGroup(tan,d)
            return V2
        tan_absf_1 = always_redraw(tan_abs_1) 
        #Para el movimiento de un objeto en la gota
        s1=ValueTracker(tmin)
        def Pgota():
            s = s1.get_value()
            x=[(1-np.sin(s))*np.cos(s),np.sin(s)-1,0]
            d = Dot(radius=0.1,color=RED,fill_opacity=1).move_to(x)
            return d
        p_gota = always_redraw(Pgota)
      
        #tangente de la gota
        s1_1=ValueTracker(tmin)
        def Dgota():
            s = s1_1.get_value()
            x=np.array([(1-np.sin(s))*np.cos(s),np.sin(s)-1,0])
            d = Dot(color=RED,fill_opacity=1).move_to(x)
            #de=np.array([(np.sin(s)**2-np.cos(s)**2,np.cos(s),0)])
            
            deriv=Arrow(((1-np.sin(s))*np.cos(s),np.sin(s)-1,0),((1-np.sin(s))*np.cos(s)+np.sin(s)**2-np.cos(s)**2,np.cos(s)+np.sin(s)-1,0),buff=0)#.shift(d,buff=0)
    
            G=VGroup(d,deriv)
            return G
        d_gota = always_redraw(Dgota)

        #Para la lemniscata    
        s2=ValueTracker(tmin1)
        def Dlemniscata():
            s = s2.get_value()
            x=[2*np.cos(s),2*np.sin(2*s),0]
            d = Dot(radius=0.1,color=RED,fill_opacity=1).move_to(x)
            deriv=Arrow([2*np.cos(s),2*np.sin(2*s),0],[-2*np.sin(s)+2*np.cos(s),4*np.cos(2*s)+2*np.sin(2*s),0],buff=0)#.move_to(d)#.get_center()+*0.2*UP+s*0.2*RIGHT)
            G1=VGroup(d,deriv)
            return G1
        d_lemniscata = always_redraw(Dlemniscata)
        fondo=Rectangle(HEIGHT=FRAME_HEIGHT,WIDHT=FRAME_WIDTH,color=BLACK,fill_opacity=1 )

        self.camera_frame.save_state()
        self.play(ShowCreation(axes))
        self.play(Write(text15))
        self.play(ShowCreation(fabs))
        self.wait(3)
        self.play(FadeOut(text15))
        self.play(Write(text16))
        self.wait(5)
        #Tangente de V
        self.add(tan_absf)
        self.play(t1.set_value, -0.0001,run_time=10)
        self.play(ReplacementTransform(tan_absf,tan_absf_1))
        self.play(t1_1.set_value,-xmin,run_time=10)
        self.wait()
        self.play(FadeOut(text16),FadeOut(tan_absf_1))
        #Termina movimiento para tangente de V
        self.play(Write(text18))
        self.wait(5)
        self.play(FadeOut(fabs),FadeOut(text18))
        self.play(Write(text19[0]))
        self.wait(3)
        self.play(Write(text19[1]))
        self.wait(5)
        self.play(Write(text19[2]))
        self.wait(2)
        self.play(ShowCreation(fgota))
        self.wait(2)
        self.play(FadeOut(text19))
        self.play(Write(text20))
        self.wait(6)
        #movimiento de una particula en la gota
        self.play(ShowCreation(p_gota))
        self.play(s1.set_value, tmax,run_time=10)
        self.wait()
        #Termina movimiento de partícula en la gota
        self.play(FadeOut(text20),FadeOut(p_gota))
        self.play(Write(text21))
        self.wait(8)
        #Animación del vector tangente
        self.add(d_gota)
        self.play(s1_1.set_value, tmax-0.1,run_time=10)
        self.wait()
        ###
        self.play(FadeOut(text21),FadeOut(axes),FadeOut(fgota),FadeOut(d_gota))
        self.play(Write(text22[0]))
        self.wait(8)
        self.play(Write(text22[1]))
        self.wait(3)
        self.play(Write(text22[2]))
        self.wait(8)
        self.play(FadeOut(text22))
        self.play(Write(text23))
        self.wait(8)
        self.play(FadeOut(text23))
        self.play(Write(text24[0]))
        self.wait(11)
        self.play(Write(text24[1]))
        self.wait(7)
        self.play(ReplacementTransform(text24,text25))
        self.wait(7)
        self.play(ReplacementTransform(text25,text26))
        self.wait(6)
        self.play(FadeOut(text26),ShowCreation(axes))
        self.play(ShowCreation(flemniscata))
        self.play(Write(text26_1))
        self.wait(4)
        self.play(ReplacementTransform(text26_1,text26_2))
        self.wait(3)
        self.play(FadeOut(text26_2))
        self.play(Write(text27))
        self.wait(6.5)
        self.play(FadeOut(text27))
        self.play(Write(text28))
        self.wait(6)
        self.play(FadeOut(text28))
        self.play(
        # Nuevo ancho
            self.camera_frame.set_width,fondo.get_width()*5,
            # Nueva posición
            self.camera_frame.move_to,ORIGIN)
        #Derivada en la lemniscata
        self.add(d_lemniscata)
        self.play(s2.set_value, tmax1,run_time=10)
        self.play(Restore(self.camera_frame))
        self.play(Write(text29))
        self.wait(5.7)
        self.play(FadeOut(text29),FadeOut(axes),FadeOut(flemniscata),FadeOut(d_lemniscata))
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


########################
### Curvas regulares ###
########################

class Regulares_y_picos(Scene):

    ### Vamos a definir previamente funciones auxiliares
    ### que son las que van a generar las curvas del video
    ### Si quieres ver otras curvas puedes definir aquí tus
    ### funciones para animar

    def lemniscata(self,t):
        x = 2*(2**(1/2)*np.cos(t)/(np.sin(t)**2+1))
        y = 2*(2**(1/2)*np.cos(t)*np.sin(t)/(np.sin(t)**2+1))
        return [x,y,0]
    
    def VCurve(self,t):
        return [2*t,2*np.abs(t),0]

    def gota(self,t):
        x = 1.0*(1-np.sin(t))*np.cos(t)
        y = (1.75)*(np.sin(t)-1)+1.5
        return [x,y,0]

    def construct(self):

        ## Textos
        Title = TextMobject("Curvas regulares y picos")
        t1 = TextMobject('''Sabes hasta ahora lo que es una parametrización, definiremos \n 
                            entonces la regularidad de una curva a partir de su parametrización.''').scale(0.8)
        t2 = TextMobject('''Sea $\\gamma:A\\subseteq\\mathbb{R}\\to\\mathbb{R}^n$, decimos que \n 
                            $\\gamma$ es regular si $\\forall t\\in A$, $||\\gamma'(t)||>0$''')
        t3 = TextMobject('''Veamos un ejemplo de curva regular en $\\mathbb{R}^2$''')
        t4 = TexMobject(r"\gamma(t)=(\sin(t),\cos(t))")
        t5 = TextMobject('''Ahora veamos otro ejemplo de curva regular''').to_edge(UP)
        t6 = TexMobject(r"\gamma(t)=\left(\dfrac{\sqrt{2}\cos(t)}{\sin^2(t)+1},\dfrac{\sqrt{2}\cos(t)\sin(t)}{\sin^2(t)+1}\right)").scale(0.7).to_edge(UP)
        t7 = TextMobject('''A esta curva se le conoce como lemniscata de Bernoulli''').scale(0.7).to_edge(DOWN)
        t8 = TextMobject('''Nota que se pueden dar parametrizaciones no regulares de estas \n
                            curvas, sin embargo, admiten parametrizaciones regulares \n
                            y por ello decimos que son curvas regulares''').scale(0.9)
        t9 = TextMobject('''Puedes tratar de animar otras curvas regulares interesantes, \n
                            como una cardioide, y ver el vector derivada de cada una.''').shift(UP)
        t10 = TextMobject('''¿Dónde tiene que empezar y terminar la parametrización \n
                            para que sea regular?''').next_to(t9,DOWN,buff=1)
        t11 = TextMobject('''Considera ahora la siguiente curva''')
        t12 = TextMobject('''¿Se puede dar una parametrización regular de la curva?, \n
                            ¿y una derivable?''').scale(0.9).to_edge(UP)
        t13 = TextMobject('''Una posible parametrización para esta curva es''').scale(0.9).to_edge(UP)
        t14 = TexMobject(r"\gamma(t)=(t,|t|)\text{ con } t\in[-1,1]").scale(0.9).next_to(t13,DOWN)
        t15 = TextMobject('''Como no es derivable, entonces no puede ser regular''').to_edge(UP)
        t16 = TextMobject('''Ahora considera la parametrización $\\gamma(t)=(t,|t|^3)$ con $t\\in[-1,1]$''').scale(0.8).to_edge(UP)
        t17 = TextMobject('''Verifica que $\\gamma$ es derivable, y que $\\gamma'(0)=(0,0)$''').scale(0.8).next_to(t16,DOWN)
        t18 = TextMobject('''Se puede demostrar que cualquier parametrización de esta\n
                            curva es no regular, ya sea por no ser derivable o porque \n
                            la derivada se anula al momento de llegar al "pico". ''')
        t19 = TextMobject('''Este tipo de "picos"  dan indicio de que la curva no tiene\n
                            parametrización regular, porque no hay forma de que en el "pico" \n
                            la curva tenga una tangente''').scale(0.9)
        t20 = TextMobject('''Ten cuidado, hay curvas regulares con puntos donde parece\n
                            no haber tangente, revisa el siguiente ejemplo.''')
        rapidez = DecimalNumber(
            0,
            num_decimal_places = 2,
            include_sign = True,
            unit = None,
        ).to_corner(DOWN+RIGHT).shift(UP)
        t21 = TexMobject(r"||\gamma'(t)||=").next_to(rapidez,LEFT)
        
        # Ejes
        ejes = Axes(
            x_min=-4,
            x_max=4,
            y_min=-2.5,
            y_max=2.5,
            axis_config={
                "tick_frequency": 2,
            }
        )

        # Para la rapidez
        # Aquí es donde se puede cambiar la rapidez, es decir la norma de la derivada,
        # para las funciones que utilices
        # Nota que esto se utiliza en conjunto con un objeto Decimal y un add.updater
        self.t_offset=0
        def rapidez_update1(mob,dt):
            rate = 0.5*dt
            mob.set_value(1)
            self.t_offset += rate
        def rapidez_update2(mob,dt):
            rate = 0.5*dt
            mob.set_value((2/(3-np.cos(2*(self.t_offset+rate))))**(0.5))
            self.t_offset += rate

        # Gráficas y demás objetos
        # Las funciones que se definen aquí son para las actualizaciones en la flecha
        # que representa el vector velocidad (derivada)
        # De nuevoe estas funcionan con un add.updater para crear las animaciones continuas
        self.t_offset=0
        circ = Circle(radius=2,color=RED)
        circ_vel = Arrow(start=((2,0,0)),end=((0,2,0)),color=BLUE,buff=0)
        def arrow_update1(mob,dt):
            rate = 0.5*dt
            new_arrow = Arrow(
                (
                    2*np.cos(self.t_offset+rate),
                    2*np.sin(self.t_offset+rate),
                    0
                    ),
                (
                    -2*np.sin(self.t_offset+rate)+2*np.cos(self.t_offset+rate),
                    2*np.sin(self.t_offset+rate)+2*np.cos(self.t_offset+rate),
                    0
                    ),
                color=BLUE,
                buff=0
            )
            mob.become(new_arrow)
            self.t_offset += rate

        lemnis = ParametricFunction(self.lemniscata,t_min=0,t_max=2*np.pi+0.1,color=RED)
        lemnis_vel = Arrow(start=((2,0,0)),end=((0,2,0)),color=BLUE,buff=0)
        def arrow_update2(mob,dt):
            rate = 0.5*dt
            new_arrow = Arrow(
                (
                    2*(2**(1/2)*np.cos(self.t_offset+rate)/(np.sin(self.t_offset+rate)**2+1)),
                    2*(2**(1/2)*np.cos(self.t_offset+rate)*np.sin(self.t_offset+rate)/(np.sin(self.t_offset+rate)**2+1)),
                    0
                    ),
                (
                    -2*(np.sin(self.t_offset+rate)*(np.sin(self.t_offset+rate)**2+2*np.cos(self.t_offset+rate)**2+1))/(np.sin(self.t_offset+rate)**2+1)**2+2*(2**(1/2)*np.cos(self.t_offset+rate)/(np.sin(self.t_offset+rate)**2+1)),
                    -2*((np.sin(self.t_offset+rate)**4+np.sin(self.t_offset+rate)**2+(np.sin(self.t_offset+rate)**2-1)*np.cos(self.t_offset+rate)**2)/(np.sin(self.t_offset+rate)**2+1)**2)+2*(2**(1/2)*np.cos(self.t_offset+rate)*np.sin(self.t_offset+rate)/(np.sin(self.t_offset+rate)**2+1)),
                    0
                    ),
                color=BLUE,
                buff=0
            )
            mob.become(new_arrow)
            self.t_offset += rate

        V = ParametricFunction(self.VCurve,t_min=-1,t_max=1,color=BLUE)
        gota = ParametricFunction(self.gota,t_min=np.pi/2,t_max=5*np.pi/2+0.1,color=BLUE)

        
        # Grupos útiles
        Group1 = VGroup(t9,t10)
        Group2 = VGroup(t13,t14)
        Group3 = VGroup(t16,t17,ejes,V)
        Group4 = VGroup(circ,circ_vel,t21,rapidez)
        Group5 = VGroup(t6,t7,lemnis,lemnis_vel,ejes,t21,rapidez)
        Group6 = VGroup(gota,ejes,t20)

        # Animación
        
        self.play(Write(Title))
        self.wait()
        self.play(FadeOut(Title))
        self.play(Write(t1))
        self.wait(9.5)
        self.play(ReplacementTransform(t1,t2))
        self.wait(11.5)
        self.play(ReplacementTransform(t2,t3))
        self.wait(5)
        self.play(ReplacementTransform(t3,t4))
        self.play(ApplyMethod(t4.to_edge,UP))
        self.play(ShowCreation(ejes,run_time=0.5))
        self.play(ShowCreation(circ))
        self.play(Write(t21))
        circ_vel.add_updater(arrow_update1)
        rapidez.add_updater(rapidez_update1)
        self.add(circ_vel,rapidez)
        self.wait(2*PI)
        circ_vel.clear_updaters()
        rapidez.clear_updaters()
        self.play(FadeOut(Group4))
        self.play(ReplacementTransform(t4,t5))
        self.wait(4.7)
        self.play(ReplacementTransform(t5,t6))
        self.play(ShowCreation(lemnis))
        self.play(Write(t21))
        lemnis_vel.add_updater(arrow_update2)
        rapidez.add_updater(rapidez_update2)
        self.add(lemnis_vel,rapidez)
        self.wait(2*PI+0.1)
        lemnis_vel.clear_updaters()
        rapidez.clear_updaters()
        self.play(Write(t7))
        self.wait(5.4)
        self.play(FadeOut(Group5))
        self.play(Write(t8))
        self.wait(11)
        self.play(ReplacementTransform(t8,t9))
        self.wait(9.2)
        self.play(Write(t10))
        self.wait(6.5)
        self.play(FadeOut(Group1))
        self.play(Write(t11))
        self.play(ApplyMethod(t11.to_edge,UP))
        self.play(ShowCreation(ejes),run_time=0.5)
        self.play(ShowCreation(V))
        self.play(ReplacementTransform(t11,t12))
        self.wait(6.5)
        self.play(ReplacementTransform(t12,t13))
        self.wait(4.25)
        self.play(Write(t14))
        self.wait()
        self.play(ReplacementTransform(Group2,t15))
        self.wait(5.4)
        self.play(ReplacementTransform(t15,t16))
        self.wait(5.8)
        self.play(Write(t17))
        self.wait(5.8)
        self.play(FadeOut(Group3))
        self.play(Write(t18))
        self.wait(13.3)
        self.play(ReplacementTransform(t18,t19))
        self.wait(12.5)
        self.play(ReplacementTransform(t19,t20))
        self.wait(8)
        self.play(ApplyMethod(t20.to_edge,UP))
        self.play(ShowCreation(ejes))
        self.play(ShowCreation(gota))
        self.wait(2)
        self.play(FadeOut(Group6))
        self.wait()