from manimlib.imports import *

############################
### NÚMERO DE LEBESGE ######
############################


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