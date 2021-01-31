from manimlib.imports import *

######################################################
##### Reparametrizacion y regla de la cadena #########
#######################################################

#Esta animación está en creada en partes, uniendo las animaciones al final del código
 
def curva1p(t):
    return [t,np.cos(4*t),np.sin(4*t)] 
def curva2p(s):
    return [-s**3,np.cos(-4*s**3),np.sin(-4*s**3)]

class Reparametrizacion_y_regla_de_la_cadena1 (ThreeDScene):    
    def textos1 (self):
        axis_config = {
            "x_min" : -8,
            "x_max" : 8,
            "y_min" : -8,
            "y_max" : 8,
            "z_min" : -8,
            "z_max" : 8,
        }
        titulo=TextMobject('''Reparametrización de curvas \n
                            y regla de la cadena''')
        text=TextMobject("Tomemos la siguiente curva").move_to(3*UP)
        text1=TextMobject('''$\\gamma(t)=(t,\\cos(4t),\\sin(4t))$ \n''',
                               '''y considera $C=Im(\gamma)$ ''').move_to(3*UP)
        text2=TextMobject('''Tomando $f(s)=-s^{3}$''').move_to(3*UP)
        text3=TextMobject('''Entonces
                            $\\xi(s)=(\\gamma\\circ f)(s)=(-s^{3},\\cos(-4s^{3}),\\sin(-4s^{3}))$''' ).move_to(3*UP)
        text4=TextMobject('''Como $Im(\\gamma)=Im(\\xi)=C$ decimos $\\xi$ \n
                                es una reparametrización de $C$.''').move_to(3*UP)
        text5=TextMobject(''' Tomemos un punto en la curva y veamos como se mueve \n
                                 al comparar ambas parametrizaciones.''').move_to(3*UP)
        axes = ThreeDAxes( **axis_config)

        tmin = -8
        tmax = 8
        vs=tmax**(1/3)
        f = ParametricFunction(curva1p,t_min=tmin,t_max=tmax,color=RED)
        g = ParametricFunction(curva1p,t_min=tmin,t_max=tmax,color=BLUE_C)
        self.play(Write(titulo))
        self.wait(5)
        self.play(FadeOut(titulo))
        self.set_camera_orientation(0.8*np.pi/2, -0.25*np.pi,distance=20)           
        self.play(ShowCreation(axes))
        self.add_fixed_in_frame_mobjects(text)
        self.play(Write(text))      
        self.wait(2)
        self.play(FadeOut(text))
        self.add_fixed_in_frame_mobjects(text1[0])
        self.play(Write(text1[0]))
        self.wait(4)
        self.add_fixed_in_frame_mobjects(text1[1])
        self.play(Write(text1[1]))
        self.play(ShowCreation(f),run_time=2)
        self.wait(3)
        self.play(FadeOut(text1))
        self.add_fixed_in_frame_mobjects(text2)
        self.play(Write(text2))
        self.wait(3)
        self.play(FadeOut(text2))
        self.add_fixed_in_frame_mobjects(text3)
        self.play(Write(text3))
        self.play(ReplacementTransform(f,g),runtime=2)
        self.wait(5)
        self.play(FadeOut(text3))
        self.add_fixed_in_frame_mobjects(text4)
        self.play(Write(text4))
        self.wait(6)
        self.play(FadeOut(text4))
        self.add_fixed_in_frame_mobjects(text5)
        self.play(Write(text5))
        self.wait(9)
        self.play(FadeOut(text5))

    def mov_particula (self):
        #Se puede modificar t0 para cambiar la longitud de los number lines
        t0=7
        line_config = {
            "x_min" : -t0+0.1,
            "x_max" : t0+0.1,
            "unit_size": 0.3,
            "include_numbers": True,
            #"numbers_to_show": None,
            ##"longer_tick_multiple": 2,
            "number_at_center": 0,
            "number_scale_val": 0.5,
            "label_direction": DOWN,
            "line_to_number_buff": MED_SMALL_BUFF,
            "include_tip": False,
            "tip_width": 0.25,
            "tip_height": 0.25,

        }
        line_config2 = {
            "x_min" : -(t0**(1/3))+0.2,
            "x_max" : t0**(1/3)+0.2,
            "unit_size": 1.1,
            "include_numbers": True,
            #"numbers_to_show": None,
            ##"longer_tick_multiple": 2,
            "number_at_center": 0,
            "number_scale_val": 0.5,
            "label_direction": DOWN,
            "line_to_number_buff": MED_SMALL_BUFF,
            "include_tip": False,
            "tip_width": 0.25,
            "tip_height": 0.25,

        }
        number_line= NumberLine( **line_config).move_to(2*DOWN+(3-0.5)*LEFT)

        ##Movimiento para una partícula en la primera parametrización
        t1 = ValueTracker(-t0)
        p_1=Sphere(radius=0.1,color=RED,fill_opacity=1).move_to([(-t0,np.cos(4*(-t0)),np.sin(4*(-t0)))])
        def mov_1(obj):
            t = t1.get_value()
            p_1.become(Sphere(radius=0.1,color=RED,fill_opacity=1).move_to([(t,np.cos(4*t),np.sin(4*t))]))
        p_1.add_updater(mov_1)

        p_t=Sphere(radius=0.1,color=RED,fill_opacity=1).move_to(number_line.number_to_point(t0))
        pt_label=TextMobject("t").next_to(p_t,UP,buff=0.1)

        def mov_t(obj):
            tn = t1.get_value()
            p_t.become(Sphere(radius=0.1,color=RED,fill_opacity=1).move_to(number_line.number_to_point(tn)))
            pt_label.become(TextMobject("t").next_to(p_t,UP,buff=0.1))
        
        Movimiento_1=VGroup(p_t,pt_label)
        Movimiento_1.add_updater(mov_t)


        #movimiento para la esfera en la parametrización

        s1=ValueTracker(-(t0**(1/3)))
        p_2 = Sphere(radius=0.1).move_to([(-(-(t0**(1/3)))**3,np.cos(-4*(-(t0**(1/3)))**3),np.sin(-4*(-(t0**(1/3)))**3))])
        def mov_2(obj):
            s = s1.get_value()
            p_2.become(Sphere(radius=0.1).move_to([(-s**3,np.cos(-4*s**3),np.sin(-4*s**3))]))
        
        p_2.add_updater(mov_2)

        number_line2= NumberLine(**line_config2).next_to(number_line,DOWN,buff=1)
        s=Dot(color=BLUE_C).move_to(number_line2.number_to_point(-(t0**(1/3))))#,UP,buff=0)#.scale(0.5)
        s_label=TextMobject("s").next_to(s,UP,buff=0.1)
        def mov_s(obj):
            sn = s1.get_value()
            s.become(Dot(color=BLUE_C).move_to(number_line2.number_to_point(sn)))#,UP,buff=0)#.scale(0.5)
            s_label.become(TextMobject("s").next_to(s,UP,buff=0.1))
        s.add_updater(mov_s)
        s_label.add_updater(mov_s)
        Movimiento_2=VGroup(s,s_label)
    
        fondo2=Circle(radius=20,color=BLACK, fill_opacity=1,fill_color=BLACK)
        self.add(p_1)
        self.add_fixed_in_frame_mobjects(number_line)
        self.add_fixed_in_frame_mobjects(Movimiento_1)
        self.play(ShowCreation(number_line),ShowCreation(Movimiento_1))
        self.play(t1.set_value, t0,run_time=20) 
        #mov para la reparametrizacion
        self.add_fixed_in_frame_mobjects(number_line2)
        self.add_fixed_in_frame_mobjects(Movimiento_2)
        self.play(ShowCreation(number_line2),ShowCreation(Movimiento_2),ShowCreation(p_2))
        self.play(s1.set_value, t0**(1/3),run_time=20) 
        self.wait()
        self.play(FadeOut(p_1),FadeOut(number_line),FadeOut(number_line2),
                    FadeOut(p_2),FadeOut(Movimiento_1),FadeOut(Movimiento_2))
        self.add_fixed_in_frame_mobjects(fondo2)       
        self.play(GrowFromCenter(fondo2))
   
    def textos2 (self):
        axis_config = {
            "x_min" : -8,
            "x_max" : 8,
            "y_min" : -8,
            "y_max" : 8,
            "z_min" : -8,
            "z_max" : 8,
        }
        text6=TextMobject('''El punto recorre de una manera diferente a la curva \n
                                dependiendo de la parametrización.''')
        text7=TextMobject('''Formalmente. \n
                               Sea $C\\in\mathbb{R}^{n}$ una curva y $\\gamma:I\\subset\\mathbb{R}\\rightarrow\\mathbb{R}^{n}$ \n
                                        una parametrización de C. \n ''',
                               ''' \n Si $f:A\\subset\\mathbb{R}\\rightarrow I\\subset\\mathbb{R}$ es sobreyectiva,\n
                                entonces \n
                                $\\rho=\\gamma\\circ f:A\\rightarrow\\mathbb{R}^{n}$ parametriza a $C$ \n
                                y es llamada una reparametrización de la curva.''')
        text7_1=TextMobject('''Además, decimos que las reparametrizaciones conservan el sentido si''','''\n
                                estas empiezan y terminanen los mismos puntos que la \n
                                 parametrización.''','''Por otro lado,\n
                                    tienen sentido contrario si con al reparametrización \n
                                    empiezan y terminan al revés. ''')
        text7_2=TextMobject('''¿Entonces la reparametrización del ejemplo conserva el sentido\n
                                         o lo cambia? ''')
        text8=TextMobject('''La regla de la cadena nos dice que la derivada de una función \n
                                 reparametrizada es: \n
                                    $\\rho'(t)=(f'\\cdot(\gamma'\\circ f))(t)$''')
        text9=TextMobject(''' Veamos como se aplica lo anterior en la \n
                                     curva presentada al inicio.''')
        text10=TextMobject(''' La derivada de la reparametrización es: \n''',
                                '''$\\xi'(s)=-3s^{2}(1,-4\\sin(-4s^{3}),4\\cos(-4s^{3})) $''').move_to(3*UP)
        text11=TextMobject("Veamos como cambia $\\xi'$ conforme cambia t").move_to(DOWN*UP)
       
        axes = ThreeDAxes( **axis_config)
        tmin = -7
        tmax = 7
        vs=tmax**(1/3)
        f = ParametricFunction(curva1p,t_min=tmin,t_max=tmax,color=RED)
        g = ParametricFunction(curva1p,t_min=tmin,t_max=tmax,color=BLUE_C)
        fondo=Rectangle(HEIGHT=FRAME_HEIGHT,WIDHT=FRAME_WIDTH,color=BLACK,fill_opacity=1 )
        self.add_fixed_in_frame_mobjects(text6)
        self.play(Write(text6))
        self.wait(8)
        self.play(FadeOut(text6))
        ###FadeOutATODO
        self.add_fixed_in_frame_mobjects(text7[0])
        self.play(Write(text7[0]))
        self.wait(9)
        self.add_fixed_in_frame_mobjects(text7[1])
        self.play(Write(text7[1]))
        self.wait(15)
        self.play(FadeOut(text7))
        self.add_fixed_in_frame_mobjects(text8)
        self.play(Write(text8))
        self.wait(11)
        self.play(FadeOut(text8))
        self.add_fixed_in_frame_mobjects(text9)
        self.play(Write(text9))
        self.wait(7)
        self.play(FadeOut(text9))
        self.add_fixed_in_frame_mobjects(text10)
        self.play(Write(text10))
        self.wait(4)
        self.play(FadeOut(text10[0]))
        self.play(text10[1].shift, 0.5*UP, runtime=3)
        self.add_fixed_in_frame_mobjects(text11)
        self.play(Write(text11))
        self.wait(7)
        self.play(FadeOut(text11),FadeOut(text10[1]))
 
    
    def construct(self):
        
        #Unión de las animaciones, siempre se pueden comentar algunas para que el proceso de compilación sea más corto
        #Presenta la primera parte de la animación
        self.textos1()
        self.wait()
        #Presenta el movimiento de una partícula con las dos parametrizaciones
        self.mov_particula()
        self.wait()
        #Presenta la segunda parte de los textos
        self.textos2()
        
