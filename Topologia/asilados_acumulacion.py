from manimlib.imports import *

#############################################################
#### PUNTOS AISLADOS, DE ACUMULACION Y CONJUNTO DERIVADO ####
#############################################################


class Puntos_Aislado_y_Acumulacion(Scene):
    def construct(self):
        title = TextMobject(
            """Puntos Aislados y \n
                            Puntos de Acumulación"""
        ).scale(1.5)
        text1 = TextMobject("""Considera el siguiente conjunto """, """$A$""")
        text1.set_color_by_tex_to_color_map({"A": YELLOW})
        text2 = TextMobject(
            """Fíjate en los puntos """, """$x$""", """ e """, """$y$"""
        ).to_edge(UP)
        text2.set_color_by_tex_to_color_map({"x": RED, "y": BLUE})
        B = (
            SVGMobject("Topologia_SVGs/cjtoA.svg", color=YELLOW, fill_color=YELLOW)
            .shift(1.5 * LEFT)
            .scale(2)
        )
        x = Dot(point=((1, 0, 0)), color=YELLOW, radius=0.1)
        x_label = TexMobject("x", color=RED).next_to(x, DOWN)
        cjto = VGroup(B, x)
        y = Dot(point=((-1.8, 0.5, 0)), color=BLUE, radius=0.1)
        y_label = TexMobject("y", color=BLUE).next_to(y, DOWN)
        grupo = VGroup(y, x_label, y_label)
        bola = Circle(radius=1, color=PURPLE_B).move_to((1, 0, 0))
        radio = Line(((1, 0, 0)), ((2, 0, 0)), color=PURPLE_B)
        eps = TexMobject(r"\varepsilon").next_to(radio, UP)
        aislado = VGroup(bola, radio, eps)

        text3 = TextMobject(
            """¿Cuál crees que sea un""", """ punto aislado""", """?"""
        ).to_edge(UP)
        text3.set_color_by_tex_to_color_map(
            {
                """punto aislado""": PURPLE_B,
            }
        )

        text4 = TextMobject(
            """¿Cuál crees que sea un""", """ punto de acumulación""", """?"""
        ).to_edge(UP)
        text4.set_color_by_tex_to_color_map(
            {
                """punto de acumulación""": GREEN_D,
            }
        )

        text5 = TextMobject(
            """$x$""",
            """ es un""",
            """ punto aislado""",
            """, al tomar alguna $\\varepsilon >0$ \n
                             vemos que $B_{\\varepsilon}($""",
            """$x$""",
            """)$\\cap$ """,
            """$A$""",
            """$=$""",
            """$\\{x\\}$""",
        ).to_edge(UP)
        # ,'''${x}$''','''\\'''
        text5.set_color_by_tex_to_color_map(
            {
                """punto aislado""": PURPLE_B,
                """$A$""": YELLOW,
                """$x$""": RED
                #'''$\\{x\\}$''': RED,
            }
        )
        text5[8][1].set_color(RED)

        text6 = TextMobject(
            """Mientras que """,
            """$y$""",
            """ es un""",
            """ punto de acumulación""",
            """ pues $\\forall\\varepsilon >0$ \n
                            se cumple que $(B_{\\varepsilon}($""",
            """$y$""",
            """)$\\backslash$""",
            """$\\{y\\}$""",
            """$)\\cap $""",
            """$A$""",
            """$\\neq \\emptyset$""",
        ).to_edge(UP)
        text6.set_color_by_tex_to_color_map(
            {
                """punto de acumulación""": GREEN_D,
                """$A$""": YELLOW,
                """$y$""": BLUE
                #'''$\\{y\\}$''': BLUE
            }
        )
        text6[7][1].set_color(BLUE)

        text7 = TextMobject(
            """El conjunto de todos los""",
            """ puntos de acumulación""",
            """ de """,
            """$A$""",
            """ \\\\ se llama""",
            """ conjunto derivado""",
            """, y se denota por """,
            """$der(A)$""",
        ).scale(0.9)
        text7.set_color_by_tex_to_color_map(
            {
                """puntos de acumulación""": GREEN_D,
                """conjunto derivado""": RED,
                """$der(A)$""": RED,
                """$A$""": YELLOW,
            }
        )

        text8 = TextMobject(
            """Intenta demostrar las siguientes propiedades \\\\ de dicho conjunto:"""
        ).move_to((0, 2.5, 0))
        prop1 = TextMobject(
            """$der(A)$""",
            """ es la unión de $int(A)$ y los puntos frontera no aislados""",
        ).move_to((0, 1, 0))
        prop2 = TextMobject(
            """$cl(A)=$""", """$A$""", """$\cup$""", """$der(A)$"""
        ).next_to(prop1, DOWN)
        prop3 = TextMobject(
            """Todos los""",
            """ puntos""",
            """ de $int(A)$ son""",
            """ de acumulación""",
        ).next_to(prop2, DOWN)
        prop1.set_color_by_tex_to_color_map(
            {
                """$der(A)$""": RED,
            }
        )
        prop2.set_color_by_tex_to_color_map({"""$der(A)$""": RED, """$A$""": YELLOW})
        prop3.set_color_by_tex_to_color_map(
            {"""puntos""": GREEN_D, """de acumulación""": GREEN_D}
        )
        prop4 = TextMobject(
            """Todos los """,
            """puntos aislados""",
            """ de """,
            """$A$""",
            """ son puntos frontera de """,
            """$A$""",
        ).next_to(prop3, DOWN)
        prop4.set_color_by_tex_to_color_map(
            {"""puntos aislados""": PURPLE_B, """$A$""": YELLOW}
        )
        propiedades = VGroup(text8, prop1, prop2, prop3, prop4)

        # Secuencia de la animación
        self.play(Write(title))
        self.wait()
        self.play(ReplacementTransform(title, text1))
        self.play(ApplyMethod(text1.to_edge, UP))
        self.play(DrawBorderThenFill(cjto))
        self.wait()
        self.play(
            ReplacementTransform(text1, text2),
            ApplyMethod(x.set_color, RED),
            Write(grupo),
        )
        self.wait(2)
        #
        self.play(ReplacementTransform(text2, text3))
        self.wait(2)
        self.play(ReplacementTransform(text3, text4))
        self.wait(2)
        self.play(ReplacementTransform(text4, text5), ShowCreation(aislado))
        self.wait(13)
        self.play(ReplacementTransform(text5, text6), FadeOut(aislado))
        ##
        i = 4
        bola_ant = Circle(radius=i, color=GREEN_D).move_to((-1.8, 0.5, 0))
        while i > 0.2:
            bola_sig = Circle(radius=i, color=GREEN_D).move_to((-1.8, 0.5, 0))

            self.play(ReplacementTransform(bola_ant, bola_sig))
            self.wait()

            bola_ant = bola_sig
            i = 0.5 * i
        self.wait(5)
        self.play(FadeOut(text6), FadeOut(bola_ant), FadeOut(cjto), FadeOut(grupo))
        self.wait(2)
        self.play(Write(text7))
        self.wait(10)
        self.play(ReplacementTransform(text7, text8))
        self.wait(5)
        self.play(Write(prop1))
        self.wait(8)
        self.play(Write(prop2))
        self.wait(7)
        self.play(Write(prop3))
        self.wait(6)
        self.play(Write(prop4))
        self.wait(6)
        self.play(FadeOut(propiedades))