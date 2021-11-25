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
    def punto3D(self):
        bola = ParametricSurface(
            lambda u, v: np.array([
                0.075*np.cos(v) * np.sin(u),
            0.075*np.sin(v) * np.sin(u),
            0.075*np.cos(u)
            ]),v_min=0,v_max=TAU,u_min=0.001,u_max=PI-0.001,
            resolution=(24,24),fill_opacity=1,stroke_color=RED,fill_color=RED)
        return bola
    def get_figure(self):
        figura = Cube(side_length=0.75,fill_opacity=0,stroke_width=1).set_color(GREEN)
        return figura   
    def particion_1(self):
        particion = []
        valores = [0.375, 1.125, 1.875, 2.625]
        for k in valores:
            for i in valores:
                for j in valores:
                    cubo = self.get_figure()
                    cubo.move_to((i,j,k))
                    particion.append(cubo)
        return particion
    def particion_2(self):
        particion = []
        valores = [0.1875, 0.5625, 0.9375, 1.3125, 1.6875, 2.0625, 2.4375, 2.8125]
        for k in valores:
            for i in valores:
                for j in valores:
                    cubo = Cube(side_length=0.375,fill_opacity=0,stroke_width=1).set_color(GREEN)
                    cubo.move_to((i,j,k))
                    particion.append(cubo)
        return particion
    def puntos_riemann(self):
        puntos =[]
        valores_x = [0.2, 0.9, 1.9, 2.825]
        valores_y = [0.1,0.85,1.6,2.8]
        valores_z =[0.2, 0.9, 1.7, 2.75]
        for k in valores_z:
            for i in valores_x:
                for j in valores_y:
                    punto = Dot(radius=0.075,color=RED).move_to((i,j,k))
                    puntos.append(punto)
        return puntos
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
    def planos_sup(self):
        planos_1 = []
        valores = [0.75,1.5,2.25,3]
        for i in valores:
            plano = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                i
            ]),v_min=0,v_max=3,u_min=0,u_max=3,fill_color=BLUE,fill_opacity=0.50, checkerboard_colors = [BLUE, BLUE], stroke_width=0.01)
            planos_1.append(plano)
        return planos_1
    def planos_inf(self):
        planos_1 = []
        valores = [0,0.75,1.5,2.25]
        for i in valores:
            plano = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                i
            ]),v_min=0,v_max=3,u_min=0,u_max=3,fill_color=YELLOW,fill_opacity=0.50, checkerboard_colors = [YELLOW, YELLOW], stroke_width=0.01)
            planos_1.append(plano)
        return planos_1
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
    
    def PrimeraEscena(self):
        #########TEXTOS#########
        texto_1 = TextMobject(''' Consideremos la siguiente función ''').move_to(1*UP)
        texto_2 = TextMobject(''' $f:A=[0,3]\\times[0,3]\\times[0,3]\\subset \\mathbb{R}^3\\to \\mathbb{R}$\n
                                $f(x,y,z)=z$ ''')
        texto_3 = TextMobject(''' A continuación veamos cómo construir la integral\n
                                 de la función $f$ sobre su dominio ''').move_to(1.5*UP)
        texto_4 = TextMobject(''' Consideremos una partición $\\mathcal{P}$ sobre el dominio $A$ ''').move_to(3*UP)
        texto_5 = TexMobject(r"\mathcal{P}:=\{0,0.75,1.5,2.25,3\}\times\{0,0.75,1.5,2.25,3\}\times\{0,0.75,1.5,2.25,3\}").move_to(3*UP).scale(0.8)
        texto_6 = TextMobject(''' La partición $\\mathcal{P}$ genera un conjunto de 64 cubos\n
                                pequeños ($\\Lambda_{\\mathcal{P}}$) de volumen $0.75^3\\text{u}^3$ dentro de $A$''').move_to(3*UP)
        texto_7 = TextMobject(''' Definimos la suma superior de Darboux sobre $\\mathcal{P}$ como\n
                                $\\mathcal{U}(f,\\mathcal{P}):= \\sum_{i=1}^{64}\\text{sup}\\{f(x,y,z)|(x,y,z)\\in( \\Lambda_{\\mathcal{P}})_i\\}(0.75^3)$ ''').move_to(3*UP)
        texto_8 = TextMobject(''' Como $f(x,y,z)=z$, los valores supremos corresponden \n
                                a cualquier punto sobre la cara superior de cada cubo pequeño ''').move_to(3*UP)
        texto_9 = TextMobject(''' Y la suma inferior de Darboux sobre $\\mathcal{P}$ se define como\n
                                $\\mathcal{L}(f,\\mathcal{P}):= \\sum_{i=1}^{64}\\text{inf}\\{f(x,y,z)|(x,y,z)\\in( \\Lambda_{\\mathcal{P}})_i\\}(0.75^3)$ ''').move_to(3*UP)
        texto_10 = TextMobject(''' Como $f(x,y,z)=z$, los valores ínfimos corresponden \n
                                a cualquier punto sobre la cara inferior de cada cubo pequeño ''').move_to(3*UP)
        texto_11 = TextMobject(''' Para toda partición $\\mathcal{P}$,\n
                                 $\\mathcal{L}(f,\\mathcal{P})\\leq\\mathcal{U}(f,\\mathcal{P})$''').move_to(3*UP)
        texto_12 = TextMobject(''' Consideremos un refinamiento $\\mathcal{P}'$ de la partición $\\mathcal{P}$ ''').move_to(3*UP)
        texto_13 = TextMobject(''' Resulta que \n
                                $\\mathcal{L}(f,\\mathcal{P})\\leq\\mathcal{L}(f,\\mathcal{P}')\\leq\\mathcal{U}(f,\\mathcal{P}')\\leq\\mathcal{U}(f,\\mathcal{P})$ ''').move_to(3*UP)
        texto_14_1 = TextMobject(''' Definimos la integral superior de Darboux como ''').move_to(1*UP)
        texto_14_2 = TexMobject(r"\overline{\iiint}f(x,y,z)dxdydz:=\text{inf}\{\mathcal{U}(f,\mathcal{P})|\mathcal{P}\text{ partición de }A\}")
        texto_15_1 = TextMobject(''' Así mismo, se define la integral inferior de Darboux como ''').move_to(1*UP)
        texto_15_2 = TexMobject(r"\underline{\iiint}f(x,y,z)dxdydz:=\text{sup}\{\mathcal{L}(f,\mathcal{P})|\mathcal{P}\text{ partición de }A\}")
        texto_16_1 = TextMobject(''' Cuando las integrales superior e inferior de Darboux coinciden\n
                                    en un valor, a este se le llama Integral de Darboux''').move_to(1*UP)
        texto_16_2 = TexMobject(r"\iiint f(x,y,z)\text{ }dxdydz").next_to(texto_16_1,1.5*DOWN)
        #########OBJETOS#########
        #Figuras
        figura = Cube(side_length=3,fill_opacity=0,stroke_width=1).move_to((1.5,1.5,1.5))
        particion_1 = self.particion_1()
        gpo_particion_1 = VGroup(*particion_1)
        particion_2 = self.particion_2()
        gpo_particion_2 = VGroup(*particion_2)
        planos_1_sup = self.planos_sup()
        planos_1_inf = self.planos_inf()
        #Ejes
        axes = ThreeDAxes(x_min=-3.5,x_max=3.5,y_min=-3.5,y_max=3.5,z_min=-1,z_max=3.5,num_axis_pieces= 30)
        x_label = TexMobject(r"x").scale(0.75).move_to((3.5,0.3,0))
        y_label = TexMobject(r"y").scale(0.75).move_to((0.3,3.5,0))

        #########Animación#########
        self.play(Write(texto_1))
        self.wait()
        self.play(Write(texto_2))
        self.wait(2)
        self.FadeOutWrite3D(texto_1,texto_3)
        self.wait(3)
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )
        self.move_camera(phi=80 * DEGREES,theta=30*DEGREES,frame_center=(0,0,2))
        self.play(ShowCreation(axes),ShowCreation(x_label),ShowCreation(y_label))
        self.play(DrawBorderThenFill(figura))
        self.wait()
        self.acomodar_textos(texto_4)
        self.wait(2)
        self.FadeOutWrite3D(texto_4,texto_5)
        self.wait(3)
        self.FadeOutWrite3D(texto_5,texto_6)
        self.wait(3)
        for i in particion_1:
            self.play(Write(i),run_time=0.05)
        self.wait()
        self.FadeOutWrite3D(texto_6,texto_7)
        self.wait(3)
        self.FadeOutWrite3D(texto_7,texto_8)
        self.wait(3)
        self.move_camera(phi=85 * DEGREES,theta=30*DEGREES,frame_center=(0,0,2))
        for i in planos_1_sup:
            self.play(Write(i),run_time=0.25)
            self.play(FadeOut(i))
        self.move_camera(phi=80 * DEGREES,theta=30*DEGREES,frame_center=(0,0,2))
        self.wait()
        self.FadeOutWrite3D(texto_8,texto_9)
        self.wait(3)
        self.FadeOutWrite3D(texto_9,texto_10)
        self.wait(3)
        self.move_camera(phi=85 * DEGREES,theta=30*DEGREES,frame_center=(0,0,2))
        for i in planos_1_inf:
            self.play(Write(i),run_time=0.25)
            self.play(FadeOut(i))
        self.move_camera(phi=80 * DEGREES,theta=30*DEGREES,frame_center=(0,0,2))
        self.wait()
        self.FadeOutWrite3D(texto_10,texto_11)
        self.wait(3)
        self.FadeOutWrite3D(texto_11,texto_12)
        self.wait(2)
        self.play(ReplacementTransform(gpo_particion_1,gpo_particion_2))
        self.FadeOutWrite3D(texto_12,texto_13)
        self.wait(5)
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
    
    def SegundaEscena(self):
        #########TEXTOS#########
        texto_1 = TextMobject(''' Regresemos  a la partición $\mathcal{P}$ y consideremos \n
        un conjunto que tome cualquier punto $(x_i,y_i,z_i)$ dentro de \n 
        cada cubo pequeño $(\Lambda_{\mathcal{P}})_i$ ''').move_to(3*UP)
        texto_2 = TextMobject(''' Entonces definimos la suma de Riemann como\n
                                $\\mathcal{R}(f,\\mathcal{P}):= \\sum_{i=1}^{64}f(x_i,y_i,z_i)(0.75^3)$ ''').move_to(3*UP)
        texto_3 = TextMobject(''' Obsérvese en el ejemplo cómo todos los puntos $(x_i,y_i,z_i)$ \n
                                    están por debajo de los valores supremos en cada cubo ''').move_to(3*UP)
        texto_4 = TextMobject(''' También véase cómo todos los puntos $(x_i,y_i,z_i)$ están\n
                                 por encima de los valores ínfimos en cada cubo''').move_to(3*UP)
        texto_5 = TextMobject(''' Resulta que para toda partición $\\mathcal{P}$ y colección\n
                                 de puntos $(x_i,y_i,z_i)$ en $(\\Lambda_{\\mathcal{P}})_{i}$, se tiene que\n
                                $\\mathcal{L}(f,\\mathcal{P})\\leq\\mathcal{R}(f,\\mathcal{P})\\leq\\mathcal{U}(f,\\mathcal{P})$''').move_to(3*UP)
        texto_6 = TextMobject(''' Decimos que $f$ es Riemann integrable si $\\mathcal{R}(f,\\mathcal{P})$\n
                                 existe conforme $\\mathcal{P}$ se vuelve más fina. ''').move_to(3*UP)
        texto_7 = TextMobject(''' En el límite, se define la Integral de Riemann, \n
                                 $\\iiint f(x,y,z)\\text{ }dxdydz$  ''').move_to(3*UP)
        texto_8 = TextMobject(''' Entonces, si\n
                                    $\\overline{\\iiint}f(x,y,z)dxdydz= \\underline{\\iiint}f(x,y,z)dxdydz$, \n
                                    decimos que la integral de Darboux es \n
                                    equivalente a la integral de Riemann''')
        texto_8_1 = TextMobject(''' Entonces, si ''').move_to(1.5*UP)
        texto_8_2 = TexMobject(r" \overline{\iiint}f(x,y,z)dxdydz= \underline{\iiint}f(x,y,z)dxdydz,").next_to(texto_8_1,1.5*DOWN)
        texto_8_3 = TextMobject(''' decimos que la integral de Darboux es \n
                                    equivalente a la integral de Riemann ''').next_to(texto_8_2,1.5*DOWN)
        texto_8 = VGroup(texto_8_1,texto_8_2,texto_8_3)
        #########OBJETOS######### 
        #Figuras
        figura = Cube(side_length=3,fill_opacity=0,stroke_width=1).move_to((1.5,1.5,1.5))
        particion_1 = self.particion_1()
        gpo_particion_1 = VGroup(*particion_1)
        particion_2 = self.particion_2()
        gpo_particion_2 = VGroup(*particion_2)
        puntos = self.puntos_riemann()
        gpo_puntos = VGroup(*puntos)
        planos_1_sup = self.planos_sup()
        gpo_planos_1_sup = VGroup(*planos_1_sup)
        planos_1_inf = self.planos_inf()
        gpo_planos_1_inf = VGroup(*planos_1_inf)
        #Ejes
        axes = ThreeDAxes(x_min=-3.5,x_max=3.5,y_min=-3.5,y_max=3.5,z_min=-1,z_max=3.5,num_axis_pieces= 30)
        x_label = TexMobject(r"x").scale(0.75).move_to((3.5,0.3,0))
        y_label = TexMobject(r"y").scale(0.75).move_to((0.3,3.5,0))

        #########Animación#########
        self.move_camera(phi=80 * DEGREES,theta=30*DEGREES,frame_center=(0,0,2))
        self.acomodar_textos(texto_1)
        self.wait(3)
        self.play(ShowCreation(axes),ShowCreation(x_label),ShowCreation(y_label))
        self.play(DrawBorderThenFill(figura))
        self.play(FadeIn(gpo_particion_1))
        self.wait()
        self.play(FadeIn(gpo_puntos))
        self.wait()
        self.FadeOutWrite3D(texto_1,texto_2)
        self.wait(3)
        self.FadeOutWrite3D(texto_2,texto_3)
        self.wait(3)
        self.move_camera(phi=82 * DEGREES,theta=30*DEGREES,frame_center=(0,0,2))
        self.play(FadeIn(gpo_planos_1_sup))
        self.wait(3)
        self.play(FadeOut(gpo_planos_1_sup))
        self.wait()
        self.FadeOutWrite3D(texto_3,texto_4)
        self.play(FadeIn(gpo_planos_1_inf))
        self.wait(3)
        self.play(FadeOut(gpo_planos_1_inf))
        self.move_camera(phi=80 * DEGREES,theta=30*DEGREES,frame_center=(0,0,2))
        self.wait()
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
        self.move_camera(phi=0 * DEGREES,theta=-90*DEGREES,frame_center=(0,0,0))
        self.play(Write(texto_8))
        self.wait(5)
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )
    
    def TerceraEscena(self):
        #########TEXTOS#########
        texto_1 = TextMobject(''' Consideremos ahora la siguiente función $f$''').move_to(1*UP)
        texto_2 = TextMobject(''' $f:A=[0,3]\\times[0,3]\\times[0,3]\\subset \\mathbb{R}^3\\to \\mathbb{R}$\n
                                $f(x,y,z)=z$ ''')
        texto_3 = TextMobject(''' Veamos en qué consiste resolver la integral de volumen\n
                                 de la función $f$ sobre su dominio $A$ ''').move_to(1*UP)
        texto_4 = TexMobject(r"\iiint_{A}z\text{ }dV=\int_{0}^{3}\int_{0}^{3}\int_{0}^{3}z\text{ }dxdydz").next_to(texto_3,1.5*DOWN)
        texto_4_1 = TextMobject(''' Recordemos que este es el dominio de integración,\n
                                     $A\\subset \\mathbb{R}^3$, y no la gráfica de $f$, contenida en $\\mathbb{R}^4$ ''').move_to(3*UP)
        texto_5 = TextMobject(''' Consideremos un conjunto de puntos $(x,y_0,z_0)\\subset A$,\n
                                     con $y_0,z_0\\in[0,3]$, fijos ''').move_to(3*UP)
        texto_6 = TextMobject(''' Para cada par $y_0,z_0\\in[0,3]$, es posible realizar la integral de $f$\n
                                en la región $(x,y_0,z_0)\\subset A$, $S(y_0,z_0)=\\int_{0}^{3}f(x,y_0,z_0)\\text{ } dx$ ''').move_to(3*UP)
        texto_int_A = TexMobject(r"S(y_0,z_0)=\int_{0}^{3}f(x,y_0,z_0)\text{ } dx").move_to(0.5*UP+4*RIGHT).scale(0.7).set_color(YELLOW)
        texto_7 = TextMobject(''' Ahora mantenemos fijo $z_0$ y notamos que $S(y,z_0)$ es integrable \n
                                para toda $y\\in[0,3]$, entonces obtenemos $S'(z_0)=\\int_0^3S(y,z_0)\\text{ }dy$ ''').move_to(3*UP)
        texto_int_A2 = TexMobject(r"S'(z_0)=\int_0^3S(y,z_0)\text{ }dy").next_to(texto_int_A,0.7*DOWN).scale(0.7).set_color(ORANGE)              
        texto_8 = TextMobject(''' Análogamente, $S'(z)$ es integrable para toda $z\\in[0,3]$, \n
                                entonces obtenemos $\\iiint_{A}f(x,y,z)\\text{ }dV=\\int_0^3S'(z)\\text{ } dz$ ''').move_to(3*UP)
        texto_int_final = TexMobject(r"\iiint_{A}f(x,y,z)\text{ }dV=\int_0^3S'(z)\text{ } dz").scale(0.7).next_to(texto_int_A2,0.7*DOWN).set_color(BLUE)
        #########OBJETOS######### 
        #Figuras
        figura = Cube(side_length=3,fill_opacity=0,stroke_width=1).move_to((1.5,1.5,1.5))
        figura_final = Cube(side_length=3,fill_opacity=0.7,stroke_width=1).move_to((1.5,1.5,1.5)).set_color(BLUE)
        
        linea_1 = Line((0,1,1),(3,1,1)).set_color(YELLOW)

        linea_2 = Line((0,2,1.7),(3,2,1.7)).set_color(YELLOW)
        linea_3 = Line((0,1.5,2.5),(3,1.5,2.5)).set_color(YELLOW)
        linea_4 = Line((0,2.5,0.5),(3,2.5,0.5)).set_color(YELLOW)
        lineas_1 = VGroup(linea_2,linea_3,linea_4)

        linea_5 = Line((0,1.5,1),(3,1.5,1)).set_color(YELLOW)
        linea_6 = Line((0,2,1),(3,2,1)).set_color(YELLOW)
        linea_7 = Line((0,2.5,1),(3,2.5,1)).set_color(YELLOW)
        lineas_2 = VGroup(linea_5,linea_6,linea_7)

        plano_1 = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                1
            ]),v_min=0,v_max=3,u_min=0,u_max=3,fill_color=ORANGE,fill_opacity=0.80, checkerboard_colors = [ORANGE, ORANGE], stroke_width=0.01)

        plano_2 = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                1.5
            ]),v_min=0,v_max=3,u_min=0,u_max=3,fill_color=ORANGE,fill_opacity=0.80, checkerboard_colors = [ORANGE, ORANGE], stroke_width=0.01)
        plano_3 = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                2
            ]),v_min=0,v_max=3,u_min=0,u_max=3,fill_color=ORANGE,fill_opacity=0.80, checkerboard_colors = [ORANGE, ORANGE], stroke_width=0.01)
        plano_4 = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                2.5
            ]),v_min=0,v_max=3,u_min=0,u_max=3,fill_color=ORANGE,fill_opacity=0.80, checkerboard_colors = [ORANGE, ORANGE], stroke_width=0.01)
        planos = VGroup(plano_2,plano_3,plano_4)
        #Ejes
        axes = ThreeDAxes(x_min=-3.5,x_max=3.5,y_min=-3.5,y_max=3.5,z_min=-1,z_max=3.5,num_axis_pieces= 30)
        x_label = TexMobject(r"x").scale(0.75).move_to((3.5,0.3,0))
        y_label = TexMobject(r"y").scale(0.75).move_to((0.3,3.5,0)).rotate_in_place(180*DEGREES)

        #########Animación#########
        self.play(Write(texto_1))
        self.wait()
        self.play(Write(texto_2))
        self.wait(2)
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )   
        self.play(Write(texto_3))
        self.wait()
        self.play(Write(texto_4))
        self.wait(3)
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )
        self.move_camera(phi=80 * DEGREES,theta=60*DEGREES,frame_center=(-1,0,1.5))
        self.play(ShowCreation(axes),ShowCreation(x_label),ShowCreation(y_label))
        self.play(DrawBorderThenFill(figura))
        self.acomodar_textos(texto_4_1)
        self.wait(3)
        self.FadeOutWrite3D(texto_4_1,texto_5)
        self.wait(2)
        self.play(ShowCreation(linea_1))
        self.wait(2)
        self.FadeOutWrite3D(texto_5,texto_6)
        self.wait()
        self.play(Write(lineas_1))
        self.wait(3)
        self.play(ReplacementTransform(texto_6,texto_int_A))
        self.add_fixed_in_frame_mobjects(texto_int_A)
        self.wait()
        self.play(FadeOut(lineas_1))
        self.acomodar_textos(texto_7)
        self.wait(3)
        self.play(Write(lineas_2))
        self.wait(2)
        self.play(ShowCreation(plano_1))
        self.wait()
        self.play(ReplacementTransform(texto_7,texto_int_A2))
        self.add_fixed_in_frame_mobjects(texto_int_A2)
        self.wait()
        self.acomodar_textos(texto_8)
        self.wait(3)
        self.play(ShowCreation(plano_2))
        self.play(ShowCreation(plano_3))
        self.play(ShowCreation(plano_4))
        self.wait(2)
        self.play(ShowCreation(figura_final))
        self.wait()
        self.play(ReplacementTransform(texto_8,texto_int_final))
        self.add_fixed_in_frame_mobjects(texto_int_final)
        self.wait(7)
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )
    
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
        self.wait(8)
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

    def Interludio(self):
        texto_1 = TextMobject('''Lo anterior se puede aplicar igualmente para cuando el dominio \n
                                 de la función es $\\mathcal{R}^3$''').move_to(2*UP)
        texto_2 = TextMobject('''Donde las definiciones de cada integral son equivalentes \n
                                 a las que se dan para una con dominio en $\\mathcal{R}^2$''').next_to(texto_1,DOWN)

        # Animacion
        self.play(Write(texto_1))
        self.wait()
        self.play(Write(texto_2))
        self.wait(3)
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )
    
    def construct(self):
        self.EscenaCero()
        self.Dom2D_PrimeraEscena()
        self.Dom2D_SegundaEscena()

        