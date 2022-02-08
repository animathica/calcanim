from manimlib.imports import *

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
        Title = TextMobject("Curvas Regulares y Picos").scale(1.5)
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
        t16 = TextMobject('''Ahora considera la parametrización $\\gamma(t)=(t^3,|t|^3)$ con $t\\in[-1,1]$''').scale(0.8).to_edge(UP)
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
        self.play(Write(t10))
        self.wait(15)
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
        