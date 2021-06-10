from manimlib.imports import *

###############################################
########## Cambio de variable #################
###############################################
#09/06/2021
class Cambio_de_Variable_1(Scene):

	def construct(self):

		Texto_Intro = TextMobject("Teorema de Cambio de Variable")

		Text_CV_1 = TextMobject("Sean $A \\subset \\mathbb{R}^n$, $f: A \\subset \\mathbb{R}^n \\to \\mathbb{R}$"," continua en $A$,")
		Text_CV_2 = TextMobject("$g: \\Omega \\subset \\mathbb{R}^n \\to \\mathbb{R}^n$"," de clase $C^1$ en $\\Omega$"," y ", "$B \\subset \\Omega$ Jordan-medible").next_to(Text_CV_1, DOWN)
		Text_CV_3 = TextMobject("tal que $\\overline{B} \\subset \\Omega$. Si se cumplen las siguientes condiciones:").next_to(Text_CV_2, DOWN)
		Text_CV_4 = TextMobject("a)", " $g$ es inyectiva en $B \\setminus C$",", con $C \\subset B$").next_to(Text_CV_3, DOWN)
		Text_CV_4_1 = TextMobject("un conjunto de medida de Jordan cero.").next_to(Text_CV_4, DOWN)
		Text_CV_5 = TextMobject("b)", " $\\text{det}(Dg(x)) \\neq 0$ para toda $x \\in B \\setminus D$",", con $D \\subset B$").next_to(Text_CV_4_1, DOWN)
		Text_CV_5_1 = TextMobject("un conjunto de medida de Jordan cero.").next_to(Text_CV_5, DOWN)
		Text_CV_6 = TextMobject("c)", " $g(B) = A$").next_to(Text_CV_5_1, DOWN)
		Text_CV_7 = TextMobject("entonces $A$ es Jordan-medible y además").next_to(Text_CV_6, DOWN)
		Text_CV_8 = TextMobject(" $\\displaystyle \\int_A f = \\int_B (f \\circ g)  \\cdot \\lvert \\text{det}(Dg) \\rvert$").next_to(Text_CV_7, DOWN)
		

		Text_CV_1[1].set_color(BLUE_D)
		Text_CV_2[1].set_color(BLUE_D)
		Text_CV_2[3].set_color(BLUE_D)
		Text_CV_4[1].set_color(BLUE_D)
		Text_CV_5[1].set_color(BLUE_D)
		Text_CV_6[1].set_color(BLUE_D)	
		Text_CV_8.set_color(BLUE_D)	

		Teorema_CV = VGroup(Text_CV_1, Text_CV_2, Text_CV_3, Text_CV_4, Text_CV_4_1, Text_CV_5, Text_CV_5_1, Text_CV_6, Text_CV_7, Text_CV_8).move_to(0.2 * UP)
		Teorema_CV.scale(0.85)

		self.play(Write(Texto_Intro, run_time = 2))
		self.wait(2)
		self.play(FadeOut(Texto_Intro, run_time = 2))

		self.play(Write(Text_CV_1, run_time = 3))
		self.wait()
		self.play(Write(Text_CV_2, run_time = 3))
		self.wait()
		self.play(Write(Text_CV_3, run_time = 3))
		self.wait()
		self.play(Write(Text_CV_4, run_time = 3))
		self.wait()
		self.play(Write(Text_CV_4_1, run_time = 3))
		self.wait()
		self.play(Write(Text_CV_5, run_time = 3))
		self.wait()
		self.play(Write(Text_CV_5_1, run_time = 3))
		self.wait()
		self.play(Write(Text_CV_6, run_time = 3))
		self.wait()
		self.play(Write(Text_CV_7, run_time = 3))
		self.wait()
		self.play(Write(Text_CV_8, run_time = 3))
		self.wait()
		self.play(FadeOut(Teorema_CV, run_time = 5))
		self.wait(2)

class Cambio_de_Variable_2(Scene):

	def construct(self):

		Area_1 = TextMobject("Consideremos:").move_to(3.5 * LEFT + 3.5 * UP)
		
		Rectangulo_1 = Rectangle(color = BLUE_D, height = 1.5, width = 3, fill_opacity = 0.5)
		Rectangulo_1.move_to(Area_1.get_center() + 1.5 * DOWN + RIGHT)

		Area_2 = TextMobject("$R= [a,b] \\times [c,d]$").next_to(Rectangulo_1, DOWN)
		Area_2.scale(0.8)

		Flecha_1 = Arrow(color = TEAL_D)
		Flecha_1.next_to(Rectangulo_1, RIGHT)

		Area_3 = TextMobject("g").next_to(Flecha_1, UP)

		Poli = [(0,0,0), (1,2,0), (5,2,0), (4,0,0)]
		Poligono_1 = Polygon(*Poli)
		Poligono_1.set_opacity(0.5)
		Poligono_1.set_color(PURPLE_C)
		Poligono_1.scale(0.8)
		Poligono_1.next_to(Flecha_1, RIGHT)

		Area_4 = TextMobject("P = g(R)").next_to(Poligono_1, DOWN)
		Area_4.scale(0.8)

		Area_G1 = VGroup(Area_1, Rectangulo_1, Area_2, Flecha_1, Area_3, Poligono_1, Area_4)

		self.play(Write(Area_1, run_time = 2))
		self.wait()
		self.play(Write(Rectangulo_1, run_time = 2))
		self.wait()
		self.play(Write(Area_2, run_time = 2))
		self.wait()
		self.play(Write(Flecha_1, run_time = 2))
		self.wait()
		self.play(Write(Area_3, run_time = 2))
		self.wait()
		self.play(Write(Poligono_1, run_time = 2))
		self.wait()
		self.play(Write(Area_4))
		self.wait()

		Area_5 = TextMobject("$\\text{área}(P) = |x_1 y_2 - x_2y_1| = \\bigg \\lvert \\text{det}$ ")
		Area_6 = TexMobject(r"\begin{bmatrix} x_1 & \quad y_1 \\ x_2 & y_2 \end{bmatrix}").next_to(Area_5, RIGHT)
		Area_7 = TextMobject("$\\bigg \\rvert$").next_to(Area_6, RIGHT)

		Formula_AP = VGroup(Area_5, Area_6, Area_7).move_to(0.5 * DOWN)
		Formula_AP.scale(0.8)

		Area_8 = TexMobject(r"M = \begin{bmatrix} \alpha & \quad \beta \\ \gamma & \delta \end{bmatrix}").scale(0.6)
		Area_8.next_to(Flecha_1, DOWN)

		self.play(Write(Area_5, run_time = 2))
		self.play(Write(Area_6, run_time = 2))
		self.play(Write(Area_7))
		self.wait()
		self.play(Write(Area_8, run_time = 2))
		self.wait()

		Area_9 = TexMobject(r"(x_1, y_1) = \begin{bmatrix} \alpha & \quad \beta \\ \gamma & \delta \end{bmatrix} \begin{pmatrix} b-a \\ 0  \end{pmatrix} = (b-a)(a,c)").next_to(Formula_AP, DOWN)
		Area_9.scale(0.8)
		Area_10 = TexMobject(r"(x_2, y_2) = \begin{bmatrix} \alpha & \quad \beta \\ \gamma & \delta \end{bmatrix} \begin{pmatrix} 0 \\ d-c \end{pmatrix} = (d-c)(b,d)").next_to(Area_9, DOWN)
		Area_10.scale(0.8)

		self.play(Write(Area_9, run_time = 2))
		self.wait()
		self.play(Write(Area_10, run_time = 2))
		self.wait(4)
		self.play(FadeOut(Area_9, run_time = 2), FadeOut(Area_10, run_time = 2), FadeOut(Formula_AP, run_time = 2))

		Area_11 = TextMobject("$m(g(R)) = \\text{área}(P) = |\\alpha \\delta \\cdot (b-a) \\cdot (d-c) - \\beta \\gamma \\cdot (b-a) \\cdot (d-c)|$").move_to(0.5 * DOWN)
		Area_11.scale(0.8)
		Area_12 = TextMobject("$=|\\alpha \\delta-\\beta \\gamma| \\cdot (b-a) \\cdot (c-d) = |\\text{det}(M)| \\cdot \\text{área}(R)$").next_to(Area_11, DOWN)
		Area_12.scale(0.8)
		Area_13 = TextMobject("$= |\\text{det}(M)| \\cdot m(R)$").next_to(Area_12, DOWN)
		Area_13.scale(0.8)

		Area_G2 = VGroup(Area_8, Area_11, Area_12, Area_13)

		self.play(Write(Area_11, run_time = 2))
		self.wait()
		self.play(Write(Area_12, run_time = 2))
		self.wait()
		self.play(Write(Area_13, run_time = 2))
		self.wait()
		self.play(FadeOut(Area_G1, run_time = 3), FadeOut(Area_G2, run_time = 3))

		# Rectángulos de Riemann
		# Gráfica y área bajo la curva.

