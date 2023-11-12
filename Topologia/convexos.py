from manimlib.imports import *

#############################
#### CONJUNTOS CONVEXOS #####
#############################


class ConjuntosConvexos(Scene):
    def construct(self):
        # Título y texto
        titulo = TextMobject("Conjuntos Convexos").scale(1.5)
        pregunta = TextMobject(
            "¿Cuál es la diferencia entre estos dos conjuntos?"
        ).to_edge(UP)

        # Conjunto convexo(izq)

        lao_svg = (
            SVGMobject("Topologia_SVGs/convexo.svg")
            .set_height(FRAME_HEIGHT * 0.4)
            .shift(3 * LEFT)
        )
        lao_svg.set_style(
            fill_opacity=0.7, stroke_width=0, stroke_opacity=1, fill_color=BLUE
        )
        lao_label = TextMobject("A").next_to(lao_svg, DOWN)
        lao = VGroup(lao_svg, lao_label)

        # Conjunto no-convexo(der)

        lau_svg = (
            SVGMobject("Topologia_SVGs/no_convexo.svg")
            .set_height(FRAME_HEIGHT * 0.4)
            .shift(3 * RIGHT)
        )
        lau_svg.set_style(
            fill_opacity=0.5, stroke_width=0, stroke_opacity=1, fill_color=YELLOW
        )
        lau_label = TextMobject("B").next_to(lau_svg, DOWN)
        lau = VGroup(lau_svg, lau_label)

        # "De manera informal"

        casual_1 = TextMobject("De manera informal, podríamos decir que el").to_edge(UP)
        casual_2 = TextMobject("conjunto B tiene una hendidura. ").next_to(
            casual_1, DOWN
        )
        casual = VGroup(casual_1, casual_2)
        formal = TextMobject("Formalicemos lo anterior.").to_edge(DOWN).scale(1.1)

        # Definición segmento de recta

        equis_dot = Dot(point=(-3, 1, 0))
        equis_label = TexMobject(r"\vec{x}").next_to(equis_dot, UP + LEFT)
        equis = VGroup(equis_dot, equis_label)
        ye_dot = Dot(point=(3, -1, 0))
        ye_label = TexMobject(r"\vec{y}").next_to(ye_dot, DOWN + RIGHT)
        ye = VGroup(ye_dot, ye_label)
        segmento_a = TextMobject("Dados dos puntos en $\mathbb{R}^n$,").to_edge(UP)  ##
        segmento_aa = TextMobject("definimos el segmento que los une como:").next_to(
            segmento_a, DOWN
        )
        segmento_b = TexMobject(
            r"[\vec{x},\vec{y}]=\{ (1-t)\vec{x}+t\vec{y}\in \mathbb{R}^n | t\in [0,1]\}"
        )  ###
        segmento_c = TextMobject(
            "Visualizando lo anterior en $\mathbb{R}^2$, tenemos:"
        ).to_edge(UP)
        segmento = Line(start=(-3, 1, 0), end=(3, -1, 0))  ###
        segmento_d = TexMobject(
            r"[\vec{x},\vec{y}]=\{ (1-t)\vec{x}+t\vec{y}\in \mathbb{R}^2 | t\in [0,1]\}"
        ).to_edge(DOWN)

        # Centrado conjunto convexo

        lao_svg_1 = SVGMobject("Topologia_SVGs/convexo.svg").set_height(
            FRAME_HEIGHT * 0.4
        )
        lao_svg_1.set_style(
            fill_opacity=0.7, stroke_width=0, stroke_opacity=1, fill_color=BLUE
        )
        Acomment = (
            TextMobject(
                "Para cualesquiera dos puntos $\\vec{x},\\vec{y} \\in$ A,  tenemos que $[\\vec{x},\\vec{y}]\\subset$ A"
            )
            .to_edge(UP)
            .scale(0.9)
        )
        ## Pares de puntos para A
        par_A1 = VGroup(
            Dot(point=(1, 1, 0)),
            Dot(point=(-1, -1, 0)),
            Line(start=(1, 1, 0), end=(-1, -1, 0)),
        )
        par_A2 = VGroup(
            Dot(point=(0, 1, 0)),
            Dot(point=(0, -1, 0)),
            Line(start=(0, 1, 0), end=(0, -1, 0)),
        )
        par_A3 = VGroup(
            Dot(point=(-0.7, 1.1, 0)),
            Dot(point=(0.5, -1.1, 0)),
            Line(start=(-0.7, 1.1, 0), end=(0.5, -1.1, 0)),
        )
        convexo = (
            TextMobject("A esto se le conoce como un", " conjunto convexo.")
            .to_edge(DOWN)
            .scale(0.9)
        )
        convexo[1].set_color(BLUE)  ##

        # Centrado conjunto no convexo

        lau_svg_1 = SVGMobject("Topologia_SVGs/no_convexo.svg").set_height(
            FRAME_HEIGHT * 0.4
        )
        lau_svg_1.set_style(
            fill_opacity=0.5, stroke_width=0, stroke_opacity=1, fill_color=YELLOW
        )
        Bcomment_a = TextMobject("Esto no sucede para el conjunto B, pues").to_edge(UP)
        Bcomment_b = TextMobject(
            "existen $\\vec{x},\\vec{y}\\subset$ B tales que $[\\vec{x},\\vec{y}]\\not\\subseteq$ B"
        ).next_to(Bcomment_a, DOWN)
        Bcomment = VGroup(Bcomment_a, Bcomment_b).scale(0.9)
        ##Pares de puntos para B
        par_B1 = VGroup(
            Dot(point=(-0.5, 1, 0)),
            Dot(point=(-0.5, -1, 0)),
            Line(start=(-0.5, 1, 0), end=(-0.5, -1, 0)),
        )
        par_B2 = VGroup(
            Dot(point=(-0.2, -1, 0)),
            Dot(point=(0.7, -1, 0)),
            Line(start=(-0.2, -1, 0), end=(0.7, -1, 0)),
        )
        par_B3 = VGroup(
            Dot(point=(-0.8, 1, 0)),
            Dot(point=(0.8, 1, 0)),
            Line(start=(-0.8, 1, 0), end=(0.8, 1, 0)),
        ).set_color(RED)
        no_convexo = (
            TextMobject("Este conjunto es", " no convexo.").to_edge(DOWN).scale(0.9)
        )
        no_convexo[1].set_color(YELLOW)

        entonces = TextMobject("Entonces, de manera formal:").to_edge(UP)
        lao_conv = TextMobject("Convexo").next_to(lao_label, 2 * DOWN).set_color(BLUE)
        lau_nconv = (
            TextMobject("No convexo").next_to(lau_label, 2 * DOWN).set_color(YELLOW)
        )

        # pregunta

        pregunta1 = TextMobject("Ahora es tu turno: ")
        pregunta2 = TextMobject(
            "Si un conjunto es convexo, ¿también es conexo?"
        ).next_to(pregunta1, DOWN)

        # Secuencia de la animación
        self.play(Write(titulo))
        self.wait()
        self.play(FadeOut(titulo))
        self.play(Write(pregunta, run_time=2))
        self.wait()
        self.play(Write(lao), Write(lau))
        self.wait()
        self.play(FadeOut(pregunta))
        self.play(Write(casual, run_time=5))  #
        self.wait(2)
        self.play(Write(formal))
        self.wait(1)
        self.play(FadeOut(casual), FadeOut(formal), FadeOut(lao), FadeOut(lau))
        # Animación definición
        self.play(Write(segmento_a))
        self.play(Write(segmento_aa, run_time=2))
        self.wait()
        self.play(Write(segmento_b, run_time=3))
        self.wait(3)
        self.play(FadeOut(segmento_aa))
        self.play(ReplacementTransform(segmento_a, segmento_c))
        self.play(ReplacementTransform(segmento_b, segmento_d))
        self.play(Write(equis), Write(ye))
        self.play(Write(segmento))
        self.wait(3)
        self.play(
            FadeOut(equis),
            FadeOut(ye),
            FadeOut(segmento),
            FadeOut(segmento_c),
            FadeOut(segmento_d),
        )
        # Animación conjunto convexo
        self.play(Write(lao_svg_1))
        self.play(Write(Acomment, run_time=3))
        self.bring_to_back(lao_svg_1)
        self.play(ShowCreation(par_A1))
        self.wait(1.2)
        self.play(ReplacementTransform(par_A1, par_A2))
        self.wait(1.2)
        self.play(ReplacementTransform(par_A2, par_A3))
        self.wait(1.2)
        self.play(Write(convexo))
        self.wait()
        self.play(
            FadeOut(Acomment), FadeOut(convexo), FadeOut(lao_svg_1), FadeOut(par_A3)
        )
        # Animación conjunto NO convexo
        self.play(Write(lau_svg_1))
        self.play(Write(Bcomment, run_time=3))
        self.bring_to_back(lau_svg_1)
        self.wait()
        self.play(ShowCreation(par_B1))
        self.wait(1.2)
        self.play(ReplacementTransform(par_B1, par_B2))
        self.wait(1.2)
        self.play(ReplacementTransform(par_B2, par_B3))
        self.play(par_B3.scale, 1.4)
        self.play(par_B3.scale, 1 / 1.4)
        self.wait()
        self.play(Write(no_convexo))
        self.wait()
        self.play(
            FadeOut(Bcomment), FadeOut(no_convexo), FadeOut(lau_svg_1), FadeOut(par_B3)
        )
        # Animación conclusión
        self.play(Write(entonces))
        self.play(Write(lao), Write(lau))
        self.play(Write(lao_conv))
        self.play(Write(lau_nconv))
        self.wait(2)
        self.play(
            FadeOut(entonces),
            FadeOut(lao),
            FadeOut(lau),
            FadeOut(lao_conv),
            FadeOut(lau_nconv),
        )
        self.wait()
        self.play(Write(pregunta1))
        self.play(Write(pregunta2))
        self.wait(6)
        self.play(FadeOut(pregunta1),FadeOut(pregunta2))


