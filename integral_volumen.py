from re import S
from manimlib.imports import *

class integral_volumen (ThreeDScene, Scene):
    def setup(self):
        Scene.setup(self)
        ThreeDScene.setup(self)
    def FadeOutWrite3D(self,objeto1,objeto2):
        self.play(FadeOut(objeto1))
        self.acomodar_textos(objeto2)
    def acomodar_textos(self,objeto):
        self.add_fixed_in_frame_mobjects(objeto)
        self.play(Write(objeto)) 
    def puntos_riemann_2D(self):
        puntos = []
        valores_x = [0.2, 0.9, 1.9, 2.825]
        valores_y = [0.1,0.85,1.6,2.8]
        for j in valores_y:
            for i in valores_x:
                punto = Dot(radius=0.075,color=RED).move_to([i,j,0])
                puntos.append(punto)
        return puntos
    def puntos_plano(self):
        puntos = []
        valores_x = [0.2, 0.9, 1.9, 2.825]
        valores_y = [0.1,0.85,1.6,2.8]
        for j in valores_y:
            for i in valores_x:
                punto = Dot(radius=0.075,color=ORANGE).move_to([i,j,j])
                puntos.append(punto)
        return puntos
    def plano_funcion(self):
        plano = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                v
            ]),v_min=0,v_max=3,u_min=0,u_max=3,fill_color=WHITE,fill_opacity=0.60, checkerboard_colors = [WHITE, WHITE], stroke_width=0.01
        )
        return plano
    def particion_1_2D(self):
        particion = []
        valores = [0.375, 1.125, 1.875, 2.625]
        for i in valores:
            for j in valores:
                cuadro = Square(side_length=0.75,fill_opacity=0,stroke_width=1).set_color(GREEN)
                cuadro.move_to((i,j,0))
                particion.append(cuadro)
        return particion
    def particion_2_2D(self):
        particion = []
        valores = [0.1875, 0.5625, 0.9375, 1.3125, 1.6875, 2.0625, 2.4375, 2.8125]
        for i in valores:
            for j in valores:
                cuadro = Square(side_length=0.375,fill_opacity=0,stroke_width=1).set_color(GREEN)
                cuadro.move_to((i,j,0))
                particion.append(cuadro)
        return particion
    def prismas_inf(self):
        prismas = []
        ancho = 3/4
        funcion = [0,0.75,1.5,2.25]
        valores = [0.375, 1.125, 1.875, 2.625]
        for i in range(4):
            for j in range(4):
                prisma = Prism(dimensions=[ancho,ancho,funcion[j]],fill_color=YELLOW,fill_opacity=0.25)
                prisma.move_to((valores[i],valores[j],funcion[j]/2))
                prismas.append(prisma)
        return prismas
    def prismas_sup(self):
        prismas = []
        ancho = 3/4
        funcion = [0.75,1.5,2.25,3]
        valores = [0.375, 1.125, 1.875, 2.625]
        for i in range(4):
            for j in range(4):
                prisma = Prism(dimensions=[ancho,ancho,funcion[j]],fill_color=BLUE,fill_opacity=0.25)
                prisma.move_to((valores[i],valores[j],funcion[j]/2))
                prismas.append(prisma)
        return prismas
    def lineas_inf(self):
        lineas_1 = []
        valores = [0,0.75,1.5,2.25]
        for i in valores:
            linea = ParametricFunction(
                lambda t: np.array([t,i,0]),
                t_min = 0,
                t_max = 3,
                fill_color = RED,
                fill_opacity = 1,
                stroke_width = 0.5,
            ).set_color(RED)
            lineas_1.append(linea)
        return lineas_1
    def lineas_inf_plano(self):
        lineas_1 = []
        valores = [0,0.75,1.5,2.25]
        for i in valores:
            linea = ParametricFunction(
                lambda t: np.array([t,i,i]),
                t_min = 0,
                t_max = 3,
                fill_color = RED,
                fill_opacity = 1,
                stroke_width = 0.5,
            ).set_color(RED)
            lineas_1.append(linea)
        return lineas_1
    def lineas_sup(self):
        lineas_1 = []
        valores = [0.75,1.5,2.25,3]
        for i in valores:
            linea = ParametricFunction(
                lambda t: np.array([t,i,0]),
                t_min = 0,
                t_max = 3,
                fill_color = RED,
                fill_opacity = 1,
                stroke_width = 0.5
            ).set_color(RED)
            lineas_1.append(linea)
        return lineas_1
    def lineas_sup_plano(self):
        lineas_1 = []
        valores = [0.75,1.5,2.25,3]
        for i in valores:
            linea = ParametricFunction(
                lambda t: np.array([t,i,i]),
                t_min = 0,
                t_max = 3,
                fill_color = RED,
                fill_opacity = 1,
                stroke_width = 0.5
            ).set_color(RED)
            lineas_1.append(linea)
        return lineas_1

    def EscenaCero(self):
        #########TEXTOS#########
        titulo = TextMobject("Integral de Volumen").scale(1.5)

        #########Animación#########
        self.play(Write(titulo))
        self.wait()
        self.play(FadeOut(titulo))
        self.wait()
    
    def Dom2D_PrimeraEscena(self):
        # TEXTOS
        texto_1 = TextMobject('''Consideremos la siguiente función''').move_to(1*UP)
        texto_2 = TextMobject('''$f:A=[0,3]\\times[0,3]\\subset \\mathbb{R}^2 \\to \\mathbb{R}$ \n
                                 $f(x,y) = y$''')
        texto_3 = TextMobject(''' A continuación veamos cómo construir la integral\n
                                 de la función $f$ sobre su dominio ''').move_to(1.5*UP)
        texto_4 = TextMobject(''' Consideremos una partición $\\mathcal{P}$ sobre el dominio $A$ ''').move_to(3*UP)
        texto_5 = TexMobject(r"\mathcal{P}:=\{0,0.75,1.5,2.25,3\}\times\{0,0.75,1.5,2.25,3\}").move_to(3*UP).scale(0.9)
        texto_6 = TextMobject(''' La partición $\\mathcal{P}$ induce un conjunto de 16 rectángulos\n
                                  pequeños, que llamaremos $R$, de área $0.75^2$ dentro de $A$''').move_to(3*UP)
        texto_6_5 = TextMobject('''Nota que $\\mathcal{P}$ es el conjunto de vértices de los rectángulos''').next_to(texto_6,DOWN)
        texto_7 = TextMobject(''' Definimos la suma superior de Darboux sobre $\\mathcal{P}$ como\n
                                $\\mathcal{U}(f,\\mathcal{P}):= \\sum_{i=1}^{16}M_i(0.75^2)$ ''').move_to(3.2*UP)
        texto_7_5 = TextMobject('''Donde $M_i=\\sup\\{f(x,y)|(x,y)\\in R_i\\}$''').next_to(texto_7,DOWN)
        texto_8 = TextMobject(''' Como $f(x,y)=y$, los valores supremos corresponden a\n
                                  cualquier punto sobre el lado del rectángulo donde \n
                                  $y$ es mayor y constante''').move_to(3*UP)
        texto_9 = TextMobject('''Análogamente, definimos la suma inferior de Darboux sobre $\\mathcal{P}$ como\n
                                $\\mathcal{L}(f,\\mathcal{P}):= \\sum_{i=1}^{16}m_i(0.75^2)$ ''').move_to(3.2*UP)
        texto_9_5 = TextMobject('''Donde $m_i=\\inf\\{f(x,y)|(x,y)\\in R_i\\}$''').next_to(texto_9,DOWN)
        texto_10 = TextMobject(''' Como $f(x,y)=y$, los valores ínfimos corresponden a\n
                                   cualquier punto sobre el lado del rectángulo donde \n
                                   $y$ es menor y constante''').move_to(3*UP)
        texto_11 = TextMobject(''' Para toda partición $\\mathcal{P}$,\n
                                 $\\mathcal{L}(f,\\mathcal{P})\\leq\\mathcal{U}(f,\\mathcal{P})$''').move_to(3*UP)
        texto_12 = TextMobject(''' Consideremos un refinamiento $\\mathcal{P}'$ de la partición $\\mathcal{P}$ ''').move_to(3*UP)
        texto_13 = TextMobject(''' Resulta que \n
                                $\\mathcal{L}(f,\\mathcal{P})\\leq\\mathcal{L}(f,\\mathcal{P}')\\leq\\mathcal{U}(f,\\mathcal{P}')\\leq\\mathcal{U}(f,\\mathcal{P})$ ''').move_to(3*UP)
        texto_14_1 = TextMobject(''' Definimos la integral superior de Darboux como ''').move_to(1*UP)
        texto_14_2 = TexMobject(r"\overline{\iint}f(x,y)dxdy:=\text{inf}\{\mathcal{U}(f,\mathcal{P})|\mathcal{P}\text{ partición de }A\}")
        texto_15_1 = TextMobject(''' Así mismo, se define la integral inferior de Darboux como ''').move_to(1*UP)
        texto_15_2 = TexMobject(r"\underline{\iint}f(x,y)dxdy:=\text{sup}\{\mathcal{L}(f,\mathcal{P})|\mathcal{P}\text{ partición de }A\}")
        texto_16_1 = TextMobject(''' Cuando las integrales superior e inferior de Darboux coinciden\n
                                    en un valor, a este se le llama Integral de Darboux''').move_to(1*UP)
        texto_16_2 = TexMobject(r"\iint f(x,y)\text{ }dxdy").next_to(texto_16_1,1.5*DOWN)
        nota_1 = TextMobject('''Para aproximar el volumen debajo de la superficie, \n
                                consideramos un paralelepípedo de base $R_i$ y altura $M_i$, \n
                                cuyo volumen es $M_i$ por el área de $R_i$, al tomar \n
                                todos los paralelepípedos, obtenemos el volumen $U(f,P)$ \n
                                que se muestra en azul''').scale(0.5).move_to((4,-1,0))
        nota_2 = TextMobject('''Esta vez el volumen debajo de la superficie lo \n
                                aproximamos con el volumen $L(f,P)$ de los \n
                                paralelepípedos en amarillo''').scale(0.5).move_to((4,-1,0))

        # GRUPOS CONVENIENTES

        texto_6_gp = VGroup(texto_6,texto_6_5)
        texto_7_gp = VGroup(texto_7,texto_7_5)
        texto_9_gp = VGroup(texto_9,texto_9_5).scale(0.9)

        # FIGURAS
        figura = Square(side_length=3,fill_opacity=0,stroke_width=1).move_to((1.5,1.5,0))
        particion_1 = self.particion_1_2D()
        particion_2 = self.particion_2_2D()
        gpo_particion_1 = VGroup(*self.particion_1_2D())
        gpo_particion_2 = VGroup(*self.particion_2_2D())
        lineas_sup = self.lineas_sup()
        lineas_inf = self.lineas_inf()
        lineas_sup_plano = self.lineas_sup_plano()
        lineas_inf_plano = self.lineas_inf_plano()
        prismas_sup = self.prismas_sup()
        prismas_inf = self.prismas_inf()
        gpo_prismas_sup = VGroup(*prismas_sup)
        gpo_prismas_inf = VGroup(*prismas_inf)
        plano = self.plano_funcion()

        # EJES
        #ejes_pos = np.array([0,0,0])
        axes = ThreeDAxes(x_min=-3.5,x_max=3.5,y_min=-3.5,y_max=3.5,z_min=-1,z_max=3.5,num_axis_pieces= 30)
        x_label = TexMobject(r"x").scale(0.75).move_to(np.array([3.5,0.3,0]))
        y_label = TexMobject(r"y").scale(0.75).move_to(np.array([0.3,3.5,0]))
        #Grupote = VGroup(*particion_1,*particion_2,gpo_particion_1,gpo_particion_2,figura,*lineas_sup,*lineas_inf,axes,x_label,y_label).move_to((0,-1.5,0))

        # ANIMACION
        self.play(Write(texto_1))
        self.wait()
        self.play(Write(texto_2))
        self.wait(2)
        self.FadeOutWrite3D(texto_1,texto_3)
        self.wait(3)
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )
        self.move_camera(phi=80 * DEGREES,theta=40*DEGREES,frame_center=(0,0,2))
        self.play(ShowCreation(axes),ShowCreation(x_label),ShowCreation(y_label),ShowCreation(plano))
        self.play(DrawBorderThenFill(figura))
        self.wait()
        self.acomodar_textos(texto_4)
        self.wait(2)
        self.FadeOutWrite3D(texto_4,texto_5)
        self.wait(3)
        self.FadeOutWrite3D(texto_5,texto_6_gp)
        self.wait(3)
        for i in particion_1:
            self.play(Write(i),run_time=0.05)
        self.wait()
        self.FadeOutWrite3D(texto_6_gp,texto_7_gp)
        self.play(FadeIn(gpo_prismas_sup))
        self.begin_ambient_camera_rotation(rate=0.15)
        self.acomodar_textos(nota_1)
        self.wait(10)
        self.play(FadeOut(nota_1))
        self.stop_ambient_camera_rotation()
        self.move_camera(phi=85 * DEGREES,theta=30*DEGREES,frame_center=(0,0,2))
        self.FadeOutWrite3D(texto_7_gp,texto_8)
        self.wait(3)
        for i in range(len(lineas_sup)):
            self.play(Write(lineas_sup[i]),Write(lineas_sup_plano[i]),run_time=1)
            self.play(FadeOut(lineas_sup[i]),FadeOut(lineas_sup_plano[i]))
        self.move_camera(phi=80 * DEGREES,theta=40*DEGREES,frame_center=(0,0,2))
        self.wait()
        self.play(FadeOut(gpo_prismas_sup))
        self.FadeOutWrite3D(texto_8,texto_9_gp)
        self.play(FadeIn(gpo_prismas_inf))
        self.begin_ambient_camera_rotation(rate=0.15)
        self.acomodar_textos(nota_2)
        self.wait(5)
        self.play(FadeOut(nota_2))
        self.stop_ambient_camera_rotation()
        self.move_camera(phi=85 * DEGREES,theta=30*DEGREES,frame_center=(0,0,2))
        self.FadeOutWrite3D(texto_9_gp,texto_10)
        self.wait(3)
        for i in range(len(lineas_inf)):
            self.play(Write(lineas_inf[i]),Write(lineas_inf_plano[i]),run_time=1)
            self.play(FadeOut(lineas_inf[i]),FadeOut(lineas_inf_plano[i]))
        self.move_camera(phi=80 * DEGREES,theta=40*DEGREES,frame_center=(0,0,2))
        self.wait()
        self.play(FadeOut(gpo_prismas_inf))
        self.FadeOutWrite3D(texto_10,texto_11)
        self.wait(3)
        self.FadeOutWrite3D(texto_11,texto_12)
        self.wait(2)
        self.play(ReplacementTransform(gpo_particion_1,gpo_particion_2))
        self.wait()
        self.FadeOutWrite3D(texto_12,texto_13)
        self.wait(2)
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )
        self.move_camera(phi=0 * DEGREES,theta=-90*DEGREES,frame_center=(0,0,0))
        self.play(Write(texto_14_1))
        self.wait()
        self.play(Write(texto_14_2))
        self.wait(3)
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )
        self.play(Write(texto_15_1))
        self.wait()
        self.play(Write(texto_15_2))
        self.wait(3)
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )
        self.play(Write(texto_16_1))
        self.wait()
        self.play(Write(texto_16_2))
        self.wait(3)
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )
    
    def Dom2D_SegundaEscena(self):
        #########TEXTOS#########
        texto_1 = TextMobject(''' Regresemos  a la partición $\mathcal{P}$ y consideremos \n
                                  un conjunto que tome cualquier punto $(x_i,y_i)$ dentro de \n 
                                  cada rectángulo pequeño $R_i$ ''').move_to(3*UP)
        texto_2 = TextMobject(''' Entonces definimos la suma de Riemann como\n
                                $\\mathcal{R}(f,\\mathcal{P}):= \\sum_{i=1}^{16}f(x_i,y_i)(0.75^2)$ ''').move_to(3*UP)
        texto_3 = TextMobject(''' Obsérvese en el ejemplo cómo la imagen del punto $(x_i,y_i)$ \n
                                    es menor que el supremo de la función en el \n
                                    rectángulo correspondiente para cualquier $i$ ''').move_to(3*UP)
        texto_4 = TextMobject(''' También véase cómo la imagen del punto $(x_i,y_i)$ es\n
                                  mayor que el ínfimo de la función en el rectángulo \n
                                  correspondiente para cualquier $i$''').move_to(3*UP)
        texto_5 = TextMobject(''' Resulta que para toda partición $\\mathcal{P}$ y colección\n
                                 de puntos $(x_i,y_i)$ en $R_{i}$, se tiene que\n
                                $\\mathcal{L}(f,\\mathcal{P})\\leq\\mathcal{R}(f,\\mathcal{P})\\leq\\mathcal{U}(f,\\mathcal{P})$''').move_to(3*UP)
        texto_6 = TextMobject(''' Decimos que $f$ es Riemann integrable si $\\mathcal{R}(f,\\mathcal{P})$\n
                                 converge conforme $\\mathcal{P}$ se vuelve más fina. ''').move_to(3*UP)
        texto_7 = TextMobject('''Investiga qué es la norma de una partición y expresa \n
                                 la integral de Riemann, la integral superior e inferior \n
                                 usando este concepto''').move_to(3*UP)

        # FIGURAS
        figura = Square(side_length=3,fill_opacity=0,stroke_width=1).move_to((1.5,1.5,0))
        particion_1 = self.particion_1_2D()
        particion_2 = self.particion_2_2D()
        gpo_particion_1 = VGroup(*self.particion_1_2D())
        gpo_particion_2 = VGroup(*self.particion_2_2D())
        lineas_sup = self.lineas_sup()
        lineas_inf = self.lineas_inf()
        gpo_lineas_sup = VGroup(*lineas_sup)
        gpo_lineas_inf = VGroup(*lineas_inf)
        lineas_sup_plano = self.lineas_sup_plano()
        lineas_inf_plano = self.lineas_inf_plano()
        gpo_lineas_sup_plano = VGroup(*lineas_sup_plano)
        gpo_lineas_inf_plano = VGroup(*lineas_inf_plano)
        plano = self.plano_funcion()
        puntos = self.puntos_riemann_2D()
        puntos_plano = self.puntos_plano()
        gpo_puntos = VGroup(*puntos)
        gpo_puntos_plano = VGroup(*puntos_plano)

        # EJES
        axes = ThreeDAxes(x_min=-3.5,x_max=3.5,y_min=-3.5,y_max=3.5,z_min=-1,z_max=3.5,num_axis_pieces= 30)
        x_label = TexMobject(r"x").scale(0.75).move_to((3.5,0.3,0))
        y_label = TexMobject(r"y").scale(0.75).move_to((0.3,3.5,0))

        # Animación
        self.move_camera(phi=80 * DEGREES,theta=30*DEGREES,frame_center=(0,0,2))
        self.acomodar_textos(texto_1)
        self.wait(3)
        self.play(ShowCreation(axes),ShowCreation(x_label),ShowCreation(y_label),ShowCreation(plano))
        self.play(DrawBorderThenFill(figura))
        self.play(FadeIn(gpo_particion_1))
        self.wait()
        self.play(FadeIn(gpo_puntos))
        self.wait()
        self.FadeOutWrite3D(texto_1,texto_2)
        self.play(FadeIn(gpo_puntos_plano))
        self.wait(3)
        self.FadeOutWrite3D(texto_2,texto_3)
        self.wait(3)
        self.move_camera(phi=82 * DEGREES,theta=30*DEGREES,frame_center=(0,0,2))
        self.play(FadeIn(gpo_lineas_sup),FadeIn(gpo_lineas_sup_plano))
        self.play(Indicate(gpo_lineas_sup,color=BLUE,scale_factor=1.5),Indicate(gpo_lineas_sup_plano,color=BLUE,scale_factor=1.5),run_time=3)
        self.play(FadeOut(gpo_lineas_sup),FadeOut(gpo_lineas_sup_plano))
        self.wait()
        self.FadeOutWrite3D(texto_3,texto_4)
        self.play(FadeIn(gpo_lineas_inf),FadeIn(gpo_lineas_inf_plano))
        self.play(Indicate(gpo_lineas_inf,color=YELLOW,scale_factor=1.5),Indicate(gpo_lineas_inf_plano,color=YELLOW,scale_factor=1.5),run_time=3)
        self.play(FadeOut(gpo_lineas_inf),FadeOut(gpo_lineas_inf_plano))
        self.move_camera(phi=80 * DEGREES,theta=30*DEGREES,frame_center=(0,0,2))
        self.wait()
        self.play(FadeOut(gpo_puntos_plano))
        self.FadeOutWrite3D(texto_4,texto_5)
        self.wait(4)
        self.FadeOutWrite3D(texto_5,texto_6)
        self.wait(3)
        self.play(FadeOut(gpo_puntos))
        self.play(ReplacementTransform(gpo_particion_1,gpo_particion_2))
        self.wait()
        self.FadeOutWrite3D(texto_6,texto_7)
        self.wait(3)
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )
    
    def construct(self):
        self.EscenaCero()
        self.Dom2D_PrimeraEscena()
        self.Dom2D_SegundaEscena()