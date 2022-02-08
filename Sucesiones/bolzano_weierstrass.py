from manimlib.imports import *

#########################################
#### TEOREMA DE BOLZANO WEIERSTRASS #####
#########################################

#Definimos un Dot con métodos específicos para la escena de BolzanoWeierstrass
class CCustomDot(Dot):
    def custom_method(self, color):
        self.set_color(color)
        self.scale(5)
        return self

    def other_method(self):
        self.scale(1 / 5)
        return self

    def small_method(self, color):
        self.set_color(color)
        self.scale(1.5)
        return self

class BolzanoWeierstrass(Scene):
    def construct(self):
        titulo = TextMobject("El Teorema de Bolzano-Weierstrass").scale(1.5)
        teorema_1 = TexMobject(r"\text{Toda sucesi\'{o}n}\ ", r"\text{acotada}\ ", r"\text{en}\  \mathbb{R}^n")
        teorema_2 = TextMobject(r"\text{tiene una}", r" subsucesi\'{o}n convergente.").next_to(teorema_1, DOWN)
        teorema = VGroup(teorema_1, teorema_2)
        teorema_1[1].set_color(YELLOW)
        teorema_2[1].set_color(RED)
        plano = NumberPlane()

        suc_acot = TexMobject(r"\text{Sea}\ \{\vec{x}_n\}\ \text{una sucesi\'{o}n}\ ", r"\text{acotada}",
                              r"\text{ por M}").to_edge(UP)
        suc_acot[1].set_color(YELLOW)
        suc_acot.bg = SurroundingRectangle(suc_acot, color=WHITE, fill_color=BLACK, fill_opacity=1)
        group_acot = VGroup(suc_acot.bg, suc_acot)  #####imp

        # Construyendo una subsucesi'{o}n acotada: "Infinidad" de puntos
        points_infinite_values = []
        for n in range(3, 1500):
            points_infinite_values.append(CCustomDot(
                point=np.array([np.sqrt(2) * np.power(-1, n) * (n) / (n + 3), np.sqrt(2) * (n) / (n + 3), 0.0]),
                color=GREY).scale(0.7))
        group2 = VGroup(*points_infinite_values)

        # C'{i}rculo y "emes"
        circulo = Circle(radius=np.sqrt(np.power(np.sqrt(2), 2) + np.power(np.sqrt(2), 2))).set_color(YELLOW)
        M_der = TexMobject("M").scale(0.75).move_to((2.4, 0, 0))
        M_izq = TexMobject("-M").scale(0.75).move_to((-2.4, 0, 0))
        M_arb = TexMobject("M").scale(0.75).move_to((0, 2.2, 0))
        M_abj = TexMobject("-M").scale(0.75).move_to((0, -2.2, 0))
        emes = VGroup(M_der, M_izq, M_arb, M_abj)
        # Rect'{a}ngulo R1
        el_rect = TextMobject(r"\text{Acotemos la sucesi\'{o}n con un rect\'{a}ngulo de lado 2M:} ",
                              r"\text{$R$}").to_edge(UP).scale(0.8)
        el_rect[1].set_color(YELLOW)
        R = Rectangle(height=2 * np.sqrt(np.power(np.sqrt(2), 2) + np.power(np.sqrt(2), 2)),
                      width=2 * np.sqrt(np.power(np.sqrt(2), 2) + np.power(np.sqrt(2), 2))).set_color(YELLOW)

        # Rect'{a}ngulo R2
        subrect_1a = TextMobject(r"\text{Tomemos un subrect\'{a}ngulo con una cantidad infinita}").to_edge(UP)
        subrect_1b = TexMobject(r"\text{de t\'{e}rminos de la sucesi\'{o}n: } ", r"\text{$R_1$}").next_to(subrect_1a,
                                                                                                         DOWN)
        subrect_1b[1].set_color(ORANGE)
        cuadrante_dR1 = TexMobject(r"\text{Notemos que}\ ", r"R_1\ ", r"\text{es un cuadrante de}\ ", r"R").to_edge(
            DOWN)
        cuadrante_dR1[1].set_color(ORANGE)
        cuadrante_dR1[3].set_color(YELLOW)
        subrect_1 = VGroup(subrect_1a, subrect_1b).scale(0.8)
        R1 = Rectangle(height=2, width=2).move_to((1, 1, 0)).set_color(ORANGE)

        # Rect'{a}ngulo R3
        subrect_2a = TextMobject(r"\text{Nuevamente tomemos un subrect\'{a}ngulo que sea un cuadrante del}").to_edge(
            UP).scale(0.8)
        subrect_2b = TextMobject(r"\text{anterior con infinitos t\'{e}rminos de la sucesi\'{o}n:} ",
                                 r"\text{$R_2$}").next_to(subrect_2a, DOWN).scale(0.8)
        subrect_2b[1].set_color(GREEN)
        subrect_2 = VGroup(subrect_2a, subrect_2b)
        R2 = Rectangle(height=1, width=1).move_to((1.5, 1.5, 0)).set_color(GREEN)

        # Rect'{a}ngulos siguientes
        subrects_a = TextMobject(r"\text{Repetimos infinitas veces, siempre tomando un subrect\'{a}ngulo}").to_edge(
            UP).scale(0.8)
        subrects_b = TextMobject(r"\text{con una cantidad infinita de t\'{e}rminos de la sucesi\'{o}n}").next_to(
            subrects_a, DOWN).scale(0.8)
        subrects = VGroup(subrects_a, subrects_b)

        R3 = Rectangle(height=0.5, width=0.5).move_to((1.25, 1.25, 0)).set_color(BLUE)
        R4 = Rectangle(height=0.25, width=0.25).move_to((1.375, 1.375, 0)).set_color(PURPLE)
        R5 = Rectangle(height=0.125, width=0.125).move_to((1.4375, 1.4375, 0)).set_color(PINK)
        R6 = Rectangle(height=0.0625, width=0.0625).move_to((1.46875, 1.46875, 0)).set_color(TEAL)

        Rects = VGroup(R, R1, R2, R3, R4, R5, R6)

        # Observaciones acerca de los rect'{a}ngulos
        notas_rect_0 = TextMobject(r"\text{Tenemos una sucesi\'{o}n de rect\'{a}ngulos anidados que cumplen:}").to_edge(
            UP).scale(0.8)
        notas_rect_1 = TexMobject(r"1)\ R_{k+1} \subset R_{k}").next_to(notas_rect_0, 5 * DOWN).shift(2 * RIGHT).scale(
            0.8)
        notas_rect_2 = TexMobject(r"2)\ diag(R_{k})= \frac{\sqrt{2}M}{2^{k-1}}").next_to(notas_rect_1, DOWN).scale(0.8)
        notas_rect_3 = TexMobject(r"3)\ R_{k+1}\ \text{tiene infinitos puntos de}\ \{\vec{x}_n\}").next_to(notas_rect_2,
                                                                                                           1.5 * DOWN).scale(
            0.8).shift(1 * RIGHT)

        # Refer'{e}ncia a los rect'{a}ngulos anidados
        TRA_a = TextMobject("Gracias a las observaciones 1 y 2, y al teorema ").move_to(notas_rect_0)
        TRA_b = TextMobject(r"\text{de los rect\'{a}ngulos anidados, existe} ", "$\\cap_{k=1}^{\\infty}R_k =$",
                            " $\\vec{x}_0$").next_to(TRA_a, DOWN)
        TRA_b[2].set_color(BLUE)
        TRA = VGroup(TRA_a, TRA_b).scale(0.9)

        construyamos_0 = TextMobject(r"\text{Construyamos una subsucesi\'{o}n}").shift(3 * RIGHT + UP)
        construyamos_1 = TextMobject("que converge a ", "$\\vec{x}_0$").next_to(construyamos_0, DOWN)
        construyamos_1[1].set_color(BLUE)
        construyamos = VGroup(construyamos_0, construyamos_1).scale(0.9)

        subsuc = TextMobject(r"\text{La observaci\'{o}n 3 nos permite tomar}").scale(0.8).shift(3 * RIGHT + UP)

        # Construyendo la subsucesi'{o}n
        subsuc_1 = TexMobject(r"\vec{x}_{n_1}", r"\in R_1").shift(3 * RIGHT)
        subsuc_1[0].set_color(RED)

        subsuc_2a = TexMobject(r"\vec{x}_{n_2}", r"\in R_2").shift(3 * RIGHT)
        subsuc_2a[0].set_color(RED)
        subsuc_2b = TexMobject(r"\text{tomando } n_2>n_1").next_to(subsuc_2a, 1.5 * DOWN).scale(0.9)
        subsuc_2 = VGroup(subsuc_2a, subsuc_2b)

        subsuc_3a = TexMobject(r"\vec{x}_{n_3}", r"\in R_3").shift(3 * RIGHT)
        subsuc_3a[0].set_color(RED)
        subsuc_3b = TexMobject(r"\text{tomando } n_3>n_2").next_to(subsuc_3a, 1.5 * DOWN).scale(0.9)
        subsuc_3 = VGroup(subsuc_3a, subsuc_3b)

        subsuc_ka = TexMobject(r"\vec{x}_{n_k}", r"\in R_k").shift(3 * RIGHT)
        subsuc_ka[0].set_color(RED)
        subsuc_kb = TexMobject(r"\text{tomando } n_k>n_{k-1}").next_to(subsuc_3a, 1.5 * DOWN).scale(0.9)
        subsuc_k = VGroup(subsuc_ka, subsuc_kb)

        casi_conclu_a = TextMobject("De esta forma").move_to(construyamos_1).shift(3 * UP)
        casi_conclu_b = TexMobject(r"0\leq d(\vec{x}_{n_k},\vec{x}_0)\leq \frac{\sqrt{2}M}{2^{k-1}}").next_to(
            casi_conclu_a, DOWN)
        casi_conclu = VGroup(casi_conclu_a, casi_conclu_b).scale(0.9)

        pre_conclu_a = TexMobject(r"\text{y como } \lim_{k \to \infty} \frac{\sqrt{2}M}{2^{k-1}} = 0").move_to(
            notas_rect_3).shift(2 * UP)
        pre_conclu_b = TexMobject(r" \Rightarrow \lim_{k \to \infty} d(\vec{x}_{n_k},\vec{x}_0) = 0").next_to(
            pre_conclu_a, DOWN)
        pre_conclu = VGroup(pre_conclu_a, pre_conclu_b).scale(0.8)

        conclu_a = TextMobject("Tenemos").move_to(notas_rect_3).scale(0.9)
        conclu_b = TexMobject(r"\lim_{k \to \infty} \{\vec{x}_{n_k}\} = \vec{x}_0").next_to(conclu_a, 1.6 * DOWN)
        conclu_c = TextMobject("nuestra ", r"\text{subsucesi\'{o}n convergente.}").next_to(conclu_b, 1.3 * DOWN)
        conclu_c[1].set_color(RED)
        conclu_rect = Rectangle(color=RED, width=1.2 * conclu_b.get_width(),
                                height=1.3 * conclu_b.get_height()).move_to(conclu_b)
        conclu = VGroup(conclu_a, conclu_b, conclu_c, conclu_rect)

        # Secuencia de la animación: Teorema de Bolzano-Weierstrass
        self.play(Write(titulo))
        self.wait()
        self.play(FadeOut(titulo))
        self.play(Write(teorema))
        self.wait(2)
        self.play(FadeOut(teorema))
        self.play(ShowCreation(plano))
        self.play(Write(group_acot))
        self.play(ShowIncreasingSubsets(group2, run_time=2.0))
        self.play(ShowCreation(circulo), ShowCreation(emes))
        self.wait()
        self.play(ReplacementTransform(group_acot, el_rect), FadeOut(plano))
        self.wait(2)
        self.play(ShowCreation(R), FadeOut(circulo))
        self.wait(2)
        self.play(ReplacementTransform(el_rect, subrect_1), Write(cuadrante_dR1))
        self.wait(3)
        self.play(ShowCreation(R1))
        self.wait(3)
        self.play(ReplacementTransform(subrect_1, subrect_2), FadeOut(cuadrante_dR1))
        self.wait(2)
        self.play(ShowCreation(R2))
        self.wait(6)
        self.play(ReplacementTransform(subrect_2, subrects))
        self.wait(2)
        self.play(ShowCreation(R3))
        self.play(ShowCreation(R4))
        self.play(ShowCreation(R5))
        self.play(ShowCreation(R6))
        self.wait()
        self.play(FadeOut(subrects))
        self.play(emes.shift, 3 * LEFT, group2.shift, 3 * LEFT, R.shift, 3 * LEFT, R1.shift, 3 * LEFT, \
                  R2.shift, 3 * LEFT, R3.shift, 3 * LEFT, R4.shift, 3 * LEFT, R5.shift, 3 * LEFT, R6.shift, 3 * LEFT
                  )  # Mover toda la construcción a la izquierda
        self.play(FadeOut(emes))
        self.play(Write(notas_rect_0))
        self.wait(2)
        self.play(Write(notas_rect_1))
        self.wait(2)
        self.play(Write(notas_rect_2))
        self.wait(2)
        self.play(Write(notas_rect_3))
        self.wait(4)
        self.play(FadeOut(notas_rect_1), FadeOut(notas_rect_2), FadeOut(notas_rect_3),
                  ReplacementTransform(notas_rect_0, TRA))
        self.wait(2)
        self.play(ApplyMethod(points_infinite_values[1495].custom_method, BLUE))
        self.play(ApplyMethod(points_infinite_values[1495].other_method, run_time=1.5))
        self.wait(2)
        self.play(Write(construyamos))
        self.wait(2)
        self.play(FadeOut(TRA), construyamos.shift, 2 * UP)
        self.wait(2)
        self.play(Write(subsuc), Write(subsuc_1))
        self.play(ApplyMethod(points_infinite_values[1].custom_method, RED))
        self.play(ApplyMethod(points_infinite_values[1].other_method))
        self.wait(2)
        self.play(FadeOut(subsuc))
        self.play(ReplacementTransform(subsuc_1, subsuc_2), ApplyMethod(points_infinite_values[7].custom_method, RED))
        self.play(ApplyMethod(points_infinite_values[7].other_method))
        self.wait(2)
        self.play(ReplacementTransform(subsuc_2, subsuc_3), ApplyMethod(points_infinite_values[51].custom_method, RED))
        self.play(ApplyMethod(points_infinite_values[51].other_method))
        self.wait(2)
        self.play(ReplacementTransform(subsuc_3, subsuc_k), ApplyMethod(points_infinite_values[799].custom_method, RED))
        self.play(ApplyMethod(points_infinite_values[799].other_method))
        self.play(FadeOut(subsuc_k), FadeOut(construyamos))
        self.play(Write(casi_conclu))
        self.wait(8)
        self.play(Write(pre_conclu))
        self.wait(11)
        self.play(Write(conclu))
        self.wait(4)
        self.play(FadeOut(casi_conclu), FadeOut(pre_conclu), FadeOut(Rects), FadeOut(group2))
        self.play(conclu.move_to, (0, 0, 0))
        self.wait(2)
        self.play(FadeOut(conclu))