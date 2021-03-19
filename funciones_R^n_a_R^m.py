from sys import float_repr_style
from manimlib.imports import *

###PARA ESTA CLASE ES NECESARIO APLICAR LA SOLUCION A LOS VECTORES 3D, TAL COMO EN LA SIGUIENTE LIGA ###
###https://github.com/3b1b/manim/issues/774###
class superficies_parametrizadas (ThreeDScene, Scene):
    def setup(self):
        Scene.setup(self)
        ThreeDScene.setup(self)
    def FadeOutWrite3D(self,objeto1,objeto2):
        self.play(FadeOut(objeto1))
        self.acomodar_textos(objeto2)
    def acomodar_textos(self,objeto):
        self.add_fixed_in_frame_mobjects(objeto)
        self.play(Write(objeto))
    def superficie(self):
        superficie = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                2*math.exp(-1*(u**2+v**2))
            ]),v_min=-3,v_max=3,u_min=-3,u_max=3,fill_color=PURPLE_E,fill_opacity=0.75,
            resolution=(30, 30))
        return superficie
    def punto3D(self):
        bola = ParametricSurface(
            lambda u, v: np.array([
                0.075*np.cos(v) * np.sin(u),
            0.075*np.sin(v) * np.sin(u),
            0.075*np.cos(u)
            ]),v_min=0,v_max=TAU,u_min=0.001,u_max=PI-0.001,
            resolution=(24,24),fill_opacity=1,stroke_color=RED,fill_color=RED)
        return bola
    def PrimeraEscena(self):
        texto_1 = TextMobject('''Sea $\\sigma$ la parametrización de una superficie, \n
                                definida de la siguiente forma''').move_to(1*UP)
        texto_2_1 = TexMobject(r"\sigma=(\sigma_1,\sigma_2,\sigma_3):[-3,3]\times[-3,3]\in\mathbb{R}^2\to\mathbb{R}^3").next_to(texto_1,1*DOWN)
        texto_2_2 = TexMobject(r"\sigma(x,y)=(x,y,2e^{-(x^2+y^2)})").next_to(texto_2_1,DOWN)
        texto_2 = VGroup(texto_2_1,texto_2_2)
        
        #EJES
        axes = ThreeDAxes(x_min=-3.5,x_max=3.5,y_min=-3.5,y_max=3.5,z_min=-1,z_max=3,num_axis_pieces= 30)
        #Superficie
        superficie = self.superficie()

        self.play(Write(texto_1))
        self.wait(5)
        self.play(Write(texto_2))
        self.wait(5)
        self.play(FadeOut(texto_1))
        self.play(
            texto_2.shift,3.5*UP
        )
        self.add_fixed_in_frame_mobjects(texto_2)
        self.wait(0.5)
        self.move_camera(phi=70 * DEGREES,theta=-30*DEGREES,frame_center=(0,0,1))
        self.play(ShowCreation(axes))
        self.play(ShowCreation(superficie))
        self.wait(4)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
        self.move_camera(phi=0,theta=-90*DEGREES,frame_center=(0,0,0))
    def SegundaEscena(self):
        texto_1 = TextMobject('''Consideremos la matriz jacobiana o derivada \n
                                    de $\\sigma$, definida como''').move_to(3*UP)
        texto_2 = TexMobject(r"""D\sigma(\hat{x}_0)=\begin{pmatrix} \dfrac{\partial \sigma_1}{\partial x}(\hat{x}_0) &  \dfrac{\partial \sigma_1}{\partial y}(\hat{x}_0)  \\ \dfrac{\partial \sigma_2}{\partial x}(\hat{x}_0) & \dfrac{\partial \sigma_2}{\partial y}(\hat{x}_0) \\ \dfrac{\partial \sigma_3}{\partial x}(\hat{x}_0) & \dfrac{\partial \sigma_3}{\partial y}(\hat{x}_0)\end{pmatrix}""")
        texto_3 = TextMobject("En el ejemplo, tomemos $\\hat{x}_0=(0.2,0.2)$").move_to(3*UP)
        texto_4 = TexMobject(r"""\text{Entonces, } D\sigma(\hat{x}_0)=\begin{pmatrix} 1 & 0 \\ 0 & 1 \\ -0.74 & -0.74  \end{pmatrix}""").move_to(2.5*UP)
        texto_5 = TextMobject(''' A partir de la matriz $D\\sigma(\\hat{x}_0)$, es posible\n
                                calcular las derivadas parciales de $\\sigma$ en $\\hat{x}_0$ ''').move_to(3*UP)
        texto_6 = TexMobject(r"""\dfrac{\partial \sigma}{\partial x}(\hat{x}_0)=\begin{pmatrix} 1 & 0 \\ 0 & 1 \\ -0.74 & -0.74  \end{pmatrix}\begin{pmatrix} 1 \\ 0 \end{pmatrix}=\begin{pmatrix} 1 \\ 0 \\ -0.74 \end{pmatrix}""").move_to(2.5*UP)
        texto_7 = TexMobject(r"""\dfrac{\partial \sigma}{\partial y}(\hat{x}_0)=\begin{pmatrix} 1 & 0 \\ 0 & 1 \\ -0.74 & -0.74  \end{pmatrix}\begin{pmatrix} 0 \\ 1 \end{pmatrix}=\begin{pmatrix} 0 \\ 1 \\ -0.74 \end{pmatrix} """).move_to(2.5*UP)
        texto_8 = TextMobject(''' Los vectores $\\dfrac{\\partial \\sigma}{\\partial x}(\\hat{x}_0)$ y $\\dfrac{\\partial \\sigma}{\\partial y}(\\hat{x}_0)$ son vectores tangentes\n
                                a la superficie en el punto $\\sigma(\\hat{x}_0)$''').move_to(3*UP)
        texto_9 = TextMobject(''' Definimos $\\dfrac{\\partial \\sigma}{\\partial x}(\\hat{x}_0) \\times \\dfrac{\\partial \\sigma}{\\partial y}(\\hat{x}_0)$ como el vector normal a la\n
                                superficie en $\\sigma(\\hat{x}_0)$, inducida por la parametrización $\\sigma$ ''').move_to(3*UP)
        texto_10 = TextMobject(''' Este vector genera un plano tangente a la superficie en $\\sigma(\\hat{x}_0)$ ''').move_to(3*UP)
        texto_11 = TextMobject(''' Si $\\hat{x}_0$ corresponde a un punto crítico de $\\sigma$, entonces\n
                                $\\dfrac{\\partial \\sigma}{\\partial x}(\\hat{x}_0) =\\vec{0}= \\dfrac{\\partial \\sigma}{\\partial y}(\\hat{x}_0)$ y no hay vector normal a la superficie ''').move_to(3*UP)
        etiqueta_1 = TexMobject(r"""\dfrac{\partial \sigma}{\partial x}(\hat{x}_0)=\begin{pmatrix} 1 \\ 0 \\ -0.74 \end{pmatrix} """).scale(0.75).set_color(PINK).move_to(4*RIGHT)
        etiqueta_2 = TexMobject(r"""\dfrac{\partial \sigma}{\partial y}(\hat{x}_0)=\begin{pmatrix} 0 \\ 1 \\ -0.74 \end{pmatrix} """).scale(0.75).set_color(YELLOW_E).next_to(etiqueta_1,DOWN)
        #EJES
        axes = ThreeDAxes(x_min=-3.5,x_max=3.5,y_min=-3.5,y_max=3.5,z_min=-1,z_max=3,num_axis_pieces= 30)
        #Superficies
        superficie = self.superficie()
        punto = self.punto3D().move_to((0.2,0.2,1.846))
        punto_critico = self.punto3D().move_to((0,0,2))

        dot = Dot().move_to(0.2).move_to(0.2*RIGHT+0.2*UP)
        linea = DashedLine((0.2,0.2,0),(0.2,0.2,1.846))

        plano = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                2.15 - 0.74*(u+v)
            ]),v_min=-0.5,v_max=1,u_min=-0.5,u_max=1,fill_color=GREEN,fill_opacity=1,checkerboard_colors=[GREEN,GREEN],
            resolution=(1, 1))

        #Vectores
        parcial_x = Arrow(start=(0.2,0.2,1.846), end=(1.2,0.2,1.106)).set_color(PINK)
        parcial_y_1 = Arrow(start=(0.2,0.2,1.846), end=(0.2,1.2,1.106)).set_color(YELLOW_E)
        parcial_y_arrow_tip = ArrowTip().set_color(YELLOW_E).scale(0.45).rotate_in_place(155*DEGREES).move_to(2.4*LEFT+0.65*DOWN)
        parcial_y = VGroup(parcial_y_1,parcial_y_arrow_tip)

        vector_normal_1 =Arrow(start=(0.2,0.2,1.846), end=(0.94,0.94,2.846))
        vector_normal_arrow_tip = ArrowTip().set_color(WHITE).scale(0.65).rotate_in_place(-15*DEGREES).move_to(2.27*LEFT+0.23*UP)
        vector_normal = VGroup(vector_normal_1,vector_normal_arrow_tip)
        
        #Animaciones
        self.play(Write(texto_1))
        self.wait(5.7)
        self.play(Write(texto_2))
        self.wait(3)
        self.play(FadeOut(texto_1),FadeOut(texto_2))
        self.acomodar_textos(texto_3)
        self.wait()
        self.move_camera(phi=70 * DEGREES,theta=-30*DEGREES,frame_center=(-3,2,3),distance=1000)
        self.play(ShowCreation(axes))
        self.play(FadeIn(dot))
        self.wait()
        self.play(ShowCreation(linea))
        self.wait(0.4)
        self.play(FadeIn(punto))
        self.play(ShowCreation(superficie))
        self.play(FadeOut(linea),FadeOut(dot))
        self.FadeOutWrite3D(texto_3,texto_4)
        self.wait(3)
        self.FadeOutWrite3D(texto_4,texto_5)
        self.wait(8)
        self.FadeOutWrite3D(texto_5,texto_6)
        self.wait(3)
        self.play(ReplacementTransform(texto_6,etiqueta_1))
        self.add_fixed_in_frame_mobjects(etiqueta_1)
        self.play(FadeIn(parcial_x))
        self.wait()
        self.FadeOutWrite3D(texto_6,texto_7)
        self.wait(3)
        self.play(ReplacementTransform(texto_7,etiqueta_2))
        self.add_fixed_in_frame_mobjects(etiqueta_2)
        self.add_fixed_in_frame_mobjects(parcial_y_arrow_tip)
        self.play(FadeIn(parcial_y_arrow_tip),FadeIn(parcial_y_1))
        self.wait(3)
        self.acomodar_textos(texto_8)
        self.wait(7)
        self.FadeOutWrite3D(texto_8,texto_9)
        self.wait(7)
        self.add_fixed_in_frame_mobjects(vector_normal_arrow_tip)
        self.play(FadeIn(vector_normal_arrow_tip),FadeIn(vector_normal_1))
        self.wait()
        self.FadeOutWrite3D(texto_9,texto_10)
        self.wait(5)
        self.play(ShowCreation(plano))
        self.bring_to_front(plano) #NO PUEDO HACER QUE EL PLANO PASE A "PRIMER PLANO"
        self.wait(3)
        self.play(FadeOut(vector_normal),FadeOut(parcial_y),FadeOut(parcial_x),FadeOut(etiqueta_1),FadeOut(etiqueta_2))
        self.play(FadeOut(plano),FadeOut(punto))
        self.FadeOutWrite3D(texto_10,texto_11)
        self.play(FadeIn(punto_critico))
        self.wait(11)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
        self.move_camera(phi=0,theta=-90*DEGREES,frame_center=(0,0,0))
    def TerceraEscena(self):
        texto_1 = TextMobject(''' Ahora veamos ejemplos de \n
                                    superficies parametrizadas ''')
        texto_2_1 = TextMobject("$\\sigma(x,y)=(\\cos{(x)}\\sin{(y)},\\sin{(x)}\\sin{(y)},\\cos{(y)})$").move_to(3*UP)
        texto_2_2 = TextMobject("con $(x,y)\\in [0,2\\pi]\\times[0,\\pi]$").next_to(texto_2_1,DOWN)
        texto_2_3 = TextMobject("Esfera Unitaria").set_color(PINK).move_to(4*LEFT+0.5*UP)
        texto_2 = VGroup(texto_2_1,texto_2_2)
        texto_3_1 = TextMobject("$\\sigma(x,y)=((R+r\\cos{(y)})\\cos{(x)},(R+r\\cos{(y)})\\sin{(x)},r\\sin{(y)})$").move_to(3*UP)
        texto_3_2 = TextMobject("con $(x,y)\\in [0,2\\pi]\\times[0,2\\pi]$").next_to(texto_3_1,DOWN)
        texto_3_3 = TextMobject("Toro").set_color(PINK).move_to(4*LEFT+0.5*UP)
        texto_3 = VGroup(texto_3_1,texto_3_2)
        texto_4_1 = TextMobject("$\\sigma(x,y)=((2+y\\cos{(x/2)})\\cos{(x)},(2+y\\cos{(x/2)})\\sin{(x)},y\\sin{(x/2)})$").move_to(3*UP).scale(0.9)
        texto_4_2 = TextMobject("con $(x,y)\\in[0,2\\pi]\\times[-1,1]$").next_to(texto_4_1,DOWN)
        texto_4_3 = TextMobject("Banda de Möbius").set_color(PINK).move_to(4*LEFT+0.5*UP)
        texto_4 = VGroup(texto_4_1,texto_4_2)
        #Ejes
        axes = ThreeDAxes(x_min=-3.5,x_max=3.5,y_min=-3.5,y_max=3.5,z_min=-2.5,z_max=3,num_axis_pieces= 30)
        #Otros Objetos
        toro_R = DashedLine((0,0,0),(-1.41,1.41,0))
        etiqueta_R = TextMobject("$R$").move_to(1.1*RIGHT+0.95*DOWN).scale(0.7)
        toro_r = DashedLine((-1.41,1.41,0),(-1.41,1.41,0.5))
        etiqueta_r = TextMobject("$r$").move_to(2*RIGHT+0.9*DOWN).scale(0.7)

        #Superficies
        esfera = ParametricSurface(
            lambda u, v: np.array([
                np.cos(v) * np.sin(u),
                np.sin(v) * np.sin(u),
                np.cos(u)
            ]),v_min=0.0001,v_max=2*PI-0.0001,u_min=0.0001,u_max=PI-0.0001,fill_color=GOLD_E,fill_opacity=1,checkerboard_colors=[PINK,LIGHT_PINK],
            resolution=(20, 30))
        
        toro = ParametricSurface(
            lambda u, v: np.array([
                (2 + 0.5*np.cos(v))*np.cos(u),
                (2 + 0.5*np.cos(v))*np.sin(u),
                0.5*np.sin(v)
            ]),v_min=0.0001,v_max=2*PI-0.0001,u_min=0.0001,u_max=2*PI-0.0001,fill_color=GOLD_E,fill_opacity=1,checkerboard_colors=[PINK,LIGHT_PINK],
            resolution=(20, 30))
        
        parte_toro = ParametricSurface(
            lambda u,v: np.array([
                -1.41-0.5*0.7*np.sin(u),
                1.41+0.5*0.7*np.sin(u),
                0.5*np.cos(u)
            ]),u_min=0.0001,u_max=2*PI-0.0001,fill_color=GOLD_E,fill_opacity=1,checkerboard_colors=[GOLD_E,GOLD_D],
            resolution=(20, 30))

        moebius = ParametricSurface(
            lambda u, v: np.array([
                (2+v*np.cos(u/2))*np.cos(u),
                (2+v*np.cos(u/2))*np.sin(u),
                v*np.sin(u/2)
            ]),u_min=0.0001,u_max=2*PI-0.0001,v_min=-1,v_max=1,fill_color=PINK,fill_opacity=1,checkerboard_colors=[PINK,LIGHT_PINK],
            resolution=(20, 30))

        #Animaciones
        self.play(Write(texto_1))
        self.wait(3)
        self.play(FadeOut(texto_1))
        self.move_camera(phi=70 * DEGREES,theta=-30*DEGREES,frame_center=(0,0,1.5))
        self.play(ShowCreation(axes))
        self.acomodar_textos(texto_2)
        self.acomodar_textos(texto_2_3)
        self.wait()
        self.play(ShowCreation(esfera))
        self.begin_ambient_camera_rotation(rate=0.25)
        self.wait(4)
        self.stop_ambient_camera_rotation()
        self.play(FadeOut(esfera),FadeOut(texto_2_3))
        self.FadeOutWrite3D(texto_2,texto_3)
        self.acomodar_textos(texto_3_3)
        self.wait()
        self.play(ShowCreation(toro_R))
        self.acomodar_textos(etiqueta_R)
        self.wait()
        self.play(ShowCreation(toro_r))
        self.acomodar_textos(etiqueta_r)
        self.wait()
        self.play(ShowCreation(parte_toro))
        self.wait()
        self.play(FadeOut(toro_R),FadeOut(toro_r),FadeOut(etiqueta_R),FadeOut(etiqueta_r))
        self.play(ShowCreation(toro))
        self.play(FadeOut(parte_toro))
        self.begin_ambient_camera_rotation(rate=0.25)
        self.wait(4)
        self.stop_ambient_camera_rotation()
        self.play(FadeOut(toro),FadeOut(texto_3_3))
        self.FadeOutWrite3D(texto_3,texto_4)
        self.acomodar_textos(texto_4_3)
        self.wait()
        self.play(ShowCreation(moebius))
        self.wait()
        self.begin_ambient_camera_rotation(rate=0.25)
        self.wait(10)
        self.stop_ambient_camera_rotation()
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
    def construct(self):
        titulo = TextMobject('''Funciones de $\\mathbb{R}^2$ en $\\mathbb{R}^3$\n
                             Superficies Parametrizadas''').scale(1.5)
        #Animaciones
        self.play(Write(titulo))
        self.wait(2)
        self.play(FadeOut(titulo))
        self.PrimeraEscena()
        self.SegundaEscena()
        self.TerceraEscena()
        