class Cambio_de_Variable_3(GraphScene):

	CONFIG = {
		"x_max" : 7,
		"y_max" : 8, 
		"y_axis_height": 5,
		"graph_origin": 3 * DOWN + 3 * LEFT,
		"axes_color": BLACK,
		"x_axis_label": None,
		"y_axis_label": None,
		}

	#Construccion

	def construct(self):
		self.show_function_graph()

	#Definir función

	def show_function_graph(self):
		self.setup_axes(animate = True)

		#Función

		def func(x):
			return 0.1 * x * (x-1) * (x - 3) * (x - 6) * (x - 5) + 5


		#Gráfica
		grafica = self.get_graph(func,x_min = 0, x_max = 6)
		grafica.set_color(YELLOW)

		self.play(ShowCreation(grafica), run_time = 3)
		self.play(FadeOut(self.axes))

		#Función para los rectángulos

		def rect(x):
			return x

		rects = self.get_graph(rect, x_min = -1, x_max = 5) #Tamaño del rectángulo

		#Añadir los rectángulos

		kwargs = {
			"x_min" : 0.2, 
			"x_max" : 5.5,
			"fill_opacity" : 0.75,
			"stroke_width" : 0.25, 
		}

		self.grafica = grafica
		iteraciones = 6 

		self.rect_list = self.get_riemann_rectangles_list(
			grafica, iteraciones, start_color = PURPLE, end_color = ORANGE, **kwargs
		)

		flat_rects = self.get_riemann_rectangles(
			self.get_graph(lambda x : 0), dx = 0.5, start_color = invert_color(PURPLE), end_color = invert_color(ORANGE), **kwargs
		)

		rects = self.rect_list[0] #Tamaño del rectángulo
		self.transform_between_riemann_rects(
			flat_rects, rects,
			replace_mobject_with_target_in_scene = True, 
			run_time = 9

		)

		#Loop

		for j in range(1,6): #Ya tenemos el [0], por eso nos lo saltamos.
			self.transform_between_riemann_rects(
				self.rect_list[j-1], self.rect_list[j], dx = 1, 
				replace_mobject_with_target_in_scene = True, 
				run_time = 4
			)

		Grafica_Tex_1 = TextMobject("$m(g(R)) \\approx m([ Dg(\\xi) ](R)) = \\big \\lvert \\text{det}(Dg(\\xi)) \\rvert \\cdot m(R)$").move_to(3 * UP)

		Grafica_Tex_2 = TextMobject("$\\displaystyle \\int_A f \\approx \\sum_{R_i \\subset \\mathcal{P}} f(g(\\eta)) \\cdot m(g(R_i)) \\approx \\sum_{R_i \\subset \\mathcal{P}} f(g(\\eta_i))$",
			"$\\cdot \\lvert \\text{det}(Dg(\\eta_i)) \\rvert \\cdot m(R_i)$").move_to(3 * UP)
		Grafica_Tex_2.scale(0.85)

		Grafica_Tex_3 = TextMobject("$\\displaystyle \\approx \\int_B (f \\circ g) \\cdot \\lvert \\text{det}(Dg) \\rvert$").move_to(2.05 * UP)
		Grafica_Tex_3.scale(0.85)

		Grafica_Tex = VGroup(Grafica_Tex_1, Grafica_Tex_2, Grafica_Tex_3)

		self.play(Write(Grafica_Tex_1, run_time = 4))
		self.wait(3)
		self.play(ReplacementTransform(Grafica_Tex_1, Grafica_Tex_2, run_time = 6))
		self.play(Write(Grafica_Tex_3, run_time = 4))
		self.wait(7)
		self.play(FadeOut(grafica, run_time = 3), *[FadeOut(mob) for mob in self.mobjects], FadeOut(Grafica_Tex_2, run_time = 3), FadeOut(Grafica_Tex_3, run_time = 3))
		self.wait(2)