class Reparametrizacion_y_regla_de_la_cadena2 (ThreeDScene):
    def construct(self):
        t0=7
        line_config = {
            "x_min" : -t0+0.1,
            "x_max" : t0+0.1,
            "unit_size": 0.3,
            "include_numbers": True,
            #"numbers_to_show": None,
            ##"longer_tick_multiple": 2,
            "number_at_center": 0,
            "number_scale_val": 0.5,
            "label_direction": DOWN,
            "line_to_number_buff": MED_SMALL_BUFF,
            "include_tip": False,
            "tip_width": 0.25,
            "tip_height": 0.25,

        }
        line_config2 = {
            "x_min" : -(t0**(1/3))+0.2,
            "x_max" : t0**(1/3)+0.2,
            "unit_size": 1.1,
            "include_numbers": True,
            #"numbers_to_show": None,
            ##"longer_tick_multiple": 2,
            "number_at_center": 0,
            "number_scale_val": 0.3,
            "label_direction": DOWN,
            "line_to_number_buff": MED_SMALL_BUFF,
            "include_tip": False,
            "tip_width": 0.25,
            "tip_height": 0.25,

        }
        axis_config = {
            "x_min" : -8,
            "x_max" : 8,
            "y_min" : -8,
            "y_max" : 8,
            "z_min" : -8,
            "z_max" : 8,
        }
        text15=TextMobject('''Derivada de la parametrización''').move_to(3*UP)
        text16=TextMobject('''Derivada con la reparametrización''').move_to(3*UP)
        text12=TextMobject('''Hay otra forma de saber si la reparetrización\n
                             cambia el sentido. Si la derivada de la función que \n
                                 induce una reparametrización es positiva,''',''' \n
                                conserva el signo, si es negativo cambia el sentido ''')
        text13=TextMobject('''¿Se te ocurre cómo saber cuál es el sentido \n
                                    de una curva suave cerrada? ''')
        text14=TextMobject('''Modifica el código para crear más ejemplos.''')
        axes = ThreeDAxes( **axis_config)
        tmin = -5
        tmax = 5
        vs=tmax**(1/3)
        g = ParametricFunction(curva1p,t_min=-t0,t_max=t0,color=BLUE_C)
        
        t2 = ValueTracker(tmin)
        number_line= NumberLine( **line_config).move_to(2*DOWN+(3-0.5)*LEFT)
        number_line3= NumberLine(**line_config2).move_to(2*DOWN+(3-0.5)*LEFT)
        #Movimiento para la parametrización
        p_parametrizacion = Sphere(radius=0.1,color=RED,fill_opacity=1).move_to([tmin,np.cos(4*tmin),np.sin(4*tmin)])
        d_parametrizacion=Arrow( (tmin,np.cos(4*tmin),np.sin(4*tmin)),(tmin+1,np.cos(4*tmin)-np.sin(4*tmin)*4,np.sin(4*tmin)+np.cos(4*tmin)*4)  ,buff=0 )


        def mov_parametrizacion(obj):
            tp = t2.get_value()
            x=[tp,np.cos(4*tp),np.sin(4*tp)]
            p_parametrizacion.become(Sphere(radius=0.1,color=RED,fill_opacity=1).move_to([tp,np.cos(4*tp),np.sin(4*tp)]))
            d_parametrizacion.become(Arrow( (tp,np.cos(4*tp),np.sin(4*tp)),(tp+1,np.cos(4*tp)-np.sin(4*tp)*4,np.sin(4*tp)+np.cos(4*tp)*4)  ,buff=0 ))
        cjto1=VGroup(p_parametrizacion,d_parametrizacion)
        cjto1.add_updater(mov_parametrizacion)
            
            
        #el movimiento en el number plane
        t=Dot(color=BLUE_C).move_to(number_line.number_to_point(tmin))#,UP,buff=0)#.scale(0.5)
        t_label=TextMobject("t").next_to(t,UP,buff=0.1)

        def mov_plane1(obj):
            tn = t2.get_value()
            t.become(Dot(color=BLUE_C).move_to(number_line.number_to_point(tn)))
            t_label.become(TextMobject("t").next_to(t,UP,buff=0.1))
            
        cjto1_1=VGroup(t,t_label)
        cjto1_1.add_updater(mov_plane1)

#Derivada para la reparametrización  
        t1 = ValueTracker(-vs)
        n=0.6#reescalamentiento de la derivada
        p_reparametrizacion = Sphere(radius=0.1,color=RED,fill_opacity=1).move_to([-(-vs)**3,np.cos(-4*(-vs)**3),np.sin(-4*(-vs)**3)])
        d_reparametrizacion=Arrow( (-(-vs)**3,np.cos(-4*(-vs)**3),np.sin(-4*(-vs)**3)),(-(-vs)**3-3*(-vs)**2*n,np.cos(-4*(-vs)**3)-np.sin(-4*(-vs)**3)*(-12*(-vs)**2)*n,np.sin(-4*(-vs)**3)+np.cos(-4*(-vs)**3)*(-12*(-vs)**2)*n),buff=0 )

        
        def mov_reparametrizacion(obj):
            s = t1.get_value()
            p_reparametrizacion.become(Sphere(radius=0.1,color=RED,fill_opacity=1).move_to([-s**3,np.cos(-4*s**3),np.sin(-4*s**3)]))
            d_reparametrizacion.become(Arrow( (-s**3,np.cos(-4*s**3),np.sin(-4*s**3)),(-s**3-3*s**2*n,np.cos(-4*s**3)-np.sin(-4*s**3)*(-12*s**2)*n,np.sin(-4*s**3)+np.cos(-4*s**3)*(-12*s**2)*n),buff=0 ))
 
        cjto2=VGroup(p_reparametrizacion,d_reparametrizacion)
        cjto2.add_updater(mov_reparametrizacion)

        sp=Dot(color=BLUE_C).move_to(number_line3.number_to_point((-vs)))#,UP,buff=0)#.scale(0.5)
        sp_label=TextMobject("s").next_to(sp,UP,buff=0.1)

        def move_plane2(obj):
            sn = t1.get_value()
            sp.become(Dot(color=BLUE_C).move_to(number_line3.number_to_point(sn)))#,UP,buff=0)#.scale(0.5)
            sp_label.become(TextMobject("s").next_to(sp,UP,buff=0.1))
        cjto2_1=VGroup(sp,sp_label)
        cjto2_1.add_updater(move_plane2)

        self.set_camera_orientation(0.8*np.pi/2, -0.25*np.pi,distance=20)           
        self.play(ShowCreation(axes))
        self.play(ShowCreation(g))
        self.add_fixed_in_frame_mobjects(text15)
        self.play(Write(text15))
        self.wait(3)
        #Parte para la derivada de la parametrización
        self.add_fixed_in_frame_mobjects(number_line)
        self.add_fixed_in_frame_mobjects(cjto1_1)
        self.play(ShowCreation(cjto1),ShowCreation(number_line),ShowCreation(cjto1_1))
        self.play(t2.set_value, tmax,run_time=20) 
        self.wait()
        self.play(FadeOut(text15),FadeOut(cjto1),FadeOut(number_line),FadeOut(cjto1_1))
        self.add_fixed_in_frame_mobjects(text16)
        self.play(Write(text16))
        self.wait(3)
        #Movimiento para la reparametrizacion
        self.add_fixed_in_frame_mobjects(number_line3)
        self.add_fixed_in_frame_mobjects(cjto2_1)
        self.play(ShowCreation(cjto2),ShowCreation(number_line3),ShowCreation(cjto2_1))
        self.play(t1.set_value, vs,run_time=20) 
        self.wait()
        self.play(FadeOut(axes),FadeOut(cjto2),FadeOut(g),FadeOut(text16),FadeOut(number_line3),FadeOut(cjto2_1))
        #termina movimiento de la segunda reparametrizacion
        self.add_fixed_in_frame_mobjects(text12)
        self.play(Write(text12))
        self.wait(15)
        self.play(FadeOut(text12))
        self.add_fixed_in_frame_mobjects(text13)
        self.play(Write(text13))
        self.wait(7)
        self.play(FadeOut(text13))
        self.add_fixed_in_frame_mobjects(text14)
        self.play(Write(text14))
        self.wait(5)
        self.play(FadeOut(text14))
  


########################################
###### Curvas suaves y cruces ##########
########################################

#En esta animación sólo se pueden modificar los intervalos en los que se evaluan las parametrizaciones
#Sin embargo se puede aconsejar que se analice el código para crear sus propias animaciones sobre derivadas 
#O para visualizar como se dibujan las curvas dependiendo de la parametrización
 
def gota(t):
    return  [(1-np.sin(t))*np.cos(t),np.sin(t)-1,0]
def lemniscata(t):
    return  [(2)*np.cos(t),2*np.sin(2*t),0]
def abs(t):
    return  [t,np.abs(t),0]
def cicloide(t):
    return  [(t-np.sin(t)),(1-np.cos(t)),0]
def curva1(x):
        return  [x,x**2*np.sin(1/x)+x,0]
