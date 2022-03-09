from manimlib.imports import *

##################################################################
#################### Regla de la cadena ##########################
##################################################################
# 08/03/2022

class Regla_de_la_Cadena_I(ThreeDScene):
    def construct(self):

        Texto_Intro = TextMobject("Regla de la Cadena")

        Text_R_C_1 = TextMobject("Sean $f: U \\subset \\mathbb{R}^n \\to \\mathbb{R}^m$, $g: V \\subset \\mathbb{R}^m \\to \\mathbb{R}^k$ y $\\hat{x_0} \\in U$ tales que")
        Text_R_C_2 = TextMobject("$f(U) \\subset V$. Si $f$ es diferenciable en $\\hat{x_0}$ y $g$ es diferenciable en $\\hat{y_0} = f(\\hat{x_0})$,").next_to(Text_R_C_1, DOWN)
        Text_R_C_3 = TextMobject("entonces $g \\circ f$ es diferenciable en $\\hat{x_0}$ y además se tiene que:").next_to(Text_R_C_2, DOWN)
        Text_R_C_4 = TextMobject("$D(g \\circ f)(\\hat{x_0}) = Dg(f(\\hat{x_0})) \\circ Df(\\hat{x_0})$").move_to(Text_R_C_3.get_center() + DOWN)
        Text_R_C_5 = TextMobject("O en forma matricial:").move_to(Text_R_C_4.get_center() + DOWN)
        Text_R_C_6 = TextMobject("$D(g \\circ f)(\\hat{x_0}) = [Dg(f(\\hat{x_0}))] [Df(\\hat{x_0})]$").move_to(Text_R_C_5.get_center() + DOWN)
        Regla_de_la_Cadena = VGroup(Text_R_C_1, Text_R_C_2, Text_R_C_3, Text_R_C_4, Text_R_C_5, Text_R_C_6).move_to(0.3*UP)
        Regla_de_la_Cadena.scale(0.85)
        Text_R_C_4.set_color(BLUE_D)
        Text_R_C_6.set_color(BLUE_D)


        Ejemplo1_T1 = TextMobject("Sea $f: \\mathbb{R} \\setminus \\{0\\} \\to \\mathbb{R}^2$ dada por $f(t) = (t^2, t^{-1}) $ y")
        Ejemplo1_T2 = TextMobject("$g: \\mathbb{R}^2 \\to \\mathbb{R}$ dada por $g(x,y) = xe^{xy}$, entonces:").next_to(Ejemplo1_T1, DOWN)

        Ejemplo1_T3 = TexMobject("D(g \\circ f) =", " [Dg(f)]"," [Df]=").move_to(Ejemplo1_T2.get_center() + DOWN)

        Ejemplo1_T4 = TexMobject(r"=\begin{bmatrix} e^t + te^t & \quad t^4 e^t \end{bmatrix}").next_to(Ejemplo1_T3, DOWN)
        Ejemplo1_T5 = TexMobject(r"\begin{bmatrix} 2t \\ -t^{-2} \end{bmatrix}=").next_to(Ejemplo1_T4, RIGHT)

        Matrices = VGroup(Ejemplo1_T4, Ejemplo1_T5).move_to(Ejemplo1_T3.get_center() + 1.3*DOWN)

        Ejemplo1_T6 = TexMobject("= 2te^t + 2t^2 e^t - t^2 e^t").next_to(Matrices, DOWN)
        Ejemplo1_T7 = TexMobject(" = 2te^t + t^2 e^t").next_to(Ejemplo1_T6, RIGHT)

        Resultado = VGroup(Ejemplo1_T6, Ejemplo1_T7).next_to(Matrices, DOWN)

        Ejemplo1 = VGroup(Ejemplo1_T1, Ejemplo1_T2, Ejemplo1_T3, Matrices, Resultado).move_to(UP)
		
        self.wait()
        self.play(Write(Texto_Intro, run_time = 2))
        self.wait()
        self.play(FadeOutAndShift(Texto_Intro, DOWN, run_time = 2))
        self.wait()

        self.play(FadeIn(Text_R_C_1), FadeIn(Text_R_C_2), FadeIn(Text_R_C_3), FadeIn(Text_R_C_4))
        self.wait(44)
        self.play(Write(Text_R_C_5, run_time = 2))
        self.wait(3)
        self.play(Write(Text_R_C_6, run_time = 3))
        self.wait(8)
        self.play(FadeOut(Regla_de_la_Cadena, run_time = 2))
        self.wait(2)

        self.play(FadeIn(Ejemplo1_T1))
        self.play(FadeIn(Ejemplo1_T2))
        self.wait(22)
        self.play(Write(Ejemplo1_T3, run_time = 3))
        self.play(Indicate(Ejemplo1_T3[1], run_time = 2))
        self.play(Write(Ejemplo1_T4, run_time = 2))
        self.play(Indicate(Ejemplo1_T3[2], run_time = 2))
        self.play(Write(Ejemplo1_T5, run_time = 2))
        self.wait()
        self.play(Write(Ejemplo1_T6, run_time = 2))
        self.wait()
        self.play(Write(Ejemplo1_T7, run_time = 2))

        self.play(FadeOut(Ejemplo1, run_time = 2))
        self.wait()

        t_final = TextMobject('''Veamos la imagen de $f$ y las gráficas \n
                                 de $g$ y $g\\circ f$''')
        t_2 = TextMobject('''Imagen de $f$''').to_edge(UP)
        t_2.bg = SurroundingRectangle(t_2, color=WHITE, fill_color=BLACK, fill_opacity=1)
        t_2_gpo = VGroup(t_2.bg,t_2)
        t_3 = TextMobject('''Gráfica de $g$''').to_edge(UP)
        t_3.bg = SurroundingRectangle(t_3, color=WHITE, fill_color=BLACK, fill_opacity=1)
        t_3_gpo = VGroup(t_3.bg,t_3)
        t_4 = TextMobject('''Gráfica de $g\\circ f$''').to_edge(UP)
        t_4.bg = SurroundingRectangle(t_4, color=WHITE, fill_color=BLACK, fill_opacity=1)
        t_4_gpo = VGroup(t_4.bg,t_4)
        t_5 = TextMobject('''Veamos la recta tangente a la curva en \n
                             $t=-2$''').to_edge(UP)
        t_5.bg = SurroundingRectangle(t_5, color=WHITE, fill_color=BLACK, fill_opacity=1)
        t_5_gpo = VGroup(t_5.bg,t_5)
        t_6 = TextMobject('''Notamos que esta tiene pendiente igual a 0.''').to_edge(UP)
        t_6.bg = SurroundingRectangle(t_6, color=WHITE, fill_color=BLACK, fill_opacity=1)
        t_6_gpo = VGroup(t_6.bg,t_6)
        t_7 = TextMobject('''Usando la regla de la cadena, obtenemos que \n
                             la derivada en $t=-2$ es precisamente 0.''').to_edge(UP)
        t_7.bg = SurroundingRectangle(t_7, color=WHITE, fill_color=BLACK, fill_opacity=1)
        t_7_gpo = VGroup(t_7.bg,t_7)
    
        ejes3D = ThreeDAxes(x_min = -5, x_max = 5, y_min = -5, y_max = 5,z_min=-4,z_max=4)
        x_label = TexMobject(r"x").scale(0.75).move_to((5.3,-0.3,0))
        y_label = TexMobject(r"y").scale(0.75).move_to((-0.3,5.3,0))
        y_label_2 = TexMobject(r"y").scale(0.75).move_to((-0.5,4,0))
        axes3D = VGroup(ejes3D,x_label,y_label)
        ejes2D = Axes(x_min = -5, x_max = 5, y_min = -4, y_max = 4)
        axes2D = VGroup(ejes2D,x_label,y_label_2)
        Superficie = ParametricSurface(lambda u, v: np.array([ u, v,  u* np.exp(u*v)]),
                                    v_min=-1.5, v_max=1.5, u_min=-1.5, u_max=1.5, checkerboard_colors=[GREEN_C, GREEN_D], resolution=(20,40), stroke_width = 0, fill_opacity = 0.7)

        Curva1 = ParametricFunction(
                lambda u : np.array([
                u**2,
                u**(-1),
                0
            ]),color=RED,t_min=-(5)**(1/2),t_max=-0.2,
            )
        Curva2 = ParametricFunction(
                lambda u : np.array([
                u**2,
                u**(-1),
                0
            ]),color=RED,t_min=0.2,t_max=(5)**(1/2),
            )
        Curva = VGroup(Curva1,Curva2)
        Composicion = ParametricFunction(lambda x: np.array([x,(x**2)*(np.exp(x)),0]), color=YELLOW,t_min=-5,t_max=1.13)
        tangente = ParametricFunction(lambda x: np.array([x,4*np.exp(-2),0]), color= RED,t_min=-5,t_max=1)

        self.play(Write(t_final))
        self.wait(3.5)
        self.play(FadeOut(t_final))
        self.play(Write(axes2D))
        self.play(Write(t_2_gpo))
        self.play(Write(Curva))
        self.wait(2)
        self.play(*[FadeOut(obj) for obj in self.mobjects])

        self.move_camera(phi=80*DEGREES,theta=30*DEGREES,frame_center=(0,0,2)) #Cambia la orientación de la cámara

        self.play(Write(axes3D),run_time=0.5)
        self.add_fixed_in_frame_mobjects(t_3_gpo)
        self.play(Write(t_3_gpo))
        self.play(Write(Superficie))
        self.wait(2)
        self.play(*[FadeOut(obj) for obj in self.mobjects])

        self.move_camera(phi = 0*DEGREES,theta = -90*DEGREES)
        axes2D.shift(2*DOWN)
        Composicion.shift(2*DOWN)
        self.play(Write(t_4_gpo))
        self.play(Write(axes2D))
        self.add(t_4_gpo)
        self.play(Write(Composicion))
        self.add(t_4_gpo)
        self.wait(2)
        self.play(FadeOut(t_4_gpo))
        self.play(Write(t_5_gpo))
        self.wait()
        tangente.shift(2*DOWN)
        self.play(ShowCreation(tangente))
        self.play(FadeOut(t_5_gpo))
        self.play(Write(t_6_gpo))
        self.wait(2)
        self.play(FadeOut(t_6_gpo))
        self.play(Write(t_7_gpo))
        self.wait(6)
        self.play(*[FadeOut(obj) for obj in self.mobjects])
	