class Cambio_de_Variable_4(Scene):

	def construct(self):

		Hipo_1_Text = TextMobject("$g: \\Omega \\subset \\mathbb{R}^n \\to \\mathbb{R}^n$ de clase $C^1$ en $\\Omega$").move_to(3 * UP)
		Hipo_1_Exp_1 = TextMobject("$(f \\circ g) \\cdot \\lvert \\text{det}(Dg) \\rvert$ sea integrable")
		Hipo_1_Exp_2 = TextMobject("$m(g(R)) \\approx \\big \\lvert \\text{det}(Dg(\\eta)) \\rvert \\cdot m(R)$ sea una buena aproximación.").next_to(Hipo_1_Exp_1, DOWN)

		Hipo_1_Exp = VGroup(Hipo_1_Exp_1, Hipo_1_Exp_2).scale(0.85)

		Hipo_2_Text = TextMobject("$g$ tiene que ser casi inyectiva en $B$").next_to(Hipo_1_Text, DOWN)
		Hipo_2_Exp_1 = TextMobject("Evitar que haya puntos duplicados en $A$").scale(0.85)

		Hipo_3_Text = TextMobject("$\\text{det}(Dg(\\xi))$ debe ser distinto de cero para casi todo punto $x \\in B$").next_to(Hipo_2_Text, DOWN)
		Hipo_3_Exp_1 = TextMobject("Para que la aplicación sea más sencilla").scale(0.85)

		Hipotesis = VGroup(Hipo_1_Text, Hipo_2_Text, Hipo_3_Text).set_color(BLUE_B)
		Hipotesis.scale(0.85)

		Jaco_Text_1 = TexMobject(" \\text{det}(Dg(\\xi)) = Jg(\\xi)")
		Jaco_Text_2 = TextMobject("Jacobiano ", "de $g$ en $\\xi$").next_to(Jaco_Text_1, DOWN)
		Jaco_Text_2[0].set_color(RED_C)
		Jacobiano = VGroup(Jaco_Text_1, Jaco_Text_2).scale(0.85)


		self.wait(2)
		self.play(Write(Hipo_1_Text, run_time = 2))
		self.wait()
		self.play(Write(Hipo_1_Exp_1, run_time = 2))
		self.wait()
		self.play(Write(Hipo_1_Exp_2, run_time = 2))
		self.wait(4)
		self.play(FadeOut(Hipo_1_Exp, run_time = 2))
		self.wait(2)
		self.play(Write(Hipo_2_Text, run_time = 2))
		self.wait()
		self.play(Write(Hipo_2_Exp_1, run_time = 2))
		self.wait(4)
		self.play(FadeOut(Hipo_2_Exp_1, run_time = 2))
		self.wait(2)
		self.play(Write(Hipo_3_Text, run_time = 2))
		self.wait()
		self.play(Write(Hipo_3_Exp_1, run_time = 2))
		self.wait(4)
		self.play(FadeOut(Hipo_3_Exp_1, run_time = 2))
		self.wait(2)
		self.play(Write(Jaco_Text_1, run_time = 2))
		self.wait()
		self.play(Write(Jaco_Text_2, run_time = 2))
		self.wait(3)
		self.play(FadeOut(Hipotesis, run_time = 3), FadeOut(Jacobiano, run_time = 3))
		self.wait(3)

