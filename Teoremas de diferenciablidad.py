from manimlib.imports import *

##################################################################
#################### Regla de la cadena ##########################
##################################################################
# 06/04/2021

class Regla_de_la_Cadena_I(ThreeDScene):

	def construct(self):

		axes_config2 = {
        "x_min": -15,
        "x_max": 15,
        "x_axis_width": 15,
        "x_tick_frequency": 1,
        "x_leftmost_tick": 0,
        "x_labeled_nums": None,
        "x_axis_label": None,
        "y_min": -15,
        "y_max": 15,
        "z_min": -15,
        "z_max": 15,
        "z_axis_height": 2,
        "y_axis_height": 2,
        "y_tick_frequency": 1,
        "y_bottom_tick": None, # Change if different from y_min
        "y_labeled_nums": None,
        "y_axis_label": None,
        "axes_color": LIGHT_GREY,
        "graph_origin": 0 * DOWN + 0 * LEFT,
        "exclude_zero_label": True,
        "num_graph_anchor_points": 25,
        "default_graph_colors": GOLD,
        "default_derivative_color": GREEN,
        "default_input_color": YELLOW,
        "default_riemann_start_color": BLUE,
        "default_riemann_end_color": GREEN,
        "function_color": WHITE,
        "area_opacity": 0.8,
        "num_rects": 50,
        "light_source": 15 * DOWN + 7 * LEFT + 3*IN,
        "number_line_config": {
            "include_tip": False,
        },        
                           
        }

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

		Ejemplo1_T3 = TexMobject("D(g \\circ f) =", " [Dg(f)]"," [Df]").move_to(Ejemplo1_T2.get_center() + DOWN)

		Ejemplo1_T4 = TexMobject(r"\begin{bmatrix} e^t + te^t & \quad t^4 e^t \end{bmatrix}").next_to(Ejemplo1_T3, DOWN)
		Ejemplo1_T5 = TexMobject(r"\begin{bmatrix} 2t \\ -t^{-2} \end{bmatrix}").next_to(Ejemplo1_T4, RIGHT)

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

		self.play(Write(Text_R_C_1, run_time = 4))
		self.wait(0.5)
		self.play(Write(Text_R_C_2, run_time = 4))
		self.wait(0.5)
		self.play(Write(Text_R_C_3, run_time = 3))
		self.wait()
		self.play(Write(Text_R_C_4, run_time = 3))
		self.wait(0.5)
		self.play(Write(Text_R_C_5, run_time = 2))
		self.wait()
		self.play(Write(Text_R_C_6, run_time = 3))

		self.wait(2)
		self.play(FadeOut(Regla_de_la_Cadena, run_time = 2))
		self.wait(2)

		self.play(Write(Ejemplo1_T1, run_time = 4))
		self.play(Write(Ejemplo1_T2, run_time = 4))
		self.wait()
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

		Superficie = ParametricSurface(lambda u, v: np.array([ u, v,  u* np.exp(u*v)]),
                                    v_min=-1.5, v_max=1.5, u_min=-1.5, u_max=1.5, checkerboard_colors=[GREEN_C, GREEN_D], resolution=(20,40), stroke_width = 0, fill_opacity = 1)

		Curva = ParametricFunction(
                lambda u : np.array([
                u**2,
                u**(-1),
                0
            ]),color=RED,t_min=-TAU,t_max=TAU,
            )


		self.set_camera_orientation(phi = 45 * DEGREES, theta = 30 * DEGREES) #Cambia la orientación de la cámara
     
		self.play(Write(Superficie, run_time = 4))
		self.wait()
		self.play(Write(Curva, run_time = 4))
		self.wait()
		self.play(FadeOut(Superficie, run_time = 2), FadeOut(Curva, run_time = 2))
		self.wait()
		

class Regla_de_la_Cadena_II(Scene):

	def construct(self):

		Ejemplo2_T1 = TextMobject("Consideremos $g:\\mathbb{R}^2 \\to \\mathbb{R}^2$, dada por $g(\\rho, \\theta) = (\\rho cos(\\theta), \\rho \\sin(\\theta))$ y")
		Ejemplo2_T2 = TextMobject("una función derivable $f: \\mathbb{R}^2 \\to \\mathbb{R}^m$, entonces:").next_to(Ejemplo2_T1, DOWN)

		Enunciado2 = VGroup(Ejemplo2_T1, Ejemplo2_T2)

		Ejemplo2_T3 = TexMobject("D(g \\circ f) =", " [Dg(f)]"," [Df]").move_to(Ejemplo2_T2.get_center() + DOWN)

		Ejemplo2_T4 = TexMobject(r"\begin{bmatrix} \cfrac{\delta f}{\delta x_1} (g) & \quad \cfrac{\delta f}{\delta y_1} (g) \\ \vdots & \vdots \\ \cfrac{\delta f}{\delta x_m} (g) & \cfrac{\delta f}{\delta y_m} (g) \end{bmatrix}").next_to(Ejemplo2_T3, DOWN)
		Ejemplo2_T5 = TexMobject(r"\begin{bmatrix} \cfrac{\delta}{\delta \rho} \rho \cos(\theta) & \cfrac{\delta}{\delta \theta} \rho \cos(\theta) \\ \cfrac{\delta}{\delta \rho} \rho \sin(\theta) & \cfrac{\delta}{\delta \theta} \rho \sin(\theta) \end{bmatrix}").next_to(Ejemplo2_T4, RIGHT)

		Ejemplo2_T6 = TexMobject(r"\begin{bmatrix} \cos(\theta) & \quad -\rho \sin{\theta} \\ \sin{\theta} & \rho \cos{\theta} \end{bmatrix}").next_to(Ejemplo2_T4, RIGHT)

		Matrices2 = VGroup(Ejemplo2_T4, Ejemplo2_T5, Ejemplo2_T6).move_to(Ejemplo2_T3.get_center() + 2.5*DOWN)

		Ejemplo2 = VGroup(Enunciado2, Ejemplo2_T3, Matrices2).scale(0.9)
		Ejemplo2.move_to(0.5*UP)

		self.wait()
		self.play(Write(Ejemplo2_T1, run_time = 4))
		self.play(Write(Ejemplo2_T2, run_time = 4))
		self.wait()
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

###############################################################################################

