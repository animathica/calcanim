from manimlib.imports import *


#########################
#### CONJUNTOS ABIERTOS #####
#########################


class Conjuntos_abiertos(Scene):
    def construct(self):
 
        # PRIMERA CARACTERIZACION

        titulo =TextMobject("Conjuntos Abiertos").scale(1.5)
        text1 = TextMobject("Veamos el siguiente conjunto")
        text1.move_to(3 * UP)
        text2 = TextMobject("A").scale(2)
        text2.move_to(text1.get_center() + DOWN)
        text2.set_color(PURPLE)
        text3_10 = TextMobject(
            "Consideramos un ", "borde", " añadido alrededor del conjunto ", "A"
        )
        text3_10[1].set_color(BLUE_C)
        text3_10[3].set_color(PURPLE)
        text3_10.move_to(text1.get_center() + 0.3 * DOWN)

        text3_11 = TextMobject("Podemos dibujar una bola con centro en")
        text3_11_1 = TextMobject("cualquier punto de este ", "borde").next_to(
            text3_11, DOWN
        )
        text3_11_1[1].set_color(BLUE_C)
        text3 = VGroup(text3_11, text3_11_1)
        text3.move_to(text1.get_center() + 0.3 * DOWN)

        text3_1_1 = TextMobject("Y con cualquier radio, la bola intersecta el")
        text3_1_2 = TextMobject("conjunto ", "A", " y el exterior de este").next_to(
            text3_1_1, DOWN
        )
        text3_1_2[1].set_color(PURPLE)
        text3_1 = VGroup(text3_1_1, text3_1_2)
        text3_1.move_to(text3)

        text4_1 = TextMobject("Con esta observación decimos que todos los puntos")
        text4_2 = TextMobject(
            "en el ", "borde", " representan la ", "frontera de ", "A"
        ).next_to(text4_1, DOWN)
        text4_2[4].set_color(PURPLE)
        text4_2[3].set_color(BLUE_C)
        text4_2[1].set_color(BLUE_C)
        text4 = VGroup(text4_1, text4_2)
        text4.move_to(text3.get_center())

        text5_1 = TextMobject(
            "Sin embargo,", " ningún elemento de la ", "frontera de ", "A"
        )
        text5_2 = TextMobject("está contenido en ", "A").next_to(text5_1, DOWN)
        text5_1[3].set_color(PURPLE)
        text5_1[2].set_color(BLUE_C)
        text5_2[1].set_color(PURPLE)
        text5 = VGroup(text5_1, text5_2)
        text5.move_to(text4.get_center())

        def1_1 = TextMobject("A los conjuntos que cumplen con lo anterior")
        def1_2 = TextMobject("se les denomina conjuntos ", "ABIERTOS").next_to(
            def1_1, DOWN
        )
        def1_2[1].set_color(YELLOW)
        def1 = VGroup(def1_1, def1_2)
        def2 = TextMobject(
            "En otras palabras, un conjunto A es ",
            "abierto",
            " si",
            "$$Fr(A) \\cap A=\\emptyset $$",
        )
        def2[1].set_color(YELLOW)
        def2[3].set_color(YELLOW)
        creature = SVGMobject(
            "Topologia_SVGs/abierto.svg", fill_color=PURPLE, color=BLACK
        )
        creature.move_to(DOWN)
        creature.scale(3)
        creature1 = SVGMobject(
            "Topologia_SVGs/abierto.svg", fill_color=PURPLE, color=BLUE_C
        )
        creature1.move_to(DOWN)
        creature1.scale(3)
        creature2 = creature.copy()

        punto1 = Dot(color=BLUE_C)
        punto1.next_to(creature, RIGHT, buff=1)
        circulo1 = Circle(color=RED, radius=1)
        circulo1.move_to(punto1)
        circulo1_1 = Circle(color=RED, radius=0.5)
        circulo1_1.move_to(punto1)

        punto2 = Dot(color=BLUE_C)
        punto2.next_to(creature, LEFT, buff=1.12)
        circulo2 = Circle(color=RED, radius=1)
        circulo2.move_to(punto2)
        circulo2_1 = Circle(color=RED, radius=2)
        circulo2_1.move_to(punto2)

        # Segunda caracterizacion
        titulo1 = TextMobject(
            """Segunda Caracterización \n 
                             de Conjuntos Abiertos"""
        )

        text7_1 = TextMobject("Decimos que un conjunto es ", "abierto", " si")
        text7_2 = TextMobject("todos sus puntos son interiores").next_to(text7_1, DOWN)
        text7_1[1].set_color(YELLOW)
        text7 = VGroup(text7_1, text7_2)
        text8_1 = TextMobject("""Consideremos el mismo conjunto""")
        text8_1.move_to(3 * UP)
        text8_2 = TextMobject("A").scale(2)
        text8_2.move_to(text1.get_center() + DOWN)
        text8_2.set_color(PURPLE)
        text9_1 = TextMobject("Notemos que al tomar cualquier punto en ", "A", ",")
        text9_2 = TextMobject("este se mantiene en el interior de ", "A").next_to(
            text9_1, DOWN
        )
        text9_1[1].set_color(PURPLE)
        text9_2[1].set_color(PURPLE)
        text9 = VGroup(text9_1, text9_2)
        text9.move_to(text1)
        text10_1 = TextMobject("Por ello decimos que todos los elementos")
        text10_2 = TextMobject("de ", "A", " son puntos interiores").next_to(
            text10_1, DOWN
        )
        text10_2[1].set_color(PURPLE)
        text10 = VGroup(text10_1, text10_2)
        text11_1 = TextMobject("Entonces decimos que un conjunto es ", "abierto", " si")
        text11_2 = TextMobject("todos sus puntos son interiores").next_to(
            text11_1, DOWN
        )
        text11_1[1].set_color(YELLOW)
        text11 = VGroup(text11_1, text11_2)
        text12_1 = TextMobject("De manera más formal,")
        text12_2 = TextMobject("Un conjunto ", "A", " es ", "abierto", " si").next_to(
            text12_1, DOWN + 0.5 * DOWN
        )
        text12_3 = TexMobject(
            r"\forall x \in A", "\\text{, x es punto interior}"
        ).next_to(text12_2, DOWN)
        text12_2[3].set_color(YELLOW)
        text12 = VGroup(text12_1, text12_2, text12_3)
        text12_1.move_to(UP)
        creature3 = SVGMobject(
            "Topologia_SVGs/abierto.svg", fill_color=PURPLE, fill_opacity=1, color=BLACK
        )
        creature3.move_to(DOWN)
        creature3.scale(3)
        punto3 = Dot()
        punto3.move_to(creature3.get_center() + 0.5 * RIGHT)
        circulo3 = Circle(color=RED, radius=0.5)
        circulo3.move_to(punto3)

        punto4 = Dot()
        punto4.move_to(creature3.get_center() + 1.5 * RIGHT + 2 * UP)
        circulo4 = Circle(color=RED, radius=0.15)
        circulo4.move_to(punto4)

        punto5 = Dot()
        punto5.move_to(creature3.get_center() + 1.9 * LEFT + 1.41 * DOWN)
        circulo5 = Circle(color=RED, radius=0.12)
        circulo5.move_to(punto5)

        # PRIMERA CARACTERIZACION
        self.play(Write(titulo))
        self.wait()
        self.play(FadeOut(titulo))
        self.wait(0.5)
        self.play(Write(text1))
        self.play(Write(text2))
        self.play(SpinInFromNothing(creature))
        self.wait()
        self.play(FadeOut(text1), FadeOut(text2))
        self.play(Write(text3_10), ReplacementTransform(creature, creature1))
        self.wait(1.5)
        self.play(ReplacementTransform(text3_10, text3))
        self.wait()
        self.play(FadeIn(punto1), FadeIn(circulo1))
        self.wait(1.5)
        self.play(ReplacementTransform(text3, text3_1))
        self.wait()
        self.play(ReplacementTransform(circulo1, circulo1_1))
        self.wait(0.5)
        self.play(FadeOut(punto1), FadeOut(circulo1_1))
        self.play(FadeIn(punto2), FadeIn(circulo2))
        self.wait()
        self.play(ReplacementTransform(circulo2, circulo2_1))
        self.play(FadeOut(punto2), FadeOut(circulo2_1))
        self.play(ReplacementTransform(text3_1, text4))
        self.wait(3.5)
        self.play(ReplacementTransform(text4, text5))
        self.wait(1.5)
        self.play(ReplacementTransform(creature1, creature2))
        self.wait(1.5)
        self.play(FadeOut(creature2))
        self.play(Write(def1))
        self.wait(3)
        self.play(FadeOut(def1), FadeOut(text5))
        self.play(Write(def2))
        self.wait(3.5)
        self.play(FadeOut(def2))
        self.wait()

        # SEGUNDA CARACTERIZACION

        self.play(Write(titulo1))
        self.wait()
        self.play(FadeOut(titulo1))
        self.play(Write(text7))
        self.play(FadeOut(text7))
        self.wait()
        self.play(Write(text8_1))
        self.play(Write(text8_2))
        self.play(GrowFromCenter(creature3))
        self.wait()
        self.play(ReplacementTransform(text8_1, text9), FadeOut(text8_2))
        self.play(FadeIn(punto3), FadeIn(circulo3))
        self.wait()
        self.play(
            ReplacementTransform(punto3, punto4),
            ReplacementTransform(circulo3, circulo4),
        )
        self.wait()
        self.play(
            ReplacementTransform(punto4, punto5),
            ReplacementTransform(circulo4, circulo5),
        )
        self.wait()
        self.play(FadeOut(punto5), FadeOut(circulo5))
        self.wait(3)
        self.play(FadeOut(creature3))
        self.play(ReplacementTransform(text9, text10))
        self.wait()
        self.play(FadeOut(text10))
        self.play(Write(text11))
        self.wait(2.5)
        self.play(ReplacementTransform(text11, text12))
        self.wait(2)

        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()