class Cambio_de_Variable_5(GraphScene):

		CONFIG = {
		"x_max" : 10,
		"y_max" : 10,
		"graph_origin": 3 * DOWN + 2 * LEFT,
		"axes_color": BLACK,
		"x_axis_label": None,
		"y_axis_label": None,

		}


		def construct(self):
			self.show_function_graph()

		#Definir función

		def show_function_graph(self):
			self.setup_axes(animate = True)

			#Funciones

			def hiper1(x):
				return 1 / x


			#Gráfica
			Hiperbola1 = self.get_graph(hiper1,x_min = 0.5, x_max = 2)
			Hiperbola1.set_color(BLUE_C)

			def hiper2(x):
				return 4 / x


			#Gráfica
			Hiperbola2 = self.get_graph(hiper2,x_min = 1, x_max = 4)
			Hiperbola2.set_color(BLUE_C)

			def recta1(x):
				return x / 4


			#Gráfica
			Recta1 = self.get_graph(recta1,x_min = 2, x_max = 4)
			Recta1.set_color(BLUE_C)

			def recta2(x):
				return 4 * x


			#Gráfica
			Recta2 = self.get_graph(recta2,x_min = 0.5, x_max = 1)
			Recta2.set_color(BLUE_C)

			Ejemplo_1_Text_1 = TextMobject("\\textbf{Ejemplo 1}:", " Calcula la integral de la función", " $f(x,y) = xy$", " sobre la región $A$ contenida en el", 
			" primer cuadrante, acotada por las hipérbolas", " $xy=1$,", " $xy = 4$", " y por las rectas", " $4y = x$,", " $y=4x$.").to_edge(UP)
			Ejemplo_1_Text_1.scale(0.75)
			Ejemplo_1_Text_1[0].set_color(RED_C)
			Ejemplo_1_Text_1[2].set_color(TEAL_C)
			Ejemplo_1_Text_1[5].set_color(BLUE_B)
			Ejemplo_1_Text_1[6].set_color(BLUE_B)
			Ejemplo_1_Text_1[8].set_color(BLUE_B)
			Ejemplo_1_Text_1[9].set_color(BLUE_B)

			Ejemplo_1_Text_2 = TextMobject("$h_1(x,y) = xy$", " y ", "$h_2(x,y) = \\cfrac{y}{x}$").next_to(Ejemplo_1_Text_1, DOWN)

			Ejemplo_1_Text_3 = TextMobject("$xy = 1$,", " $xy = 4$,", " $\\cfrac{y}{x} = \\cfrac{1}{4}$,", " $\\cfrac{y}{x} = 4$").next_to(Ejemplo_1_Text_2, DOWN)

			Ejemplo_1_Text_4 = TextMobject("$h=(h_1(x,y), h_2(x,y)) = \\bigg(xy, \\cfrac{y}{x}\\bigg)$")

			Ejemplo_1_Text_5 = TextMobject("$h(A) = R = \\bigg[1 , 4 \\bigg] \\times \\bigg[\\cfrac{1}{4} , 4 \\bigg]$").next_to(Ejemplo_1_Text_4, RIGHT)

			Funcion_Nueva = VGroup(Ejemplo_1_Text_4, Ejemplo_1_Text_5).next_to(Ejemplo_1_Text_1, DOWN)

			Ejemplo_1_Text_6 = TextMobject("$g(u,v) = h^{-1} (x,y) = \\bigg(\\sqrt{\\cfrac{u}{v}}, \\sqrt{uv}\\bigg)$")

			Ejemplo_1_Text_7 = TextMobject("$\\lvert Jg \\rvert = \\bigg \\lvert - \\cfrac{1}{2v} \\bigg \\rvert$").next_to(Ejemplo_1_Text_6, RIGHT)

			Funcion_Inversa = VGroup(Ejemplo_1_Text_6, Ejemplo_1_Text_7).next_to(Ejemplo_1_Text_1, DOWN)

			Rectang = TextMobject("$R = \\bigg[1 , 4 \\bigg] \\times \\bigg[\\cfrac{1}{4} , 4 \\bigg]$")

			Ejemplo_1_Text_6_1 = TextMobject("$g(u,v) = \\bigg(\\sqrt{\\cfrac{u}{v}}, \\sqrt{uv}\\bigg)$").next_to(Rectang, RIGHT)

			Ejemplo_1_Text_7_1 = TextMobject("$\\lvert Jg \\rvert = \\bigg \\lvert - \\cfrac{1}{2v} \\bigg \\rvert$").next_to(Ejemplo_1_Text_6_1, RIGHT)

			Funcion_Inversa_2 = VGroup(Rectang, Ejemplo_1_Text_6_1, Ejemplo_1_Text_7_1).scale(0.85)
			Funcion_Inversa_2.next_to(Ejemplo_1_Text_1, DOWN)

			Ejemplo_1_Text_8 = TextMobject("$\\displaystyle \\int_{A=g(R)} f = \\int_R (f \\circ g) \\cdot \\lvert Jg \\rvert =$").next_to(Ejemplo_1_Text_7, RIGHT)

			Ejemplo_1_Text_9 = TextMobject("$\\displaystyle \\int_{1}^{4} \\int_{\\frac{1}{4}}^{4} f(g(u,v)) \\text{  } \\lvert Jg \\rvert \\text{  }dv \\text{  }du$").next_to(Ejemplo_1_Text_8, RIGHT)

			Primera_Integral = VGroup(Ejemplo_1_Text_8, Ejemplo_1_Text_9).next_to(Funcion_Inversa, DOWN)

			Ejemplo_1_Text_10 = TextMobject("= $\\displaystyle \\int_{1}^{4} \\int_{\\frac{1}{4}}^{4} u \\text{  } \\bigg \\lvert - \\cfrac{1}{2v} \\bigg \\rvert \\text{  }dv \\text{  }du $")

			Ejemplo_1_Text_11 = TextMobject("= $\\displaystyle \\Big(\\int_{1}^{4} u \\text{  } du \\Big) \\Big(\\int_{\\frac{1}{4}}^{4} \\cfrac{1}{2v} \\text{  }dv \\Big)$").next_to(Ejemplo_1_Text_10, RIGHT)

			Segunda_Integral = VGroup(Ejemplo_1_Text_10, Ejemplo_1_Text_11).next_to(Primera_Integral, DOWN)

			Ejemplo_1_Text_12 = TextMobject("= $\\displaystyle = \\bigg(\\cfrac{15}{2} \\bigg)\\bigg(\\ln(4)\\bigg) = 15 \\ln(2)$").next_to(Segunda_Integral, DOWN)

			Pantalla_Final_1 = VGroup(Primera_Integral, Segunda_Integral, Ejemplo_1_Text_12, Ejemplo_1_Text_1, Funcion_Inversa_2)


			Ejemplo_1 = VGroup(Ejemplo_1_Text_2, Ejemplo_1_Text_3, Ejemplo_1_Text_4, Ejemplo_1_Text_5, Ejemplo_1_Text_6, Ejemplo_1_Text_7, Ejemplo_1_Text_8,
				Ejemplo_1_Text_9, Ejemplo_1_Text_10, Ejemplo_1_Text_11, Ejemplo_1_Text_12).scale(0.85)

			self.play(Write(Ejemplo_1_Text_1, run_time = 5))
			self.wait(10)
			self.play(Indicate(Ejemplo_1_Text_1[5], run_time = 2))
			self.play(ShowCreation(Hiperbola1, run_time = 3))
			self.play(FadeOut(self.axes))
			self.play(Indicate(Ejemplo_1_Text_1[6], run_time = 2))
			self.play(ShowCreation(Hiperbola2, run_time = 3))
			self.wait(3)
			self.play(Indicate(Ejemplo_1_Text_1[8], run_time = 2))
			self.play(ShowCreation(Recta1, run_time = 3))
			self.wait()
			self.play(Indicate(Ejemplo_1_Text_1[9], run_time = 2))
			self.play(ShowCreation(Recta2, run_time = 3))
			self.wait(2)
			self.play(Write(Ejemplo_1_Text_2, run_time = 2))
			self.wait()
			self.play(Indicate(Ejemplo_1_Text_1[5], run_time = 2))
			self.wait()
			self.play(Write(Ejemplo_1_Text_3[0], run_time = 2))
			self.wait()
			self.play(Indicate(Ejemplo_1_Text_1[6], run_time = 2))
			self.wait()
			self.play(Write(Ejemplo_1_Text_3[1], run_time = 2))
			self.wait()
			self.play(Indicate(Ejemplo_1_Text_1[8], run_time = 2))
			self.wait()
			self.play(Write(Ejemplo_1_Text_3[2], run_time = 2))
			self.wait()
			self.play(Indicate(Ejemplo_1_Text_1[9], run_time = 2))
			self.wait()
			self.play(Write(Ejemplo_1_Text_3[3], run_time = 2))
			self.play(FadeOut(Ejemplo_1_Text_2, run_time = 2))
			self.play(Write(Ejemplo_1_Text_4, run_time = 2))
			self.wait(2)
			self.play(Write(Ejemplo_1_Text_5, run_time = 2))
			self.wait(2)
			self.play(FadeOut(Ejemplo_1_Text_3, run_time = 3))
			self.play(FadeOut(Hiperbola1, run_time = 3), FadeOut(Hiperbola2, run_time = 3), FadeOut(Recta1, run_time = 3), FadeOut(Recta2, run_time = 3))
			self.wait()
			self.play(ReplacementTransform(Funcion_Nueva, Ejemplo_1_Text_6, run_time = 3))
			self.wait()
			self.play(Write(Ejemplo_1_Text_7, run_time = 3))
			self.wait(2)
			self.play(ReplacementTransform(Funcion_Inversa, Funcion_Inversa_2, run_time = 3))
			self.wait()
			self.play(Write(Ejemplo_1_Text_8, run_time = 3))
			self.wait(2)
			self.play(Write(Ejemplo_1_Text_9, run_time = 3))
			self.wait(2)
			self.play(Write(Ejemplo_1_Text_10, run_time = 3))
			self.wait(2)
			self.play(Write(Ejemplo_1_Text_11, run_time = 3))
			self.wait(2)
			self.play(Write(Ejemplo_1_Text_12, run_time = 3))
			self.wait(5)
			self.play(FadeOut(Pantalla_Final_1))
			self.wait(2)