def curva2(t):
        return [t**3,np.exp(t),np.cos(10*t)]

class Curvas_suaves_y_cruces_1 (MovingCameraScene,Scene):
    
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

        f1 = ParametricFunction(curva1,t_min=tmin1,t_max=tmax1,color=BLUE_C)
        text4_1=TextMobject('''y $f(0)=0$. ''').scale(0.05).next_to(ref,UP,buff=0.01)        
        
        f2 = ParametricFunction(curva1,t_min=tmin2,t_max=tmax2,color=BLUE_C)
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
 
        f1 = ParametricFunction(curva2,t_min=tmin,t_max=tmax,color=RED)
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
        fabs = ParametricFunction(abs,t_min=-4,t_max=4,color=BLUE_C)
        tmin = np.pi/2
        tmax = 5*np.pi/2
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
        #derivada_gota=Arrow(((1-np.sin(si))*np.cos(si),np.sin(si)-1,0),((1-np.sin(si))*np.cos(si)+np.sin(si)**2-np.cos(si)**2,np.cos(si)+np.sin(si)-1,0),buff=0)#.shift(d,buff=0)
        punto_gota = Dot(color=RED,fill_opacity=1).move_to([(1-np.sin(si))*np.cos(si),np.sin(si)-1,0])
        def Dgota(obj):
            s = s1_1.get_value()
            x=np.array([(1-np.sin(s))*np.cos(s),np.sin(s)-1,0])
            punto_gota.become(Dot(color=RED,fill_opacity=1).move_to(x))
        #para mover el punto
        punto_gota.add_updater(Dgota)

        #Para generar el movimiento de la derivada
        s1_2=ValueTracker(tmin)
        derivada_gota=Arrow(((1-np.sin(si))*np.cos(si),np.sin(si)-1,0),((1-np.sin(si))*np.cos(si)+np.sin(si)**2-np.cos(si)**2,np.cos(si)+np.sin(si)-1,0),buff=0)#.shift(d,buff=0)
        punto_gota1 = Dot(color=RED,fill_opacity=1).move_to([(1-np.sin(si))*np.cos(si),np.sin(si)-1,0])
        def Dgota(obj):
            s = s1_2.get_value()
            x=np.array([(1-np.sin(s))*np.cos(s),np.sin(s)-1,0])
            punto_gota1.become(Dot(color=RED,fill_opacity=1).move_to(x))
            derivada_gota.become(Arrow(((1-np.sin(s))*np.cos(s),np.sin(s)-1,0),((1-np.sin(s))*np.cos(s)+np.sin(s)**2-np.cos(s)**2,np.cos(s)+np.sin(s)-1,0),buff=0))#.shift(d,buff=0)
        #mover el vector
        derivada_gota.add_updater(Dgota)
        #para mover el punto
        punto_gota1.add_updater(Dgota)



        #Para la lemniscata    
        s2=ValueTracker(tmin1)
        sg=tmin1
        derivada_lem=Arrow([2*np.cos(sg),2*np.sin(2*sg),0],[-2*np.sin(sg)+2*np.cos(sg),4*np.cos(2*sg)+2*np.sin(2*sg),0],buff=0)#.move_to(d)#.get_center()+*0.2*UP+s*0.2*RIGHT)
        punto_lem=Dot(radius=0.1,color=RED,fill_opacity=1).move_to([2*np.cos(sg),2*np.sin(2*sg),0])

        def Dlemniscata(obj):
            sg1 = s2.get_value()
            xg=[2*np.cos(sg1),2*np.sin(2*sg1),0]
            punto_lem.become(Dot(radius=0.1,color=RED,fill_opacity=1).move_to(xg))
            derivada_lem.become(Arrow([2*np.cos(sg1),2*np.sin(2*sg1),0],[-2*np.sin(sg1)+2*np.cos(sg1),4*np.cos(2*sg1)+2*np.sin(2*sg1),0],buff=0))#.move_to(d)#.get_center()+*0.2*UP+s*0.2*RIGHT)
    
        derivada_lem.add_updater(Dlemniscata)
        punto_lem.add_updater(Dlemniscata)
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
        self.play(ShowCreation(punto_gota))
        self.play(s1_1.set_value, tmax,run_time=10)
        self.wait()
        #Termina movimiento de partícula en la gota
        self.play(FadeOut(text20),FadeOut(punto_gota))
        self.play(Write(text21))
        self.wait(8)
        #Animación del vector tangente
        self.play(ShowCreation(punto_gota1),ShowCreation(derivada_gota))
        self.play(s1_2.set_value, tmax-0.1,run_time=10)
        self.wait()
        ###
        self.play(FadeOut(text21),FadeOut(axes),FadeOut(fgota),FadeOut(punto_gota1),FadeOut(derivada_gota))
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
        self.play(ShowCreation(punto_lem),ShowCreation(derivada_lem))
        self.play(s2.set_value, tmax1,run_time=10)
        self.play(Restore(self.camera_frame))
        self.play(Write(text29))
        self.wait(5.7)
        self.play(FadeOut(text29),FadeOut(axes),FadeOut(flemniscata),FadeOut(punto_lem),FadeOut(derivada_lem))
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
        
######################################################
##### Curvas rectificables ###########################
######################################################

#-------------Fuciones auxiliares para la función partición_círculo-------------
def set_angs():
    return [0, 1*2*np.pi/3.0, 2*2*np.pi/3.0, 3*2*np.pi/3.0]
def partir(angulos,j):
    left = 0
    right = left+1
    for iteracion in range(1,j):
        index = 2*iteracion-1
        angulos.insert(index,(angulos[left]+angulos[right])/2.0)
        left = 2*iteracion
        right = left+1
    return angulos
#-------------Fución utilizada en la clase Curvas_Rectificables-----------------
def particion_circulo(n):
    '''
    INPUT:
        Esta función recibe el número de puntos, n, que se le agregan a la 
    partición inicial [0, 1*2*np.pi/3.0, 2*2*np.pi/3.0, 3*2*np.pi/3.0]. De manera
    que al círculo se le van agragando puntos al círculo en sentido antihorario.
    n es un entero que va de [0,21], pero se puede generalizar a más puntos.

    OUTPUT:
        Devuelve la partición en forma de un array
    
    No modificar los valores aquí dados, a menos que se necesite generalizar el
    algoritmo.
    '''
    angs = set_angs()
    for num_puntos in range(n+1):
        for i in range(1,num_puntos+2):
            if num_puntos<=3:
                angs = set_angs()
                angs = partir(angs, i)
            elif 3<num_puntos<=9:
                angs = set_angs()
                angs = partir(angs, 4)
                angs = partir(angs, i-3)
            elif 9<num_puntos<=21:
                angs = set_angs()
                angs = partir(angs, 4)
                angs = partir(angs, 7)
                angs = partir(angs, i-9)
    return angs

