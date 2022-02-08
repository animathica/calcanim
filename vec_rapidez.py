from manimlib.imports import *

######################################################
##### Derivabilidad, velocidad y rápidez #########
#######################################################

class Velocidad_y_rapidez(ThreeDScene):
    def cur(self, t):
        return np.array([-np.exp(t/12)*np.cos(t), -np.exp(t/12)*np.sin(t),0])

    def construct(self):
    
        ###Texto
        titulo = TextMobject('''Derivabilidad de Curvas, \n
                                Vector Velocidad y Rapidez''').scale(1.5)
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