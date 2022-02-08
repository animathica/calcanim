from manimlib.imports import *

################################
###### CURVAS EN EL PLANO ######
################################
#06/07/2021
class Curvas(GraphScene):

	CONFIG = {
		"x_max" : 10,
		"y_max" : 10, 
		"y_axis_height": 1,
		"x_axis_width": 1,
		"graph_origin": 0.1 * DOWN ,
		"axes_color": BLACK,
		"x_axis_label": None,
		"y_axis_label": None,
		"x_tick_frequency": 10,
		"y_tick_frequency": 10,

		}

	#Construccion

	def construct(self):
		self.show_function_graph()

	#Definir función

	def show_function_graph(self):
		self.setup_axes(animate = False)

		Titulo = TextMobject("Curvas")

		#Función

		def func_1(x):
			return  0.2

		#Gráfica
		curva_1 = self.get_graph(func_1,x_min = -25, x_max = 25)
		curva_1.set_color(RED)

		#Función

		def func_2(x):
			return  5 * np.cos(0.1 * x)

		#Gráfica
		curva_2 = self.get_graph(func_2,x_min = -25, x_max = 25)
		curva_2.set_color(RED)

		Nombre_1 = TexMobject("\\mathcal{C}").next_to(curva_2, DOWN)

		#Función 

		def func_3(x):
			return 30

		#Gráfica
		curva_3 = self.get_graph(func_3,x_min = -25, x_max = 25)
		curva_3.set_color(BLUE)

		Nombre_2 = TexMobject("[a,b]").next_to(curva_3, UP)

		Flecha = Arrow(np.array([0, 2.5, 0]), np.array([0, 0.5, 0]))

		Nombre_3 = TexMobject("f").next_to(Flecha, RIGHT)

		Nombre_4 = TexMobject("\\mathcal{C} = Im(f)").next_to(curva_2, DOWN)

		Texto_1 = TextMobject("¿Qué es una curva?").to_corner(UL)

		Texto_2 = TextMobject("Formalmente:").to_corner(UL)

		Pantalla_1 = VGroup(curva_2, curva_3, Nombre_1, Nombre_2, Nombre_3, Nombre_4, Flecha, Texto_2)

		Def_1 = TextMobject("Una", " curva", " es la imagen de una función $f: \\mathbb{R} \\to \\mathbb{R}^n$.").move_to(UP)
		Def_1[1].set_color(RED)

		Req_1 = TextMobject("Dominio", " conexo", " en $\\mathbb{R}$: Un intervalo.").next_to(Def_1, DOWN)
		Req_1[1].set_color(GREEN)

		Req_2 = TextMobject("f", " continua", ".").next_to(Req_1, DOWN)
		Req_2[1].set_color(GREEN)

		Req_3 = TextMobject("En ese caso: $Im(f)$ es una", " curva de Jordan", ".").move_to(Req_2.get_center() + DOWN)
		Req_3[1].set_color(RED)

		Pantalla_2 = VGroup(Def_1, Req_1, Req_2, Req_3)

		curva_4 = ParametricFunction(
                lambda u : np.array([
                math.sin(u),
                math.cos(1.5 * u),
                0
            ]),color=RED,t_min=0,t_max= 4 * PI,
            )

		Texto_3 = TextMobject("Visualmente:").to_corner(UL)

		Función_Final_1 = TexMobject("f: [0, 4 \\pi] \\to \\mathbb{R}^2").to_edge(UP)

		Función_Final_P = TexMobject("t", "\\to (sen(", "t" ,"), cos(1.5", "t", ")").next_to(Función_Final_1, DOWN)

		Nombre_5 = TexMobject("\\mathcal{C} = Im(f)").next_to(curva_4, RIGHT)

		Decimos_1 = TextMobject("Decimos que:")

		Decimos_2 = TextMobject("Im(f) es la", " curva asociada", " a f").next_to(Decimos_1, DOWN)
		Decimos_2[1].set_color(YELLOW_B)

		Decimos_3 = TextMobject("f es una", " parametrización", " de $\\mathcal{C}$").next_to(Decimos_2, DOWN)
		Decimos_3[1].set_color(YELLOW_B)

		Decimos_4 = TextMobject("t es el", " parámetro").next_to(Decimos_3, DOWN)
		Decimos_4[1].set_color(YELLOW_B)

		Parametro = VGroup(Función_Final_P[0], Función_Final_P[2], Función_Final_P[4])

		Decimos = VGroup(Decimos_1, Decimos_2, Decimos_3, Decimos_4).move_to(curva_4.get_center() + 4.25 * LEFT)
		Decimos.scale(0.8)


		def func_4(x):
			return 1

		#Gráfica
		curva_5 = self.get_graph(func_4,x_min = 0, x_max = 4 * PI).move_to(curva_4.get_center() + 2 * DOWN)
		curva_5.set_color(BLUE)
		curva_5.scale(6)

		C5_text_1 = TexMobject("0").next_to(curva_5, LEFT)
		C5_text_2 = TexMobject("4 \\pi").next_to(curva_5, RIGHT)

		Intervalo = VGroup(curva_5, C5_text_1, C5_text_2)

		Punto_1 = Dot(color = BLUE).move_to(curva_5.get_center() + 3.5 * LEFT)
		Im_Punto_1 = Dot(point = np.array([np.sin(0),np.cos(1.5 * 0),0]), color = RED)

		Punto_2 = Dot(color = BLUE).move_to(curva_5.get_center() + 2.625 * LEFT)
		Im_Punto_2 = Dot(point = np.array([np.sin(PI/2),np.cos(1.5 * PI/2),0]), color = RED)

		Punto_3 = Dot(color = BLUE).move_to(curva_5.get_center() + 1.75 * LEFT)
		Im_Punto_3 = Dot(point = np.array([np.sin(PI),np.cos(1.5 * PI),0]), color = RED)

		Punto_4 = Dot(color = BLUE).move_to(curva_5.get_center() + 0.875 * LEFT)
		Im_Punto_4 = Dot(point = np.array([np.sin(1.5 * PI),np.cos(1.5 * 1.5 * PI),0]), color = RED)

		Punto_5 = Dot(color = BLUE).move_to(curva_5.get_center())
		Im_Punto_5 = Dot(point = np.array([np.sin(2 * PI),np.cos(1.5 * 2 * PI),0]), color = RED)

		Punto_6 = Dot(color = BLUE).move_to(curva_5.get_center() + 0.875 * RIGHT)
		Im_Punto_6 = Dot(point = np.array([np.sin(2.5 * PI),np.cos(1.5 * 2.5 * PI),0]), color = RED)

		Punto_7 = Dot(color = BLUE).move_to(curva_5.get_center() + 1.75 * RIGHT)
		Im_Punto_7 = Dot(point = np.array([np.sin(3 * PI),np.cos(1.5 * 3 * PI),0]), color = RED)

		Punto_8 = Dot(color = BLUE).move_to(curva_5.get_center() + 2.625 * RIGHT)
		Im_Punto_8 = Dot(point = np.array([np.sin(3.5 * PI),np.cos(1.5 * 3.5 * PI),0]), color = RED)

		Punto_9 = Dot(color = BLUE).move_to(curva_5.get_center() + 3.5 * RIGHT)
		Im_Punto_9 = Dot(point = np.array([np.sin(4 * PI),np.cos(1.5 * 4 * PI),0]), color = RED)

		Puntos = VGroup(Punto_1, Punto_2, Punto_3, Punto_4, Punto_5, Punto_6, Punto_7, Punto_8, Punto_9)
		Imagenes = VGroup(Im_Punto_1,  Im_Punto_2, Im_Punto_3, Im_Punto_4, Im_Punto_5, Im_Punto_6, Im_Punto_7, Im_Punto_8, Im_Punto_9)

		Pantalla_3 = VGroup(Función_Final_1, Función_Final_P, curva_4, Nombre_5, Intervalo, Puntos, Imagenes)

		Texto_4 = TextMobject("Una curva de Jordan puede no coincidir con nuestra noción geométrica de curva.").move_to(4 * UP)

		Texto_5 = TextMobject("Investiga:", " ¿Qué es una curva de Peano?").next_to(Texto_4, DOWN)

		Texto_6 = TextMobject("¿Una curva puede admitir más de una parametrización?").to_edge(DOWN)

		Textos = VGroup(Texto_4, Texto_5, Texto_6).scale(0.8)

		Cardioide = ParametricFunction(
			lambda u : np.array([
				math.cos(u) * (1 - math.cos(u)),
				math.sin(u) * (1 - math.cos(u)),
				0]),color=LIGHT_PINK,t_min=0,t_max= 6,)
		Cardioide.to_edge(LEFT)

		Curva_Peano = PeanoCurve(order = 3).scale(0.6)

		Astroide = ParametricFunction(
				lambda u : np.array([
				2 * math.cos(u) ** 3,
				2 * math.sin(u) ** 3,
				0]),color=BLUE_B,t_min=0,t_max= 7,)
		Astroide.to_edge(RIGHT)
		Astroide.scale(0.8)

		Pantalla_4 = VGroup(Texto_4, Texto_5, Texto_6, Curva_Peano, Cardioide, Astroide)

		self.play(Write(Titulo, run_time = 2))
		self.wait(2)
		self.play(FadeOut(Titulo, run_time = 2))
		self.wait(2)

		self.play(Write(Texto_1, run_time = 3))
		self.wait()
		self.play(Write(curva_1), run_time = 3)
		self.wait(4)
		self.play(ReplacementTransform(curva_1, curva_2, run_time = 3))
		self.play(Write(Nombre_1, run_time = 2))
		self.play(ReplacementTransform(Texto_1, Texto_2, run_time = 2))
		self.play(Write(curva_3, run_time = 3))
		self.wait(3)
		self.play(Write(Nombre_2, run_time = 2))
		self.wait(2)
		self.play(Write(Flecha, run_time = 3))
		self.wait(2)
		self.play(Write(Nombre_3, run_time = 2))
		self.wait(2)
		self.play(ReplacementTransform(Nombre_1, Nombre_4, run_time = 3))
		self.wait(4)
		self.play(FadeOut(Pantalla_1, run_time = 3))
		self.play(FadeOut(self.axes), run_time = 3)
		self.wait()

		self.play(Write(Def_1, run_time = 4))
		self.wait(4)
		self.play(Write(Req_1, run_time = 2))
		self.wait(4)
		self.play(Write(Req_2, run_time = 2))
		self.wait()
		self.play(Write(Req_3, run_time = 2))
		self.wait(6)
		self.play(FadeOut(Pantalla_2, run_time = 3))
		self.wait(2)

		self.play(Write(Texto_3, run_time = 2))
		self.wait()
		self.play(Write(Función_Final_1, run_time = 3))
		self.wait()
		self.play(Write(Función_Final_P, run_time = 3))
		self.wait()
		self.play(Write(curva_4, run_time = 6))
		self.play(Write(Nombre_5, run_time = 3))
		self.wait(3)
		self.play(Write(Decimos_1, run_time = 2))
		self.wait()
		self.play(Write(Decimos_2, run_time = 3), Indicate(Nombre_5, run_time = 3))
		self.wait()
		self.play(Write(Decimos_3, run_time = 3), Indicate(Función_Final_1, run_time = 3))
		self.wait()
		self.play(Write(Decimos_4, run_time = 3), Indicate(Parametro, run_time = 3))
		self.wait(4)
		self.play(FadeOut(Decimos, run_time = 2))
		self.wait()
		self.play(Write(Intervalo, run_time = 3))
		self.wait()
		self.play(ShowCreation(Puntos, run_time = 2))
		self.wait(2)
		self.play(ReplacementTransform(Punto_1, Im_Punto_1))
		self.play(ReplacementTransform(Punto_2, Im_Punto_2))
		self.play(ReplacementTransform(Punto_3, Im_Punto_3))
		self.play(ReplacementTransform(Punto_4, Im_Punto_4))
		self.play(ReplacementTransform(Punto_5, Im_Punto_5))
		self.play(ReplacementTransform(Punto_6, Im_Punto_6))
		self.play(ReplacementTransform(Punto_7, Im_Punto_7))
		self.play(ReplacementTransform(Punto_8, Im_Punto_8))
		self.play(ReplacementTransform(Punto_9, Im_Punto_9))
		self.wait(2)
		self.play(FadeOut(Pantalla_3, run_time = 3), FadeOut(Texto_3, run_time = 3))
		self.wait(2)

		self.play(Write(Texto_4, run_time = 5), Write(Cardioide, run_time = 5))
		self.wait(2)
		self.play(Write(Texto_5, run_time = 3), Write(Curva_Peano, run_time = 5, rate_func=linear))
		self.wait(2)
		self.play(Write(Texto_6, run_time = 3), Write(Astroide, run_time = 5))
		self.wait(3)
		self.play(FadeOut(Pantalla_4, run_time = 3))
		self.wait(2)