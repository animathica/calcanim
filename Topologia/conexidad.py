from manimlib.imports import *

##########################################
##### CONJUNTOS CONEXOS Y DISCONEXOS #####
##########################################

##Vídeo conjuntos conexos y disconexos
class ConjuntosConexos(Scene):
    def construct(self):
        # Título y texto
        titulo = TextMobject("Disconexidad y Conexidad").scale(1.5)
        intui = TextMobject(
            "De forma intuitiva, un conjunto", " disconexo", " es aquel"
        )
        intui[1].set_color(GREEN_C)
        tivo = TextMobject("compuesto por dos o más partes", " separadas").next_to(
            intui, DOWN
        )
        tivo[1].set_color(GREEN_C)
        intuitivo = VGroup(intui, tivo)
        tdisconexo_a = TextMobject(
            "Formalmente, un conjunto es", " disconexo", " si y sólo si"
        )
        tdisconexo_a[1].set_color(GREEN_C)
        tdisconexo_b = TextMobject(
            "satisface tres propiedades con respecto a otros conjuntos:"
        ).next_to(tdisconexo_a, DOWN)
        tdisconexo = VGroup(tdisconexo_a, tdisconexo_b)

        # Conjunto disconexo
        el_disconexo = TextMobject(
            " A", " es un conjunto", " disconexo", " si y sólo si "
        ).to_edge(UP)
        el_disconexo[0].set_color(GREEN_C)
        el_disconexo[2].set_color(GREEN_C)
        disconexo = SVGMobject(
            "Topologia_SVGs/disconexo.svg",
            fill_color=GREEN_C,
            fill_opacity=1,
            stroke_opacity=0,
        ).shift(3 * LEFT)
        disconexo_label = (
            TextMobject("A")
            .next_to(disconexo.get_center(), 5 * DOWN)
            .set_color(GREEN_C)
        )
        gdisconexo = VGroup(disconexo, disconexo_label)

        # Conjuntos abiertos
        abiertos = (
            TextMobject("Existen ", "U", " y", " V", " conjuntos abiertos tales que:")
            .scale(0.9)
            .shift(2 * UP + 3 * RIGHT)
        )
        abiertos[1].set_color(ORANGE)
        abiertos[3].set_color(YELLOW)
        cjtoU_set = (
            Circle(radius=1.0, fill_opacity=0.6, stroke_opacity=0,stroke_width=0)
            .shift(4.2 * LEFT)
            .set_color(ORANGE)
        )
        cjtoU_label = TextMobject("U").next_to(cjtoU_set, UP).set_color(ORANGE)
        cjtoU = VGroup(cjtoU_set, cjtoU_label)
        cjtoV_set = (
            Circle(radius=1.0, fill_opacity=0.6, stroke_opacity=0,stroke_width=0)
            .shift(1.8 * LEFT)
            .set_color(YELLOW)
        )
        cjtoV_label = TextMobject("V").next_to(cjtoV_set, UP).set_color(YELLOW)
        cjtoV = VGroup(cjtoV_set, cjtoV_label)
        cjtoU1_set = (
            Circle(radius=1.5, fill_opacity=0.6, stroke_opacity=0,stroke_width=0)
            .shift(4.2 * LEFT)
            .set_color(ORANGE)
        )
        cjtoU1_label = TextMobject("U").next_to(cjtoU1_set, UP).set_color(ORANGE)
        cjtoU1 = VGroup(cjtoU1_set, cjtoU1_label)
        cjtoV1_set = (
            Circle(radius=1.5, fill_opacity=0.6, stroke_opacity=0,stroke_width=0)
            .shift(1.8 * LEFT)
            .set_color(YELLOW)
        )
        cjtoV1_label = TextMobject("V").next_to(cjtoV1_set, UP).set_color(YELLOW)
        cjtoV1 = VGroup(cjtoV1_set, cjtoV1_label)
        inter = (
            SVGMobject("Topologia_SVGs/inter.svg", stroke_opacity=0, fill_opacity=0.8)
            .shift(3 * LEFT)
            .scale(0.93)
        )  # A ojo para darle al tamaño
        inter_label = TexMobject(r" U \cap V").next_to(inter, 2 * UP)
        intergroup = VGroup(inter, inter_label)
        abiertos_labels = VGroup(cjtoU_label, cjtoV_label)
        abiertos_labels1 = VGroup(cjtoU1_label, cjtoV1_label)
        union_label = (
            TexMobject(r" U \cup V").next_to(inter, 2.5 * UP).set_color(YELLOW_E)
        )

        # Primera propiedad

        prop_1 = TexMobject(r"1)\ A \subset U \cup V").shift(1 * UP + 1.8 * RIGHT)
        prop_1a = TexMobject(r"\text{1)}", r"\ A ", r"\subset", r"{U \cup V}").shift(
            1 * UP + 1.8 * RIGHT
        )
        prop_1a.set_color_by_tex_to_color_map({"A": GREEN_C, "{U \cup V}": YELLOW_E})

        # Segunda propiedad

        prop_2 = TexMobject(r"2)\ A \cap U \neq \varnothing").shift(1.82 * RIGHT)
        prop_2_2 = TexMobject(r"\text{y}\ A \cap V \neq \varnothing").next_to(
            prop_2, RIGHT
        )

        # Tercera propiedad

        prop_3 = TexMobject(r"3) \ U \cap V = \varnothing").shift(
            1 * DOWN + 1.82 * RIGHT
        )
        caracts = VGroup(prop_1, prop_2, prop_3)

        # Comenzamos con conexos
        conex_a = TextMobject(
            "Un conjunto es",
            " conexo",
            "  si \\textbf{no} es",
            " disconexo",
            " es decir,",
        )
        conex_a[1].set_color(BLUE)
        conex_a[3].set_color(GREEN_C)
        conex_b = TextMobject("si cualesquiera dos conjuntos abiertos U y V no cumplen").next_to(
            conex_a, DOWN
        )
        conex_c = TextMobject("alguna de las tres propiedades.").next_to(conex_b, DOWN)
        conex = VGroup(conex_a, conex_b, conex_c)
        ejs = TextMobject("Veamos algunos ejemplos:")

        satisface = TextMobject("El conjunto satisface:").move_to(abiertos)
        no_satisface1 = (
            TextMobject("\\textbf{No} satisface la primera propiedad, pues:")
            .shift(1 * DOWN + 3.2 * RIGHT)
            .scale(0.75)
        )
        no_satisface2 = (
            TextMobject("\\textbf{No} satisface la segunda propiedad, pues:")
            .shift(1 * DOWN + 3.2 * RIGHT)
            .scale(0.75)
        )
        no_satisface3 = (
            TextMobject("\\textbf{No} satisface la tercera propiedad, pues:")
            .shift(1 * DOWN + 3.2 * RIGHT)
            .scale(0.75)
        )

        esconexo = TextMobject("Este conjunto es", " conexo.").to_edge(DOWN)
        esconexo[1].set_color(BLUE)

        # Conexo1

        conexo1_svg = (
            SVGMobject(
                "Topologia_SVGs/conexo1.svg",
                stroke_opacity=0,
                fill_opacity=1,
                fill_color=BLUE,
            )
            .shift(3 * LEFT)
            .scale(0.5)
        )
        conexo1_label = TextMobject("B").next_to(conexo1_svg, 4 * DOWN).set_color(BLUE)
        conexo1 = VGroup(conexo1_svg, conexo1_label)

        conexo1_p1 = TexMobject(r" B \subset U \cup V").shift(1 * UP + 1.8 * RIGHT)
        conexo1_p2 = TexMobject(
            r" B \cap U \neq \varnothing\ \text{y}\ B \cap V \neq \varnothing"
        ).shift(3.2 * RIGHT)
        conexo1_p3 = TexMobject(r" U \cap V \neq \varnothing").next_to(
            no_satisface3, DOWN
        )

        textc1 = VGroup(satisface, conexo1_p1, conexo1_p2, conexo1_p3, no_satisface3)

        # Conexo2

        conexo2_svg = (
            SVGMobject(
                "Topologia_SVGs/conexo2.svg",
                stroke_opacity=0,
                fill_opacity=1,
                fill_color=BLUE,
            )
            .shift(4 * LEFT)
            .scale(0.5)
        )
        conexo2_label = TextMobject("C").next_to(conexo2_svg, 5 * DOWN).set_color(BLUE)
        conexo2 = VGroup(conexo2_svg, conexo2_label)
        conexo2_p1 = TexMobject(r" C \subset U \cup V").shift(1 * UP + 1.8 * RIGHT)
        conexo2_p3 = TexMobject(r" U \cap V = \varnothing").shift(2.2 * RIGHT)
        conexo2_p2 = TexMobject(r"\ C \cap V = \varnothing").next_to(
            no_satisface3, DOWN
        )
        textc2 = VGroup(satisface, conexo2_p1, conexo2_p2, conexo2_p3, no_satisface2)

        # Conexo3

        conexo3_svg = (
            SVGMobject(
                "Topologia_SVGs/conexo3.svg",
                stroke_opacity=0,
                fill_opacity=1,
                fill_color=BLUE,
            )
            .shift(3.05 * LEFT + 0.5 * UP)
            .scale(1)
        )
        conexo3_label = TextMobject("D").next_to(conexo3_svg, 3 * UP).set_color(BLUE)
        conexo3 = VGroup(conexo3_svg, conexo3_label)

        # Etiquetas de unión e interseccion para mostrar abajo

        inter_dlabel = TexMobject(r" U \cap V").next_to(inter, 2 * DOWN)
        union_dlabel = (
            TexMobject(r" U \cup V").next_to(inter, 2.5 * DOWN).set_color(YELLOW_E)
        )
        conexo3_p2 = TexMobject(
            r" D \cap U \neq \varnothing\ \text{y}\ D \cap V \neq \varnothing"
        ).shift(1 * UP + 3 * RIGHT)
        conexo3_p3 = TexMobject(r" U \cap V = \varnothing").shift(2.2 * RIGHT)
        conexo3_p1 = TexMobject(r" D \not\subset U \cup V").next_to(no_satisface3, DOWN)
        textc3 = VGroup(satisface, conexo3_p1, conexo3_p2, conexo3_p3, no_satisface1)

        # Comentario final

        cfinal_a = TextMobject(
            "¡Si un conjunto es", " conexo", ", ningún par de conjuntos abiertos"
        )
        cfinal_a[1].set_color(BLUE)
        cfinal_b = TextMobject("podrán satisfacer las tres propiedades mencionadas!").next_to(
            cfinal_a, DOWN
        )
        cfinal = VGroup(cfinal_a, cfinal_b)

        # Secuencia de la animación

        self.play(Write(titulo))
        self.play(FadeOut(titulo))
        self.play(Write(intuitivo))
        self.wait(8)
        self.play(FadeOut(intuitivo))
        self.play(Write(tdisconexo))
        self.wait(8)
        self.play(FadeOut(tdisconexo))
        # Propiedades de un conjunto disconexo
        self.play(Write(el_disconexo))
        self.play(DrawBorderThenFill(disconexo), Write(disconexo_label))
        self.wait()
        self.play(Write(abiertos))
        self.bring_to_back(cjtoU)
        self.play(Write(cjtoU))
        self.bring_to_back(cjtoV)
        self.play(Write(cjtoV))
        self.play(Write(prop_1), abiertos_labels.set_opacity, 0)
        self.play(
            cjtoU_set.set_color,
            YELLOW_E,
            cjtoU_set.set_opacity,
            0.6,
            cjtoV_set.set_color,
            YELLOW_E,
            cjtoV_set.set_opacity,
            0.6,
            Write(union_label),
        )
        self.wait(1.5)
        self.play(FadeOut(union_label), FadeOut(cjtoU_set), FadeOut(cjtoV_set))
        self.wait()
        self.play(Write(prop_2))
        self.play(
            cjtoU_label.set_opacity,
            0.9,
            cjtoU_set.set_color,
            ORANGE,
            cjtoU_set.set_opacity,
            0.6,
        )
        self.wait()
        self.play(FadeOut(cjtoU))
        self.wait()
        self.play(Write(prop_2_2))
        self.play(
            cjtoV_label.set_opacity,
            0.9,
            cjtoV_set.set_color,
            YELLOW,
            cjtoV_set.set_opacity,
            0.6,
        )
        self.wait()
        self.play(FadeOut(cjtoV))
        self.wait(1.5)
        self.play(Write(prop_3))
        self.wait(1.5)
        self.play(Write(cjtoU), Write(cjtoV))
        self.wait(1.5)
        self.play(
            FadeOut(cjtoU),
            FadeOut(cjtoV),
            FadeOut(gdisconexo),
            FadeOut(caracts),
            FadeOut(el_disconexo),
            FadeOut(abiertos),
            FadeOut(prop_2_2),
        )
        self.play(Write(conex_a))
        self.wait()
        self.play(Write(conex_b))
        self.play(Write(conex_c))
        self.wait()
        self.play(FadeOut(conex))
        self.play(Write(ejs))
        self.wait()
        self.play(FadeOut(ejs))

        # ANIMACIÓN:PROPIEDADES CONEXO 1

        self.play(DrawBorderThenFill(conexo1))
        self.wait()
        self.play(Write(satisface))
        self.bring_to_back(cjtoU1)
        self.bring_to_back(cjtoV1)
        self.play(Write(cjtoU1), Write(cjtoV1), abiertos_labels1.set_opacity, 1)
        self.wait()
        self.play(Write(conexo1_p1), abiertos_labels1.set_opacity, 0)
        self.play(
            cjtoU1_set.set_color,
            YELLOW_E,
            cjtoU1_set.set_opacity,
            0.6,
            cjtoV1_set.set_color,
            YELLOW_E,
            cjtoV1_set.set_opacity,
            0.6,
            Write(union_label),
        )  ###YELLOW
        self.wait(1.5)
        self.play(Write(conexo1_p2))
        self.play(abiertos_labels1.set_opacity, 1, FadeOut(union_label))
        self.play(
            cjtoU1_set.set_color,
            ORANGE,
            cjtoU1_set.set_opacity,
            0.6,
            cjtoV1_set.set_color,
            YELLOW,
            cjtoV1_set.set_opacity,
            0,
            cjtoV1_label.set_opacity,
            0,
        )
        self.wait()
        self.wait(1.5)
        self.play(cjtoV1_set.set_opacity, 0.6)
        self.wait(1.5)
        self.play(
            cjtoU1_set.set_opacity,
            0.6,
            cjtoV1_set.set_opacity,
            0.6,
            cjtoV1_label.set_opacity,
            1,
            cjtoU1_set.set_opacity,
            0,
            cjtoU1_label.set_opacity,
            0,
        )
        self.wait(1.5)
        self.play(cjtoU1_set.set_opacity, 0.6, cjtoU1_label.set_opacity, 1)
        self.play(Write(no_satisface3))
        self.play(Write(conexo1_p3))
        self.wait(2)
        self.play(Write(esconexo))
        self.wait(8)
        self.play(
            FadeOut(textc1),
            FadeOut(conexo1),
            FadeOut(esconexo),
            FadeOut(abiertos_labels1),
            FadeOut(cjtoV1),
            FadeOut(cjtoU1),
        )

        # ANIMACIÓN:PROPIEDADES CONEXO 2

        self.play(DrawBorderThenFill(conexo2))
        self.wait()
        self.play(Write(satisface))
        self.bring_to_back(cjtoU)
        self.play(
            cjtoU_set.set_color,
            ORANGE,
            cjtoU_set.set_opacity,
            0.6,
            cjtoV_set.set_opacity,
            0.6,
            abiertos_labels.set_opacity,
            1,
        )
        self.play(Write(conexo2_p1), abiertos_labels.set_opacity, 0)
        self.play(
            cjtoU_set.set_color,
            YELLOW_E,
            cjtoU_set.set_opacity,
            0.6,
            cjtoV_set.set_color,
            YELLOW_E,
            cjtoV_set.set_opacity,
            0.6,
            Write(union_label),
        )  ###YELLOW
        self.wait(1.5)
        self.play(Write(conexo2_p3))
        self.play(FadeOut(union_label))
        self.play(
            cjtoU_set.set_color,
            ORANGE,
            cjtoU_set.set_opacity,
            0.6,
            cjtoU_label.set_opacity,
            0.6,
            cjtoV_set.set_color,
            YELLOW,
            cjtoV_set.set_opacity,
            0,
        )
        self.wait()
        self.play(Write(no_satisface2))
        self.play(Write(conexo2_p2))
        self.play(Write(cjtoV_label))
        self.play(cjtoV.set_opacity, 0.6)
        self.wait()
        self.play(Write(esconexo))
        self.wait(1)
        self.play(
            FadeOut(conexo2), FadeOut(textc2), FadeOut(esconexo), cjtoV.set_opacity, 0
        )

        # ANIMACIÓN:PROPIEDADES CONEXO 3

        self.play(Write(conexo3))
        self.wait()
        self.play(
            cjtoU_set.set_color,
            ORANGE,
            cjtoU_set.set_opacity,
            0.6,
            cjtoV_set.set_color,
            YELLOW,
            cjtoV_set.set_opacity,
            0.6,
            cjtoU_label.set_opacity,
            1,
            cjtoV_label.set_opacity,
            1,
        )
        self.play(Write(satisface))
        self.play(Write(conexo3_p2))
        self.play(cjtoU.set_opacity, 0.6, cjtoV.set_opacity, 0)
        self.wait(1.5)
        self.play(cjtoU.set_opacity, 0, cjtoV.set_opacity, 0.6)
        self.wait(1.5)
        self.play(
            cjtoU_set.set_opacity,
            0.6,
            cjtoV_set.set_opacity,
            0.6,
            abiertos_labels.set_opacity,
            1,
        )
        self.wait()
        self.play(Write(conexo3_p3))
        self.wait()
        self.play(Write(no_satisface1))
        self.bring_to_back(cjtoU)
        self.bring_to_back(cjtoV)
        self.play(
            cjtoU_set.set_opacity,
            0.6,
            cjtoV_set.set_opacity,
            0.6,
            abiertos_labels.set_opacity,
            1,
        )
        self.play(Write(conexo3_p1))
        self.play(
            cjtoU_set.set_color,
            YELLOW_E,
            cjtoU_set.set_opacity,
            0.6,
            cjtoV_set.set_color,
            YELLOW_E,
            cjtoV_set.set_opacity,
            0.6,
            abiertos_labels.set_opacity,
            0,
            Write(union_dlabel),
        )
        self.wait(1.5)
        self.play(Write(esconexo))
        self.wait(5)
        self.play(
            FadeOut(textc3),
            FadeOut(conexo3),
            FadeOut(esconexo),
            FadeOut(cjtoU),
            FadeOut(cjtoV),
            FadeOut(union_dlabel),
            cjtoV_set.set_opacity,
            0,
            cjtoU_set.set_opacity,
            0,
        )
        # Comentario fnal
        self.play(Write(cfinal))
        self.wait(7)
        self.play(FadeOut(cfinal))