#########################
#### CONJUNTOS CERRADOS #####
#########################


class Conjuntos_cerrados(Scene):
    def construct(self):

        titulo = TextMobject("Conjuntos Cerrados").scale(1.5)

        # PRIMERA CARACTERIZACION

        text1 = TextMobject("Consideremos el siguiente conjunto")
        text1.move_to(3 * UP)
        text1_1 = TextMobject("B").scale(2)
        text1_1.move_to(text1.get_center() + DOWN)
        text1_1.set_color(BLUE_C)
        text2_1 = TextMobject("Podemos tomar un punto sobre la orilla de ", "B")
        text2_2 = TextMobject("y dibujar una bola con centro en ese punto").next_to(
            text2_1, DOWN
        )
        text2_1[1].set_color(BLUE_C)
        text2 = VGroup(text2_1, text2_2)
        text2.move_to(2.5 * UP)
        text3_1 = TextMobject("Para todo radio, la bola intersecta al")
        text3_2 = TextMobject("conjunto ", "B", " y a su complemento").next_to(
            text3_1, DOWN
        )
        text3_2[1].set_color(BLUE_B)
        text3 = VGroup(text3_1, text3_2)
        text3.move_to(text2)
        text4_1 = TextMobject("A esta ", "orilla", " se le llama ", "frontera de ", "B")
        text4_2 = TextMobject("y se denota como ", "$Fr($", "B", "$)$").next_to(
            text4_1, DOWN
        )
        text4_1[1].set_color(RED)
        text4_1[3].set_color(RED)
        text4_1[4].set_color(BLUE_C)
        text4_2[1].set_color(RED)
        text4_2[2].set_color(BLUE_C)
        text4_2[3].set_color(RED)
        text4 = VGroup(text4_1, text4_2)
        text4.move_to(text2)
        text5_1 = TextMobject(
            "Obsérvese que todos los puntos en la ", "frontera de ", "B"
        )
        text5_2 = TextMobject("están contenidos en el mismo conjunto ", "B").next_to(
            text5_1, DOWN
        )
        text5_1[1].set_color(RED)
        text5_1[2].set_color(BLUE_C)
        text5_2[1].set_color(BLUE_C)
        text5 = VGroup(text5_1, text5_2)
        text5.move_to(text2)
        text6_1 = TextMobject("A los conjuntos que cumplen lo anterior se")
        text6_2 = TextMobject("les denomina conjuntos ", "CERRADOS").next_to(
            text6_1, DOWN
        )
        text6_2[1].set_color(GREEN)
        text6 = VGroup(text6_1, text6_2)
        def1_1 = TextMobject("De manera más formal,")
        def1_2 = TextMobject("un conjunto ", "A", " es ", "cerrado", " si:").next_to(
            def1_1, DOWN + 0.5 * DOWN
        )
        def1_3 = TexMobject(r"Fr(A) \subset A", color=ORANGE).next_to(def1_2, DOWN)
        def1_2[1].set_color(ORANGE)
        def1_2[3].set_color(GREEN)
        def1 = VGroup(def1_1, def1_2, def1_3)
        def1.move_to(UP)

        cerrado = SVGMobject(
            "cerrado.svg", color=WHITE, fill_color=BLUE_B
        )
        cerrado.move_to(DOWN)
        cerrado.scale(3)
        cerrado1 = cerrado.copy()
        cerrado1.set_stroke(RED)
        cerrado2 = SVGMobject(
            "cerrado.svg", color=WHITE, fill_color=BLUE_B
        )
        cerrado2.move_to(DOWN)
        cerrado2.scale(3)

        punto1 = Dot(color=RED)
        punto1.next_to(cerrado, LEFT, buff=-0.22)
        circulo1 = Circle(color=RED, radius=0.5)
        circulo1.move_to(punto1)
        circulo1_1 = Circle(color=RED, radius=2)
        circulo1_1.move_to(punto1)

        punto2 = Dot(color=RED)
        punto2.next_to(cerrado, UP + RIGHT, buff=-0.1)
        circulo2 = Circle(color=RED, radius=1)
        circulo2.move_to(punto2)
        circulo2_1 = Circle(color=RED, radius=0.4)
        circulo2_1.move_to(punto2)

        # Segunda caracterizacion

        titulo2 = TextMobject(
            """Segunda Caracterización \n
                            de Conjuntos Cerrados"""
        )
        text7 = TextMobject("""Tomemos el mismo conjunto""")
        text7.move_to(3 * UP)
        text7_1 = TextMobject("B").scale(2)
        text7_1.move_to(text7.get_center() + DOWN)
        text7_1.set_color(BLUE_B)
        text8_1 = TextMobject("Consideremos un punto que no esté contenido")
        text8_2 = TextMobject(
            "en ", "B", ", sino en su complemento,", " B", "$^{\\text{c}}$"
        ).next_to(text8_1, DOWN)
        text8_2[1].set_color(BLUE_C)
        text8_2[3].set_color(BLUE_C)
        text8_2[4].set_color(RED)
        text8 = VGroup(text8_1, text8_2)
        text8.move_to(text2)
        text9_1 = TextMobject("Es entonces posible dibujar una bola que")
        text9_2 = TextMobject(
            "esté completamente contenida en ", "B", "$^{\\text{c}}$"
        ).next_to(text9_1, DOWN)
        text9_2[1].set_color(BLUE_C)
        text9_2[2].set_color(RED)
        text9 = VGroup(text9_1, text9_2)
        text9.move_to(text2)
        # text10=TextMobject('''Y queda contenida en Ext(B)''')
        # text10.move_to(text7)
        text11_1 = TextMobject(
            "Esto se cumple para todo punto en ", "B", "$^{\\text{c}}$", " y es"
        )
        text11_2 = TextMobject(
            "equivalente a decir que ",
            "B",
            "$^{\\text{c}}$",
            " es un conjunto ",
            "abierto",
        ).next_to(text11_1, DOWN)
        text11_1[1].set_color(BLUE_C)
        text11_1[2].set_color(RED)
        text11_2[1].set_color(BLUE_C)
        text11_2[2].set_color(RED)
        text11_2[4].set_color(YELLOW)
        text11 = VGroup(text11_1, text11_2)
        text11.move_to(text2)
        text12_1 = TextMobject(
            "Entonces se dice que un conjunto ", "B", " es ", "cerrado ", "si"
        )
        text12_2 = TextMobject("B", "$^{\\text{c}}$", " es un ", "abierto").next_to(
            text12_1, DOWN
        )
        text12_1[1].set_color(BLUE_C)
        text12_1[3].set_color(GREEN)
        text12_2[0].set_color(BLUE_C)
        text12_2[1].set_color(RED)
        text12_2[3].set_color(YELLOW)
        text12 = VGroup(text12_1, text12_2)
        pregunta_1 = TextMobject("¿Consideras que los conjuntos se pueden")
        pregunta_2 = TextMobject(
            "clasificar únicamente como ", "abiertos", " y ", "cerrados", "?"
        ).next_to(pregunta_1, DOWN)
        pregunta_2[1].set_color(YELLOW)
        pregunta_2[3].set_color(GREEN)
        pregunta = VGroup(pregunta_1, pregunta_2)
        cerrado3 = SVGMobject(
            "cerrado.svg", color=WHITE, fill_color=BLUE_B
        )
        cerrado3.move_to(DOWN)
        cerrado3.scale(3)

        punto3 = Dot(color=RED)
        punto3.move_to(cerrado3.get_center() + LEFT + 2 * DOWN)
        circulo3 = Circle(color=RED, radius=0.8)
        circulo3.move_to(punto3)

        punto4 = Dot(color=RED)
        punto4.move_to(cerrado3.get_center() + 1.5 * RIGHT + 2 * UP)
        circulo4 = Circle(color=RED, radius=0.24)
        circulo4.move_to(punto4)

        # PRIMERA CARACTERIZACION

        # Secuencia de la animación
        self.play(Write(titulo))
        self.wait()
        self.play(FadeOut(titulo))
        self.play(Write(text1))
        self.play(Write(text1_1))
        self.play(SpinInFromNothing(cerrado))
        self.wait()
        self.play(FadeOut(text1_1), ReplacementTransform(text1, text2))
        self.wait()
        self.play(FadeIn(punto1))
        self.wait(0.5)
        self.play(FadeIn(circulo1))
        self.wait()
        self.play(ReplacementTransform(text2, text3))
        self.play(ReplacementTransform(circulo1, circulo1_1))
        self.wait()
        self.play(FadeOut(circulo1_1), FadeOut(punto1))
        self.play(
            ReplacementTransform(punto1, punto2),
            ReplacementTransform(circulo1_1, circulo2),
        )
        self.play(ReplacementTransform(circulo2, circulo2_1))
        self.wait(1.5)
        self.play(FadeOut(circulo2_1), FadeOut(punto2))
        self.play(ReplacementTransform(cerrado, cerrado1))
        self.play(ReplacementTransform(text3, text4))
        self.wait()
        self.play(ReplacementTransform(cerrado, cerrado1))
        self.wait(3)
        self.play(ReplacementTransform(text4, text5))
        self.wait(3.5)
        self.play(ReplacementTransform(cerrado1, cerrado2))
        self.wait(1.5)
        self.play(FadeOut(cerrado2))
        self.wait()
        self.play(Write(text6))
        self.wait(2.5)
        self.play(FadeOut(text5), FadeOut(text6))
        self.wait(0.5)
        self.play(Write(def1))
        self.wait(8)
        self.play(FadeOut(def1))
        self.wait(0.5)

        # SEGUNDA CARACTERIZACION
        # Secuenca de la animación
        self.play(Write(titulo2))
        self.play(FadeOut(titulo2))
        self.play(Write(text7))
        self.play(Write(text7_1))
        self.play(DrawBorderThenFill(cerrado3))
        self.wait()
        self.play(FadeOut(text7_1), ReplacementTransform(text7, text8))
        self.wait(2.5)
        self.play(FadeIn(punto3))
        self.wait()
        self.play(ReplacementTransform(text8, text9))
        self.wait(8)
        self.play(FadeIn(circulo3))
        self.wait(1.5)
        self.play(ReplacementTransform(text9, text11))
        self.wait(11)
        self.play(
            ReplacementTransform(punto3, punto4),
            ReplacementTransform(circulo3, circulo4),
        )
        self.wait(2.5)
        self.play(
            FadeOut(text11), FadeOut(cerrado3), FadeOut(punto4), FadeOut(circulo4)
        )
        self.play(Write(text12))
        self.wait(11)
        self.play(ReplacementTransform(text12, pregunta))
        self.wait(5)

        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()


