from manimlib.imports import *

class ExtremeValue(GraphScene, Scene):
    def setup(self):
        Scene.setup(self)
        GraphScene.setup(self)

    CONFIG = {
        "x_axis_label": "$x$",
        "y_axis_label": "$y$",
        "y_max": 27,
        "y_min": -27,
        "x_max": 5,
        "x_min": -1,
        "x_labeled_nums": range(-1, 5),
        "y_labeled_nums": range(-27, 28, 9),
        "y_tick_frequency": 3,
        "axes_color": GREEN_C,
        "graph_origin": np.array((-3, 0, 0)),
        "number_scale_val": 0.7,
        "unit_size": 0.5
    }

    # defining text
    def construct(self):
        extreme = TextMobject('Teorema del Valor Extremo')
        # Definición intuitiva
        def_intuitiva = TextMobject("""De manera intuitiva, este teorema nos dice que si \n
        tenemos una función continua en un conjunto compacto, \n
        esta alcanza sus valores extremos en dicho conjunto, \n
        aunque estos no siempre se pueden conocer. """).shift(2 * UP)
        tex0 = TextMobject("Procedamos a enunciar formalmente este teorema.").next_to(def_intuitiva, 2 * DOWN)
        texto = VGroup(def_intuitiva, tex0)
        # Definición formal

        tex1 = TextMobject("Sea", " $f : A \subset \mathbb{R}^{n} \\rightarrow \mathbb{R}$",
                           " continua en $A$ tal que $A$").shift(1.5 * UP)
        tex2 = TextMobject( " cerrado y acotado, entonces $\\exists$",
                           " $ \hat{x_{1}}, \hat{x_{2}} \in A$").next_to(tex1, DOWN)
        tex3 = TextMobject("tales que", " $f(\hat{x_{1}}) \leq f(\hat{x}) \leq f(\hat{x_{2}})$",
                           " $\\forall \hat{x} \in A$.", " Es decir,").next_to(tex2, DOWN)
        tex4 = TextMobject("\\textit{f} alcanza un valor", " máximo", " y un valor", " mínimo",
                           " sobre \\textit{A}.").next_to(tex3, DOWN)
        tex4[1].set_color(GREEN_C)
        tex4[3].set_color(YELLOW_C)
        tex = VGroup(tex1, tex2, tex3, tex4)

        # Ejemplo en R
        ejm1 = TextMobject("""Comencemos por visualizar la definición \n
         anterior en una función $f:\mathbb{R} \\rightarrow \mathbb{R}$.""").to_corner(UL)

        # Secuencia de animación
        self.play(Write(extreme.scale(1.5)))
        self.wait(3.5)
        self.play(FadeOut(extreme))
        self.wait()
        self.play(Write(texto), run_time=7)
        self.wait(15.8)
        self.remove(texto)
        self.wait()
        self.play(Write(tex), run_time=6)
        self.wait(15.8)
        self.play(FadeOut(tex))
        self.play(FadeIn(ejm1))
        self.wait(6.8)
        self.play(ShrinkToCenter(ejm1))

        # Example function
        self.setup_axes()
        graph = self.get_graph(lambda x: 2 * x ** 3 - 9 * x ** 2,
                               color=YELLOW_D,
                               x_min=-1,
                               x_max=5
                               )
        # labeling
        etiqueta = TextMobject("$f(x)= 2x^{3}-9x^{2}$").set_color(YELLOW_D)
        etiqueta.move_to(np.array((0.5, 1, 0)))
        # critic values
        dot_at_start = Dot().move_to(graph.points[0])
        dot_at_start1 = Dot().move_to(self.coords_to_point(-1, 0))
        dot_at_start2 = Dot().move_to(self.coords_to_point(0, -11))
        line_at_start1 = DashedLine(dot_at_start1.get_bottom(), dot_at_start)
        line_at_start2 = DashedLine(dot_at_start2.get_left(), dot_at_start)
        dot_at_start_label = TexMobject((-1, -11)).next_to(dot_at_start, 0.5 * LEFT).scale(0.7)
        dot_start = Group(dot_at_start, dot_at_start_label, dot_at_start1, dot_at_start2,
                          line_at_start1, line_at_start2)
        dot_at_center = Dot().move_to(self.coords_to_point(0, 0))
        dot_at_center_label = TexMobject((0, 0)).next_to(dot_at_center, 0.5 * UP + 0.5 * RIGHT).scale(0.7)
        dot_center = Group(dot_at_center, dot_at_center_label)
        dot_at_min1 = Dot().move_to(self.coords_to_point(3, 0))
        dot_at_min2 = Dot().move_to(self.coords_to_point(0, -27))
        dot_at_min = Dot().move_to(self.coords_to_point(3, -27))
        line_at_min1 = DashedLine(dot_at_min1.get_bottom(), dot_at_min)
        line_at_min2 = DashedLine(dot_at_min2.get_right(), dot_at_min)
        dot_at_min_label = TexMobject((3, -27)).next_to(dot_at_min, 0.5 * DOWN).scale(0.7)
        dot_min = Group(dot_at_min, dot_at_min_label, dot_at_min1, dot_at_min2,
                        line_at_min1, line_at_min2)
        dot_at_end = Dot().move_to(graph.points[-1])
        dot_at_end1 = Dot().move_to(self.coords_to_point(5, 0))
        dot_at_end2 = Dot().move_to(self.coords_to_point(0, 25))
        line_at_end1 = DashedLine(dot_at_end1.get_top(), dot_at_end)
        line_at_end2 = DashedLine(dot_at_end2.get_right(), dot_at_end)
        dot_at_end_label = TexMobject((5, 25)).next_to(dot_at_end, 0.5 * UP).scale(0.7)
        dot_end = Group(dot_at_end, dot_at_end_label, dot_at_end1, dot_at_end2,
                        line_at_end1, line_at_end2)

        grafica = Group(graph, etiqueta)

        self.play(FadeIn(self.axes))
        self.play(ShowCreation(grafica), run_time=2)  #####
        self.wait()
        self.play(ShowCreation(dot_start), ShowCreation(dot_center),
                  ShowCreation(dot_min), ShowCreation(dot_end), run_time=4)
        self.wait(3)
        self.play(FadeOut(self.axes), FadeOut(grafica), FadeOut(dot_end),
                  FadeOut(dot_min), FadeOut(dot_center), FadeOut(dot_start))

        pto0 = TextMobject("Nótese que", " $f(x)= 2x^{3}-9x^{2}$", " es una función continua").to_edge(UP)
        pto0[1].set_color(YELLOW_D)
        pto1 = TextMobject("en el intervalo cerrado $I= [-1,5]$").next_to(pto0, DOWN)
        pto2 = TextMobject("De la gráfica, se observa  ").next_to(pto1, DOWN)
        pto3 = TextMobject("que los valores extremos en $I$").next_to(pto2, DOWN)
        pto4 = TextMobject("se alcanzan cuando:").next_to(pto3, DOWN)
        pto5 = TextMobject("$-27=f(3) \leq f(\hat{x}) \leq f(5)=25$, $ \\forall \hat{x} \in I$").next_to(pto4, DOWN)
        ptos = VGroup(pto0, pto1, pto2, pto3, pto4, pto5)

        self.play(Write(ptos), run_time=6)
        self.wait(12.5)
        self.play(FadeOut(ptos))
        self.wait()

