from manimlib.imports import *

####IMAGEN INVERSA
class ImgInversa(GraphScene):
    def construct(self):
        titulo = TextMobject("Imagen Inversa")
        # titulo_b = TextMobject("$f: \\mathbb{R}^n \\to \\mathbb{R}^m$").next_to(titulo_a,DOWN)
        # titulo = VGroup(titulo_a, titulo_b)
        text_1a = TextMobject("Sea $f$ una función ").to_edge(UP)
        text_1b = TexMobject(r"f: ","A",r"\subset\mathbb{R}^n \to \mathbb{R}^m").next_to(text_1a, DOWN)
        text_1b.set_color_by_tex_to_color_map({
            "A": BLUE,
        })
        text_1 = VGroup(text_1a, text_1b)

        ### Todo para ilustrar la "acción" de nuestra función
        EjeY_1 = Arrow(start=(0, -1, 0), end=(0, 4, 0), stroke_width=2)
        EjeX_1 = Arrow(start=(-1, 0, 0), end=(4, 0, 0), stroke_width=2)
        Ejes_1 = VGroup(EjeX_1, EjeY_1).shift(5 * LEFT + 2.5 * DOWN)

        EjeY_2 = Arrow(start=(0, -1, 0), end=(0, 4, 0), stroke_width=2)
        EjeX_2 = Arrow(start=(-1, 0, 0), end=(4, 0, 0), stroke_width=2)
        Ejes_2 = VGroup(EjeX_2, EjeY_2).shift(2 * RIGHT + 2.5 * DOWN)

        A_svg_1 = SVGMobject('Func_SVGs/enRn.svg').set_height(FRAME_HEIGHT * 0.3)
        A_svg_1.set_style(fill_opacity=0.7, stroke_width=0, stroke_opacity=1, fill_color=BLUE)
        A_svg_1.shift(DOWN + 3 * LEFT)

        A_svg_2 = SVGMobject('Func_SVGs/enRn.svg').set_height(FRAME_HEIGHT * 0.3)
        A_svg_2.set_style(fill_opacity=0, stroke_width=0, stroke_opacity=1, fill_color=BLUE)
        A_svg_2.shift(DOWN + 3 * LEFT)

        A_svg_2 = SVGMobject('Func_SVGs/enRn.svg').set_height(FRAME_HEIGHT * 0.3)
        A_svg_2.set_style(fill_opacity=0, stroke_width=0, stroke_opacity=1, fill_color=BLUE)
        A_svg_2.shift(DOWN + 3 * LEFT)

        A_svg_2 = SVGMobject('Func_SVGs/enRn.svg').set_height(FRAME_HEIGHT * 0.3)
        A_svg_2.set_style(fill_opacity=0, stroke_width=0, stroke_opacity=1, fill_color=BLUE)
        A_svg_2.shift(DOWN + 3 * LEFT)

        A_svg_2 = SVGMobject('Func_SVGs/enRn.svg').set_height(FRAME_HEIGHT * 0.3)
        A_svg_2.set_style(fill_opacity=0, stroke_width=0, stroke_opacity=1, fill_color=BLUE)
        A_svg_2.shift(DOWN + 3 * LEFT)

        f_arrow = Arrow(start_point=LEFT, end_point=RIGHT, stroke_width=2.5)
        f_label = TexMobject(r"f").next_to(f_arrow, UP)
        f = VGroup(f_arrow, f_label)

        B_svg = SVGMobject('Func_SVGs/enRm.svg').set_height(FRAME_HEIGHT * 0.3)
        B_svg.set_style(fill_opacity=0.8, stroke_width=0, stroke_opacity=1, fill_color=ORANGE)
        B_svg.shift(0.7 * DOWN + 4 * RIGHT)

        ## Mencionamos y dibujamos el conjunto D en el contradominio
        text_2a = TextMobject("Si nos tomamos un subconjunto", " $D$ ", "en el contradominio").to_edge(UP)
        text_2a[1].set_color(YELLOW)
        text_2b = TextMobject("(en este caso solamente tres puntos)").scale(0.7).next_to(text_2a, DOWN)
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

        text_3 = TextMobject("Podemos preguntarnos, ¿de qué parte de"," A"," provienen?").to_edge(UP)
        text_3.set_color_by_tex_to_color_map({
            "A": BLUE,
        })
        ## Ahora si, mencionamos y dibujamos los puntos que son la imagen inversa
        text_4 = TextMobject("Buscamos $\\{\\vec{x}\\in A | f(\\vec{x})\\in D \\}$").to_edge(UP)
        C_1 = Dot(point=(-3.2, -1, 0)).set_color(RED)
        A_C1D1 = Arrow(start=(-3.2, -1, 0), end=(3.2, -1, 0), stroke_width=2)
        C_2 = Dot(point=(-3.3, -0.5, 0)).set_color(RED)
        A_C2D3 = Arrow(start=(-3.3, -0.5, 0), end=(3, -0.8, 0), stroke_width=2)
        C_3 = Dot(point=(-3, -0.8, 0)).set_color(RED)
        A_C3D2 = Arrow(start=(-3, -0.8, 0), end=(3.3, -0.5, 0), stroke_width=2)
        finv_label = TexMobject(r"f^{-1}(D)").set_color(RED).next_to(A_svg_1, 1.5 * UP)

        finv_stuff = VGroup(C_1, A_C1D1, C_2, A_C2D3, C_3, A_C3D2, finv_label)

        text_5a = TextMobject("$f^{-1}(D)$", "$:=\\{\\vec{x}\\in A | f(\\vec{x})\\in D \\}$").to_edge(UP)
        text_5a[0].set_color(RED)
        text_5b = TextMobject("a este conjunto se le llama la", " imagen inversa ", "de", " $D$").next_to(text_5a,
                                                                                                              DOWN)
        text_5b[1].set_color(RED)
        text_5b[3].set_color(YELLOW)
        text_5 = VGroup(text_5a, text_5b).scale(0.9)

        ### Pasamos al ejemplo
        text_6 = TextMobject("Veamos un ejemplo en $\mathbb{R}^2$").to_edge(UP)
        text_7a = TexMobject(r"f:=[0,1]\times[0,1] \to [0,2]\times[0,2]").to_edge(UP)
        text_7b = TexMobject(r"f(x,y)=(2x,2y)").next_to(text_7a, DOWN)
        text_7 = VGroup(text_7a, text_7b).scale(0.9)

        squareA = Square(side_length=1).set_color(BLUE).move_to((-4.5, -2, 0)).set_fill(BLUE, opacity=0.5)
        squareA_dup = Square(side_length=1, fill_opacity=0).set_color(BLUE).move_to((-4.5, -2, 0))
        squareB = Square(side_length=2).set_color(ORANGE).move_to((3, -1.5, 0)).set_fill(ORANGE, opacity=0.5)

        ### Cuadrante D
        text_8 = TexMobject(r"\text{Si } ", r"D", r"= [1,2]\times[1,2]").shift(4 * RIGHT + 3 * UP).scale(0.9)
        text_8[1].set_color(YELLOW)
        squareD = Square(side_length=1).set_color(YELLOW).move_to((3.5, -1, 0)).set_fill(YELLOW, opacity=0.5)
        squareD_dup = Square(side_length=1, ).set_color(YELLOW).move_to((3.5, -1, 0)).set_fill(YELLOW, opacity=0.0)
        ### Cuadrante f^-1(D)
        text_9 = TexMobject(r"f^{-1}(D)", r"= [0.5,1]\times[0.5,1]").shift(4 * LEFT + 3 * UP).scale(0.9)
        text_9[0].set_color(RED)
        square_finv = Square(side_length=0.5).set_color(RED).move_to((-4.25, -1.75, 0)).set_fill(RED, opacity=0.5)
        finv_D_arrow = Arrow(start=square_finv.get_center(), end=squareD.get_center(), stroke_width=2)

        squares = VGroup(squareA, squareB, squareD, squareD_dup, square_finv, squareA_dup)

        ### Retou
        text_10 = TextMobject("¡Obtén la imagen inversa de los tres cuadrantes restantes!").to_edge(UP)

        ### Secuencia de la animación
        self.play(Write(titulo.scale(1.5)))
        self.wait(3.5)
        self.play(FadeOut(titulo))
        self.play(Write(text_1))
        self.play(ShowCreation(Ejes_1), ShowCreation(Ejes_2), ShowCreation(A_svg_1), ShowCreation(A_svg_2))
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
        self.play(FadeOut(text_5), FadeOut(finv_stuff), FadeOut(D_stuff), FadeOut(A_svg_1),
                  FadeOut(B_svg))
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
        self.play(Write(tedxt_9))
        self.play(ReplacementTransform(squareD_dup, square_finv), FadeOut(f))
        self.wait(5.7)
        self.play(ShowCreation(finv_D_arrow))
        self.play(FadeOut(text_8), text_9.shift, 4 * RIGHT)
        self.wait(2)
        self.play(ReplacementTransform(text_9, text_10))
        self.wait(5.3)
        self.play(FadeOut(squares), FadeOut(text_10), FadeOut(Ejes_1), FadeOut(Ejes_2),
                  FadeOut(finv_D_arrow))