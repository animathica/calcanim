from manimlib.imports import *

######################################################
##### Reparametrización de curvas #########
#######################################################
#04/11/2021

def curva1p(t):
    return [t, np.cos(4 * t), np.sin(4 * t)]


def curva2p(s):
    return [-s ** 3, np.cos(-4 * s ** 3), np.sin(-4 * s ** 3)]


class Reparametrizacion_de_curvas_1(ThreeDScene):
    def textos1(self):
        axis_config = {
            "x_min": -8,
            "x_max": 8,
            "y_min": -8,
            "y_max": 8,
            "z_min": -8,
            "z_max": 8,
        }
        titulo = TextMobject('''Reparametrización \n
                                de Curvas''').scale(2)
        t_0 = TextMobject("Tomemos la siguiente curva").to_edge(UP)
        t_0.bg = SurroundingRectangle(t_0, color=WHITE, fill_color=BLACK, fill_opacity=1)
        text=VGroup(t_0.bg,t_0)
        t_1 = TextMobject('''$\\gamma(t)=(t,\\cos(4t),\\sin(4t))$ \n''',
                            '''y considera $C=Im(\gamma)$. ''').move_to(3 * UP)
        t_1.bg = SurroundingRectangle(t_1, color=WHITE, fill_color=BLACK, fill_opacity=1)
        t_1.set_color_by_tex_to_color_map({
            "$C$": BLUE,
        })
        text1=VGroup(t_1.bg,t_1)
        t_2 = TextMobject('''Tomando $f(s)=-s^{3}$''').move_to(3 * UP)
        t_2.bg = SurroundingRectangle(t_2, color=WHITE, fill_color=BLACK, fill_opacity=1)
        text2=VGroup(t_2.bg,t_2)
        t_3 = TextMobject('''Entonces
                            $\\xi(s)=(\\gamma\\circ f)(s)=(-s^{3},\\cos(-4s^{3}),\\sin(-4s^{3}))$''').move_to(3 * UP)
        t_3.bg = SurroundingRectangle(t_3, color=WHITE, fill_color=BLACK, fill_opacity=1)
        text3=VGroup(t_3.bg,t_3)
        t_4 = TextMobject('''Como $Im(\\gamma)=Im(\\xi)=C$ decimos $\\xi$ \n
                                es una reparametrización de $C$.''').move_to(3 * UP)
        t_4.bg = SurroundingRectangle(t_4, color=WHITE, fill_color=BLACK, fill_opacity=1)
        text4=VGroup(t_4.bg,t_4)
        t_5 = TextMobject(''' Tomemos un punto en la curva y veamos como se mueve \n
                                 al comparar ambas parametrizaciones.''').move_to(3 * UP)
        t_5.bg = SurroundingRectangle(t_5, color=WHITE, fill_color=BLACK, fill_opacity=1)
        text5=VGroup(t_5.bg,t_5)


        axes = ThreeDAxes(**axis_config)

        tmin = -8
        tmax = 8
        vs = tmax ** (1 / 3)
        f = ParametricFunction(curva1p, t_min=tmin, t_max=tmax, color=RED)
        g = ParametricFunction(curva1p, t_min=tmin, t_max=tmax, color=BLUE_C)
        self.play(Write(titulo.scale(1.5)))
        self.wait(5)
        self.play(FadeOut(titulo))
        self.set_camera_orientation(0.8 * np.pi / 2, -0.25 * np.pi, distance=20)
        self.play(ShowCreation(axes))
        self.add_fixed_in_frame_mobjects(text)
        self.play(Write(text))
        self.wait(3)
        self.play(FadeOut(text))
        self.add_fixed_in_frame_mobjects(text1[0])
        self.play(Write(text1[0]))
        self.wait()
        self.play(ShowCreation(f), run_time=2)
        self.wait(4)
        self.add_fixed_in_frame_mobjects(text1[1])
        self.play(Write(text1[1]))
        self.wait(5)
        self.play(FadeOut(text1))
        self.add_fixed_in_frame_mobjects(text2)
        self.play(Write(text2))
        self.wait(5.7)
        self.play(FadeOut(text2))
        self.add_fixed_in_frame_mobjects(text3)
        self.play(Write(text3))
        self.play(ReplacementTransform(f, g), runtime=2)
        self.wait(11.25)
        self.play(FadeOut(text3))
        self.add_fixed_in_frame_mobjects(text4)
        self.play(Write(text4))
        self.wait(7.6)
        self.play(FadeOut(text4))
        self.add_fixed_in_frame_mobjects(text5)
        self.play(Write(text5))
        self.wait(8.5)
        self.play(FadeOut(text5))

    def mov_particula(self):
        # Se puede modificar t0 para cambiar la longitud de los number lines
        t0 = 7
        line_config = {
            "x_min": -t0 + 0.1,
            "x_max": t0 + 0.1,
            "unit_size": 0.3,
            "include_numbers": True,
            # "numbers_to_show": None,
            ##"longer_tick_multiple": 2,
            "number_at_center": 0,
            "number_scale_val": 0.5,
            "label_direction": DOWN,
            "line_to_number_buff": MED_SMALL_BUFF,
            "include_tip": False,
            "tip_width": 0.25,
            "tip_height": 0.25,

        }
        line_config2 = {
            "x_min": -(t0 ** (1 / 3)) + 0.2,
            "x_max": t0 ** (1 / 3) + 0.2,
            "unit_size": 1.1,
            "include_numbers": True,
            # "numbers_to_show": None,
            ##"longer_tick_multiple": 2,
            "number_at_center": 0,
            "number_scale_val": 0.5,
            "label_direction": DOWN,
            "line_to_number_buff": MED_SMALL_BUFF,
            "include_tip": False,
            "tip_width": 0.25,
            "tip_height": 0.25,

        }
        number_line = NumberLine(**line_config).move_to(2 * DOWN + (3 - 0.5) * LEFT)

        ##Movimiento para una partícula en la primera parametrización
        t1 = ValueTracker(-t0)
        p_1 = Sphere(radius=0.1, color=RED, fill_opacity=1).move_to([(-t0, np.cos(4 * (-t0)), np.sin(4 * (-t0)))])

        def mov_1(obj):
            t = t1.get_value()
            p_1.become(Sphere(radius=0.1, color=RED, fill_opacity=1).move_to([(t, np.cos(4 * t), np.sin(4 * t))]))

        p_1.add_updater(mov_1)

        p_t = Sphere(radius=0.1, color=RED, fill_opacity=1).move_to(number_line.number_to_point(t0))
        pt_label = TextMobject("t").next_to(p_t, UP, buff=0.1)

        def mov_t(obj):
            tn = t1.get_value()
            p_t.become(Sphere(radius=0.1, color=RED, fill_opacity=1).move_to(number_line.number_to_point(tn)))
            pt_label.become(TextMobject("t").next_to(p_t, UP, buff=0.1))

        Movimiento_1 = VGroup(p_t, pt_label)
        Movimiento_1.add_updater(mov_t)

        # movimiento para la esfera en la parametrización

        s1 = ValueTracker(-(t0 ** (1 / 3)))
        p_2 = Sphere(radius=0.1).move_to(
            [(-(-(t0 ** (1 / 3))) ** 3, np.cos(-4 * (-(t0 ** (1 / 3))) ** 3), np.sin(-4 * (-(t0 ** (1 / 3))) ** 3))])

        def mov_2(obj):
            s = s1.get_value()
            p_2.become(Sphere(radius=0.1).move_to([(-s ** 3, np.cos(-4 * s ** 3), np.sin(-4 * s ** 3))]))

        p_2.add_updater(mov_2)

        number_line2 = NumberLine(**line_config2).next_to(number_line, DOWN, buff=1)
        s = Dot(color=BLUE_C).move_to(number_line2.number_to_point(-(t0 ** (1 / 3))))  # ,UP,buff=0)#.scale(0.5)
        s_label = TextMobject("s").next_to(s, UP, buff=0.1)

        def mov_s(obj):
            sn = s1.get_value()
            s.become(Dot(color=BLUE_C).move_to(number_line2.number_to_point(sn)))  # ,UP,buff=0)#.scale(0.5)
            s_label.become(TextMobject("s").next_to(s, UP, buff=0.1))

        s.add_updater(mov_s)
        s_label.add_updater(mov_s)
        Movimiento_2 = VGroup(s, s_label)

        fondo2 = Circle(radius=20, color=BLACK, fill_opacity=1, fill_color=BLACK)
        self.add(p_1)
        self.add_fixed_in_frame_mobjects(number_line)
        self.add_fixed_in_frame_mobjects(Movimiento_1)
        self.play(ShowCreation(number_line), ShowCreation(Movimiento_1))
        self.play(t1.set_value, t0, run_time=20)
        # mov para la reparametrizacion
        self.add_fixed_in_frame_mobjects(number_line2)
        self.add_fixed_in_frame_mobjects(Movimiento_2)
        self.play(ShowCreation(number_line2), ShowCreation(Movimiento_2), ShowCreation(p_2))
        self.play(s1.set_value, t0 ** (1 / 3), run_time=20)
        self.wait()
        self.play(FadeOut(p_1), FadeOut(number_line), FadeOut(number_line2),
                  FadeOut(p_2), FadeOut(Movimiento_1), FadeOut(Movimiento_2))
        self.add_fixed_in_frame_mobjects(fondo2)
        self.play(GrowFromCenter(fondo2))

    def textos2(self):
        axis_config = {
            "x_min": -8,
            "x_max": 8,
            "y_min": -8,
            "y_max": 8,
            "z_min": -8,
            "z_max": 8,
        }
        text6 = TextMobject('''El punto recorre de una manera diferente a la curva \n
                                dependiendo de la parametrización.''')
        text7 = TextMobject('''Formalmente. \n
                               Sea $C\\in\mathbb{R}^{n}$ una curva y $\\gamma:I\\subset\\mathbb{R}\\rightarrow\\mathbb{R}^{n}$ \n
                                        una parametrización de C. \n ''',
                            ''' \n Si $f:A\\subset\\mathbb{R}\\rightarrow I\\subset\\mathbb{R}$ es sobreyectiva,\n
                           entonces \n
                           $\\rho=\\gamma\\circ f:A\\rightarrow\\mathbb{R}^{n}$ parametriza a $C$ \n
                           y es llamada una reparametrización de la curva.''')
        text7_1 = TextMobject('''Además, decimos que las reparametrizaciones conservan el sentido si''', '''\n
                                estas empiezan y terminanen los mismos puntos que la \n
                                 parametrización.''', '''Por otro lado,\n
                                    tienen sentido contrario si con al reparametrización \n
                                    empiezan y terminan al revés. ''')
        text7_2 = TextMobject('''¿Entonces la reparametrización del ejemplo conserva el sentido\n
                                         o lo cambia? ''')
        text8 = TextMobject('''La regla de la cadena nos dice que la derivada  \n
                                 de una función reparametrizada es: \n
                                    $\\rho'(t)=(f'\\cdot(\gamma'\\circ f))(t)$''')
        text9 = TextMobject(''' Veamos como se aplica lo anterior en la \n
                                     curva presentada al inicio.''')
        text10 = TextMobject(''' La derivada de la reparametrización es: \n''',
                             '''$\\xi'(s)=-3s^{2}(1,-4\\sin(-4s^{3}),4\\cos(-4s^{3})) $''').move_to(0.5* UP)
        text11 = TextMobject("Veamos como cambia $\\xi'$ conforme cambia s.").move_to(-0.5 * UP)

        axes = ThreeDAxes(**axis_config)
        tmin = -7
        tmax = 7
        vs = tmax ** (1 / 3)
        f = ParametricFunction(curva1p, t_min=tmin, t_max=tmax, color=RED)
        g = ParametricFunction(curva1p, t_min=tmin, t_max=tmax, color=BLUE_C)
        fondo = Rectangle(HEIGHT=FRAME_HEIGHT, WIDHT=FRAME_WIDTH, color=BLACK, fill_opacity=1)
        self.add_fixed_in_frame_mobjects(text6)
        self.play(Write(text6))
        self.wait(8)
        self.play(FadeOut(text6))
        ###FadeOutATODO
        self.add_fixed_in_frame_mobjects(text7[0])
        self.play(Write(text7[0]))
        self.add_fixed_in_frame_mobjects(text7[1])
        self.play(Write(text7[1]))
        self.wait(25)
        self.play(FadeOut(text7))
        self.add_fixed_in_frame_mobjects(text8)
        self.play(Write(text8))
        self.wait(11)
        self.play(FadeOut(text8))
        self.add_fixed_in_frame_mobjects(text9)
        self.play(Write(text9))
        self.wait(7)
        self.play(FadeOut(text9))
        self.add_fixed_in_frame_mobjects(text10)
        self.play(Write(text10))
        self.wait(13.2)
        self.play(FadeOut(text10[0]))
        self.add_fixed_in_frame_mobjects(text11)
        self.play(Write(text11))
        self.wait(6)
        self.play(FadeOut(text11), FadeOut(text10[1]))

    def construct(self):
        # Unión de las animaciones, siempre se pueden comentar algunas para que el proceso de compilación sea más corto
        # Presenta la primera parte de la animación
        self.textos1()
        self.wait()
        # Presenta el movimiento de una partícula con las dos parametrizaciones
        self.mov_particula()
        self.wait()
        # Presenta la segunda parte de los textos
        self.textos2()