#2
class Superficie(ThreeDScene):
    def setup(self):
        Scene.setup(self)
        ThreeDScene.setup(self)

    def construct(self):
        axis_config = {
            "x_min": -4,
            "x_max": 4,
            "y_min": -4,
            "y_max": 4,
            "z_min": -5,
            "z_max": 6,
            "unit_size": 0.5,
            "graph_origin": np.array([0, 0, -4])
        }

        ejm2 = TextMobject(""" Visualicemos ahora este teorema usando \n
                una función $f:\mathbb{R}^{2} \\rightarrow \mathbb{R}$.""").shift(1.5 * UP)
        nota1 = TextMobject("Sea", " $f(x,y)=x^{2} - y^{2}+5$", " una función continua ").next_to(ejm2, DOWN)
        nota1[1].set_color(BLUE)
        nota2 = TextMobject("en un conjunto cerrado y acotado $T$, ").next_to(nota1, DOWN)
        nota3 = TextMobject("tal que T es ").next_to(nota2, DOWN)
        nota4 = TextMobject("[-3,3]x[-3,3]").next_to(nota3, DOWN)
        notas = VGroup(ejm2, nota1, nota2, nota3, nota4)
        nota5 = TextMobject("""Se puede demostrar que los valores extremos \n
        se alcanzan en la frontera $T$, """).shift(1.5 * UP)
        nota6 = TextMobject("""se podrá hacer con las herramientas del \n
         Cálculo Diferencial para superficies . """).next_to(nota5, DOWN)
        notas_1 = VGroup(nota5, nota6)

        nota7 = TextMobject(""" Se podrá demostrar que el valor máximo es  \n
                 $f(3,0)= 14$, mientras \n
                que el mínimo corresponde a  $f(0,-3)= -4 $""").scale(0.7).to_corner(DL)

        axes = ThreeDAxes(**axis_config)
        #vertices = [(-1, -2, 0), (0, 1, 0), (2, -2, 0)]
        #triangulo = Polygon(*vertices)
        #triangulo.set_color(MAROON_C)
        #triangulo.set_fill(MAROON_C, opacity=0.4)

        # construimos sabanita
        sabanita = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                u ** 2 - v ** 2 + 5
            ]), v_min=-3, v_max=3, u_min=-3, u_max=3, checkerboard_colors=[BLUE_E, BLUE],
            resolution=(15, 32))

        # Si alguien puede hacer que el triángulo pueda pegarse a la sabana, use el triángulo parametrizado akí.
        #        lado1 = ParametricFunction(lambda t: np.array([-1*t,  -3*t+1, 0]),
        #                color = MAROON_C, t_min = 0, t_max = 1)
        #        lado2 = ParametricFunction(lambda t: np.array([2*t,  -3*t+1, 0]),
        #                color = MAROON_C, t_min = 0, t_max = 1)
        #        lado3 = ParametricFunction(lambda t: np.array([-3*t+2, -2, 0]),
        #                color = MAROON_C, t_min = 0, t_max = 1)
        #        triangulo = VGroup(lado1, lado2, lado3)

        # puntitos y líneas punteadas
        ver1 = Dot(np.array([-3, 0, 0]), radius=0.07)
        ver2 = Dot(np.array([3, 0, 0]), radius=0.07)
        ver3 = Dot(np.array([0, -3, 0]), radius=0.07)
        ver4 = Dot(np.array([0, 3, 0]), radius=0.07)
        abs_min = Dot(np.array([0, -3, -4]), radius=0.07)
        abs_min_0 = Dot(np.array([0, 3, -4]), radius=0.07)
        abs_max_0 = Dot(np.array([3,0, 14]), radius=0.07)
        abs_max = Dot(np.array([-3,0,14]), radius=0.07)
        linea = DashedLine(ver1, abs_max, opacity=0.7, stroke_width=5)
        linea2 = DashedLine(ver2, abs_max_0, opacity=0.7, stroke_width=5)
        linea3 = DashedLine(ver3, abs_min, opacity=0.7, stroke_width=5)
        linea4 = DashedLine(ver4, abs_min_0, opacity=0.7, stroke_width=5)

        # etiquetas
        ver1_label = TexMobject((0, -3)).next_to(ver3, 0.5 * LEFT).scale(0.7)
        ver2_label = TexMobject((0, 3)).next_to(ver4, 0.5 * LEFT).scale(0.7)
        ver3_label = TexMobject((3, 0)).next_to(ver2, 0.5 * LEFT).scale(0.7)
        ver4_label = TexMobject((-3, 0)).next_to(ver1, 0.5 * LEFT).scale(0.7)
        #        abs_min_label = TexMobject(r"$(f(0,-2),1)$").next_to(abs_min, 0.5*LEFT).scale(0.7)
        #        abs_max_label = TexMobject(r"$(f(6/5,-4/5),29/5)$").next_to(abs_max, 0.5*LEFT).scale(0.7)
        #        min1_label = TexMobject(r"$(f(-1,-2),2)$").next_to(min1, 0.5*LEFT).scale(0.7)
        #        min2_label = TexMobject(r"$(f(2,-2),5)$").next_to(min2, 0.5*LEFT).scale(0.7)
        #        min3_label = TexMobject(r"$(f(-3/8,-1/8),41/8)$").next_to(min3, 0.5*LEFT).scale(0.7)
        #        min4_label = TexMobject(r"$(f(0,1),4)$").next_to(min4, 0.5*LEFT).scale(0.7)
        # puntitos y etiquetas
        verts = Group(ver1, ver2, ver3,ver4, ver1_label, ver2_label, ver3_label,ver4_label)
        extremos = Group(abs_max, abs_min,abs_max_0, abs_min_0)
        minimos = Group(linea,linea2,linea3,linea4)
        # Animando texto
        self.play(Write(notas), run_time=5)
        self.wait(12.4)
        self.play(ReplacementTransform(notas, notas_1), run_time=3)
        self.wait(7.6)
        self.remove(notas_1)
        self.wait(2)
        self.play(FadeInFromDown(nota7))
        self.wait(10)
        # Animando la gráfica
        self.play(ShowCreation(axes))
        self.play(FadeOut(nota7))
        # self.set_camera_orientation(phi=75 * DEGREES,distance=10, frame_center=(0,0,-3))
        self.move_camera(phi=75 * DEGREES, frame_center=(0, 0, 3))
        self.begin_ambient_camera_rotation(rate=0.2)
        self.play( ShowCreation(verts), ShowCreation(sabanita),
                  ShowCreation(extremos), ShowCreation(minimos), run_time=12)
        self.wait(3)
        self.play(FadeOut(minimos), FadeOut(extremos), FadeOut(sabanita), FadeOut(verts),
                  FadeOut(axes))
        self.wait(2)