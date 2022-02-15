from manimlib.imports import *

###################################
###### LIMITES DIRECCIONALES ######
###################################

class LimitesDireccionales(ThreeDScene):
    def rectangulo_texto(self,objeto):
        rect = SurroundingRectangle(objeto,color=WHITE, fill_color=BLACK, fill_opacity=1)
        grupo = VGroup(rect,objeto)
        return grupo
    
    def acomodar_textos(self,objeto):
        self.add_fixed_in_frame_mobjects(objeto)
        self.play(Write(objeto))

    def Introduccion(self):
        ### TEXTOS

        t_1 = TextMobject('Límites Direccionales').scale(1.3)
        t_2 = TextMobject('''Sea $f:D\\subseteq \\mathbb{R}^n\\rightarrow \\mathbb{R}^m$, $x_0\\in Int(D)$ \n
                            y $u\\in \\mathbb{R}^n\\setminus\\{\\overline{0}\\}$. El límite direccional de \n
                            $f$ en $x_0$ en la dirección $u$ es  \n
                            $\\lim_{h\\rightarrow 0}f(x_0+hu)$, $h\in\mathbb{R}$.''')
        t_3 = TextMobject('''Recordemos que en $\mathbb{R}$, para obtener el límite sólo podemos \n
                             aproximarnos por ``la derecha'' y ``la izquierda'' a $x_0$.''')
        t_4 = TextMobject('''Sin embargo, al analizar funciones en $\mathbb{R}^n$, con $n>1$, \n
                             ya no sólo poseemos una dirección para aproximarnos a un\n
                             punto, sino que tenemos una infinidad de ellas.''')
        t_5 = TextMobject('''Veamos un teorema relacionado con las derivadas direccionales.''')
        t_6 = TextMobject('''Teorema: Si existe el límite de $f$ en $x_0$, entonces \n
                            existen todos los límites direccionales y son iguales.''')
        t_7= TextMobject('''Pero, ¿qué significa que para cualquier dirección el límite \n
                            exista y sea el mismo?''')

        ### ANIMACION

        self.play(Write(t_1))
        self.wait(3)
        self.play(ReplacementTransform(t_1,t_2))
        self.wait(29)
        self.play(ReplacementTransform(t_2,t_3))
        self.wait(9)
        self.play(ReplacementTransform(t_3,t_4))
        self.wait(11)
        self.play(ReplacementTransform(t_4,t_5))
        self.wait(4)
        self.play(ReplacementTransform(t_5,t_6))
        self.wait(9)
        self.play(ReplacementTransform(t_6,t_7))
        self.wait(5)
        self.play(*[FadeOut(obj) for obj in self.mobjects])

    def Ejemplo_Teo(self):
        # Para los updaters
        def act_gr_plano(grafica):
            te = t.get_value()
            plano_i.become(
                ParametricSurface(
                lambda u, v: np.array([
                    np.cos(te)*u,
                    np.sin(te)*u,
                    v
                ]),u_min=-4, u_max=4,v_min=-0.5,v_max=4,checkerboard_colors=[GREEN_A, GREEN_B],resolution=(15, 64),fill_opacity=0.6
                )
            )
        def act_gr_par(grafica):
            te = t.get_value()
            parabola_i.become(
                ParametricFunction(lambda x: np.array([np.cos(te)*x,np.sin(te)*x,x**2]),t_min=-1.5,t_max=1.5,color=YELLOW,opacity=0.6)
            )
        def act_vec_direc(vector):
            te = t.get_value()
            direcu.become(
                Arrow(start=(0,0,0),end=(np.cos(te),np.sin(te),0),color=YELLOW,buff=0)
                )

        ### TEXTOS

        t_1 = TextMobject('''Considera la función $f:\\mathbb{R}^2\\rightarrow\\mathbb{R}$ \n
                               dada por $f(x,y) = x^2+y^2$''')
        t_2 = TextMobject('''Podemos notar que la función tiene límite en $(0,0)$ \n
                               y de hecho el límite vale 0.''')
        t_3 = TextMobject('''Considera el vector director en $\\mathbb{R}^2$ $u=(1,0)$''').to_edge(UP).scale(0.7)
        gpot3 = self.rectangulo_texto(t_3)
        t_4 = TextMobject('''Y el plano en $\mathbb{R}^3$ que contiene a $u$ y es ortogonal \n
                             al plano $xy$''').to_edge(UP).scale(0.7)
        gpot4 = self.rectangulo_texto(t_4)
        t_5 = TextMobject('''La intersección del plano anterior y la superficie dada por $f$\n
                             es una curva, y sobre esta curva nos aproximamos al punto en el \n
                             que queremos conocer el límite, comprobando que el límite \n
                             direccional en la dirección $u$ converge a 0.''').to_corner(RIGHT+DOWN).scale(0.6)
        gpot5 = self.rectangulo_texto(t_5)
        t_6 = TextMobject('''Puedes observar que por cualquier dirección que te aproximes\n
                             a $(0,0)$, el límite direccional es $0$.''').to_corner(RIGHT+DOWN).scale(0.6)
        gpot6 = self.rectangulo_texto(t_6)

        ### OBJETOS-GRAFICAS

        axes = ThreeDAxes(x_min = -5, x_max = 5, y_min = -5, y_max = 5,z_min=-1,z_max=5)
        x_label = TexMobject(r"x").scale(0.75).move_to((5.5,0.3,0))
        y_label = TexMobject(r"y").scale(0.75).move_to((0.3,5.5,0))
        ejes = VGroup(axes,x_label,y_label)
        direcu = Arrow(start=(0,0,0),end=(1,0,0),color=YELLOW,buff=0)
        parabola_i = ParametricFunction(lambda x: np.array([np.cos(0)*x,np.sin(0)*x,x**2]),t_min=-1.5,t_max=1.5,color=YELLOW,opacity=0.6)
        plano_i = ParametricSurface(
            lambda u,v: np.array([
                u,
                0,
                v
            ]),u_min=-4, u_max=4,v_min=-0.5,v_max=4,checkerboard_colors=[GREEN_A, GREEN_B],resolution=(15, 64),fill_opacity=0.6
        )
        superficie = ParametricSurface(
            lambda u,v: np.array([
                u,
                v,
                u**2+v**2
            ]),u_min=-1.5,u_max=1.5,v_min=-1.5,v_max=1.5,checkerboard_colors=[RED_A, RED_B],resolution=(15, 64)
        )
        t = ValueTracker(0)

        ### ANIMACION

        self.play(Write(t_1))
        self.wait(8)
        self.play(ReplacementTransform(t_1,t_2))
        self.wait(6)
        self.play(FadeOut(t_2))
        self.acomodar_textos(gpot3)
        self.play(Write(ejes))
        self.play(ShowCreation(direcu))
        self.play(FadeOut(gpot3))
        self.move_camera(phi=80*DEGREES,theta=30*DEGREES,frame_center=(0,0,2))
        self.acomodar_textos(gpot4)
        self.play(ShowCreation(plano_i))
        self.wait(2)
        self.play(ShowCreation(superficie))
        self.wait(2)
        self.play(FadeOut(gpot4))
        self.acomodar_textos(gpot5)
        self.play(Write(parabola_i))
        self.remove(gpot5)
        self.add(gpot5)
        self.wait(15)
        self.play(FadeOut(gpot5))
        self.acomodar_textos(gpot6)

        self.remove(plano_i)
        self.remove(parabola_i)
        self.remove(direcu)
        plano_i.add_updater(act_gr_plano)
        parabola_i.add_updater(act_gr_par)
        direcu.add_updater(act_vec_direc)
        self.add(plano_i)
        self.add(parabola_i)
        self.add(direcu)
        self.bring_to_back(plano_i)
        self.bring_to_back(parabola_i)
        self.bring_to_back(direcu)
        self.play(t.increment_value, 2*np.pi,run_time=4)
        plano_i.remove_updater(act_gr_plano)
        parabola_i.remove_updater(act_gr_par)
        direcu.remove_updater(act_vec_direc)

        self.play(*[FadeOut(obj) for obj in self.mobjects])

    def Regreso(self):
        # Para los updaters
        def act_gr_direc(linea):
            te = t.get_value()
            direc.become(
                ParametricFunction(lambda x: np.array([np.cos(te)*x,np.sin(te)*x,0]),t_min=-4,t_max=4).set_color(YELLOW)
            )
        
        ### TEXTOS
        
        t_1 = TextMobject('''Ahora nos preguntamos, ¿Se vale el regreso del teorema?\n
                             NO''')
        gpot1 = self.rectangulo_texto(t_1)
        t_2 = TextMobject('''Considera la función característica $\\chi:\\mathbb{R}^2\\rightarrow\\mathbb{R}$ \n
                             de la curva $y = x^2$ (vale 1 en los puntos de la curva \n
                             y 0 en lo demás).''').to_edge(UP).scale(0.7)
        gpot2 = self.rectangulo_texto(t_2)
        t_3 = TextMobject('''Observa ahora cómo, para toda dirección, la curva amarilla\n
                             siempre converge a 0 cuando tomamos el límite en (0,0).''').scale(0.6)\
                                                                                        .move_to((0,3,0))#agregar rectangulo
        gpot3 = self.rectangulo_texto(t_3)
        t_4 = TextMobject('''Pero al aproximarnos a (0,0) sobre la curva dada por\n
                             $y=x^2$, el límite resulta 1. Debido a esto, la función \n
                             no tiene límite en (0,0).''').scale(0.6)\
                                                          .move_to((0,3,0))#agregar rectangulo
        gpot4 = self.rectangulo_texto(t_4)
        t_5 = TextMobject('''Sabiendo lo anterior, no caigas en el error de querer\n
                             probar la existencia de un límite utilizando que todos \n
                             los límites direccionales existen y valen lo mismo.''')

        ### OBJETOS-GRAFICAS
        
        axes = ThreeDAxes(x_min = -5, x_max = 5, y_min = -5, y_max = 5,z_min=-1,z_max=4)
        x_label = TexMobject(r"x").scale(0.75).move_to((5.5,0.3,0))
        y_label = TexMobject(r"y").scale(0.75).move_to((0.3,5.5,0))
        ejes = VGroup(axes,x_label,y_label)
        para_1 = ParametricFunction(lambda x: np.array([x,x**2,1]),t_min=-2,t_max=2).set_color(RED_A)
        para_2 = ParametricFunction(lambda x: np.array([x,x**2,0]),t_min=-2,t_max=2).set_color(BLACK)
        func = ParametricSurface(
            lambda u,v: np.array([
                u,
                v,
                0
            ]),u_min=-4, u_max=4,v_min=-4,v_max=4,checkerboard_colors=[RED_A, RED_B],resolution=(15, 64),fill_opacity=0.6 
        )
        direc = ParametricFunction(lambda x: np.array([np.cos(0)*x,np.sin(0)*x,0]),t_min=-4,t_max=4).set_color(YELLOW)
        t = ValueTracker(0)

        ### ANIMACION
        
        self.acomodar_textos(gpot1)
        self.wait(9)
        self.play(FadeOut(gpot1))
        self.move_camera(phi=70*DEGREES,theta=30*DEGREES,frame_center=(0,0,1))
        self.play(Write(ejes))
        self.acomodar_textos(gpot2)
        self.play(ShowCreation(func),ShowCreation(para_1),ShowCreation(para_2))
        self.wait(2)
        self.play(FadeOut(gpot2))
        self.acomodar_textos(gpot3)

        self.remove(direc)
        direc.add_updater(act_gr_direc)
        self.add(direc)
        self.play(t.increment_value, 2*np.pi,run_time=4)
        direc.remove_updater(act_gr_direc)
        self.wait(6)
        self.play(FadeOut(gpot3),FadeOut(direc))
        self.acomodar_textos(gpot4)
        self.wait(11)
        self.remove(para_1)
        para_1.set_color(YELLOW)
        self.add(para_1)
        self.wait(2)
        self.play(*[FadeOut(obj) for obj in self.mobjects])
        self.move_camera(phi=0 * DEGREES,theta=-90*DEGREES,frame_center=(0,0,0))
        self.play(Write(t_5))
        self.wait(9)
        self.play(FadeOut(t_5))

    def Ejemplo_regreso(self):
        ### TEXTOS

        t_1 = TextMobject('''Ahora considera la función
                             $$f(x,y) = \\dfrac{xy}{x^2+y^2}$$''').shift(UP)
        t_2 = TextMobject('''Y toma los vectores directores ''','''$u=(1,0)$''',''' y ''','''$v=(1,1)$''',''' \n
                             para ver el límite en $x_0=(0,0)$''').next_to(t_1,DOWN)
        t_2.set_color_by_tex_to_color_map(
            {
                '''$u=(1,0)$''' : RED,
                '''$v=(1,1)$''' : YELLOW
            }
        )
        t_3 = TextMobject('''Vemos que para ''','''$u$''',''' se tiene
                             $$\\lim_{h\\rightarrow 0}f(x_0+hu)=0$$''').to_edge(UP).scale(0.7)
        t_3.set_color_by_tex_to_color_map(
            {
                '''$u$''' : RED
            }
        )
        gpot3 = self.rectangulo_texto(t_3)
        t_4 = TextMobject('''Mientras que para ''','''$v$''',''' se tiene
                             $$\\lim_{h\\rightarrow 0}f(x_0+hv)=\\frac{1}{2}$$''').to_edge(UP).scale(0.7)
        t_4.set_color_by_tex_to_color_map(
            {
                '''$v$''' : YELLOW
            }
        )
        gpot4 = self.rectangulo_texto(t_4)
        t_5= TextMobject('''Con lo que puedes concluir que el límite de\n
                             $f$ en $(0,0)$ no existe.''').to_corner(UP)
        gpot5 = self.rectangulo_texto(t_5)
        t_6= TextMobject('''¿Podemos usar los límites direccionales \n
                            si $x_0$ está en la frontera del dominio?''')

        ### OBJETOS - GRAFICAS

        axes = ThreeDAxes(x_min = -4, x_max = 4, y_min = -4, y_max = 4,z_min=-1,z_max=3)
        x_label = TexMobject(r"x").scale(0.75).move_to((4.5,0.3,0))
        y_label = TexMobject(r"y").scale(0.75).move_to((0.3,4.5,0))
        ejes = VGroup(axes,x_label,y_label)
        direcu = Arrow(start=(0,0,0),end=(1,0,0),color=RED,buff=0)
        direcv = Arrow(start=(0,0,0),end=(1,1,0),color=YELLOW,buff=0)
        intersecu = ParametricFunction(lambda x: np.array([x,0,0]),t_min=-3,t_max=3,color=RED)
        intersecv = ParametricFunction(lambda x: np.array([x,x,1/2]),t_min=-3,t_max=3,color=YELLOW)
        superficie_1=ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                (u*v)/(u**2+v**2)
            ]),v_min=-3,v_max=-0.005,u_min=-3,u_max=-0.005,fill_opacity=0.7,checkerboard_colors=[GREEN_A,GREEN_B])
        superficie_2=ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                (u*v)/(u**2+v**2)
            ]),v_min=-3,v_max=-0.005,u_min=0.005,u_max=3,fill_opacity=0.7,checkerboard_colors=[GREEN_A,GREEN_B])
        superficie_3=ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                (u*v)/(u**2+v**2)
            ]),v_min=0.005,v_max=3,u_min=-3,u_max=-0.005,fill_opacity=0.7,checkerboard_colors=[GREEN_A,GREEN_B])
        superficie_4=ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                (u*v)/(u**2+v**2)
            ]),v_min=0.005,v_max=3,u_min=0.005,u_max=3,fill_opacity=0.7,checkerboard_colors=[GREEN_A,GREEN_B])
        superficie=VGroup(superficie_1,superficie_2,superficie_3,superficie_4)

        ### ANIMACION

        self.play(Write(t_1))
        self.wait(8)
        self.play(Write(t_2))
        self.wait(7)
        self.play(*[FadeOut(obj) for obj in self.mobjects])
        self.move_camera(phi=75*DEGREES,theta=30*DEGREES,frame_center=(0,0,1))
        self.play(Write(ejes))
        self.play(Write(direcu),Write(direcv))
        self.play(ShowCreation(superficie))
        self.acomodar_textos(gpot3)
        self.play(Indicate(direcu,color=RED,scale_factor=1.5))
        self.play(Write(intersecu))
        self.wait(8)
        self.play(FadeOut(gpot3),FadeOut(intersecu))
        self.acomodar_textos(gpot4)
        self.play(Indicate(direcv,scale_factor=1.5))
        self.play(Write(intersecv))
        self.wait(2)
        self.play(FadeOut(gpot4),FadeOut(intersecv))
        self.acomodar_textos(gpot5)
        self.wait(4)
        self.play(*[FadeOut(obj) for obj in self.mobjects])
        self.move_camera(phi=0 * DEGREES,theta=-90*DEGREES,frame_center=(0,0,0))
        self.play(Write(t_6))
        self.wait(6)
        self.play(FadeOut(t_6))

    def construct(self):
        self.Introduccion()
        self.Ejemplo_Teo()
        self.Regreso()
        self.Ejemplo_regreso()
