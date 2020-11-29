from manimlib.imports import *

##A lo largo de este código estan todas las animaciones realizadas
# por AniMathica sobre el tema de continuidad, límite y funciones
# de Rn a Rm fecha
# 14/10/2020​


class Operaciones_continuidad(ThreeDScene):
    def acomodar_textos(self, objeto):
        self.add_fixed_in_frame_mobjects(objeto)
        self.play(Write(objeto))

    def acomodar_puntos(self, objeto):
        self.add_fixed_in_frame_mobjects(objeto)
        self.add(objeto)

    # Definimos las funciones a utilizar (las que vamos a graficar)
    # Puedes cambiar estas funciones con las que se te ocurra
    # Son funciones de R  a R2, y estamos obteniendo sus gráficas
    # por lo que la primer entrada siempre debe ser lo que parametriza
    # la función, es decir, la variable independiente
    def helicoide(self, t):
        return [t, np.cos(5 * t), np.sin(5 * t)]  # f(t)=(cos(5t),sin(5t))

    def identidad(self, t):
        return [t, t, t]  # g(t)=(t,t)

    def func_suma(self, t):
        return [
            t,
            t + np.cos(5 * t),
            t + np.sin(5 * t),
        ]  # (f+g)(t)=(t+cos(5t),t+sin(5t))

    def func_por_escalar(self, t):
        k = 3  # Cambiar esta constante hará que se cambie la gráfica de k*f, también debes cambiarla en construct
        return [t, k * np.cos(5 * t), k * np.sin(5 * t)]  # (k*f)(t)=(kcos(5t),ksin(5t))

    def func_prod_int(self, t):
        return [
            t,
            2 * t ** 2 + t * np.cos(5 * t) + t * np.sin(5 * t),
            0,
        ]  # (f\cdot g)(t)=2t^2+tcos(5t)+tsin(5t)

    # Aquí se realiza la animación
    def construct(self):
        k = 3  # Cambia también esta constante al mismo valor que la de la función
        title = TextMobject("""Continuidad: Teoremas de Operaciones""").scale(1.5)
        t_1 = TextMobject(
            """Sean $f,g:D\\subseteq\\mathbb{R}^n\\longrightarrow\\mathbb{R}^m$, """,
            """$x_0$""",
            """$\\in D$ \n
                            $f$ y $g$ """,
            """continuas""",
            """ en """,
            """$x_0$""",
            """ entonces:""",
        ).shift(2 * UP)
        t_1.set_color_by_tex_to_color_map(
            {"""continuas""": BLUE, """$x_0$""": PURPLE_B}
        )
        t_2 = TextMobject(
            """1) $f+g$ es """, """continua""", """ en """, """$x_0$"""
        ).next_to(t_1, DOWN, buff=1.2)
        t_2.set_color_by_tex_to_color_map({"""continua""": BLUE, """$x_0$""": PURPLE_B})
        t_3 = TextMobject(
            """2) Sea $k\\in\\mathbb{R}$, $kf$ es """,
            """continua""",
            """ en """,
            """$x_0$""",
        ).next_to(t_2, DOWN)
        t_3.set_color_by_tex_to_color_map({"""continua""": BLUE, """$x_0$""": PURPLE_B})
        t_4 = TextMobject(
            """3) $f\\cdot g$ es """, """continua""", """ en """, """$x_0$"""
        ).next_to(t_3, DOWN)
        t_4.set_color_by_tex_to_color_map({"""continua""": BLUE, """$x_0$""": PURPLE_B})
        Nota = (
            TextMobject(
                """Nota: la tercera operación es un producto interior \\\\
                            Si $m=1$ se trata de producto de reales"""
            )
            .scale(0.75)
            .to_edge(DOWN)
        )
        t_5 = TextMobject("""Veamos algunos ejemplos...""")
        reglaf = (
            TextMobject("""$f(t)$""", """$=(\cos(5t),\sin(5t))$""")
            .scale(0.85)
            .to_corner(LEFT + UP)
            .shift(1 * RIGHT)
        )
        reglaf.set_color_by_tex_to_color_map({"""$f(t)$""": RED})
        reglaf.bg = SurroundingRectangle(
            reglaf, color=WHITE, fill_color=BLACK, fill_opacity=1
        )
        reglag = (
            TextMobject("""$g(t)$""", """$=(t,t)$""")
            .scale(0.85)
            .to_corner(LEFT + UP)
            .shift(2 * RIGHT)
        )
        reglag.set_color_by_tex_to_color_map({"""$g(t)$""": TEAL_D})
        reglag.bg = SurroundingRectangle(
            reglag, color=WHITE, fill_color=BLACK, fill_opacity=1
        )
        t_6 = (
            TextMobject(
                """$f$""",
                """ y """,
                """$g$""",
                """ son funciones """,
                """continuas""",
                """ \n
                            en """,
                """$t_0=0$""",
                """, ¿puedes demostrarlo?""",
            )
            .scale(0.85)
            .to_corner(LEFT + UP)
        )
        t_6.set_color_by_tex_to_color_map(
            {
                """continuas""": BLUE,
                """$f$""": RED,
                """$g$""": TEAL_D,
                """$t_0=0$""": YELLOW,
            }
        )
        t_6.bg = SurroundingRectangle(
            t_6, color=WHITE, fill_color=BLACK, fill_opacity=1
        )
        t_7 = (
            TextMobject(
                """Entonces $f+g$ también es \n
                            """,
                """continua""",
                """ en """,
                """$t_0$""",
            )
            .scale(0.85)
            .to_corner(LEFT + UP)
        )
        t_7.set_color_by_tex_to_color_map({"""continua""": BLUE, """$t_0$""": YELLOW})
        t_7.bg = SurroundingRectangle(
            t_7, color=WHITE, fill_color=BLACK, fill_opacity=1
        )
        reglafmasg = (
            TextMobject("""$(f+g)(t)$""", """$=(t+\cos(5t),t+\sin(5t))$""")
            .scale(0.85)
            .to_corner(LEFT + UP)
        )
        reglafmasg.set_color_by_tex_to_color_map({"""$(f+g)(t)$""": PINK})
        reglafmasg.bg = SurroundingRectangle(
            reglafmasg, color=WHITE, fill_color=BLACK, fill_opacity=1
        )
        t_8 = (
            TextMobject(
                """Si tomamos $k=$"""
                + str(k)
                + """, \n
                            $kf$ también es """,
                """continua""",
                """ en """,
                """$t_0$""",
            )
            .scale(0.85)
            .to_corner(LEFT + UP)
            .shift(0.4 * RIGHT)
        )
        t_8.set_color_by_tex_to_color_map({"""continua""": BLUE, """$t_0$""": YELLOW})
        t_8.bg = SurroundingRectangle(
            t_8, color=WHITE, fill_color=BLACK, fill_opacity=1
        )
        reglakf = (
            TexMobject(
                r"("
                + str(k)
                + r"f)(t)=("
                + str(k)
                + r"\cos(5t),"
                + str(k)
                + r"\sin(5t))"
            )
            .scale(0.85)
            .to_corner(LEFT + UP)
            .shift(0.4 * RIGHT)
        )
        reglakf.bg = SurroundingRectangle(
            reglakf, color=WHITE, fill_color=BLACK, fill_opacity=1
        )
        for i in range(0, 7):
            reglakf[0][i].set_color(ORANGE)
        t_9 = TextMobject(
            """Por último, al tomar el producto punto de """,
            """$f$""",
            """ y """,
            """$g$""",
            """, la función \n
                            resultante es también """,
            """continua""",
            """ en """,
            """$t_0$""",
        )
        t_9.set_color_by_tex_to_color_map(
            {
                """$f$""": RED,
                """$g$""": TEAL_D,
                """continua""": BLUE,
                """$t_0$""": YELLOW,
            }
        )
        reglafpuntog = (
            TextMobject("""$(f\cdot g)(t)$""", """$=2t^2+t\cos(5t)+t\sin(5t)$""")
            .scale(0.85)
            .to_corner(LEFT + UP)
        )
        reglafpuntog.set_color_by_tex_to_color_map({"""$(f\cdot g)(t)$""": GREEN_D})
        reglafpuntog.bg = SurroundingRectangle(
            reglafpuntog, color=WHITE, fill_color=BLACK, fill_opacity=1
        )

        # Ejes en 3D
        axis_config = {
            "x_min": -6,
            "x_max": 6,
            "y_min": -6,
            "y_max": 6,
            "z_min": -6,
            "z_max": 6,
        }
        ejes = ThreeDAxes(**axis_config)
        # Ejes en 2D
        ejes2 = Axes(x_min=-6, x_max=6, y_min=-3.5, y_max=3.5)
        # Funciones que se van a utilizar
        tmin = -6
        tmax = 6
        f = ParametricFunction(
            self.helicoide, t_min=tmin, t_max=tmax, color=RED
        ).set_shade_in_3d(True)
        g = ParametricFunction(
            self.identidad, t_min=tmin, t_max=tmax, color=TEAL_D
        ).set_shade_in_3d(True)
        fmasg = ParametricFunction(
            self.func_suma, t_min=tmin, t_max=tmax, color=PINK
        ).set_shade_in_3d(True)
        kf = ParametricFunction(
            self.func_por_escalar, t_min=tmin, t_max=tmax, color=ORANGE
        ).set_shade_in_3d(True)
        fpuntog = ParametricFunction(
            self.func_prod_int, t_min=-1.3, t_max=1.3, color=GREEN_D
        ).set_shade_in_3d(True)
        dot1 = Dot(point=(0, 1, 0), color=YELLOW, radius=0.1)
        dot2 = Dot(point=(0, 0, 0), color=YELLOW, radius=0.1)
        dot3 = Dot(point=(0, 1, 0), color=YELLOW, radius=0.1)
        dot4 = Dot(point=(0, k, 0), color=YELLOW, radius=0.1)
        dot5 = Dot(point=(0, 0, 0), color=YELLOW, radius=0.1)
        ### Grupos ###
        Group1 = VGroup(t_1, t_2, t_3, t_4, Nota)
        ### Animación ###
        self.play(Write(title))
        self.wait()
        self.play(FadeOutAndShiftDown(title))
        self.play(Write(t_1))
        self.wait(8)
        self.play(Write(t_2))
        self.wait(3)
        self.play(Write(t_3))
        self.wait(3.25)
        self.play(Write(t_4))
        self.wait(3.25)
        self.play(Write(Nota))
        self.wait(2.75)
        self.play(FadeOut(Group1))
        self.play(Write(t_5))
        self.wait(2)
        self.play(FadeOut(t_5))

        self.set_camera_orientation(phi=115 * DEGREES, theta=-65 * DEGREES)
        self.play(ShowCreation(ejes))
        self.begin_ambient_camera_rotation(rate=0.07)
        self.acomodar_textos(reglaf.bg)
        self.acomodar_textos(reglaf)
        self.add_foreground_mobjects(reglaf.bg)
        self.add_foreground_mobjects(reglaf)
        self.play(ShowCreation(f), run_time=2)
        self.wait(2.5)
        self.play(FadeOut(reglaf), FadeOut(reglaf.bg))
        self.remove_foreground_mobjects(reglaf.bg)
        self.remove_foreground_mobjects(reglaf)
        self.acomodar_textos(reglag.bg)
        self.acomodar_textos(reglag)
        self.add_foreground_mobjects(reglag.bg)
        self.add_foreground_mobjects(reglag)
        self.play(ShowCreation(g), run_time=2)
        self.wait(2.5)
        self.play(FadeOut(reglag), FadeOut(reglag.bg))
        self.remove_foreground_mobjects(reglag.bg)
        self.remove_foreground_mobjects(reglag)
        self.acomodar_textos(t_6.bg)
        self.acomodar_textos(t_6)
        self.add_foreground_mobjects(t_6.bg)
        self.add_foreground_mobjects(t_6)
        self.add(dot1, dot2)
        self.wait(4.5)
        self.remove(dot1, dot2)
        self.play(FadeOut(f), FadeOut(g), FadeOut(t_6), FadeOut(t_6.bg))
        self.remove_foreground_mobjects(t_6.bg)
        self.remove_foreground_mobjects(t_6)
        self.acomodar_textos(t_7.bg)
        self.acomodar_textos(t_7)
        self.add_foreground_mobjects(t_7.bg)
        self.add_foreground_mobjects(t_7)
        self.wait(4.5)
        self.play(FadeOut(t_7), FadeOut(t_7.bg))
        self.remove_foreground_mobjects(t_7.bg)
        self.remove_foreground_mobjects(t_7)
        self.acomodar_textos(reglafmasg.bg)
        self.acomodar_textos(reglafmasg)
        self.add_foreground_mobjects(reglafmasg.bg)
        self.add_foreground_mobjects(reglafmasg)
        self.play(ShowCreation(fmasg), run_time=2)
        self.add(dot3)
        self.wait(6)
        self.remove(dot3)
        self.play(FadeOut(fmasg), FadeOut(reglafmasg), FadeOut(reglafmasg.bg))
        self.remove_foreground_mobjects(reglafmasg.bg)
        self.remove_foreground_mobjects(reglafmasg)
        self.acomodar_textos(t_8.bg)
        self.acomodar_textos(t_8)
        self.add_foreground_mobjects(t_8.bg)
        self.add_foreground_mobjects(t_8)
        self.wait(4.5)
        self.play(FadeOut(t_8), FadeOut(t_8.bg))
        self.remove_foreground_mobjects(t_8.bg)
        self.remove_foreground_mobjects(t_8)
        self.acomodar_textos(reglakf.bg)
        self.acomodar_textos(reglakf)
        self.add_foreground_mobjects(reglakf.bg)
        self.add_foreground_mobjects(reglakf)
        self.play(ShowCreation(kf), run_time=2)
        self.add(dot4)
        self.wait(2)
        self.remove(dot4)
        self.play(FadeOut(reglakf.bg), FadeOut(reglakf), FadeOut(kf), FadeOut(ejes))
        self.remove_foreground_mobjects(reglakf.bg)
        self.remove_foreground_mobjects(reglakf)
        self.stop_ambient_camera_rotation()
        self.set_camera_orientation(phi=0, theta=-90 * DEGREES)
        self.play(Write(t_9))
        self.wait(8)
        self.play(FadeOutAndShiftDown(t_9))
        self.play(ShowCreation(ejes2))
        self.play(FadeIn(reglafpuntog.bg))
        self.play(Write(reglafpuntog))
        self.add_foreground_mobjects(reglafpuntog.bg)
        self.add_foreground_mobjects(reglafpuntog)
        self.play(ShowCreation(fpuntog))
        self.add(dot5)
        self.wait(4)
        self.play(
            FadeOut(ejes2), FadeOut(reglafpuntog), FadeOut(fpuntog), FadeOut(dot5)
        )
        self.remove_foreground_mobjects(reglafpuntog.bg)
        self.remove_foreground_mobjects(reglafpuntog)


class Continuidad_con_sucesiones(ThreeDScene):
    def acomodar_textos(self, objeto):
        self.add_fixed_in_frame_mobjects(objeto)
        self.play(Write(objeto))

    def acomodar_puntos(self, objeto):
        self.add_fixed_in_frame_mobjects(objeto)
        self.add(objeto)

    # Definimos las funciones a utilizar (las que vamos a graficar)
    # Puedes cambiar estas funciones con las que se te ocurra
    # Son funciones de R  a R2, y estamos obteniendo sus gráficas
    # por lo que la primer entrada siempre debe ser lo que parametriza
    # la función, es decir, la variable independiente

    def helicoide(self, t):
        return [t, np.cos(4 * t), np.sin(4 * t)]  # f(t)=(cos(4t),sin(4t))

    def func_suma(self, t):
        return [t, t + np.cos(4 * t), t + np.sin(4 * t)]  # g(t)=(t+cos(4t),t+sin(4t))

    def contra1(self, t):
        return [t, 1, 1]  # h(t)=(1,1)

    def contra2(self, t):
        return [t, -1, -1]  # u(t)=(-1,-1)

    def construct(self):
        # Textos
        t_1 = TextMobject("""Continuidad en Curvas con Sucesiones""").scale(1.5)
        t_2 = TextMobject(
            """Recuerda que una posible definición de """,
            """continuidad""",
            """ es: \n
                            $f:\\mathbb{R}\\to\\mathbb{R}^2$ es """,
            """continua""",
            """ en $t_0$ si""",
        ).shift(1 * UP)
        t_2.set_color_by_tex_to_color_map(
            {"""continuidad""": BLUE, """continua""": BLUE}
        )
        t_3 = TexMobject(r"\lim_{t\to t_0}f(t)=f(t_0)").next_to(t_2, DOWN)
        t_4 = TextMobject(
            """Aquí utilizaremos una equivalencia con """, """sucesiones""", """:"""
        )
        t_4.set_color_by_tex_to_color_map({"""sucesiones""": PURPLE_B})
        t_4_1 = TextMobject(
            """$f:\\mathbb{R}\\to\\mathbb{R}^2$ es """,
            """continua""",
            """ en $t_0$ \n
                            $\\Leftrightarrow \\forall\\{x_n\\}\\subset\\mathbb{R}$ """,
            """sucesión""",
            """ tal que""",
        ).shift(1 * UP)
        t_4_1.set_color_by_tex_to_color_map(
            {"""sucesión""": PURPLE_B, """continua""": BLUE}
        )
        t_5 = TexMobject(
            r"\lim_{n\to\infty}x_n=t_0,\\\\ \lim_{n\to\infty}f(x_n)=f(t_0)"
        ).next_to(t_4_1, DOWN)
        t_6 = TextMobject("""Veamos un par de ejemplos...""")
        nota = (
            TextMobject(
                """NOTA: Aquí ejemplificaremos usando solo una sucesión, puedes probar con \n
                            otras sucesiones modificando el código correspondiente."""
            )
            .scale(0.5)
            .shift(3.5 * DOWN)
        )
        t_7 = (
            TextMobject("""Considera $t_0=0$""")
            .scale(0.7)
            .to_corner(LEFT + UP)
            .shift(1 * RIGHT)
        )
        t_7.bg = SurroundingRectangle(
            t_7, color=WHITE, fill_color=BLACK, fill_opacity=0.5
        )
        reglaf = (
            TextMobject("""$f(t)$""", """$=(\cos(4t),\sin(4t))$""")
            .scale(0.7)
            .align_to(t_7, LEFT)
            .shift(2.7 * UP)
            .shift(0.5 * LEFT)
        )
        reglaf.set_color_by_tex_to_color_map({"""$f(t)$""": RED})
        reglaf.bg = SurroundingRectangle(
            reglaf, color=WHITE, fill_color=BLACK, fill_opacity=0.5
        )
        reglaf.group = VGroup(reglaf, reglaf.bg)
        t_8 = (
            TextMobject(
                """Toma la """, """sucesión """, """$X_n$""", """$=\\dfrac{3}{n}$"""
            )
            .scale(0.7)
            .to_corner(RIGHT + DOWN)
            .shift(2.5 * UP)
            .shift(1.5 * LEFT)
        )
        t_8.set_color_by_tex_to_color_map({"""$X_n$""": YELLOW})
        t_8.bg = SurroundingRectangle(
            t_8, color=WHITE, fill_color=BLACK, fill_opacity=0.5
        )
        t_8.group = VGroup(t_8, t_8.bg)
        # t_9 = TextMobject('''Converge a 0, su imagen a $(1,0)$ \n
        #                    y su gráfica a $(0,1,0)$''').scale(0.7).next_to(t_8.bg,DOWN)
        t_9 = (
            TextMobject(
                """$\\lim_{n \\to \\infty} $""",
                """$X_n$""",
                """$ = 0$ \\\\
                                $\\lim_{n \\to \\infty} f(X_n) = (1,0)$ \\\\
                                $\\lim_{n \\to \\infty} (X_n,f(X_n)) = (0,1,0)$""",
            )
            .scale(0.7)
            .next_to(t_8.bg, DOWN)
        )
        t_9[1].set_color(YELLOW)
        reglag = (
            TextMobject("""$g(t)$""", """$=(t+\cos(4t),t+\sin(4t))$""")
            .scale(0.7)
            .align_to(t_7, LEFT)
            .shift(2.7 * UP)
            .shift(1 * LEFT)
        )
        t_9.bg = SurroundingRectangle(
            t_9, color=WHITE, fill_color=BLACK, fill_opacity=0.5
        )
        t_9.group = VGroup(t_9, t_9.bg)
        reglag.set_color_by_tex_to_color_map({"""$g(t)$""": BLUE})
        reglag.bg = SurroundingRectangle(
            reglag, color=WHITE, fill_color=BLACK, fill_opacity=0.5
        )
        t_10 = (
            TextMobject("""¿Y cómo sería una función """, """discontinua?""")
            .scale(0.7)
            .to_corner(LEFT + UP)
        )
        t_10.bg = SurroundingRectangle(
            t_10, color=WHITE, fill_color=BLACK, fill_opacity=0.5
        )
        t_10.group = VGroup(t_10, t_10.bg)
        t_10.set_color_by_tex_to_color_map({"""discontinua""": GREEN_D})
        # reglacontra1_tex = ["(1,1)",",","t\\leq 0"]
        reglacontra1_tex = ["(1,1),", "t\\leq 0"]
        reglacontra2_tex = ["(-1,-1)", ",", "t>0"]
        reglacontra1_mob = TexMobject(*reglacontra1_tex)
        reglacontra2_mob = TexMobject(*reglacontra2_tex)
        for i, item in enumerate(reglacontra1_mob):
            item.align_to(reglacontra2_mob[i], LEFT)
        reglacontra1 = VGroup(*reglacontra1_mob)
        reglacontra2 = VGroup(*reglacontra2_mob).shift(DOWN)
        reglacontra = VGroup(reglacontra1, reglacontra2)
        brace = Brace(reglacontra, LEFT)
        h = brace.get_text("$h(x)$", "$=$")
        h.set_color_by_tex_to_color_map({"$h(x)$": ORANGE})
        reglacompleta = (
            VGroup(reglacontra, brace, h)
            .scale(0.7)
            .next_to(t_7.bg, DOWN)
            .align_to(t_7, LEFT)
        )
        reglacompleta.bg = SurroundingRectangle(
            reglacompleta, color=WHITE, fill_color=BLACK, fill_opacity=0.5
        )
        t_11 = (
            TextMobject(
                """Toma las """,
                """sucesiones """,
                """$X_n$""",
                """$=\\dfrac{3}{n}$ y \n
                            """,
                """$Y_n$""",
                """$=-\\dfrac{3}{n}$""",
            )
            .scale(0.7)
            .to_corner(RIGHT + UP)
        )
        t_11.bg = SurroundingRectangle(
            t_11, color=WHITE, fill_color=BLACK, fill_opacity=0.5
        )
        t_11.set_color_by_tex_to_color_map({"""$X_n$""": YELLOW, """$Y_n$""": YELLOW})
        # t_12 = TextMobject('''$X_n$''',''' converge a 0, su imagen a $(-1,-1)$ \n
        #                    y su gráfica a $(0,-1,-1)$''').scale(0.7).to_corner(RIGHT+DOWN).shift(2*UP)
        t_12 = (
            TextMobject(
                """$\\lim_{n \\to \\infty} $""",
                """$X_n$""",
                """$ = 0$ \\\\
                                $\\lim_{n \\to \\infty} f(X_n) = (-1,-1)$ \\\\
                                $\\lim_{n \\to \\infty} (X_n,f(X_n)) = (0,-1,-1)$""",
            )
            .scale(0.7)
            .to_corner(RIGHT + DOWN)
            .shift(2 * UP)
        )
        t_12[1].set_color(YELLOW)
        t_12.bg = SurroundingRectangle(
            t_12, color=WHITE, fill_color=BLACK, fill_opacity=0.5
        )
        # t_12.set_color_by_tex_to_color_map({
        #    '''$X_n$''': YELLOW
        #    })
        # t_13 = TextMobject('''$Y_n$''',''' converge a 0, su imagen a $(1,1)$ \n
        #                    y su gráfica a $(0,1,1)$''').scale(0.7).next_to(t_12.bg,DOWN)
        t_13 = (
            TextMobject(
                """$\\lim_{n \\to \\infty} $""",
                """$Y_n$""",
                """$ = 0$ \\\\
                                $\\lim_{n \\to \\infty} f(Y_n) = (1,1)$ \\\\
                                $\\lim_{n \\to \\infty} (Y_n,f(Y_n)) = (0,1,1)$""",
            )
            .scale(0.7)
            .next_to(t_12.bg, DOWN)
        )
        t_13.bg = SurroundingRectangle(
            t_13, color=WHITE, fill_color=BLACK, fill_opacity=0.5
        )
        t_13.set_color_by_tex_to_color_map({"""$Y_n$""": YELLOW})
        t_13.group = VGroup(t_13, t_13.bg)
        t_14 = (
            TextMobject(
                """Tenemos entonces dos """,
                """sucesiones""",
                """ \\\\ 
                            que convergen a $t_0$ cuyas """,
                """sucesiones""",
                """ \\\\ 
                            de imágenes convergen a cosas distintas.\\\\
                            Concluimos que la función \\\\ 
                            es """,
                """discontinua""",
                """ en $t_0$.""",
            )
            .scale(0.7)
            .to_corner(RIGHT + DOWN)
            .shift(1 * UP)
        )
        t_14.bg = SurroundingRectangle(
            t_14, color=WHITE, fill_color=BLACK, fill_opacity=0.5
        )
        t_14.set_color_by_tex_to_color_map(
            {"""discontinua""": GREEN_D, """sucesiones""": PURPLE_B}
        )
        t_14.group = VGroup(t_14, t_14.bg)

        # Ejes en 3D
        axis_config = {
            "x_min": -6,
            "x_max": 6,
            "y_min": -6,
            "y_max": 6,
            "z_min": -6,
            "z_max": 6,
        }
        ejes = ThreeDAxes(**axis_config)

        # Funciones que se van a utilizar
        tmin = -6
        tmax = 6
        f = ParametricFunction(
            self.helicoide, t_min=tmin, t_max=tmax, color=RED
        ).set_shade_in_3d(True)
        g = ParametricFunction(
            self.func_suma, t_min=tmin, t_max=tmax, color=BLUE
        ).set_shade_in_3d(True)
        contra_1 = ParametricFunction(
            self.contra1, t_min=tmin, t_max=0, color=ORANGE
        ).set_shade_in_3d(True)
        contra_2 = ParametricFunction(
            self.contra2, t_min=0.001, t_max=tmax, color=ORANGE
        ).set_shade_in_3d(True)

        # Sucesiones
        X = []
        Y = []
        Z = []
        W = []
        for n in range(1, 101):
            x_n = Dot(color=YELLOW, point=(3 / n, np.cos(4 * 3 / n), np.sin(4 * 3 / n)))
            X.append(x_n)
            y_n = Dot(
                color=YELLOW,
                point=(3 / n, 3 / n + np.cos(4 * 3 / n), 3 / n + np.sin(4 * 3 / n)),
            )
            Y.append(y_n)
            z_n = Dot(color=YELLOW, point=(3 / n, -1, -1))
            Z.append(z_n)
            w_n = Dot(color=YELLOW, point=(-3 / n, 1, 1))
            W.append(w_n)
        suce1 = VGroup(*X)
        suce2 = VGroup(*Y)
        suce3 = VGroup(*Z)
        suce4 = VGroup(*W)

        # Grupos útiles
        Grupo1 = VGroup(t_2, t_3)
        Grupo1_1 = VGroup(t_4)
        Grupo2 = VGroup(t_4_1, t_5)
        Grupo3 = VGroup(t_8, t_9, t_8.bg, t_9.bg)
        Grupo4 = VGroup(t_6, nota)
        Grupo5 = VGroup(t_11, t_12, t_11.bg, t_12.bg, t_13, t_13.bg)
        Grupo6 = VGroup(
            t_7,
            t_7.bg,
            reglacompleta,
            reglacompleta.bg,
            contra_1,
            contra_2,
            t_14,
            t_14.bg,
            suce3,
            suce4,
            ejes,
        )

        # Animación

        self.play(Write(t_1))
        self.wait()
        self.play(FadeOutAndShiftDown(t_1))
        self.play(Write(Grupo1))
        self.wait(10)
        self.play(ReplacementTransform(Grupo1, Grupo1_1))
        self.wait(2.5)
        self.play(ReplacementTransform(Grupo1_1, Grupo2))
        self.wait(10)
        self.play(FadeOut(Grupo2))
        self.play(Write(Grupo4))
        self.wait(3)
        self.play(FadeOutAndShiftDown(Grupo4))

        self.set_camera_orientation(phi=115 * DEGREES, theta=-65 * DEGREES)
        self.play(ShowCreation(ejes))
        self.acomodar_textos(t_7.bg)
        self.acomodar_textos(t_7)
        self.add_foreground_mobjects(t_7.bg)
        self.add_foreground_mobjects(t_7)
        self.wait(2)
        self.begin_ambient_camera_rotation(rate=0.07)

        self.acomodar_textos(reglaf.bg)
        self.acomodar_textos(reglaf)
        self.add_foreground_mobjects(reglaf.bg)
        self.add_foreground_mobjects(reglaf)
        self.play(ShowCreation(f), run_time=2)
        self.wait(2.5)
        self.acomodar_textos(t_8.bg)
        self.acomodar_textos(t_8)
        self.add_foreground_mobjects(t_8.bg)
        self.add_foreground_mobjects(t_8)
        self.play(Write(suce1), run_time=3)
        self.wait(2)
        self.acomodar_textos(t_9.bg)
        self.acomodar_textos(t_9)
        self.add_foreground_mobjects(t_9.bg)
        self.add_foreground_mobjects(t_9)
        self.wait(10)
        self.remove_foreground_mobjects(reglaf.bg)
        self.remove_foreground_mobjects(reglaf)
        self.remove_foreground_mobjects(t_8.bg)
        self.remove_foreground_mobjects(t_8)
        self.remove_foreground_mobjects(t_9.bg)
        self.remove_foreground_mobjects(t_9)
        self.play(
            FadeOut(suce1),
            FadeOut(reglaf.group),
            FadeOut(f),
            FadeOut(Grupo3),
            FadeOut(t_8.group),
            FadeOut(t_9.group),
        )

        self.acomodar_textos(reglag.bg)
        self.acomodar_textos(reglag)
        self.add_foreground_mobjects(reglag.bg)
        self.add_foreground_mobjects(reglag)
        self.play(ShowCreation(g), run_time=2)
        self.wait(4)
        self.acomodar_textos(t_8.bg)
        self.acomodar_textos(t_8)
        self.play(Write(suce2), run_time=3)
        self.wait(2)
        self.acomodar_textos(t_9.bg)
        self.acomodar_textos(t_9)
        self.wait(10)
        self.remove_foreground_mobjects(reglag.bg)
        self.remove_foreground_mobjects(reglag)
        self.remove_foreground_mobjects(t_7.bg)
        self.remove_foreground_mobjects(t_7)
        self.remove_foreground_mobjects(t_8.bg)
        self.remove_foreground_mobjects(t_8)
        self.remove_foreground_mobjects(t_9.bg)
        self.remove_foreground_mobjects(t_9)
        self.play(
            FadeOut(suce2),
            FadeOut(reglag),
            FadeOut(g),
            FadeOut(reglag.bg),
            FadeOut(Grupo3),
            FadeOut(t_7),
            FadeOut(t_7.bg),
        )

        self.acomodar_textos(t_10.bg)
        self.acomodar_textos(t_10)
        self.add_foreground_mobjects(t_10.bg)
        self.add_foreground_mobjects(t_10)
        self.wait(2.5)
        self.play(FadeOut(t_10), FadeOut(t_10.bg))
        self.remove_foreground_mobjects(t_10.bg)
        self.remove_foreground_mobjects(t_10)
        self.acomodar_textos(t_7.bg)
        self.acomodar_textos(t_7)
        self.add_foreground_mobjects(t_7.bg)
        self.add_foreground_mobjects(t_7)
        self.wait(2)
        self.acomodar_textos(reglacompleta.bg)
        self.acomodar_textos(reglacompleta)
        self.add_foreground_mobjects(reglacompleta.bg)
        self.add_foreground_mobjects(reglacompleta)
        self.wait(9)
        self.play(ShowCreation(contra_1), ShowCreation(contra_2), run_time=2)
        self.acomodar_textos(t_11.bg)
        self.acomodar_textos(t_11)
        self.add_foreground_mobjects(t_11.bg)
        self.add_foreground_mobjects(t_11)
        self.wait(5)
        self.play(Write(suce3), Write(suce4))
        self.wait()
        self.acomodar_textos(t_12.bg)
        self.acomodar_textos(t_12)
        self.add_foreground_mobjects(t_12.bg)
        self.add_foreground_mobjects(t_12)
        self.wait(10)
        self.acomodar_textos(t_13.bg)
        self.acomodar_textos(t_13)
        self.add_foreground_mobjects(t_13.bg)
        self.add_foreground_mobjects(t_13)
        self.wait(10)
        self.remove_foreground_mobjects(t_11.bg)
        self.remove_foreground_mobjects(t_11)
        self.remove_foreground_mobjects(t_12.bg)
        self.remove_foreground_mobjects(t_12)
        self.remove_foreground_mobjects(t_13.bg)
        self.remove_foreground_mobjects(t_13)
        self.remove_foreground_mobject(Grupo5)
        self.play(FadeOut(Grupo5))
        self.acomodar_textos(t_14.bg)
        self.acomodar_textos(t_14)
        self.add_foreground_mobjects(t_14.bg)
        self.add_foreground_mobjects(t_14)
        self.wait(9)
        self.remove_foreground_mobjects(t_14.bg)
        self.remove_foreground_mobjects(t_14)
        self.remove_foreground_mobjects(t_7.bg)
        self.remove_foreground_mobjects(t_7)
        self.remove_foreground_mobjects(reglacompleta.bg)
        self.remove_foreground_mobjects(reglacompleta)
        self.play(FadeOut(Grupo6))
        self.wait(3)

        self.stop_ambient_camera_rotation()