#########################
#### OBSERVACION CERRADOS/ABIERTOS #####
#########################


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


# Para versiones anteriores de manim usar:
# from big_ol_pile_of_manim_imports import *


#### SUGERENCIA: SIEMPRE QUE CAMBIESLOS VECTORES A VISUALIZAR ###
### CONSIDERA QUE EL PLNO ES DE [-7,7]x[-4,4] ####

#### ESTE GRID SOLO SE USA PARA LA CLASE BOLAS ####


class Grid(VGroup):
    CONFIG = {
        "height": 6.0,
        "width": 6.0,
    }

    def __init__(self, rows, columns, **kwargs):
        digest_config(self, kwargs, locals())
        super().__init__(**kwargs)

        x_step = self.width / self.columns
        y_step = self.height / self.rows

        for x in np.arange(0, self.width + x_step, x_step):
            self.add(
                Line(
                    [x - self.width / 2.0, -self.height / 2.0, 0],
                    [x - self.width / 2.0, self.height / 2.0, 0],
                )
            )
        for y in np.arange(0, self.height + y_step, y_step):
            self.add(
                Line(
                    [-self.width / 2.0, y - self.height / 2.0, 0],
                    [self.width / 2.0, y - self.height / 2.0, 0],
                )
            )


#############################
#### DISCONEXOS/CONEXOS #####
#############################

