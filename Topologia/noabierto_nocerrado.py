from manimlib.imports import *

########################################
####### NI ABIERTO, NI CERRADO ########
########################################


class ObservacionCerradosAbiertos(Scene):
    def construct(self):
        titulo = TextMobject(
            """Ni abierto,\n
                             ni cerrado """
        ).scale(1.5)
        # OBSERVACION
        text1 = TextMobject("""Consideremos el siguiente conjunto""")
        text1.move_to(3 * UP)
        text1_1 = TextMobject("A").scale(2)
        text1_1.set_color(BLUE_E)
        text1_1.move_to(text1.get_center() + 0.8 * DOWN)
        text2_1 = TextMobject("Obsérvese cómo los puntos añadidos en ", "rojo")
        text2_2 = TextMobject("completan la frontera de ", "A").next_to(text2_1, DOWN)
        text2_1[1].set_color(RED)
        text2_2[1].set_color(BLUE_E)
        text2 = VGroup(text2_1, text2_2)
        text2.move_to(text1)

        text3 = TextMobject("Sin embargo, ", "estos", " no están contenidos en ", "A")
        text3[1].set_color(RED)
        text3[3].set_color(BLUE_E)
        text3.move_to(text1.get_center() + 0.8 * DOWN)
        text3_1_1 = TextMobject("Es decir,")
        text3_1_2 = TexMobject(
            r"Fr(", r"A", r")", r"\not\subset", r"A", color=ORANGE
        ).next_to(text3_1_1, DOWN)
        text3_1_2[1].set_color(BLUE_E)
        text3_1_2[4].set_color(BLUE_E)
        text3_1 = VGroup(text3_1_1, text3_1_2)
        text3_1.move_to(text1)
        text4 = TextMobject("Esto implica que ", "A", " no es ", "cerrado")
        text4[1].set_color(BLUE_E)
        text4[3].set_color(GREEN)
        text4.move_to(text1.get_center() + 0.8 * DOWN)
        text5_1 = TextMobject("Por otro lado, los puntos blancos")
        text5_2 = TextMobject("pertenecen a la frontera de ", "A").next_to(
            text5_1, DOWN
        )
        text5_2[1].set_color(BLUE_E)
        text5 = VGroup(text5_1, text5_2)
        text5.move_to(text1.get_center() + 0.8 * DOWN)
        text5_1_1 = TextMobject("Es decir,")
        text5_1_2 = TexMobject(
            r"Fr(", r"A", r")", r"\cap", r"A", r"\neq\emptyset", color=ORANGE
        ).next_to(text5_1_1, DOWN)
        text5_1_2[1].set_color(BLUE_E)
        text5_1_2[4].set_color(BLUE_E)
        text5_1 = VGroup(text5_1_1, text5_1_2)
        text5_1.move_to(text1)
        text6 = TextMobject(
            "Por lo tanto, ", "A", " no es ", "cerrado", " y no es ", "abierto"
        )
        text6[1].set_color(BLUE_E)
        text6[3].set_color(GREEN)
        text6[5].set_color(YELLOW)
        text6.move_to(text1.get_center() + 0.8 * DOWN)
        text7_1 = TextMobject(
            "Entonces las descripciones de ", "abierto", " y ", "cerrado"
        ).move_to(text1.get_center() + 1.5 * DOWN)
        text7_2 = TextMobject(
            "no son características complementarias ", "de un conjunto,"
        ).next_to(text7_1, DOWN)
        text7_3 = TextMobject("pues dado un conjunto ", "A", ":").next_to(text7_2, DOWN)
        text7_4 = TexMobject(
            r"\text{A}",
            r"\text{ no abierto  }",
            r"\text{no implica}",
            r"\text{  A}",
            r"\text{ cerrado}",
            color=WHITE,
        ).next_to(text7_3, 2 * DOWN)
        text7_5 = TexMobject(
            r"\text{A}",
            r"\text{ no cerrado  }",
            r"\text{no implica}",
            r"\text{  A}",
            r"\text{ abierto}",
            color=WHITE,
        ).next_to(text7_4, 1.5 * DOWN)
        text7_1[1].set_color(YELLOW)
        text7_1[3].set_color(GREEN)
        text7_4[2].set_color(RED)
        text7_5[2].set_color(RED)
        text7 = VGroup(text7_1, text7_2, text7_3)
        pregunta_1 = TextMobject("Ahora que sabes más de los conjuntos ", "abiertos")
        pregunta_2 = TextMobject(
            "y ", "cerrados", ", ¿puedes responder lo siguiente?"
        ).next_to(pregunta_1, DOWN)
        pregunta_1[1].set_color(YELLOW)
        pregunta_2[1].set_color(GREEN)
        pregunta = VGroup(pregunta_1, pregunta_2)
        pregunta_copy = pregunta.copy()
        pregunta_copy.move_to(text1.get_center() + 0.8 * DOWN)
        pregunta0 = TextMobject("Sea ", "A", " un conjunto:").next_to(
            pregunta_copy, DOWN * 2
        )
        pregunta1 = TextMobject(
            "¿Int(A)", " es ", "abierto", " o ", "cerrado", "?"
        ).next_to(pregunta0, DOWN * 1.5)
        pregunta1[2].set_color(YELLOW)
        pregunta1[4].set_color(GREEN)
        pregunta2 = TextMobject(
            "¿Fr(A)", " es ", "abierta", " o ", "cerrada", "?"
        ).next_to(pregunta1, DOWN * 1.5)
        pregunta2[2].set_color(YELLOW)
        pregunta2[4].set_color(GREEN)
        pregunta3 = TextMobject(
            "Dado ",
            "$x_0$",
            "$\in$",
            "A",
            " y ",
            "r ",
            "$> 0$",
            ", ¿",
            "$B_r(x_0)$ ",
            " es ",
            "abierto",
            " o ",
            "cerrado",
            "?",
        ).next_to(pregunta2, DOWN * 1.5)
        pregunta3[1].set_color(ORANGE)
        pregunta3[10].set_color(YELLOW)
        pregunta3[12].set_color(GREEN)
        obs1 = SVGMobject("Topologia_SVGs/observacion1.svg")
        obs1.move_to(1 * DOWN)
        obs1.scale(2.5)
        obs1[0:1].set_color(BLUE_E)
        obs1[0:1].set_stroke(BLUE_E)
        obs1[1:2].set_color(BLUE_E)
        obs1[1:2].set_stroke(WHITE)
        obs1[2:3].set_stroke(WHITE)
        obs1[2:3].set_color(BLUE_E)

        obs1_1 = obs1.copy()
        obs1_1.move_to(1 * DOWN)
        obs1_1[0:1].set_color(BLUE_E)
        obs1_1[0:1].set_stroke(RED)
        obs1_1[1:2].set_color(BLUE_E)
        obs1_1[1:2].set_stroke(WHITE)
        obs1[2:3].set_stroke(BLUE_E)
        obs1[2:3].set_color(BLUE_E)

        obs1_2 = SVGMobject("Topologia_SVGs/observacion1.svg")
        obs1_2.move_to(1 * DOWN)
        obs1_2.scale(2.5)
        obs1_2[0:1].set_color(BLUE_E)
        obs1_2[0:1].set_stroke(BLUE_E)
        obs1_2[1:2].set_color(BLUE_E)
        obs1_2[1:2].set_stroke(WHITE)
        obs1_2[2:3].set_stroke(BLUE_E)
        obs1_2[2:3].set_color(BLUE_E)

        obs1_3 = obs1.copy()

        # Secuencia de la animación
        self.play(Write(titulo))
        self.wait()
        self.play(FadeOut(titulo))
        self.play(Write(text1))
        self.play(Write(text1_1))
        self.play(SpinInFromNothing(obs1))
        self.wait(2)
        self.play(ReplacementTransform(text1, text2), FadeOut(text1_1))
        self.wait(7)
        self.play(ReplacementTransform(obs1, obs1_1))
        self.wait(1.5)
        self.play(ReplacementTransform(text2, text3))
        self.wait(1.5)
        self.play(ReplacementTransform(obs1_1, obs1_2))
        self.wait()
        self.play(ReplacementTransform(text3, text3_1))
        self.wait(6)
        self.play(ReplacementTransform(text3_1, text4))
        self.wait(2)
        self.play(ReplacementTransform(obs1_2, obs1_3))
        self.play(ReplacementTransform(text4, text5))
        self.wait(2.5)
        self.play(ReplacementTransform(text5, text5_1))
        self.wait(7)
        self.play(ReplacementTransform(text5_1, text6))
        self.wait(3)
        self.play(FadeOut(text6), ShrinkToCenter(obs1_3))

        self.play(Write(text7))
        self.wait(9)
        self.play(Write(text7_4))
        self.wait(1.5)
        self.play(Write(text7_5))
        self.wait(1.5)
        self.play(FadeOut(text7), FadeOut(text7_4), FadeOut(text7_5))

        self.play(Write(pregunta))
        self.wait()
        self.play(ReplacementTransform(pregunta, pregunta_copy))
        self.play(Write(pregunta0))
        self.wait(0.4)
        self.play(Write(pregunta1))
        self.wait(3)
        self.play(Write(pregunta2))
        self.wait(7)
        self.play(Write(pregunta3))
        self.wait(10)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()