class Cambio_de_Variable_6(Scene):

	def construct(self):

		Ejemplo_2_Text_1 = TextMobject("\\textbf{Coordenadas Polares:}", " La función $g$ que nos da una relación entre  coordenadas rectangulares y polares es:").to_edge(UP)
		Ejemplo_2_Text_1[0].set_color(RED_C)
		Ejemplo_2_Text_1.scale(0.75)

		Ejemplo_2_Text_2 = TexMobject("g(r, \\theta) = (r \\cos(\\theta), r \\sin(\\theta))").next_to(Ejemplo_2_Text_1, DOWN)
		Ejemplo_2_Text_2.set_color(BLUE_C)

		Ejemplo_2_Text_3 = TextMobject("$R=[0,1] \\times [0, 2\\pi]$")
		Ejemplo_2_Text_3.set_color(TEAL_C)

		Flecha_2 = Arrow(color = TEAL_D)
		Flecha_2.move_to(Ejemplo_2_Text_3.get_center() + 3.2 * RIGHT + 0.25 * DOWN)

		Ejemplo_2_Text_4 = TexMobject("g").move_to(Flecha_2.get_center() + 0.65 * UP + 0.4 * LEFT)

		Ejemplo_2_Text_5 = TexMobject("A=\\{(x,y) \\in \\mathbb{R}^2 \\lvert x^2 + y^2 \\leq 1 \\}").move_to(Ejemplo_2_Text_3.get_center() + 7.3 * RIGHT + 0.05 * DOWN)
		Ejemplo_2_Text_5.set_color(TEAL_C)

		Transforma_R_2 = VGroup(Ejemplo_2_Text_3, Flecha_2, Ejemplo_2_Text_4, Ejemplo_2_Text_5).next_to(Ejemplo_2_Text_2, DOWN)

		Identidad_1 = TextMobject("$r^2 = x^2 + y^2$ ").next_to(Transforma_R_2, DOWN)

		Identidad_2_1 = TextMobject(" $Jg(r , \\theta) = \\text{det}(Dg(r, \\theta))$")
		Identidad_2_2 = TexMobject(r"= \text{det} \begin{pmatrix} \cos(\theta) & \quad -r \sin(\theta) \\ \sin(\theta) & \quad r\cos(\theta) \end{pmatrix}").next_to(Identidad_2_1, RIGHT)
		Identidad_2 = VGroup(Identidad_2_1, Identidad_2_2).next_to(Identidad_1, DOWN)

		Identidad_2_3 = TextMobject("$= r (\\cos^2(\\theta) + \\sin(\\theta) ) = r$").next_to(Identidad_2, DOWN)

		Identidad_Viejo = VGroup(Identidad_1, Identidad_2, Identidad_2_3)

		Identidad_3 = TexMobject("g(r, \\theta) = (r \\cos(\\theta), r \\sin(\\theta)), ")

		Identidad_4 = TextMobject("$r^2 = x^2 + y^2$, ").next_to(Identidad_3, RIGHT)

		Identidad_5 = TextMobject(" $Jg(r , \\theta) = r$").next_to(Identidad_4, RIGHT)

		Identidad_Nuevo = VGroup(Identidad_3, Identidad_4, Identidad_5).next_to(Ejemplo_2_Text_1, DOWN)
		Identidad_Nuevo.set_color(BLUE_C)

		Ejemplo_2_Text_6 = TextMobject("\\textbf{Ejemplo 2:}", " Calcula la integral de la función $f(x,y) = e^{x^2 + y^2}$", 
			" sobre el conjunto $A=\\{(x,y)\\in \\mathbb{R}^2 | x^2 + y^2 \\leq 1 \\}$").to_edge(UP)
		Ejemplo_2_Text_6[0].set_color(RED_C)
		Ejemplo_2_Text_6.scale(0.75)

		Ejemplo_2_Text_7 = TextMobject("$g(r, \\theta) = (r \\cos(\\theta), r \\sin(\\theta))$ es de clase $C^{\\infty}$.")

		Ejemplo_2_Text_8 = TextMobject("$g$ es inyectiva en $R'=(0,1] \\times (0, 2\\pi]$ y $m(R \\setminus R') = 0$.").next_to(Ejemplo_2_Text_7, DOWN)

		Ejemplo_2_Text_9 = TextMobject("$g(R) = A$ y $Jg \\neq 0$.").next_to(Ejemplo_2_Text_8, DOWN)

		Hipotesis_2 = VGroup(Ejemplo_2_Text_7, Ejemplo_2_Text_8, Ejemplo_2_Text_9).next_to(Transforma_R_2, DOWN)

		Primera_Integral_2 = TextMobject("$\\displaystyle \\int_{A=g(R)} f = \\int_R (f \\circ g) \\cdot \\lvert Jg \\rvert =$", 
			" $\\displaystyle \\int_{0}^{2\\pi}\\int_{0}^{1} (f \\circ g) (r, \\theta) \\cdot  \\text{  } \\lvert Jg \\rvert \\text{  }dr \\text{  }d \\theta$").next_to(Transforma_R_2, DOWN)

		Segunda_Integral_2 = TextMobject("$\\displaystyle  \\int_{0}^{2\\pi}\\int_{0}^{1} r \\cdot f(r \\cos(\\theta), r \\sin(\\theta))  \\text{  } dr \\text{  } d\\theta =$", 
			" $\\displaystyle \\int_{0}^{2\\pi}\\int_{0}^{1} r \\cdot e^{r^2} \\text{  } dr \\text{  }d \\theta $").next_to(Primera_Integral_2, DOWN)

		Tercera_Integral_2 = TextMobject("$\\displaystyle  = \\Big(\\int_{0}^{2\\pi} \\text{  } d \\theta \\Big)$", " $ \\Big(\\int_{0}^{1} r \\cdot e^{r^2} \\text{  }dr \\Big) =$", 
			" $\\displaystyle \\pi \\int_{0}^{1} 2r \\cdot e^{r^2} \\text{  }dr$", "$ = \\pi \\cdot (e-1)$").next_to(Segunda_Integral_2, DOWN)

		Integrales_2 = VGroup(Primera_Integral_2, Segunda_Integral_2, Tercera_Integral_2)

		Ejemplo_2 = VGroup(Ejemplo_2_Text_2, Ejemplo_2_Text_3, Ejemplo_2_Text_4, Ejemplo_2_Text_5, Identidad_Viejo, Identidad_Nuevo, Hipotesis_2, Integrales_2).scale(0.85)

		Pantalla_Final_2 = VGroup(Ejemplo_2_Text_6, Identidad_Nuevo, Transforma_R_2, Integrales_2)


		self.wait(2)
		self.play(Write(Ejemplo_2_Text_1, run_time = 3))
		self.wait()
		self.play(Write(Ejemplo_2_Text_2, run_time = 3))
		self.wait()
		self.play(Write(Transforma_R_2, run_time = 3))
		self.wait(3)
		self.play(Write(Identidad_1, run_time = 3))
		self.wait(2)
		self.play(Write(Identidad_2, run_time = 5))
		self.wait()
		self.play(Write(Identidad_2_3, run_time = 3))
		self.wait(2)
		self.play(ReplacementTransform(Identidad_Viejo, Identidad_Nuevo, run_time = 3), FadeOut(Ejemplo_2_Text_2, run_time = 3))
		self.wait(2)
		self.play(ReplacementTransform(Ejemplo_2_Text_1, Ejemplo_2_Text_6, run_time = 3))
		self.wait(2)
		self.play(Write(Ejemplo_2_Text_7, run_time = 3))
		self.wait(2)
		self.play(Write(Ejemplo_2_Text_8, run_time = 3))
		self.wait(2)
		self.play(Write(Ejemplo_2_Text_9, run_time = 3))
		self.wait(5)
		self.play(FadeOut(Hipotesis_2, run_time = 3))
		self.wait()
		self.play(Write(Primera_Integral_2, run_time = 3))
		self.wait(3)
		self.play(Write(Segunda_Integral_2, run_time = 3))
		self.wait(3)
		self.play(Write(Tercera_Integral_2, run_time = 3))
		self.wait(6)
		self.play(Indicate(Tercera_Integral_2[1], run_time = 2))
		self.wait(3)
		self.play(FadeOut(Pantalla_Final_2, run_time = 3))
		self.wait(4)