#### Función proyección
class Proyeccion(ThreeDScene):
    def acomodar_textos(self, objeto):
        self.add_fixed_in_frame_mobjects(objeto)
        self.play(Write(objeto))

    def construct(self):
        grid = NumberPlane()

        # X1,X2,X3,Y1,Y2,Y3 PUEDEN MODIFICARSE PARA PROBAR CON OTROS VECTORES
        x1 = 0
        x2 = 3
        x3 = 0

        y1 = 1
        y2 = 1
        y3 = 2

        Vx = Arrow((0, 0, 0), x1 * RIGHT + x2 * UP, buff=0, color=BLUE_C)
        Vxlabel = TexMobject("\\vec{x}").set_color(BLUE_C)
        Vxlabel.move_to(Vx.get_end() + 0.5 * LEFT)
        Vy = Arrow((0, 0, 0), y1 * RIGHT + y2 * UP, buff=0, color=YELLOW_C)
        Vylabel = TexMobject("\\vec{y}").set_color(YELLOW_C)
        Vy1 = Vy.copy()
        Vylabel.move_to(Vy.get_end() + 0.5 * RIGHT - 0.3 * UP)
        escalar = ((x1 * y1) + (x2 * y2)) / ((y1 * y1) + (y2 * y2))
        vec = Arrow(
            (0, 0, 0),
            (y1 * escalar) * RIGHT + (y2 * escalar) * UP,
            buff=0,
            color=PURPLE_B,
        )
        veclabel = TexMobject("\\vec{z}").set_color(PURPLE_B)
        veclabel.move_to(vec.get_end() + 0.5 * LEFT)
        linea = DashedLine(
            (y1 * escalar, y2 * escalar, 0),
            (x1, x2, 0),
            dash_length=0.1,
            positive_space_ratio=0.5,
            stroke_width=3,
            color="#88FF00",
        )

        escalar1 = ((x1 * y1) + (x2 * y2)) / ((x1 * x1) + (x2 * x2))
        vec1 = Arrow(
            (0, 0, 0), (x1 * escalar1) * RIGHT + (x2 * escalar1) * UP, buff=0, color=RED
        )
        linea1 = DashedLine(
            (x1 * escalar1, x2 * escalar1, 0),
            (y1, y2, 0),
            dash_length=0.1,
            positive_space_ratio=0.5,
            stroke_width=3,
            color=WHITE,
        )

        titulo = TextMobject("Vector Proyección").scale(1.5)
        text = TextMobject(
            """Tomemos dos vectores en \\\\ 
                            el plano cartesiano"""
        )
        text.bg = SurroundingRectangle(
            text, color=WHITE, fill_color=BLACK, fill_opacity=1
        )
        text.group = VGroup(text.bg, text).shift(2 * DOWN + 3 * LEFT)
        text1 = TextMobject(
            """Podemos representar geométricamente\n
                            la proyección de""",
            """ $\\vec{x}$""",
            """ sobre""",
            """ $\\vec{y}$""",
            """ como""",
            """ $\\vec{z}$""",
        ).move_to(text.get_center() + 1 * RIGHT)
        text1.bg = SurroundingRectangle(
            text1, color=WHITE, fill_color=BLACK, fill_opacity=1
        )
        text1.group = VGroup(text1.bg, text1).move_to(text.get_center() + 1 * RIGHT)
        text1[1].set_color(BLUE_C)
        text1[3].set_color(YELLOW_C)
        text1[5].set_color(PURPLE_B)

        text2 = TextMobject(
            """Notemos que con la sombra de """,
            """$\\vec{x}$""",
            """ sobre la recta que \n
                            genera """,
            """$\\vec{y}$""",
            """ obtenemos el """,
            """vector proyección""",
            """.""",
        )
        text2[1].set_color(BLUE_C)
        text2[3].set_color(YELLOW)
        text2[5].set_color(PURPLE_C)
        text2.bg = SurroundingRectangle(
            text2, color=WHITE, fill_color=BLACK, fill_opacity=1
        )
        text2.group = VGroup(text2.bg, text2)
        text2.group.move_to(2 * DOWN)
        text3 = TextMobject(
            """Además de que la """,
            """proyección de $\\vec{y}$ sobre $\\vec{x} $""",
            """ \\\\
                            es diferente a la """,
            """proyección de $\\vec{x}$ sobre $\\vec{y}$""",
        )
        text3.bg = SurroundingRectangle(
            text3, color=WHITE, fill_color=BLACK, fill_opacity=1
        )
        text3.group = VGroup(text3.bg, text3)
        text3.group.move_to(-2 * UP)
        text3[1].set_color(RED)
        text3[3].set_color(PURPLE_B)
        Def = TextMobject(
            """La """,
            """proyección""",
            """ de """,
            """$\\vec{x}$""",
            """ sobre\n
                            """,
            """$\\vec{y}$""",
            """ se define como:""",
        )  # Revisar que este bien dicho
        Def[1].set_color(GREEN_D)
        Def[3].set_color(BLUE)
        Def[5].set_color(YELLOW)
        Def_copy = Def.copy()
        Def_copy.move_to(2.5 * UP)
        Def1 = TextMobject(
            """$Proy_{\\vec{y}}(\\vec{x}):=\\frac{\\vec{x}\\cdot\\vec{y}}{\\vec{y}\\cdot\\vec{y}} \\vec{y}$"""
        )
        Def1[0][0].set_color(GREEN_D)
        Def1[0][1].set_color(GREEN_D)
        Def1[0][2].set_color(GREEN_D)
        Def1[0][3].set_color(GREEN_D)
        Def1_1 = Def1.copy().move_to(2.5 * UP)
        text4 = TextMobject(
            """Veamos un último ejemplo, agregándole una coordenada \n
                                en """,
            """z""",
            """ a los vectores anteriores""",
        )
        text4[1].set_color(PURPLE_B)

        # Animacion2d
        self.play(Write(titulo))
        self.wait()
        self.play(FadeOut(titulo))
        self.play(Write(grid))
        self.wait()
        self.play(Write(text.group))
        self.play(ShowCreation(Vx), Write(Vxlabel))
        self.play(ShowCreation(Vy), Write(Vylabel))
        self.wait(2)
        self.play(ReplacementTransform(text.group, text1.group))
        self.wait()
        self.play(ShowCreation(linea))
        self.wait(2)
        self.play(ShowCreation(vec), Write(veclabel))
        self.wait()
        self.play(ReplacementTransform(text1.group, text2.group))
        self.wait(7)
        self.play(ReplacementTransform(text2.group, text3.group))
        self.play(ReplacementTransform(linea, linea1), FadeIn(Vy1))
        self.play(ShowCreation(vec1))
        self.wait(2)
        self.play(
            FadeOut(Vx),
            FadeOut(Vy),
            FadeOut(linea1),
            FadeOut(Vxlabel),
            FadeOut(Vylabel),
            FadeOut(veclabel),
            FadeOut(Vy1),
        )
        self.wait()
        self.play(FadeOut(grid), FadeOut(text3.group), FadeOut(vec), FadeOut(vec1))
        self.wait()
        self.play(Write(Def))
        self.wait(3)
        self.play(ReplacementTransform(Def, Def_copy))
        self.play(Write(Def1))
        self.wait(3.5)
        self.play(FadeOut(Def_copy))
        self.wait()
        self.play(ReplacementTransform(Def1, Def1_1))
        self.play(Write(text4))
        self.wait(5)
        self.play(FadeOut(text4), FadeOut(Def1_1))
        self.wait()

        # CÓDIGO PARA LA ANIMACION 3D
        axes = ThreeDAxes()

        Vx3d = Arrow((0, 0, 0), x1 * RIGHT + x2 * UP + x3 * OUT, buff=0, color=BLUE)
        Vx3dlabel = TexMobject("\\vec{x}", color=BLUE_C)
        Vx3dlabel.move_to(3 * UP + 5 * LEFT)
        # Vy3d=Arrow((0, 0, 0), y1 * RIGHT + y2*UP+y3*OUT,buff=0,color=YELLOW)
        Vy3d = Line((0, 0, 0), y1 * RIGHT + y2 * UP + y3 * OUT, buff=0, color=YELLOW)

        Vy3da = ArrowTip(start_angle=Vy3d.get_angle(), color=YELLOW).move_to(
            y1 * RIGHT + y2 * UP + y3 * OUT
        )

        Vy3d.group = VGroup(Vy3d, Vy3da)

        Vy3dlabel = TexMobject("\\vec{y}", color=YELLOW)
        Vy3dlabel.move_to(2.5 * UP + 5 * LEFT)
        Plabel = TextMobject(
            """Proyección""",
            """ de $\\vec{y}$ \n
                            sobre $\\vec{x}$""",
        ).shift(0.25 * DOWN)
        Plabel[0].set_color(RED)
        Plabel.move_to(1.7 * UP + 5 * LEFT)
        escalar3d = ((x1 * y1) + (x2 * y2) + (x3 * y3)) / (
            (x1 * x1) + (x2 * x2) + (x3 * x3)
        )
        vec3d = Arrow(
            (0, 0, 0),
            (x1 * escalar3d) * RIGHT + (x2 * escalar3d) * UP + ((x3 * escalar3d)) * OUT,
            buff=0,
            color=RED,
        )
        linea3d = DashedLine(
            (y1, y2, y3),
            (x1 * escalar3d, x2 * escalar3d, x3 * escalar3d),
            dash_length=0.1,
            positive_space_ratio=0.5,
            stroke_width=3,
            color="#88FF00",
        )
        text5 = TextMobject(
            """Modifica el código para probar con nuevos vectores \n
                             y perspectivas en la animación en $\\mathbb{R}^{3}$"""
        )

        # Se puede cambiar la siguiente linea para modificar la posición de la camara
        self.set_camera_orientation(phi=80 * DEGREES, theta=45 * DEGREES, distance=6)
        self.play(ShowCreation(axes))
        self.play(ShowCreation(Vx3d), run_time=0.75)
        self.acomodar_textos(Vx3dlabel)
        # self.add_fixed_in_frame_mobjects(Vx3dlabel)
        self.play(ShowCreation(Vy3d.group), run_time=0.75)
        self.acomodar_textos(Vy3dlabel)
        # self.add_fixed_in_frame_mobjects(Vy3dlabel)
        self.play(ShowCreation(linea3d))
        self.play(ShowCreation(vec3d))
        self.acomodar_textos(Plabel)
        # self.add_fixed_in_frame_mobjects(Plabel)
        # inicia movimiento de la camara, se puede cambiar la velocidad con rate
        self.begin_ambient_camera_rotation(rate=0.5)
        self.wait(4)
        self.play(
            FadeOut(axes),
            FadeOut(Vy3d.group),
            FadeOut(Vx3d),
            FadeOut(Vy3dlabel),
            FadeOut(Vx3dlabel),
            FadeOut(Plabel),
            FadeOut(vec3d),
            FadeOut(linea3d),
        )
        self.add_fixed_in_frame_mobjects(text5)

        self.wait(2)
        self.play(FadeOut(text5))


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
            """Existencia del límite de funciones de \n
            $\\mathbb{R}^{n}\\rightarrow\\mathbb{R}^{m}$"""
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


