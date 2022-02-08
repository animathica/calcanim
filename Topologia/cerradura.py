from manimlib.imports import *

##################################
#### CERRADURA DE UN CONJUNTO ####
##################################


class Cerradura(Scene):
    def construct(self):
        title = TextMobject("""Cerradura""")
        defi = TextMobject(
            """Definimos la""",
            """ cerradura""",
            """ de un conjunto""",
            """ $A$""",
            """ como """,
        )
        defi.set_color_by_tex_to_color_map({"""cerradura""": PURPLE, """$A$""": YELLOW})
        defi2 = TextMobject(
            """ $\\bar{A}$""",
            """=""",
            """$cl(A)$""",
            """:=""",
            """$A$""",
            """$\\cup$""",
            """$Fr(A)$""",
        ).next_to(defi, DOWN)
        defi2.set_color_by_tex_to_color_map(
            {
                """$\\bar{A}$""": PURPLE,
                """$cl(A)$""": PURPLE,
                """$A$""": YELLOW,
                """Fr(A)""": RED,
            }
        )

        conjuntoA = SVGMobject(
            "Topologia_SVGs/cjtoA.svg",
            color=RED,
            fill_color=YELLOW,
            fill_opacity=1.2,
        ).scale(2)
        nameA = TexMobject("A").next_to(conjuntoA, DOWN)
        note = (
            TextMobject(
                """*Recuerda que el conjunto puede contener elementos de su frontera, es decir, \n
                            el conjunto no es necesariamente igual a su interior."""
            )
            .scale(0.55)
            .to_edge(DOWN)
        )
        group = VGroup(conjuntoA, defi, defi2, nameA, note)
        group2 = VGroup(defi, defi2)

        text1 = TextMobject("""Veamos algunas propiedades sobre la""", """ cerradura""")
        text1.set_color_by_tex_to_color_map({"""cerradura""": PURPLE})
        text2 = TexMobject(r"cl(A\cup B)", r"=", r"cl(A)", r"\cup", r"cl(B)")
        text2.set_color_by_tex_to_color_map({"cl(A)": YELLOW, "cl(B)": BLUE})

        conjuntoB = (
            SVGMobject("Topologia_SVGs/cjtoB.svg", color=BLUE, fill_color=BLUE)
            .shift(1.5 * RIGHT)
            .scale(2)
        )
        conjuntoA1 = conjuntoA.copy()
        conjuntoA1.set_color(YELLOW).shift(1.5 * LEFT)
        A = TexMobject("A").next_to(conjuntoA1, DOWN)
        B = TexMobject("B").next_to(conjuntoB, DOWN)
        names = VGroup(A, B)
        conjuntos = VGroup(conjuntoA1, conjuntoB)
        conjuntoA2 = (
            SVGMobject("Topologia_SVGs/cjtoA.svg", color=WHITE, fill_color=WHITE)
            .shift(2.5 * LEFT)
            .scale(2)
        )
        conjuntoB2 = (
            SVGMobject("Topologia_SVGs/cjtoB.svg", color=WHITE, fill_color=WHITE)
            .shift(2.5 * RIGHT)
            .scale(2)
        )
        conjuntos2 = VGroup(conjuntoA2, conjuntoB2)

        text3 = TextMobject("""Intenta demostrar que:""")
        prop1 = TexMobject(
            r"x\in cl(A) \Leftrightarrow \forall \varepsilon>0,\ B_{\varepsilon}\cap A\neq\emptyset"
        ).next_to(text3, DOWN)

        # Secuencia de la animación
        self.play(Write(title.scale(1.5)))
        self.wait()
        self.play(FadeOut(title), run_time=0.5)
        self.play(Write(defi))
        self.play(Write(defi2))
        self.wait(2)
        self.play(ApplyMethod(group2.to_edge, UP))
        #
        self.play(DrawBorderThenFill(conjuntoA), rate_func=linear)
        self.play(Write(nameA))
        self.wait(1)
        self.play(Write(note), run_time=6)
        self.wait(1)
        self.play(FadeOut(group))
        #
        self.play(Write(text1))
        self.wait(2)
        self.play(ReplacementTransform(text1, text2))
        self.play(ApplyMethod(text2.to_edge, UP))
        self.play(DrawBorderThenFill(conjuntos2), Write(names))
        self.wait()
        self.play(ReplacementTransform(conjuntos2, conjuntos))
        self.wait(9)
        self.play(FadeOut(conjuntos), FadeOut(text2), FadeOut(names))
        #
        self.play(Write(text3))
        self.play(Write(prop1))
        self.wait(14)
        self.play(FadeOut(text3), FadeOut(prop1))