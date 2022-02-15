from manimlib.imports import *

class Limites_Al_Infinito(ThreeDScene):
    def cur_1(self, t):
        return np.array([t, t * np.sin(5 * t), -np.exp(t / 2) * np.cos(5 * t)])

    def construct(self):

        ###Texto
        titulo = TextMobject(
            """Divergencia a Infinito de Funciones de \n
            $\\mathbb{R}\\rightarrow\\mathbb{R}^{n}$ en Infinito""",
        )
        definicion_1 = TextMobject(
            """Sea $f: \\mathbb{R} \\rightarrow \\mathbb{R}^{n}$"""
        )
        definicion_2 = TextMobject(
            """$$\\implies \\ \\lim_{t \\rightarrow  \\infty} f(t) = \\vec{\\infty} \\Leftrightarrow  \\forall \\: M >0$$"""
        )
        definicion_3 = TextMobject(
            """$\\exists$ $\\delta >0$ tal que si $ t> \\delta$ \n 
            $\\implies \\ \\Vert f(t) \\Vert > M$"""
        ).move_to(definicion_2.get_center() + 0.9 * DOWN)

        ##Animacion definiciones
        self.play(Write(titulo.scale(1.5)))
        self.wait()
        self.play(FadeOut(titulo))
        self.play(Write(definicion_1))
        self.wait(2.5)
        self.play(definicion_1.shift, 1.2 * UP, runtime=1.5)
        self.play(Write(definicion_2))
        self.wait(6.5)
        self.play(Write(definicion_3))
        self.wait(7.6)
        self.play(FadeOut(definicion_2), FadeOut(definicion_3), FadeOut(definicion_1))
        self.wait()
        self.custom_method()

    def custom_method(self):
        t_1 = TextMobject("""Por ejemplo:""")
        t_2 = TextMobject("""$f(t) = (t \\sin(5t),- e^{\\frac{t}{2}} \\cos(5t))$""")
        t_2.set_color(TEAL)
        t_3 = TextMobject("""Cuando  $t \\rightarrow \\infty$""")
        t_4 = TextMobject("""Vemos que  $\\forall$""", """ $M$""", """$>0$""")
        t_4[1].set_color(YELLOW)
        t_5 = TextMobject("""Si $t > $  """, """$\\delta$ """, """ adecuada""")
        t_5[1].set_color(RED)
        t_6 = TextMobject(
            """Notamos que \n 
        $ \\Vert $""",
            """$f(t)$""",
            """$ \\Vert > $""",
            """$  M$""",
        )
        t_6[1].set_color(TEAL)
        t_6[3].set_color(YELLOW)
        t_7 = TextMobject("""$\\forall$""", """ $M $""", """$> 0$""")
        t_7[1].set_color(YELLOW)
        t_8 = TextMobject(
            """¿Qué crees que sucede cuando $t \\rightarrow - \\infty$?"""
        )

        t_1.to_corner(UL)
        t_2.to_corner(UL)
        t_3.to_corner(UL)
        t_4.to_corner(UL)
        t_5.to_corner(UL)
        t_6.to_corner(UL)
        t_7.to_corner(UL)

        axes = ThreeDAxes(
            x_min=-5.5, x_max=5.5, z_min=-5.5, z_max=40, num_axis_pieces=50
        )
        axes.add(axes.get_x_axis_label("t"))
        curve_1 = ParametricFunction(self.cur_1, color=TEAL, t_min=-5, t_max=5)

        M = Line(
            np.array([0, 0, 0]),
            np.array([0, -1 / np.sqrt(2), 1 / np.sqrt(2)]),
            stroke_width=8,
            color=YELLOW,
        ).move_to(np.array([1, -1 / (2 * np.sqrt(2)), 1 / (2 * np.sqrt(2))]))
        m = (
            TextMobject("$M$")
            .rotate(PI / 2, axis=RIGHT)
            .rotate(PI / 2, about_edge=Z_AXIS)
            .move_to(M.get_center() + np.array([0, -0.5, 0.5]))
            .set_color(YELLOW)
        )
        Delta = Line(
            np.array([0, 0, 0]), np.array([1, 0, 0]), stroke_width=8, color=RED
        ).move_to(np.array([0.5, 0, 0]))
        delta = (
            TextMobject("$\\delta$")
            .rotate(PI / 2, axis=RIGHT)
            .rotate(PI / 2, about_edge=Z_AXIS)
            .move_to(Delta.get_center() + np.array([0.5, 0.5, 0]))
            .set_color(RED)
        )
        Bola = (
            Circle(radius=1, color=YELLOW)
            .rotate(PI / 2, axis=RIGHT)
            .rotate(PI / 2, about_edge=Z_AXIS)
            .move_to(np.array([1, 0, 0]))
        )

        ###Grupos
        Group = VGroup(M, m, Delta, delta, Bola)
        Group_1 = VGroup(curve_1)
        Group_2 = VGroup(M, m)
        Group_3 = VGroup(Delta, delta)

        ### Update

        x = ValueTracker(1)

        def update_group(Group):
            M, m, Delta, delta, Bola = Group
            M_new = Line(
                np.array([0, 0, 0]),
                np.array([0, -x.get_value() / np.sqrt(2), x.get_value() / np.sqrt(2)]),
                stroke_width=8,
                color=YELLOW,
            ).move_to(
                np.array(
                    [
                        x.get_value(),
                        -x.get_value() / (2 * np.sqrt(2)),
                        x.get_value() / (2 * np.sqrt(2)),
                    ]
                )
            )
            M.become(M_new)
            m.move_to(
                M_new.get_center()
                + np.array([0, -x.get_value() / np.sqrt(2), x.get_value() / np.sqrt(2)])
            )
            Delta_new = Line(
                np.array([0, 0, 0]),
                np.array([x.get_value(), 0, 0]),
                stroke_width=8,
                color=RED,
            ).move_to(np.array([(x.get_value()) / 2, 0, 0]))
            Delta.become(Delta_new)
            delta.move_to(Delta_new.get_center() + np.array([0.5, 0.5, 0]))
            Bola_new = (
                Circle(radius=x.get_value(), color=YELLOW)
                .rotate(PI / 2, axis=RIGHT)
                .rotate(PI / 2, about_edge=Z_AXIS)
                .move_to(np.array([x.get_value(), 0, 0]))
            )
            Bola.become(Bola_new)
            return Group

        ### Animaciones
        self.begin_ambient_camera_rotation(rate=0.12)
        self.add_fixed_in_frame_mobjects(t_1)
        self.play(Write(t_1))
        self.wait(2.75)
        self.play(FadeOut(t_1))
        self.add(axes)
        self.set_camera_orientation(phi=65 * DEGREES, theta=-90 * DEGREES)
        self.play(LaggedStart(ShowCreation(Group_1)))
        self.wait(2)
        self.add_fixed_in_frame_mobjects(t_2)
        self.play(Write(t_2))
        self.wait(6)
        self.play(FadeOut(t_2))
        self.add_fixed_in_frame_mobjects(t_3)
        self.play(Write(t_3))
        self.wait(3.5)
        self.play(FadeOut(t_3))
        self.add_fixed_in_frame_mobjects(t_4)
        self.play(Write(t_4))
        self.wait(4.2)
        self.add(Group_2)
        self.wait()
        self.play(FadeOut(t_4))
        self.wait()
        self.add_fixed_in_frame_mobjects(t_5)
        self.play(Write(t_5))
        self.wait(3.8)
        self.add(Group_3)
        self.wait()
        self.play(FadeOut(t_5))
        self.add(Bola)
        self.add_fixed_in_frame_mobjects(t_6)
        self.play(Write(t_6))
        self.wait(4.2)
        self.play(FadeOut(t_6))
        self.wait()
        self.add_fixed_in_frame_mobjects(t_7)
        self.play(Write(t_7))
        self.wait(3.5)
        Group.add_updater(update_group)
        self.add(Group)
        self.play(x.increment_value, 2, rate_func=linear, run_time=10)
        self.wait()
        self.play(FadeOut(t_7))
        self.play(FadeOut(Group))
        self.play(FadeOut(Group_1), FadeOut(axes))
        self.add_fixed_in_frame_mobjects(t_8)
        self.play(Write(t_8))
        self.wait(5)
        self.play(FadeOut(t_8))