class Reparametrizacion_de_curvas2(ThreeDScene):
    def construct(self):
        t0 = 7
        line_config = {
            "x_min": -t0 + 0.1,
            "x_max": t0 + 0.1,
            "unit_size": 0.3,
            "include_numbers": True,
            # "numbers_to_show": None,
            ##"longer_tick_multiple": 2,
            "number_at_center": 0,
            "number_scale_val": 0.5,
            "label_direction": DOWN,
            "line_to_number_buff": MED_SMALL_BUFF,
            "include_tip": False,
            "tip_width": 0.25,
            "tip_height": 0.25,

        }
        line_config2 = {
            "x_min": -(t0 ** (1 / 3)) - 0.2,
            "x_max": t0 ** (1 / 3) + 0.2,
            "unit_size": 1.1,
            "include_numbers": True,
            # "numbers_to_show": None,
            ##"longer_tick_multiple": 2,
            "number_at_center": 0,
            "number_scale_val": 0.3,
            "label_direction": DOWN,
            "line_to_number_buff": MED_SMALL_BUFF,
            "include_tip": False,
            "tip_width": 0.25,
            "tip_height": 0.25,

        }
        axis_config = {
            "x_min": -8,
            "x_max": 8,
            "y_min": -8,
            "y_max": 8,
            "z_min": -8,
            "z_max": 8,
        }

        t_15 = TextMobject('''Derivada de la parametrización.''').to_edge(UP)
        t_15.bg = SurroundingRectangle(t_15, color=WHITE, fill_color=BLACK, fill_opacity=1)
        text15=VGroup(t_15.bg,t_15)
        t_16 = TextMobject('''Derivada con la reparametrización.''').to_edge(UP)
        t_16.bg = SurroundingRectangle(t_16, color=WHITE, fill_color=BLACK, fill_opacity=1)
        text16=VGroup(t_16.bg,t_16)
        text12 = TextMobject('''Hay otra forma de saber si la reparametrización\n
        cambia el sentido. Si la derivada de la función que \n
        induce una reparametrización es positiva, \n
        entonces se conserva el sentido; si es negativa, \n
        sí cambia. ''')
        text13 = TextMobject('''¿Se te ocurre cómo saber cuál es el sentido \n
                                    de una curva simple cerrada? ''')
        text14 = TextMobject('''Modifica el código para crear más ejemplos.''')
        axes = ThreeDAxes(**axis_config)
        tmin = -5
        tmax = 5
        vs = tmax ** (1 / 3)
        g = ParametricFunction(curva1p, t_min=-t0, t_max=t0, color=BLUE_C)

        t2 = ValueTracker(tmin)
        number_line = NumberLine(**line_config).move_to(2 * DOWN + (3 - 0.5) * LEFT)
        
        # Movimiento para la parametrización
        p_parametrizacion = Sphere(radius=0.1, color=RED, fill_opacity=1).move_to(
            [tmin, np.cos(4 * tmin), np.sin(4 * tmin)])
        d_parametrizacion = Arrow((tmin, np.cos(4 * tmin), np.sin(4 * tmin)), (
        tmin + 1, np.cos(4 * tmin) - np.sin(4 * tmin) * 4, np.sin(4 * tmin) + np.cos(4 * tmin) * 4), buff=0)

        def mov_parametrizacion(obj):
            tp = t2.get_value()
            x = [tp, np.cos(4 * tp), np.sin(4 * tp)]
            p_parametrizacion.become(
                Sphere(radius=0.1, color=RED, fill_opacity=1).move_to([tp, np.cos(4 * tp), np.sin(4 * tp)]))
            d_parametrizacion.become(Arrow((tp, np.cos(4 * tp), np.sin(4 * tp)), (
            tp + 1, np.cos(4 * tp) - np.sin(4 * tp) * 4, np.sin(4 * tp) + np.cos(4 * tp) * 4), buff=0))

        cjto1 = VGroup(p_parametrizacion, d_parametrizacion)
        cjto1.add_updater(mov_parametrizacion)

        # el movimiento en el number plane
        t = Dot(color=BLUE_C).move_to(number_line.number_to_point(tmin))  # ,UP,buff=0)#.scale(0.5)
        t_label = TextMobject("t").next_to(t, UP, buff=0.1)

        def mov_plane1(obj):
            tn = t2.get_value()
            t.become(Dot(color=BLUE_C).move_to(number_line.number_to_point(tn)))
            t_label.become(TextMobject("t").next_to(t, UP, buff=0.1))

        cjto1_1 = VGroup(t, t_label)
        cjto1_1.add_updater(mov_plane1)

        # Derivada para la reparametrización
        s1 = ValueTracker(-(t0 ** (1 / 3)))
        n = 0.6  # reescalamentiento de la derivada
        p_reparametrizacion = Sphere(radius=0.1, color=RED, fill_opacity=1).move_to(
            [-(-vs) ** 3, np.cos(-4 * (-vs) ** 3), np.sin(-4 * (-vs) ** 3)])
        d_reparametrizacion = Arrow((-(-vs) ** 3, np.cos(-4 * (-vs) ** 3), np.sin(-4 * (-vs) ** 3)), (
        -(-vs) ** 3 - 3 * (-vs) ** 2 * n, np.cos(-4 * (-vs) ** 3) - np.sin(-4 * (-vs) ** 3) * (-12 * (-vs) ** 2) * n,
        np.sin(-4 * (-vs) ** 3) + np.cos(-4 * (-vs) ** 3) * (-12 * (-vs) ** 2) * n), buff=0)

        def mov_reparametrizacion(obj):
            s = s1.get_value()
            p_reparametrizacion.become(Sphere(radius=0.1, color=RED, fill_opacity=1).move_to(
                [-s ** 3, np.cos(-4 * s ** 3), np.sin(-4 * s ** 3)]))
            d_reparametrizacion.become(Arrow((-s ** 3, np.cos(-4 * s ** 3), np.sin(-4 * s ** 3)), (
            -s ** 3 - 3 * s ** 2 * n, np.cos(-4 * s ** 3) - np.sin(-4 * s ** 3) * (-12 * s ** 2) * n,
            np.sin(-4 * s ** 3) + np.cos(-4 * s ** 3) * (-12 * s ** 2) * n), buff=0))

        cjto2 = VGroup(p_reparametrizacion, d_reparametrizacion)
        cjto2.add_updater(mov_reparametrizacion)



        number_line2 = NumberLine(**line_config2).move_to(2 * DOWN + (3 - 0.5) * LEFT)
        s = Dot(color=BLUE_C).move_to(number_line2.number_to_point(-(t0 ** (1 / 3))))  # ,UP,buff=0)#.scale(0.5)
        s_label = TextMobject("s").next_to(s, UP, buff=0.1)
        t0=7
        
        def move_plane2(obj):
            sn = s1.get_value()
            s.become(Dot(color=BLUE_C).move_to(number_line2.number_to_point(sn)))  # ,UP,buff=0)#.scale(0.5)
            s_label.become(TextMobject("s").next_to(s, UP, buff=0.1))

        
       
        cjto2_1 = VGroup(s, s_label)
        cjto2_1.add_updater(move_plane2)


        self.set_camera_orientation(0.8 * np.pi / 2, -0.25 * np.pi, distance=20)
        self.play(ShowCreation(axes))
        self.play(ShowCreation(g))
        self.add_fixed_in_frame_mobjects(text15)
        self.play(Write(text15))
        self.wait(3)
        # Parte para la derivada de la parametrización
        self.add_fixed_in_frame_mobjects(number_line)
        self.add_fixed_in_frame_mobjects(cjto1_1)
        self.play(ShowCreation(cjto1), ShowCreation(number_line), ShowCreation(cjto1_1))
        self.play(t2.set_value, tmax, run_time=20)
        self.wait()

        self.play(FadeOut(text15), FadeOut(cjto1), FadeOut(number_line), FadeOut(cjto1_1))
        self.add_fixed_in_frame_mobjects(text16)
        self.play(Write(text16))
        self.wait(3.2)
        # Movimiento para la reparametrizacion
        self.add_fixed_in_frame_mobjects(number_line2)
        self.add_fixed_in_frame_mobjects(cjto2_1)
        self.play(ShowCreation(cjto2), ShowCreation(number_line2), ShowCreation(cjto2_1))
        self.play(s1.set_value, t0 ** (1 / 3), run_time=20)
        self.wait()
        self.play(FadeOut(axes), FadeOut(cjto2), FadeOut(g), FadeOut(text16), FadeOut(number_line2), FadeOut(cjto2_1))
        # termina movimiento de la segunda reparametrizacion

        self.add_fixed_in_frame_mobjects(text12)
        self.play(Write(text12))
        self.wait(16.6)
        self.play(FadeOut(text12))
        self.add_fixed_in_frame_mobjects(text13)
        self.play(Write(text13))
        self.wait(7.2)
        self.play(FadeOut(text13))
        self.add_fixed_in_frame_mobjects(text14)
        self.play(Write(text14))
        self.wait(5)
        self.play(FadeOut(text14))