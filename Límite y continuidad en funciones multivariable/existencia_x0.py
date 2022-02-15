from manimlib.imports import *

#######################
#######################
####LIMITES DE R a R2


class Existencia_Limites(ThreeDScene):
    def cur(self, t):
        return np.array([t, t ** 2, t ** 3])

    def sur(self, x, y):
        return np.array([x, y, 1 / (1 + x ** 2 + y ** 2)])

    def construct(self):

        ###Texto
        titulo = TextMobject(
            """Existencia del Límite de Funciones de \n
            $\\mathbb{R}^{n}\\rightarrow\\mathbb{R}^{m}$ en $\\vec{x}_0$"""
        )
        definicion_1 = TextMobject(
            """Sean $f:A \\subset \\mathbb{R}^{n}\\rightarrow\\mathbb{R}^{m}$ y $\\vec{x}_0 \\in A^{\\prime} $. """
        )
        definicion_2 = TextMobject(
            """Decimos que $f$ tiene límite en $\\vec{x}_0$ y  que su límite es $\\vec{l} \\in \\mathbb{R}^{m}$, """
        )
        definicion_3 = TextMobject(
            """si $\\forall$ $\\epsilon > 0$ $\\exists$ $\\delta>0$ tal que si $\\Vert  \\vec{x} - \\vec{x}_0 \\Vert  < \\delta$ y $\\vec{x} \\in A \\setminus  \{\\vec{x}_0\}$, """
        ).move_to(definicion_2.get_center() + 0.8 * DOWN)
        definicion_4 = TextMobject(
            """ entonces $\\Vert f(\\vec{x}) - \\vec{l} \\Vert < \\epsilon$"""
        ).move_to(definicion_3.get_center() + 0.8 * DOWN)
        ### Animacion definiciones
        self.play(Write(titulo.scale(1.5)))
        self.wait()
        self.play(FadeOut(titulo))
        self.play(Write(definicion_1))
        self.wait(6.87)
        self.play(definicion_1.shift, 1.2 * UP, runtime=1.5)
        self.play(Write(definicion_2))
        self.wait(8)
        self.play(Write(definicion_3))
        self.wait(11)
        self.play(Write(definicion_4))
        self.wait(4.62)
        self.play(
            FadeOut(definicion_2),
            FadeOut(definicion_3),
            FadeOut(definicion_4),
            FadeOut(definicion_1),
        )
        self.wait()
        self.custom_method()

    def custom_method(self):
        t_1 = TextMobject("Por ejemplo, consideremos la siguiente función:")
        t_2 = TextMobject("$f(t) = (t^2, t^3)$")
        t_2[0].set_color(RED)
        t_3 = TextMobject(
            """Veamos el límite cuando \n  
        $ t \\rightarrow 0$"""
        )
        t_4 = TextMobject(
            """Tomamos de forma \n  
        arbitraria """,
            """ $\\epsilon$""",
            """$> 0$""",
        )
        t_4[1].set_color(BLUE)
        t_5 = TextMobject(
            """Y observamos gráficamente \n
        que $\\exists$ """,
            """ $\\delta$""",
            """$> 0$""",
        )
        t_5[1].set_color("#88FF00")
        t_6 = TextMobject(
            """tal que se cumple \n 
        la definción \n
        de limite cuando $ t \\rightarrow 0$ """
        )
        t_7 = TextMobject(
            """Veamos que esto se \n
        sigue cumpliendo con valores \n 
        más pequeños de """,
            """$\\epsilon$ """,
        )
        t_7[1].set_color(BLUE)
        t_8 = TextMobject(
            """$\\displaystyle \\therefore \lim_{t \\to 0}$""",
            """ $f(t) = \\vec{0} $""",
        )
        t_8[1].set_color(RED)
        t_9 = TextMobject(
            """Ahora consideremos \n 
        esta otra función"""
        )
        t_10 = TextMobject("""$g(x,y) = \\frac{1}{1 + x^2 + y^2}$""")
        t_10[0].set_color(BLUE)
        t_11 = TextMobject(
            """¿Existe límite cuando \n 
        $(x,y)\\rightarrow (0,0)$ ?"""
        )
        t_12 = TextMobject(
            """De la misma manera \n 
        podemos visualizar que \n
         se cumple la definición"""
        )
        t_13 = TextMobject(
            """Observamos que \n
        $\\displaystyle \lim_{(x,y) \\to (0,0)}$""",
            """$\\ g(x,y) = 1 $""",
        )
        t_13[1].set_color(BLUE)
        t_14 = TextMobject(
            """¿Puedes encontrar de forma analítica \n
             la""",
            """ $\\delta$""",
            """ apropiada para demostrar estos límites?""",
        )
        t_14[1].set_color("#88FF00")

        t_1.to_corner(UL)
        t_2.to_corner(UL)
        t_3.to_corner(UL)
        t_4.to_corner(UL)
        t_5.to_corner(UL)
        t_6.to_corner(UL)
        t_7.to_corner(UL)
        t_8.to_corner(UL)
        t_9.to_corner(UL)
        t_10.to_corner(UL)
        t_11.to_corner(UL)
        t_12.to_corner(UL)
        t_13.to_corner(UL)

        ### Objetos

        axes = ThreeDAxes()
        axes.add(axes.get_x_axis_label("t"))
        axes1 = ThreeDAxes()
        axes1.add(axes1.get_axis_labels())
        curve = ParametricFunction(self.cur, color=RED, t_min=-3, t_max=3)
        surface = ParametricSurface(
            self.sur, color=GREEN, u_min=-3, u_max=3, v_min=-3, v_max=3
        )
        linea = Line(
            np.array([0, 0, 0]),
            np.array([0, 1 / np.sqrt(2), 1 / np.sqrt(2)]),
            stroke_width=8,
            color=BLUE,
        ).move_to((0, 1 / (2 * np.sqrt(2)), 1 / (2 * np.sqrt(2))))
        lineas = [
            Line(
                np.array([0, 0, 0]),
                np.array([0, x / np.sqrt(2), x / np.sqrt(2)]),
                stroke_width=8,
                color=BLUE,
            ).move_to((0, x / (2 * np.sqrt(2)), x / (2 * np.sqrt(2))))
            for x in np.arange(0.1, 1.1, 0.2)[::-1]
        ]
        bolas = [
            Circle(radius=x, color=BLUE)
            .rotate(PI / 2, axis=RIGHT)
            .rotate(PI / 2, about_edge=Z_AXIS)
            for x in np.arange(0.1, 1.1, 0.2)[::-1]
        ]
        deltas = [
            Line(
                np.array([0, 0, 0]),
                np.array([x / 2, 0, 0]),
                stroke_width=8,
                color="#88FF00",
            ).move_to((x / 4, 0, 0))
            for x in np.arange(0.1, 1.1, 0.2)[::-1]
        ]

        lineas_2 = [
            Line(
                np.array([0, 0, 0]), np.array([0, 0, x]), stroke_width=8, color=RED
            ).move_to((0, 0, x / 2 + 1))
            for x in np.arange(0.1, 1.1, 0.2)[::-1]
        ]
        bolas_2 = [
            Circle(radius=x, color="#88FF00").move_to((0, 0, 1))
            for x in np.arange(0.1, 1.1, 0.2)[::-1]
        ]
        deltas_2 = [
            Line(
                np.array([0, 0, 0]),
                np.array([x / (np.sqrt(2)), x / (np.sqrt(2)), 0]),
                stroke_width=8,
                color="#88FF00",
            ).move_to((x / (2 * np.sqrt(2)), x / (2 * np.sqrt(2)), 1))
            for x in np.arange(0.1, 1.1, 0.2)[::-1]
        ]

        ### Objetos nuevos

        Epsilon = Line(
            np.array([0, 0, 0]),
            np.array([0, 1 / np.sqrt(2), 1 / np.sqrt(2)]),
            stroke_width=8,
            color=BLUE,
        ).move_to((0, 1 / (2 * np.sqrt(2)), 1 / (2 * np.sqrt(2))))
        Bola = (
            Circle(radius=1, color=BLUE)
            .rotate(PI / 2, axis=RIGHT)
            .rotate(PI / 2, about_edge=Z_AXIS)
        )
        Delta = Line(
            np.array([0, 0, 0]),
            np.array([1 / 2, 0, 0]),
            stroke_width=8,
            color="#88FF00",
        ).move_to((1 / 4, 0, 0))

        Epsilon_2 = Line(
            np.array([0, 0, 0]), np.array([0, 0, 1]), stroke_width=8, color=RED
        ).move_to((0, 0, 1 / 2 + 1))
        Bola_2 = Circle(radius=1, color="#88FF00").move_to((0, 0, 1))
        Delta_2 = Line(
            np.array([0, 0, 0]),
            np.array([1 / (np.sqrt(2)), 1 / (np.sqrt(2)), 0]),
            stroke_width=8,
            color="#88FF00",
        ).move_to((1 / (2 * np.sqrt(2)), 1 / (2 * np.sqrt(2)), 1))

        epsilon = TextMobject("$\\epsilon$")
        epsilon.rotate(PI / 2, axis=RIGHT).rotate(PI / 2, about_edge=Z_AXIS).move_to(
            Epsilon.get_center() + np.array([0, 0.5, 0.5])
        ).set_color(BLUE)
        delta = TextMobject("$\\delta$")
        delta.rotate(PI / 2, axis=RIGHT).rotate(PI / 2, about_edge=Z_AXIS).move_to(
            Delta.get_center() + np.array([0.5, 0.5, 0])
        ).set_color("#88FF00")

        epsilon_2 = TextMobject("$\\epsilon$")
        epsilon_2.rotate(PI / 2, axis=RIGHT).rotate(PI / 2, about_edge=Z_AXIS).move_to(
            Epsilon_2.get_center() + np.array([0.5, 0, 0.5])
        ).set_color(RED)
        delta_2 = TextMobject("$\\delta$")
        delta_2.rotate(PI / 2, axis=RIGHT).rotate(PI / 2, about_edge=Z_AXIS).move_to(
            Delta_2.get_center() + np.array([0.5, 0.5, 0])
        ).set_color("#88FF00")

        ### Update

        x = ValueTracker(1)

        def update_group_1(Group):
            Epsilon, Delta, Bola, epsilon, delta = Group
            Epsilon_new = Line(
                np.array([0, 0, 0]),
                np.array(
                    [
                        0,
                        (1 / x.get_value()) / np.sqrt(2),
                        (1 / x.get_value()) / np.sqrt(2),
                    ]
                ),
                stroke_width=8,
                color=BLUE,
            ).move_to(
                (
                    0,
                    (1 / x.get_value()) / (2 * np.sqrt(2)),
                    (1 / x.get_value()) / (2 * np.sqrt(2)),
                )
            )
            Epsilon.become(Epsilon_new)
            epsilon.move_to(Epsilon_new.get_center() + np.array([0, 0.5, 0.5]))
            Delta_new = Line(
                np.array([0, 0, 0]),
                np.array([(1 / x.get_value()) / 2, 0, 0]),
                stroke_width=8,
                color="#88FF00",
            ).move_to(((1 / x.get_value()) / 4, 0, 0))
            Delta.become(Delta_new)
            delta.move_to(Delta.get_center() + np.array([0.5, 0.5, 0]))
            Bola_new = (
                Circle(radius=(1 / x.get_value()), color=BLUE)
                .rotate(PI / 2, axis=RIGHT)
                .rotate(PI / 2, about_edge=Z_AXIS)
            )
            Bola.become(Bola_new)
            return Group

        y = ValueTracker(1)

        def update_group_2(Group):
            Epsilon_2, Delta_2, Bola_2, epsilon_2, delta_2 = Group
            Epsilon_new_2 = Line(
                np.array([0, 0, 0]),
                np.array([0, 0, (1 / y.get_value())]),
                stroke_width=8,
                color=RED,
            ).move_to((0, 0, (1 / y.get_value()) / 2 + 1))
            Epsilon_2.become(Epsilon_new_2)
            epsilon_2.move_to(Epsilon_new_2.get_center() + np.array([0, 0.5, 0.5]))
            Delta_new_2 = Line(
                np.array([0, 0, 0]),
                np.array(
                    [
                        (1 / y.get_value()) / (np.sqrt(2)),
                        (1 / y.get_value()) / (np.sqrt(2)),
                        0,
                    ]
                ),
                stroke_width=8,
                color="#88FF00",
            ).move_to(
                (
                    (1 / y.get_value()) / (2 * np.sqrt(2)),
                    (1 / y.get_value()) / (2 * np.sqrt(2)),
                    1,
                )
            )
            Delta_2.become(Delta_new_2)
            delta_2.move_to(Delta_new_2.get_center() + np.array([0.5, 0.5, 0]))
            Bola_new_2 = Circle(radius=(1 / y.get_value()), color="#88FF00").move_to(
                (0, 0, 1)
            )
            Bola_2.become(Bola_new_2)
            return Group

        ### Grupos
        Group_1 = VGroup(Epsilon, epsilon)
        Group_2 = VGroup(Delta, delta)
        Group_3 = VGroup(Epsilon_2, epsilon_2)
        Group_4 = VGroup(Delta_2, delta_2)
        Big_Group_1 = VGroup(Epsilon, Delta, Bola, epsilon, delta)
        Big_Group_2 = VGroup(Epsilon_2, Delta_2, Bola_2, epsilon_2, delta_2)

        ###Animaciones
        self.begin_ambient_camera_rotation(rate=0.06)
        self.add_fixed_in_frame_mobjects(t_1)
        self.play(Write(t_1))
        self.wait(4.25)
        self.play(FadeOut(t_1))
        self.add_fixed_in_frame_mobjects(t_2)
        self.play(Write(t_2))
        self.wait(3.125)
        self.add(axes)
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        self.play(LaggedStart(ShowCreation(curve)))
        self.wait(2)
        self.play(FadeOut(t_2))
        self.add_fixed_in_frame_mobjects(t_3)
        self.play(Write(t_3))
        self.wait(4.625)
        self.play(FadeOut(t_3))
        self.add_fixed_in_frame_mobjects(t_4)
        self.play(Write(t_4))
        self.wait(4.625)
        self.add(Group_1)
        self.wait(2)
        self.play(FadeOut(t_4))
        self.add_fixed_in_frame_mobjects(t_5)
        self.play(Write(t_5))
        self.wait(5)
        self.add(Group_2)
        self.wait(2)
        self.play(FadeOut(t_5))
        self.add_fixed_in_frame_mobjects(t_6)
        self.play(Write(t_6))
        self.wait(6.5)
        self.add(Bola)
        self.wait(2)
        self.play(FadeOut(t_6))
        self.add_fixed_in_frame_mobjects(t_7)
        self.play(Write(t_7))
        self.wait(6.5)
        Big_Group_1.add_updater(update_group_1)
        self.add(Big_Group_1)
        self.play(x.increment_value, 5, rate_func=linear, run_time=10)
        self.wait()
        self.play(FadeOut(t_7))
        self.add_fixed_in_frame_mobjects(t_8)
        self.play(Write(t_8))
        self.wait(5)
        self.play(FadeOut(Big_Group_1))
        self.play(FadeOut(t_8))
        self.play(FadeOut(curve))
        self.add_fixed_in_frame_mobjects(t_9)
        self.play(FadeOut(axes))
        self.add(axes1)
        self.play(Write(t_9))
        self.wait(3.875)
        self.play(FadeOut(t_9))
        self.add_fixed_in_frame_mobjects(t_10)
        self.play(Write(t_10))
        self.wait(3.875)
        self.play(LaggedStart(ShowCreation(surface)))
        self.wait(2)
        self.play(FadeOut(t_10))
        self.add_fixed_in_frame_mobjects(t_11)
        self.play(Write(t_11))
        self.wait(4.25)
        self.play(FadeOut(t_11))
        self.add_fixed_in_frame_mobjects(t_12)
        self.play(Write(t_12))
        self.wait(6.125)
        self.add(Group_3, Group_4, Bola_2)
        self.wait()
        Big_Group_2.add_updater(update_group_2)
        self.add(Big_Group_2)
        self.play(y.increment_value, 5, rate_func=linear, run_time=10)
        self.wait()
        self.play(FadeOut(t_12))
        self.add_fixed_in_frame_mobjects(t_13)
        self.play(Write(t_13))
        self.wait(5)
        self.play(FadeOut(Big_Group_2))
        self.play(FadeOut(t_13))
        self.play(FadeOut(surface))
        self.play(FadeOut(axes1))
        self.add_fixed_in_frame_mobjects(t_14)
        self.play(Write(t_14))
        self.wait(6.5)
        self.play(FadeOut(t_14))