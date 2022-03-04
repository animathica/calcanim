from manimlib.imports import *

class CurvaturaOsculador(Scene):
    def parte1(self):
        title = TextMobject('''¿Qué tanto se dobla una curva?''')
        t1 = TextMobject('''Consideremos las funciones ''','''$f(t)=(t,t^2)$''',''' y ''','''$g(t)=(t,2t^2)$''')
        t1.set_color_by_tex_to_color_map({
            '''$f(t)=(t,t^2)$''': RED,
            '''$g(t)=(t,2t^2)$''': BLUE
        })
        t2 = TextMobject('''Ambas funciones parametrizan una parábola en el plano.''').to_edge(DOWN)
        gpot2 = self.rectangulo_texto(t2)
        t3 = TextMobject('''En el origen, ambas curvas tienen una recta \n
                            horizontal como tangente, pero $g$ se ``despega'' más\n
                            de la tangente que $f$.''').to_edge(DOWN).scale(0.8)
        gpot3 = self.rectangulo_texto(t3)
        t4 = TextMobject('''Queremos medir qué tanto se doblan las curvas a partir de\n
                            medir qué tanto se despegan de su tangente, sin importar \n
                            la rapidez.''').to_edge(DOWN).scale(0.8)
        gpot4 = self.rectangulo_texto(t4)
        t5 = TextMobject('''Observemos que cerca del origen el vector tangente unitario\n
                            de $f$, ''','''$T_f(t)$''',''' cambia de dirección menos rápido que el \n
                            de $g$, ''','''$T_g(t)$''').to_edge(DOWN).scale(0.8)
        t5.set_color_by_tex_to_color_map({
            '''$T_f(t)$''': ORANGE,
            '''$T_g(t)$''': GREEN
        })    
        gpot5 = self.rectangulo_texto(t5)
        t6 = TextMobject('''Por lo que utilizaremos $T'(t)$ para medir qué tanto \n
                            se dobla una curva.''').to_edge(DOWN).scale(0.8)
        gpot6 = self.rectangulo_texto(t6)

        ### OBJETOS
        axes = Axes(x_min = -5, x_max = 5, y_min = -0.5, y_max = 5)
        x_label = TexMobject(r"x").scale(0.75).move_to((5.1,-0.3,0))
        y_label = TexMobject(r"y").scale(0.75).move_to((-0.3,5.1,0))
        ejes = VGroup(axes,x_label,y_label)
        parabola1 = ParametricFunction(lambda t: np.array([t,t**2,0]),t_min=-5**(1/2),t_max=5**(1/2),color = RED)
        parabola2 = ParametricFunction(lambda t: np.array([t,2*t**2,0]),t_min=-(5/2)**(1/2),t_max=(5/2)**(1/2),color = BLUE)
        tangente = ParametricFunction(lambda t: np.array([t,0,0]),t_min=-3,t_max=3,color=YELLOW)
        T_f = Arrow(start=np.array([-1,1,0]),end=(1/((1+(2*(-1))**2)**(1/2)))*np.array([1,2*(-1),0])+np.array([-1,1,0]),color=ORANGE,buff=0)
        T_g = Arrow(start=np.array([-1,2,0]),end=(1/((1+(4*(-1))**2)**(1/2)))*np.array([1,4*(-1),0])+np.array([-1,2,0]),color=GREEN,buff=0)

        grupo_util = VGroup(ejes,parabola1,parabola2,tangente,T_f,T_g)

        def tangente_f(objeto):
            te = t.get_value()
            inicio = np.array([te,te**2,0])
            final = (1/(1+(2*te)**2)**(1/2))*np.array([1,2*te,0])+inicio
            T_f.become(
                Arrow(start=inicio+1.5*DOWN,end=final+1.5*DOWN,color=ORANGE,buff=0)
            )
        def tangente_g(objeto):
            te = t.get_value()
            inicio = np.array([te,2*te**2,0])
            final = (1/(1+(4*te)**2)**(1/2))*np.array([1,4*te,0])+inicio
            T_g.become(
                Arrow(start=inicio+1.5*DOWN,end=final+1.5*DOWN,color=GREEN,buff=0)
            )
        t = ValueTracker(-1)

        self.write_wait_fade(title)
        self.play(Write(t1))
        self.play(ApplyMethod(t1.to_edge,DOWN))
        grupo_util.shift(1.5*DOWN)
        self.play(Write(ejes))
        self.play(ShowCreation(parabola1),ShowCreation(parabola2))
        self.play(FadeOut(t1))
        self.write_wait_fade(gpot2,1.5)
        self.play(Write(gpot3))
        self.play(Write(tangente))
        self.wait(2)
        self.play(FadeOut(gpot3))
        self.write_wait_fade(gpot4,3)
        self.play(FadeOut(tangente))
        self.play(Write(gpot5))
        self.wait(3)
        T_f.add_updater(tangente_f)
        T_g.add_updater(tangente_g)
        self.play(Write(T_f),run_time=0.5)
        self.play(Write(T_g),run_time=0.5)
        self.play(t.increment_value,2,run_time=6)
        T_f.remove_updater(tangente_f)
        T_g.remove_updater(tangente_g)
        self.wait()
        self.play(FadeOut(gpot5))
        self.play(Write(gpot6))
        self.wait(2)
        self.play(*[FadeOut(obj) for obj in self.mobjects])

    def parte2(self):
        t1 = TextMobject('''Ahora consideremos las funciones $f(t)=(\\cos t,\\sin t)$ \n
                            y $g(t)=f(2t)$, $t\\in\\mathbb{R}$.''')
        t2 = TextMobject('''Ambas funciones parametrizan una circunferencia de radio 1\n
                            con centro en el origen en el plano, es decir, están \n
                            dobladas de la misma manera, pero $g$ tiene mayor rapidez, \n
                            de hecho $||f'(t)||=1$ y $||g'(t)||=2$ para toda $t$.''')
        t3 = TextMobject('''Más aún, $T'_f(t)\\neq T'_g(t)$, por lo que necesitamos \n
                            medir el cambio del vector tangente unitario en relación con \n
                            la rapidez.''')
        t4 = TextMobject('''Adicionalmente, solo queremos saber qué tanto se dobla \n 
                            la curva sin importar la dirección de la tangente, \n
                            por ello solo tomaremos en cuenta la norma de $T'$.''')
        t5 = TextMobject('''Por lo anterior, la curvatura de $f$ en $t$ es:''').shift(UP)
        t6 = TexMobject(r"\kappa(t)=\dfrac{||T'(t)||}{||f'(t)||}").next_to(t5,DOWN)
        t7 = TextMobject('''que nos permite medir qué tan doblada está la curva \n
                            en un punto.''').next_to(t6,DOWN)
        gpo = VGroup(t5,t6,t7)

        self.write_wait_fade(t1,4)
        self.write_wait_fade(t2,9)
        self.write_wait_fade(t3,5)
        self.write_wait_fade(t4,6)
        self.write_wait_fade(gpo,8)

    def parte3(self):
        t1 = TextMobject('''Considera las siguientes funciones''')
        t2 = TextMobject('''$f(t)=(t,10t^2)$''',''' y ''','''$g(t)=(t,t^2/10)$''').next_to(t1,DOWN)
        t2.set_color_by_tex_to_color_map({
            '''$f(t)=(t,10t^2)$''': RED,
            '''$g(t)=(t,t^2/10)$''': BLUE
        })
        t3 = TextMobject('''Puedes hacer las cuentas para encontrar la curvatura \n
                            de ambas curvas en $t=0$.''').to_edge(DOWN)
        t4 = TextMobject('''De las cuentas encontramos que \n
                            $\\kappa_f(0)\\approx 201$ y $\\kappa_g(0)= 0.2$\n.''').to_edge(DOWN)
        t5 = TextMobject('''Para la primer curva, la curvatura es grande, mientras que \n
                            para la segunda, la curvatura es muy pequeña''').to_edge(DOWN)
        t6 = TextMobject('''Nota que en el caso de una circunferencia de radio $r$, \n
                            la curvatura es constante y es $\\kappa(t)=1/r$.''')
        t7 = TextMobject('''Esto nos permite definir el círculo osculador de $f$ en $t$ \n
                            como aquella circunferencia que tiene la misma tangente \n
                            y curvatura que $f$ en $t$.''')
        t8 = TextMobject('''Además, este círculo y la curva están del mismo lado de\n
                            la tangente que tienen en común.''')
        t9 = TextMobject('''En otras palabra, el círculo osculador es el que más \n
                            se parece a la función en $t$.''')

        gpo = VGroup(t1,t2)

        ### OBJETOS
        axes = Axes(x_min = -5, x_max = 5, y_min = -0.5, y_max = 5)
        x_label = TexMobject(r"x").scale(0.75).move_to((5.1,-0.3,0))
        y_label = TexMobject(r"y").scale(0.75).move_to((-0.3,5.1,0))
        ejes = VGroup(axes,x_label,y_label)
        parabola1 = ParametricFunction(lambda t: np.array([t,10*t**2,0]),t_min=-(1/2)**(1/2),t_max=(1/2)**(1/2),color=RED)
        parabola2 = ParametricFunction(lambda t: np.array([t,t**2/10,0]),t_min=-5,t_max=5,color=BLUE)

        grupo_util = VGroup(ejes,parabola1,parabola2)

        self.play(Write(t1))
        self.play(Write(t2))
        self.wait(3)
        self.play(ApplyMethod(gpo.to_edge,DOWN))
        grupo_util.shift(1.5*DOWN)
        self.play(Write(ejes))
        self.play(Write(parabola1),Write(parabola2))
        self.play(FadeOut(gpo))
        self.write_wait_fade(t3,3)
        self.write_wait_fade(t4,4)
        self.write_wait_fade(t5,3)
        self.play(*[FadeOut(obj) for obj in self.mobjects])
        self.write_wait_fade(t6,3)
        self.write_wait_fade(t7,5)
        self.write_wait_fade(t8,4)
        self.write_wait_fade(t9,3)
    
    def definiciones(self):
        t1 = TextMobject('''Por lo anterior, el círculo osculador de $f(t)$ en $t_0$ \n
                            está dado por''')\
            .shift(3*UP)
        t2 = TexMobject(r"C(t)=\frac{1}{\kappa(t_0)}(\cos t,\sin t)+D_0").next_to(t1,DOWN)
        t3 = TexMobject(r"D_0 = f(t_0)+\frac{N(t_0)}{\kappa(t_0)}").next_to(t2,DOWN)
        t4 = TexMobject(r"\kappa(t_0)=\frac{||T'(t_0)||}{||f'(t_0)||}").next_to(t3,DOWN)
        t5 = TexMobject(r"N(t_0)=\frac{T'(t_0)}{||T'(t_0)||}").next_to(t4,DOWN)

        self.play(Write(t1))
        self.play(Write(t2))
        self.play(Write(t3))
        self.play(Write(t4))
        self.play(Write(t5))
        self.wait(7)
        self.play(*[FadeOut(mob) for mob in self.mobjects])


    def ejemplo(self):
        t1 = TextMobject('''Considera el ejemplo dado por la siguiente curva''').to_edge(UP)
        t2 = TexMobject(r"f(t)=(3\cos t,2\sin t)").next_to(t1,DOWN)
        t12 = VGroup(t1,t2)
        t12gpo = self.rectangulo_texto(t12)
        ejes = Axes(
            y_min = -2.5,
            y_max = 2.5,
            x_min = -5,
            x_max = 5
        )
        elipse = ParametricFunction(self.elipse,t_min=0,t_max=2*PI,color=RED)

        self.play(ShowCreation(ejes),Write(t12gpo))
        self.play(ShowCreation(elipse))
        osculador = Circle(radius=1/self.curvatura(0),color=YELLOW,arc_center=self.centro_circ(0))

        self.t_offset = 0
        def osculador_update(mob,dt):
            rate = 0.7*dt
            new_osculador = Circle(
                radius=1/self.curvatura(self.t_offset+rate),
                color=YELLOW,
                arc_center=self.centro_circ(self.t_offset+rate))
            mob.become(new_osculador)
            self.t_offset += rate

        t3 = TextMobject('''Nota que siempre el círculo "besa" \n
                            en un solo punto a la curva $f$ \n
                            de ahí su nombre.''',color="#a5f0e6")\
                                .to_corner(LEFT+DOWN)\
                                .scale(0.6)

        self.play(ShowCreation(osculador))
        osculador.add_updater(osculador_update)
        self.play(Write(t3),run_time=2)
        self.wait(8.5)
        osculador.clear_updaters()
        self.play(*[FadeOut(mob) for mob in self.mobjects])

    def construct(self):
        self.parte1()
        self.parte2()
        self.parte3()
        self.definiciones()
        self.ejemplo()

    def write_wait_fade(self,obj,time=1):
        self.play(Write(obj))
        self.wait(time)
        self.play(FadeOut(obj))

    def rectangulo_texto(self,obj):
        rect = SurroundingRectangle(obj,color=WHITE,fill_color=BLACK,fill_opacity=1)
        grupo = VGroup(rect,obj)
        return grupo
    
    def elipse(self,t):
        return [3*np.cos(t),2*np.sin(t),0]

    def curvatura(self,t):
        k = 6/((9*np.sin(t)**2 + 4*np.cos(t)**2)**(1/2))
        return k

    def centro_circ(self,t):
        D_0 = [(8/3)*np.cos(t),(3/2)*np.sin(t),0]
        return D_0