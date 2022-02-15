from manimlib.imports import *

class Continuidad_con_sucesiones(ThreeDScene):
    def acomodar_textos(self,objeto):
        self.add_fixed_in_frame_mobjects(objeto)
        self.play(Write(objeto))
    def acomodar_puntos(self,objeto):
        self.add_fixed_in_frame_mobjects(objeto)
        self.add(objeto)
    # Definimos las funciones a utilizar (las que vamos a graficar)
    # Puedes cambiar estas funciones con las que se te ocurra
    # Son funciones de R  a R2, y estamos obteniendo sus gráficas
    # por lo que la primer entrada siempre debe ser lo que parametriza
    # la función, es decir, la variable independiente

    def helicoide(self,t):
        return [t,np.cos(4*t),np.sin(4*t)] #f(t)=(cos(4t),sin(4t))
    
    def func_suma(self,t):
        return [t,t+np.cos(4*t),t+np.sin(4*t)] #g(t)=(t+cos(4t),t+sin(4t))
    
    def contra1(self,t):
        return [t,1,1] #h(t)=(1,1)
    
    def contra2(self,t):
        return [t,-1,-1] #u(t)=(-1,-1)
    
    def construct(self):
        # Textos
        t_1 = TextMobject('''Continuidad en Curvas con Sucesiones''').scale(1.5)
        t_2 = TextMobject('''Recuerda que una posible definición de ''','''continuidad''',''' es: \n
                            $f:\\mathbb{R}\\to\\mathbb{R}^2$ es ''','''continua''',''' en $t_0$ si''').shift(1*UP)
        t_2.set_color_by_tex_to_color_map({
            '''continuidad''': BLUE,
            '''continua''': BLUE
        })
        t_3 = TexMobject(r"\lim_{t\to t_0}f(t)=f(t_0)").next_to(t_2,DOWN)
        t_4 = TextMobject('''Aquí utilizaremos una equivalencia con ''','''sucesiones''',''':''')
        t_4.set_color_by_tex_to_color_map({
            '''sucesiones''': PURPLE_B
        })
        t_4_1 = TextMobject('''$f:\\mathbb{R}\\to\\mathbb{R}^2$ es ''','''continua''',''' en $t_0$ \n
                            $\\Leftrightarrow \\forall\\{x_n\\}\\subset\\mathbb{R}$ ''','''sucesión''',''' tal que''').shift(1*UP)
        t_4_1.set_color_by_tex_to_color_map({
            '''sucesión''': PURPLE_B,
            '''continua''': BLUE
        })
        t_5 = TexMobject(r"\lim_{n\to\infty}x_n=t_0,\\\\ \lim_{n\to\infty}f(x_n)=f(t_0)").next_to(t_4_1,DOWN)
        t_6 = TextMobject('''Veamos un par de ejemplos...''')
        nota = TextMobject('''NOTA: Aquí ejemplificaremos usando solo una sucesión, puedes probar con \n
                            otras sucesiones modificando el código correspondiente.''').scale(0.5).shift(3.5*DOWN)
        t_7 = TextMobject('''Considera $t_0=0$''').scale(0.7).to_corner(LEFT+UP).shift(1*RIGHT)
        t_7.bg = SurroundingRectangle(t_7,color=WHITE,fill_color=BLACK,fill_opacity=0.5)
        reglaf = TextMobject('''$f(t)$''','''$=(\cos(4t),\sin(4t))$''').scale(0.7).align_to(t_7,LEFT).shift(2.7*UP).shift(0.5*LEFT)
        reglaf.set_color_by_tex_to_color_map({
            '''$f(t)$''': RED
        })
        reglaf.bg = SurroundingRectangle(reglaf,color=WHITE,fill_color=BLACK,fill_opacity=0.5)
        reglaf.group = VGroup(reglaf,reglaf.bg)
        t_8 = TextMobject('''Toma la ''','''sucesión ''','''$X_n$''','''$=\\dfrac{3}{n}$''').scale(0.7).to_corner(RIGHT+DOWN).shift(2.5*UP).shift(1.5*LEFT)
        t_8.set_color_by_tex_to_color_map({
            '''$X_n$''': YELLOW
        })
        t_8.bg = SurroundingRectangle(t_8,color=WHITE,fill_color=BLACK,fill_opacity=0.5)
        t_8.group = VGroup(t_8,t_8.bg)
        #t_9 = TextMobject('''Converge a 0, su imagen a $(1,0)$ \n
        #                    y su gráfica a $(0,1,0)$''').scale(0.7).next_to(t_8.bg,DOWN)
        t_9 = TextMobject('''$\\lim_{n \\to \\infty} $''','''$X_n$''','''$ = 0$ \\\\
                                $\\lim_{n \\to \\infty} f(X_n) = (1,0)$ \\\\
                                $\\lim_{n \\to \\infty} (X_n,f(X_n)) = (0,1,0)$''').scale(0.7).next_to(t_8.bg,DOWN)
        t_9[1].set_color(YELLOW)
        reglag = TextMobject('''$g(t)$''','''$=(t+\cos(4t),t+\sin(4t))$''').scale(0.7).align_to(t_7,LEFT).shift(2.7*UP).shift(1*LEFT)
        t_9.bg = SurroundingRectangle(t_9,color=WHITE,fill_color=BLACK,fill_opacity=0.5)
        t_9.group = VGroup(t_9,t_9.bg)
        reglag.set_color_by_tex_to_color_map({
            '''$g(t)$''': BLUE
        })
        reglag.bg = SurroundingRectangle(reglag,color=WHITE,fill_color=BLACK,fill_opacity=0.5)
        t_10 = TextMobject('''¿Y cómo sería una función ''','''discontinua?''').scale(0.7).to_corner(LEFT+UP)
        t_10.bg = SurroundingRectangle(t_10,color=WHITE,fill_color=BLACK,fill_opacity=0.5)
        t_10.group = VGroup(t_10,t_10.bg)
        t_10.set_color_by_tex_to_color_map({
            '''discontinua''': GREEN_D
        })
        #reglacontra1_tex = ["(1,1)",",","t\\leq 0"]
        reglacontra1_tex = ["(1,1),","t\\leq 0"]
        reglacontra2_tex = ["(-1,-1)",",","t>0"]
        reglacontra1_mob = TexMobject(*reglacontra1_tex)
        reglacontra2_mob = TexMobject(*reglacontra2_tex)
        for i,item in enumerate(reglacontra1_mob):
            item.align_to(reglacontra2_mob[i],LEFT)
        reglacontra1 = VGroup(*reglacontra1_mob)
        reglacontra2 = VGroup(*reglacontra2_mob).shift(DOWN)
        reglacontra = VGroup(reglacontra1,reglacontra2)
        brace = Brace(reglacontra,LEFT)
        h = brace.get_text("$h(x)$","$=$")
        h.set_color_by_tex_to_color_map({
            "$h(x)$": ORANGE
            })
        reglacompleta = VGroup(reglacontra,brace,h).scale(0.7).next_to(t_7.bg,DOWN).align_to(t_7,LEFT)
        reglacompleta.bg = SurroundingRectangle(reglacompleta,color=WHITE,fill_color=BLACK,fill_opacity=0.5)
        t_11 = TextMobject('''Toma las ''','''sucesiones ''','''$X_n$''','''$=\\dfrac{3}{n}$ y \n
                            ''','''$Y_n$''','''$=-\\dfrac{3}{n}$''').scale(0.7).to_corner(RIGHT+UP)
        t_11.bg = SurroundingRectangle(t_11,color=WHITE,fill_color=BLACK,fill_opacity=0.5)
        t_11.set_color_by_tex_to_color_map({
            '''$X_n$''': YELLOW,
            '''$Y_n$''': YELLOW
            })
        #t_12 = TextMobject('''$X_n$''',''' converge a 0, su imagen a $(-1,-1)$ \n
        #                    y su gráfica a $(0,-1,-1)$''').scale(0.7).to_corner(RIGHT+DOWN).shift(2*UP)
        t_12 = TextMobject('''$\\lim_{n \\to \\infty} $''','''$X_n$''','''$ = 0$ \\\\
                                $\\lim_{n \\to \\infty} f(X_n) = (-1,-1)$ \\\\
                                $\\lim_{n \\to \\infty} (X_n,f(X_n)) = (0,-1,-1)$''').scale(0.7).to_corner(RIGHT+DOWN).shift(2*UP)
        t_12[1].set_color(YELLOW)
        t_12.bg = SurroundingRectangle(t_12,color=WHITE,fill_color=BLACK,fill_opacity=0.5)
        #t_12.set_color_by_tex_to_color_map({
        #    '''$X_n$''': YELLOW
        #    })
        #t_13 = TextMobject('''$Y_n$''',''' converge a 0, su imagen a $(1,1)$ \n
        #                    y su gráfica a $(0,1,1)$''').scale(0.7).next_to(t_12.bg,DOWN)
        t_13 = TextMobject('''$\\lim_{n \\to \\infty} $''','''$Y_n$''','''$ = 0$ \\\\
                                $\\lim_{n \\to \\infty} f(Y_n) = (1,1)$ \\\\
                                $\\lim_{n \\to \\infty} (Y_n,f(Y_n)) = (0,1,1)$''').scale(0.7).next_to(t_12.bg,DOWN)
        t_13.bg = SurroundingRectangle(t_13,color=WHITE,fill_color=BLACK,fill_opacity=0.5)
        t_13.set_color_by_tex_to_color_map({
            '''$Y_n$''': YELLOW
            })
        t_13.group = VGroup(t_13,t_13.bg)
        t_14 = TextMobject('''Tenemos entonces dos ''','''sucesiones''',''' \\\\ 
                            que convergen a $t_0$ cuyas ''','''sucesiones''',''' \\\\ 
                            de imágenes convergen a cosas distintas.\\\\
                            Concluimos que la función \\\\ 
                            es ''','''discontinua''',''' en $t_0$.''').scale(0.7).to_corner(RIGHT+DOWN).shift(1*UP)
        t_14.bg = SurroundingRectangle(t_14,color=WHITE,fill_color=BLACK,fill_opacity=0.5)
        t_14.set_color_by_tex_to_color_map({
            '''discontinua''': GREEN_D,
            '''sucesiones''': PURPLE_B
        })
        t_14.group = VGroup(t_14,t_14.bg)
        
        # Ejes en 3D
        axis_config = {
            "x_min" : -6,
            "x_max" : 6,
            "y_min" : -6,
            "y_max" : 6,
            "z_min" : -6,
            "z_max" : 6
        }
        ejes = ThreeDAxes(**axis_config)

        # Funciones que se van a utilizar
        tmin = -6
        tmax = 6
        f = ParametricFunction(self.helicoide,t_min=tmin,t_max=tmax,color=RED).set_shade_in_3d(True)
        g = ParametricFunction(self.func_suma,t_min=tmin,t_max=tmax,color=BLUE).set_shade_in_3d(True)
        contra_1 = ParametricFunction(self.contra1,t_min=tmin,t_max=0,color=ORANGE).set_shade_in_3d(True)
        contra_2 = ParametricFunction(self.contra2,t_min=0.001,t_max=tmax,color=ORANGE).set_shade_in_3d(True)

        # Sucesiones
        X = []
        Y = []
        Z = []
        W = []
        for n in range(1,101):
            x_n = Dot(color=YELLOW,point=(3/n,np.cos(4*3/n),np.sin(4*3/n)))
            X.append(x_n)
            y_n = Dot(color=YELLOW,point=(3/n,3/n+np.cos(4*3/n),3/n+np.sin(4*3/n)))
            Y.append(y_n)
            z_n = Dot(color=YELLOW,point=(3/n,-1,-1))
            Z.append(z_n)
            w_n = Dot(color=YELLOW,point=(-3/n,1,1))
            W.append(w_n)
        suce1 = VGroup(*X)
        suce2 = VGroup(*Y)
        suce3 = VGroup(*Z)
        suce4 = VGroup(*W)

        # Grupos útiles
        Grupo1 = VGroup(t_2,t_3)
        Grupo1_1 = VGroup(t_4)
        Grupo2 = VGroup(t_4_1,t_5)
        Grupo3 = VGroup(t_8,t_9,t_8.bg,t_9.bg)
        Grupo4 = VGroup(t_6,nota)
        Grupo5 = VGroup(t_11,t_12,t_11.bg,t_12.bg,t_13,t_13.bg)
        Grupo6 = VGroup(t_7,t_7.bg,reglacompleta,reglacompleta.bg,contra_1,contra_2,t_14,t_14.bg,suce3,suce4,ejes)

        # Animación        
        
        self.play(Write(t_1))
        self.wait()
        self.play(FadeOutAndShiftDown(t_1))
        self.play(Write(Grupo1))
        self.wait(10)
        self.play(ReplacementTransform(Grupo1,Grupo1_1))
        self.wait(2.5)
        self.play(ReplacementTransform(Grupo1_1,Grupo2))
        self.wait(10)
        self.play(FadeOut(Grupo2))
        self.play(Write(Grupo4))
        self.wait(3)
        self.play(FadeOutAndShiftDown(Grupo4))

        self.set_camera_orientation(phi=115*DEGREES,theta=-65*DEGREES)
        self.play(ShowCreation(ejes))
        self.acomodar_textos(t_7.bg)
        self.acomodar_textos(t_7)
        self.add_foreground_mobjects(t_7.bg)
        self.add_foreground_mobjects(t_7)
        self.wait(2)
        self.begin_ambient_camera_rotation(rate=0.07)

        self.acomodar_textos(reglaf.bg)
        self.acomodar_textos(reglaf)
        self.add_foreground_mobjects(reglaf.bg)
        self.add_foreground_mobjects(reglaf)
        self.play(ShowCreation(f),run_time=2)
        self.wait(2.5)
        self.acomodar_textos(t_8.bg)
        self.acomodar_textos(t_8)
        self.add_foreground_mobjects(t_8.bg)
        self.add_foreground_mobjects(t_8)
        self.play(Write(suce1),run_time=3)
        self.wait(2)
        self.acomodar_textos(t_9.bg)
        self.acomodar_textos(t_9)
        self.add_foreground_mobjects(t_9.bg)
        self.add_foreground_mobjects(t_9)
        self.wait(10)
        self.remove_foreground_mobjects(reglaf.bg)
        self.remove_foreground_mobjects(reglaf)
        self.remove_foreground_mobjects(t_8.bg)
        self.remove_foreground_mobjects(t_8)
        self.remove_foreground_mobjects(t_9.bg)
        self.remove_foreground_mobjects(t_9)
        self.play(FadeOut(suce1),FadeOut(reglaf.group),FadeOut(f),FadeOut(Grupo3),FadeOut(t_8.group),FadeOut(t_9.group))

        self.acomodar_textos(reglag.bg)
        self.acomodar_textos(reglag)
        self.add_foreground_mobjects(reglag.bg)
        self.add_foreground_mobjects(reglag)
        self.play(ShowCreation(g),run_time=2)
        self.wait(4)
        self.acomodar_textos(t_8.bg)
        self.acomodar_textos(t_8)
        self.play(Write(suce2),run_time=3)
        self.wait(2)
        self.acomodar_textos(t_9.bg)
        self.acomodar_textos(t_9)
        self.wait(10)
        self.remove_foreground_mobjects(reglag.bg)
        self.remove_foreground_mobjects(reglag)
        self.remove_foreground_mobjects(t_7.bg)
        self.remove_foreground_mobjects(t_7)
        self.remove_foreground_mobjects(t_8.bg)
        self.remove_foreground_mobjects(t_8)
        self.remove_foreground_mobjects(t_9.bg)
        self.remove_foreground_mobjects(t_9)
        self.play(FadeOut(suce2),FadeOut(reglag),FadeOut(g),FadeOut(reglag.bg),FadeOut(Grupo3),FadeOut(t_7),FadeOut(t_7.bg))
        
        self.acomodar_textos(t_10.bg)
        self.acomodar_textos(t_10)
        self.add_foreground_mobjects(t_10.bg)
        self.add_foreground_mobjects(t_10)
        self.wait(2.5)
        self.play(FadeOut(t_10),FadeOut(t_10.bg))
        self.remove_foreground_mobjects(t_10.bg)
        self.remove_foreground_mobjects(t_10)
        self.acomodar_textos(t_7.bg)
        self.acomodar_textos(t_7)
        self.add_foreground_mobjects(t_7.bg)
        self.add_foreground_mobjects(t_7)
        self.wait(2)
        self.acomodar_textos(reglacompleta.bg)
        self.acomodar_textos(reglacompleta)
        self.add_foreground_mobjects(reglacompleta.bg)
        self.add_foreground_mobjects(reglacompleta)
        self.wait(9)
        self.play(ShowCreation(contra_1),ShowCreation(contra_2),run_time=2)
        self.acomodar_textos(t_11.bg)
        self.acomodar_textos(t_11)
        self.add_foreground_mobjects(t_11.bg)
        self.add_foreground_mobjects(t_11)
        self.wait(5)
        self.play(Write(suce3),Write(suce4))
        self.wait()
        self.acomodar_textos(t_12.bg)
        self.acomodar_textos(t_12)
        self.add_foreground_mobjects(t_12.bg)
        self.add_foreground_mobjects(t_12)
        self.wait(10)
        self.acomodar_textos(t_13.bg)
        self.acomodar_textos(t_13)
        self.add_foreground_mobjects(t_13.bg)
        self.add_foreground_mobjects(t_13)
        self.wait(10)
        self.remove_foreground_mobjects(t_11.bg)
        self.remove_foreground_mobjects(t_11)
        self.remove_foreground_mobjects(t_12.bg)
        self.remove_foreground_mobjects(t_12)
        self.remove_foreground_mobjects(t_13.bg)
        self.remove_foreground_mobjects(t_13)
        self.remove_foreground_mobject(Grupo5)
        self.play(FadeOut(Grupo5))
        self.acomodar_textos(t_14.bg)
        self.acomodar_textos(t_14)
        self.add_foreground_mobjects(t_14.bg)
        self.add_foreground_mobjects(t_14)
        self.wait(9)
        self.remove_foreground_mobjects(t_14.bg)
        self.remove_foreground_mobjects(t_14)
        self.remove_foreground_mobjects(t_7.bg)
        self.remove_foreground_mobjects(t_7)
        self.remove_foreground_mobjects(reglacompleta.bg)
        self.remove_foreground_mobjects(reglacompleta)
        self.play(FadeOut(Grupo6))
        self.wait(3)

        self.stop_ambient_camera_rotation()