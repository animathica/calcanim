from manimlib.imports import *

class Divergencia_A_Infinito(ThreeDScene):
    def cur_1(self, t):
        return np.array([t, 1 / (1 - t), t ** 2])

    def construct(self):

        ###Texto
        titulo = TextMobject(
            """Divergencia a Infinito de Funciones de \n
            $\\mathbb{R}\\rightarrow\\mathbb{R}^{n}$ en un Punto $t_0$"""
        )
        definicion_1 = TextMobject(
            """Sea $f: \\mathbb{R} \\rightarrow \\mathbb{R}^{n}$"""
        )
        definicion_2 = TextMobject(
            """$$\\lim_{t \\rightarrow t_{0}} f(t) = \\vec{\\infty} \\Leftrightarrow  \\forall \\: M >0$$"""
        )
        definicion_3 = TextMobject(
            """$\\exists \\delta >0$ tal que si $0< |t-t_{0}| < \\delta$ \n $\\Rightarrow \\Vert f(t) \\Vert > M$"""
        ).move_to(definicion_2.get_center() + 0.8 * DOWN)

        ### Animaciones
        self.play(Write(titulo.scale(1.5)))
        self.wait()
        self.play(FadeOut(titulo))
        self.play(Write(definicion_1))
        self.wait(4.25)
        self.play(definicion_1.shift, 1.2 * UP, runtime=1.5)
        self.play(Write(definicion_2))
        self.wait(6.125)
        self.play(Write(definicion_3))
        self.wait(8.75)
        self.play(FadeOut(definicion_2), FadeOut(definicion_3), FadeOut(definicion_1))
        self.wait()
        self.custom_method()

    def custom_method(self):
        t_1 = TextMobject("""Veamos este ejemplo:""")
        t_2 = TextMobject("""$f(t) = (\\frac{1}{1-t},t^2)$""")
        t_2[0].set_color(PURPLE)
        t_3 = TextMobject(
            """¿Qué sucede cuando \n
        $t \\rightarrow 1$?"""
        )
        t_4 = TextMobject("""Tomemos """, """$M$""", """$>0$""")
        t_4[1].set_color("#88FF00")
        t_5 = TextMobject(
            """Si elegimos adecuadamente \n
        """,
            """$\\delta$""",
            """$>0 $""",
        )
        t_5[1].set_color(BLUE)
        t_6 = TextMobject(
            """Es claro que \n
        $\\Vert$""",
            """$ f(t) $""",
            """$\\Vert >$""",
            """$  M$""",
        )
        t_6[1].set_color(PURPLE)
        t_6[3].set_color("#88FF00")
        t_7 = TextMobject("""$\\forall$""", """ $M$""", """$> 0$""")
        t_7[1].set_color("#88FF00")
        t_8 = TextMobject(
            """¿Se te ocurre como definir este límite usando sucesiones?"""
        )

        t_1.to_corner(UL)
        t_2.to_corner(UL)
        t_3.to_corner(UL)
        t_4.to_corner(UL)
        t_5.to_corner(UL)
        t_6.to_corner(UL)
        t_7.to_corner(UL)

        ### Objetos

        axes = ThreeDAxes()
        axes.add(axes.get_x_axis_label("t"))
        curve_1_1 = ParametricFunction(self.cur_1, color=PURPLE, t_min=-3, t_max=0.9)
        curve_1_2 = ParametricFunction(self.cur_1, color=PURPLE, t_min=1.1, t_max=3)

        M = Line(
            np.array([0, 0, 0]),
            np.array([0, -1 / np.sqrt(2), 1 / np.sqrt(2)]),
            stroke_width=8,
            color="#88FF00",
        ).move_to(np.array([1, -1 / (2 * np.sqrt(2)), 1 / (2 * np.sqrt(2))]))
        m = (
            TextMobject("$M$")
            .rotate(PI / 2, axis=RIGHT)
            .rotate(PI / 2, about_edge=Z_AXIS)
            .move_to(M.get_center() + np.array([0, -0.5, 0.5]))
            .set_color("#88FF00")
        )
        Delta = Line(
            np.array([0, 0, 0]), np.array([1.5, 0, 0]), stroke_width=8, color=BLUE
        ).move_to(np.array([1.75, 0, 0]))
        delta = (
            TextMobject("$\\delta$")
            .rotate(PI / 2, axis=RIGHT)
            .rotate(PI / 2, about_edge=Z_AXIS)
            .move_to(Delta.get_center() + np.array([0.5, 0.5, 0]))
            .set_color(BLUE)
        )
        Bola = (
            Circle(radius=1, color="#88FF00")
            .rotate(PI / 2, axis=RIGHT)
            .rotate(PI / 2, about_edge=Z_AXIS)
            .move_to(np.array([1, 0, 0]))
        )

        ###Grupos
        Group = VGroup(M, m, Delta, delta, Bola)
        Group_1 = VGroup(curve_1_1, curve_1_2)
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
                color="#88FF00",
            ).move_to(
                np.array(
                    [
                        1,
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
                np.array([1 / x.get_value(), 0, 0]),
                stroke_width=8,
                color=BLUE,
            ).move_to(np.array([1 + (1 / x.get_value()) / 2, 0, 0]))
            Delta.become(Delta_new)
            delta.move_to(Delta_new.get_center() + np.array([0.5, 0.5, 0]))
            Bola_new = (
                Circle(radius=x.get_value(), color="#88FF00")
                .rotate(PI / 2, axis=RIGHT)
                .rotate(PI / 2, about_edge=Z_AXIS)
                .move_to(np.array([1, 0, 0]))
            )
            Bola.become(Bola_new)
            return Group

        ## Animaciones
        self.begin_ambient_camera_rotation(rate=0.1)
        self.add_fixed_in_frame_mobjects(t_1)
        self.play(Write(t_1))
        self.wait(3.125)
        self.play(FadeOut(t_1))
        self.add(axes)
        self.set_camera_orientation(phi=65 * DEGREES, theta=-90 * DEGREES)
        self.play(LaggedStart(ShowCreation(Group_1)))
        self.wait(2)
        self.add_fixed_in_frame_mobjects(t_2)
        self.play(Write(t_2))
        self.wait(3.87)
        self.play(FadeOut(t_2))
        self.add_fixed_in_frame_mobjects(t_3)
        self.play(Write(t_3))
        self.wait(4.25)
        self.play(FadeOut(t_3))
        self.add_fixed_in_frame_mobjects(t_4)
        self.play(Write(t_4))
        self.wait(3.5)
        self.add(Group_2)
        self.wait()
        self.play(FadeOut(t_4))
        self.add(Group_3)
        self.wait()
        self.add_fixed_in_frame_mobjects(t_5)
        self.play(Write(t_5))
        self.wait(4.25)
        self.play(FadeOut(t_5))
        self.add(Bola)
        self.add_fixed_in_frame_mobjects(t_6)
        self.play(Write(t_6))
        self.wait(4.625)
        self.play(FadeOut(t_6))
        self.wait()
        self.add_fixed_in_frame_mobjects(t_7)
        self.play(Write(t_7))
        self.wait(3.5)
        Group.add_updater(update_group)
        self.add(Group)
        self.play(x.increment_value, 1, rate_func=linear, run_time=10)
        self.play(FadeOut(t_7))
        self.wait()
        self.play(FadeOut(Group), FadeOut(Group_1), FadeOut(axes))
        self.add_fixed_in_frame_mobjects(t_8)
        self.play(Write(t_8))
        self.wait(5.375)
        self.play(FadeOut(t_8))