class Cambio_de_Variable_7(Scene):

	def construct(self):

		Ejemplo_3_Text_1 = TextMobject("\\textbf{Coordenadas Cilíndricas:}", " La función $g$ que nos da una relación entre coordenadas rectangulares y cilíndricas es:").to_edge(UP)
		Ejemplo_3_Text_1[0].set_color(RED_C)
		Ejemplo_3_Text_1.scale(0.75)

		Ejemplo_3_Text_2 = TextMobject("$g(r, \\theta, z) = (r \\cos(\\theta), r\\sin(\\theta), z)$").next_to(Ejemplo_3_Text_1, DOWN)
		Ejemplo_3_Text_2.set_color(BLUE_C)

		Ejemplo_3_Text_3 = TextMobject("$R=[0,1] \\times [0, 2\\pi] \\times [0,1]$")
		Ejemplo_3_Text_3.set_color(TEAL_C)

		Flecha_3 = Arrow(color = TEAL_D)
		Flecha_3.move_to(Ejemplo_3_Text_3.get_center() + 4 * RIGHT + 0.25 * DOWN)

		Ejemplo_3_Text_4 = TexMobject("g").move_to(Flecha_3.get_center() + 0.65 * UP + 0.4 * LEFT)

		Ejemplo_3_Text_5 = TextMobject("$\\{(x,y,z) \\in \\mathbb{R}^2 \\lvert x^2 + y^2 \\leq 1, 0 \\leq z \\leq 1 \\}$").move_to(Ejemplo_3_Text_3.get_center() + 9 * RIGHT + 0.05 * DOWN)
		Ejemplo_3_Text_5.set_color(TEAL_C)

		Transforma_R_3 = VGroup(Ejemplo_3_Text_3, Flecha_3, Ejemplo_3_Text_4, Ejemplo_3_Text_5).next_to(Ejemplo_3_Text_2, DOWN)

		Ej_3_Identidad_1 = TextMobject("$r^2 = x^2 + y^2$ ").next_to(Transforma_R_3, DOWN)

		Ej_3_Identidad_2_1 = TextMobject(" $Jg(r , \\theta, z) = \\text{det}(Dg(r, \\theta, z))$")
		Ej_3_Identidad_2_2 = TexMobject(r"= \text{det} \begin{pmatrix} \cos(\theta) & \quad -r \sin(\theta) & \quad 0 \\ \sin(\theta) & \quad r\cos(\theta) & \quad 0 \\ 0 & \quad 0 & \quad 1 \end{pmatrix}").next_to(Ej_3_Identidad_2_1, RIGHT)
		Ej_3_Identidad_2 = VGroup(Ej_3_Identidad_2_1, Ej_3_Identidad_2_2).next_to(Ej_3_Identidad_1, DOWN)

		Ej_3_Identidad_2_3 = TextMobject("$= r$").next_to(Ej_3_Identidad_2, DOWN)

		Ej_3_Identidad_Viejo = VGroup(Ej_3_Identidad_1, Ej_3_Identidad_2, Ej_3_Identidad_2_3)

		Ej_3_Identidad_3 = TexMobject("g(r, \\theta, z) = (r \\cos(\\theta), r \\sin(\\theta), z), ")

		Ej_3_Identidad_4 = TextMobject("$r^2 = x^2 + y^2$, ").next_to(Ej_3_Identidad_3, RIGHT)

		Ej_3_Identidad_5 = TextMobject(" $Jg(r , \\theta) = r$").next_to(Ej_3_Identidad_4, RIGHT)

		Ej_3_Identidad_Nuevo = VGroup(Ej_3_Identidad_3, Ej_3_Identidad_4, Ej_3_Identidad_5).next_to(Ejemplo_3_Text_1, DOWN)
		Ej_3_Identidad_Nuevo.set_color(BLUE_C)

		Ejemplo_3_Text_6 = TextMobject("\\textbf{Ejemplo 3:}", " Calcula la integral de la función $f(x,y,z) = \\sqrt{x^2 + y^2} \\cdot e^{x\\sqrt{x^2 + y^2}}$", 
			" sobre el conjunto $A= \\big \\{ (x,y,z) \\in \\mathbb{R}^3 \\lvert 0 \\leq x^2 + y^2 \\leq 1$, $0 \\leq z \\leq \\sqrt{x^2 + y^2} \\}$").to_edge(UP)
		Ejemplo_3_Text_6[0].set_color(RED_C)
		Ejemplo_3_Text_6.scale(0.75)

		Conjunto_Trans_1 = TextMobject("$A= \\big \\{ (x,y,z) \\in \\mathbb{R}^3 \\lvert 0 \\leq r \\leq 1$, $0 \\leq z \\leq r \\}$").move_to(Ej_3_Identidad_Nuevo.get_center() + 1.3 *  DOWN)
		Conjunto_Trans_1.set_color(TEAL_C)

		Conjunto_Trans_2 = TextMobject("$B = \\big \\{ (r, \\theta,z) \\in \\mathbb{R}^3 \\lvert 0 \\leq \\theta \\leq 2\\pi$, $ 0 \\leq r \\leq 1$, $0 \\leq z \\leq r \\} $").move_to(Ej_3_Identidad_Nuevo.get_center() + 1.3 *  DOWN)
		Conjunto_Trans_2.set_color(TEAL_C)

		Primera_Integral_3 = TextMobject("$\\displaystyle \\int_{A} f = \\int_R (f \\circ g) \\cdot \\lvert Jg \\rvert =$", 
			" $\\displaystyle \\int_{0}^{2\\pi}\\int_{0}^{1} \\int_{0}^{r}(f \\circ g) (r, \\theta, z) \\cdot  \\text{  } \\lvert Jg \\rvert \\text{   }dz \\text{  }dr \\text{  }d \\theta$").next_to(Transforma_R_3, DOWN)

		Segunda_Integral_3 = TextMobject("$\\displaystyle  \\int_{0}^{2\\pi}\\int_{0}^{1} \\int_{0}^{r} r \\cdot f(r \\cos(\\theta), r \\sin(\\theta), z) \\text{  } dz \\text{  } dr \\text{  } d\\theta =$", 
			" $\\displaystyle \\int_{0}^{2\\pi}\\int_{0}^{1} \\int_{0}^{r} r^2 \\cdot e^{zr} \\text{  } dz \\text{  } dr \\text{  }d \\theta $").next_to(Primera_Integral_3, DOWN)

		Tercera_Integral_3 = TextMobject("$\\displaystyle  = \\Big(\\int_{0}^{2\\pi} \\text{  } d \\theta \\Big) \\Big(\\int_{0}^{1} r \\cdot (e^{r^2} - 1) \\text{  }dr \\Big) =$", 
			" $\\displaystyle \\pi \\int_{0}^{1} 2r \\cdot (e^{r^2} - 1 ) \\text{  }dr = \\pi \\cdot (e-2)$").next_to(Segunda_Integral_3, DOWN)

		Integrales_3 = VGroup(Primera_Integral_3, Segunda_Integral_3, Tercera_Integral_3)

		Ejemplo_3 = VGroup(Ejemplo_3_Text_2, Ejemplo_3_Text_3, Ejemplo_3_Text_4, Ejemplo_3_Text_5, Ej_3_Identidad_Viejo, Ej_3_Identidad_Nuevo, Integrales_3).scale(0.85)

		Pantalla_Final_3 = VGroup(Ejemplo_3_Text_6, Ej_3_Identidad_Nuevo, Conjunto_Trans_2, Integrales_3)

		self.wait(2)
		self.play(Write(Ejemplo_3_Text_1, run_time = 3))
		self.wait()
		self.play(Write(Ejemplo_3_Text_2, run_time = 3))
		self.wait()
		self.play(Write(Transforma_R_3, run_time = 3))
		self.wait(3)
		self.play(Write(Ej_3_Identidad_1, run_time = 3))
		self.wait(2)
		self.play(Write(Ej_3_Identidad_2, run_time = 5))
		self.wait()
		self.play(Write(Ej_3_Identidad_2_3, run_time = 3))
		self.wait(2)
		self.play(ReplacementTransform(Ej_3_Identidad_Viejo, Ej_3_Identidad_Nuevo, run_time = 3), FadeOut(Ejemplo_3_Text_2, run_time = 3), FadeOut(Transforma_R_3, run_time = 3))
		self.wait(2)
		self.play(ReplacementTransform(Ejemplo_3_Text_1, Ejemplo_3_Text_6, run_time = 3))
		self.wait(2)
		self.play(Indicate(Ej_3_Identidad_4, run_time = 2))
		self.wait(2)
		self.play(Write(Conjunto_Trans_1, run_time = 3))
		self.wait(3)
		self.play(ReplacementTransform(Conjunto_Trans_1, Conjunto_Trans_2, run_time = 3))
		self.wait(3)
		self.play(Write(Primera_Integral_3, run_time = 3))
		self.wait(3)
		self.play(Write(Segunda_Integral_3, run_time = 3))
		self.wait(3)
		self.play(Write(Tercera_Integral_3, run_time = 3))
		self.wait(6)
		self.play(FadeOut(Pantalla_Final_3, run_time = 3))
		self.wait(4)