##Vídeo conjuntos conexos y diconexos
class ConjuntosConexos(Scene):
    def construct(self):
        # Título y texto
        titulo = TextMobject("Disconexidad y Conexidad").scale(1.5)
        intui = TextMobject(
            "De forma intuitiva, un conjunto", " disconexo", " es aquel"
        )
        intui[1].set_color(GREEN_C)
        tivo = TextMobject("compuesto por dos o más partes", " separadas").next_to(
            intui, DOWN
        )
        tivo[1].set_color(GREEN_C)
        intuitivo = VGroup(intui, tivo)
        tdisconexo_a = TextMobject(
            "Formalmente, un conjunto es", " disconexo", " si y sólo si"
        )
        tdisconexo_a[1].set_color(GREEN_C)
        tdisconexo_b = TextMobject(
            "satisface tres propiedades con respecto a otros conjuntos:"
        ).next_to(tdisconexo_a, DOWN)
        tdisconexo = VGroup(tdisconexo_a, tdisconexo_b)

        # Conjunto disconexo
        el_disconexo = TextMobject(
            " A", " es un conjunto", " disconexo", " si y sólo si "
        ).to_edge(UP)
        el_disconexo[0].set_color(GREEN_C)
        el_disconexo[2].set_color(GREEN_C)
        disconexo = SVGMobject(
            "Topologia_SVGs/disconexo.svg",
            fill_color=GREEN_C,
            fill_opacity=1,
            stroke_opacity=0,
        ).shift(3 * LEFT)
        disconexo_label = (
            TextMobject("A")
            .next_to(disconexo.get_center(), 5 * DOWN)
            .set_color(GREEN_C)
        )
        gdisconexo = VGroup(disconexo, disconexo_label)

        # Conjuntos abiertos
        abiertos = (
            TextMobject("Existen ", "U", " y", " V", " conjuntos abiertos tales que:")
            .scale(0.9)
            .shift(2 * UP + 3 * RIGHT)
        )
        abiertos[1].set_color(ORANGE)
        abiertos[3].set_color(YELLOW)
        cjtoU_set = (
            Circle(radius=1.0, fill_opacity=0.6, stroke_opacity=0,stroke_width=0)
            .shift(4.2 * LEFT)
            .set_color(ORANGE)
        )
        cjtoU_label = TextMobject("U").next_to(cjtoU_set, UP).set_color(ORANGE)
        cjtoU = VGroup(cjtoU_set, cjtoU_label)
        cjtoV_set = (
            Circle(radius=1.0, fill_opacity=0.6, stroke_opacity=0,stroke_width=0)
            .shift(1.8 * LEFT)
            .set_color(YELLOW)
        )
        cjtoV_label = TextMobject("V").next_to(cjtoV_set, UP).set_color(YELLOW)
        cjtoV = VGroup(cjtoV_set, cjtoV_label)
        cjtoU1_set = (
            Circle(radius=1.5, fill_opacity=0.6, stroke_opacity=0,stroke_width=0)
            .shift(4.2 * LEFT)
            .set_color(ORANGE)
        )
        cjtoU1_label = TextMobject("U").next_to(cjtoU1_set, UP).set_color(ORANGE)
        cjtoU1 = VGroup(cjtoU1_set, cjtoU1_label)
        cjtoV1_set = (
            Circle(radius=1.5, fill_opacity=0.6, stroke_opacity=0,stroke_width=0)
            .shift(1.8 * LEFT)
            .set_color(YELLOW)
        )
        cjtoV1_label = TextMobject("V").next_to(cjtoV1_set, UP).set_color(YELLOW)
        cjtoV1 = VGroup(cjtoV1_set, cjtoV1_label)
        inter = (
            SVGMobject("Topologia_SVGs/inter.svg", stroke_opacity=0, fill_opacity=0.8)
            .shift(3 * LEFT)
            .scale(0.93)
        )  # A ojo para darle al tamaño
        inter_label = TexMobject(r" U \cap V").next_to(inter, 2 * UP)
        intergroup = VGroup(inter, inter_label)
        abiertos_labels = VGroup(cjtoU_label, cjtoV_label)
        abiertos_labels1 = VGroup(cjtoU1_label, cjtoV1_label)
        union_label = (
            TexMobject(r" U \cup V").next_to(inter, 2.5 * UP).set_color(YELLOW_E)
        )

        # Primera propiedad

        prop_1 = TexMobject(r"1)\ A \subset U \cup V").shift(1 * UP + 1.8 * RIGHT)
        prop_1a = TexMobject(r"\text{1)}", r"\ A ", r"\subset", r"{U \cup V}").shift(
            1 * UP + 1.8 * RIGHT
        )
        prop_1a.set_color_by_tex_to_color_map({"A": GREEN_C, "{U \cup V}": YELLOW_E})

        # Segunda propiedad

        prop_2 = TexMobject(r"2)\ A \cap U \neq \varnothing").shift(1.82 * RIGHT)
        prop_2_2 = TexMobject(r"\text{y}\ A \cap V \neq \varnothing").next_to(
            prop_2, RIGHT
        )

        # Tercera propiedad

        prop_3 = TexMobject(r"3) \ U \cap V = \varnothing").shift(
            1 * DOWN + 1.82 * RIGHT
        )
        caracts = VGroup(prop_1, prop_2, prop_3)

        # Comenzamos con conexos
        conex_a = TextMobject(
            "Un conjunto es",
            " conexo",
            "  si \\textbf{no} es",
            " disconexo",
            " es decir,",
        )
        conex_a[1].set_color(BLUE)
        conex_a[3].set_color(GREEN_C)
        conex_b = TextMobject("si cualesquiera dos conjuntos abiertos U y V no cumplen").next_to(
            conex_a, DOWN
        )
        conex_c = TextMobject("alguna de las tres propiedades.").next_to(conex_b, DOWN)
        conex = VGroup(conex_a, conex_b, conex_c)
        ejs = TextMobject("Veamos algunos ejemplos:")

        satisface = TextMobject("El conjunto satisface:").move_to(abiertos)
        no_satisface1 = (
            TextMobject("\\textbf{No} satisface la primera propiedad, pues:")
            .shift(1 * DOWN + 3.2 * RIGHT)
            .scale(0.75)
        )
        no_satisface2 = (
            TextMobject("\\textbf{No} satisface la segunda propiedad, pues:")
            .shift(1 * DOWN + 3.2 * RIGHT)
            .scale(0.75)
        )
        no_satisface3 = (
            TextMobject("\\textbf{No} satisface la tercera propiedad, pues:")
            .shift(1 * DOWN + 3.2 * RIGHT)
            .scale(0.75)
        )

        esconexo = TextMobject("Este conjunto es", " conexo.").to_edge(DOWN)
        esconexo[1].set_color(BLUE)

        # Conexo1

        conexo1_svg = (
            SVGMobject(
                "Topologia_SVGs/conexo1.svg",
                stroke_opacity=0,
                fill_opacity=1,
                fill_color=BLUE,
            )
            .shift(3 * LEFT)
            .scale(0.5)
        )
        conexo1_label = TextMobject("B").next_to(conexo1_svg, 4 * DOWN).set_color(BLUE)
        conexo1 = VGroup(conexo1_svg, conexo1_label)

        conexo1_p1 = TexMobject(r" B \subset U \cup V").shift(1 * UP + 1.8 * RIGHT)
        conexo1_p2 = TexMobject(
            r" B \cap U \neq \varnothing\ \text{y}\ B \cap V \neq \varnothing"
        ).shift(3.2 * RIGHT)
        conexo1_p3 = TexMobject(r" U \cap V \neq \varnothing").next_to(
            no_satisface3, DOWN
        )

        textc1 = VGroup(satisface, conexo1_p1, conexo1_p2, conexo1_p3, no_satisface3)

        # Conexo2

        conexo2_svg = (
            SVGMobject(
                "Topologia_SVGs/conexo2.svg",
                stroke_opacity=0,
                fill_opacity=1,
                fill_color=BLUE,
            )
            .shift(4 * LEFT)
            .scale(0.5)
        )
        conexo2_label = TextMobject("C").next_to(conexo2_svg, 5 * DOWN).set_color(BLUE)
        conexo2 = VGroup(conexo2_svg, conexo2_label)
        conexo2_p1 = TexMobject(r" C \subset U \cup V").shift(1 * UP + 1.8 * RIGHT)
        conexo2_p3 = TexMobject(r" U \cap V = \varnothing").shift(2.2 * RIGHT)
        conexo2_p2 = TexMobject(r"\ C \cap V = \varnothing").next_to(
            no_satisface3, DOWN
        )
        textc2 = VGroup(satisface, conexo2_p1, conexo2_p2, conexo2_p3, no_satisface2)

        # Conexo3

        conexo3_svg = (
            SVGMobject(
                "Topologia_SVGs/conexo3.svg",
                stroke_opacity=0,
                fill_opacity=1,
                fill_color=BLUE,
            )
            .shift(3.05 * LEFT + 0.5 * UP)
            .scale(1)
        )
        conexo3_label = TextMobject("D").next_to(conexo3_svg, 3 * UP).set_color(BLUE)
        conexo3 = VGroup(conexo3_svg, conexo3_label)

        # Etiquetas de unión e interseccion para mostrar abajo

        inter_dlabel = TexMobject(r" U \cap V").next_to(inter, 2 * DOWN)
        union_dlabel = (
            TexMobject(r" U \cup V").next_to(inter, 2.5 * DOWN).set_color(YELLOW_E)
        )
        conexo3_p2 = TexMobject(
            r" D \cap U \neq \varnothing\ \text{y}\ D \cap V \neq \varnothing"
        ).shift(1 * UP + 3 * RIGHT)
        conexo3_p3 = TexMobject(r" U \cap V = \varnothing").shift(2.2 * RIGHT)
        conexo3_p1 = TexMobject(r" D \not\subset U \cup V").next_to(no_satisface3, DOWN)
        textc3 = VGroup(satisface, conexo3_p1, conexo3_p2, conexo3_p3, no_satisface1)

        # Comentario final

        cfinal_a = TextMobject(
            "¡Si un conjunto es", " conexo", ", ningún par de conjuntos abiertos"
        )
        cfinal_a[1].set_color(BLUE)
        cfinal_b = TextMobject("podrán satisfacer las tres propiedades mencionadas!").next_to(
            cfinal_a, DOWN
        )
        cfinal = VGroup(cfinal_a, cfinal_b)

        # Secuencia de la animación

        self.play(Write(titulo))
        self.play(FadeOut(titulo))
        self.play(Write(intuitivo))
        self.wait(8)
        self.play(FadeOut(intuitivo))
        self.play(Write(tdisconexo))
        self.wait(8)
        self.play(FadeOut(tdisconexo))
        # Propiedades de un conjunto disconexo
        self.play(Write(el_disconexo))
        self.play(DrawBorderThenFill(disconexo), Write(disconexo_label))
        self.wait()
        self.play(Write(abiertos))
        self.bring_to_back(cjtoU)
        self.play(Write(cjtoU))
        self.bring_to_back(cjtoV)
        self.play(Write(cjtoV))
        self.play(Write(prop_1), abiertos_labels.set_opacity, 0)
        self.play(
            cjtoU_set.set_color,
            YELLOW_E,
            cjtoU_set.set_opacity,
            0.6,
            cjtoV_set.set_color,
            YELLOW_E,
            cjtoV_set.set_opacity,
            0.6,
            Write(union_label),
        )
        self.wait(1.5)
        self.play(FadeOut(union_label), FadeOut(cjtoU_set), FadeOut(cjtoV_set))
        self.wait()
        self.play(Write(prop_2))
        self.play(
            cjtoU_label.set_opacity,
            0.9,
            cjtoU_set.set_color,
            ORANGE,
            cjtoU_set.set_opacity,
            0.6,
        )
        self.wait()
        self.play(FadeOut(cjtoU))
        self.wait()
        self.play(Write(prop_2_2))
        self.play(
            cjtoV_label.set_opacity,
            0.9,
            cjtoV_set.set_color,
            YELLOW,
            cjtoV_set.set_opacity,
            0.6,
        )
        self.wait()
        self.play(FadeOut(cjtoV))
        self.wait(1.5)
        self.play(Write(prop_3))
        self.wait(1.5)
        self.play(Write(cjtoU), Write(cjtoV))
        self.wait(1.5)
        self.play(
            FadeOut(cjtoU),
            FadeOut(cjtoV),
            FadeOut(gdisconexo),
            FadeOut(caracts),
            FadeOut(el_disconexo),
            FadeOut(abiertos),
            FadeOut(prop_2_2),
        )
        self.play(Write(conex_a))
        self.wait()
        self.play(Write(conex_b))
        self.play(Write(conex_c))
        self.wait()
        self.play(FadeOut(conex))
        self.play(Write(ejs))
        self.wait()
        self.play(FadeOut(ejs))

        # ANIMACIÓN:PROPIEDADES CONEXO 1

        self.play(DrawBorderThenFill(conexo1))
        self.wait()
        self.play(Write(satisface))
        self.bring_to_back(cjtoU1)
        self.bring_to_back(cjtoV1)
        self.play(Write(cjtoU1), Write(cjtoV1), abiertos_labels1.set_opacity, 1)
        self.wait()
        self.play(Write(conexo1_p1), abiertos_labels1.set_opacity, 0)
        self.play(
            cjtoU1_set.set_color,
            YELLOW_E,
            cjtoU1_set.set_opacity,
            0.6,
            cjtoV1_set.set_color,
            YELLOW_E,
            cjtoV1_set.set_opacity,
            0.6,
            Write(union_label),
        )  ###YELLOW
        self.wait(1.5)
        self.play(Write(conexo1_p2))
        self.play(abiertos_labels1.set_opacity, 1, FadeOut(union_label))
        self.play(
            cjtoU1_set.set_color,
            ORANGE,
            cjtoU1_set.set_opacity,
            0.6,
            cjtoV1_set.set_color,
            YELLOW,
            cjtoV1_set.set_opacity,
            0,
            cjtoV1_label.set_opacity,
            0,
        )
        self.wait()
        self.wait(1.5)
        self.play(cjtoV1_set.set_opacity, 0.6)
        self.wait(1.5)
        self.play(
            cjtoU1_set.set_opacity,
            0.6,
            cjtoV1_set.set_opacity,
            0.6,
            cjtoV1_label.set_opacity,
            1,
            cjtoU1_set.set_opacity,
            0,
            cjtoU1_label.set_opacity,
            0,
        )
        self.wait(1.5)
        self.play(cjtoU1_set.set_opacity, 0.6, cjtoU1_label.set_opacity, 1)
        self.play(Write(no_satisface3))
        self.play(Write(conexo1_p3))
        self.wait(2)
        self.play(Write(esconexo))
        self.wait(8)
        self.play(
            FadeOut(textc1),
            FadeOut(conexo1),
            FadeOut(esconexo),
            FadeOut(abiertos_labels1),
            FadeOut(cjtoV1),
            FadeOut(cjtoU1),
        )

        # ANIMACIÓN:PROPIEDADES CONEXO 2

        self.play(DrawBorderThenFill(conexo2))
        self.wait()
        self.play(Write(satisface))
        self.bring_to_back(cjtoU)
        self.play(
            cjtoU_set.set_color,
            ORANGE,
            cjtoU_set.set_opacity,
            0.6,
            cjtoV_set.set_opacity,
            0.6,
            abiertos_labels.set_opacity,
            1,
        )
        self.play(Write(conexo2_p1), abiertos_labels.set_opacity, 0)
        self.play(
            cjtoU_set.set_color,
            YELLOW_E,
            cjtoU_set.set_opacity,
            0.6,
            cjtoV_set.set_color,
            YELLOW_E,
            cjtoV_set.set_opacity,
            0.6,
            Write(union_label),
        )  ###YELLOW
        self.wait(1.5)
        self.play(Write(conexo2_p3))
        self.play(FadeOut(union_label))
        self.play(
            cjtoU_set.set_color,
            ORANGE,
            cjtoU_set.set_opacity,
            0.6,
            cjtoU_label.set_opacity,
            0.6,
            cjtoV_set.set_color,
            YELLOW,
            cjtoV_set.set_opacity,
            0,
        )
        self.wait()
        self.play(Write(no_satisface2))
        self.play(Write(conexo2_p2))
        self.play(Write(cjtoV_label))
        self.play(cjtoV.set_opacity, 0.6)
        self.wait()
        self.play(Write(esconexo))
        self.wait(1)
        self.play(
            FadeOut(conexo2), FadeOut(textc2), FadeOut(esconexo), cjtoV.set_opacity, 0
        )

        # ANIMACIÓN:PROPIEDADES CONEXO 3

        self.play(Write(conexo3))
        self.wait()
        self.play(
            cjtoU_set.set_color,
            ORANGE,
            cjtoU_set.set_opacity,
            0.6,
            cjtoV_set.set_color,
            YELLOW,
            cjtoV_set.set_opacity,
            0.6,
            cjtoU_label.set_opacity,
            1,
            cjtoV_label.set_opacity,
            1,
        )
        self.play(Write(satisface))
        self.play(Write(conexo3_p2))
        self.play(cjtoU.set_opacity, 0.6, cjtoV.set_opacity, 0)
        self.wait(1.5)
        self.play(cjtoU.set_opacity, 0, cjtoV.set_opacity, 0.6)
        self.wait(1.5)
        self.play(
            cjtoU_set.set_opacity,
            0.6,
            cjtoV_set.set_opacity,
            0.6,
            abiertos_labels.set_opacity,
            1,
        )
        self.wait()
        self.play(Write(conexo3_p3))
        self.wait()
        self.play(Write(no_satisface1))
        self.bring_to_back(cjtoU)
        self.bring_to_back(cjtoV)
        self.play(
            cjtoU_set.set_opacity,
            0.6,
            cjtoV_set.set_opacity,
            0.6,
            abiertos_labels.set_opacity,
            1,
        )
        self.play(Write(conexo3_p1))
        self.play(
            cjtoU_set.set_color,
            YELLOW_E,
            cjtoU_set.set_opacity,
            0.6,
            cjtoV_set.set_color,
            YELLOW_E,
            cjtoV_set.set_opacity,
            0.6,
            abiertos_labels.set_opacity,
            0,
            Write(union_dlabel),
        )
        self.wait(1.5)
        self.play(Write(esconexo))
        self.wait(5)
        self.play(
            FadeOut(textc3),
            FadeOut(conexo3),
            FadeOut(esconexo),
            FadeOut(cjtoU),
            FadeOut(cjtoV),
            FadeOut(union_dlabel),
            cjtoV_set.set_opacity,
            0,
            cjtoU_set.set_opacity,
            0,
        )
        # Comentario fnal
        self.play(Write(cfinal))
        self.wait(7)
        self.play(FadeOut(cfinal))


