from manimlib.imports import *

#############################
#### CONJUNTOS ABIERTOS #####
#############################


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