class Cambio_de_Variable_8(Scene):

	def construct(self):

		Ejemplo_4_Text_6 = TextMobject("\\textbf{Ejemplo 4:}", " Calcula el volumen de la región que está dentro de la esfera unitaria con centro en el origen y", 
			" fuera del cono determinado por la ecuación $z^2 = x^2 + y^2$.", " Es decir, el volumen de la región $A= \\{ (x,y,z) \\in  \\mathbb{R}^3 \\lvert x^2 + y^2 + z^2 \\leq 1, z^2 \\leq x^2 + y^2 \\}$").to_edge(UP)
		Ejemplo_4_Text_6[0].set_color(RED_C)
		Ejemplo_4_Text_6.scale(0.8)

		Ejemplo_4_Text_1 = TextMobject("\\textbf{Coordenadas Esféricas:}", " La función $g$ que nos da una relación entre  coordenadas rectangulares y esféricas es:").move_to(Ejemplo_4_Text_6.get_center())
		Ejemplo_4_Text_1[0].set_color(RED_C)
		Ejemplo_4_Text_1.scale(0.75)

		Ejemplo_4_Text_2 = TextMobject("$g(\\rho, \\theta , \\Phi) = (\\rho \\sin(\\phi)\\cos(\\theta), \\rho \\sin(\\phi)\\sin(\\theta), \\rho \\cos(\\theta))$").next_to(Ejemplo_4_Text_6, DOWN)
		Ejemplo_4_Text_2.set_color(BLUE_C)

		Ejemplo_4_Text_3 = TextMobject("$R=[0,1] \\times [0, 2\\pi] \\times [0,1]$")
		Ejemplo_4_Text_3.set_color(TEAL_C)

		Flecha_3 = Arrow(color = TEAL_D)
		Flecha_3.move_to(Ejemplo_4_Text_3.get_center() + 4 * RIGHT + 0.25 * DOWN)

		Ejemplo_4_Text_4 = TexMobject("g").move_to(Flecha_3.get_center() + 0.65 * UP + 0.4 * LEFT)

		Ejemplo_4_Text_5 = TextMobject("$\\{(x,y,z) \\in \\mathbb{R}^2 \\lvert x^2 + y^2 + z^2 \\leq 1 \\}$").move_to(Ejemplo_4_Text_3.get_center() + 8.5 * RIGHT + 0.05 * DOWN)
		Ejemplo_4_Text_5.set_color(TEAL_C)

		Transforma_R_4 = VGroup(Ejemplo_4_Text_3, Flecha_3, Ejemplo_4_Text_4, Ejemplo_4_Text_5).next_to(Ejemplo_4_Text_2, DOWN)

		Ej_4_Identidad_1 = TextMobject("$\\rho^2 = x^2 + y^2 + z^2$ ").next_to(Transforma_R_4, DOWN)

		Ej_4_Identidad_2_1 = TextMobject(" $Jg(r , \\theta, z) = \\text{det}(Dg(r, \\theta, z))$")
		Ej_4_Identidad_2_2 = TexMobject(r"= \text{det} \begin{pmatrix} \sin(\phi)\cos(\theta) & \quad -\rho \sin(\phi)\sin(\theta) & \quad \rho \cos(\phi)\cos(\theta) \\ \sin(\phi)\sin(\theta) & \quad \rho \sin(\phi)\cos(\theta) & \quad \rho \cos(\phi)\sin(\theta) \\ \cos(\phi) & \quad 0 & \quad -\rho \sin(\phi) \end{pmatrix}").next_to(Ej_4_Identidad_2_1, RIGHT)
		Ej_4_Identidad_2 = VGroup(Ej_4_Identidad_2_1, Ej_4_Identidad_2_2).next_to(Ej_4_Identidad_1, DOWN)

		Ej_4_Identidad_2_3 = TextMobject("$= \\cos(\\phi) \\cdot (-\\rho ^2 \\sin(\\phi) \\cos(\\phi)) - \\rho \\sin(\\phi) \\cdot (\\rho \\sin ^2(\\phi)) = - \\rho ^2 \\sin(\\phi)$").next_to(Ej_4_Identidad_2, DOWN)

		Ej_4_Identidad_Viejo = VGroup(Ej_4_Identidad_1, Ej_4_Identidad_2, Ej_4_Identidad_2_3).scale(0.85)

		Ej_4_Identidad_3 = TexMobject("g(r, \\theta, z) = (r \\cos(\\theta), r \\sin(\\theta), z), ")

		Ej_4_Identidad_4 = TextMobject("$r^2 = x^2 + y^2$, ").next_to(Ej_4_Identidad_3, RIGHT)

		Ej_4_Identidad_5 = TextMobject(" $Jg(r , \\theta) = - \\rho ^2 \\sin(\\phi)$").next_to(Ej_4_Identidad_4, RIGHT)

		Ej_4_Identidad_Nuevo = VGroup(Ej_4_Identidad_3, Ej_4_Identidad_4, Ej_4_Identidad_5).next_to(Ejemplo_4_Text_1, DOWN)
		Ej_4_Identidad_Nuevo.set_color(BLUE_C)

		Conjunto_Trans_1 = TextMobject("$A= \\{ (x,y,z) \\in  \\mathbb{R}^3 \\lvert x^2 + y^2 + z^2 \\leq 1, z^2 \\leq x^2 + y^2 \\}$").move_to(Ej_4_Identidad_Nuevo.get_center() + 1.3 *  DOWN)
		Conjunto_Trans_1.set_color(TEAL_C)
		Conjunto_Trans_1.scale(0.8)

		Conjunto_Trans_2 = TextMobject("$B = \\bigg \\{ (\\rho, \\theta, \\phi) \\in \\mathbb{R}^3 \\bigg \\lvert 0 \\leq \\rho \\leq 1, 0 \\leq \\theta \\leq 2 \\pi, \\cfrac{\\pi}{4} \\leq \\phi \\leq \\cfrac{3 \\pi}{4} \\bigg \\} $").move_to(Ej_4_Identidad_Nuevo.get_center() + 1.3 *  DOWN)
		Conjunto_Trans_2.set_color(TEAL_C)
		Conjunto_Trans_2.scale(0.8)

		Primera_Integral_4 = TextMobject("$\\displaystyle \\int_{A} f = \\int_B (f \\circ g) \\cdot \\lvert Jg \\rvert = \\int_B  \\lvert Jg \\rvert $").move_to(Conjunto_Trans_2.get_center() + 0.5 * DOWN)

		Segunda_Integral_4 = TextMobject("$\\displaystyle  \\int_{0}^{1} \\int_{0}^{2\\pi} \\int_{\\frac{\\pi}{4}}^{\\frac{3 \\pi}{4}} \\rho^2 \\cdot \\sin(\\phi) \\text{  } d\\phi \\text{  } d\\theta \\text{  } d\\rho =$", 
			" $\\displaystyle  \\Big(\\int_{0}^{1}  \\rho ^2 \\text{  } d \\rho \\Big) \\Big(\\int_{0}^{2\\pi} d\\theta \\Big) \\Big( \\int_{\\frac{\\pi}{4}}^{\\frac{3 \\pi}{4}} \\sin(\\phi) \\text{   } d\\phi \\Big)$").next_to(Primera_Integral_4, DOWN)

		Tercera_Integral_4 = TextMobject("$\\displaystyle  = \\Big( \\cfrac{\\rho^3}{3} \\Big\\lvert_{0}^{1} \\Big) \\Big( \\theta \\Big\\lvert_{0}^{2\\pi} \\Big) \\Big( -\\cos(\\phi) \\Big\\lvert_{\\frac{\\pi}{4}}^{\\frac{3 \\pi}{4}} \\Big)=$", 
			" $\\displaystyle  \\cfrac{1}{3} \\cdot 2\\pi \\cdot \\bigg( -\\cos\\bigg(\\cfrac{3 \\pi}{4} \\bigg) + \\cos\\bigg(\\cfrac{\\pi}{4} \\bigg) \\bigg) = \\cfrac{4}{3} \\cdot \\cfrac{\\pi}{\\sqrt{2}}$").next_to(Segunda_Integral_4, DOWN)

		Integrales_4 = VGroup(Primera_Integral_4, Segunda_Integral_4, Tercera_Integral_4).scale(0.9)

		Ejemplo_4 = VGroup(Ejemplo_4_Text_2, Ejemplo_4_Text_3, Ejemplo_4_Text_4, Ejemplo_4_Text_5, Ej_4_Identidad_Viejo, Ej_4_Identidad_Nuevo, Integrales_4).scale(0.85)

		Pantalla_Final_3 = VGroup(Ejemplo_4_Text_6, Ej_4_Identidad_Nuevo, Conjunto_Trans_2, Integrales_4)

		self.wait(2)
		self.play(Write(Ejemplo_4_Text_1, run_time = 3))
		self.wait()
		self.play(Write(Ejemplo_4_Text_2, run_time = 3))
		self.wait()
		self.play(Write(Transforma_R_4, run_time = 3))
		self.wait(3)
		self.play(Write(Ej_4_Identidad_1, run_time = 3))
		self.wait(2)
		self.play(Write(Ej_4_Identidad_2, run_time = 5))
		self.wait()
		self.play(Write(Ej_4_Identidad_2_3, run_time = 3))
		self.wait(2)
		self.play(ReplacementTransform(Ej_4_Identidad_Viejo, Ej_4_Identidad_Nuevo, run_time = 3), FadeOut(Ejemplo_4_Text_2, run_time = 3), FadeOut(Transforma_R_4, run_time = 3))
		self.wait(2)
		self.play(ReplacementTransform(Ejemplo_4_Text_1, Ejemplo_4_Text_6, run_time = 3))
		self.wait(2)
		self.play(Indicate(Ej_4_Identidad_4, run_time = 2))
		self.wait(2)
		self.play(Write(Conjunto_Trans_1, run_time = 3))
		self.wait(3)
		self.play(ReplacementTransform(Conjunto_Trans_1, Conjunto_Trans_2, run_time = 3))
		self.wait(3)
		self.play(Write(Primera_Integral_4, run_time = 3))
		self.wait(3)
		self.play(Write(Segunda_Integral_4, run_time = 3))
		self.wait(3)
		self.play(Write(Tercera_Integral_4, run_time = 3))
		self.wait(6)
		self.play(FadeOut(Pantalla_Final_3, run_time = 3))
		self.wait(4)