class Regla_de_la_Cadena_II(Scene):

	def construct(self):

		Ejemplo2_T1 = TextMobject("Consideremos $g:\\mathbb{R}^2 \\to \\mathbb{R}^2$, dada por $g(\\rho, \\theta) = (\\rho cos(\\theta), \\rho \\sin(\\theta))$ y")
		Ejemplo2_T2 = TextMobject("una función derivable $f: \\mathbb{R}^2 \\to \\mathbb{R}^m$, entonces:").next_to(Ejemplo2_T1, DOWN)

		Enunciado2 = VGroup(Ejemplo2_T1, Ejemplo2_T2)

		Ejemplo2_T3 = TexMobject("D(f \\circ g) =", " [Df(g)]"," [Dg]").move_to(Ejemplo2_T2.get_center() + DOWN)

		Ejemplo2_T4 = TexMobject(r"\begin{bmatrix} \cfrac{\partial f}{\partial x_1} (g) & \quad \cfrac{\partial f}{\partial y_1} (g) \\ \vdots & \vdots \\ \cfrac{\partial f}{\partial x_m} (g) & \cfrac{\partial f}{\partial y_m} (g) \end{bmatrix}").next_to(Ejemplo2_T3, DOWN)
		Ejemplo2_T5 = TexMobject(r"\begin{bmatrix} \cfrac{\partial}{\partial \rho} \rho \cos(\theta) & \cfrac{\partial}{\partial \theta} \rho \cos(\theta) \\ \cfrac{\partial}{\partial \rho} \rho \sin(\theta) & \cfrac{\partial}{\partial \theta} \rho \sin(\theta) \end{bmatrix}").next_to(Ejemplo2_T4, RIGHT)

		Ejemplo2_T6 = TexMobject(r"\begin{bmatrix} \cos(\theta) & \quad -\rho \sin{\theta} \\ \sin{\theta} & \rho \cos{\theta} \end{bmatrix}").next_to(Ejemplo2_T4, RIGHT)

		Matrices2 = VGroup(Ejemplo2_T4, Ejemplo2_T5, Ejemplo2_T6).move_to(Ejemplo2_T3.get_center() + 2.5*DOWN)

		Ejemplo2 = VGroup(Enunciado2, Ejemplo2_T3, Matrices2).scale(0.9)
		Ejemplo2.move_to(0.5*UP)

		self.wait()
		self.play(FadeIn(Ejemplo2_T1))
		self.play(FadeIn(Ejemplo2_T2))
		self.wait(15.5)
		self.play(Write(Ejemplo2_T3, run_time = 3))
		self.play(Indicate(Ejemplo2_T3[1], run_time = 2))
		self.wait()
		self.play(Write(Ejemplo2_T4, run_time = 3))
		self.wait()
		self.play(Indicate(Ejemplo2_T3[2], run_time = 2))
		self.wait()
		self.play(Write(Ejemplo2_T5, run_time = 3))
		self.wait(2)
		self.play(ReplacementTransform(Ejemplo2_T5, Ejemplo2_T6, run_time = 3))
		self.wait(4)
		self.play(FadeOut(Ejemplo2, run_time = 2))
		self.wait()