class Limites_Al_Infinito(ThreeDScene):
    def cur_1(self, t):
        return np.array([t, t * np.sin(5 * t), -np.exp(t / 2) * np.cos(5 * t)])

    def construct(self):

        ###Texto
        titulo = TextMobject(
            """Divergencia a infinito de funciones de \n
            $\\mathbb{R}\\rightarrow\\mathbb{R}^{n}$ en infinito""",
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


class Divergencia_A_Infinito(ThreeDScene):
    def cur_1(self, t):
        return np.array([t, 1 / (1 - t), t ** 2])

    def construct(self):

        ###Texto
        titulo = TextMobject(
            """Divergencia a infinito de funciones de \n
            $\\mathbb{R}\\rightarrow\\mathbb{R}^{n}$ en un punto $t_0$"""
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


#### Limite al infinito positivo
class superficie2(ParametricSurface):
    def __init__(self, **kwargs):
        kwargs = {
            "u_min": 0.1,
            "u_max": 4,
            "v_min": 0.1,
            "v_max": 4,
            "checkerboard_colors": [BLUE_C],
        }
        ParametricSurface.__init__(self, self.func, **kwargs)

    def func(self, x, y):
        return np.array([x, (1 / (x * x * x)), (1 / (x * x * x))])


class Limites2(ThreeDScene):
    def construct(self):
        titulo2 = TextMobject(
            """Limite de funciones al infinito de \n
                                $\\mathbb{R}\\rightarrow\\mathbb{R}^{n}$"""
        )
        texto = TextMobject("""Sea $f:\\mathbb{R}\\rightarrow\\mathbb{R}^{n}$""")
        texto1 = TexMobject(
            r""" \lim_{x \to \infty}f(x)=\vec{L}\leftrightarrow\forall \ \epsilon>0"""
        )
        texto1_1 = TextMobject(
            """$\\exists \\ M\\in\\mathbb{R}$ tal que $x>M \\ \\implies ||f(x)-\\vec{L}||<\\epsilon$"""
        ).move_to(texto1.get_center() + 0.8 * DOWN)
        texto1_2 = TextMobject("""Veamos el siguiente ejemplo.""")
        texto1_3 = TextMobject(
            """$f$""",
            """$:\\mathbb{R}^{+}\\rightarrow\\mathbb{R}^{2}$ \n""",
            """$f(x)=(\\frac{1}{x^{3}},\\frac{1}{x^{3}})$""",
        )
        texto1_3[0].set_color(BLUE_C)
        texto1_3[2].set_color(BLUE_C)
        ###Animacion
        self.play(Write(titulo2.scale(1.5)))
        self.wait()
        self.play(FadeOut(titulo2))
        self.play(Write(texto))
        self.wait(4.25)
        self.play(texto.shift, 1.2 * UP, runtime=1.5)
        self.play(Write(texto1))
        self.wait(6.125)
        self.play(Write(texto1_1))
        self.wait(8)
        self.play(FadeOut(texto1), FadeOut(texto1_1), FadeOut(texto))
        self.wait()
        self.play(Write(texto1_2))
        self.wait(3.5)
        self.play(FadeOut(texto1_2))
        self.play(Write(texto1_3))
        self.wait(6.125)
        self.play(FadeOut(texto1_3))
        self.wait()
        self.custom_method()

    def custom_method(self):
        axes1 = ThreeDAxes()
        axes.add(axes.get_x_axis_label("t"))
        surface2 = superficie2()
        texto2 = TextMobject("""Tomemos""", """  $\\epsilon$=0.8""")
        texto2[1].set_color(RED)
        texto2.to_corner(UL)

        texto3 = TextMobject(
            """Los puntos dentro del círculo en el plano\n
                                yz están a una distancia 0.8 del $\\vec{0}$\n
                                del plano yz."""
        )
        texto3.to_corner(UL)
        texto4 = TextMobject(
            """Veamos que hay un punto \n 
            en x desde el cual """,
            """$f(x)$""",
            """ esta a una distancia menor  \n
             de """,
            """$\\epsilon$""",
            """ del 0 del plano yz.""",
        )
        texto4[1].set_color(BLUE_C)
        texto4[3].set_color(RED)
        texto4.to_corner(UL)
        texto4_1 = TextMobject(
            """Es posible hacer lo mismo \n
            con cualquier """,
            """$\\epsilon$""",
            """$>0$""",
        )
        texto4_1[1].set_color(RED)
        texto4_1.to_corner(UL)
        texto5 = TextMobject(
            """Por lo cual notaremos que \n 
            la función tiene límite cuando \n  
            $x\\rightarrow \\infty^{+}$ y es (0,0)"""
        )
        texto5.to_corner(UL)
        texto6 = TextMobject(
            """¿Se te ocurre como modificar la definición \n
                    anterior cuando el límite es a $\\infty^{-}$?"""
        )
        r = 0.8
        r1 = 0.4
        circulo = Circle(radius=r)
        circulo.rotate(PI / 2, axis=UP)
        circulo1 = Circle(radius=r1).move_to(1.8 * RIGHT)
        circulo1.rotate(PI / 2, axis=UP)

        plano = Rectangle(height=2, width=3, fill_color=YELLOW_C, fill_opacity=0.3)
        plano.move_to(0.5 * RIGHT)
        plano.rotate(PI / 2, axis=UP)

        self.set_camera_orientation(0.8 * np.pi / 2, -0.25 * np.pi, distance=10)
        self.play(ShowCreation(axes1))
        self.play(ShowCreation(surface2))
        self.wait()
        self.move_camera(phi=80 * DEGREES, theta=0)
        self.begin_ambient_camera_rotation(rate=0.001)
        self.add_fixed_in_frame_mobjects(texto2)
        self.play(Write(texto2))
        self.wait(3.5)
        self.play(ShowCreation(circulo))
        self.play(FadeOut(texto2))
        self.add_fixed_in_frame_mobjects(texto3)
        self.play(Write(texto3))
        self.wait(9.125)
        self.play(FadeOut(texto3))
        self.move_camera(phi=80 * DEGREES, theta=-PI / 8, rate=0.2)
        self.play(circulo.shift, 1.8 * RIGHT, runtime=3)
        self.add_fixed_in_frame_mobjects(texto4)
        self.play(Write(texto4))
        self.wait(9.875)
        self.play(FadeOut(texto4))
        self.add_fixed_in_frame_mobjects(texto4_1)
        self.play(Write(texto4_1))
        self.wait(5.75)
        self.play(ReplacementTransform(circulo, circulo1))
        self.play(circulo1.shift, 2 * RIGHT, runtime=3)
        self.wait()
        self.play(FadeOut(texto4_1))
        self.add_fixed_in_frame_mobjects(texto5)
        self.play(Write(texto5))
        self.wait(8.375)
        self.play(FadeOut(texto5), FadeOut(circulo1), FadeOut(axes1), FadeOut(surface2))
        self.add_fixed_in_frame_mobjects(texto6)
        self.play(Write(texto6))
        self.wait(7.625)
        self.play(FadeOut(texto6))


##############################
###########################3

######## Limite de funciones de Rn a R
# Esta clase genera la grafica en R3
class ThreeDSurface(ParametricSurface):
    def __init__(self, **kwargs):
        kwargs = {
            "u_min": 0.1,
            "u_max": 5,
            "v_min": 0.1,
            "v_max": 5,
            # "checkerboard_colors": [BLUE_D]
            # "fill_color": BLUE_D,
            "fill_opacity": 1.0,
            # "checkerboard_colors": [BLUE_D, RED_E]
            # "should_make_jagged": True
        }
        ParametricSurface.__init__(self, self.func, **kwargs)

    def func(self, x, y):
        return np.array([x, y, (1 / (x + y))])


class LimitesR2_a_R_1(ThreeDScene):
    def construct(self):

        titulo=TextMobject('''Divergencia a infinito de funciones de\n
                                $\\mathbb{R}^{n}\\rightarrow\\mathbb{R}$\n
                                en un punto $a$''')
        text=TextMobject(''' En el caso de funciones de:\n
                            $\\mathbb{R}^{n}\\rightarrow\\mathbb{R}$.''')
        text_1=TextMobject('''Donde $n\\in\\lbrace 1,2,3...\\rbrace$''').move_to(text.get_center()+1*DOWN)
        G1=VGroup(text,text_1)
        Def=TextMobject('''Sea una función $f:D\\subseteq\\mathbb{R}^{n}\\rightarrow\\mathbb{R}$''').shift(1.5*UP)
        Def1=TextMobject('''Y sea $\\vec{a}\\in D$''').shift(0.6*UP)
        Def2=TexMobject(r''' \lim_{x \to \vec{a}}f(\vec{x})=\infty\leftrightarrow\forall M\in\mathbb{R}''').shift(0.5*DOWN)
        #En el video la definción dice limite al infinito, pero ya lo corregí para que sea el limite cuando x tiende a a
        Def3=TextMobject('''$\\exists \\ \\delta>0$ tal que si $\\vec{x}\\in B_{\\delta}(\\vec{a})\\setminus\\vec{a}\\cap
                                D\\implies f(\\vec{x})>M$''').shift(1.5*DOWN)
        text_2=TextMobject('''Veamos el siguiente ejemplo.''')
        text1=TexMobject(r"f:D\subset\mathbb{R}^2\rightarrow\mathbb{R}").shift(2.5*UP)
        text1_1=TexMobject(r"D=\lbrace (x,y)|x,y\in\mathbb{R}^{+}-\lbrace 0 \rbrace \rbrace").shift(1.25*UP)
        text2=TexMobject(r"f(x,y)=\frac{1}{x+y}").shift(-.1*UP)
        text3=TextMobject('''Veamos el límite cuando:''').shift(-1*UP)
        text4=TextMobject("(x,y)$\\rightarrow\\vec{0}=(0,0)$").shift(-1.8*UP)
        
        
        #ANIMACION

        titulo = TextMobject(
            """Límite de funciones de \n
                                $\\mathbb{R}^{n}\\rightarrow\\mathbb{R}^{m}$"""
        )
        text = TextMobject(
            """ En el caso de funciones de:\n
                            $\\mathbb{R}^{n}\\rightarrow\\mathbb{R}$."""
        )
        text_1 = TextMobject("""Donde $n\\in\\lbrace 1,2,3...\\rbrace$""").move_to(
            text.get_center() + 1 * DOWN
        )
        G1 = VGroup(text, text_1)
        Def = TextMobject(
            """Sea una función $f:D\\subseteq\\mathbb{R}^{n}\\rightarrow\\mathbb{R}$"""
        ).shift(1.5 * UP)
        Def1 = TextMobject("""Y sea $\\vec{a}\\in D$""").shift(0.6 * UP)
        Def2 = TexMobject(
            r""" \lim_{x \to \vec{a}}f(\vec{x})=\infty\leftrightarrow\forall M\in\mathbb{R}"""
        ).shift(0.5 * DOWN)
        # En el video la definción dice limite al infinito, pero ya lo corregí para que sea el limite cuando x tiende a a
        Def3 = TextMobject(
            """$\\exists \\ \\delta>0$ tal que si $\\vec{x}\\in B_{\\delta}(\\vec{a})\\setminus\\vec{a}\\cap
                                D\\implies f(\\vec{x})>M$"""
        ).shift(1.5 * DOWN)
        text_2 = TextMobject("""Veamos el siguiente ejemplo.""")
        text1 = TexMobject(
            r"f:D\subset\mathbb{R}-\lbrace\vec{0}\rbrace\rightarrow\mathbb{R}"
        ).shift(2.5 * UP)
        text1_1 = TexMobject(
            r"D=\lbrace (x,y)|x,y\in\mathbb{R}^{+}-\lbrace 0 \rbrace \rbrace"
        ).shift(1.25 * UP)
        text2 = TexMobject(r"f(x,y)=\frac{1}{x+y}").shift(-0.1 * UP)
        text3 = TextMobject("""Veamos el límite cuando:""").shift(-1 * UP)
        text4 = TextMobject("(x,y)$\\rightarrow\\vec{0}=(0,0)$").shift(-1.8 * UP)

        # ANIMACION

        self.play(Write(titulo))
        self.wait(6.5)
        self.play(FadeOut(titulo))
        self.play(Write(text))
        self.play(Write(text_1))
        self.wait(6.5)
        self.play(FadeOut(G1))
        self.play(Write(Def))
        self.play(Write(Def1))
        self.play(Write(Def2))
        self.play(Write(Def3))

        self.wait(11)
        self.play(FadeOut(Def),FadeOut(Def1),FadeOut(Def2),FadeOut(Def3))

        self.wait()
        self.play(FadeOut(Def), FadeOut(Def1), FadeOut(Def2), FadeOut(Def3))

        self.play(Write(text_2))
        self.wait()
        self.play(FadeOut(text_2))
        self.play(Write(text1))
        self.play(Write(text1_1))
        self.play(Write(text2))
        self.wait()
        self.play(Write(text3))
        self.wait()
        self.play(Write(text4))

        self.wait(7.6)
        self.play(FadeOut(text4),FadeOut(text3),FadeOut(text2),FadeOut(text1_1),
                    FadeOut(text1))

        self.wait()
        self.play(
            FadeOut(text4),
            FadeOut(text3),
            FadeOut(text2),
            FadeOut(text1_1),
            FadeOut(text1),
        )

        self.wait()
        self.custom_method()

    def custom_method(self):
        axes = ThreeDAxes()
        surface = ThreeDSurface()

        text4=TextMobject('''Tomemos  M=1''')
        M=TextMobject("M").move_to(1*UP+0.3*LEFT)

        text4 = TextMobject("""Tomemos  M=1""")

        text4.to_corner(UL)
        text5 = TextMobject("""Si tomamos""", """ $\\delta=0.5$""")
        text5[1].set_color("#88FF00")
        text5.to_corner(UL)
        text6 = TextMobject(
            """La imagen de los puntos en D  \n
                            y la bola son mayores a 1"""
        )
        text6.to_corner(UL)
        text7 = TextMobject(
            """Es posible verificar lo anterior \n
                            a través de operaciones\n
                            algebraicas."""
        )
        text7.to_corner(UL)

        text8=TextMobject('''Puedes visualizar con mejor detalle la gráfica \n
                                de la función anterior en el notebook anexo, así\n
                                como modificar los valores de M''')
        r=0.5
        #cilindro = ParametricSurface(
        #    lambda u, v: np.array([
        #        r*np.cos(TAU * v),
        #        r*np.sin(TAU * v),
        #        2*u
        #    ]),
        #    resolution=(6, 32)).fade(0.1).set_opacity(0.2) 
        linea=Line((0,0,0),(0.5*np.cos(np.pi/4),0.5*np.sin(np.pi/4),0),stroke_width=4,color="#88FF00")
        bola=Circle(radius=r,color=PURPLE,fill_opacity=1)
        text5_1=TexMobject(r"\delta").move_to(bola.get_center()+0.7*UP+0.7*RIGHT)
        text5_1.set_color("#88FF00")
        linea1=Line((0,0,1),(0.5,0.5,1),stroke_width=6,color=PURPLE_D)
        #plano1=Rectangle(height=2, width=3,color=PURPLE_C,fill_color=PURPLE_C,fill_opacity=0.4,color_opacity=0.4).move_to(-1*IN)
        linea2=Line((0.5*np.cos(np.pi/4),0.5*np.sin(np.pi/4),0),(0.5*np.cos(np.pi/4),0.5*np.sin(np.pi/4),1/(r*(2*np.cos(np.pi/4)))),stroke_width=6,color=RED)
        
        lineaZ=Line((0,0,1),(0,0,3.2),stroke_width=7,color=PURPLE)

        def puntosEnSuperficie(rad):
            puntos=[]
            for i in range(2000):
                azar=np.random.rand(1,2)
                if (0.1 < np.sqrt(azar[0][0]**2 + azar[0][1]**2) < rad):
                    puntos.append(Dot(surface.func(azar[0][0], azar[0][1]),radius=0.05,
                        color=PURPLE))
            return puntos

        puntos=puntosEnSuperficie(r)

        grupo= VGroup(*puntos)

        text8 = TextMobject(
            """Puedes visualizar con mejor detalle la gráfica \n
                                de la función anterior en el notebook anexo"""
        )
        r = 0.5
        cilindro = (
            ParametricSurface(
                lambda u, v: np.array(
                    [r * np.cos(TAU * v), r * np.sin(TAU * v), 2 * u]
                ),
                resolution=(6, 32),
            )
            .fade(0.1)
            .set_opacity(0.2)
        )
        linea = Line(
            (0, 0, 0),
            (0.5 * np.cos(np.pi / 4), 0.5 * np.sin(np.pi / 4), 0),
            stroke_width=4,
            color="#88FF00",
        )
        bola = Circle(radius=r, color=WHITE)
        text5_1 = TexMobject(r"\delta").move_to(
            bola.get_center() + 0.7 * UP + 0.7 * RIGHT
        )
        text5_1.set_color("#88FF00")
        linea1 = Line((0, 0, 1), (0.5, 0.5, 1), stroke_width=6, color=PURPLE_D)
        plano1 = Rectangle(
            height=2,
            width=3,
            color=PURPLE_C,
            fill_color=PURPLE_C,
            fill_opacity=0.4,
            color_opacity=0.4,
        ).move_to(-1 * IN)
        linea2 = Line(
            (0.5 * np.cos(np.pi / 4), 0.5 * np.sin(np.pi / 4), 0),
            (
                0.5 * np.cos(np.pi / 4),
                0.5 * np.sin(np.pi / 4),
                1 / (r * (2 * np.cos(np.pi / 4))),
            ),
            stroke_width=6,
            color=RED,
        )


        # ANIMACION
        self.set_camera_orientation(0.8 * np.pi / 2, -0.25 * np.pi, distance=4)
        self.add(axes)
        self.play(ShowCreation(surface))
        self.begin_ambient_camera_rotation(rate=0.001)
        self.wait()
        self.add_fixed_in_frame_mobjects(text4)
        self.play(Write(text4))
        self.add_fixed_in_frame_mobjects(M)
        self.wait()
        self.play(FadeOut(text4))
        self.play(ShowCreation(bola))
        self.wait()
        self.add_fixed_in_frame_mobjects(text5)
        self.play(Write(text5))
        self.play(ShowCreation(linea), Write(text5_1))
        self.wait()
        self.play(FadeOut(text5))
        self.play(FadeOut(linea), FadeOut(text5_1))
        self.add_fixed_in_frame_mobjects(text6)
        self.play(Write(text6))
        self.play()
        #self.play(ShowCreation(plano1))
        self.play(ShowCreation(lineaZ))
        self.play(FadeIn(grupo))
        self.wait(5.75)
        #self.play(ShowCreation(cilindro))
        self.play(FadeOut(text6))
        self.add_fixed_in_frame_mobjects(text7)
        self.play(Write(text7))

        self.wait(5.7)
        #self.play(FadeOut(text7),FadeOut(axes),FadeOut(plano1),FadeOut(surface),
        self.play(FadeOut(text7),FadeOut(axes),FadeOut(lineaZ),FadeOut(surface),FadeOut(bola),FadeOut(M),
                FadeOut(grupo))

        self.wait()
        self.play(
            FadeOut(text7),
            FadeOut(axes),
            FadeOut(plano1),
            FadeOut(surface),
            FadeOut(bola),
            FadeOut(cilindro),
        )

        self.add_fixed_in_frame_mobjects(text8)
        self.play(Write(text8))
        self.wait(4)
        self.play(FadeOut(text8))


# Cuando el lim es igual a infinito
class superficie3(ParametricSurface):
    def __init__(self, **kwargs):
        kwargs = {
            "u_min": -3,
            "u_max": 3,
            "v_min": -3,
            "v_max": 3,
            "checkerboard_colors": [BLUE_E],
        }
        ParametricSurface.__init__(self, self.func, **kwargs)

    def func(self, x, y):
        return np.array([x, y, (x * x) + (y * y) - 1])


class superficie4(ParametricSurface):
    def __init__(self, **kwargs):
        kwargs = {
            "u_min": 0.1,
            "u_max": 5,
            "v_min": 0.1,
            "v_max": 5,
            "checkerboard_colors": [GREEN_B],
        }
        ParametricSurface.__init__(self, self.func, **kwargs)

    def func(self, x, y):
        return np.array([x, y, 1 + (1 / ((x * x) + (y * y)))])


class LimitesRnaR(ThreeDScene):
    def construct(self):

        titulo=TextMobject('''Divergencia a infinito de funciones \n
                            de $\\mathbb{R}^{n}\\rightarrow\\mathbb{R}$ en infinito''')

        text1=TextMobject('''Sea $f:\\mathbb{R}^{n}\\rightarrow\\mathbb{R}$''').move_to(2*UP)
        text2=TexMobject(r"\lím_{\vec{x}\rightarrow\infty}f(\vec{x})=\infty^{+} \leftrightarrow\forall\ M\in\mathbb{R}").move_to(0.8*UP)
        text3=TextMobject('''$\\exists\\delta>0$ tal que si $\\vec{x}\\in B^{c}_{\\delta}(\\vec{0})$ ''' ).move_to(0.5*DOWN)
        text4=TexMobject(r'''\implies f(\vec{x})>M''').move_to(1.6*DOWN)
        text5=TextMobject("Veamos el siguiente ejemplo para aterrizar lo anterior.")
        text6=TextMobject('''Tomemos el paraboloide:\n
                                $f(x,y)=y^{2}+x^{2}-1$''')
        

        titulo = TextMobject(
            """Limite de funciones a $\\infty$ \n
                                de $\\mathbb{R}^{n}\\rightarrow\\mathbb{R}$"""
        )

        text1 = TextMobject(
            """Sea $f:\\mathbb{R}^{n}\\rightarrow\\mathbb{R}$"""
        ).move_to(2 * UP)
        text2 = TexMobject(
            r"\lim_{\vec{x}\rightarrow\infty}f(\vec{x})=\infty^{+} \leftrightarrow\forall\ M\in\mathbb{R}"
        ).move_to(0.8 * UP)
        text3 = TextMobject(
            """$\\exists\\delta>0$ tal que si $\\vec{x}\\in B^{c}_{\\delta}(\\vec{0})$ """
        ).move_to(0.5 * DOWN)
        text4 = TexMobject(r"""\implies f(\vec{x})>M""").move_to(1.6 * DOWN)
        text5 = TextMobject("Veamos el siguiente ejemplo para aterrizar lo anterior.")
        text6 = TextMobject(
            """Tomemos:\n
                                $f(x,y)=y^{2}+x^{2}-1$"""
        )


        self.play(Write(titulo))
        self.wait(5.3)
        self.play(FadeOut(titulo))
        self.play(Write(text1))
        self.play(Write(text2))
        self.play(Write(text3))
        self.play(Write(text4))

        self.wait(8)
        self.play(FadeOut(text1),FadeOut(text2),FadeOut(text3),FadeOut(text4))

        self.wait(3)
        self.play(FadeOut(text1), FadeOut(text2), FadeOut(text3), FadeOut(text4))

        self.play(Write(text5))
        self.wait(5)
        self.play(FadeOut(text5))
        self.play(Write(text6))
        self.wait(3.8)
        self.play(FadeOut(text6))
        self.custom_method()

    def custom_method(self):
        axes = ThreeDAxes()
        superficie = superficie3()
        superficie.set_opacity(0.8)
        text1 = TexMobject(r"""f(x,y)=y^{2}+x^{2}-1""")
        text1.to_corner(UL)
        text2 = TextMobject("""Tomemos M=0""")
        text2.to_corner(UL)
        text3 = TextMobject("""Tomamos $\\delta$""")
        text3.to_corner(UL)

        text4 = TextMobject(
            """Veremos que la imagen de los puntos que no \n
                            están en la bola, son mayor a M"""
        )
        text4.to_corner(UL)
        text5 = TextMobject(
            """Podemos realizar lo mismo con cualquier M$\\in\\mathbb{R}$"""
        )
        text5.to_corner(UL)

        text6=TextMobject('''Por lo cual notaremos que la función diverge a $+\\infty$ \n
                             cuando $\\vec{x}\\rightarrow\\infty$.''')

        text6 = TextMobject(
            """Por lo cual notaremos que la función no \n
                                tiene límite cuando $\\vec{x}\\rightarrow\\infty$."""
        )

        text6.to_corner(UL)
        # text7=TextMobject('''¿Se te ocurre como modificar la definición \n
        #                        cuando la función diverge a $\\infty^{-}$''')

        M=0
        r=M+1.4
        #cilindro = ParametricSurface(
       #     lambda u, v: np.array([
       #         r*np.cos(TAU * v),
       #         r*np.sin(TAU * v),
       #         2*u
       #     ]),
       #     resolution=(6, 32)).fade(0.1).set_opacity(0.4)
       # cilindro.set_color(RED_C).move_to(M*IN)
        #cilindro.set_opacity(0.4)
        M1=-0.5
        r1=M1+1.5
        #cilindro1 = ParametricSurface(
        #    lambda u, v: np.array([
        #        r1*np.cos(TAU * v),
        #        r1*np.sin(TAU * v),
        #        4*u
        #    ]),
        #    resolution=(6, 32)).fade(0.1).set_opacity(0.4)
        #cilindro1.set_color(RED_C).move_to((M1/2)*IN)
       # cilindro2.set_opacity(0.4)
        
        #bola1=Circle(radius=r1,color=RED,color_opacity=1).move_to(M1*OUT)
        bola1=Circle(radius=r1,color=RED,color_opacity=1)
       
        #plano1=Rectangle(height=3, width=5,color=PURPLE_C,fill_color=PURPLE_C,fill_opacity=0.4,
        #                        color_opacity=0.4 ).move_to(M*OUT)
        bola=Circle(radius=r,color=RED,color_opacity=1).move_to(M*OUT)
        linealabel=TexMobject(r'''\delta''').next_to(bola,RIGHT,buff=0.5).set_color(RED_C).rotate(PI/2,axis=RIGHT).scale(2)
        linea=Line((0,0,0),(r,0,0),stroke_width=3,color=RED_C) 

        def puntosEnSuperficie(rad,lim,num):
            puntosDom = []
            puntosSur = []
            for i in range(num):
                azar = np.random.uniform(-lim,lim, (1,2))[0]
                if ((rad < np.sqrt(azar[0]**2 + azar[1]**2)) and not (azar[0]<0 and azar[1]>0)):
                    puntosDom.append(Dot(np.array([azar[0], azar[1],0]), color = PURPLE))
                    puntosSur.append(Dot(superficie.func(azar[0], azar[1]), color = RED))
            return puntosDom, puntosSur

        puntosD1, puntosS1 = puntosEnSuperficie(r, 3, 6000)
        puntosD2, puntosS2 = puntosEnSuperficie(r1, r, 3000)

        GPuntosD1 = VGroup(*puntosD1)
        GPuntosS1 = VGroup(*puntosS1)
        GPuntosD2 = VGroup(*puntosD2)
        GPuntosS2 = VGroup(*puntosS2)

    ###Animacion
        self.set_camera_orientation(0.8*np.pi/2, -0.25*np.pi,distance=15)

        M = 0
        r = M + 1.4
        cilindro = (
            ParametricSurface(
                lambda u, v: np.array(
                    [r * np.cos(TAU * v), r * np.sin(TAU * v), 2 * u]
                ),
                resolution=(6, 32),
            )
            .fade(0.1)
            .set_opacity(0.4)
        )
        cilindro.set_color(RED_C).move_to(M * IN)
        # cilindro.set_opacity(0.4)
        M1 = -0.5
        r1 = M1 + 1.5
        cilindro1 = (
            ParametricSurface(
                lambda u, v: np.array(
                    [r1 * np.cos(TAU * v), r1 * np.sin(TAU * v), 4 * u]
                ),
                resolution=(6, 32),
            )
            .fade(0.1)
            .set_opacity(0.4)
        )
        cilindro1.set_color(RED_C).move_to((M1 / 2) * IN)
        # cilindro2.set_opacity(0.4)
        bola1 = Circle(radius=r1, color=RED, color_opacity=1).move_to(M1 * OUT)

        plano1 = Rectangle(
            height=3,
            width=5,
            color=PURPLE_C,
            fill_color=PURPLE_C,
            fill_opacity=0.4,
            color_opacity=0.4,
        ).move_to(M * OUT)
        bola = Circle(radius=r, color=RED, color_opacity=1).move_to(M * OUT)
        linealabel = (
            TexMobject(r"""\delta""")
            .next_to(bola, RIGHT, buff=0.5)
            .set_color(RED_C)
            .rotate(PI / 2, axis=RIGHT)
            .scale(2)
        )
        linea = Line((0, 0, 0), (r, 0, 0), stroke_width=3, color=RED_C)
        ###Animacion
        self.set_camera_orientation(0.8 * np.pi / 2, -0.25 * np.pi, distance=15)

        self.begin_ambient_camera_rotation(rate=0.001)
        self.play(ShowCreation(axes))
        self.add_fixed_in_frame_mobjects(text1)
        self.play(Write(text1))
        self.play(ShowCreation(superficie))
        self.wait(2)
        self.play(FadeOut(text1))
        self.add_fixed_in_frame_mobjects(text2)
        self.play(Write(text2))
        #self.play(ShowCreation(plano1))
        self.wait(2.75)
        self.play(FadeOut(text2))
        self.add_fixed_in_frame_mobjects(text3)
        self.play(Write(text3))
        self.play(ShowCreation(linea))
        self.play(Write(linealabel))
        self.play(ShowCreation(bola))
        self.play(FadeOut(linea), FadeOut(linealabel))
        self.play(FadeOut(text3))
        self.add_fixed_in_frame_mobjects(text4)
        self.play(Write(text4))
        self.play(FadeIn(GPuntosD1))
        self.play(FadeIn(GPuntosS1))
        #self.play(ShowCreation(cilindro))
        self.wait(8.3)
        self.play(FadeOut(text4))
        self.add_fixed_in_frame_mobjects(text5)
        self.play(Write(text5))

        ##self.play(plano1.shift,M1*OUT,runtime=1.5)
        self.play(ReplacementTransform(bola,bola1))
        self.wait()
        self.play(FadeIn(GPuntosD2))
        self.play(FadeIn(GPuntosS2))
        #self.play(ReplacementTransform(cilindro,cilindro1))
        self.wait(4.6)
        self.play(FadeOut(text5))
        self.add_fixed_in_frame_mobjects(text6)
        self.play(Write(text6))
        self.wait(6.5)
        self.play(FadeOut(axes),FadeOut(text6),FadeOut(superficie),FadeOut(bola1),
                FadeOut(GPuntosD1),FadeOut(GPuntosS1),FadeOut(GPuntosD2),FadeOut(GPuntosS2))
       

        self.play(plano1.shift, M1 * OUT, runtime=1.5)
        self.play(ReplacementTransform(bola, bola1))
        self.play(ReplacementTransform(cilindro, cilindro1))
        self.play(FadeOut(text5))
        self.add_fixed_in_frame_mobjects(text6)
        self.play(Write(text6))
        self.wait()
        self.play(
            FadeOut(cilindro1),
            FadeOut(axes),
            FadeOut(text6),
            FadeOut(superficie),
            FadeOut(plano1),
            FadeOut(bola1),
        )



# Cuando el limite es r



class Limite4_1 (ThreeDScene):
    def construct (self):
        titulo=TextMobject('''Límite en infinito de funciones de \n

class Limite4_1(ThreeDScene):
    def construct(self):
        titulo = TextMobject(
            """Límite a $\\infty$ de funciones de \n

                                $\\mathbb{R}^{n}$ a $\\mathbb{R}$\n
                                cuando es un valor L"""
        )
        text = TextMobject("Sea $f:\\mathbb{R}^{n}\\rightarrow\\mathbb{R}$").move_to(
            2.2 * UP
        )
        text1 = TexMobject(
            r"\lim_{\vec{x}\rightarrow\infty}f(\vec{x})=L\leftrightarrow\forall\epsilon>0"
        ).move_to(1 * UP)
        text2 = TexMobject(
            r"\exists\delta>0 \ tq \ \forall \vec{x}\in B^{c}_{\delta}(\vec{0})"
        ).move_to(-0.2 * UP)
        text3 = TexMobject(r"\implies d(f(\vec{x}),L)<\epsilon").move_to(1.4 * DOWN)
        G1 = VGroup(text, text1, text2, text3)
        text4 = TextMobject("""Veamos el siguiente ejemplo para aterrizar ideas:""")
        text5 = TexMobject(r"f:\mathbb{R}^{2}\rightarrow\mathbb{R}")
        text6 = TexMobject(r"f(x,y)=1+\frac{1}{x^{2}+y^{2}}").move_to(1.5 * DOWN)
        G2 = VGroup(text4, text5, text6)

        self.play(Write(titulo))
        self.wait(5.25)
        self.play(FadeOut(titulo))
        self.play(Write(text))
        self.play(Write(text1))
        self.play(Write(text2))
        self.play(Write(text3))
        self.wait(6)
        self.play(FadeOut(G1))
        self.play(Write(text4))

        self.wait(4.6)
        self.play(text4.shift,2*UP,runtime=1.5)

        self.wait()
        self.play(text4.shift, 2 * UP, runtime=1.5)

        self.play(Write(text5))
        self.play(Write(text6))
        self.wait(3)
        self.play(FadeOut(G2))
        self.wait()
        self.custom_method()

    def custom_method(self):
        axes = ThreeDAxes()
        superficie = superficie4()
        text1 = TexMobject(r"""f(x,y)=1+\frac{1}{x^{2}+y^{2}}""")
        text1.to_corner(UL)
        text2 = TextMobject("Tomemos", " $\epsilon$=0.5")
        text2.to_corner(UL)
        text2[1].set_color(RED)
        text3 = TextMobject("Y notemos que podemos escoger").to_corner(UL)
        text3_1 = TextMobject("una", " $\\delta>0$").move_to(
            text3.get_center() + 1 * DOWN
        )
        text3_1[1].set_color(YELLOW_C)

        text4=TextMobject('''Tal que la imagen de los puntos que no \n
                            pertenecen a $ B_{\\delta}(\\vec{0})$''').to_corner(UL)
        text5=TextMobject('''Están a una distancia $\\epsilon$\n
                                de 1.''').to_corner(UL)
        text5_1=TextMobject('''Es posible hacer lo mismo con toda\n
                                $\\epsilon>0$.''').to_corner(UL)
        text6=TextMobject('''Por lo cual:''').to_corner(UL)
        text7=TexMobject(r"\lim_{\vec{x}\rightarrow\infty}f(\vec{x})=1").move_to(text5.get_center()+1*DOWN)
        
        M=TextMobject("1").move_to(1*UP+0.2*LEFT)

        #epsilons se pueden modificar
        r=0.5
        r1=1
        linea=Line((0,0,1),(0,0,1+r),stroke_width=6,color=RED)
        linea_1=Line((0,0,1),(0,0,1+r1),stroke_width=6,color=RED)
        R=1.7
        R1=R-0.5
        linea1=Line((0,0,0),(R,0,0),stroke_width=6,color=YELLOW_C)
        
        circulo=Circle(radius=R,color=YELLOW_C)
        circulo1=Circle(radius=R1,color=YELLOW_C)
        #cilindro = ParametricSurface(
        #    lambda u, v: np.array([
        #        R*np.cos(TAU * v),
        #        R*np.sin(TAU * v),
        #        4*u
        #    ]),
        #    resolution=(6, 32)).fade(0.1).set_opacity(0.2)
        #cilindro.set_color(YELLOW_C)
        #cilindro1 = ParametricSurface(
        #    lambda u, v: np.array([
        #        R1*np.cos(TAU * v),
        #        R1*np.sin(TAU * v),
        #        4*u
        #    ]),
        #    resolution=(6, 32)).fade(0.1).set_opacity(0.2)
        #cilindro1.set_color(YELLOW_C)

        def puntosEnSuperficie(rad,lim,num):
            puntosDom = []
            puntosSur = []
            for i in range(num):
                azar = lim*np.random.rand(1,2)[0] + 0.1
                if (rad < np.sqrt(azar[0]**2 + azar[1]**2) < lim):
                    puntosDom.append(Dot(np.array([azar[0], azar[1],0]), color = BLUE))
                    puntosSur.append(Dot(superficie.func(azar[0], azar[1]), color = RED))
            return puntosDom, puntosSur

        puntosD1, puntosS1 = puntosEnSuperficie(R, 5, 6000)
        puntosD2, puntosS2 = puntosEnSuperficie(R1, R, 3000)

        GPuntosD1 = VGroup(*puntosD1)
        GPuntosS1 = VGroup(*puntosS1)
        GPuntosD2 = VGroup(*puntosD2)
        GPuntosS2 = VGroup(*puntosS2)

    ###Animacion
        self.set_camera_orientation(0.8*np.pi/2, -0.25*np.pi,distance=12)

        text4 = TextMobject(
            """Tal que la imagen de los puntos que no \n
                            pertenecen a $ B_{\\delta}(\\vec{0})$"""
        ).to_corner(UL)
        text5 = TextMobject(
            """Están a una distancia $\\epsilon$\n
                                de 1."""
        ).to_corner(UL)
        text5_1 = TextMobject(
            """Es posible hacer lo mismo con toda\n
                                $\\epsilon>0$."""
        ).to_corner(UL)
        text6 = TextMobject("""Por lo cual:""").to_corner(UL)
        text7 = TexMobject(r"\lim_{\vec{x}\rightarrow\infty}f(\vec{x})=1").move_to(
            text5.get_center() + 1 * DOWN
        )

        # epsilons se pueden modificar
        r = 0.5
        r1 = 1
        linea = Line((0, 0, 1), (0, 0, 1 + r), stroke_width=6, color=RED)
        linea_1 = Line((0, 0, 1), (0, 0, 1 + r1), stroke_width=6, color=RED)
        R = 1.7
        R1 = R - 0.5
        linea1 = Line((0, 0, 0), (R, 0, 0), stroke_width=6, color=YELLOW_C)

        circulo = Circle(radius=R, color=YELLOW_C)
        circulo1 = Circle(radius=R1, color=YELLOW_C)
        cilindro = (
            ParametricSurface(
                lambda u, v: np.array(
                    [R * np.cos(TAU * v), R * np.sin(TAU * v), 4 * u]
                ),
                resolution=(6, 32),
            )
            .fade(0.1)
            .set_opacity(0.2)
        )
        cilindro.set_color(YELLOW_C)
        cilindro1 = (
            ParametricSurface(
                lambda u, v: np.array(
                    [R1 * np.cos(TAU * v), R1 * np.sin(TAU * v), 4 * u]
                ),
                resolution=(6, 32),
            )
            .fade(0.1)
            .set_opacity(0.2)
        )
        cilindro1.set_color(YELLOW_C)
        ###Animacion
        self.set_camera_orientation(0.8 * np.pi / 2, -0.25 * np.pi, distance=12)

        self.begin_ambient_camera_rotation(rate=0.001)
        self.play(ShowCreation(axes))
        self.add_fixed_in_frame_mobjects(text1)
        self.add_fixed_in_frame_mobjects(M)
        self.play(Write(text1))
        self.play(ShowCreation(superficie))
        self.wait()
        self.play(FadeOut(text1))
        self.add_fixed_in_frame_mobjects(text2)
        self.play(Write(text2))
        self.play(ShowCreation(linea))
        self.play(FadeOut(text2))
        self.add_fixed_in_frame_mobjects(text3)
        self.play(Write(text3))
        self.add_fixed_in_frame_mobjects(text3_1)
        self.play(Write(text3_1))
        self.play(ShowCreation(linea1))
        self.play(ShowCreation(circulo))
        self.play(FadeOut(text3), FadeOut(text3_1))
        self.add_fixed_in_frame_mobjects(text4)
        self.play(Write(text4))
        #self.play(ShowCreation(cilindro))
        self.wait()
        self.play(FadeOut(text4))
        self.play(FadeIn(GPuntosD1))
        self.add_fixed_in_frame_mobjects(text5)

        self.play(Write(text5),FadeOut(linea1))
        self.play(FadeIn(GPuntosS1))
        self.play(linea.shift,(R+0.1)*RIGHT,runtime=10)        
        self.wait(6.5)
        self.play(FadeOut(text5))
        self.add_fixed_in_frame_mobjects(text5_1)
        self.play(Write(text5_1))
        self.play(ReplacementTransform(linea,linea_1))
        self.play(ReplacementTransform(circulo,circulo1))
        #self.play(ReplacementTransform(cilindro,cilindro1))
        self.play(FadeIn(GPuntosD2))
        self.play(FadeIn(GPuntosS2))
        self.play(linea_1.shift,(R1+0.1)*RIGHT,runtime=10)
        self.wait(3)

        self.play(Write(text5), FadeOut(linea1))
        self.play(linea.shift, (R + 0.1) * RIGHT, runtime=10)
        self.wait()
        self.play(FadeOut(text5))
        self.add_fixed_in_frame_mobjects(text5_1)
        self.play(Write(text5_1))
        self.play(ReplacementTransform(linea, linea_1))
        self.play(ReplacementTransform(circulo, circulo1))
        self.play(ReplacementTransform(cilindro, cilindro1))
        self.play(linea_1.shift, (R1 + 0.1) * RIGHT, runtime=10)
        self.wait()

        self.play(FadeOut(text5_1))
        self.add_fixed_in_frame_mobjects(text6)
        self.play(Write(text6))
        self.add_fixed_in_frame_mobjects(text7)
        self.play(Write(text7))
        self.wait(2)

        self.play(FadeOut(text7),FadeOut(text6),FadeOut(axes),FadeOut(M),
                    FadeOut(superficie),FadeOut(linea_1),FadeOut(circulo1),FadeOut(GPuntosD1),
                    FadeOut(GPuntosS1),FadeOut(GPuntosD2),FadeOut(GPuntosS2))        
        

        self.play(
            FadeOut(text7),
            FadeOut(text6),
            FadeOut(axes),
            FadeOut(cilindro1),
            FadeOut(superficie),
            FadeOut(linea_1),
            FadeOut(circulo1),
        )



##########################
##########################
# Funciones de R2 A R2
# Definimos los campos vectoriales
def campo(point):
    x, y = point[:2]
    return -((1 / (y * y * y * y * y))) * RIGHT + x * UP


def campo2(point):
    x, y = point[:2]
    return -(y) * RIGHT + x * UP


class LimiteR2aR2(Scene):
    def construct(self):

        titulo = TextMobject(
            """Límite de funciones de:\n
                                $\\mathbb{R}^{2}\\rightarrow\\mathbb{R}^{2}$"""
        )
        text = TextMobject("""Consideremos la función:""")
        text1 = TexMobject(r"f(x,y)=(-y,x)")
        text2 = TextMobject(
            """ Es posible mostrar que esta función tiene límite \n
                                en todo $\\mathbb{R}^{2}$"""
        ).to_corner(UL)
        text2_1 = TextMobject(
            """En particular en (0,0) el límite es (0,0)"""
        ).to_corner(UL)
        text3 = TextMobject(
            """Podemos ver lo anterior gráficamente de \n
                                la siguiente manera"""
        ).to_corner(UL)
        text4 = TextMobject("Escogemos una bola de radio", " $\\delta$").to_corner(UL)
        text4[1].set_color(PINK)
        text5 = TextMobject(
            """Podemos encontrar una bola, tal que la imagen de los\n
                            puntos dentro de la bola"""
        ).to_edge(UP)

        text6 = TextMobject(
            """Esten a una distancia menor a""", """ $\\delta$"""
        ).to_edge(UP)
        text6[1].set_color(PINK)
        text7 = TextMobject(
            """Es posible hacer lo anterior con cualquier $\\delta$"""
        ).to_edge(UP)

        text8 = TextMobject(
            """Una función $f:A\subset\\mathbb{R}^{n}\\rightarrow\\mathbb{R}^{m}$"""
        ).move_to(2.8 * UP)
        text8_1 = TextMobject(
            """tiene límite en $\\vec{x}_0$ y es $\\vec{l}$ si:"""
        ).move_to(1.5 * UP)
        text8_2 = TexMobject(
            r"\forall\epsilon>0\ \exists\delta>0 \ tq \ si ||\vec{x}-\vec{x_0}||<\delta"
        )
        text8_3 = TexMobject(
            r"(\vec{x}\in A-\lbrace\vec{x_0}\rbrace) \ ||f(\vec{x})-\vec{l}||<\epsilon"
        ).move_to(1.5 * DOWN)
        G1 = VGroup(text8, text8_1, text8_2, text8_3)

        # Se puede cambiar delta y x para modificar las bolas
        delta = 1.1
        x = 0
        delta1 = Line((0, 0, 0), (0, delta, 0), color=PINK, stroke_width=3)
        bola = Circle(radius=delta, color=PINK).move_to(x * RIGHT)
        bola1 = Circle(radius=delta - 0.05, color=WHITE)
        bola_1 = Circle(radius=delta + 1, color=PINK).move_to(x * RIGHT)
        bola1_1 = Circle(radius=delta + 1 - 0.05, color=WHITE)

        axes = Axes()
        # Se crea el campo vectorial con la funcion
        campo_2 = VectorField(
            campo2,
            x_min=-8,
            x_max=8,
            y_min=-6,
            y_max=6,
            delta_x=0.25,
            delta_y=0.25,
            length_func=lambda norm: 0.25 * sigmoid(norm),
        )

        self.play(Write(titulo))
        self.wait()
        self.play(FadeOut(titulo))
        self.play(Write(text))
        self.wait()
        self.play(text.shift, 1.5 * UP, runtime=1.5)
        self.play(Write(text1))
        self.wait()
        self.play(FadeOut(text))
        self.add_foreground_mobjects(text1)
        self.play(Write(axes), text1.shift, 3 * UP + 4 * LEFT, runtime=1.5)
        # Dibujamos el campo vectorial
        self.play(*[GrowArrow(vec) for vec in campo_2], runtime=20)
        self.wait()
        self.play(ReplacementTransform(text1, text2))
        self.add_foreground_mobjects(text2)
        self.wait(2)
        self.play(ReplacementTransform(text2, text2_1))
        self.wait(2)
        self.play(FadeOut(text2_1))
        self.play(Write(text3))
        self.wait()
        self.play(ReplacementTransform(text3, text4))
        self.wait()
        self.play(ShowCreation(delta1))
        self.play(ShowCreation(bola))
        self.play(ReplacementTransform(text4, text5))
        self.wait()
        self.play(ShowCreation(bola1))
        self.wait()
        self.play(ReplacementTransform(text5, text6))
        self.wait()
        self.play(ReplacementTransform(text6, text7))
        self.play(ReplacementTransform(bola, bola_1))
        self.play(ReplacementTransform(bola1, bola1_1))
        self.wait()
        self.play(
            FadeOut(campo_2),
            FadeOut(bola1_1),
            FadeOut(bola_1),
            FadeOut(axes),
            FadeOut(text7),
            FadeOut(delta1),
        )
        self.play(Write(text8))
        self.play(Write(text8_1))
        self.play(Write(text8_2))
        self.play(Write(text8_3))
        self.wait(3)
        self.play(FadeOut(G1))
        self.wait()
        self.custom_method()

    def custom_method(self):

        text = TextMobject("""Consideremos ahora la función:""")
        text1 = TexMobject(r"f(x,y)=({\frac{-1}{y^{5}}},x)")
        text2 = TextMobject(
            """ Es posible demostrar que esta función no tiene\n
                                límite en cualquier punto de la forma (x,0)"""
        ).move_to(text1.get_center() - 2 * UP)
        text3 = TextMobject(
            """Podemos ver lo anterior gráficamente de \n
                                la siguiente manera"""
        ).to_corner(UL)
        text4 = TextMobject(
            """La imagen de la función\n
                            siempre está creciendo en el eje x"""
        ).to_corner(UL)
        text5 = TextMobject(
            """¿Se te ocurre como demostrar que la función anterior\n
                                no tiene límite?"""
        )
        axes = Axes()
        # Se crea el campo vectorial con la función CurlFunc
        campo_1 = VectorField(
            campo,
            x_min=-8,
            x_max=8,
            y_min=-6,
            y_max=6,
            delta_x=0.45,
            delta_y=0.45,
            length_func=lambda norm: 0.49 * sigmoid(norm),
        )

        self.play(Write(text))
        self.wait()
        self.play(text.shift, 2 * UP, runtime=1.5)
        self.play(Write(text1))
        self.wait()
        self.play(FadeOut(text))
        self.add_foreground_mobjects(text1)
        self.play(Write(axes), text1.shift, 3 * UP + 4 * LEFT, runtime=1.5)
        # Dibujamos el campo vectorial
        self.play(*[GrowArrow(vec) for vec in campo_1], runtime=20)
        self.wait()
        self.play(Write(text2))
        self.add_foreground_mobjects(text2)
        self.wait(2)
        self.play(FadeOut(text1), FadeOut(text2))
        self.play(Write(text3))
        self.wait()
        self.play(ReplacementTransform(text3, text4))
        self.wait(3)
        self.play(FadeOut(text4))
        self.play(FadeOut(axes), FadeOut(campo_1))
        self.play(Write(text5))
        self.wait(2)
        self.play(FadeOut(text5))


###Definición de Gráficas###


class Definición_Gráficas(GraphScene, Scene):
    def setup(self):
        Scene.setup(self)
        GraphScene.setup(self)

    CONFIG = {
        "x_min": -1,
        "x_max": 4,
        "x_axis_width": 5,
        "x_tick_frequency": 1,
        "x_leftmost_tick": None,  # Change if different from x_min
        "x_labeled_nums": [1, 2, 3],
        "x_axis_label": "$x$",
        "y_min": -1.5,
        "y_max": 5,
        "y_axis_height": 4,
        "y_tick_frequency": 1,
        "y_bottom_tick": None,  # Change if different from y_min
        "y_labeled_nums": [-1, 1, 3, 5],
        "y_axis_label": "$y$",
        "axes_color": GREY,
        "graph_origin": 2.7 * DOWN + 1.8 * LEFT,
        "exclude_zero_label": True,
        "default_graph_colors": [BLUE, GREEN, YELLOW],
        "default_derivative_color": GREEN,
        "default_input_color": YELLOW,
        "default_riemann_start_color": BLUE,
        "default_riemann_end_color": GREEN,
        "area_opacity": 0.8,
        "num_rects": 50,
    }

    def construct(self):

        # Textos
        titulo = TextMobject("Gráficas de Funciones").scale(1.5)

        text_1 = TextMobject("Consideremos la siguiente función:").move_to(3.2 * UP)
        ejemplo_1_1 = TexMobject(r"f:[0,3]\subset\mathbb{R}\rightarrow\mathbb{R}")
        ejemplo_1_2 = TexMobject(r"f(x)=5-2x").next_to(ejemplo_1_1, DOWN)
        ejemplo_1 = VGroup(ejemplo_1_1, ejemplo_1_2).next_to(text_1, 1.5 * DOWN)

        text_2_1 = TextMobject(
            "La función $f$ nos permite definir relaciones entre pares"
        )
        text_2_2 = TextMobject(
            "correspondientes del ", "dominio", " y el ", "contradominio"
        ).next_to(text_2_1, DOWN)
        text_2_2[1].set_color(BLUE_E)
        text_2_2[3].set_color(RED_E)
        text_2 = VGroup(text_2_1, text_2_2).move_to(text_1.get_center())

        text_3_1 = TextMobject("Para cada elemento del ", "dominio", " de $f$")
        text_3_2 = TextMobject(
            "corresponde un sólo elemento del ", "contradominio"
        ).next_to(text_3_1, DOWN)
        text_3_1[1].set_color(BLUE_E)
        text_3_2[1].set_color(RED_E)
        text_3 = VGroup(text_3_1, text_3_2).move_to(text_1.get_center())

        text_4_1 = TextMobject("Consideremos las parejas ordenadas")
        text_4_2 = TextMobject(
            "$($", "$x$", " , ", "$f(x)$", "$)$, con ", "$x$", " en el dominio de $f$"
        ).next_to(text_4_1, DOWN)
        text_4_2[1].set_color(BLUE_E)
        text_4_2[3].set_color(RED_E)
        text_4_2[5].set_color(BLUE_E)
        text_4 = VGroup(text_4_1, text_4_2).move_to(text_1.get_center())

        text_5 = TextMobject(
            "Definimos la ", "gráfica", " de $f$ como el siguiente conjunto:"
        ).move_to(3.2 * UP)
        text_5[1].set_color(YELLOW_E)
        text_6 = TexMobject(
            r"G_f:=\{(x,f(x))\in \mathbb{R}^2|x\in[0,3] \}", color=YELLOW_E
        ).next_to(text_5, 1 * DOWN)
        def_graf = VGroup(text_5, text_6)

        text_7_1 = TextMobject(
            "En general, dada una función $f:A\\subset\\mathbb{R}^n\\rightarrow\\mathbb{R}^m$,"
        )
        text_7_2 = TextMobject(
            "se define la ", "gráfica", " de $f$ de la siguiente forma:"
        ).next_to(text_7_1, DOWN)
        text_7_2[1].set_color(YELLOW_E)
        text_7 = VGroup(text_7_1, text_7_2).move_to(text_1.get_center() + 1 * DOWN)

        def_1 = TexMobject(
            r"G_f:=\{ (x_1,...,x_n,f_1(\vec{x}),...,f_m(\vec{x}))\in\mathbb{R}^{n+m}|\vec{x}=(x_1,...x_n)\in A \}"
        ).scale(0.95)
        text_8 = TextMobject("Es decir, ").next_to(def_1, 1.5 * DOWN)
        def_2 = TexMobject(
            r"G_f:=\{(\vec{x},f(\vec{x}))\in \mathbb{R}^{n+m}| \vec{x}\text{ en el domino de } f \}"
        ).next_to(text_8, 1.5 * DOWN)
        dt = VGroup(text_8, def_2)
        # RECTAS REALES
        numberline_1 = NumberLine(
            x_min=0,
            x_max=4,
            unit_size=0.75,
            include_numbers=True,
            include_tip=True,
            number_scale_val=0.6,
            lable_direction=1.2 * DOWN,
        ).move_to(4.4 * LEFT + 0.5 * UP)
        numberline_2 = NumberLine(
            x_min=-2,
            x_max=4,
            unit_size=0.5,
            include_numbers=True,
            numbers_to_show=[-1, 1, 3],
            include_tip=True,
            number_scale_val=0.6,
            label_direction=1.2 * DOWN,
            numbers_with_elongated_ticks=[],
        ).move_to(4.4 * RIGHT + 0.5 * UP)
        text_numberline_1 = (
            TextMobject("Dominio ($x$)", color=BLUE_E)
            .scale(0.75)
            .move_to(numberline_1.get_bottom() + 0.4 * DOWN)
        )
        text_numberline_2 = (
            TextMobject("Contradominio (f$(x)$)", color=RED_E)
            .scale(0.75)
            .move_to(numberline_2.get_bottom() + 0.4 * DOWN)
        )

        # PAREJAS DE PUNTOS X - F(X)

        punto_dom_1 = Dot(color=BLUE_E).move_to((-5.11, 0.63, 0))
        punto_dom_2 = Dot(color=BLUE_E).move_to((-4.36, 0.63, 0))
        punto_dom_3 = Dot(color=BLUE_E).move_to((-3.62, 0.63, 0))
        punto_contra_1 = Dot(color=RED_E).move_to((5.4, 0.665, 0))
        punto_contra_2 = Dot(color=RED_E).move_to((4.4, 0.665, 0))
        punto_contra_3 = Dot(color=RED_E).move_to((3.4, 0.665, 0))

        text_punto_dom_1 = (
            TexMobject(r"x=1", color=BLUE_E)
            .scale(0.75)
            .next_to(text_numberline_1, 1.5 * DOWN)
        )
        text_punto_dom_2 = (
            TexMobject(r"x=2", color=BLUE_E)
            .scale(0.75)
            .next_to(text_punto_dom_1, 1.5 * DOWN)
        )
        text_punto_dom_3 = (
            TexMobject(r"x=3", color=BLUE_E)
            .scale(0.75)
            .next_to(text_punto_dom_2, 1.5 * DOWN)
        )
        text_punto_contra_1 = (
            TexMobject(r"f(1)=3", color=RED_E)
            .scale(0.75)
            .next_to(text_numberline_2, 1.5 * DOWN)
        )
        text_punto_contra_2 = (
            TexMobject(r"f(2)=1", color=RED_E)
            .scale(0.75)
            .next_to(text_punto_contra_1, 1.5 * DOWN)
        )
        text_punto_contra_3 = (
            TexMobject(r"f(3)=-1", color=RED_E)
            .scale(0.75)
            .next_to(text_punto_contra_2, 1.5 * DOWN)
        )

        text_puntos = VGroup(
            text_punto_dom_1,
            text_punto_dom_2,
            text_punto_dom_3,
            text_punto_contra_1,
            text_punto_contra_2,
            text_punto_contra_3,
            text_numberline_1,
            text_numberline_2,
        )
        # Lineas para puntos

        linea_dom_1 = Line(
            punto_dom_1.get_center(),
            ejemplo_1_2.get_left(),
            color=BLUE_E,
            path_arc=-0.5,
        )
        linea_dom_2 = Line(
            punto_dom_2.get_center(),
            ejemplo_1_2.get_left(),
            color=BLUE_E,
            path_arc=-0.5,
        )
        linea_dom_3 = Line(
            punto_dom_3.get_center(),
            ejemplo_1_2.get_left(),
            color=BLUE_E,
            path_arc=-0.5,
        )
        linea_contra_1 = Line(
            ejemplo_1_2.get_right(),
            punto_contra_1.get_center(),
            color=RED_E,
            path_arc=-0.5,
        )
        linea_contra_2 = Line(
            ejemplo_1_2.get_right(),
            punto_contra_2.get_center(),
            color=RED_E,
            path_arc=-0.5,
        )
        linea_contra_3 = Line(
            ejemplo_1_2.get_right(),
            punto_contra_3.get_center(),
            color=RED_E,
            path_arc=-0.5,
        )

        # GRUPOS PARA FADE OUT
        dom_contra_1 = VGroup(punto_dom_1, punto_contra_1, linea_dom_1, linea_contra_1)
        dom_contra_2 = VGroup(punto_dom_2, punto_contra_2, linea_dom_2, linea_contra_2)
        dom_contra_3 = VGroup(punto_dom_3, punto_contra_3, linea_dom_3, linea_contra_3)

        # secuencia de Animaciones

        self.play(Write(titulo))
        self.wait(3)
        self.play(FadeOut(titulo))
        self.play(Write(text_1))
        self.play(Write(ejemplo_1))
        self.wait(10)
        self.play(FadeOut(text_1), FadeOut(ejemplo_1_1))
        self.play(ShowCreation(numberline_1), ShowCreation(numberline_2))
        self.play(Write(text_numberline_1), Write(text_numberline_2))
        self.play(Write(text_2))
        self.wait(7.625)
        self.play(FadeOut(text_2))
        self.play(Write(text_3))
        self.wait(6.875)

        self.play(FadeIn(punto_dom_1), FadeIn(text_punto_dom_1))
        self.play(FadeIn(linea_dom_1))
        self.play(FadeIn(linea_contra_1))
        self.play(FadeIn(punto_contra_1), FadeIn(text_punto_contra_1))
        self.play(FadeOut(dom_contra_1))

        self.play(FadeIn(punto_dom_2), FadeIn(text_punto_dom_2))
        self.play(FadeIn(linea_dom_2))
        self.play(FadeIn(linea_contra_2))
        self.play(FadeIn(punto_contra_2), FadeIn(text_punto_contra_2))
        self.play(FadeOut(dom_contra_2))

        self.play(FadeIn(punto_dom_3), FadeIn(text_punto_dom_3))
        self.play(FadeIn(linea_dom_3))
        self.play(FadeIn(linea_contra_3))
        self.play(FadeIn(punto_contra_3), FadeIn(text_punto_contra_3))
        self.play(FadeOut(dom_contra_3))

        self.wait(0.5)

        self.play(FadeOut(numberline_1), FadeOut(numberline_2), FadeOut(text_3))
        self.play(text_puntos.shift, 1.7 * UP)

        # COMIENZA ESCENA CON LOS EJES

        self.setup_axes(animate=True)
        # Función
        f = lambda x: 5 - 2 * x
        graph = self.get_graph(f, color=YELLOW_E, x_min=0, x_max=3)
        # Coordenadas y Puntos
        coord_1 = (
            TexMobject(r"(", r"1", r",", r"3", r")")
            .scale(0.75)
            .move_to(0.7 * UP + 0.6 * RIGHT)
        )
        coord_1[1].set_color(BLUE_E)
        coord_1[3].set_color(RED_E)
        coord_2 = (
            TexMobject(r"(", r"2", r",", r"1", r")")
            .scale(0.75)
            .next_to(coord_1, 1.5 * DOWN)
        )
        coord_2[1].set_color(BLUE_E)
        coord_2[3].set_color(RED_E)
        coord_3 = (
            TexMobject(r"(", r"3", r",", r"-1", r")")
            .scale(0.75)
            .next_to(coord_2, 1.5 * DOWN)
        )
        coord_3[1].set_color(BLUE_E)
        coord_3[3].set_color(RED_E)
        # Grupos para el ReplacementT
        pre_coord_1 = VGroup(text_punto_dom_1, text_punto_contra_1)
        pre_coord_2 = VGroup(text_punto_dom_2, text_punto_contra_2)
        pre_coord_3 = VGroup(text_punto_dom_3, text_punto_contra_3)

        punto_graph_1 = Dot(color=GREEN_E).move_to(self.coords_to_point(1, f(1)))
        punto_graph_2 = Dot(color=GREEN_E).move_to(self.coords_to_point(2, f(2)))
        punto_graph_3 = Dot(color=GREEN_E).move_to(self.coords_to_point(3, f(3)))
        puntos_graph = VGroup(punto_graph_1, punto_graph_2, punto_graph_3)

        self.play(Write(text_4))
        self.wait(8)
        self.play(ReplacementTransform(pre_coord_1, coord_1))
        self.play(FadeIn(punto_graph_1))
        self.play(coord_1.move_to, self.coords_to_point(0.8, f(1) + 0.5))
        self.wait(0.5)

        self.play(ReplacementTransform(pre_coord_2, coord_2))
        self.play(FadeIn(punto_graph_2))
        self.play(coord_2.move_to, self.coords_to_point(2.5, f(2) + 0.5))
        self.play(ReplacementTransform(pre_coord_3, coord_3))
        self.play(FadeIn(punto_graph_3))
        self.play(coord_3.move_to, self.coords_to_point(3.8, f(3)))
        self.play(FadeOut(text_4))
        self.play(Write(text_5))
        self.wait(5.375)
        self.play(Write(text_6))
        self.wait(8.75)
        self.play(FadeOut(text_numberline_1), FadeOut(text_numberline_2))
        self.play(FadeOut(coord_1), FadeOut(coord_2), FadeOut(coord_3))
        self.play(ShowCreation(graph))
        self.wait(5)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()
        self.play(Write(text_7))
        self.wait(10)
        self.play(Write(def_1))
        self.wait(13)
        self.play(Write(dt))
        self.wait(13)
        self.play(*[FadeOut(mob) for mob in self.mobjects])


# Visualización de Gráficas (Va después de Gráficas)


def Range(in_val, end_val, step=1):
    return list(np.arange(in_val, end_val + step, step))


### VISUALIZACIÓN DE GRÁFICAS (DIVIDO EN 3 CLASES, PERO ES UN SÓLO VIDEO) ###


# EJEMPLO 1 R -> R#
class Visualización_Gráficas_1(GraphScene, Scene):
    def setup(self):
        Scene.setup(self)
        GraphScene.setup(self)

    CONFIG = {
        "y_max": 20,
        "y_min": 0,
        "x_max": 5,
        "x_min": 0,
        "y_tick_frequency": 1,
        "x_tick_frequency": 1,
        "axes_color": BLUE,
        "graph_origin": np.array((-2.5, -3, 0)),
    }

    def construct(self):

        titulo = TextMobject("Visualización de Gráficas").scale(1.5)

        text1_1 = TextMobject("Recordemos que dada una función")
        text1_2 = TexMobject(
            r"f:A \subset \mathbb{R}^{n} \rightarrow \mathbb{R}^{m}", color=YELLOW
        ).next_to(text1_1, DOWN)
        text1_3 = TextMobject(
            "la gráfica de $f$ es subconjunto de ", "$\mathbb{R}^{n+m}$"
        ).next_to(text1_2, DOWN)
        text1_3[1].set_color(YELLOW)
        text1 = VGroup(text1_1, text1_2, text1_3).move_to(0.5 * UP)

        funcion_1 = TexMobject(
            r"f:A \subset \mathbb{R} \rightarrow \mathbb{R}"
        ).move_to(1 * DOWN)
        funcion_2 = TexMobject(
            r"f:A \subset \mathbb{R}^{2} \rightarrow \mathbb{R}"
        ).next_to(funcion_1, DOWN)
        funcion_3 = TexMobject(
            r"f:A \subset \mathbb{R} \rightarrow \mathbb{R}^{2}"
        ).next_to(funcion_2, DOWN)
        funciones = VGroup(funcion_1, funcion_2, funcion_3)

        text3 = TextMobject("Ahora, veamos algunos ejemplos")

        text4_1 = TextMobject("Consideremos una recta $x=$ ", "$x_0$", ",").move_to(
            3.3 * UP + 2.5 * RIGHT
        )
        text4_2 = TextMobject(
            "¿qué pasa si ", "$x_0$", " pertenece al dominio de $f$?"
        ).next_to(text4_1, DOWN)
        text4_1[1].set_color(GREEN_E)
        text4_2[1].set_color(GREEN_E)
        text4 = VGroup(text4_1, text4_2).scale(0.8)

        text5 = (
            TextMobject(
                """Cada recta intersecta a la gráfica\n
                                en un sólo punto """
            )
            .move_to(3.3 * UP + 2.5 * RIGHT)
            .scale(0.8)
        )
        text6 = (
            TextMobject(
                """¿Qué pasará si $x_0$ no pertenece\n
                             al dominio de $f$?"""
            )
            .move_to(3.3 * UP + 2.5 * RIGHT)
            .scale(0.8)
        )

        # PRIMERA CAJA
        funciones.bg = SurroundingRectangle(
            funciones, buff=0.8 * SMALL_BUFF, color=WHITE
        )
        Caja = VGroup(funciones.bg, funciones)

        # CAJA UPPER LEFT PRE EJEMPLO

        funciones_copy_0 = funciones.copy().to_corner(UL)
        funciones_copy_0.bg = SurroundingRectangle(
            funciones_copy_0, buff=0.8 * SMALL_BUFF, color=WHITE
        )
        Caja_0 = VGroup(funciones_copy_0.bg, funciones_copy_0)

        # CAJA EJEMPLO 1

        funcion_1_1 = TexMobject(
            r"f:A \subset \mathbb{R} \rightarrow \mathbb{R}", color=YELLOW
        )
        funcion_2_1 = TexMobject(
            r"f:A \subset \mathbb{R}^{2} \rightarrow \mathbb{R}"
        ).next_to(funcion_1_1, DOWN)
        funcion_3_1 = TexMobject(
            r"f:A \subset \mathbb{R} \rightarrow \mathbb{R}^{2}"
        ).next_to(funcion_2_1, DOWN)
        funciones_1 = VGroup(funcion_1_1, funcion_2_1, funcion_3_1).to_corner(UL)
        funciones_1.bg = SurroundingRectangle(
            funciones_1, buff=0.8 * SMALL_BUFF, color=WHITE
        )
        Caja_1 = VGroup(funciones_1.bg, funciones_1)

        # Texto ejemplo función
        ejemplo_1_1 = TexMobject(r"f(x)=x^{2}", color=YELLOW)
        ejemplo_1_2 = TexMobject(
            r"G_{f}:=\{(x,f(x))\in \mathbb{R}^{2}|x\in[0,4]\}", color=YELLOW
        ).next_to(ejemplo_1_1, DOWN)
        ejemplo_1 = VGroup(ejemplo_1_1, ejemplo_1_2).move_to(2.8 * UP + 2 * RIGHT)
        # OBJETOS PARA EJEMPLO 1
        dot_1_1 = Dot().set_color(WHITE).move_to(np.array((1.1, -1.8, 0)))
        dot_1_x1 = Dot().set_color(WHITE).move_to(np.array((1.1, -3, 0)))
        dot_1_y1 = Dot().set_color(WHITE).move_to(np.array((-2.5, -1.8, 0)))
        linea_1_x1 = DashedLine(dot_1_x1.get_top(), dot_1_1.get_bottom(), buff=0.1)
        linea_1_x1.set_color(WHITE)
        linea_1_y1 = DashedLine(dot_1_y1.get_right(), dot_1_1.get_left(), buff=0.1)
        linea_1_y1.set_color(WHITE)
        text_dot_1_x1 = (
            TexMobject(r"x=2").move_to(dot_1_x1.get_bottom() + 0.5 * DOWN).scale(0.75)
        )
        text_dot_1_y1 = (
            TexMobject(r"f(2)=4").move_to(dot_1_y1.get_left() + 1.2 * LEFT).scale(0.75)
        )
        text_dot_1_1 = (
            TexMobject(r"(2,f(2))")
            .move_to(dot_1_1.get_top() + 0.4 * UP + 0.5 * LEFT)
            .scale(0.75)
        )

        dot_1_2 = Dot().set_color(WHITE).move_to(np.array((2.9, -0.3, 0)))
        dot_1_x2 = Dot().set_color(WHITE).move_to(np.array((2.9, -3, 0)))
        dot_1_y2 = Dot().set_color(WHITE).move_to(np.array((-2.5, -0.3, 0)))
        linea_1_x2 = DashedLine(dot_1_x2.get_top(), dot_1_2.get_bottom(), buff=0.1)
        linea_1_x2.set_color(WHITE)
        linea_1_y2 = DashedLine(dot_1_y2.get_right(), dot_1_2.get_left(), buff=0.1)
        linea_1_y2.set_color(WHITE)
        text_dot_1_x2 = (
            TexMobject(r"x=3").move_to(dot_1_x2.get_bottom() + 0.5 * DOWN).scale(0.75)
        )
        text_dot_1_y2 = (
            TexMobject(r"f(3)=9").move_to(dot_1_y2.get_left() + 1.2 * LEFT).scale(0.75)
        )
        text_dot_1_2 = (
            TexMobject(r"(3,f(3))")
            .move_to(dot_1_2.get_top() + 0.4 * UP + 0.5 * LEFT)
            .scale(0.75)
        )

        text_dots_1_1 = VGroup(text_dot_1_1, text_dot_1_2)
        text_dots_1_2 = (
            TextMobject(
                """$(2,f(2))\\in G_{f}$ \n 
                                    $(3,f(3))\\in G_{f}$"""
            )
            .to_edge(LEFT)
            .scale(0.75)
        )
        text_grafica_1 = TexMobject(r"G_{f}", color=YELLOW).move_to(
            ejemplo_1.get_bottom() + 0.75 * DOWN + 3 * RIGHT
        )

        ###Rectas verticales
        dot_dom_1 = Dot().set_color(GREEN_E).move_to((1.5, -3.0, 0))
        dot_dom_2 = Dot().set_color(GREEN_E).move_to((4, -3.0, 0))
        dot_func_1 = Dot().move_to((1.5, -1.5, 0))
        dot_func_2 = Dot().move_to((4, 0.9, 0))
        linea_vert_1 = Line((1.5, -3.5, 0), (1.5, 1.5, 0)).set_color(GREEN_E)
        linea_vert_2 = Line((4, -3.5, 0), (4, 1.5, 0)).set_color(GREEN_E)
        RectVert = VGroup(
            dot_dom_1, dot_dom_2, dot_func_1, dot_func_2, linea_vert_1, linea_vert_2
        )
        # Secuencia de Animación
        self.play(Write(titulo))
        self.wait(3)
        self.play(FadeOut(titulo))
        self.play(Write(text1))
        self.wait(9)
        self.play(FadeOut(text1))
        self.play(Write(text3))
        self.wait(3)
        self.play(Write(funciones))
        self.wait(0.5)
        self.play(ShowCreation(funciones.bg))
        self.wait(0.5)
        self.play(FadeOut(text3))
        self.play(ReplacementTransform(Caja, Caja_0))
        # EJEMPLO 1
        self.play(ReplacementTransform(Caja_0, Caja_1))
        self.setup_axes(animate=True)
        graph = self.get_graph(lambda x: x ** 2, color=YELLOW, x_min=0, x_max=4)
        self.play(FadeIn(ejemplo_1))
        self.play(
            FadeIn(dot_1_1),
            FadeIn(dot_1_x1),
            FadeIn(text_dot_1_x1),
            FadeIn(dot_1_y1),
            FadeIn(text_dot_1_y1),
        )
        self.wait(2)
        self.play(ShowCreation(linea_1_x1), ShowCreation(linea_1_y1))
        self.play(FadeIn(text_dot_1_1))
        self.wait(2)
        self.play(
            FadeIn(dot_1_2),
            FadeIn(dot_1_x2),
            FadeIn(text_dot_1_x2),
            FadeIn(dot_1_y2),
            FadeIn(text_dot_1_y2),
        )
        self.wait(2)
        self.play(ShowCreation(linea_1_x2), ShowCreation(linea_1_y2))
        self.play(FadeIn(text_dot_1_2))
        self.wait(2)
        self.play(
            FadeOut(text_dot_1_x1),
            FadeOut(text_dot_1_x2),
            FadeOut(text_dot_1_y1),
            FadeOut(text_dot_1_y2),
        )
        self.play(ReplacementTransform(text_dots_1_1, text_dots_1_2))
        self.wait(3)
        self.play(
            FadeOut(linea_1_x1),
            FadeOut(linea_1_x2),
            FadeOut(linea_1_y1),
            FadeOut(linea_1_y2),
            FadeOut(dot_1_x1),
            FadeOut(dot_1_x2),
            FadeOut(dot_1_y1),
            FadeOut(dot_1_y2),
        )
        self.play(ShowCreation(graph), run_time=3)
        self.play(FadeIn(text_grafica_1))
        self.wait()
        self.play(
            FadeOut(ejemplo_1),
            FadeOut(dot_1_1),
            FadeOut(dot_1_2),
            FadeOut(text_dots_1_2),
        )
        self.play(Write(text4))
        self.wait(6.5)
        self.play(FadeIn(dot_dom_1))
        self.play(ShowCreation(linea_vert_1))
        self.play(FadeOut(text4))
        self.play(FadeIn(text5))
        self.wait(5)
        self.play(FadeIn(dot_func_1))
        self.play(FadeIn(dot_dom_2))
        self.play(ShowCreation(linea_vert_2))
        self.play(FadeIn(dot_func_2))
        self.wait(2.5)
        self.play(FadeOut(RectVert))
        self.play(FadeOut(text5))
        self.play(FadeIn(text6))
        self.wait(7)
        self.play(
            FadeOut(text_grafica_1), FadeOut(self.axes), FadeOut(graph), FadeOut(text6)
        )


# EJEMPLO 2 R^2 -> R#
class Visualización_Gráficas_2(ThreeDScene, Scene):
    def setup(self):
        Scene.setup(self)
        ThreeDScene.setup(self)

    def acomodar_textos(self, objeto):
        self.add_fixed_in_frame_mobjects(objeto)
        self.play(Write(objeto))

    def FadeOutWrite3D(self, objeto1, objeto2):
        self.play(FadeOut(objeto1))
        self.acomodar_textos(objeto2)

    def punto3D(self):
        bola = ParametricSurface(
            lambda u, v: np.array(
                [
                    0.075 * np.cos(v) * np.sin(u),
                    0.075 * np.sin(v) * np.sin(u),
                    0.075 * np.cos(u),
                ]
            ),
            v_min=0,
            v_max=TAU,
            u_min=0.001,
            u_max=PI - 0.001,
            resolution=(12, 24),
            fill_opacity=1,
            stroke_color=GREEN_E,
            fill_color=GREEN_E,
        )
        return bola

    def punto3D_2(self):
        bola = ParametricSurface(
            lambda u, v: np.array(
                [
                    0.075 * np.cos(v) * np.sin(u),
                    0.075 * np.sin(v) * np.sin(u),
                    0.075 * np.cos(u),
                ]
            ),
            v_min=0,
            v_max=TAU,
            u_min=0.001,
            u_max=PI - 0.001,
            resolution=(12, 24),
            fill_opacity=1,
            stroke_color=GOLD_E,
            fill_color=GOLD_E,
        )
        return bola

    def construct(self):

        # Caja Ejemplo 1 (Para transición de cajas)
        funcion_1_1 = TexMobject(
            r"f:A \subset \mathbb{R} \rightarrow \mathbb{R}", color=YELLOW
        )
        funcion_2_1 = TexMobject(
            r"f:A \subset \mathbb{R}^{2} \rightarrow \mathbb{R}"
        ).next_to(funcion_1_1, DOWN)
        funcion_3_1 = TexMobject(
            r"f:A \subset \mathbb{R} \rightarrow \mathbb{R}^{2}"
        ).next_to(funcion_2_1, DOWN)
        funciones_1 = VGroup(funcion_1_1, funcion_2_1, funcion_3_1).to_corner(UL)
        funciones_1.bg = SurroundingRectangle(
            funciones_1, buff=0.8 * SMALL_BUFF, color=WHITE
        )
        Caja_1 = VGroup(funciones_1.bg, funciones_1)

        # CAJA EJEMPLO 2
        funcion_1_2 = TexMobject(r"f:A \subset \mathbb{R} \rightarrow \mathbb{R}")
        funcion_2_2 = TexMobject(
            r"f:A \subset \mathbb{R}^{2} \rightarrow \mathbb{R}", color=YELLOW
        ).next_to(funcion_1_2, DOWN)
        funcion_3_2 = TexMobject(
            r"f:A \subset \mathbb{R} \rightarrow \mathbb{R}^{2}"
        ).next_to(funcion_2_2, DOWN)
        funciones_2 = VGroup(funcion_1_2, funcion_2_2, funcion_3_2).to_corner(UL)
        funciones_2.bg = SurroundingRectangle(
            funciones_2, buff=0.8 * SMALL_BUFF, color=WHITE
        )
        Caja_2 = VGroup(funciones_2.bg, funciones_2)

        # EJEMPLO 2

        ejemplo_2_1 = TexMobject(r"f(x,y)=\sin(x)\cos(y)", color=YELLOW)
        ejemplo_2_2 = TexMobject(
            r"G_{f}:=\{(x,y,f(x,y))\in \mathbb{R}^{3}|(x,y)\in A\}", color=YELLOW
        ).next_to(ejemplo_2_1, DOWN)
        ejemplo_2 = (
            VGroup(ejemplo_2_1, ejemplo_2_2).move_to(3.3 * UP + 3.6 * RIGHT).scale(0.8)
        )

        ###Líneas verticales
        text_1 = TextMobject(
            "Consideremos una recta $(x,y,z)=($",
            "$x_0$",
            ",",
            "$y_0$",
            "$,0)+\\alpha\\hat{z}$, con $\\alpha\\in\\mathbb{R}$",
        ).move_to(3.5 * UP + 2 * RIGHT)
        text_1[1].set_color(GREEN_E)
        text_1[3].set_color(GREEN_E)
        text_1_1 = TextMobject(
            "¿qué pasa si ", "$(x_0,y_0)$", " pertence al dominio de $f$?"
        ).next_to(text_1, DOWN)
        text_1_1[1].set_color(GREEN_E)
        text_1 = VGroup(text_1, text_1_1).scale(0.7)

        text_2 = (
            TextMobject("La recta intersecta  la gráfica en un sólo punto")
            .move_to(3.3 * UP + 2 * RIGHT)
            .scale(0.6)
        )
        text_3 = (
            TextMobject(
                "¿Qué pasará si ", "$(x_0,y_0)$", " no pertence al dominio de $f$?"
            )
            .move_to(3.3 * UP + 2 * RIGHT)
            .scale(0.6)
        )
        text_3[1].set_color(GREEN_E)
        Superficie = ParametricSurface(
            lambda u, v: np.array([u, v, np.sin(u) * np.cos(v)]),
            v_min=-2.5,
            v_max=4,
            u_min=-3,
            u_max=5,
            checkerboard_colors=[GOLD_E, GOLD_E],
            resolution=(20, 50),
        )
        Superficie2 = ParametricSurface(
            lambda u, v: np.array([u, v, np.sin(u) * np.cos(v)]),
            v_min=-2.5,
            v_max=4,
            u_min=-3,
            u_max=5,
            checkerboard_colors=[GOLD_E, GOLD_E],
            resolution=(20, 50),
            fill_opacity=0.5,
        )

        axes = ThreeDAxes(
            x_min=-3, x_max=6, y_min=-3, y_max=6, z_min=-3, z_max=3, num_axis_pieces=40
        )
        # Creo que es redundante lo del color=WHITE en los Dot, pero no importa
        dot_2_1 = Dot().set_color(RED).move_to(np.array((3 * PI / 2, 2.5, 0.8)))
        dot_2_x1 = Dot().set_color(WHITE).move_to(np.array((3 * PI / 2, 0, 0)))
        dot_2_y1 = Dot().set_color(WHITE).move_to(np.array((0, 2.5, 0)))
        dot_2_z1 = Dot().set_color(WHITE).move_to(np.array((0, 0, 0.8)))
        dot_2_xy1 = Dot().set_color(WHITE).move_to(np.array((3 * PI / 2, 2.5, 0)))
        linea_2_x1 = DashedLine(
            dot_2_x1.get_center(), dot_2_xy1.get_center(), buff=0.1, rate=0.25
        )
        linea_2_x1.set_color(WHITE)
        linea_2_y1 = DashedLine(dot_2_y1.get_center(), dot_2_xy1.get_center(), buff=0.1)
        linea_2_y1.set_color(WHITE)
        linea_2_z1 = DashedLine(dot_2_z1.get_center(), dot_2_1.get_center(), buff=0.1)
        linea_2_z1.set_color(WHITE)
        linea_2_xy1 = DashedLine(dot_2_xy1.get_center(), dot_2_1.get_center(), buff=0.1)
        linea_2_xy1.set_color(WHITE)
        text_dot_2_x1 = (
            TexMobject(r"x=\frac{3\pi}{2}")
            .move_to(dot_2_x1.get_top() + 0.5 * UP)
            .scale(0.75)
        )
        text_dot_2_y1 = (
            TexMobject(r"y=2.5").move_to(dot_2_y1.get_left() + 1 * RIGHT).scale(0.75)
        )
        text_dot_2_z1 = (
            TexMobject(r"f(x,y)=0.8")
            .move_to(dot_2_z1.get_left() + 1.5 * LEFT)
            .scale(0.75)
        )
        text_dot_2_1 = (
            TexMobject(r"(x,y,f(x,y))", color=RED)
            .move_to(dot_2_1.get_right() + 0.8 * UP)
            .scale(0.75)
        )
        text_dot_2_xy1 = (
            TexMobject(r"(x,y)\in A")
            .move_to(dot_2_xy1.get_top() + 0.5 * RIGHT + 0.5 * UP)
            .scale(0.75)
        )
        gpo_coordxy_2_1 = VGroup(text_dot_2_x1, text_dot_2_y1)
        gpo_coordxyz_2_1 = VGroup(text_dot_2_xy1, text_dot_2_z1)

        text_grafica_2 = TexMobject(r"G_{f}", color=GOLD_E).move_to(
            4.75 * RIGHT + 1 * DOWN
        )
        ###Objetos Rectas

        dot_dom_1 = self.punto3D().move_to((PI / 2, 0, 0))
        dot_func_1 = self.punto3D_2().move_to((PI / 2, 0, 1))
        dot_dom_2 = self.punto3D().move_to((0, 5, 0))
        linea_vert_1 = Line((PI / 2, 0, -3), (PI / 2, 0, 3)).set_color(GREEN_E)
        linea_vert_2 = Line((0, 5, -3), (0, 5, 3)).set_color(GREEN_E)
        RectVert = VGroup(dot_dom_1, dot_dom_2, dot_func_1, linea_vert_1)

        # EJEMPLO 2
        self.add(Caja_1)
        self.wait(0.5)
        self.play(ReplacementTransform(Caja_1, Caja_2))
        self.add_fixed_in_frame_mobjects(Caja_2)
        self.play(FadeIn(ejemplo_2))
        self.add_fixed_in_frame_mobjects(ejemplo_2)
        self.set_camera_orientation(phi=55 * DEGREES, theta=-50 * DEGREES, distance=50)
        self.play(ShowCreation(axes))
        self.wait()
        self.play(FadeIn(dot_2_x1), FadeIn(text_dot_2_x1))
        self.wait(1.5)
        self.play(FadeIn(dot_2_y1), FadeIn(text_dot_2_y1))
        self.wait(1.5)
        self.play(FadeIn(dot_2_z1), FadeIn(text_dot_2_z1))
        self.wait(1.5)
        self.begin_ambient_camera_rotation(rate=0.04)
        self.play(
            FadeIn(dot_2_xy1), ReplacementTransform(gpo_coordxy_2_1, text_dot_2_xy1)
        )
        self.play(FadeIn(linea_2_x1))
        self.play(FadeIn(linea_2_y1))
        self.play(FadeIn(dot_2_1))
        self.play(FadeIn(linea_2_xy1), FadeIn(linea_2_z1))
        self.wait(2)
        self.play(ReplacementTransform(gpo_coordxyz_2_1, text_dot_2_1))
        self.wait(3.5)
        self.play(
            FadeOut(dot_2_xy1),
            FadeOut(dot_2_x1),
            FadeOut(dot_2_y1),
            FadeOut(dot_2_z1),
            FadeOut(linea_2_x1),
            FadeOut(linea_2_xy1),
            FadeOut(linea_2_y1),
            FadeOut(linea_2_z1),
            FadeOut(text_dot_2_1),
        )
        self.play(ShowCreation(Superficie))
        self.add_fixed_in_frame_mobjects(text_grafica_2)
        self.wait(23)
        self.stop_ambient_camera_rotation()
        self.play(FadeOut(dot_2_1), FadeOut(text_grafica_2), FadeOut(ejemplo_2))
        self.wait()
        self.acomodar_textos(text_1)
        self.wait(12)
        self.move_camera(
            phi=75 * DEGREES, theta=-50 * DEGREES, distance=50, frame_center=[0, 0, 1]
        )
        self.play(ReplacementTransform(Superficie, Superficie2))
        self.begin_ambient_camera_rotation(rate=0.04)
        self.play(FadeIn(dot_dom_1))
        self.play(ShowCreation(linea_vert_1))
        self.FadeOutWrite3D(text_1, text_2)
        self.play(FadeIn(dot_func_1))
        self.wait(4.5)
        self.play(FadeOut(dot_dom_1), FadeOut(dot_func_1), FadeOut(linea_vert_1))
        self.FadeOutWrite3D(text_2, text_3)
        self.wait(5)
        self.play(FadeIn(dot_dom_2))
        self.wait(1.5)
        self.play(ShowCreation(linea_vert_2))
        self.stop_ambient_camera_rotation
        self.wait(5)
        self.play(
            FadeOut(axes),
            FadeOut(Superficie2),
            FadeOut(text_3),
            FadeOut(dot_dom_2),
            FadeOut(linea_vert_2),
        )


# EJEMPLO 3 R -> R^2#
class Visualización_Gráficas_3(ThreeDScene, Scene):
    def setup(self):
        Scene.setup(self)
        ThreeDScene.setup(self)

    def FadeOutWrite3D(self, objeto1, objeto2):
        self.play(FadeOut(objeto1))
        self.acomodar_textos(objeto2)

    def acomodar_textos(self, objeto):
        self.add_fixed_in_frame_mobjects(objeto)
        self.play(Write(objeto))

    def construct(self):

        # CAJA EJEMPLO 2
        funcion_1_2 = TexMobject(r"f:A \subset \mathbb{R} \rightarrow \mathbb{R}")
        funcion_2_2 = TexMobject(
            r"f:A \subset \mathbb{R}^{2} \rightarrow \mathbb{R}", color=YELLOW
        ).next_to(funcion_1_2, DOWN)
        funcion_3_2 = TexMobject(
            r"f:A \subset \mathbb{R} \rightarrow \mathbb{R}^{2}"
        ).next_to(funcion_2_2, DOWN)
        funciones_2 = VGroup(funcion_1_2, funcion_2_2, funcion_3_2).to_corner(UL)
        funciones_2.bg = SurroundingRectangle(
            funciones_2, buff=0.8 * SMALL_BUFF, color=WHITE
        )
        Caja_2 = VGroup(funciones_2.bg, funciones_2)

        # Caja ejemplo 3
        funcion_1_3 = TexMobject(r"f:A \subset \mathbb{R} \rightarrow \mathbb{R}")
        funcion_2_3 = TexMobject(
            r"f:A \subset \mathbb{R}^{2} \rightarrow \mathbb{R}"
        ).next_to(funcion_1_3, DOWN)
        funcion_3_3 = TexMobject(
            r"f:A \subset \mathbb{R} \rightarrow \mathbb{R}^{2}", color=YELLOW
        ).next_to(funcion_2_3, DOWN)
        funciones_3 = VGroup(funcion_1_3, funcion_2_3, funcion_3_3).to_corner(UL)
        funciones_3.bg = SurroundingRectangle(
            funciones_3, buff=0.8 * SMALL_BUFF, color=WHITE
        )
        Caja_3 = VGroup(funciones_3.bg, funciones_3)

        text_3 = TextMobject(
            """No es común en clase graficar funciones de $\\mathbb{R}\\rightarrow\\mathbb{R}^2$\n
                                por la dificultad de hacer los dibujos en pizarrón"""
        )
        text_4 = TextMobject(
            """Generalmente se trabaja con la imagen de la\n
                                función, dibujando las curvas correspondientes\n
                                 en el plano del contradominio """
        )
        text_5 = TextMobject(
            """En este y otros videos podemos usar\n
                                 la gráfica de este tipo de funciones """
        )

        text_6 = (
            TextMobject("Consideremos algunos puntos de la gráfica")
            .move_to(3.3 * UP + 2 * RIGHT)
            .scale(0.8)
        )
        text_7 = (
            TextMobject(
                """Análogo a los casos anteriores, podemos tomar \n
                                planos paralelos al plano $xy$"""
            )
            .move_to(3.3 * UP + 2 * RIGHT)
            .scale(0.8)
        )
        text_8 = (
            TextMobject(
                """La intersección de la gráfica con estos\n
                                 planos sólo puede ser un punto"""
            )
            .move_to(3.3 * UP + 2 * RIGHT)
            .scale(0.8)
        )
        text_9 = (
            TextMobject(
                """Si fuera más de un punto,\n
                                $f$ no sería función"""
            )
            .move_to(3.3 * UP + RIGHT)
            .scale(0.8)
        )
        text_10 = (
            TextMobject(
                """Si la intersección fuera el vacío,\n
                                 el punto correspondiente en el eje t\n
                                 no sería parte del dominio """
            )
            .move_to(3.3 * UP)
            .scale(0.7)
        )
        # EJEMPLO 3

        ejemplo_3_1 = TexMobject(r"f(t)=\frac{t}{4\pi}(\cos(t),\sin(t))", color=YELLOW)
        ejemplo_3_2 = TexMobject(
            r"G_{f}:=\{(t,f(t))\in \mathbb{R}^{3}|t\in A\}", color=YELLOW
        ).next_to(ejemplo_3_1, DOWN)
        ejemplo_3 = VGroup(ejemplo_3_1, ejemplo_3_2).move_to(3.2 * UP).scale(0.65)

        ejemplo_3_10 = ejemplo_3.copy().move_to(3.2 * UP + 4 * RIGHT)

        # EJES
        axes_2 = ThreeDAxes(
            x_min=-3.5,
            x_max=3.2,
            y_min=-3.5,
            y_max=3.5,
            z_min=0,
            z_max=5 * PI,
            num_axis_pieces=30,
        )

        # AQUÍ VAN TODAS LOS PLANOS, PUNTOS Y LA CURVA
        curva_1 = ParametricFunction(
            lambda u: np.array(
                [(u / (4 * PI)) * math.cos(u), (u / (4 * PI)) * math.sin(u), u]
            ),
            color=YELLOW,
            t_min=0,
            t_max=4 * PI,
        )

        plano_1 = ParametricSurface(
            lambda u, v: np.array([u, v, PI / 2]),
            v_min=-1.5,
            v_max=1.5,
            u_min=-1.5,
            u_max=1.5,
            fill_color=BLUE_E,
            fill_opacity=0.25,
            resolution=(1, 1),
        )

        punto_1 = Dot(color=RED).move_to((0, 1 * 1 * PI / (8 * PI), PI / 2))

        plano_2 = ParametricSurface(
            lambda u, v: np.array([u, v, PI]),
            v_min=-1.5,
            v_max=1.5,
            u_min=-1.5,
            u_max=1.5,
            fill_color=TEAL_E,
            fill_opacity=0.25,
            resolution=(1, 1),
        )

        punto_2 = Dot(color=RED).move_to((-1 * 2 * PI / (8 * PI), 0, PI))

        plano_3 = ParametricSurface(
            lambda u, v: np.array([u, v, 3 * PI / 2]),
            v_min=-1.5,
            v_max=1.5,
            u_min=-1.5,
            u_max=1.5,
            fill_color=GREEN_E,
            fill_opacity=0.25,
            resolution=(1, 1),
        )

        punto_3 = Dot(color=RED).move_to((0, -1 * 3 * PI / (8 * PI), 3 * PI / 2))

        plano_4 = ParametricSurface(
            lambda u, v: np.array([u, v, 2 * PI]),
            v_min=-1.5,
            v_max=1.5,
            u_min=-1.5,
            u_max=1.5,
            fill_color=YELLOW_E,
            fill_opacity=0.25,
            resolution=(1, 1),
        )

        punto_4 = Dot(color=RED).move_to((1 * 4 * PI / (8 * PI), 0, 4 * PI / 2))

        plano_5 = ParametricSurface(
            lambda u, v: np.array([u, v, 5 * PI / 2]),
            v_min=-1.5,
            v_max=1.5,
            u_min=-1.5,
            u_max=1.5,
            fill_color=GOLD_E,
            fill_opacity=0.25,
            resolution=(1, 1),
        )

        punto_5 = Dot(color=RED).move_to((0, 1 * 5 * PI / (8 * PI), 5 * PI / 2))

        plano_6 = ParametricSurface(
            lambda u, v: np.array([u, v, 3 * PI]),
            v_min=-1.5,
            v_max=1.5,
            u_min=-1.5,
            u_max=1.5,
            fill_color=RED_E,
            fill_opacity=0.25,
            resolution=(1, 1),
        )

        punto_6 = Dot(color=RED).move_to((-1 * 6 * PI / (8 * PI), 0, 6 * PI / 2))

        plano_7 = ParametricSurface(
            lambda u, v: np.array([u, v, 7 * PI / 2]),
            v_min=-1.5,
            v_max=1.5,
            u_min=-1.5,
            u_max=1.5,
            fill_color=MAROON_E,
            fill_opacity=0.25,
            resolution=(1, 1),
        )

        punto_7 = Dot(color=RED).move_to((0, -1 * 7 * PI / (8 * PI), 7 * PI / 2))

        plano_8 = ParametricSurface(
            lambda u, v: np.array([u, v, 8 * PI / 2]),
            v_min=-1.5,
            v_max=1.5,
            u_min=-1.5,
            u_max=1.5,
            fill_color=PURPLE_E,
            fill_opacity=0.25,
            resolution=(1, 1),
        )

        punto_8 = Dot(color=RED).move_to((1 * 8 * PI / (8 * PI), 0, 8 * PI / 2))

        plano_9 = ParametricSurface(
            lambda u, v: np.array([u, v, 9 * PI / 2]),
            v_min=-1.5,
            v_max=1.5,
            u_min=-1.5,
            u_max=1.5,
            fill_color=PURPLE_E,
            fill_opacity=0.25,
            resolution=(1, 1),
        )

        planos = VGroup(
            plano_1, plano_2, plano_3, plano_4, plano_5, plano_6, plano_7, plano_8
        )
        puntos = VGroup(
            punto_1, punto_2, punto_3, punto_4, punto_5, punto_6, punto_7, punto_8
        )
        # Etiquetas ejes
        # POR EL MOVIMIENTO DE CÁMARA, TUVE QUE HACER VARIOS DEL MISMO
        eje_x_1 = TexMobject(r"x").scale(0.75).move_to((3.2, 0.25, 0))
        eje_x_2 = TexMobject(r"x").scale(0.75).move_to((-2.6, 1, 0))
        eje_x_3 = TexMobject(r"x").scale(0.75).move_to((-2.4, 0.75, 0))
        eje_y_1 = TexMobject(r"y").scale(0.75).move_to((0.3, 3.5, 0))
        eje_y_2 = TexMobject(r"y").scale(0.75).move_to((1, -3.3, 0))
        eje_y_3 = TexMobject(r"y").scale(0.75).move_to((1.3, -3.5, 0))
        eje_z_1 = TexMobject(r"t").scale(0.75).move_to((4.7, 2, 0))
        eje_z_2 = TexMobject(r"t").scale(0.75).move_to((4.7, 1.6, 0))
        ejes_1 = VGroup(eje_x_1, eje_y_1)
        ejes_2 = VGroup(eje_x_2, eje_y_2, eje_z_1)
        ejes_3 = VGroup(eje_x_3, eje_y_3, eje_z_2)

        # Etiquetas Planos
        text_plano_1 = TexMobject(r"t_1").move_to((-3.65, -3, 0)).scale(0.75)
        text_plano_2 = TexMobject(r"t_2").move_to((-2.1, -2.4, 0)).scale(0.75)
        text_plano_3 = TexMobject(r"t_3").move_to((-0.62, -1.9, 0)).scale(0.75)
        text_planos_1 = VGroup(text_plano_1, text_plano_2, text_plano_3)
        text_plano_4 = TexMobject(r"t_4").move_to((0.7, -1.4, 0)).scale(0.75)
        text_plano_5 = TexMobject(r"t_5").move_to((2, -1, 0)).scale(0.75)
        text_plano_6 = TexMobject(r"t_6").move_to((3.15, -0.5, 0)).scale(0.75)
        text_plano_7 = TexMobject(r"t_7").move_to((4.25, -0.05, 0)).scale(0.75)
        text_plano_8 = TexMobject(r"t_8").move_to((5.2, 0.4, 0)).scale(0.75)
        text_planos_2 = VGroup(
            text_plano_4,
            text_plano_5,
            text_plano_6,
            text_plano_7,
            text_plano_8,
            text_plano_1,
            text_plano_2,
            text_plano_3,
        )
        text_planos_i = (
            TexMobject(r"\forall i, t_i \in A").move_to((4, -2.5, 0)).scale(1.25)
        )

        text_grafica_3 = TexMobject(r"G_{f}", color=YELLOW).move_to(
            eje_z_2.get_left() + 2.5 * LEFT
        )

        # EJEMPLO 3
        self.add(Caja_2)
        self.wait(0.5)
        self.play(ReplacementTransform(Caja_2, Caja_3))
        self.add_fixed_in_frame_mobjects(Caja_3)
        self.play(Write(text_3))
        self.wait(9.5)
        self.play(FadeOut(text_3))
        self.play(Write(text_4))
        self.wait(8.5)
        self.play(FadeOut(text_4))
        self.play(Write(text_5))
        self.wait(7.2)
        self.play(FadeOut(text_5))
        self.wait(0.5)
        self.play(FadeIn(ejemplo_3_10))
        self.set_camera_orientation(phi=0)
        self.play(ShowCreation(axes_2), FadeIn(ejes_1))
        self.wait(0.5)
        self.play(ShowCreation(curva_1))
        self.wait(19)
        self.play(FadeOut(ejes_1), FadeOut(ejemplo_3_10))
        self.move_camera(
            phi=142 * DEGREES,
            theta=55 * DEGREES,
            gamma=-60 * DEGREES,
            frame_center=(0.5, 0, 5),
            run_time=3,
        )
        self.acomodar_textos(ejes_2)
        self.wait(2.5)
        self.acomodar_textos(text_6)
        self.wait(4)
        self.play(FadeOut(curva_1), FadeIn(puntos))
        self.wait(0.5)
        self.play(FadeOut(ejes_2))
        self.move_camera(
            phi=115 * DEGREES,
            theta=32 * DEGREES,
            gamma=-70 * DEGREES,
            frame_center=(0, -0.1, 6),
            run_time=2,
        )
        self.wait()
        self.FadeOutWrite3D(text_6, text_7)
        self.wait(6.5)
        self.play(FadeIn(plano_1))
        self.acomodar_textos(text_plano_1)
        self.acomodar_textos(text_planos_i)
        self.play(FadeIn(plano_2))
        self.acomodar_textos(text_plano_2)
        self.FadeOutWrite3D(text_7, text_8)
        self.wait(6.5)
        self.play(FadeIn(plano_3))
        self.acomodar_textos(text_plano_3)
        self.play(FadeIn(plano_4))
        self.acomodar_textos(text_plano_4)
        self.FadeOutWrite3D(text_8, text_9)
        self.wait(5.7)
        self.play(FadeIn(plano_5))
        self.acomodar_textos(text_plano_5)
        self.play(FadeIn(plano_6))
        self.acomodar_textos(text_plano_6)
        self.FadeOutWrite3D(text_9, text_10)
        self.wait(8.75)
        self.play(FadeIn(plano_7))
        self.acomodar_textos(text_plano_7)
        self.play(FadeIn(plano_8))
        self.acomodar_textos(text_plano_8)
        self.play(FadeIn(plano_9))
        self.play(ShowCreation(curva_1), run_time=2)
        self.wait(2)
        self.play(FadeOut(plano_9))
        self.play(FadeOut(text_planos_2), FadeOut(text_planos_i), FadeOut(text_10))
        self.move_camera(
            phi=142 * DEGREES,
            theta=55 * DEGREES,
            gamma=-60 * DEGREES,
            frame_center=(0, -0.8, 5),
            run_time=2,
        )
        self.acomodar_textos(ejes_3)
        self.wait(2.5)
        self.play(FadeOut(planos))
        self.acomodar_textos(text_grafica_3)
        self.wait(3)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()


########################################
## DEFINICION DE CONJUNTOS DE NIVEL ####
########################################


def Range(in_val, end_val, step=1):
    return list(np.arange(in_val, end_val + step, step))


class ConjNiv_Def(GraphScene, Scene):
    CONFIG = {
        "y_max": 2,
        "y_min": -2,
        "x_max": 4 * PI,
        "x_min": -4 * PI,
        "y_tick_frequency": 0.5,
        "x_tick_frequency": PI / 2,
        "graph_origin": ORIGIN,
        "y_axis_label": None,  # Vamos a poner las labels en el self.setup_axes()
        "x_axis_label": "$x$",
    }

    def construct(self):
        titulo = TextMobject("Conjuntos de Nivel").scale(1.5)

        intro_a = TextMobject(
            "Para funciones $f:A\\subset \\mathbb{R}^n \\to \\mathbb{R} $, se"
        ).shift(UP)
        intro_b = TextMobject("""define al conjunto de nivel de $f$ como """).next_to(
            intro_a, DOWN
        )
        intro_c = TextMobject("$N_c(f):=\\{ \\vec{x}\\in A| f(\\vec{x})=c\\}$").next_to(
            intro_b, DOWN
        )
        intro = VGroup(intro_a, intro_b, intro_c)

        # COMENZAMOS CON LA DEFINICIÓN
        # Conjunto abstracto en R^n
        text_1 = TextMobject(
            "Sea",
            " A",
            " el dominio de una función $f:A\\subset \\mathbb{R}^n \\to \\mathbb{R} $",
        ).to_edge(UP)
        text_1[1].set_color(BLUE)

        EjeY_1 = Arrow(start=(0, -1, 0), end=(0, 4, 0), stroke_width=2)
        EjeX_1 = Arrow(start=(-1, 0, 0), end=(4, 0, 0), stroke_width=2)
        label_Rn = TexMobject(r"\mathbb{R}^n").shift(0.5 * RIGHT + 0.5 * DOWN)
        Ejes_1 = VGroup(EjeX_1, EjeY_1, label_Rn).shift(5 * LEFT + 2.5 * DOWN)

        A_svg_1 = SVGMobject("Func_SVGs/enRn.svg").set_height(FRAME_HEIGHT * 0.3)
        A_svg_1.set_style(
            fill_opacity=0.7, stroke_width=0, stroke_opacity=1, fill_color=BLUE
        )
        A_svg_1.shift(DOWN + 3 * LEFT)

        # Construimos nuestro eje real sencillo
        text_2 = TextMobject(
            "Consideremos un número real", " $c$", " $\\in \\mathbb{R}$"
        ).to_edge(UP)
        text_2[1].set_color(RED_C)

        Linea_Eje_Real = DoubleArrow(
            start=(-1, 0, 0), end=(4, 0, 0), stroke_width=2, buff=0.1
        ).shift(2 * RIGHT + DOWN)
        ticks = []
        for i in range(20):
            ticks.append(
                Line(
                    start=(-1 + (2 * i / 10), 0.1, 0),
                    end=(-1 + (2 * i / 10), -0.1, 0),
                    stroke_width=1,
                ).shift(2.6 * RIGHT + DOWN)
            )
        label_R = TexMobject(r"\mathbb{R}").shift(1.5 * DOWN + 2 * RIGHT)
        Eje_Real = VGroup(*ticks, Linea_Eje_Real, label_R)

        dot_c = Dot(point=(2.5, 0, 0), color=RED_C, radius=0.1).shift(2 * RIGHT + DOWN)
        dot_c_dup = Dot(point=(2.5, 0, 0), color=RED_C, radius=0.1).shift(
            2 * RIGHT + DOWN
        )
        label_c = TextMobject("c").set_color(RED_C).next_to(dot_c, 1.5 * DOWN)
        punto_c = VGroup(dot_c, label_c)

        text_3a = TextMobject(
            "Si tomamos todos los puntos ",
            "$\\vec{x}_i$ ",
            "en ",
            "A",
            " que al aplicarles la función",
        ).to_edge(UP)
        text_3a[3].set_color(BLUE)
        text_3b = TextMobject("toman el valor de", " $c$").next_to(text_3a, DOWN)
        text_3b[1].set_color(RED_C)
        text_3 = VGroup(text_3a, text_3b).scale(0.9)

        pto_cn1 = Dot(point=(0, 0, 0)).shift(DOWN + 3 * LEFT)
        pto_cn1_dup = Dot(point=(0, 0, 0)).shift(DOWN + 3 * LEFT)
        pto_cn2 = Dot(point=(0.3, 0.1, 0)).shift(DOWN + 3 * LEFT)
        pto_cn2_dup = Dot(point=(0.3, 0.1, 0)).shift(DOWN + 3 * LEFT)
        pto_cn3 = Dot(point=(-0.5, 0.2, 0)).shift(DOWN + 3 * LEFT)
        pto_cn3_dup = Dot(point=(-0.5, 0.2, 0)).shift(DOWN + 3 * LEFT)

        conjniv = VGroup(pto_cn1, pto_cn2, pto_cn3)
        conjniv_dup = VGroup(pto_cn1_dup, pto_cn2_dup, pto_cn3_dup)

        f_arrow = Arrow(start_point=LEFT, end_point=RIGHT + 2 * DOWN, buff=0.1)
        f_label = TexMobject(r"f").next_to(f_arrow, UP)
        f = VGroup(f_arrow, f_label)

        text_4a = TextMobject(
            "Entonces el conjunto de puntos $\\vec{x}_i$ es el "
        ).to_edge(UP)
        text_4b = TextMobject(
            "conjunto de nivel $c$ de nuestra función: $N_c(f)$"
        ).next_to(text_4a, DOWN)
        text_4 = VGroup(text_4a, text_4b).scale(0.9)

        def_conjniv = TexMobject(
            r"N_c(f):=\{\vec{x}\in A \vert f(\vec{x}) = c \}"
        ).to_edge(UP)
        def_conjniv1 = TextMobject(
            "O, usando la definición de imagen inversa, "
        ).to_edge(UP)
        def_conjniv2 = TexMobject("N_c(f):= f^{-1}(\\{c\\})").next_to(
            def_conjniv1, DOWN
        )
        def_conjniv_group = VGroup(def_conjniv1, def_conjniv2)

        text5 = TextMobject("Veamos un ejemplo")

        ### Secuencia de la animación HASTA ANTES DE DECLARAR LOS EJES
        self.play(Write(titulo))
        self.wait(1.15)
        self.play(FadeOut(titulo))
        self.play(Write(intro_a))
        self.play(Write(intro_b))
        self.play(Write(intro_c))
        self.wait(8)
        self.play(FadeOut(intro))
        self.play(Write(text_1), FadeIn(Ejes_1), FadeIn(A_svg_1))
        self.play(FadeIn(Eje_Real))
        self.wait(4.5)
        self.play(FadeIn(punto_c), ReplacementTransform(text_1, text_2))
        self.wait(3.5)
        self.play(ReplacementTransform(text_2, text_3))
        self.play(ShowCreation(conjniv), ShowCreation(f))
        self.wait(7.7)
        self.play(Transform(conjniv_dup, dot_c_dup), runtime=3)
        self.wait(2)
        self.play(ReplacementTransform(text_3, text_4))
        self.wait(7)
        self.play(ReplacementTransform(text_4, def_conjniv))
        self.wait(4)
        self.play(ReplacementTransform(def_conjniv, def_conjniv_group))
        self.wait(4)
        self.play(
            FadeOut(punto_c),
            FadeOut(conjniv_dup),
            FadeOut(conjniv),
            FadeOut(A_svg_1),
            FadeOut(f),
            FadeOut(Ejes_1),
            FadeOut(Eje_Real),
        )
        self.wait()
        self.play(FadeOut(def_conjniv_group))
        self.play(Write(text5))
        self.wait(2.5)
        self.play(FadeOut(text5))
        """
        A partir de este punto tengo que romper el esquema tradicional de sólo instanciar objetos
        antes de la secuencia de animación. Esto tengo que hacerlo para poder utilizar el método
        coords_to_point() que solo funciona después de declarar los ejes. Si declaro los ejes
        en la sección de objetos, aparecen en toda la animación.
        """

        ##La línea que lo cambia todo (agrega los ejes a la escena)
        self.setup_axes()
        line_1 = Line(
            start=self.coords_to_point(-4 * PI, 1),
            end=self.coords_to_point(4 * PI, 1),
            stroke_width=2,
            color=RED,
        )
        # Ejemplo de funciones R -> R
        text_6 = (
            TextMobject("Obtengamos el conjunto de nivel 1 de ", "$f(x) = \\sin(x)$")
            .to_edge(UP)
            .scale(0.8)
        )
        text_6[1].set_color(YELLOW)
        text_7 = (
            TextMobject("Este conjunto estará contenido en $\\mathbb{R}$")
            .to_edge(UP)
            .scale(0.8)
        )
        text_8 = (
            TexMobject(
                r"N_1(f) = \left\{\frac{\pi}{2}+2k\pi \vert k \in \mathbb{Z} \right\}"
            )
            .to_edge(UP)
            .shift(0.5 * UP)
            .scale(0.8)
        )
        graph_dotlines = []
        for i in range(-2, 2):
            graph_dotlines.append(
                DashedLine(
                    start=self.coords_to_point((PI / 2) + i * 2 * PI, 0),
                    end=self.coords_to_point((PI / 2) + i * 2 * PI, 1),
                )
            )
        Dotlines = VGroup(*graph_dotlines)

        graph_dots = []
        gdots_dup = []
        yellow_dots = []
        for i in range(-2, 2):
            graph_dots.append(
                Dot(point=self.coords_to_point((PI / 2) + i * 2 * PI, 0), radius=0.1)
            )
            gdots_dup.append(
                Dot(point=self.coords_to_point((PI / 2) + i * 2 * PI, 0), radius=0.1)
            )
            yellow_dots.append(
                Dot(
                    point=self.coords_to_point((PI / 2) + i * 2 * PI, 1),
                    radius=0.1,
                    color=YELLOW,
                )
            )
        GraphDots = VGroup(*graph_dots)
        GDotsDup = VGroup(*gdots_dup)
        YellowDots = VGroup(*yellow_dots)

        text_9 = (
            TextMobject("Pues para todo $x \in N_c(f)$, se tiene que $\\sin(x) = 1$")
            .to_edge(UP)
            .scale(0.9)
        )

        """
        DECLARO TODOS LOS OBJETOS EN ESTA SECCIÓN, Y DEPUÉS SIGO CON EL ESQUEMA HABITUAL
        """

        ### Secuencia de la animación DESPUÉS DE DECLARAR LOS EJES
        self.play(
            *[
                Write(objeto)
                for objeto in [
                    self.y_axis,
                    self.x_axis,
                    self.x_axis_labels,
                ]
            ],
            run_time=2
        )
        plotSin = self.get_graph(
            lambda x: np.sin(x),
            color=YELLOW,
            x_min=-4 * PI,
            x_max=4 * PI,
        )
        self.play(ShowCreation(plotSin), run_time=3)
        self.play(Write(text_6))
        self.wait(4.5)
        self.play(ShowCreation(line_1))
        self.wait()
        self.wait(2)
        self.play(ReplacementTransform(text_6, text_7))
        self.wait(3.25)
        self.play(ReplacementTransform(text_7, text_8))
        self.play(ShowCreation(Dotlines))
        self.wait(4)
        self.play(ShowCreation(GraphDots))
        self.wait(2)
        self.play(text_8.shift, 6 * DOWN + 3 * LEFT, runtime=2)
        self.wait(1.5)
        self.play(Write(text_9))
        self.wait(6)
        self.play(Transform(GDotsDup, YellowDots), runtime=4)
        self.wait(3)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()

    """
    AQUI SE CONFIGURAN LOS EJES A DETALLE, NO FORMA PARTE DE LA ANIMACIÓN.
    """

    def setup_axes(self):
        GraphScene.setup_axes(self)
        # Para cambiar el ancho de los ejes
        self.x_axis.set_stroke(width=2)
        self.y_axis.set_stroke(width=2)
        # Etiquetas en Y
        self.y_axis.label_direction = 0.5 * RIGHT + 0.5 * UP
        self.y_axis.add_numbers(*[-1, 1])
        # Lo siguiente es para generar las etiquetas en X automáticamente
        init_val_x = -7 * PI / 2
        step_x = 2 * PI
        end_val_x = 5 * PI / 2
        # Esta función global nos genera una lista de puntos
        values_decimal_x = Range(init_val_x, end_val_x, step_x)
        self.x_axis_labels = VGroup()
        # Los textos que vamos a escribir
        list_x = TexMobject(
            "-\\frac{7\\pi}{2}",  #   -5pi/2
            "-\\frac{3\\pi}{2}",  #   -3pi/2
            "\\frac{\\pi}{2}",  #     pi/2
            "\\frac{5\\pi}{2}",  #     3pi/2
        )
        # Creamos una lista de tuplas, el valor y el símbolo correspondiente
        values_x = [(i, j) for i, j in zip(values_decimal_x, list_x)]

        for x_val, x_tex in values_x:
            x_tex.scale(0.5)
            if x_val == -PI or x_val == PI:  # if x is equals -pi or pi
                x_tex.next_to(self.coords_to_point(x_val, 0), 2 * DOWN)  # Put 2*Down
            else:  # In another case
                x_tex.next_to(self.coords_to_point(x_val, 0), DOWN)
            self.x_axis_labels.add(x_tex)


#############################
###CONJUNTO DE NIVEL EN R3###
#############################
class ConjNiv_R3(ThreeDScene, Scene):
    def setup(self):
        Scene.setup(self)
        ThreeDScene.setup(self)

    def construct(self):

        text_1 = (
            TextMobject(
                "Veamos ahora los conjuntos de nivel de", " $f(x,y) = \\sqrt{x^2+y^2}$"
            )
            .to_edge(DOWN)
            .set_opacity(0)
        )
        text_1[1].set_color(GOLD_E)
        text_1.scale(0.9)

        # Creamos la superficie con f(x,y) = \\sqrt(x^2+y^2)
        superficie = ParametricSurface(
            lambda u, v: np.array([u, v, np.sqrt(u ** 2 + v ** 2)]),
            v_min=-3,
            v_max=3,
            u_min=-3,
            u_max=3,
            fill_opacity=0.75,
            checkerboard_colors=[GOLD_E, GOLD_E],
            resolution=(80, 80),
        )

        text_2 = TextMobject("Consideremos", " $c=2$").to_edge(DOWN).set_opacity(0)
        text_2[1].set_color(RED)
        text_3 = (
            TextMobject("Este conjunto estará contenido en $\mathbb{R}^2$")
            .to_edge(DOWN)
            .set_opacity(0)
        )

        # CREAMOS EL PLANO Z=2
        plano_1 = ParametricSurface(
            lambda u, v: np.array([u, v, 2]),
            v_min=-3,
            v_max=3,
            u_min=-3,
            u_max=3,
            fill_color=RED,
            fill_opacity=0.7,
            checkerboard_colors=[RED, RED],
            resolution=(60, 60),
        )

        # EL CONJUNTO DE NIVEL PARA C=2
        circulo_niv2 = ParametricFunction(
            lambda u: np.array([2 * math.cos(u), 2 * math.sin(u), 2]),
            color=WHITE,
            t_min=0,
            t_max=2 * PI,
        )

        circulo_niv2_dup = ParametricFunction(
            lambda u: np.array([2 * math.cos(u), 2 * math.sin(u), 2]),
            color=WHITE,
            t_min=0,
            t_max=2 * PI,
        )

        circulo_niv2_R2 = ParametricFunction(
            lambda u: np.array([2 * math.cos(u), 2 * math.sin(u), 0]),
            color=WHITE,
            t_min=0,
            t_max=2 * PI,
        )

        conjunto_nivel2 = (
            TexMobject(
                r"N_2(f) = \{ \vec{x} \in \mathbb{R}^2 \vert \Vert \vec{x} \Vert = 2 \}"
            )
            .shift(2 * UP + 3 * RIGHT)
            .scale(0.7)
        )
        conjunto_nivel2_short = (
            TexMobject(r"N_2(f)").shift(1.75 * UP + 1.75 * RIGHT).scale(0.6)
        )
        text_4 = (
            TextMobject("Repitamos lo anterior ahora con ", "$c = 1$")
            .to_edge(DOWN)
            .set_opacity(0)
        )
        text_4[1].set_color(RED)

        plano_2 = ParametricSurface(
            lambda u, v: np.array([u, v, 1]),
            v_min=-3,
            v_max=3,
            u_min=-3,
            u_max=3,
            fill_color=RED,
            fill_opacity=0.5,
            checkerboard_colors=[RED, RED],
            resolution=(60, 60),
        )

        circulo_niv1 = ParametricFunction(
            lambda u: np.array([1 * math.cos(u), 1 * math.sin(u), 1]),
            color=WHITE,
            t_min=0,
            t_max=2 * PI,
        )
        circulo_niv1_dup = ParametricFunction(
            lambda u: np.array([1 * math.cos(u), 1 * math.sin(u), 1]),
            color=WHITE,
            t_min=0,
            t_max=2 * PI,
        )

        circulo_niv1_R2 = ParametricFunction(
            lambda u: np.array([1 * math.cos(u), 1 * math.sin(u), 0]),
            color=WHITE,
            t_min=0,
            t_max=2 * PI,
        )

        conjunto_nivel1 = (
            TexMobject(
                r"N_1(f) = \{ \vec{x} \in \mathbb{R}^2 \vert \Vert \vec{x} \Vert = 1 \}"
            )
            .shift(2 * DOWN + 3 * RIGHT)
            .scale(0.7)
        )
        conjunto_nivel1_short = TexMobject(r"N_1(f)").shift(UP + RIGHT).scale(0.6)
        text_5 = (
            TextMobject("¡Los conjuntos de nivel nos ayudan a esbozar la gráfica!")
            .to_edge(DOWN)
            .set_opacity(0)
            .scale(0.8)
        )

        ## Secuencia de la Animación
        axes = ThreeDAxes(
            x_min=-4, x_max=4, y_min=-4, y_max=4, z_min=-2, z_max=4, num_axis_pieces=40
        )
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES, distance=100)
        self.add_fixed_in_frame_mobjects(text_1)
        self.play(text_1.set_opacity, 1, runtime=2)
        self.play(ShowCreation(axes))
        self.play(ShowCreation(superficie))
        self.wait(5.5)

        # PLANO 1
        self.play(FadeOut(text_1))
        self.add_fixed_in_frame_mobjects(text_2)
        self.play(text_2.set_opacity, 1, runtime=2)
        self.play(ShowCreation(plano_1))
        self.wait(2)
        self.move_camera(
            phi=90 * DEGREES, theta=-90 * DEGREES, frame_center=(0.1, 0, 1)
        )

        self.play(FadeOut(text_2))
        self.add_fixed_in_frame_mobjects(text_3)
        self.play(text_3.set_opacity, 1, runtime=2)
        self.wait(4)

        # CONJUNTO DE NIVEL
        self.play(FadeOut(text_3))
        self.move_camera(phi=0 * DEGREES, theta=-90 * DEGREES, run_time=2)
        self.play(ShowCreation(circulo_niv2), runtime=2)

        self.move_camera(
            phi=75 * DEGREES, theta=-45 * DEGREES, distance=100, run_time=2
        )
        self.play(ReplacementTransform(circulo_niv2_dup, circulo_niv2_R2))
        self.add_foreground_mobjects(superficie)
        self.play(Write(conjunto_nivel2))

        self.play(
            FadeOut(superficie),
            FadeOut(plano_1),
            FadeOut(circulo_niv2),
            FadeOut(circulo_niv2_dup),
        )
        self.move_camera(phi=0 * DEGREES, theta=-90 * DEGREES, run_time=2)
        self.wait(5.5)
        self.play(ReplacementTransform(conjunto_nivel2, conjunto_nivel2_short))

        self.move_camera(
            phi=75 * DEGREES, theta=-45 * DEGREES, distance=100, run_time=2
        )
        self.play(ShowCreation(superficie))
        self.add_fixed_in_frame_mobjects(text_4)
        self.play(text_4.set_opacity, 1, runtime=2)
        self.play(ShowCreation(plano_2))
        self.wait(4)
        self.play(FadeOut(text_4))
        self.move_camera(phi=0 * DEGREES, theta=-90 * DEGREES, run_time=3)
        self.play(ShowCreation(circulo_niv1), runtime=2)
        self.wait()
        self.move_camera(
            phi=75 * DEGREES, theta=-45 * DEGREES, distance=100, run_time=3
        )
        self.play(ReplacementTransform(circulo_niv1_dup, circulo_niv1_R2))

        self.play(
            FadeOut(superficie),
            FadeOut(plano_2),
            FadeOut(circulo_niv1),
            FadeOut(circulo_niv1_dup),
        )
        self.move_camera(phi=0 * DEGREES, theta=-90 * DEGREES, run_time=3)
        self.play(Write(conjunto_nivel1_short))
        self.wait(4)

        self.move_camera(
            phi=75 * DEGREES, theta=-45 * DEGREES, distance=100, run_time=3
        )
        self.play(
            ShowCreation(superficie),
            ShowCreation(circulo_niv1),
            ShowCreation(circulo_niv2),
        )

        self.add_fixed_in_frame_mobjects(text_5)
        self.play(text_5.set_opacity, 1, runtime=2)
        self.wait(4)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait(2)


####IMAGEN INVERSA
class ImgInversa(GraphScene):
    def construct(self):
        titulo = TextMobject("Imagen Inversa")
        # titulo_b = TextMobject("$f: \\mathbb{R}^n \\to \\mathbb{R}^m$").next_to(titulo_a,DOWN)
        # titulo = VGroup(titulo_a, titulo_b)
        text_1a = TextMobject("Sea $f$ una función ").to_edge(UP)
        text_1b = TexMobject(
            r"f: ", "A", r"\subset\mathbb{R}^n \to \mathbb{R}^m"
        ).next_to(text_1a, DOWN)
        text_1b.set_color_by_tex_to_color_map(
            {
                "A": BLUE,
            }
        )
        text_1 = VGroup(text_1a, text_1b)

        ### Todo para ilustrar la "acción" de nuestra función
        EjeY_1 = Arrow(start=(0, -1, 0), end=(0, 4, 0), stroke_width=2)
        EjeX_1 = Arrow(start=(-1, 0, 0), end=(4, 0, 0), stroke_width=2)
        Ejes_1 = VGroup(EjeX_1, EjeY_1).shift(5 * LEFT + 2.5 * DOWN)

        EjeY_2 = Arrow(start=(0, -1, 0), end=(0, 4, 0), stroke_width=2)
        EjeX_2 = Arrow(start=(-1, 0, 0), end=(4, 0, 0), stroke_width=2)
        Ejes_2 = VGroup(EjeX_2, EjeY_2).shift(2 * RIGHT + 2.5 * DOWN)

        A_svg_1 = SVGMobject("Func_SVGs/enRn.svg").set_height(FRAME_HEIGHT * 0.3)
        A_svg_1.set_style(
            fill_opacity=0.7, stroke_width=0, stroke_opacity=1, fill_color=BLUE
        )
        A_svg_1.shift(DOWN + 3 * LEFT)

        A_svg_2 = SVGMobject("Func_SVGs/enRn.svg").set_height(FRAME_HEIGHT * 0.3)
        A_svg_2.set_style(
            fill_opacity=0, stroke_width=0, stroke_opacity=1, fill_color=BLUE
        )
        A_svg_2.shift(DOWN + 3 * LEFT)

        A_svg_2 = SVGMobject("Func_SVGs/enRn.svg").set_height(FRAME_HEIGHT * 0.3)
        A_svg_2.set_style(
            fill_opacity=0, stroke_width=0, stroke_opacity=1, fill_color=BLUE
        )
        A_svg_2.shift(DOWN + 3 * LEFT)

        A_svg_2 = SVGMobject("Func_SVGs/enRn.svg").set_height(FRAME_HEIGHT * 0.3)
        A_svg_2.set_style(
            fill_opacity=0, stroke_width=0, stroke_opacity=1, fill_color=BLUE
        )
        A_svg_2.shift(DOWN + 3 * LEFT)

        A_svg_2 = SVGMobject("Func_SVGs/enRn.svg").set_height(FRAME_HEIGHT * 0.3)
        A_svg_2.set_style(
            fill_opacity=0, stroke_width=0, stroke_opacity=1, fill_color=BLUE
        )
        A_svg_2.shift(DOWN + 3 * LEFT)

        f_arrow = Arrow(start_point=LEFT, end_point=RIGHT, stroke_width=2.5)
        f_label = TexMobject(r"f").next_to(f_arrow, UP)
        f = VGroup(f_arrow, f_label)

        B_svg = SVGMobject("Func_SVGs/enRm.svg").set_height(FRAME_HEIGHT * 0.3)
        B_svg.set_style(
            fill_opacity=0.8, stroke_width=0, stroke_opacity=1, fill_color=ORANGE
        )
        B_svg.shift(0.7 * DOWN + 4 * RIGHT)

        ## Mencionamos y dibujamos el conjunto D en el contradominio
        text_2a = TextMobject(
            "Si nos tomamos un subconjunto", " $D$ ", "en el contradominio"
        ).to_edge(UP)
        text_2a[1].set_color(YELLOW)
        text_2b = (
            TextMobject("(en este caso solamente tres puntos)")
            .scale(0.7)
            .next_to(text_2a, DOWN)
        )
        text_2 = VGroup(text_2a, text_2b).scale(0.9)

        D_1 = Dot(point=(3.2, -1, 0)).set_color(YELLOW)
        D_2 = Dot(point=(3.3, -0.5, 0)).set_color(YELLOW)
        D_3 = Dot(point=(3, -0.8, 0)).set_color(YELLOW)
        D_label = TexMobject(r"D").set_color(YELLOW).next_to(B_svg, UP)
        ## Duplicados de los puntos anteriores para un RepTransform
        D_1dup = Dot(point=(3.2, -1, 0), fill_opacity=0).set_color(YELLOW)
        D_2dup = Dot(point=(3.3, -0.5, 0), fill_opacity=0).set_color(YELLOW)
        D_3dup = Dot(point=(3, -0.8, 0), fill_opacity=0).set_color(YELLOW)

        D = VGroup(D_1, D_2, D_3)
        D_stuff = VGroup(D_1, D_2, D_3, D_label)

        text_3 = TextMobject(
            "Podemos preguntarnos, ¿de qué parte de", " A", " provienen?"
        ).to_edge(UP)
        text_3.set_color_by_tex_to_color_map(
            {
                "A": BLUE,
            }
        )
        ## Ahora si, mencionamos y dibujamos los puntos que son la imagen inversa
        text_4 = TextMobject(
            "Buscamos $\\{\\vec{x}\\in A | f(\\vec{x})\\in D \\}$"
        ).to_edge(UP)
        C_1 = Dot(point=(-3.2, -1, 0)).set_color(RED)
        A_C1D1 = Arrow(start=(-3.2, -1, 0), end=(3.2, -1, 0), stroke_width=2)
        C_2 = Dot(point=(-3.3, -0.5, 0)).set_color(RED)
        A_C2D3 = Arrow(start=(-3.3, -0.5, 0), end=(3, -0.8, 0), stroke_width=2)
        C_3 = Dot(point=(-3, -0.8, 0)).set_color(RED)
        A_C3D2 = Arrow(start=(-3, -0.8, 0), end=(3.3, -0.5, 0), stroke_width=2)
        finv_label = TexMobject(r"f^{-1}(D)").set_color(RED).next_to(A_svg_1, 1.5 * UP)

        finv_stuff = VGroup(C_1, A_C1D1, C_2, A_C2D3, C_3, A_C3D2, finv_label)

        text_5a = TextMobject(
            "$f^{-1}(D)$", "$:=\\{\\vec{x}\\in A | f(\\vec{x})\\in D \\}$"
        ).to_edge(UP)
        text_5a[0].set_color(RED)
        text_5b = TextMobject(
            "a este conjunto se le llama la", " imagen inversa ", "de", " $D$"
        ).next_to(text_5a, DOWN)
        text_5b[1].set_color(RED)
        text_5b[3].set_color(YELLOW)
        text_5 = VGroup(text_5a, text_5b).scale(0.9)

        ### Pasamos al ejemplo
        text_6 = TextMobject("Veamos un ejemplo en $\mathbb{R}^2$").to_edge(UP)
        text_7a = TexMobject(r"f:=[0,1]\times[0,1] \to [0,2]\times[0,2]").to_edge(UP)
        text_7b = TexMobject(r"f(x,y)=(2x,2y)").next_to(text_7a, DOWN)
        text_7 = VGroup(text_7a, text_7b).scale(0.9)

        squareA = (
            Square(side_length=1)
            .set_color(BLUE)
            .move_to((-4.5, -2, 0))
            .set_fill(BLUE, opacity=0.5)
        )
        squareA_dup = (
            Square(side_length=1, fill_opacity=0).set_color(BLUE).move_to((-4.5, -2, 0))
        )
        squareB = (
            Square(side_length=2)
            .set_color(ORANGE)
            .move_to((3, -1.5, 0))
            .set_fill(ORANGE, opacity=0.5)
        )

        ### Cuadrante D
        text_8 = (
            TexMobject(r"\text{Si } ", r"D", r"= [1,2]\times[1,2]")
            .shift(4 * RIGHT + 3 * UP)
            .scale(0.9)
        )
        text_8[1].set_color(YELLOW)
        squareD = (
            Square(side_length=1)
            .set_color(YELLOW)
            .move_to((3.5, -1, 0))
            .set_fill(YELLOW, opacity=0.5)
        )
        squareD_dup = (
            Square(
                side_length=1,
            )
            .set_color(YELLOW)
            .move_to((3.5, -1, 0))
            .set_fill(YELLOW, opacity=0.0)
        )
        ### Cuadrante f^-1(D)
        text_9 = (
            TexMobject(r"f^{-1}(D)", r"= [0.5,1]\times[0.5,1]")
            .shift(4 * LEFT + 3 * UP)
            .scale(0.9)
        )
        text_9[0].set_color(RED)
        square_finv = (
            Square(side_length=0.5)
            .set_color(RED)
            .move_to((-4.25, -1.75, 0))
            .set_fill(RED, opacity=0.5)
        )
        finv_D_arrow = Arrow(
            start=square_finv.get_center(), end=squareD.get_center(), stroke_width=2
        )

        squares = VGroup(
            squareA, squareB, squareD, squareD_dup, square_finv, squareA_dup
        )

        ### Retou
        text_10 = TextMobject(
            "¡Obtén la imagen inversa de los tres cuadrantes restantes!"
        ).to_edge(UP)

        ### Secuencia de la animación
        self.play(Write(titulo.scale(1.5)))
        self.wait(3.5)
        self.play(FadeOut(titulo))
        self.play(Write(text_1))
        self.play(
            ShowCreation(Ejes_1),
            ShowCreation(Ejes_2),
            ShowCreation(A_svg_1),
            ShowCreation(A_svg_2),
        )
        self.wait(6)
        self.play(ShowCreation(f))
        self.wait()
        self.play(ReplacementTransform(A_svg_2, B_svg))
        self.wait()
        self.play(ReplacementTransform(text_1, text_2))
        self.wait(7.6)
        self.play(Write(D))
        self.play(Write(D_label))
        self.wait(2)
        self.play(ReplacementTransform(text_2a, text_3), FadeOut(text_2b))
        self.wait(5)
        self.play(ReplacementTransform(text_3, text_4))
        self.wait(5.3)
        self.play(FadeOut(f))
        self.play(ReplacementTransform(D_1dup, C_1), ShowCreation(A_C1D1))
        self.wait()
        self.play(ReplacementTransform(D_2dup, C_2), ShowCreation(A_C2D3))
        self.wait()
        self.play(ReplacementTransform(D_3dup, C_3), ShowCreation(A_C3D2))
        self.play(Write(finv_label))
        self.wait()
        self.play(ReplacementTransform(text_4, text_5a))
        self.wait(5.3)
        self.play(Write(text_5b))
        self.wait(6)
        self.play(
            FadeOut(text_5),
            FadeOut(finv_stuff),
            FadeOut(D_stuff),
            FadeOut(A_svg_1),
            FadeOut(B_svg),
        )
        self.play(Write(text_6))
        self.wait(3.8)
        self.play(ReplacementTransform(text_6, text_7))
        self.play(ShowCreation(squareA))
        self.wait(10)
        self.play(ShowCreation(f), ReplacementTransform(squareA_dup, squareB))
        self.wait()
        self.play(FadeOut(text_7), Write(text_8))
        self.play(ShowCreation(squareD))
        self.wait(8)
        self.play(Write(text_9))
        self.play(ReplacementTransform(squareD_dup, square_finv), FadeOut(f))
        self.wait(5.7)
        self.play(ShowCreation(finv_D_arrow))
        self.play(FadeOut(text_8), text_9.shift, 4 * RIGHT)
        self.wait(2)
        self.play(ReplacementTransform(text_9, text_10))
        self.wait(5.3)
        self.play(
            FadeOut(squares),
            FadeOut(text_10),
            FadeOut(Ejes_1),
            FadeOut(Ejes_2),
            FadeOut(finv_D_arrow),
        )


####
#### ExtremeValue y Superficies (la que sigue) pertenecen a un mismo video.


class ExtremeValue(GraphScene, Scene):
    def setup(self):
        Scene.setup(self)
        GraphScene.setup(self)

    CONFIG = {
        "x_axis_label": "$x$",
        "y_axis_label": "$y$",
        "y_max": 27,
        "y_min": -27,
        "x_max": 5,
        "x_min": -1,
        "x_labeled_nums": range(-1, 5),
        "y_labeled_nums": range(-27, 28, 9),
        "y_tick_frequency": 3,
        "axes_color": GREEN_C,
        "graph_origin": np.array((-3, 0, 0)),
        "number_scale_val": 0.7,
        "unit_size": 0.5,
    }

    # defining text
    def construct(self):
        extreme = TextMobject("Teorema del Valor Extremo").scale(1.5)
        # Definición intuitiva
        def_intuitiva = TextMobject(
            """De manera intuitiva, este teorema nos dice que si \n
        tenemos una función continua en un conjunto compacto, \n
        esta alcanza sus valores extremos en dicho conjunto, \n
        aunque estos no siempre se pueden conocer. """
        ).shift(2 * UP)
        tex0 = TextMobject("Procedamos a enunciar formalmente este teorema.").next_to(
            def_intuitiva, 2 * DOWN
        )
        texto = VGroup(def_intuitiva, tex0)
        # Definición formal

        tex1 = TextMobject(
            "Sea",
            " $f : A \subset \mathbb{R}^{n} \\rightarrow \mathbb{R}$",
            " continua en $A$ tal que $B \subset A$.",
        ).shift(1.5 * UP)
        tex2 = TextMobject(
            "Si  $B \\neq \emptyset$,",
            " cerrado y acotado, entonces $\\exists$",
            " $ \hat{x_{1}}, \hat{x_{2}} \in B$",
        ).next_to(tex1, DOWN)
        tex3 = TextMobject(
            "tales que",
            " $f(\hat{x_{1}}) \leq f(\hat{x}) \leq f(\hat{x_{2}})$",
            " $\\forall \hat{x} \in B$.",
            " Es decir,",
        ).next_to(tex2, DOWN)
        tex4 = TextMobject(
            "\\textit{f} alcanza un valor",
            " máximo",
            " y un valor",
            " mínimo",
            " sobre \\textit{B}.",
        ).next_to(tex3, DOWN)
        tex4[1].set_color(GREEN_C)
        tex4[3].set_color(YELLOW_C)
        tex = VGroup(tex1, tex2, tex3, tex4)

        # Ejemplo en R
        ejm1 = TextMobject(
            """Comencemos por visualizar la definición \n
         anterior en una función $f:\mathbb{R} \\rightarrow \mathbb{R}$."""
        ).to_corner(UL)

        # Secuencia de animación
        self.play(Write(extreme))
        self.wait()
        self.play(FadeOut(extreme))
        self.wait()
        self.play(Write(texto), run_time=5)
        self.wait(3)
        self.remove(texto)
        self.wait()
        self.play(Write(tex), run_time=5)
        self.wait(3)
        self.play(FadeOut(tex))
        self.play(FadeIn(ejm1))
        self.wait(2)
        self.play(ShrinkToCenter(ejm1))

        # Example function
        self.setup_axes()
        graph = self.get_graph(
            lambda x: 2 * x ** 3 - 9 * x ** 2, color=YELLOW_D, x_min=-1, x_max=5
        )
        # labeling
        etiqueta = TextMobject("$f(x)= 2x^{3}-9x^{2}$").set_color(YELLOW_D)
        etiqueta.move_to(np.array((0.5, 1, 0)))
        # critic values
        dot_at_start = Dot().move_to(graph.points[0])
        dot_at_start1 = Dot().move_to(self.coords_to_point(-1, 0))
        dot_at_start2 = Dot().move_to(self.coords_to_point(0, -11))
        line_at_start1 = DashedLine(dot_at_start1.get_bottom(), dot_at_start)
        line_at_start2 = DashedLine(dot_at_start2.get_left(), dot_at_start)
        dot_at_start_label = (
            TexMobject((-1, -11)).next_to(dot_at_start, 0.5 * LEFT).scale(0.7)
        )
        dot_start = Group(
            dot_at_start,
            dot_at_start_label,
            dot_at_start1,
            dot_at_start2,
            line_at_start1,
            line_at_start2,
        )
        dot_at_center = Dot().move_to(self.coords_to_point(0, 0))
        dot_at_center_label = (
            TexMobject((0, 0)).next_to(dot_at_center, 0.5 * UP + 0.5 * RIGHT).scale(0.7)
        )
        dot_center = Group(dot_at_center, dot_at_center_label)
        dot_at_min1 = Dot().move_to(self.coords_to_point(3, 0))
        dot_at_min2 = Dot().move_to(self.coords_to_point(0, -27))
        dot_at_min = Dot().move_to(self.coords_to_point(3, -27))
        line_at_min1 = DashedLine(dot_at_min1.get_bottom(), dot_at_min)
        line_at_min2 = DashedLine(dot_at_min2.get_right(), dot_at_min)
        dot_at_min_label = (
            TexMobject((3, -27)).next_to(dot_at_min, 0.5 * DOWN).scale(0.7)
        )
        dot_min = Group(
            dot_at_min,
            dot_at_min_label,
            dot_at_min1,
            dot_at_min2,
            line_at_min1,
            line_at_min2,
        )
        dot_at_end = Dot().move_to(graph.points[-1])
        dot_at_end1 = Dot().move_to(self.coords_to_point(5, 0))
        dot_at_end2 = Dot().move_to(self.coords_to_point(0, 25))
        line_at_end1 = DashedLine(dot_at_end1.get_top(), dot_at_end)
        line_at_end2 = DashedLine(dot_at_end2.get_right(), dot_at_end)
        dot_at_end_label = TexMobject((5, 25)).next_to(dot_at_end, 0.5 * UP).scale(0.7)
        dot_end = Group(
            dot_at_end,
            dot_at_end_label,
            dot_at_end1,
            dot_at_end2,
            line_at_end1,
            line_at_end2,
        )

        grafica = Group(graph, etiqueta)

        self.play(FadeIn(self.axes))
        self.play(ShowCreation(grafica), run_time=2)  #####
        self.wait()
        self.play(
            ShowCreation(dot_start),
            ShowCreation(dot_center),
            ShowCreation(dot_min),
            ShowCreation(dot_end),
            run_time=4,
        )
        self.wait(3)
        self.play(
            FadeOut(self.axes),
            FadeOut(grafica),
            FadeOut(dot_end),
            FadeOut(dot_min),
            FadeOut(dot_center),
            FadeOut(dot_start),
        )

        pto0 = TextMobject(
            "Nótese que", " $f(x)= 2x^{3}-9x^{2}$", " es una función continua"
        ).to_edge(UP)
        pto0[1].set_color(YELLOW_D)
        pto1 = TextMobject("en el intervalo cerrado $I= [-1,5]$").next_to(pto0, DOWN)
        pto2 = TextMobject(
            "De la gráfica, se observa que los puntos críticos en $I$ son: "
        ).next_to(pto1, DOWN)
        pto3 = TextMobject("$(0,0)$, $(-1,-11)$, $(3,-27)$ y $(5,25)$.").next_to(
            pto2, DOWN
        )
        pto4 = TextMobject(
            "Con lo cual, los valores extremos se alcanzan cuando"
        ).next_to(pto3, DOWN)
        pto5 = TextMobject(
            "$-27=f(3) \leq f(\hat{x}) \leq f(5)=25$, $ \\forall \hat{x} \in I$"
        ).next_to(pto4, DOWN)
        ptos = VGroup(pto0, pto1, pto2, pto3, pto4, pto5)

        self.play(Write(ptos), run_time=6)
        self.wait(4)
        self.play(FadeOut(ptos))
        self.wait()


class Superficie(ThreeDScene):
    def setup(self):
        Scene.setup(self)
        ThreeDScene.setup(self)

    def construct(self):
        axis_config = {
            "x_min": -4,
            "x_max": 4,
            "y_min": -4,
            "y_max": 4,
            "z_min": -5,
            "z_max": 6,
            "unit_size": 0.5,
            "graph_origin": np.array([0, 0, -4]),
        }

        ejm2 = TextMobject(
            """ Visualicemos ahora este teorema usando \n
                una función $f:\mathbb{R}^{2} \\rightarrow \mathbb{R}$."""
        ).shift(1.5 * UP)
        nota1 = TextMobject(
            "Sea", " $f(x,y)=x^{2} - y^{2}+5$", " una función continua "
        ).next_to(ejm2, DOWN)
        nota1[1].set_color(PURPLE_E)
        nota2 = TextMobject("en un conjunto cerrado y acotado $T$, ").next_to(
            nota1, DOWN
        )
        nota3 = TextMobject("tal que T es el triángulo con vértices en ").next_to(
            nota2, DOWN
        )
        nota4 = TextMobject("(-1,-2,0), (0,1,0), (2,-2,0).").next_to(nota3, DOWN)
        notas = VGroup(ejm2, nota1, nota2, nota3, nota4)
        nota5 = TextMobject(
            """Queremos verificar que $f$ alcanza un \n
                valor mínimo y un máximo en el triángulo $T$. """
        ).shift(1.5 * UP)
        nota6 = TextMobject(
            """ Como $f$ tiene un único punto crítico en (0,0) \n
                procedemos a encontrar los valores mínimos y máximos  \n
                que $f$ alcanza en la frontera de $T$. """
        ).next_to(nota5, DOWN)
        notas_1 = VGroup(nota5, nota6)

        nota7 = (
            TextMobject(
                """Encuentra los puntos críticos y verifica que \n
                el valor máximo es $f(\\frac{6}{5}, -\\frac{4}{5})= \\frac{9}{5}$, mientras \n
                que el mínimo corresponde a  $f(0,-2)= 1 $"""
            )
            .scale(0.7)
            .to_corner(DL)
        )

        axes = ThreeDAxes(**axis_config)
        vertices = [(-1, -2, 0), (0, 1, 0), (2, -2, 0)]
        triangulo = Polygon(*vertices)
        triangulo.set_color(MAROON_C)
        triangulo.set_fill(MAROON_C, opacity=0.4)
        # construimos sabanita
        sabanita = ParametricSurface(
            lambda u, v: np.array([u, v, u ** 2 - v ** 2 + 5]),
            v_min=-3,
            v_max=3,
            u_min=-3,
            u_max=3,
            checkerboard_colors=[PURPLE_D, PURPLE_E],
            resolution=(15, 32),
        )

        # Si alguien puede hacer que el triángulo pueda pegarse a la sabana, use el triángulo parametrizado akí.
        #        lado1 = ParametricFunction(lambda t: np.array([-1*t,  -3*t+1, 0]),
        #                color = MAROON_C, t_min = 0, t_max = 1)
        #        lado2 = ParametricFunction(lambda t: np.array([2*t,  -3*t+1, 0]),
        #                color = MAROON_C, t_min = 0, t_max = 1)
        #        lado3 = ParametricFunction(lambda t: np.array([-3*t+2, -2, 0]),
        #                color = MAROON_C, t_min = 0, t_max = 1)
        #        triangulo = VGroup(lado1, lado2, lado3)

        # puntitos y líneas punteadas
        ver1 = Dot(np.array([-1, -2, 0]), radius=0.07)
        ver2 = Dot(np.array([0, 1, 0]), radius=0.07)
        ver3 = Dot(np.array([2, -2, 0]), radius=0.07)
        abs_min = Dot(np.array([0, -2, 1]), radius=0.07)
        abs_min_0 = Dot(np.array([0, -2, 0]), radius=0.07)
        abs_max_0 = Dot(np.array([6 / 5, -4 / 5, 0]), radius=0.07)
        abs_max = Dot(np.array([6 / 5, -4 / 5, 29 / 5]), radius=0.07)
        linea = DashedLine(abs_min_0, abs_min, opacity=0.7, stroke_width=5)
        linea2 = DashedLine(abs_max_0, abs_max, opacity=0.7, stroke_width=5)
        min1 = Dot(np.array([-1, -2, 2]), radius=0.07)
        min1_1 = Dot(np.array([-1, -2, 0]), radius=0.07)
        linea_min1 = DashedLine(min1_1, min1, opacity=0.7, stroke_width=5)
        min2 = Dot(np.array([2, -2, 5]), radius=0.07)
        min2_1 = Dot(np.array([2, -2, 0]), radius=0.07)
        linea_min2 = DashedLine(min2_1, min2, opacity=0.7, stroke_width=5)
        min3 = Dot(np.array([-3 / 8, -1 / 8, 41 / 8]), radius=0.07)
        min3_1 = Dot(np.array([-3 / 8, -1 / 8, 0]), radius=0.07)
        linea_min3 = DashedLine(min3_1, min3, opacity=0.7, stroke_width=5)
        min4 = Dot(np.array([0, 1, 4]), radius=0.07)
        min4_1 = Dot(np.array([0, 1, 0]), radius=0.07)
        linea_min4 = DashedLine(min4_1, min4, opacity=0.7, stroke_width=5)
        # etiquetas
        ver1_label = TexMobject((-1, -2, 0)).next_to(ver1, 0.5 * LEFT).scale(0.7)
        ver2_label = TexMobject((0, 1, 0)).next_to(ver2, 0.5 * LEFT).scale(0.7)
        ver3_label = TexMobject((2, -2, 0)).next_to(ver3, 0.5 * LEFT).scale(0.7)
        #        abs_min_label = TexMobject(r"$(f(0,-2),1)$").next_to(abs_min, 0.5*LEFT).scale(0.7)
        #        abs_max_label = TexMobject(r"$(f(6/5,-4/5),29/5)$").next_to(abs_max, 0.5*LEFT).scale(0.7)
        #        min1_label = TexMobject(r"$(f(-1,-2),2)$").next_to(min1, 0.5*LEFT).scale(0.7)
        #        min2_label = TexMobject(r"$(f(2,-2),5)$").next_to(min2, 0.5*LEFT).scale(0.7)
        #        min3_label = TexMobject(r"$(f(-3/8,-1/8),41/8)$").next_to(min3, 0.5*LEFT).scale(0.7)
        #        min4_label = TexMobject(r"$(f(0,1),4)$").next_to(min4, 0.5*LEFT).scale(0.7)
        # puntitos y etiquetas
        verts = Group(ver1, ver2, ver3, ver1_label, ver2_label, ver3_label)
        extremos = Group(abs_max, abs_min, linea, linea2)
        minimos = Group(
            min1, min2, min3, min4, linea_min1, linea_min2, linea_min3, linea_min4
        )
        # Animando texto
        self.play(Write(notas), run_time=5)
        self.wait(3)
        self.play(ReplacementTransform(notas, notas_1), run_time=3)
        self.wait(6)
        self.remove(notas_1)
        self.wait(2)
        self.play(FadeInFromDown(nota7))
        self.wait(3)
        # Animando la gráfica
        self.play(ShowCreation(axes))
        self.play(FadeOut(nota7))
        # self.set_camera_orientation(phi=75 * DEGREES,distance=10, frame_center=(0,0,-3))
        self.move_camera(phi=75 * DEGREES, frame_center=(0, 0, 3))
        self.begin_ambient_camera_rotation(rate=0.2)
        self.play(
            ShowCreation(triangulo),
            ShowCreation(verts),
            ShowCreation(sabanita),
            ShowCreation(extremos),
            ShowCreation(minimos),
            run_time=12,
        )
        self.wait(3)
        self.play(
            FadeOut(minimos),
            FadeOut(extremos),
            FadeOut(sabanita),
            FadeOut(verts),
            FadeOut(triangulo),
            FadeOut(axes),
        )
        self.wait(2)


####### FUNCION CONTINUA ENVIA CONTINUOS EN CONTINUOS
class FunContinuasEnAbiertos(Scene):
    def construct(self):
        titulo = TextMobject("""Funciones continuas y topología""").scale(1.5)
        titulo1 = (
            TextMobject(
                """La imagen inversa de un abierto,\n
                                 bajo una función continua,\n 

                                     es un abierto''').move_to(-0.5*UP).scale(1.5)
        text1=TextMobject('''Tomemos la función ''',''' $f(x,y)=(x^{2},y)$''','''$ \ , \  (x,y)\\in\\mathbb{R}^{2}$''').move_to(1*UP)
        text2=TextMobject('''Notemos que $Im(f)={(x,z)\\in\\mathbb{R}^2|x\\geq 0}$ y''').move_to(0*UP)
        
        text3=TextMobject(''' $f(x,y)$ es continua en  $\\mathbb{R}^{2}$''').move_to(1*DOWN)
        text4=TextMobject('''Ahora tomemos un abierto en el contradominio de f \n
                            $U\\subset\\mathbb{R}^{2}$''').move_to(2.3*UP)
        text5=TextMobject('''Tomemos la imagen inversa de U''').move_to(text4)
        text6=TextMobject(''' $f^{-1}(U)$\n
                           $\\leftarrow$ ''').move_to(-1*UP)
        text7=TextMobject('''Lo mismo ocurre con cualquier abierto de $\\mathbb{R}^{2}$''').move_to(text5)
        text8=TextMobject(''' $f^{-1}(A)$\n
                           $\\leftarrow$ ''').move_to(-1*UP)

        textf=TextMobject('''$f:\\mathbb{R}^{n}\\rightarrow\\mathbb{R}^{m}$\n''',
                               '''f es continua en $\\bf{TODO}$ $\\mathbb{R}^{n}$\n
                                si solo si para todo \n  ''',    
                               '''$ U\\subset\\mathbb{R}^{m}$ abierto \n
                                   se cumple que $f^{-1}(U)$ es abierto ''')
        textf1=TextMobject(''' Lo mismo ocurre si el dominio de $f$ es abierto,\n 
                                      ''',''' ¿qué pasa si no lo es? \n
                                      ''',''' Investiga sobre topología relativa.''')
        textf2=TextMobject('''También puedes modificar el código para ver más \n
                                ejemplos con cajas''')
        linea1=Arrow((-6,-4,0),(-0.5,-4,0),stroke_width=6,color=WHITE,buff=0)
        linea2=Arrow((-3.5,-7,0),(-3.5,0,0),stroke_width=6,color=WHITE,buff=0)
        G1=VGroup(linea1,linea2).move_to(-2.5*UP+3.5*LEFT)

        linea3=Arrow((0.5,-4,0),(6,-4,0),stroke_width=6,color=WHITE,buff=0)
        linea4=Arrow((3,-7,0),(3,0,0),stroke_width=6,color=WHITE,buff=0)
        G2=VGroup(linea3,linea4).move_to(3.5*RIGHT-2.5*UP)

        #Pueden cambiar estos parametros para cambiar la caja de la imagen inversa
        r1=1#altura
        r2=1.5#ancho
    
        caja1=Rectangle(height=r1, width=r2,fill_color=YELLOW_C,color=YELLOW_C ,fill_opacity=1,buff=0).move_to((3.7+(-r2/2))*LEFT-2.5*UP)
        
        caja2=Rectangle(height=r1, width=r2*r2,fill_color=PURPLE_C,color=PURPLE_C ,fill_opacity=1,buff=0).move_to((3.3+r2*r2/2)*RIGHT+-2.5*UP)
        caja2label=TextMobject("U").next_to(caja2)
        #Tambien se puede cambiar r3 y r4 para cambiar los tamaños de la caja en el 2do ejemplo
        r3=2#altura
        r4=2#ancho
        #posiciones de la caja, por si se quiere
        #usar una caja que no este esquinada y elevada en y en el segundo ejemplo
        y=0

        caja3=Rectangle(height=r3, width=(r4/3),fill_color=YELLOW_C,color=YELLOW_C ,fill_opacity=1,buff=0).move_to((4.7)*LEFT+(-3+(r3/2))*UP)
        
        caja5=Rectangle(height=r3, width=(r4/3),fill_color=YELLOW_C,color=YELLOW_C ,fill_opacity=1,buff=0).move_to((2.8)*LEFT+(-3+(r3/2))*UP)

        caja4=Rectangle(height=r3, width=(r4/2)**2,fill_color=PURPLE_C,color=PURPLE_C ,fill_opacity=1,buff=0).move_to((3.8+((((r4/2)**2)/2)))*RIGHT+(-3+(r3/2))*UP)
        caja4label=TextMobject("A").next_to(caja4)

        punto=np.array([1,-4,0])
        

### Animación

                                     es un abierto"""
            )
            .move_to(-0.5 * UP)
            .scale(1.5)
        )
        text1 = TextMobject(
            """Tomemos la función """,
            """ $f(x,y)=(x^{2},y)$""",
            """$ \ , \  (x,y)\\in\\mathbb{R}^{2}$""",
        ).move_to(1 * UP)
        text2 = TextMobject(
            """Notemos que $Im(f)={(x,z)\\in\\mathbb{R}^2|x\\geq 0}$ y"""
        ).move_to(0 * UP)

        text3 = TextMobject(""" $f(x,y)$ es continua en  $\\mathbb{R}^{2}$""").move_to(
            1 * DOWN
        )
        text4 = TextMobject(
            """Ahora tomemos un abierto en el contradominio de f \n
                            $U\\subset\\mathbb{R}^{2}$"""
        ).move_to(2.3 * UP)
        text5 = TextMobject("""Tomemos la imagen inversa de U""").move_to(text4)
        text6 = TextMobject(
            """ $f^{-1}[U]$\n
                           $\\leftarrow$ """
        ).move_to(-1 * UP)
        text7 = TextMobject(
            """Lo mismo ocurre con cualquier abierto de $\\mathbb{R}^{2}$"""
        ).move_to(text5)
        text8 = TextMobject(
            """ $f^{-1}[A]$\n
                           $\\leftarrow$ """
        ).move_to(-1 * UP)

        textf = TextMobject(
            """Entonces\n
                            $f:\\mathbb{R}^{n}\\rightarrow\\mathbb{R}^{m}$\n""",
            """f es continua en $\\bf{TODO}$ $\\mathbb{R}^{n}$\n
                                si solo si para todo \n  """,
            """$ U\\subset\\mathbb{R}^{m}$ abierto \n
                                   se cumple que $f^{-1}[U]$ es abierto """,
        )
        textf1 = TextMobject(
            """ Lo mismo ocurre si el dominio de $f$ es abierto,\n 
                                      """,
            """ ¿qué pasa si no lo es? \n
                                      """,
            """ Investiga sobre topología relativa.""",
        )
        textf2 = TextMobject(
            """También puedes modificar el código para ver más \n
                                ejemplos con cajas"""
        )
        linea1 = Arrow((-6, -4, 0), (-0.5, -4, 0), stroke_width=6, color=WHITE, buff=0)
        linea2 = Arrow((-3.5, -7, 0), (-3.5, 0, 0), stroke_width=6, color=WHITE, buff=0)
        G1 = VGroup(linea1, linea2).move_to(-2.5 * UP + 3.5 * LEFT)

        linea3 = Arrow((0.5, -4, 0), (6, -4, 0), stroke_width=6, color=WHITE, buff=0)
        linea4 = Arrow((3, -7, 0), (3, 0, 0), stroke_width=6, color=WHITE, buff=0)
        G2 = VGroup(linea3, linea4).move_to(3.5 * RIGHT - 2.5 * UP)

        # Pueden cambiar estos parametros para cambiar la caja de la imagen inversa
        r1 = 1  # altura
        r2 = 1.5  # ancho

        caja1 = Rectangle(
            height=r1,
            width=r2,
            fill_color=YELLOW_C,
            color=YELLOW_C,
            fill_opacity=1,
            buff=0,
        ).move_to((3.7 + (-r2 / 2)) * LEFT - 2.5 * UP)

        caja2 = Rectangle(
            height=r1,
            width=r2 * r2,
            fill_color=PURPLE_C,
            color=PURPLE_C,
            fill_opacity=1,
            buff=0,
        ).move_to((3.3 + r2 * r2 / 2) * RIGHT + -2.5 * UP)
        caja2label = TextMobject("U").next_to(caja2)
        # Tambien se puede cambiar r3 y r4 para cambiar los tamaños de la caja en el 2do ejemplo
        r3 = 2  # altura
        r4 = 2  # ancho
        # posiciones de la caja, por si se quiere
        # usar una caja que no este esquinada y elevada en y en el segundo ejemplo
        y = 0

        caja3 = Rectangle(
            height=r3,
            width=r4,
            fill_color=YELLOW_C,
            color=YELLOW_C,
            fill_opacity=1,
            buff=0,
        ).move_to((3.7) * LEFT + (-3 + (r3 / 2)) * UP)

        caja4 = Rectangle(
            height=r3,
            width=(r4 / 2) ** 2,
            fill_color=PURPLE_C,
            color=PURPLE_C,
            fill_opacity=1,
            buff=0,
        ).move_to((3.3 + ((((r4 / 2) ** 2) / 2))) * RIGHT + (-3 + (r3 / 2)) * UP)
        caja4label = TextMobject("A").next_to(caja4)

        punto = np.array([1, -4, 0])

        ### Animación

        self.play(Write(titulo))
        self.wait()
        self.play(titulo.shift, 2 * UP, runtime=1.5)
        self.wait(2)
        self.play(Write(titulo1))
        self.wait(5)
        self.play(FadeOut(titulo), FadeOut(titulo1))
        self.play(Write(text1))
        self.wait(6)
        self.play(Write(text2))
        self.wait(3)
        self.play(Write(text3))
        self.wait(4)
        self.play(FadeOut(text1[0]), FadeOut(text2), FadeOut(text3), FadeOut(text1[2]))
        self.play(text1[1].shift, 2.5 * UP + 1.2 * LEFT, runtime=1.5)
        self.play(ShowCreation(G1), ShowCreation(G2))
        self.play(Write(text4))
        self.wait(6)
        self.play(ShowCreation(caja2), Write(caja2label))
        self.play(ReplacementTransform(text4, text5))
        self.wait(3)
        self.play(Write(text6))
        self.wait()
        self.play(ShowCreation(caja1))
        self.play(ReplacementTransform(text5, text7))
        self.wait(5)

        self.play(ReplacementTransform(caja2,caja4),ReplacementTransform(caja2label,caja4label))
        self.play(ReplacementTransform(text6,text8))
        self.play(ReplacementTransform(caja1,caja3))
        self.play(ShowCreation(caja5))
        self.wait()
        self.play(FadeOut(caja3),FadeOut(caja4),FadeOut(caja5),FadeOut(G1),FadeOut(G2),FadeOut(text8),FadeOut(text1[1]),
                     FadeOut(text7),FadeOut(caja4label)   )

        self.play(
            ReplacementTransform(caja2, caja4),
            ReplacementTransform(caja2label, caja4label),
        )
        self.play(ReplacementTransform(text6, text8))
        self.play(ReplacementTransform(caja1, caja3))
        self.wait()
        self.play(
            FadeOut(caja3),
            FadeOut(caja4),
            FadeOut(G1),
            FadeOut(G2),
            FadeOut(text8),
            FadeOut(text1[1]),
            FadeOut(text7),
            FadeOut(caja4label),
        )

        self.play(Write(textf[0]))
        self.wait(5)
        self.play(Write(textf[1]))
        self.wait()
        self.play(Write(textf[2]))
        self.wait(5)
        self.play(FadeOut(textf))
        self.play(Write(textf1[0]))
        self.wait(5)
        self.play(Write(textf1[1]))
        self.wait(2)
        self.play(Write(textf1[2]))
        self.wait(3)
        self.play(ReplacementTransform(textf1, textf2))
        self.wait(5)
        self.play(FadeOut(textf2))


## Teorema fuerte: Continuas son acotadas en compactos ##


class Continua_y_acotada(Scene):
    def construct(self):
        # Textos
        # title = TextMobject('''Continua en compactos implica acotada''').scale(1.5)
        title = TextMobject(
            """Teorema Fuerte: \\\\
                            las funciones continuas son ccotadas \n
                            en compactos"""
        ).scale(1.5)
        t1 = TextMobject(
            """$f:A\\subset\\mathbb{R}^n\\to\\mathbb{R}^m$ es """,
            """acotada""",
            """ si \n
                            $f(A)\\subset\\mathbb{R}^m$ es """,
            """acotada""",
        )
        t1.set_color_by_tex_to_color_map({"""acotada""": PURPLE_B})
        t2 = TextMobject(
            """Teniendo en cuenta la definición anterior consideremos el \n 
                            conjunto """,
            """$A$""",
            """$ =[0,\\ 1.5]\\times[0,2]$ en $\\mathbb{R}^2$""",
        )
        t2[1].set_color(RED)
        t3 = (
            TextMobject("""Recuerda que este conjunto es """, """compacto""")
            .next_to(t2, DOWN)
            .scale(0.85)
            .shift(2.5 * UP)
        )
        t3[1].set_color(ORANGE)
        t4 = TextMobject(
            """Toma la función $f:A\\to\\mathbb{R}^2$ dada por $f(x,y)=(x^2,y^2)$, \n 
                            ¿cuál es la """,
            """imagen""",
            """ de """,
            """$A$""",
            """ bajo $f$?""",
        ).scale(1.17)
        t4[1].set_color(BLUE)
        t4[3].set_color(RED)
        t5 = TextMobject(
            """$f$ es """,
            """continua""",
            """ y $f(A)$ es un conjunto """,
            """acotado""",
            """. \n
                            Intenta demostrar ambas afirmaciones.""",
        ).scale(1.17)
        t5[1].set_color(GREEN_D)
        t5[3].set_color(PURPLE_B)
        t6 = TextMobject(
            """El resultado que vimos, es uno de los teoremas importantes \n
                            de continuidad, y dice lo siguiente:"""
        ).shift(UP * 0.75)
        t7 = TextMobject(
            """Si $F:K\\subset\\mathbb{R}^n\\to\\mathbb{R}^m$ es """,
            """continua""",
            """ y $K$ """,
            """compacto""",
            """ \n
                            entonces $F$ es """,
            """acotada""",
        ).next_to(t6, DOWN * 1)
        t7[-1].set_color(PURPLE_B)
        t7[1].set_color(GREEN_D)
        t7[3].set_color(ORANGE)

        # Ejes
        ejes1 = Axes(x_min=-0.5, x_max=5, y_min=-0.5, y_max=4).move_to(
            (-6 + 2.25, -3 + 1.75, 0)
        )
        ejes2 = Axes(x_min=-0.5, x_max=5, y_min=-0.5, y_max=4).move_to(
            (1.5 + 2.25, -3 + 1.75, 0)
        )

        # Objetos
        compacto = Rectangle(
            height=1.5, width=2, color=RED, fill_color=RED, fill_opacity=0.8
        ).move_to((-5, -2.25, 0))
        imagen = Rectangle(
            height=2.25, width=4, color=BLUE, fill_color=BLUE, fill_opacity=0.8
        ).move_to((3.5, -1.875, 0))
        flecha = Arrow(start=(-1, 0, 0), end=(1, 0, 0), color=WHITE)
        f = TexMobject(r"f(x,y)").next_to(flecha, DOWN).shift(0.25 * DOWN)

        # Grupos
        Grupo0 = VGroup(t2, t3)
        Grupo1 = VGroup(t4, t5).to_edge(UP).scale(0.7)
        Grupo2 = VGroup(flecha, f)
        Grupo3 = VGroup(ejes1, ejes2, compacto, imagen, Grupo2, t5)

        # Animación

        self.play(Write(title))
        self.wait(3.25)
        self.play(ReplacementTransform(title, t1))
        self.wait(7.5)
        self.play(ReplacementTransform(t1, t2))
        self.wait(5)
        self.play(ApplyMethod(t2.scale, 0.85))
        self.play(ApplyMethod(t2.to_edge, UP))
        self.wait()
        self.play(ShowCreation(ejes1))
        self.play(ShowCreation(compacto))
        self.wait()
        self.play(Write(t3))
        self.wait(3)
        self.play(FadeOut(t3))
        self.play(ReplacementTransform(t2, t4))
        self.wait(7)
        self.play(Write(Grupo2))
        self.play(ShowCreation(ejes2))
        self.play(ShowCreation(imagen))
        self.wait()
        self.play(ReplacementTransform(t4, t5))
        self.wait(7)
        self.play(FadeOut(Grupo3))
        self.play(Write(t6))
        self.wait(5)
        self.play(Write(t7))
        self.wait(5)
        self.play(FadeOut(t6), FadeOut(t7))


##Teorema del valor intermedio, sin corregir
class TeoValorIntermedio_1(Scene):
    def construct(self):

        titulo = TextMobject(
            """Teoremas Fuertes de Continuidad""",
            """ \n
                        Teorema del Valor Intermedio""",
        ).scale(
            1.5
        )  # .move_to(1*UP)
        text_1_1 = TextMobject(
            """Sea $f:A\\subset\\mathbb{R}^{n}\\rightarrow\\mathbb{R}$ """,
            """continua""",
            """ en A.""",
        ).shift(UP * 1.8)
        text_1_2 = TextMobject(
            """Sea A """, """conexo""", """ y $\\vec{x}_1,\\vec{x}_2\\in A$"""
        ).next_to(text_1_1, DOWN)
        text_1_3 = TextMobject(""" tales que $f(\\vec{x}_1)<f(\\vec{x}_2)$.""").next_to(
            text_1_2, DOWN
        )
        text_1_4 = TextMobject(
            """Si $c\\in\\mathbb{R}$ es tal que $f(\\vec{x}_1)<c<f(\\vec{x}_2)$,"""
        ).next_to(text_1_3, DOWN)
        text_1_5 = TextMobject(
            """entonces existe $\\vec{x}$ tal que $f(\\vec{x})=c$ """
        ).next_to(text_1_4, DOWN)
        text_1_1[1].set_color(PURPLE_B)
        text_1_1[3].set_color(ORANGE)
        text1 = VGroup(text_1_1, text_1_2, text_1_3, text_1_4, text_1_5)
        text_2 = TextMobject("Veamos algunos ejemplos que ilustran este teorema")

        self.play(Write(titulo[0]))
        self.wait(4)
        self.play(Write(titulo[1]))
        self.wait(4)
        self.play(FadeOut(titulo))
        self.play(Write(text_1_1))
        self.wait(4)
        self.play(Write(text_1_2))
        self.wait(5)
        self.play(Write(text_1_3))
        self.wait(4)
        self.play(Write(text_1_4))
        self.wait(6)
        self.play(Write(text_1_5))
        self.wait(4)
        self.play(ReplacementTransform(text1, text_2))
        self.wait(4)
        self.play(FadeOut(text_2))


class TeoValorIntermedio_2(GraphScene):
    CONFIG = {
        "x_min": -2,
        "x_max": 2,
        "y_min": -2,
        "y_max": 2,
        "graph_origin": ORIGIN + 0.6 * DOWN,
        "function_color": BLUE_C,
        "x_axis_label": None,
        "y_axis_label": None
        # "axes_color" : YELLOW_C,
        # "x_labeled_nums" :range(-1,1)
    }

    def construct(self):
        ### ¡NO MOVER!
        ###############
        self.setup_axes(animate=True)
        func_graph = self.get_graph(self.func_to_graph, self.function_color)
        #####################
        ################
        # axes=Axes().move_to(2*DOWN)

        text1 = TextMobject("Sea ", "$f(x)=e^{x^{2}}\sin(10x)$").move_to(3.5 * UP)
        for i in range(0, 4):
            text1[1][i].set_color(BLUE)
        text1.bg = SurroundingRectangle(
            text1, color=WHITE, fill_color=BLACK, fill_opacity=0.75
        )
        text1.group = VGroup(text1.bg, text1)
        text1[1].bg = SurroundingRectangle(
            text1[1], color=WHITE, fill_color=BLACK, fill_opacity=0.75
        ).shift(6.85 * DOWN)
        text1[1].group = VGroup(text1[1].bg, text1[1])
        text2 = TextMobject("""Tomemos $\\vec{x}_1=0$ y $\\vec{x}_2=0.8128$""").move_to(
            3.3 * UP
        )
        text2.bg = SurroundingRectangle(
            text2, color=WHITE, fill_color=BLACK, fill_opacity=0.75
        )
        text2.group = VGroup(text2.bg, text2)
        text2_1 = (
            TextMobject(
                """Además """,
                """$f(\\vec{x}_1)$""",
                """$=0$ y """,
                """$f(\\vec{x}_2)$""",
                """$=1.8764$""",
            )
            .next_to(text2, DOWN)
            .shift(0.1 * UP)
        )
        text2_1[1].set_color(RED)
        text2_1[3].set_color(PINK)
        text2_1.group = VGroup(text2, text2_1)
        text2_1.bg = SurroundingRectangle(
            text2_1.group, color=WHITE, fill_color=BLACK, fill_opacity=0.75
        )
        text3 = TextMobject("""Y escojamos c=1""").move_to(3.5 * UP)
        text3[0][10].set_color(ORANGE)
        text3.bg = SurroundingRectangle(
            text3, color=WHITE, fill_color=BLACK, fill_opacity=0.75
        )
        text3.group = VGroup(text3.bg, text3)
        text4 = TextMobject(
            """Podemos apreciar que $\\Vec{x}_0=0.8960$ cumple que\n""",
            """$f(\\Vec{x}_0)$""",
            """$=$""",
            """$c$""",
            """$=1$ """,
        ).move_to(3 * UP)
        text4[1].set_color(GREEN)
        text4[3].set_color(ORANGE)
        text4.bg = SurroundingRectangle(
            text4, color=WHITE, fill_color=BLACK, fill_opacity=0.75
        )
        text4.group = VGroup(text4.bg, text4)
        text5 = TextMobject(
            """Además si tomamos $A=\\mathbb{R}, \ \\Vec{x}_0,\\Vec{x}_1,\\Vec{x}_2\\in A$."""
        ).move_to(3.3 * UP)
        text5.bg = SurroundingRectangle(
            text5, color=WHITE, fill_color=BLACK, fill_opacity=0.75
        )
        text5.group = VGroup(text5.bg, text5)
        text6 = TextMobject(
            """Sin embargo, en A, $\\Vec{x}_0$ no es el único \n
                                elemento que satisface que $f(\\Vec{x})=1$"""
        ).move_to(3.3 * UP)
        text6.bg = SurroundingRectangle(
            text6, color=WHITE, fill_color=BLACK, fill_opacity=0.75
        )
        text6.group = VGroup(text6.bg, text6)
        text6_1 = TextMobject(
            """También """, """$f(\\vec{x}'_0)$""", """$=1$"""
        ).move_to(3 * UP)
        text6_1[1].set_color(GREEN)
        text6_1.bg = SurroundingRectangle(
            text6_1, color=WHITE, fill_color=BLACK, fill_opacity=0.75
        )
        text6_1.group = VGroup(text6_1.bg, text6_1)
        text7 = TextMobject(
            """¿Esto contradice el teorema del valor intermedio?"""
        ).shift(0.5 * UP)
        text7_1 = TextMobject(
            """¡NO! por que el teorema del valor intermedio no nos \n
                             dice que $\\Vec{x}$ es único. """
        ).next_to(
            text7, DOWN
        )  # .move_to(3*UP)
        text7.group = VGroup(text7, text7_1)
        text8 = TextMobject("""Veamos un último ejemplo""")

        # Se puede modifica x2,x1,x_p y x_pp para cambiar los puntos que se representan en la función, tambien se puede cambiar c
        x2 = 0.8012888224891
        fx2 = np.exp(x2 * x2) * np.sin(10 * x2)
        vec_x2 = Dot(color=PINK).move_to(
            (self.coords_to_point(x2, fx2))
        )  # (0.8128+2.47)*RIGHT+(1.8764-0.1)*UP)
        v_x2 = Dot(color=PINK).move_to(
            (self.coords_to_point(x2, 0))
        )  # (0.8128+2.47)*RIGHT+(1.8764-0.1)*UP)
        x1 = 0
        fx1 = np.exp(x1 * x1) * np.sin(10 * x1)
        vec_x1 = Dot(color=RED).move_to(
            self.coords_to_point(0, fx1)
        )  # (0)*RIGHT+(0-1)*UP)
        v_x1 = Dot(color=RED).move_to(self.coords_to_point(0, 0))  # (0)*RIGHT+(0-1)*UP)
        # v_x1_label = TexMobject(r"\Vec{x}_2").next_to(v_x2,RIGHT,buff=0.2).set_color(RED)
        # v_x2_label = TexMobject(r"\Vec{x}_2").next_to(v_x2,RIGHT,buff=0.2).set_color(PINK)
        vec_x2_label = (
            TexMobject(r"f(\Vec{x}_2)")
            .next_to(vec_x2, RIGHT, buff=0.2)
            .set_color(PINK)
            .shift(0.3 * DOWN)
        )
        vec_x1_label = (
            TexMobject(r"f(\Vec{x}_1)")
            .next_to(vec_x1, UP, buff=0.3)
            .set_color(RED)
            .shift(0.6 * RIGHT)
            .shift(0.3 * DOWN)
        )
        puntos = VGroup(vec_x2, vec_x1, vec_x2_label, vec_x1_label)
        c = Dot(color=ORANGE).move_to(
            self.coords_to_point(0, 1)
        )  ## se puede cambiar la corrdenada (0,1)
        c_label = TextMobject("c").next_to(c, LEFT, buff=0.1).set_color(ORANGE)
        x_p = 0.186  # 2785740061
        fx_p = np.exp(x_p * x_p) * np.sin(10 * x_p)
        vec_x_p = Dot(color=GREEN).move_to(
            self.coords_to_point(x_p, fx_p)
        )  # (0.3528+2.47)*RIGHT+(0.45-0.1)*UP)
        x_pp = 0.8961
        label_x_p = (
            TexMobject(r"f(\vec{x}_0)")
            .next_to(vec_x_p, RIGHT, buff=0.1)
            .set_color(GREEN)
        )
        fx_pp = np.exp(x_pp * x_pp) * np.sin(10 * x_pp)
        vec_x_pp = Dot(color=GREEN).move_to(self.coords_to_point(x_pp, fx_pp))
        label_x_pp = TexMobject(r"f(\vec{x}'_0)").next_to(vec_x_pp).set_color(GREEN)
        puntos = VGroup(vec_x2, vec_x1, c, vec_x_p, vec_x_pp)
        rec = Rectangle(
            height=FRAME_HEIGHT,
            width=FRAME_WIDTH,
            color=BLACK,
            fill_color=BLACK,
            fill_opacity=1,
        )

        self.play(Write(text1.group))
        self.add_foreground_mobjects(text1.group)
        self.wait(3)
        self.play(ShowCreation(func_graph), runtime=1.5)
        self.remove_foreground_mobjects(text1[0])
        self.play(
            FadeOut(text1.bg),
            FadeOut(text1[0]),
            text1[1].shift,
            6.85 * DOWN,
            runtime=1.5,
        )
        self.play(Write(text1[1].bg))
        self.play(Write(text2.group))
        self.add_foreground_mobjects(text2)
        self.wait(3)
        # self.play(ShowCreation(v_x1))
        # self.play(Write(v_x1_label))
        # self.play(ShowCreation(v_x2))
        # self.play(Write(v_x2_label))
        self.play(ReplacementTransform(text2.bg, text2_1.bg))
        # self.play(FadeOut(v_x1_label),FadeOut(v_x2_label))
        self.add_foreground_mobjects(text2_1.bg, text2_1, text2)
        self.play(Write(text2_1))
        self.play(ShowCreation(vec_x1))
        self.play(Write(vec_x1_label))
        self.play(ShowCreation(vec_x2))
        self.play(Write(vec_x2_label))
        self.wait(5)
        self.remove_foreground_mobjects(text2_1.bg, text2_1, text2)
        self.play(FadeOut(text2_1.group), FadeOut(text2_1.bg))
        self.play(Write(text3.group))
        self.play(ShowCreation(c))
        self.play(Write(c_label))
        self.play(FadeOut(vec_x1_label), FadeOut(vec_x2_label))
        self.wait(3)
        self.play(FadeOut(text3.group))
        self.play(Write(text4.group))
        self.play(ShowCreation(vec_x_p), Write(label_x_p))
        self.play(FadeOut(c_label))
        self.wait(6)
        self.play(ReplacementTransform(text4.group, text5.group))
        self.wait(7)
        self.play(ReplacementTransform(text5.group, text6.group))
        self.play(ShowCreation(vec_x_pp))
        self.wait(7)
        self.play(ReplacementTransform(text6.group, text6_1.group))
        self.play(ShowCreation(vec_x_pp))
        self.wait()
        self.play(Write(label_x_pp))
        self.play(FadeOut(label_x_p))
        self.wait(3)
        self.remove_foreground_mobjects(text1[1])
        self.play(FadeOut(text6.group), FadeOut(text1[1].group), FadeOut(puntos))
        self.play(FadeOut(func_graph))
        self.play(GrowFromCenter(rec))
        self.play(Write(text7))
        self.wait(4)
        self.play(Write(text7_1))
        self.wait(7)
        self.play(ReplacementTransform(text7.group, text8))
        self.wait(2)
        self.play(FadeOut(text8))

    def func_to_graph(self, x):
        return np.exp(x * x) * np.sin(10 * x)


class sup(ParametricSurface):
    def __init__(self, **kwargs):
        kwargs = {
            "u_min": -3,
            "u_max": 3,
            "v_min": -3,
            "v_max": 3,
            "checkerboard_colors": [BLUE_C],
        }
        ParametricSurface.__init__(self, self.func, **kwargs)

    def func(self, x, y):
        return np.array([x, y, x ** 2 + y ** 2 - 2])


class TeoValorIntermedio_3(ThreeDScene):
    CONFIG = {"x_axis_label": "$x$", "y_axis_label": "$y$"}

    def construct(self):

        text2 = TextMobject("""Sea $f(x,y)=x^{2}+y^{2}-2$""")
        for i in range(3, 9):
            text2[0][i].set_color(BLUE)
        text2_copy = text2.copy()
        text2_copy.to_edge(DOWN)
        text2.bg = SurroundingRectangle(
            text2_copy, color=WHITE, fill_color=BLACK, fill_opacity=1
        )
        text2.group = VGroup(text2.bg, text2_copy)
        # text3_0=TextMobject('''Y sea $\\Vec{x}_1=(0,0),\\Vec{x}_2=(2,0)$''').to_edge(DOWN)
        # text3_0.bg = SurroundingRectangle(text3_0,color=WHITE,fill_color=BLACK,fill_opacity=1)
        # text3_0.group = VGroup(text3_0.bg,text3_0)
        # text3_0[0][4].set_color(PURPLE_B)
        # text3_0[0][5].set_color(PURPLE_B)
        # text3_0[0][6].set_color(PURPLE_B)
        # text3_0[0][14].set_color(RED)
        # text3_0[0][15].set_color(RED)
        # text3_0[0][16].set_color(RED)
        text3 = TextMobject(
            """Y sea $\\Vec{x}_1=(0,0),\\Vec{x}_2=(2,0)$""", """ y $c=5$"""
        ).to_edge(DOWN)
        text3.bg = SurroundingRectangle(
            text3, color=WHITE, fill_color=BLACK, fill_opacity=1
        )
        text3.group = VGroup(text3.bg, text3)
        text3[0][4].set_color(PURPLE_B)
        text3[0][5].set_color(PURPLE_B)
        text3[0][6].set_color(PURPLE_B)
        text3[0][14].set_color(RED)
        text3[0][15].set_color(RED)
        text3[0][16].set_color(RED)
        text4 = TextMobject(
            """Se puede comprobar que """,
            """$f(\\Vec{x}_1)$""",
            """$<0<$""",
            """$f(\\Vec{x}_2)$""",
        )
        text4.to_edge(DOWN)
        text4.bg = SurroundingRectangle(
            text4, color=WHITE, fill_color=BLACK, fill_opacity=1
        )
        text4.group = VGroup(text4.bg, text4)
        text4[1].set_color(PURPLE_B)
        text4[3].set_color(RED)
        text5 = TextMobject(
            """Si tomamos $\\vec{x}=(x,y)$ tal que $||\\vec{x}||^{2}=2$, \\\\""",
            """se cumple que $f(\\vec{x})=0$.""",
        )
        text5.to_edge(DOWN)
        text5.bg = SurroundingRectangle(
            text5, color=WHITE, fill_color=BLACK, fill_opacity=1
        )
        text5.group = VGroup(text5.bg, text5)
        text6 = TextMobject(
            """Si tomamos $\\vec{x}$ tal que $||\\vec{x}||=2$ \n""",
            """se cumple que $f(\\vec{x})$=0""",
        )
        text6.to_edge(DOWN)
        text6.bg = SurroundingRectangle(
            text6, color=WHITE, fill_color=BLACK, fill_opacity=1
        )
        text6.group = VGroup(text6.bg, text6)
        text6_1 = TextMobject(
            """Por lo cual se cumple el teorema del valor intermedio."""
        )
        text6_1.to_edge(DOWN)
        text6_1.bg = SurroundingRectangle(
            text6_1, color=WHITE, fill_color=BLACK, fill_opacity=1
        )
        text6_1.group = VGroup(text6_1.bg, text6_1)
        text7 = TextMobject(
            """Como $f$ es continua en un conexo y tiene cambio de signo, \\\\""",
            """por el teorema del valor intermedio, \\\\""",
            """$f$ tiene raíces en el dominio.""",
        ).to_edge(DOWN)
        text7.bg = SurroundingRectangle(
            text7, color=WHITE, fill_color=BLACK, fill_opacity=1
        )
        text7.group = VGroup(text7.bg, text7)

        superficie = sup(color=BLUE_C, fill_opacity=0.5)
        axes = ThreeDAxes()
        axes.add(axes.get_axis_labels())
        axes.axis_labels[0].rotate(PI / 2, axis=RIGHT)
        axes.axis_labels[1].rotate(PI / 2, axis=RIGHT)
        # axes
        # Se puede cambiar x1,x1,x2,y2 para cambiar lospuntos referentes al valor extremo
        x1 = 0
        y1 = 0
        f_1 = Dot(color=PURPLE_C).move_to([x1, y1, 0])
        # xf_1=Dot(color=PURPLE_B).move_to([x1,y1,x1**2+y1**2-2]).set_color(PURPLE_C)
        f_1_label = (
            TexMobject(r"\vec{x}_1")
            .rotate(PI / 2, axis=RIGHT)
            .move_to(f_1.get_center() + 0.2 * UP + 0.4 * RIGHT)
            .set_color(PURPLE_C)
            .scale(1.5)
        )
        x2 = 2
        y2 = 0
        f_2 = Dot(color=RED).move_to([x2, y2, 0])
        # xf_2=Dot(color=RED).move_to([x2,y2,x2**2+y2**2-2]).set_color(RED)
        f_2_label = (
            TexMobject(r"\vec{x}_2")
            .rotate(PI / 2, axis=RIGHT)
            .move_to(f_2.get_center() + 0.2 * UP + 0.4 * RIGHT)
            .set_color(RED)
            .scale(1.5)
        )
        # Tambien se puede cambiar el radio de la bola y su posición
        bola = Circle(radius=(2 ** (1 / 2)), color=ORANGE).move_to([0, 0, 0])
        # G1=VGroup(f_1,f_1_label,f_2,f_2_label)
        dots1 = VGroup(f_1, f_2, f_1_label, f_2_label)
        xf_1 = (
            Dot(color=PURPLE_B)
            .move_to([x1, y1, x1 ** 2 + y1 ** 2 - 2])
            .set_color(PURPLE_C)
        )
        xf_2 = Dot(color=RED).move_to([x2, y2, x2 ** 2 + y2 ** 2 - 2]).set_color(RED)
        xf_1_label = (
            TexMobject(r"f(\vec{x}_1)")
            .rotate(PI / 2, axis=RIGHT)
            .move_to(xf_1.get_center() + 1 * RIGHT)
            .set_color(PURPLE_C)
            .scale(1.5)
        )
        xf_2_label = (
            TexMobject(r"f(\vec{x}_2 ) ")
            .rotate(PI / 2, axis=RIGHT)
            .move_to(xf_2.get_center() + 1 * RIGHT)
            .set_color(RED)
            .scale(1.5)
        )
        dots2 = VGroup(xf_1, xf_2, xf_1_label, xf_2_label)

        # Def dot radius = 0.08

        # self.set_camera_orientation(0.8*np.pi/2, -0.25*np.pi,distance=20)
        self.set_camera_orientation(
            phi=0.8 * np.pi / 2, theta=1.75 * np.pi, distance=20
        )
        self.add_fixed_in_frame_mobjects(text2)
        self.play(Write(text2))
        self.wait(4)
        self.play(ReplacementTransform(text2, text2_copy))
        self.add_foreground_mobject(text2_copy)
        self.add_fixed_in_frame_mobjects(text2_copy, text2.bg)
        self.play(Write(text2.bg))
        # self.wait(4)
        self.play(ShowCreation(axes))
        self.play(ShowCreation(superficie), fill_opacity=0.5)
        self.remove_foreground_mobject(text2_copy)
        self.play(FadeOut(text2.group))
        self.add_foreground_mobject(text3[0])
        self.add_fixed_in_frame_mobjects(text3.bg, text3[0])
        self.play(Write(text3.bg), Write(text3[0]))
        self.play(ShowCreation(f_1), Write(f_1_label))
        self.play(Write(f_2_label), ShowCreation(f_2))
        self.wait(5)
        # self.remove_foreground_mobject(text3_0)
        self.add_fixed_in_frame_mobjects(text3[1], text3.bg)
        # self.play(ReplacementTransform(text3_0.group,text3.group))
        self.add_foreground_mobject(text3[1])
        self.play(Write(text3[1]))
        # self.add_foreground_mobject(text3)
        self.wait(3)
        self.remove_foreground_mobject(text3)
        self.play(FadeOut(text3.group))
        self.add_fixed_in_frame_mobjects(text4.group)
        self.play(Write(text4.group))
        self.add_foreground_mobject(text4)
        self.play(FadeOut(dots1))
        self.play(Write(dots2))
        self.wait(6)
        self.remove_foreground_mobject(text4)
        self.play(FadeOut(text4.group))
        self.add_fixed_in_frame_mobjects(text5[0], text5.bg)
        self.add_foreground_mobject(text5[0])
        self.play(Write(text5.bg), Write(text5[0]))
        self.wait(6.6)
        # self.play(FadeOut(text5))
        self.add_foreground_mobject(text5[1])
        self.add_fixed_in_frame_mobjects(text5[1])
        self.play(Write(text5[1]))
        self.play(ShowCreation(bola))
        self.wait(4.5)
        self.remove_foreground_mobject(text5)
        self.play(FadeOut(text5.group))
        self.add_fixed_in_frame_mobjects(text6_1, text6_1.bg)
        self.add_foreground_mobject(text6_1)
        self.play(Write(text6_1.bg), Write(text6_1))
        self.wait(4.5)
        self.remove_foreground_mobject(text6_1)
        self.play(FadeOut(text6_1.group))
        self.add_fixed_in_frame_mobjects(text7.bg, text7[0])
        self.play(Write(text7.bg), Write(text7[0]))
        self.wait(5.5)
        self.add_fixed_in_frame_mobjects(text7[1])
        self.play(Write(text7[1]))
        self.wait(3)
        self.add_fixed_in_frame_mobjects(text7[2])
        self.play(Write(text7[2]))
        self.wait(3)
        self.play(
            FadeOut(text7.group),
            FadeOut(superficie),
            FadeOut(axes),
            FadeOut(dots2),
            FadeOut(bola),
        )
