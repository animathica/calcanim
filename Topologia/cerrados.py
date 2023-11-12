from manimlib.imports import *

#############################
#### CONJUNTOS CERRADOS #####
#############################


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