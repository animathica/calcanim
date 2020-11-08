from manimlib.imports import *

#########################
######## Bolas ##########
#########################

class Bolas(Scene):
    def construct(self):
        grid = NumberPlane()
        titulo = TextMobject("Bolas o Vecindades")
        titulo.scale(1.5)
        text1 = TextMobject("Tomemos un punto en el espacio $\\vec{x}_0$")
        text1.move_to((0, 3, 0))
        text2 = TextMobject("Y un radio r>0")
        text2.move_to(text1)
        text3 = TextMobject(
            """Podemos seleccionar los puntos que se encuentran\n
                                a una distancia menor a r de $\\vec{x}_0$"""
        )
        text3.move_to(text1)
        text4 = TextMobject("""Esto es conocido como una bola o vecindad""")
        text4.move_to(text1)
        text5 = TextMobject("De manera formal, definimos bola o vecindad como:")
        text6 = TexMobject(
            "B_r(\\vec{x}_0) :=\\lbrace \\vec{x} \\  | \\ d(\\vec{x},\\vec{x}_0)=\\norm{\\vec{x}-\\vec{x}_0}<r \\rbrace"
        )
        text5.move_to(text6.get_center() + UP)
        text7 = TextMobject(
            """Notemos que, por lo anterior, la bola depende de la norma \n
                            o distancia definida en el espacio"""
        )
        text8 = TextMobject(
            """ \\textquestiondown Puedes imaginar c\\'{o}mo se ver\\'{i}a una bola \n
                            con otras normas, por ejemplo con la norma \n
                             infinito o la distancia 1?"""
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
        puntolabel.set_color(YELLOW_E)
        puntolabel.move_to((0.39, 0.39, 0))

        bola = Circle(radius=r, fill_color=YELLOW_D, color=YELLOW_E, fill_opacity=0.6)

        # animación

        self.play(Write(titulo))
        self.wait(2)
        self.play(FadeOut(titulo))
        self.play(Write(grid))
        self.play(Write(Group11))
        self.play(FadeIn(punto), FadeIn(puntolabel))
        self.wait(3.2)
        self.play(ReplacementTransform(Group11, Group12))
        self.wait(2.5)
        self.play(ReplacementTransform(Group12, Group13))
        self.wait(6)
        self.play(FadeIn(bola))
        self.wait()
        self.play(ReplacementTransform(Group13, Group14), FadeOut(puntolabel))
        self.wait(4.5)
        self.play(FadeOut(bola), FadeOut(grid), FadeOut(Group14), FadeOut(punto))
        self.wait()
        self.play(Write(text5))
        self.play(Write(text6))
        self.wait(2)
        self.play(FadeOut(text5), FadeOut(text6))
        self.play(Write(text7))
        self.wait(5.5)
        self.play(ReplacementTransform(text7, text8))
        self.wait(7)
        self.play(FadeOut(text8))