#############################
#### CONJUNTOS CONVEXOS #####
#############################


class ConjuntosConvexos(Scene):
    def construct(self):
        # Título y texto
        titulo = TextMobject("Conjuntos Convexos").scale(1.5)
        pregunta = TextMobject(
            "¿Cuál es la diferencia entre estos dos conjuntos?"
        ).to_edge(UP)

        # Conjunto convexo(izq)

        lao_svg = (
            SVGMobject("Topologia_SVGs/convexo.svg")
            .set_height(FRAME_HEIGHT * 0.4)
            .shift(3 * LEFT)
        )
        lao_svg.set_style(
            fill_opacity=0.7, stroke_width=0, stroke_opacity=1, fill_color=BLUE
        )
        lao_label = TextMobject("A").next_to(lao_svg, DOWN)
        lao = VGroup(lao_svg, lao_label)

        # Conjunto no-convexo(der)

        lau_svg = (
            SVGMobject("Topologia_SVGs/no_convexo.svg")
            .set_height(FRAME_HEIGHT * 0.4)
            .shift(3 * RIGHT)
        )
        lau_svg.set_style(
            fill_opacity=0.5, stroke_width=0, stroke_opacity=1, fill_color=YELLOW
        )
        lau_label = TextMobject("B").next_to(lau_svg, DOWN)
        lau = VGroup(lau_svg, lau_label)

        # "De manera informal"

        casual_1 = TextMobject("De manera informal, podríamos decir que el").to_edge(UP)
        casual_2 = TextMobject("conjunto B tiene una hendidura. ").next_to(
            casual_1, DOWN
        )
        casual = VGroup(casual_1, casual_2)
        formal = TextMobject("Formalicemos lo anterior.").to_edge(DOWN).scale(1.1)

        # Definición segmento de recta

        equis_dot = Dot(point=(-3, 1, 0))
        equis_label = TexMobject(r"\vec{x}").next_to(equis_dot, UP + LEFT)
        equis = VGroup(equis_dot, equis_label)
        ye_dot = Dot(point=(3, -1, 0))
        ye_label = TexMobject(r"\vec{y}").next_to(ye_dot, DOWN + RIGHT)
        ye = VGroup(ye_dot, ye_label)
        segmento_a = TextMobject("Dados dos puntos en $\mathbb{R}^n$,").to_edge(UP)  ##
        segmento_aa = TextMobject("definimos el segmento que los une como:").next_to(
            segmento_a, DOWN
        )
        segmento_b = TexMobject(
            r"[\vec{x},\vec{y}]=\{ (1-t)\vec{x}+t\vec{y}\in \mathbb{R}^n | t\in [0,1]\}"
        )  ###
        segmento_c = TextMobject(
            "Visualizando lo anterior en $\mathbb{R}^2$, tenemos:"
        ).to_edge(UP)
        segmento = Line(start=(-3, 1, 0), end=(3, -1, 0))  ###
        segmento_d = TexMobject(
            r"[\vec{x},\vec{y}]=\{ (1-t)\vec{x}+t\vec{y}\in \mathbb{R}^2 | t\in [0,1]\}"
        ).to_edge(DOWN)

        # Centrado conjunto convexo

        lao_svg_1 = SVGMobject("Topologia_SVGs/convexo.svg").set_height(
            FRAME_HEIGHT * 0.4
        )
        lao_svg_1.set_style(
            fill_opacity=0.7, stroke_width=0, stroke_opacity=1, fill_color=BLUE
        )
        Acomment = (
            TextMobject(
                "Para cualesquiera dos puntos $\\vec{x},\\vec{y} \\in$ A,  tenemos que $[\\vec{x},\\vec{y}]\\subset$ A"
            )
            .to_edge(UP)
            .scale(0.9)
        )
        ## Pares de puntos para A
        par_A1 = VGroup(
            Dot(point=(1, 1, 0)),
            Dot(point=(-1, -1, 0)),
            Line(start=(1, 1, 0), end=(-1, -1, 0)),
        )
        par_A2 = VGroup(
            Dot(point=(0, 1, 0)),
            Dot(point=(0, -1, 0)),
            Line(start=(0, 1, 0), end=(0, -1, 0)),
        )
        par_A3 = VGroup(
            Dot(point=(-0.7, 1.1, 0)),
            Dot(point=(0.5, -1.1, 0)),
            Line(start=(-0.7, 1.1, 0), end=(0.5, -1.1, 0)),
        )
        convexo = (
            TextMobject("A esto se le conoce como un", " conjunto convexo.")
            .to_edge(DOWN)
            .scale(0.9)
        )
        convexo[1].set_color(BLUE)  ##

        # Centrado conjunto no convexo

        lau_svg_1 = SVGMobject("Topologia_SVGs/no_convexo.svg").set_height(
            FRAME_HEIGHT * 0.4
        )
        lau_svg_1.set_style(
            fill_opacity=0.5, stroke_width=0, stroke_opacity=1, fill_color=YELLOW
        )
        Bcomment_a = TextMobject("Esto no sucede para el conjunto B, pues").to_edge(UP)
        Bcomment_b = TextMobject(
            "existen $\\vec{x},\\vec{y}\\subset$ B tales que $[\\vec{x},\\vec{y}]\\not\\subseteq$ B"
        ).next_to(Bcomment_a, DOWN)
        Bcomment = VGroup(Bcomment_a, Bcomment_b).scale(0.9)
        ##Pares de puntos para B
        par_B1 = VGroup(
            Dot(point=(-0.5, 1, 0)),
            Dot(point=(-0.5, -1, 0)),
            Line(start=(-0.5, 1, 0), end=(-0.5, -1, 0)),
        )
        par_B2 = VGroup(
            Dot(point=(-0.2, -1, 0)),
            Dot(point=(0.7, -1, 0)),
            Line(start=(-0.2, -1, 0), end=(0.7, -1, 0)),
        )
        par_B3 = VGroup(
            Dot(point=(-0.8, 1, 0)),
            Dot(point=(0.8, 1, 0)),
            Line(start=(-0.8, 1, 0), end=(0.8, 1, 0)),
        ).set_color(RED)
        no_convexo = (
            TextMobject("Este conjunto es", " no convexo.").to_edge(DOWN).scale(0.9)
        )
        no_convexo[1].set_color(YELLOW)

        entonces = TextMobject("Entonces, de manera formal:").to_edge(UP)
        lao_conv = TextMobject("Convexo").next_to(lao_label, 2 * DOWN).set_color(BLUE)
        lau_nconv = (
            TextMobject("No convexo").next_to(lau_label, 2 * DOWN).set_color(YELLOW)
        )

        # pregunta

        pregunta1 = TextMobject("Ahora es tu turno: ")
        pregunta2 = TextMobject(
            "Si un conjunto es convexo, ¿también es conexo?"
        ).next_to(pregunta1, DOWN)

        # Secuencia de la animación
        self.play(Write(titulo))
        self.wait()
        self.play(FadeOut(titulo))
        self.play(Write(pregunta, run_time=2))
        self.wait()
        self.play(Write(lao), Write(lau))
        self.wait()
        self.play(FadeOut(pregunta))
        self.play(Write(casual, run_time=5))  #
        self.wait(2)
        self.play(Write(formal))
        self.wait(1)
        self.play(FadeOut(casual), FadeOut(formal), FadeOut(lao), FadeOut(lau))
        # Animación definición
        self.play(Write(segmento_a))
        self.play(Write(segmento_aa, run_time=2))
        self.wait()
        self.play(Write(segmento_b, run_time=3))
        self.wait(3)
        self.play(FadeOut(segmento_aa))
        self.play(ReplacementTransform(segmento_a, segmento_c))
        self.play(ReplacementTransform(segmento_b, segmento_d))
        self.play(Write(equis), Write(ye))
        self.play(Write(segmento))
        self.wait(3)
        self.play(
            FadeOut(equis),
            FadeOut(ye),
            FadeOut(segmento),
            FadeOut(segmento_c),
            FadeOut(segmento_d),
        )
        # Animación conjunto convexo
        self.play(Write(lao_svg_1))
        self.play(Write(Acomment, run_time=3))
        self.bring_to_back(lao_svg_1)
        self.play(ShowCreation(par_A1))
        self.wait(1.2)
        self.play(ReplacementTransform(par_A1, par_A2))
        self.wait(1.2)
        self.play(ReplacementTransform(par_A2, par_A3))
        self.wait(1.2)
        self.play(Write(convexo))
        self.wait()
        self.play(
            FadeOut(Acomment), FadeOut(convexo), FadeOut(lao_svg_1), FadeOut(par_A3)
        )
        # Animación conjunto NO convexo
        self.play(Write(lau_svg_1))
        self.play(Write(Bcomment, run_time=3))
        self.bring_to_back(lau_svg_1)
        self.wait()
        self.play(ShowCreation(par_B1))
        self.wait(1.2)
        self.play(ReplacementTransform(par_B1, par_B2))
        self.wait(1.2)
        self.play(ReplacementTransform(par_B2, par_B3))
        self.play(par_B3.scale, 1.4)
        self.play(par_B3.scale, 1 / 1.4)
        self.wait()
        self.play(Write(no_convexo))
        self.wait()
        self.play(
            FadeOut(Bcomment), FadeOut(no_convexo), FadeOut(lau_svg_1), FadeOut(par_B3)
        )
        # Animación conclusión
        self.play(Write(entonces))
        self.play(Write(lao), Write(lau))
        self.play(Write(lao_conv))
        self.play(Write(lau_nconv))
        self.wait(2)
        self.play(
            FadeOut(entonces),
            FadeOut(lao),
            FadeOut(lau),
            FadeOut(lao_conv),
            FadeOut(lau_nconv),
        )
        self.wait()
        self.play(Write(pregunta1))
        self.play(Write(pregunta2))
        self.wait(6)
        self.play(FadeOut(pregunta1),FadeOut(pregunta2))


