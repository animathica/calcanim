from manimlib.imports import *

#######################
### TIPOS DE PUNTOS ###
#######################


class TiposPuntos(Scene):
    def construct(self):
        titulo = TextMobject("Tipos de Puntos")
        titulo.scale(1.5)
        t_1 = TextMobject("Sea A un conjunto cualquiera")
        interior_t = TextMobject("Punto interior de A")
        interior_t.move_to((-3.75, 2.5, 0)).set_color(RED)
        exterior_t = TextMobject("Punto exterior de A")
        exterior_t.move_to((-3.75, 1, 0)).set_color(BLUE)
        frontera_t = TextMobject("Punto frontera de A")
        frontera_t.move_to((-3.75, 0, 0)).set_color(GREEN)
        interior_def = TexMobject(
            "\\exists r>0, \\ tq. \\ \\mathbb{B}_r(x_0)\\subset A"
        )
        interior_def.move_to((3, 2.5, 0)).set_color(WHITE)
        exterior_def = TexMobject(
            "\\exists r>0, \\ tq. \\ \\mathbb{B}_r(x_0)\\subset A^c"
        )
        exterior_def.move_to((3, 1, 0)).set_color(WHITE)
        frontera_def = TexMobject("""\\forall r>0, \\ tq.""")
        frontera_def_1 = TexMobject("""\\mathbb{B}_r(x_0)\\cap A\\neq \\emptyset""")
        frontera_def_2 = TexMobject("""y""")
        frontera_def_3 = TexMobject("""\\mathbb{B}_r(x_0)\\cap A^c\\neq \\emptyset""")
        frontera_def.move_to((3, 0, 0)).set_color(WHITE)
        frontera_def_1.next_to(frontera_def, DOWN, buff=0.1).set_color(WHITE)
        frontera_def_2.next_to(frontera_def_1, DOWN, buff=0.1).set_color(WHITE)
        frontera_def_3.next_to(frontera_def_2, DOWN, buff=0.1).set_color(WHITE)

        texto_1 = TextMobject(
            """Pero \\textquestiondown qu\\'{e} significa geom\\'{e}tricamente?"""
        )


        texto_3 = (
            TextMobject(
                """ \\textexclamdown Por favor regresa el video e intenta \n
                                 asociar las definiciones de cada tipo \n
                                 de punto con el dibujo y visualiza cada \n
                                 definici\\'{o}n en este dibujo!"""
            )
            .scale(0.5)
            .move_to((-4.5, 2.5, 0))
        )
        texto_4 = TextMobject(
            """El conjunto de todos los puntos \n
                                interiores de un conjunto es el""",
            " INTERIOR",
            """ del \n
                                conjunto.""",
        ).move_to((0, 2, 0))
        texto_4[1].set_color(RED)

        texto_5 = TextMobject(
            """El conjunto de todos los puntos \n
                                exteriores de un conjunto es el""",
            """ EXTERIOR""",
            """ del \n
                                conjunto. """,
        ).move_to((0, 0, 0))
        texto_5[1].set_color(BLUE)

        texto_6 = TextMobject(
            """El conjunto de todos los puntos \n
                                frontera de un conjunto es la""",
            " FRONTERA",
            """ del \n
                                conjunto. """,
        ).move_to((0, -2, 0))
        texto_6[1].set_color(GREEN)

        texto_7t = TextMobject(
            """Intenta probar lo siguiente: Si $A$ es un conjunto"""
        )
        texto_71 = TextMobject("""1) \\ $Int(A)\\cap Fr(A) = \\emptyset$""")
        texto_72 = TextMobject("""2) \\ $Int(A)\\cap Ext(A) = \\emptyset$""")
        texto_73 = TextMobject("""3) \\ $Ext(A)\\cap Fr(A) = \\emptyset$""")
        texto_74 = TextMobject("""4) \\ $Int(A^c) = Ext(A)$""")

        texto_7t.shift(3 * UP)
        texto_71.next_to(texto_7t, 2*DOWN)
        texto_72.next_to(texto_71, DOWN)
        texto_73.next_to(texto_72, DOWN)
        texto_74.next_to(texto_73, DOWN)

        texto_7 = VGroup(texto_7t, texto_71, texto_72, texto_73, texto_74)

        # figs:

        conjunto = Circle(
            radius=3, color=YELLOW_B, fill_color=YELLOW_D, fill_opacity=0.7
        )
        punto_int = Dot(point=(1, 1, 0)).set_color(RED)
        punto_ext = Dot(point=(3, 3, 0)).set_color(BLUE)
        punto_fr = Dot(point=(1.5, np.sqrt(9 - 1.5 ** 2), 0)).set_color(GREEN)

        flecha_int = Arrow((-1.5, 2.5, 0), (0.3, 2.5, 0)).set_color(RED)
        flecha_ext = Arrow((-1.5, 1, 0), (0.3, 1, 0)).set_color(BLUE)
        flecha_fr = Arrow((-1.5, 0, 0), (0.3, 0, 0)).set_color(GREEN)

        cjto_int = Circle(
            radius=1, color=RED, fill_color=RED, fill_opacity=0.7
        ).move_to((1, 1, 0))
        cjto_ext = Circle(
            radius=0.5, color=BLUE, fill_color=BLUE, fill_opacity=0.7
        ).move_to((3, 3, 0))
        cjto_fr = Circle(
            radius=0.5, color=GREEN, fill_color=GREEN, fill_opacity=0.7
        ).move_to(punto_fr.get_center())

        # GPOS

        gpo_1 = VGroup(
            interior_t,
            exterior_t,
            frontera_t,
            interior_def,
            exterior_def,
            frontera_def,
            flecha_int,
            flecha_ext,
            flecha_fr,
            frontera_def_1,
            frontera_def_2,
            frontera_def_3,
        )

        gpo_11 = VGroup(interior_t, interior_def, flecha_int)
        gpo_12 = VGroup(exterior_t, exterior_def, flecha_ext)
        gpo_13 = VGroup(
            frontera_t,
            frontera_def,
            flecha_fr,
            frontera_def_1,
            frontera_def_2,
            frontera_def_3,
        )

        # animación
        self.play(Write(titulo))
        self.wait(2)
        self.play(FadeOut(titulo))
        self.play(Write(t_1))
        self.wait(2)
        self.play(FadeOut(t_1))
        self.play(Write(gpo_11))
        self.wait(1.4)
        self.play(Write(gpo_12))
        self.wait(1.4)
        self.play(Write(gpo_13))
        self.wait(3)
        self.play(ReplacementTransform(gpo_1, texto_1))
        self.wait(2.6)
        self.play(ReplacementTransform(texto_1, conjunto))
        self.wait(2.7)
        self.play(Write(punto_int), Write(punto_ext), Write(punto_fr))
        self.wait(1.2)
        self.play(DrawBorderThenFill(cjto_int), runtime=0.2)
        self.play(DrawBorderThenFill(cjto_ext), runtime=0.2)
        self.play(DrawBorderThenFill(cjto_fr), runtime=0.2)
        self.play(Write(texto_3))
        self.wait(4)
        self.play(
            FadeOut(texto_3),
            FadeOut(cjto_int),
            FadeOut(cjto_ext),
            FadeOut(cjto_fr),
            FadeOut(conjunto),
            FadeOut(punto_int),
            FadeOut(punto_ext),
            FadeOut(punto_fr),
        )
        self.play(Write(texto_4))
        self.wait(2)
        self.play(Write(texto_5))
        self.wait(2)
        self.play(Write(texto_6))
        self.wait(2)
        self.play(FadeOut(texto_4), FadeOut(texto_5), FadeOut(texto_6))
        self.play(Write(texto_7t))
        self.wait(2)
        self.play(Write(texto_71))
        self.wait(2)
        self.play(Write(texto_72))
        self.wait(2)
        self.play(Write(texto_73))
        self.wait(2)
        self.play(Write(texto_74))
        self.wait(2)
        self.play(FadeOut(texto_7))