class ScreenGrid(VGroup):
    CONFIG = {
        "rows": 8,
        "columns": 14,
        "height": FRAME_Y_RADIUS * 2,
        "width": 14,
        "grid_stroke": 0.5,
        "grid_color": WHITE,
        "axis_color": RED,
        "axis_stroke": 2,
        "labels_scale": 0.25,
        "labels_buff": 0,
        "number_decimals": 2,
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        rows = self.rows
        columns = self.columns
        grid = Grid(width=self.width, height=self.height, rows=rows, columns=columns)
        grid.set_stroke(self.grid_color, self.grid_stroke)

        vector_ii = ORIGIN + np.array((-self.width / 2, -self.height / 2, 0))
        vector_si = ORIGIN + np.array((-self.width / 2, self.height / 2, 0))
        vector_sd = ORIGIN + np.array((self.width / 2, self.height / 2, 0))

        axes_x = Line(LEFT * self.width / 2, RIGHT * self.width / 2)
        axes_y = Line(DOWN * self.height / 2, UP * self.height / 2)

        axes = VGroup(axes_x, axes_y).set_stroke(self.axis_color, self.axis_stroke)

        divisions_x = self.width / columns
        divisions_y = self.height / rows

        directions_buff_x = [UP, DOWN]
        directions_buff_y = [RIGHT, LEFT]
        dd_buff = [directions_buff_x, directions_buff_y]
        vectors_init_x = [vector_ii, vector_si]
        vectors_init_y = [vector_si, vector_sd]
        vectors_init = [vectors_init_x, vectors_init_y]
        divisions = [divisions_x, divisions_y]
        orientations = [RIGHT, DOWN]
        labels = VGroup()
        set_changes = zip(
            [columns, rows], divisions, orientations, [0, 1], vectors_init, dd_buff
        )
        for c_and_r, division, orientation, coord, vi_c, d_buff in set_changes:
            for i in range(1, c_and_r):
                for v_i, directions_buff in zip(vi_c, d_buff):
                    ubication = v_i + orientation * division * i
                    coord_point = round(ubication[coord], self.number_decimals)
                    label = Text(f"{coord_point}", font="Arial", stroke_width=0).scale(
                        self.labels_scale
                    )
                    label.next_to(ubication, directions_buff, buff=self.labels_buff)
                    labels.add(label)

        self.add(grid, axes, labels)