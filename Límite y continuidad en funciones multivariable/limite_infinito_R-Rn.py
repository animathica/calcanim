from manimlib.imports import *

#### Limite al infinito positivo
class superficie2(ParametricSurface):
    def __init__(self, **kwargs):
        kwargs = {
            "u_min": 0.1,
            "u_max": 3.2,
            "v_min": 0.1,
            "v_max": 4,
            "checkerboard_colors": [BLUE_C],
        }
        ParametricSurface.__init__(self, self.func, **kwargs)

    def func(self, x, y):
        return np.array([x, (1 / (x * x * x)), (1 / (x * x * x))])


class Limites2(ThreeDScene):
    def construct(self):
        titulo2 = TextMobject(
            """Existencia del Límite en Infinito de \n
                            Funciones de $\\mathbb{R}\\rightarrow\\mathbb{R}^{n}$"""
        )
        texto = TextMobject("""Sea $f:\\mathbb{R}\\rightarrow\\mathbb{R}^{n}$""")
        texto1 = TexMobject(
            r""" \lim_{x \to \infty}f(x)=\vec{L}\leftrightarrow\forall \ \epsilon>0"""
        )
        texto1_1 = TextMobject(
            """$\\exists \\ M\\in\\mathbb{R}$ tal que $x>M \\ \\implies ||f(x)-\\vec{L}||<\\epsilon$"""
        ).move_to(texto1.get_center() + 0.8 * DOWN)
        texto1_2 = TextMobject("""Veamos el siguiente ejemplo""")
        texto1_3 = TextMobject(
            """$f$""",
            """$:\\mathbb{R}^{+}\\rightarrow\\mathbb{R}^{2}$ \n""",
            """$f(x)=(\\frac{1}{x^{3}},\\frac{1}{x^{3}})$""",
        )
        texto1_3[0].set_color(BLUE_C)
        texto1_3[2].set_color(BLUE_C)
        ###Animacion
        self.play(Write(titulo2.scale(1.5)))
        self.wait(6)
        self.play(FadeOut(titulo2))
        self.play(Write(texto))
        self.wait(4.25)
        self.play(texto.shift, 1.2 * UP, runtime=1.5)
        self.play(Write(texto1))
        self.wait(6.125)
        self.play(Write(texto1_1))
        self.wait(8)
        self.play(FadeOut(texto1), FadeOut(texto1_1), FadeOut(texto))
        self.wait()
        self.play(Write(texto1_2))
        self.wait(3.5)
        self.play(FadeOut(texto1_2))
        self.play(Write(texto1_3))
        self.wait(6.125)
        self.play(FadeOut(texto1_3))
        self.wait()
        self.custom_method()

    def custom_method(self):
        axes = ThreeDAxes()
        axes.add(axes.get_x_axis_label("t"))
        surface2 = superficie2()
        texto2 = TextMobject("""Tomemos""", """  $\\epsilon$=0.8""")
        texto2[1].set_color(RED)
        texto2.to_corner(UL)

        texto3 = TextMobject(
            """Los puntos dentro del círculo \n
            en el plano yz están a una \n
            distancia 0.8 del $\\vec{0}$\n del plano yz"""
        )
        texto3.move_to(3.6*LEFT+3*UP)
        text_4_1 = TextMobject("Veamos que hay un punto").move_to(3.6*LEFT+3.5*UP)
        text_4_2 = TextMobject("en x desde el cual ", "$f(x)$").next_to(text_4_1,DOWN)
        text_4_2[1].set_color(BLUE_C)
        text_4_3 = TextMobject("está a una distancia menor").next_to(text_4_2,DOWN)
        text_4_4 = TextMobject("que ", "$\\epsilon$", " del $\\Vec{0}$ del plano yz").next_to(text_4_3,DOWN)
        text_4_4[1].set_color(RED)
        texto4 = VGroup(text_4_1,text_4_2,text_4_3,text_4_4)
        texto4_1 = TextMobject(
            """Es posible hacer lo mismo \n
            con cualquier """,
            """$\\epsilon$""",
            """$>0$""",
        )
        texto4_1[1].set_color(RED)
        texto4_1.to_corner(UL)
        texto5 = TextMobject(
            """Por lo cual notaremos que \n 
            la función tiene límite cuando \n  
            $x\\rightarrow \\infty$ y es (0,0)"""
        )
        texto5.to_corner(UL)
        texto6 = TextMobject(
            """¿Se te ocurre cómo modificar la definición \n
                    anterior cuando el límite es con\n
                     la variable tendiendo a $-\\infty$?"""
        )
        r = 0.8
        r1 = 0.4
        circulo = Circle(radius=r)
        circulo.rotate(PI / 2, axis=UP)
        circulo1 = Circle(radius=r1).move_to(1.8 * RIGHT)
        circulo1.rotate(PI / 2, axis=UP)

        plano = Rectangle(height=2, width=3, fill_color=YELLOW_C, fill_opacity=0.3)
        plano.move_to(0.5 * RIGHT)
        plano.rotate(PI / 2, axis=UP)

        self.set_camera_orientation(0.8 * np.pi / 2, -0.25 * np.pi, distance=10)
        self.play(ShowCreation(axes))
        self.play(ShowCreation(surface2))
        self.wait()
        self.move_camera(phi=80 * DEGREES, theta=0)
        self.begin_ambient_camera_rotation(rate=0.001)
        self.add_fixed_in_frame_mobjects(texto2)
        self.play(Write(texto2))
        self.wait(3.5)
        self.play(ShowCreation(circulo))
        self.play(FadeOut(texto2))
        self.add_fixed_in_frame_mobjects(texto3)
        self.play(Write(texto3))
        self.wait(9.125)
        self.play(FadeOut(texto3))
        self.move_camera(phi=80 * DEGREES, theta=-PI / 8, rate=0.2)
        self.play(circulo.shift, 1.8 * RIGHT, runtime=3)
        self.add_fixed_in_frame_mobjects(texto4)
        self.play(Write(texto4))
        self.wait(9.875)
        self.play(FadeOut(texto4))
        self.add_fixed_in_frame_mobjects(texto4_1)
        self.play(Write(texto4_1))
        self.wait(5.75)
        self.play(ReplacementTransform(circulo, circulo1))
        self.play(circulo1.shift, 2 * RIGHT, runtime=3)
        self.wait()
        self.play(FadeOut(texto4_1))
        self.add_fixed_in_frame_mobjects(texto5)
        self.play(Write(texto5))
        self.wait(8.375)
        self.play(FadeOut(texto5), FadeOut(circulo1), FadeOut(axes), FadeOut(surface2))
        self.add_fixed_in_frame_mobjects(texto6)
        self.play(Write(texto6))
        self.wait(7.625)
        self.play(FadeOut(texto6))