class Curvas_Rectificables(GraphScene,Scene):
    def setup(self):
        Scene.setup(self)
        GraphScene.setup(self)
    def FadeOutWrite(self,objeto1,objeto2):
        self.play(FadeOut(objeto1))
        self.play(Write(objeto2))
    ###### la función particiones lo que hace es generar particiones, puntos de evaluación, poligonales, puntos en el diagrama de longitud y corre las animaciones correspondientes.
    def particiones(self):
        numberline_1 = NumberLine(x_min=0,x_max=2*PI+1,unit_size=0.75).move_to(2.8*LEFT+3*DOWN)
        distancias_poligonales_2 =[]
        arrow = Arrow((-1.2,1,0),(0.0,1,0)).set_color(RED)

        dot_4 = Dot(color=RED,radius=0.05).move_to((1.5,-2+0.40,0))
        dist_4 = TexMobject(r"d(\mathcal{P})=7.79").move_to((-0.8,1.5,0)).scale(0.7).set_color(RED_E)

        dot_5 = Dot(color=RED,radius=0.05).move_to((2,-2+1.40,0))
        dist_5 = TexMobject(r"d(\mathcal{P}')=8.19").move_to((-0.8,1.5,0)).scale(0.7).set_color(RED_E)

        dot_6 = Dot(color=RED,radius=0.05).move_to((2.5,-2+2.4,0))
        dist_6 = TexMobject(r"d(\mathcal{P}')=8.59").move_to((-0.8,1.5,0)).scale(0.7).set_color(RED_E)

        dot_7 = Dot(color=RED,radius=0.05).move_to((3,-2+3.2,0))
        dist_7 = TexMobject(r"d(\mathcal{P}')=9.0").move_to((-0.8,1.5,0)).scale(0.7).set_color(RED_E)

        dot_8 = Dot(color=RED,radius=0.05).move_to((3.5,-2+3.40,0))
        dist_8 = TexMobject(r"d(\mathcal{P}')=9.05").move_to((-0.8,1.5,0)).scale(0.7).set_color(RED_E)

        dot_9 = Dot(color=RED,radius=0.05).move_to((4,-2+3.55,0))
        dist_9 = TexMobject(r"d(\mathcal{P}')=9.10").move_to((-0.8,1.5,0)).scale(0.7).set_color(RED_E)

        dot_10 = Dot(color=RED,radius=0.05).move_to((4.5,-2+3.70,0))
        dist_10 = TexMobject(r"d(\mathcal{P}')=9.15").move_to((-0.8,1.5,0)).scale(0.7).set_color(RED_E)

        dot_11 = Dot(color=RED,radius=0.05).move_to((5,-2+3.80,0))
        dist_11 = TexMobject(r"d(\mathcal{P}')=9.21").move_to((-0.8,1.5,0)).scale(0.7).set_color(RED_E)

        dot_12 = Dot(color=RED,radius=0.05).move_to((5.5,-2+3.90,0))
        dist_12 = TexMobject(r"d(\mathcal{P}')=9.26").move_to((-0.8,1.5,0)).scale(0.7).set_color(RED_E)

        dot_13 = Dot(color=RED,radius=0.05).move_to((6,-2+4.0,0))
        dist_13 = TexMobject(r"d(\mathcal{P}')=9.31").move_to((-0.8,1.5,0)).scale(0.7).set_color(RED_E)

        dots = [dot_4, dot_5, dot_6, dot_7, dot_8, dot_9, dot_10, dot_11, dot_12, dot_13]
        dists = [dist_4, dist_5, dist_6, dist_7, dist_8, dist_9, dist_10, dist_11, dist_12, dist_13]
        Grupo_1 = VGroup(Dot(radius=0).move_to(3*LEFT))

        for j in range(10):
            
            conj_puntos_particion = []
            conj_evaluacion_particion = []
            conj_poligonal_particion = []
            suma_distancias = 0

            particion = particion_circulo(j)
            for i in range(len(particion)):
                punto_dom = Dot().move_to(numberline_1.get_left()+particion[i]*0.75*RIGHT)
                conj_puntos_particion.append(punto_dom)
                punto_eval = Dot().move_to((1.5*np.cos(particion[i])-3,1.5*np.sin(particion[i]),0))
                conj_evaluacion_particion.append(punto_eval)
                if i<(len(particion)-1):
                    linea_poligonal = Line((1.5*np.cos(particion[i])-3,1.5*np.sin(particion[i]),0),(1.5*np.cos(particion[i+1])-3,1.5*np.sin(particion[i+1]),0))
                    conj_poligonal_particion.append(linea_poligonal)
                    suma_distancias += np.linalg.norm(np.array((1.5*np.cos(particion[i])-3,1.5*np.sin(particion[i]),0))-\
                                                    np.array((1.5*np.cos(particion[i+1])-3,1.5*np.sin(particion[i+1]),0)))
        ####Conjuntos con elementos
            puntos_particion = VGroup(*conj_puntos_particion)
            puntos_evaluacion_particion = VGroup(*conj_evaluacion_particion)
            poligonal_particion = VGroup(*conj_poligonal_particion)
            distancias_poligonales_2.append(suma_distancias)

        ####Animaciones con poligonal
            focus_poligonal_1 = []
            for i in range(0,len(poligonal_particion)):
                focus_poligonal_1.append(FadeToColor(poligonal_particion[i],RED,rate_func=there_and_back))
            focus_poligonal_2 = []
            for i in range(0,len(poligonal_particion)):
                focus_poligonal_2.append(FadeToColor(poligonal_particion[i],RED,rate_func=there_and_back))
        ####Ejecución de Animaciones        
            Grupo = VGroup(puntos_particion,puntos_evaluacion_particion,poligonal_particion)
            self.play(ReplacementTransform(Grupo_1,Grupo))
            
            self.play(ShowCreation(arrow))
            self.play(FadeIn(dots[j]),FadeIn(dists[j]))
            self.play(FadeOut(dists[j]))

            Grupo_1 = VGroup(puntos_particion,puntos_evaluacion_particion,poligonal_particion)
            self.play(LaggedStart(*focus_poligonal_2),run_time=2)
        self.play(FadeOut(arrow))
    CONFIG = {
        "x_min": -2,
        "x_max": 2,
        "x_axis_width": 4,
        "x_tick_frequency": 0.5,
        "x_leftmost_tick": None,  # Change if different from x_min
        "x_labeled_nums": [],
        "x_axis_label": "$x$",
        "y_min": -2,
        "y_max": 2,
        "y_axis_height": 4,
        "y_tick_frequency": 0.5,
        "y_bottom_tick": None,  # Change if different from y_min
        "y_labeled_nums": [],
        "y_axis_label": "$y$",
        "axes_color": BLUE,
        "graph_origin": 3*LEFT,
        "exclude_zero_label": True,
        "default_graph_colors": [BLUE, GREEN, YELLOW],
        "default_derivative_color": GREEN,
        "default_input_color": YELLOW,
        "default_riemann_start_color": BLUE,
        "default_riemann_end_color": GREEN,
        "area_opacity": 0.8,
        "num_rects": 50,
    }
    def construct(self):
        ####TEXTOS
        titulo = TextMobject("Curvas Rectificables").scale(1.5)
        text_1 = TextMobject('''Sea $\\gamma$ una curva en $\\mathbb{R}^n$\n
                                $\\gamma: A\\subset\\mathbb{R}\\rightarrow\\mathbb{R}^n$''')
        text_2 = TextMobject('''Como ejemplo, tomemos la curva \n
                                $\\gamma : A=[0,2\\pi]\\rightarrow\\mathbb{R}^2$ \n
                             $\\gamma(t)=\\dfrac{3}{2}(\\cos{(t)},\\sin{(t)})$''')
        funcion_1 = TextMobject('''$\\gamma : A=[0,2\\pi]\\rightarrow\\mathbb{R}^2$\n
                                    $\\gamma(t)=\\dfrac{3}{2}(\\cos{(t)},\\sin{(t)})$''').set_color(YELLOW).scale(0.6).move_to(5.3*LEFT+1.9*UP)
        text_3 = TextMobject('''El dominio de la curva $\\gamma$ es el intervalo $A=[a,b]=[0,2\\pi]\\subset \\mathbb{R}$ ''').move_to(3*UP)
        text_4 = TextMobject('''Definimos una partición $\\mathcal{S}$ de $A$ como ''').move_to(3*UP)
        text_5 = TexMobject(r'''\mathcal{S}:=\{a = t_0, t_1, t_2, ... , t_m = b\}\subset A ''').move_to(3*UP)
        text_6 = TextMobject('''En el ejemplo, sea $\\mathcal{S}:=\\{0 = t_0, t_1, t_2, t_3 = 2\\pi\\}$ ''').move_to(3*UP)
        text_7 = TextMobject('''Como $\\mathcal{S}\subset A$, entonces podemos definir la \n 
                                siguiente sucesión finita de puntos del contradominio de $\\gamma$''').move_to(3.2*UP)
        text_8 = TexMobject(r'''\gamma_{\mathcal{S}}:=\{ \gamma (a)=\gamma (t_0), \gamma (t_1), \gamma (t_2), ..., \gamma (b)=\gamma (t_m) \} ''').move_to(3*UP)
        text_9 = TextMobject("Obsérvese que en el ejemplo, $\\gamma(t_0)=\\gamma(t_m)$").move_to(3*UP)
        text_10 = TextMobject('''A partir de $\gamma_{\mathcal{S}}$ se define una poligonal\n
                                 $\\mathcal{P}$ con vértices en cada punto de $\\gamma_{\\mathcal{S}}$''').move_to(3.2*UP)
        text_11 = TextMobject('''La longitud $d(\\mathcal{P})$ de la poligonal se define\n
                                     como la suma de cada segmento de recta:''').move_to(3.2*UP)
        text_12 = TexMobject(r'''d(\mathcal{P})=\sum_{i=1}^m \left\Vert \gamma(t_i)-\gamma(t_{i-1}) \right\Vert''').move_to(3.2*UP)
        text_12_1 = TextMobject('''En el ejemplo, para esta partición, $d(\\mathcal{P})=7.79$ ''').move_to(3.2*UP)
        text_13 = TextMobject('''Consideremos un refinamiento $\\mathcal{S}'$ de la partición $\\mathcal{S}$  ''').move_to(3.2*UP)
        text_14 = TextMobject('''A partir de $\\mathcal{S}'$ definimos otra poligonal $\\mathcal{P}'$ ''').move_to(3.2*UP)
        text_15 = TextMobject(''' Por ser $\\mathcal{P}'$ refinamiento de $\mathcal{P}$, $d(\mathcal{P}')\geq d(\mathcal{P})$''').move_to(3.2*UP)
        text_15_1 = TextMobject(''' En el ejemplo, para esta partición, $d(\\mathcal{P}')=8.19$''').move_to(3.2*UP)
        text_16_1 = TextMobject("Consideremos el conjunto").move_to(3.6*UP)
        text_16_2 = TextMobject("$L:=\\{ d(\\mathcal{P}) | \\text{$\\mathcal{P}$ es una poligonal sobre $\\gamma$} \}$").move_to(2.9*UP)
        text_16 = VGroup(text_16_1,text_16_2)
        text_17 = TextMobject('''Decimos que $\\gamma$ es una curva rectificable\n
                                 si $L$ es un conjunto acotado superiormente ''').move_to(3.2*UP)
        text_18 = TextMobject(''' Además, $\\text{sup}(L)= \\text{ longitud de curva $\\gamma$}$''').move_to(3.2*UP)
        text_18_0 = TextMobject(''' Para curvas suaves, $\\text{sup}(L)=\\displaystyle\\int_{a}^{b}\\left\\Vert \\gamma'(t) \\right\\Vert dt$''').move_to(3.2*UP)
        text_18_1 = TextMobject("En el ejemplo, $\\text{sup}(L)=3\\pi$").move_to(3.2*UP)
        text_19 = TextMobject(''' En general, una curva en $\\mathbb{R}^n$,  $\\gamma: A\\subset\\mathbb{R}\\rightarrow\\mathbb{R}^n$\n
                                 es rectificable si $\\forall$  $a,b\\in A, a<b$, \n
                                $\\gamma$ es rectificable en $[a,b]$''')
        ###OBJETOS

        #Función
        curva_1 = ParametricFunction(
                lambda u : np.array([
                1.5*math.cos(u),
                1.5*math.sin(u),
                0
            ]),color=YELLOW,t_min=0,t_max=2*PI,
            ).move_to(3*LEFT)
        
        
        #Numberline de Dominio
        numberline_1 = NumberLine(x_min=0,x_max=2*PI+1,unit_size=0.75, tick_frequency=PI/2,
                                include_tip=True,number_scale_val=0.6,numbers_with_elongated_ticks=[0,2*PI],lable_direction=1.2*DOWN).move_to(2.8*LEFT+3*DOWN).set_color(BLUE)
        etiqueta_numberline_1 = TexMobject(r"t").move_to(numberline_1.get_right()+0.4*UP)
        etiqueta_numberline_2 = TexMobject(r"2\pi").move_to(numberline_1.get_right()+0.4*DOWN+0.75*LEFT)
        etiqueta_numberline_3 = TexMobject(r"0").move_to(numberline_1.get_left()+0.4*DOWN)
        etiqueta_numberline_4 = TexMobject(r"\pi").move_to(numberline_1.get_center()+0.4*DOWN+0.4*LEFT)
        etiquetas_numberline = VGroup(etiqueta_numberline_1,etiqueta_numberline_2,etiqueta_numberline_3,etiqueta_numberline_4)
        
        ##########Particiones, Evaluaciones y poligonal con 4 elementos#########
        ####En esta función se generan los puntos de la partición en el dominio, puntos de evaluación, sus poligonales y puntos en diagrama de longitudes para la partición de 4 elementos
        #### La razón por la que este caso no se trató con la función particiones(), es que con estos conjuntos se aplicarán otras animaciones, así como textos particulares
        distancias_poligonales_1 =[]

        conj_puntos_particion_1 = []
        conj_evaluacion_particion_1 = []
        conj_poligonal_particion_1 = []
        suma_distancias_1 = 0

        particion = particion_circulo(0) ##Se añadirán cero puntos al triángulo inscrito
        for i in range(len(particion)):
            punto_dom = Dot().move_to(numberline_1.get_left()+particion[i]*0.75*RIGHT)
            conj_puntos_particion_1.append(punto_dom)
            punto_eval = Dot().move_to((1.5*np.cos(particion[i])-3,1.5*np.sin(particion[i]),0))
            conj_evaluacion_particion_1.append(punto_eval)
            if i<(len(particion)-1):
                linea_poligonal = Line((1.5*np.cos(particion[i])-3,1.5*np.sin(particion[i]),0),(1.5*np.cos(particion[i+1])-3,1.5*np.sin(particion[i+1]),0))
                conj_poligonal_particion_1.append(linea_poligonal)
                suma_distancias_1 += np.linalg.norm(np.array((1.5*np.cos(particion[i])-3,1.5*np.sin(particion[i]),0))-\
                                                    np.array((1.5*np.cos(particion[i+1])-3,1.5*np.sin(particion[i+1]),0)))
        ####Conjuntos con elementos
        puntos_particion_1 = VGroup(*conj_puntos_particion_1)
        puntos_evaluacion_particion_1 = VGroup(*conj_evaluacion_particion_1)
        poligonal_particion_1 = VGroup(*conj_poligonal_particion_1)
        distancias_poligonales_1.append(suma_distancias_1)
        
        ####Animaciones con poligonal
        focus_poligonal_1_1 = []
        for i in range(0,len(conj_poligonal_particion_1)):
            focus_poligonal_1_1.append(FadeToColor(poligonal_particion_1[i],RED,rate_func=there_and_back))
        focus_poligonal_1_2 = []
        for i in range(0,len(conj_poligonal_particion_1)):
            focus_poligonal_1_2.append(FadeToColor(poligonal_particion_1[i],RED,rate_func=there_and_back))

        ##########Particiones, Evaluaciones y poligonal con 5 elementos#########
        ####En esta función se generan los puntos de la partición en el dominio, puntos de evaluación, sus poligonales y puntos en diagrama de longitudes para la partición de 5 elementos
        #### La razón por la que este caso no se trató con la función particiones(), es que con estos conjuntos se aplicarán otras animaciones, así como textos particulares
        conj_puntos_particion_2 = []
        conj_evaluacion_particion_2 = []
        conj_poligonal_particion_2 = []
        suma_distancias_2 = 0

        particion = particion_circulo(1) ##Se añadirán cero puntos al triángulo inscrito
        for i in range(len(particion)):
            punto_dom = Dot().move_to(numberline_1.get_left()+particion[i]*0.75*RIGHT)
            conj_puntos_particion_2.append(punto_dom)
            punto_eval = Dot().move_to((1.5*np.cos(particion[i])-3,1.5*np.sin(particion[i]),0))
            conj_evaluacion_particion_2.append(punto_eval)
            if i<(len(particion)-1):
                linea_poligonal = Line((1.5*np.cos(particion[i])-3,1.5*np.sin(particion[i]),0),(1.5*np.cos(particion[i+1])-3,1.5*np.sin(particion[i+1]),0))
                conj_poligonal_particion_2.append(linea_poligonal)
                suma_distancias_2 += np.linalg.norm(np.array((1.5*np.cos(particion[i])-3,1.5*np.sin(particion[i]),0))-\
                                                    np.array((1.5*np.cos(particion[i+1])-3,1.5*np.sin(particion[i+1]),0)))
        ####Conjuntos con elementos
        puntos_particion_2 = VGroup(*conj_puntos_particion_2)
        puntos_evaluacion_particion_2 = VGroup(*conj_evaluacion_particion_2)
        poligonal_particion_2 = VGroup(*conj_poligonal_particion_2)
        poligonal_particion_2_copy = poligonal_particion_2.copy()
        distancias_poligonales_1.append(suma_distancias_2)
        
        ####Animaciones con poligonal
        focus_poligonal_2_1 = []
        for i in range(0,len(conj_poligonal_particion_1)):
            focus_poligonal_1_1.append(FadeToColor(poligonal_particion_1[i],RED,rate_func=there_and_back))
        focus_poligonal_2_2 = []
        for i in range(0,len(conj_poligonal_particion_1)):
            focus_poligonal_1_2.append(FadeToColor(poligonal_particion_1[i],RED,rate_func=there_and_back))
               
        #### Diagrama de distancias
        #### Los labels y líneas fueron creados aquí mismo con iteraciones for
        EjeY_1 = Arrow(start = (-1,-1,0), end = (-1,4.8,0), stroke_width = 2).set_color(BLUE)
        EjeX_1 = Arrow(start = (-2,0,0), end = (5.0,0,0), stroke_width = 2).set_color(BLUE)
        label_x = TextMobject("Elementos de Partición $\\mathcal{P}$").shift(1.75*RIGHT+0.75*DOWN).scale(0.5)
        label_y = TextMobject("$d(\\mathcal{P})$").move_to(1.75*UP+2.0*LEFT).rotate_in_place(90*DEGREES).scale(0.5)
        etiquetas_eje_x = []
        for i in range(4,14):
            line_x = Line((0.5+0.5*(i-4)-1,-0.05,0),(0.5+0.5*(i-4)-1,0.05,0))
            lable_line_x = TexMobject(round(i,2)).move_to(line_x.get_bottom()+0.25*DOWN).scale(0.6)
            both_1 = VGroup(line_x,lable_line_x)
            etiquetas_eje_x.append(both_1)
        etiquetas_eje_y = []
        for i in range(4,12):
            line_y = Line((-0.05-1,0.2+0.5*(i-4),0),(0.05-1,0.2+0.5*(i-4),0))
            label_line_y = TexMobject(round(7.7+(i-4)*0.2,3)).scale(0.6).move_to(line_y.get_left()+0.35*LEFT)
            both_2 = VGroup(line_y,label_line_y)
            etiquetas_eje_y.append(both_2)
        line_3pi = Line((2-1-0.05,-0.6+0.5*(9.5-4),0),(2-1+0.05,-0.6+0.5*(9.5-4),0))
        label_line_3pi = TexMobject(r"3\pi").scale(0.8).move_to(line_3pi.get_left()+0.4*LEFT+0.1*UP).set_color(YELLOW)
        Ejes_1 = VGroup(EjeX_1, EjeY_1,label_x,label_y,*etiquetas_eje_x,*etiquetas_eje_y).shift(2*RIGHT+2*DOWN)
        recta_3pi = Line((2-1,-0.6+0.5*(9.5-4),0),(6, -0.6+0.5*(9.5-4),0)).set_color(YELLOW)
        ###Puntos en diagrama
        arrow = Arrow((-1.2,1,0),(0.0,1,0)).set_color(RED)
        dot_1 = Dot(color=RED,radius=0.05).move_to((2.5-1,-2.0+0.40,0))
        dist_1 = TexMobject(r"d(\mathcal{P})=7.79").move_to((-0.8,1.5,0)).scale(0.7).set_color(RED_E)
        dot_2 = Dot(color=RED,radius=0.05).move_to((3-1,-2+1.40,0))
        dist_2 = TexMobject(r"d(\mathcal{P}')=8.19").move_to((-0.8,1.5,0)).scale(0.7).set_color(RED_E)
        
        ####ANIMACIONES
        self.play(Write(titulo))
        self.wait(2.75)
        self.FadeOutWrite(titulo,text_1)
        self.wait(6.875)
        self.FadeOutWrite(text_1,text_2)
        self.wait(10)
        self.play(ReplacementTransform(text_2,funcion_1))
        self.setup_axes(animate=True)
        self.wait()
        self.play(ShowCreation(curva_1))
        self.wait()
        self.play(Write(text_3))
        self.wait(9.5)
        self.play(ShowCreation(numberline_1))
        self.play(FadeIn(etiquetas_numberline))
        self.wait()
        self.FadeOutWrite(text_3,text_4)
        self.wait(4.5)
        self.FadeOutWrite(text_4,text_5)
        self.wait(6.9)
        self.FadeOutWrite(text_5,text_6)
        self.play(FadeIn(puntos_particion_1))
        self.wait(3)
        self.FadeOutWrite(text_6,text_7)
        self.wait(7.25)
        self.FadeOutWrite(text_7,text_8)
        self.wait(8.3)
        self.play(Write(puntos_evaluacion_particion_1))
        self.FadeOutWrite(text_8,text_9)
        self.wait(7.6)
        self.FadeOutWrite(text_9,text_10)
        self.wait(5.75)
        self.play(Write(poligonal_particion_1),run_time=3)
        self.FadeOutWrite(text_10,text_11)
        self.wait(7.6)
        self.play(Succession(*focus_poligonal_1_1),run_time=3) ##LINEA 11
        self.FadeOutWrite(text_11,text_12)
        self.wait(7.25)
        self.play(Write(Ejes_1),run_time=3)
        self.wait(6.5)
        self.FadeOutWrite(text_12,text_12_1)
        self.wait(5.3)
        self.play(LaggedStart(*focus_poligonal_1_2),run_time=2) ##LINEA 12
        self.play(ShowCreation(arrow))
        self.play(FadeIn(dot_1),FadeIn(dist_1))
        self.wait(0.5)
        self.play(LaggedStart(*focus_poligonal_1_2),run_time=2) ##LINEA 12
        self.play(FadeOut(dist_1))
        self.play(FadeOut(arrow))
        self.play(FadeOut(poligonal_particion_1))
        self.FadeOutWrite(text_12_1,text_13)
        self.wait(5.3)
        self.play(ReplacementTransform(puntos_particion_1,puntos_particion_2))
        self.wait(0.5)
        self.play(ReplacementTransform(puntos_evaluacion_particion_1,puntos_evaluacion_particion_2))
        self.FadeOutWrite(text_13,text_14)
        self.wait(5.3)
        self.play(Write(poligonal_particion_2),run_time=3)
        self.FadeOutWrite(text_14,text_15)
        self.wait(5.7)
        self.play(ReplacementTransform(poligonal_particion_2,poligonal_particion_1))
        self.play(ReplacementTransform(poligonal_particion_1,poligonal_particion_2_copy))
        self.FadeOutWrite(text_15,text_15_1)
        self.wait(5.7)
        self.play(LaggedStart(*focus_poligonal_2_2),run_time=2) ##LINEA 12
        self.play(ShowCreation(arrow))
        self.play(FadeIn(dot_2),FadeIn(dist_2))
        self.wait(2)
        self.play(FadeOut(dist_2))
        self.play(FadeOut(arrow))
        self.play(FadeOut(puntos_particion_2),FadeOut(puntos_evaluacion_particion_2),FadeOut(poligonal_particion_2_copy))
        self.FadeOutWrite(text_15_1,text_16)
        self.wait(6.8)
        self.play(FadeOut(text_16_1))
        self.play(ShowCreation(arrow))
        self.particiones()
        self.play(FadeOut(arrow))
        self.FadeOutWrite(text_16_2,text_17)
        self.wait(8)
        self.play(ShowCreation(recta_3pi))
        self.FadeOutWrite(text_17,text_18)
        self.wait(5)
        self.FadeOutWrite(text_18,text_18_0)
        self.wait(10)
        self.FadeOutWrite(text_18_0,text_18_1)
        self.wait(4.6)
        self.play(Write(line_3pi))
        self.play(Write(label_line_3pi))
        self.wait(2)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
        self.play(Write(text_19))
        self.wait(13)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )



######################################################
##### Curvas no rectificables ########################
######################################################
#### Falta agregar el caso del fractal
class Curvas_No_Rectificables(GraphScene,Scene):
    def setup(self):
        Scene.setup(self)
        GraphScene.setup(self)
    def FadeOutWrite(self,objeto1,objeto2):
        self.play(FadeOut(objeto1))
        self.play(Write(objeto2))
    def particiones(self):
        Grupo_1 = Dot(radius=0)
        numberline_1 = NumberLine(x_min=0,x_max=(2/PI)+0.127,unit_size=6, tick_frequency=(2/(5*PI)),
                                include_tip=True,number_scale_val=0.6,numbers_with_elongated_ticks=[0,2/PI]).move_to(3.5*RIGHT+0.7*DOWN).set_color(BLUE)
        for j in range(4,12):
            conj_puntos_particion = []
            conj_evaluacion_particion = []
            conj_poligonal_particion = []

            for i in range(0,j-1):
                punto_dom = Dot(radius=0.05).move_to(numberline_1.get_left()+(1/(PI*(0.5+i)))*6*RIGHT)
                conj_puntos_particion.append(punto_dom)
                punto_eval = Dot(radius=0.05).move_to(((1/(PI*(0.5+i)))*4-4.5,1.5*math.sin((PI*(0.5+i)))-0.7,0))
                conj_evaluacion_particion.append(punto_eval)
                if (i<j-2):
                    linea_poligonal = Line(((1/(PI*(0.5+i)))*4-4.5,1.5*math.sin((PI*(0.5+i)))-0.7,0),((1/(PI*(0.5+i+1)))*4-4.5,1.5*math.sin((PI*(0.5+i+1)))-0.7,0))
                    conj_poligonal_particion.append(linea_poligonal)
            
            ##### Primer elemento de la partición
            punto_dom = Dot(radius=0.05).move_to(numberline_1.get_left())
            conj_puntos_particion.append(punto_dom)
            punto_eval = Dot(radius=0.05).move_to(((-4.5,-0.7,0)))
            conj_evaluacion_particion.append(punto_eval)
            linea_poligonal = Line(((1/(PI*(0.5+j-2)))*4-4.5,1.5*math.sin((PI*(0.5+j-2)))-0.7,0),(-4.5,-0.7,0))
            conj_poligonal_particion.append(linea_poligonal)

            ####Conjuntos con elementos
            puntos_particion = VGroup(*conj_puntos_particion)
            puntos_evaluacion_particion = VGroup(*conj_evaluacion_particion)
            poligonal_particion = VGroup(*conj_poligonal_particion)

            ####Animaciones con poligonal
            focus_poligonal = []
            for i in range(0,j-1):
                focus_poligonal.append(FadeToColor(poligonal_particion[i],RED,rate_func=there_and_back))

            Grupo = VGroup(puntos_particion,puntos_evaluacion_particion)
            self.play(ShowCreation(Grupo))
            
            Grupo_1 = VGroup(puntos_evaluacion_particion,poligonal_particion)
            self.play(LaggedStart(*focus_poligonal),run_time=2.0)
            self.play(FadeOut(Grupo_1))
            
    CONFIG = {
        "x_min": -0.25,
        "x_max": 1,
        "x_axis_width": 5,
        "x_tick_frequency": 10,
        "x_leftmost_tick": None,  # Change if different from x_min
        "x_labeled_nums": [],
        "x_axis_label": "$x$",
        "y_min": -1.5,
        "y_max": 1.5,
        "y_axis_height": 3*1.5,
        "y_tick_frequency": 0.5,
        "y_bottom_tick": None,  # Change if different from y_min
        "y_labeled_nums": [-1,1],
        "y_axis_label": "$y$",
        "axes_color": BLUE,
        "graph_origin": 4.5*LEFT+0.7*DOWN,
        "exclude_zero_label": True,
        "default_graph_colors": [BLUE, GREEN, YELLOW],
        "default_derivative_color": GREEN,
        "default_input_color": YELLOW,
        "default_riemann_start_color": BLUE,
        "default_riemann_end_color": GREEN,
        "area_opacity": 0.8,
        "num_rects": 50,
        "num_graph_anchor_points": 30000
    }
    def construct(self):
        titulo = TextMobject("Curvas No Rectificables").scale(1.5) 
        text_1 = TextMobject('''Sea $\\sigma : [0,\\infty)\\rightarrow \\mathbb{R}^2$\n
                                $\\sigma (t)=\\left( t,\\sin{\\dfrac{1}{t}} \\right), t>0$\n
                                 $\\sigma (0)=(0,0)$''')
        funcion_1 = TexMobject(r"""\sigma (t)=\left( t,\sin{\dfrac{1}{t}} \right), t>0\\
                                \sigma (0)=(0,0)""").set_color(YELLOW).scale(0.7).move_to(2.9*DOWN)
        text_2 = TextMobject(''' En general, una curva en $\\mathbb{R}^n$,  $\\sigma: A\\subset\\mathbb{R}\\rightarrow\\mathbb{R}^n$\n
                                 es rectificable si $\\forall$  $a,b\\in A, a<b$, \n
                                $\\sigma$ es rectificable en $[a,b]$''').move_to(3*UP)
        text_3 = TextMobject("Consideremos $A=\\left[ 0,\\dfrac{2}{\\pi} \\right]$").move_to(3*UP)
        text_4 = TextMobject("Veremos que $\\sigma$ no es rectificable en $A$").move_to(3*UP)

        text_5 = TextMobject('''Sea $t_n=\\dfrac{1}{\\pi(1/2+k-n)}$, $n=1,...,k$,\n 
                                con $k\\in\\mathbb{N}$ fijo, y $t_0=0.$''').move_to(2.5*UP)
        text_5_2 = TextMobject("donde $\\sin{\\dfrac{1}{t_n}}=(-1)^{k-n}$").move_to(3*UP)
        text_5_1 = TextMobject("En el ejemplo, tomamos $k=3$").move_to(3*UP)
        text_tn = TexMobject(r"""t_n=\dfrac{1}{\pi(1/2+k-n)},\quad n=1,...,k\\
                             t_0=0""").scale(0.7).move_to(0.75*UP+3.5*RIGHT)
        text_6 = TextMobject('''Sea $\\mathcal{S}$ una partición de $A$\n 
                                $\\mathcal{S}:=\\{t_0,t_1,...,t_k\\}$''' ).move_to(3*UP)
        text_7 = TextMobject('''$\\mathcal{S}$ genera una poligonal $\\mathcal{P}$ con los puntos\n
                                 $\\sigma_{\\mathcal{P}}:=\\{ \\sigma(t_0),...,\\sigma(t_k) \\}$''').move_to(3*UP)
        text_8 = TextMobject('''Obsérvese que $\\left|\\sin\\dfrac{1}{t_n}-\\sin\\dfrac{1}{t_{n-1}}\\right|=2$, $n=2,...,k$''').move_to(3*UP)
        text_9 = TextMobject('''Entonces, $\\left\\Vert \\sigma(t_n)-\\sigma(t_{n-1}) \\right\\Vert > 2$, $n=2,...,k$''').move_to(3*UP)
        text_10 = TextMobject('''Por lo tanto, \n
                                $\\text{long}(C)>d(\\mathcal{P})=\\sum_{n=1}^{k}\\left\\Vert\\sigma(t_n)-\\sigma(t_{n-1})\\right\\Vert >\\sum_{n=2}^k 2,$\n
                                con $C=\\text{Im}(\\sigma).$''').move_to(3.0*UP)
        text_11 = TextMobject('''La serie $\\sum_{n=2}^{\\infty}2$ diverge, entonces para toda $M>0$, \n
                                podemos definir una partición $\\mathcal{P}$ de $A$,\n
                                tal que $d(\\mathcal{P})>M$. ''').move_to(2.7*UP)
        text_13 = TextMobject('''Por lo tanto, decimos que $\\sigma$ no es rectificable en $A$\n
                                y por ende no es rectificable en $(0,\\infty)$''').move_to(3*UP)
        
        ####Objetos
        
        ####Punto en dominio 2/pi
        text_punto_dom_1 = TexMobject(r"\dfrac{2}{\pi}").scale(0.7).move_to((-4.5+(2/PI)*4,-0.7-0.9,0))
        linea_punto_dom_1 = Line((-4.5+(2/PI)*4,-0.7-0.25,0),(-4.5+(2/PI)*4,-0.7+.25,0))
        punto_dom_1 = VGroup(text_punto_dom_1,linea_punto_dom_1)

        #### Recta real de particiones
        numberline_1 = NumberLine(x_min=0,x_max=(2/PI)+0.127,unit_size=6, tick_frequency=(2/(5*PI)),
                                include_tip=True,number_scale_val=0.6,numbers_with_elongated_ticks=[0,2/PI]).move_to(3.5*RIGHT+0.7*DOWN).set_color(BLUE)
        etiqueta_numberline_1 = TexMobject(r"t").move_to(numberline_1.get_right()+0.4*UP)
        etiqueta_numberline_2 = TexMobject(r"\dfrac{2}{\pi}").move_to(numberline_1.get_left()+0.7*DOWN+(2/PI)*6*RIGHT).scale(0.7)
        etiqueta_numberline_3 = TexMobject(r"0").move_to(numberline_1.get_left()+0.4*DOWN).scale(0.7)
        etiquetas_numberline = VGroup(etiqueta_numberline_1,etiqueta_numberline_2,etiqueta_numberline_3)

        ###Recta vertical de longitud 2
        recta_hor_1 = DashedLine((-4.5,-1.5-0.7,0),(-1.5,-1.5-0.7,0))
        recta_hor_2 = DashedLine((-4.5,1.5-0.7,0),(-1.5,1.5-0.7,0))
        recta_vert = DashedLine((-1.5,-1.5-0.7,0),(-1.5,1.5-0.7,0))
        rectas =  VGroup(recta_vert,recta_hor_1,recta_hor_2)

        
     
        ##########Particiones, Evaluaciones y poligonal con 4 elementos#########
        ####En esta función se generan los puntos de la partición en el dominio, puntos de evaluación, sus poligonales y puntos en diagrama de longitudes para la partición de 5 elementos
        #### La razón por la que este caso no se trató con la función particiones(), es que con estos conjuntos se aplicarán otras animaciones, así como textos particulares
        conj_puntos_particion = []
        conj_evaluacion_particion = []
        conj_poligonal_particion = []
        j = 4
        for i in range(0,j-1):
            punto_dom = Dot(radius=0.05).move_to(numberline_1.get_left()+(1/(PI*(0.5+i)))*6*RIGHT)
            conj_puntos_particion.append(punto_dom)
            punto_eval = Dot(radius=0.05).move_to(((1/(PI*(0.5+i)))*4-4.5,1.5*math.sin((PI*(0.5+i)))-0.7,0))
            conj_evaluacion_particion.append(punto_eval)
            if (i<j-2):
                linea_poligonal = Line(((1/(PI*(0.5+i)))*4-4.5,1.5*math.sin((PI*(0.5+i)))-0.7,0),((1/(PI*(0.5+i+1)))*4-4.5,1.5*math.sin((PI*(0.5+i+1)))-0.7,0))
                conj_poligonal_particion.append(linea_poligonal)
            
            ##### Primer elemento de la partición
        punto_dom = Dot(radius=0.05).move_to(numberline_1.get_left())
        conj_puntos_particion.append(punto_dom)
        punto_eval = Dot(radius=0.05).move_to(((-4.5,-0.7,0)))
        conj_evaluacion_particion.append(punto_eval)
        linea_poligonal = Line(((1/(PI*(0.5+j-2)))*4-4.5,1.5*math.sin((PI*(0.5+j-2)))-0.7,0),(-4.5,-0.7,0))
        conj_poligonal_particion.append(linea_poligonal)

        ####Conjuntos con elementos
        puntos_particion = VGroup(*conj_puntos_particion)
        puntos_evaluacion_particion = VGroup(*conj_evaluacion_particion)
        poligonal_particion = VGroup(*conj_poligonal_particion)

        ####Animaciones con poligonal
        focus_poligonal_1 = []
        for i in range(0,j-1):
            focus_poligonal_1.append(FadeToColor(poligonal_particion[i],RED,rate_func=there_and_back))
        focus_poligonal_2 = []
        for i in range(0,j-1):
            focus_poligonal_2.append(FadeToColor(poligonal_particion[i],RED,rate_func=there_and_back))

        ####Etiquetas en particion
        t_0 = TexMobject(r"t_0").scale(0.7).move_to(conj_puntos_particion[3].get_top()+0.4*UP)
        t_1 = TexMobject(r"t_1").scale(0.7).move_to(conj_puntos_particion[2].get_top()+0.4*UP)
        t_2 = TexMobject(r"t_2").scale(0.7).move_to(conj_puntos_particion[1].get_top()+0.4*UP)
        t_3 = TexMobject(r"t_3").scale(0.7).move_to(conj_puntos_particion[0].get_top()+0.4*UP)
        etiquetas_particiones = VGroup(t_0,t_1,t_2,t_3)

        ###ANIMACIONES
        self.play(Write(titulo))
        self.wait(3)
        self.FadeOutWrite(titulo,text_1)
        self.wait(13.25)
        self.play(ReplacementTransform(text_1,funcion_1))
        self.setup_axes(animate=True)
        #Función

        f = lambda x: math.sin(1/x)
        graph = self.get_graph(
            f, 
            color = YELLOW,
            x_min = 0.00005,
            x_max = 1
        )

        self.play(Write(graph),run_time=3)
        self.wait()
        self.play(Write(text_2))
        self.wait(13.75)
        self.FadeOutWrite(text_2,text_3)
        self.wait(5)
        self.play(Write(punto_dom_1))
        self.play(ShowCreation(numberline_1))
        self.play(Write(etiquetas_numberline))
        self.wait()
        self.FadeOutWrite(text_3,text_4)
        self.wait(5)
        self.FadeOutWrite(text_4,text_5)
        self.wait(11.25)
        self.play(ShowCreation(puntos_particion))
        self.play(ReplacementTransform(text_5,text_tn))
        self.play(Write(text_5_2))
        self.wait(6.875)
        self.FadeOutWrite(text_5_2,text_5_1)
        self.wait(4.6)
        self.FadeOutWrite(text_5_1,text_6)
        self.wait(6.125)
        self.play(Write(etiquetas_particiones))
        self.FadeOutWrite(text_6,text_7)
        self.wait(7.25)
        self.play(ShowCreation(puntos_evaluacion_particion))
        self.play(Write(poligonal_particion),run_time=3)
        self.play(FadeOut(graph))
        self.wait()
        self.play(FadeIn(graph))
        self.FadeOutWrite(text_7,text_8)
        self.wait(9.875)
        self.play(ShowCreation(recta_vert))
        self.play(ShowCreation(recta_hor_1))
        self.play(ShowCreation(recta_hor_2))
        self.FadeOutWrite(text_8,text_9)
        self.wait(15.5)
        self.play(Succession(*focus_poligonal_2),run_time=3)
        self.FadeOutWrite(text_9,text_10)
        self.wait(12.5)
        self.play(LaggedStart(*focus_poligonal_1),run_time=3)
        self.wait()
        self.play(FadeOut(etiquetas_particiones),FadeOut(puntos_particion),FadeOut(poligonal_particion),FadeOut(puntos_evaluacion_particion),FadeOut(rectas))
        self.FadeOutWrite(text_10,text_11)
        self.wait(12.5)
        self.play(FadeOut(text_11))
        self.particiones()
        self.play(Write(text_13))
        self.wait(9.5)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )

######################################################
##### Derivabilidad, velocidad y rápidez #########
#######################################################

class Velocidad_y_rapidez(ThreeDScene):
    def cur(self, t):
        return np.array([-np.exp(t/12)*np.cos(t), -np.exp(t/12)*np.sin(t),0])

    def construct(self):
    
        ###Texto
        titulo = TextMobject('Derivabilidad de curvas, vector velocidad y rapidez')
        t_1 = TextMobject('''Sea $\\gamma : I \\subset \\mathbb{R} \\rightarrow \\mathbb{R}^n$, con $I$ un intervalo.''')
        t_2 = TextMobject('''Por ejemplo considera que la siguiente función \n
        describe el movimiento de un objeto respecto al tiempo''')
        t_3 = TextMobject('''$\\gamma(t) = -e^{\\frac{t}{12}}(\\cos t, \\sin t)$''')
        t_3.set_color(TEAL)
        t_4 = TextMobject('''Con $t \\in [-5 \\pi, 5 \\pi]$''')
        t_5 = TextMobject('''Dado $t_0 \\in I$, consideremos \n
        los vectores ''', '''$\\gamma (t)$''', ''' y ''', '''$\\gamma(t_0)$''') 
        t_5.set_color_by_tex_to_color_map({
            '''$\\gamma (t)$''': RED,
            '''$\\gamma(t_0)$''': GREEN})
        t_6 = TextMobject('''y su diferencia, ''')
        t_7 = TextMobject('''que representa el vector \n
        de cambio de posición en el \n
        intervalo $[t_0,t]$ o $[t,t_0]$:''')
        t_8 = TextMobject('''$\\gamma(t) - \\gamma(t_0)$''')
        t_8.set_color_by_tex_to_color_map({
            '''$\\gamma(t) - \\gamma(t_0)$''': YELLOW})
        t_9 = TextMobject('''Notemos que si $t - t_0 > 0$, \n
        el vector: ''', '''$\\frac{\\gamma (t) - \\gamma (t_0)}{t - t_0}$''')
        t_9.set_color_by_tex_to_color_map({
            '''$\\frac{\\gamma (t) - \\gamma (t_0)}{t - t_0}$''':LIGHT_PINK    
        })
        t_10 = TextMobject('''nos dice cómo cambió \n
        la posición en proporción 
        \n al tiempo transcurrido. \n''')
        t_11 = TextMobject('''Este vector es paralelo a \n
         ''',
         '''$\\gamma(t) - \\gamma(t_0)$, ''')
        t_11.set_color_by_tex_to_color_map({
            '''$\\gamma(t) - \\gamma(t_0)$''': YELLOW})
        t_12 = TextMobject('''Este vector es la velocidad \n
        promedio de $\\gamma$ en $[t_0,t]$''')
        t_13 = TextMobject('''Con esto en mente, decimos \n
        que $\\gamma$ es derivable \n 
        en $t_0$ si existe ''')
        t_14 = TextMobject(''' $$\\gamma ' (t_0) : = \\lim_{t \\rightarrow t_0} \\frac{\gamma (t) - \\gamma (t_0)}{t - t_0}$$''')
        t_14.set_color_by_tex_to_color_map({''' $$\\gamma ' (t_0) : = \\lim_{t \\rightarrow t_0} \\frac{\gamma (t) - \\gamma (t_0)}{t - t_0}$$''':LIGHT_PINK})
        t_15 = TextMobject(''' El vector ''', '''$\\gamma ' (t_0)$''', ''' se llama \n 
        la derivada de $\\gamma$ en $t_0$ ''')
        t_15.set_color_by_tex_to_color_map({'''$\\gamma ' (t_0)$''': LIGHT_PINK})
        t_16 = TextMobject('''que es la velocidad \n 
        (instantánea) del movimiento \n 
        al tiempo $t_0$''')
        t_17 = TextMobject('''$\\gamma'(t_0)$''', ''' nos da información \n 
        sobre la dirección, ''')
        t_17.set_color_by_tex_to_color_map({'''$\\gamma'(t_0)$''': LIGHT_PINK})
        t_18 = TextMobject('''sentido y rapidez de cómo \n
        $\gamma(t)$ recorre la curva \n 
        cerca de $\gamma(t_0)$.''')
        t_19 = TextMobject('''Además ''','''$\\Vert \\gamma'(t_0) \\Vert$''',''' depende \n 
        de cómo es $\\Vert \\gamma(t)-\\gamma(t_0)\\Vert$ ''')
        t_19.set_color_by_tex_to_color_map({'''$\\Vert \\gamma'(t_0) \\Vert$''': ORANGE})
        t_20 = TextMobject('''respecto a $|t-t_0|$ \n
        conforme $t$ se acerca a $t_0$. ''')
        t_21 = TextMobject('''Por ejemplo, ''','''$\\Vert \\gamma'(t_0) \\Vert$''', ''' es \n
        muy grande si y sólo si ''')
        t_21.set_color_by_tex_to_color_map({'''$\\Vert \\gamma'(t_0) \\Vert$''': ORANGE})
        t_22=TextMobject('''$\\Vert \\gamma(t)-\\gamma(t_0)\\Vert$ \n
         es muy grande \n
         respecto a $|t-t_0|$, ''')
        t_23 = TextMobject('''es decir, $\\gamma(t)$ está lejos de \n 
        $\\gamma(t_0)$ en proporción \n 
        al tiempo transcurrido. ''')
        t_24 = TextMobject('''En cambio, si $\\Vert \\gamma'(t_0) \\Vert \\approx 0$, \n
        es porque $\\gamma(t)$ está \n 
        cerca de $\\gamma(t_0)$ ''')
        t_25 = TextMobject(''' en proporción al tiempo \n 
        transcurrido. ''')
        t_26 = TextMobject(''' Es decir, $\\Vert \\gamma'(t_0) \\Vert$ \n 
        depende de qué tan rápido \n 
        se recorre la curva, ''')
        t_27 = TextMobject('''por ello se llama la \n 
        rapidez de $\\gamma$ en $t_0$.''')
        t_28 = TextMobject('''Sabiendo esto, ¿crees que la velocidad y rapidez dependen de la parametrización de la curva? ''')

        
        
    
        t_3.next_to(t_2, DOWN)
        t_4.to_corner(UR)
        t_5.to_corner(UR)
        t_6.to_corner(UR)
        t_7.to_corner(UR)
        t_8.to_corner(UR)
        t_9.to_corner(UR)
        t_10.to_corner(UR)
        t_11.to_corner(UR)
        t_12.to_corner(UR)
        t_13.to_corner(UR)
        t_14.to_corner(UR)
        t_15.to_corner(UL)
        t_16.to_corner(UL)
        t_17.to_corner(UL)
        t_18.to_corner(UL)
        t_19.to_corner(UL)
        t_20.to_corner(UL)
        t_21.to_corner(UL)
        t_22.to_corner(UL)
        t_23.to_corner(UL)
        t_24.to_corner(UL)
        t_25.to_corner(UL)
        t_26.to_corner(UL)
        t_27.to_corner(UL)

        ### Objetos

        axes = ThreeDAxes(x_min = -5, x_max = 5, y_min = -4, y_max=4, num_axis_pieces= 4)
        curve_1 = ParametricFunction(self.cur, color=TEAL, t_min= -5*PI,t_max=5*PI)
        t_0 = 9.5
        t=t_0 +1.2
        gamma = Vector(direction= self.cur(t), color=RED)
        gamma_0 =  Vector(direction= self.cur(t_0), color=GREEN)
        diferencia = Vector(direction=self.cur(t) - self.cur(t_0), color=YELLOW).move_to((self.cur(t) + self.cur(t_0))/2)
        derivada =  Vector(direction=(self.cur(t) - self.cur(t_0))/(t - t_0), color=PINK).move_to((self.cur(t) + self.cur(t_0))/2 + ((self.cur(t) - self.cur(t_0))/(t - t_0)- (self.cur(t) - self.cur(t_0)))/2)
        
       



        ### Update


        x = ValueTracker(t)

        def update_group(Group):
            gamma, gamma_0, derivada = Group
            gamma_new = Vector(direction= self.cur(x.get_value()), color=RED)
            gamma.become(gamma_new)
            derivada_new = Vector(direction=(self.cur(x.get_value()) - self.cur(t_0))/(x.get_value() - t_0), color=PINK).move_to((self.cur(x.get_value()) + self.cur(t_0))/2 + ((self.cur(x.get_value()) - self.cur(t_0))/(x.get_value() - t_0)- (self.cur(x.get_value()) - self.cur(t_0)))/2)
            derivada.become(derivada_new)
            return Group

        y = ValueTracker(t_0)
        def update_group_0(derivada):
            derivada_new = Vector(direction=(self.cur(x.get_value()) - self.cur(y.get_value()))/(x.get_value() - y.get_value()), color=PINK).move_to((self.cur(x.get_value()) + self.cur(y.get_value()))/2 + ((self.cur(x.get_value()) - self.cur(y.get_value()))/(x.get_value() - y.get_value())- (self.cur(x.get_value()) - self.cur(y.get_value())))/2)
            derivada.become(derivada_new)
            return Group

        


        ###Grupos
        Group = VGroup(gamma,gamma_0,derivada)
        Group_1 = VGroup(curve_1)
        Group_2 = VGroup(gamma,gamma_0)
        Group_3 = VGroup(diferencia)
        Group_4 = VGroup(derivada)
    
        


        ### Animaciones
        #self.begin_ambient_camera_rotation(rate=0.12)
        self.add_fixed_in_frame_mobjects(titulo)
        self.play(Write(titulo))
        self.wait(2.5)
        self.play(FadeOut(titulo))
        self.add_fixed_in_frame_mobjects(t_1)
        self.play(Write(t_1))
        self.wait(4)
        self.play(FadeOut(t_1))
        self.add_fixed_in_frame_mobjects(t_2)
        self.play(Write(t_2))
        self.add_fixed_in_frame_mobjects(t_3)
        self.play(Write(t_3))
        self.wait(6)
        self.play(FadeOut(t_2))
        self.play(ApplyMethod(t_3.shift, 4*UP + 4*RIGHT))
        self.add(axes)
        self.set_camera_orientation(phi=0* DEGREES,theta=-90*DEGREES)
        self.play(LaggedStart(ShowCreation(Group_1)))
        self.wait(2)
        self.play(FadeOut(t_3))
        self.add_fixed_in_frame_mobjects(t_4)
        self.play(Write(t_4))
        self.wait()
        self.play(FadeOut(t_4))
        self.wait(1.8)
        self.add_fixed_in_frame_mobjects(t_5)
        self.play(Write(t_5))
        self.play(LaggedStart(ShowCreation(Group_2)))
        self.wait(3.7)
        self.play(FadeOut(t_5))
        self.add_fixed_in_frame_mobjects(t_6)
        self.play(Write(t_6))
        self.wait(1)
        self.play(FadeOut(t_6))
        self.add_fixed_in_frame_mobjects(t_7)
        self.play(Write(t_7))
        self.wait(5.2)
        self.play(FadeOut(t_7))
        self.add_fixed_in_frame_mobjects(t_8)
        self.play(Write(t_8))
        self.wait(1)
        self.play(LaggedStart(ShowCreation(Group_3)))
        self.wait()
        self.play(FadeOut(t_8))
        self.wait()
        self.add_fixed_in_frame_mobjects(t_9)
        self.play(Write(t_9))
        self.play(LaggedStart(ShowCreation(Group_4)))
        self.wait(3.3)
        self.play(FadeOut(t_9))
        self.add_fixed_in_frame_mobjects(t_10)
        self.play(Write(t_10))
        self.wait(4.1)
        self.play(FadeOut(t_10))
        self.add_fixed_in_frame_mobjects(t_11)
        self.play(Write(t_11))
        self.wait(2.6)
        self.play(FadeOut(t_11))
        self.wait()
        self.play(FadeOut(Group_3))
        self.add_fixed_in_frame_mobjects(t_12)
        self.play(Write(t_12))
        self.wait(3.7)
        self.play(FadeOut(t_12))
        self.add_fixed_in_frame_mobjects(t_13)
        self.play(Write(t_13))
        self.wait(4.8)
        self.play(FadeOut(t_13))
        self.add_fixed_in_frame_mobjects(t_14)
        self.play(Write(t_14))
        self.wait(4.5)
        Group.add_updater(update_group)
        self.add(Group)
        self.play(x.increment_value,-1.199999, rate_func=linear,run_time=4)
        self.wait()
        self.play(FadeOut(Group_2))
        self.play(FadeOut(t_14))
        self.add_fixed_in_frame_mobjects(t_15)
        self.play(Write(t_15))
        self.wait(4.5)
        self.play(FadeOut(t_15))
        self.add_fixed_in_frame_mobjects(t_16)
        self.play(Write(t_16))
        self.wait(3.7)
        self.play(FadeOut(t_16))
        self.add_fixed_in_frame_mobjects(t_17)
        self.play(Write(t_17))
        self.wait(2.6)
        self.play(FadeOut(t_17))
        self.add_fixed_in_frame_mobjects(t_18)
        self.play(Write(t_18))
        self.wait(4.5)
        derivada.add_updater(update_group_0)
        self.add(derivada)
        self.play(x.increment_value,4.71,y.increment_value,4.71, rate_func=linear,run_time=2)
        self.play(FadeOut(t_18))
        self.wait()
        self.add_fixed_in_frame_mobjects(t_19)
        Group_5= VGroup(Brace(derivada, 0.3*UP, color=ORANGE), TextMobject('''$\\Vert \\gamma'(t_0) \\Vert$''').next_to(derivada, 2*UP).set_color(ORANGE))
        self.play(Write(t_19), FadeIn(Group_5))
        self.wait(4.5)
        self.play(FadeOut(t_19))
        self.add_fixed_in_frame_mobjects(t_20)
        self.play(Write(t_20))
        self.wait(3.3)
        self.play(FadeOut(t_20))
        self.add_fixed_in_frame_mobjects(t_21)
        self.play(Write(t_21))
        self.wait(4.1)
        self.play(FadeOut(t_21))
        self.add_fixed_in_frame_mobjects(t_22)
        self.play(Write(t_22))
        self.wait(4.1)
        self.play(FadeOut(t_22))
        self.add_fixed_in_frame_mobjects(t_23)
        self.play(Write(t_23))
        self.wait(4.5)
        self.play(FadeOut(t_23))
        self.add_fixed_in_frame_mobjects(t_24)
        self.play(Write(t_24))
        self.wait(5.2)
        self.play(FadeOut(t_24))
        self.add_fixed_in_frame_mobjects(t_25)
        self.play(Write(t_25))
        self.wait(2.2)
        self.play(FadeOut(t_25))
        self.add_fixed_in_frame_mobjects(t_26)
        self.play(Write(t_26))
        self.wait(5.2)
        self.play(FadeOut(t_26))
        self.add_fixed_in_frame_mobjects(t_27)
        self.play(Write(t_27))
        self.wait(3.7)
        self.play(FadeOut(t_27))
        self.remove(derivada)
        self.play(FadeOut(Group_5), FadeOut(Group_1), FadeOut(axes))
        self.add_fixed_in_frame_mobjects(t_28)
        self.play(Write(t_28))
        self.wait(5.6)
        self.play(FadeOut(t_28))
