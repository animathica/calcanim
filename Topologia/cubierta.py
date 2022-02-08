from manimlib.imports import *

#################################
#### CUBIERTA DE UN CONJUNTO ####
#################################


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