class ScreenGrid(VGroup):
    CONFIG = {
        "rows": 8,
        "columns": 14,
        "height": FRAME_Y_RADIUS * 2,
        "width": 14,
        "grid_stroke": 0.5,
        "grid_color": WHITE,
        "axis_color": RED,
        "axis_stroke": 2,
        "labels_scale": 0.25,
        "labels_buff": 0,
        "number_decimals": 2,
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        rows = self.rows
        columns = self.columns
        grid = Grid(width=self.width, height=self.height, rows=rows, columns=columns)
        grid.set_stroke(self.grid_color, self.grid_stroke)

        vector_ii = ORIGIN + np.array((-self.width / 2, -self.height / 2, 0))
        vector_si = ORIGIN + np.array((-self.width / 2, self.height / 2, 0))
        vector_sd = ORIGIN + np.array((self.width / 2, self.height / 2, 0))

        axes_x = Line(LEFT * self.width / 2, RIGHT * self.width / 2)
        axes_y = Line(DOWN * self.height / 2, UP * self.height / 2)

        axes = VGroup(axes_x, axes_y).set_stroke(self.axis_color, self.axis_stroke)

        divisions_x = self.width / columns
        divisions_y = self.height / rows

        directions_buff_x = [UP, DOWN]
        directions_buff_y = [RIGHT, LEFT]
        dd_buff = [directions_buff_x, directions_buff_y]
        vectors_init_x = [vector_ii, vector_si]
        vectors_init_y = [vector_si, vector_sd]
        vectors_init = [vectors_init_x, vectors_init_y]
        divisions = [divisions_x, divisions_y]
        orientations = [RIGHT, DOWN]
        labels = VGroup()
        set_changes = zip(
            [columns, rows], divisions, orientations, [0, 1], vectors_init, dd_buff
        )
        for c_and_r, division, orientation, coord, vi_c, d_buff in set_changes:
            for i in range(1, c_and_r):
                for v_i, directions_buff in zip(vi_c, d_buff):
                    ubication = v_i + orientation * division * i
                    coord_point = round(ubication[coord], self.number_decimals)
                    label = Text(f"{coord_point}", font="Arial", stroke_width=0).scale(
                        self.labels_scale
                    )
                    label.next_to(ubication, directions_buff, buff=self.labels_buff)
                    labels.add(label)

        self.add(grid, axes, labels)


###################################
#### PUNTOS AISLADOS/ACUMULACION #####
###################################


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


########################
#### CUBIERTAS     #####
########################


class Cubierta(Scene):
    def construct(self):
        title = TextMobject("""Cubiertas""").scale(1.5)

        grid = ScreenGrid()

        ###Texto
        t_1 = TextMobject("Sea ", "$A$", " $\\subset \\mathbb{R}^n$")
        t_1.set_color_by_tex_to_color_map({"$A$": BLUE})
        t_2 = TextMobject("Definimos una", " cubierta", " de ", "$A$")
        t_2.set_color_by_tex_to_color_map({"cubierta": PURPLE_B, "$A$": BLUE})

        t_3_1 = TextMobject(
            "como una colección de",
            " subconjuntos ",
            "$\\mathcal{F}$",
            " $\\subset \\mathcal{P}(\\mathbb{R}^n)$,",
        )
        t_3_1.set_color_by_tex_to_color_map(
            {"subconjuntos": GREEN_D, "$\\mathcal{F}": PURPLE_B}
        )
        t_3_2 = TextMobject("donde $\\mathcal{P}(\\mathbb{R}^n)$ es el conjunto potencia de $\\mathbb{R}^n$").move_to(1*DOWN)
        t_3 = VGroup(t_3_1,t_3_2)

        t_4 = TextMobject(
            "tal que ", "$A$", " $\\subseteq \\bigcup_{U \\subset \\mathcal{F}} U$, con $U\\subset\\mathbb{R}^n$"
        )
        t_4.set_color_by_tex_to_color_map({"$A$": BLUE})
        t_4[2][4].set_color(PURPLE_B)

        t_5 = TextMobject(
            "Por ejemplo, sea ", "$A$", "  el siguiente", " conjunto:"
        ).move_to(3 * UP)
        t_5.set_color_by_tex_to_color_map({"conjunto": BLUE, "$A$": BLUE})

        t_6 = TextMobject(
            "Entonces una posible", " cubierta $\\mathcal{F}$", " podría ser: "
        ).move_to(3 * UP)
        t_6.set_color_by_tex_to_color_map({"cubierta $\\mathcal{F}$": PURPLE_B})

        t_7 = TextMobject(
            "Una", " cubierta", " puede ser", " abierta", " o", " cerrada"
        ).move_to(3 * UP)
        t_7.set_color_by_tex_to_color_map(
            {"cubierta": PURPLE_B, "abierta": RED, "cerrada": ORANGE}
        )
        t_8 = TextMobject(
            "dependiendo de si los", " subconjuntos $U_{i}$", " que la componen"
        ).move_to(3 * UP)
        t_8.set_color_by_tex_to_color_map({"subconjuntos $U_{i}$": GREEN_D})

        t_9 = TextMobject("son todos", " abiertos").move_to(3 * UP)
        t_9.set_color_by_tex_to_color_map({"abiertos": RED})

        t_10 = TextMobject("o todos", " cerrados").move_to(3 * UP)
        t_10.set_color_by_tex_to_color_map({"cerrados": ORANGE})

        t_11 = TextMobject(
            "Observemos que en este caso los ",
            "subconjuntos $U_{i}$",
            "\\\\ se sobreponen",
        ).move_to(3 * UP)
        t_11.set_color_by_tex_to_color_map({"subconjuntos $U_{i}$": GREEN_D})

        t_12 = TextMobject(
            "por lo que el", " conjunto $A$", " queda totalmente cubierto"
        ).move_to(3 * UP)
        t_12.set_color_by_tex_to_color_map({"conjunto $A$": BLUE})

        t_13 = TextMobject(
            "independientemente de que ",
            "$\\mathcal{F}$",
            " sea",
            " abierta",
            " o",
            " cerrada",
        ).move_to(3 * UP)
        t_13.set_color_by_tex_to_color_map(
            {"abierta": RED, "cerrada": ORANGE, "$\\mathcal{F}$": PURPLE_B}
        )

        t_14 = TextMobject(
            "Si ", "A", " es ", "cerrado"," y $diam(U_i)<diam(A)$,"
        ).move_to(3 * UP)
        t_14[1].set_color(BLUE)
        t_14[3].set_color(ORANGE)
        t_15_1 = TextMobject("¿existe ", "cubierta ", "abierta de ", "A",", donde").move_to(3*UP)
        t_15_2 = TextMobject("los elementos ", "$U_i$",  " \\textbf{no} se intersecten?").next_to(t_15_1,DOWN)
        t_15_1[1].set_color(PURPLE_B)
        t_15_1[3].set_color(BLUE)
        t_15_2[1].set_color(GREEN_D)
        t_15=VGroup(t_15_1,t_15_2)
        ###Conjunto y cubiertas
        Conjunto_Cubierto = SVGMobject("Topologia_SVGs/Cubierta.svg").scale(2)
        A = Conjunto_Cubierto[0].set_color(BLUE).next_to(t_5, 7 * DOWN)
        cover_1 = Conjunto_Cubierto[1:6].next_to(t_6, 4 * DOWN)
        index = VGroup()
        colors = it.cycle([YELLOW, GREEN_D, PURPLE_B, PINK, RED, TEAL])
        for i in range(len(cover_1)):
            text = TextMobject("$U_{%d}$" % (i + 1))
            color = next(colors)
            cover_1[i].set_fill(color, opacity=0.4).set_stroke(color, 0.5)
            text.move_to(cover_1[i])
            index.add(text)
        cover_2 = Conjunto_Cubierto[6:11].next_to(t_12, 4 * DOWN)
        for i in range(len(cover_2)):
            color = next(colors)
            cover_2[i].set_fill(color, opacity=0.4).set_stroke(color, 0.5)

        ###Grupos
        Group_1 = VGroup(t_5, A)
        Group_2 = VGroup(t_6, A)
        Group_3 = VGroup(cover_1, index)
        Group_4 = VGroup(t_15, cover_2, A)

        # Secuencia de la animación
        self.play(Write(title))
        self.wait()
        self.play(ReplacementTransform(title, t_1))
        self.wait(2)
        self.play(ReplacementTransform(t_1, t_2))
        self.wait(2)
        self.play(ReplacementTransform(t_2, t_3))
        self.wait(6)
        self.play(ReplacementTransform(t_3, t_4))
        self.wait(11)
        self.play(ReplacementTransform(t_4, Group_1))
        self.wait(5)
        self.play(ReplacementTransform(Group_1, Group_2))
        self.wait(5)
        self.play(FadeIn(Group_3))
        self.wait(2.5)
        self.play(ReplacementTransform(t_6, t_7))
        self.wait(5)
        self.play(ReplacementTransform(t_7, t_8))
        self.wait(5)
        self.play(ReplacementTransform(t_8, t_9))
        self.wait(2)
        self.play(ReplacementTransform(t_9, t_10))
        self.remove(Group_3).add(cover_1.set_stroke(WHITE, 3))
        self.wait(2)
        self.play(ReplacementTransform(t_10, t_11))
        self.wait(6)
        self.play(ReplacementTransform(t_11, t_12))
        self.wait(5)
        self.play(ReplacementTransform(t_12, t_13))
        self.wait(5)
        self.play(ReplacementTransform(t_13, t_14))
        self.play(ReplacementTransform(cover_1.set_stroke(WHITE, 3), cover_2))
        self.wait(8)
        self.play(ReplacementTransform(t_14, t_15))
        self.wait(7)
        self.play(FadeOut(Group_4))


#########################
######## Bolas ##########
#########################


class Bolas(Scene):
    def construct(self):
        grid = NumberPlane()
        titulo = TextMobject("Bolas o Vecindades")
        titulo.scale(1.5)
        text1 = TextMobject("Tomemos un punto en el espacio, $\\vec{x}_0$")
        text1.move_to((0, 3, 0))
        text2 = TextMobject("Y un radio ", "r ", "> 0")
        text2[1].set_color(TEAL)
        text2.move_to(text1)
        text_3_1=TextMobject("Podemos seleccionar los puntos que se encuentran")
        text_3_2=TextMobject("a una distancia menor a ", "r", " de $\\vec{x}_0$").next_to(text_3_1,DOWN)
        text_3_2[1].set_color(TEAL)
        text3=VGroup(text_3_1,text_3_2)
        text3.move_to(text1)
        text4 = TextMobject("""Esto es conocido como una bola o vecindad""")
        text4.move_to(text1)
        text5 = TextMobject("De manera formal, definimos bola o vecindad como:")
        text6 = TexMobject(
            "B_r(\\vec{x}_0) :=\\lbrace \\vec{x} \\  | \\ d(\\vec{x},\\vec{x}_0)=\\norm{\\vec{x}-\\vec{x}_0}<r \\rbrace"
        )
        text5.move_to(text6.get_center() + UP)
        text7 = TextMobject(
            """Notemos que, por lo anterior, la bola depende de la \n
                           métrica o norma definida en el espacio"""
        )
        text8 = TextMobject(
            """ \\textquestiondown Puedes imaginar c\\'{o}mo se ver\\'{i}a una bola \n
                            con otras normas, por ejemplo con la norma \n
                             infinito o la norma 1?"""
        )

        text1.bg = SurroundingRectangle(
            text1, color=YELLOW_E, fill_color=BLACK, fill_opacity=1
        )
        Group11 = VGroup(text1.bg, text1)

        text2.bg = SurroundingRectangle(
            text2, color=YELLOW_E, fill_color=BLACK, fill_opacity=1
        )
        Group12 = VGroup(text2.bg, text2)

        text3.bg = SurroundingRectangle(
            text3, color=YELLOW_E, fill_color=BLACK, fill_opacity=1
        )
        Group13 = VGroup(text3.bg, text3)

        text4.bg = SurroundingRectangle(
            text4, color=YELLOW_E, fill_color=BLACK, fill_opacity=1
        )
        Group14 = VGroup(text4.bg, text4)

        r = 2  # Se puede modificar para cambiar el radio de la bola
        x0 = np.array(
            [0, 0, 0]
        )  # Se  puede modificar para cambiar el centro de la bola

        punto = Dot()
        punto.scale(1.14)
        punto.set_color(YELLOW)
        puntolabel = TextMobject("$$\\vec{x}_0$$")
        puntolabel.scale(1.15)
        punto.move_to(x0)
        puntolabel.set_color(YELLOW_B)
        puntolabel.move_to((0.39, 0.39, 0))

        bola = Dot(radius=r, fill_color=YELLOW_D, fill_opacity=0.6)
        linea_r = Line((0,0,0),(2,0,0)).set_color(TEAL)
        label_r = TextMobject("r").move_to(0.75*RIGHT+0.25*DOWN).set_color(TEAL)
        Bola_1 = VGroup(bola,linea_r,label_r)
        


        # animación

        self.play(Write(titulo))
        self.wait(2)
        self.play(FadeOut(titulo))
        self.play(Write(grid))
        self.play(Write(Group11))
        self.play(FadeIn(punto), FadeIn(puntolabel))
        self.wait(3.2)
        self.play(ReplacementTransform(Group11, Group12))
        self.wait(5)
        self.play(ReplacementTransform(Group12, Group13))
        self.wait(6)
        self.play(FadeIn(Bola_1))
        self.wait()
        self.play(ReplacementTransform(Group13, Group14), FadeOut(puntolabel))
        self.wait(4.5)
        self.play(FadeOut(Bola_1), FadeOut(grid), FadeOut(Group14), FadeOut(punto))
        self.wait()
        self.play(Write(text5))
        self.play(Write(text6))
        self.wait(2)
        self.play(FadeOut(text5), FadeOut(text6))
        self.play(Write(text7))
        self.wait(5.5)
        self.play(ReplacementTransform(text7, text8))
        self.wait(10)
        self.play(FadeOut(text8))


#######################
### Tipos de puntos ###
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


#######################
### Num Lebesgue ######
#######################


class NumLebesgue(Scene):
    def construct(self):
        grid = NumberPlane()
        ###Texto
        titulo = TextMobject("""Lema del N\\'{u}mero de Lebesgue""")
        titulo.scale(1.2)
        t_1 = TextMobject("""Sea $X \\subset \\mathbb{R}^{n}$ compacto""").move_to(
            3 * UP
        )
        t_2 = TextMobject("y $\\mathcal{F}$ una cubierta abierta de $X$").move_to(
            3 * UP
        )
        t_3 = TextMobject("$\\implies \\exists$ $\\epsilon > 0$").move_to(3 * UP)
        t_4 = TextMobject("tal que $\\forall$ $x \in X$").move_to(3 * UP)
        t_5 = TextMobject("$\\exists$ $U \\in \\mathcal{F}$").move_to(3 * UP)
        t_6 = TextMobject("tal que $B(x, \\epsilon) \\subseteq U$").move_to(3 * UP)
        t_7 = TextMobject(" \\textquestiondown Puedes probarlo formalmente?")

        ###Dibujos

        Conjunto_Cubierto = SVGMobject("Topologia_SVGs/Lebesgue.svg").scale(2)
        X = Conjunto_Cubierto[0].set_color(GREEN).next_to(t_1, 5 * DOWN)
        cover = Conjunto_Cubierto[1:7].next_to(t_2, 2 * DOWN)
        colors = it.cycle([YELLOW, RED, PURPLE, PINK, BLUE, TEAL, WHITE])
        for i in range(len(cover)):
            color = next(colors)
            cover[i].set_fill(color, opacity=0.4).set_stroke(color, 0.5)
        line = Line(np.array([1, 0, 0]), np.array([1.27, 0, 0])).move_to((1, -0.8, 0))
        brace = Brace(line, UP)
        epsilon = TextMobject("$\\epsilon$").next_to(brace, UP)
        dot = Dot((0, 0, 0), color=WHITE, radius=0.05).move_to(line, LEFT)
        x = TextMobject("$x_1$").next_to(dot, LEFT)
        U1 = TextMobject("$U_1$").next_to(cover[5], RIGHT)
        U3 = TextMobject("$U_2$").next_to(cover[1], LEFT)
        U4 = TextMobject("$U_3$").next_to(cover[0], LEFT)
        U5 = TextMobject("$U_4$").next_to(cover[4], RIGHT)
        circle = Circle(
            radius=0.2, fill_color=RED, color=RED, fill_opacity=0.8
        ).move_to(dot)

        line3 = Line(np.array([1, 0, 0]), np.array([1.27, 0, 0])).move_to(
            (-0.85, -0.75, 0)
        )
        dot3 = Dot((0, 0, 0), color=WHITE, radius=0.05).move_to(line3, LEFT)
        x3 = TextMobject("$x_2$").next_to(dot3, LEFT)
        circle3 = Circle(
            radius=0.2, fill_color=RED, color=RED, fill_opacity=0.8
        ).move_to(dot3)

        line4 = Line(np.array([1, 0, 0]), np.array([1.27, 0, 0])).move_to((-1.7, 1, 0))
        dot4 = Dot((0, 0, 0), color=WHITE, radius=0.05).move_to(line4, LEFT)
        x4 = TextMobject("$x_3$").next_to(dot4, DOWN)
        circle4 = Circle(
            radius=0.2, fill_color=RED, color=RED, fill_opacity=0.8
        ).move_to(dot4)

        line5 = Line(np.array([1, 0, 0]), np.array([1.27, 0, 0])).move_to(
            (-0.55, 1.2, 0)
        )
        dot5 = Dot((0, 0, 0), color=WHITE, radius=0.05).move_to(line5, LEFT)
        x5 = TextMobject("$x_4$").next_to(dot5, UP)
        circle5 = Circle(
            radius=0.2, fill_color=RED, color=RED, fill_opacity=0.8
        ).move_to(dot5)

        ###Grupos
        Group_1 = VGroup(t_1, X)
        Group_2 = VGroup(line, brace, epsilon)
        Group_3 = VGroup(dot, dot3, dot4, dot5, x, x3, x4, x5)
        Group_4 = VGroup(line, brace, epsilon, dot, dot3, dot4, dot5, x, x3, x4, x5)
        Group_5 = VGroup(
            line,
            line3,
            line4,
            line5,
            brace,
            epsilon,
            dot,
            dot3,
            dot4,
            dot5,
            x,
            x3,
            x4,
            x5,
            cover,
            X,
            t_6,
            circle,
            circle3,
            circle4,
            circle5,
            U1,
            U3,
            U4,
            U5,
        )
        Group_6 = VGroup(x, x3, x4, x5)
        Group_7 = VGroup(line3, line4, line5)

        # animación
        self.play(Write(titulo))
        self.wait(2)
        self.play(ReplacementTransform(titulo, Group_1))
        self.wait(4)
        self.play(ReplacementTransform(t_1, t_2))
        self.play(FadeIn(cover))
        self.wait(2)
        self.play(ReplacementTransform(t_2, t_3))
        self.play(FadeIn(Group_2))
        self.play(FadeOut(brace))
        self.play(FadeOut(epsilon))
        self.add(Group_3)
        self.play(ReplacementTransform(t_3, t_4))
        self.play(FadeIn(Group_7))
        self.wait(2.2)
        self.play(FadeOut(Group_6))
        self.play(ReplacementTransform(t_4, t_5))
        self.play(DrawBorderThenFill(cover[5].set_stroke(WHITE, 1)))
        self.add(U1)
        self.play(DrawBorderThenFill(cover[1].set_stroke(WHITE, 1)))
        self.add(U3)
        self.play(DrawBorderThenFill(cover[0].set_stroke(WHITE, 1)))
        self.add(U4)
        self.play(DrawBorderThenFill(cover[4].set_stroke(WHITE, 1)))
        self.add(U5)
        self.wait(3)
        self.play(ReplacementTransform(t_5, t_6))
        self.play(DrawBorderThenFill(circle))
        self.play(DrawBorderThenFill(circle3))
        self.play(DrawBorderThenFill(circle4))
        self.play(DrawBorderThenFill(circle5))
        self.play(FadeIn(Group_4))
        self.wait(4)
        self.wait(4)
        self.play(ReplacementTransform(Group_5, t_7))
        self.wait(3)
        self.play(FadeOut(t_7))

    class Grid(VGroup):
        CONFIG = {
            "height": 6.0,
            "width": 6.0,
        }

        def __init__(self, rows, columns, **kwargs):
            digest_config(self, kwargs, locals())
            super().__init__(**kwargs)

            x_step = self.width / self.columns
            y_step = self.height / self.rows

            for x in np.arange(0, self.width + x_step, x_step):
                self.add(
                    Line(
                        [x - self.width / 2.0, -self.height / 2.0, 0],
                        [x - self.width / 2.0, self.height / 2.0, 0],
                    )
                )
            for y in np.arange(0, self.height + y_step, y_step):
                self.add(
                    Line(
                        [-self.width / 2.0, y - self.height / 2.0, 0],
                        [self.width / 2.0, y - self.height / 2.0, 0],
                    )
                )


class ScreenGrid(VGroup):
    CONFIG = {
        "rows": 8,
        "columns": 14,
        "height": FRAME_Y_RADIUS * 2,
        "width": 14,
        "grid_stroke": 0.5,
        "grid_color": WHITE,
        "axis_color": RED,
        "axis_stroke": 2,
        "labels_scale": 0.25,
        "labels_buff": 0,
        "number_decimals": 2,
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        rows = self.rows
        columns = self.columns
        grid = Grid(width=self.width, height=self.height, rows=rows, columns=columns)
        grid.set_stroke(self.grid_color, self.grid_stroke)

        vector_ii = ORIGIN + np.array((-self.width / 2, -self.height / 2, 0))
        vector_si = ORIGIN + np.array((-self.width / 2, self.height / 2, 0))
        vector_sd = ORIGIN + np.array((self.width / 2, self.height / 2, 0))

        axes_x = Line(LEFT * self.width / 2, RIGHT * self.width / 2)
        axes_y = Line(DOWN * self.height / 2, UP * self.height / 2)

        axes = VGroup(axes_x, axes_y).set_stroke(self.axis_color, self.axis_stroke)

        divisions_x = self.width / columns
        divisions_y = self.height / rows

        directions_buff_x = [UP, DOWN]
        directions_buff_y = [RIGHT, LEFT]
        dd_buff = [directions_buff_x, directions_buff_y]
        vectors_init_x = [vector_ii, vector_si]
        vectors_init_y = [vector_si, vector_sd]
        vectors_init = [vectors_init_x, vectors_init_y]
        divisions = [divisions_x, divisions_y]
        orientations = [RIGHT, DOWN]
        labels = VGroup()
        set_changes = zip(
            [columns, rows], divisions, orientations, [0, 1], vectors_init, dd_buff
        )
        for c_and_r, division, orientation, coord, vi_c, d_buff in set_changes:
            for i in range(1, c_and_r):
                for v_i, directions_buff in zip(vi_c, d_buff):
                    ubication = v_i + orientation * division * i
                    coord_point = round(ubication[coord], self.number_decimals)
                    label = Text(f"{coord_point}", font="Arial", stroke_width=0).scale(
                        self.labels_scale
                    )
                    label.next_to(ubication, directions_buff, buff=self.labels_buff)
                    labels.add(label)

        self.add(grid, axes, labels)


#########################
#### CERRADURA #####
#########################


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

    # 2 in construct
    # 3 uno de los dispositivos conectados al sistema no funciona ----meter chcp 1252/chcp 65001
    # del 3 quite los math-algo y nada
    # acentos y ? debi quitar
