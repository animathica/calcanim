from sys import float_repr_style
from manimlib.imports import *

##########################################################################
############# Campos lineales y Cambios de Coordenadas ###################
#########################################################################
# 15/11/2021
class CamposLineales2(Scene):

    def parte1(self):
        ejes_config = {
            "stroke_width": 3,
            "buff": 0,
            "max_tip_length_to_length_ratio": 0.10,
            "max_stroke_width_to_length_ratio": 2,
            "preserve_tip_size_when_scaling": False,
        }
        titulo = TextMobject('''Campos Lineales y \n
                            Cambios de \n
                            Coordenadas''').scale(2)
        text1 = TextMobject(''' Considera el conjunto''', ''' $\\gamma=\\{(1,1),(0,1)\\}$ ''')
        text1[1].set_color(BLUE_C)
        text2 = TextMobject('''Puedes corroborar que cualquier vector descrito en la  \n
                            base canónica''', '''  $\\beta=\\{(0,1),(1,0) \\}$''', ''', es decir, \n
                            cualquier vector en el plano cartesiano, se puede  \n
                           escribir como una combinación lineal de los vectores en \n
                            el conjunto''', ''' $\\gamma.$ ''').move_to(2.2 * UP)
        text2[1].set_color(YELLOW)
        text2[3].set_color(BLUE_C)

        text3 = TextMobject('''Por ejemplo considera''', ''' $\\vec{w}=(1,2)_\\beta$. ''').move_to(3 * UP)
        text3[1].set_color(PURPLE_C)
        # El índice $\\beta$ indica que el vector está descrito en la base canónica. ''')
        text4 = TextMobject('''En el conjunto ''', '''$\\gamma$,''', ''' $\\vec{w}$ ''', '''se escribe como\n
                             $1\\cdot(1,1)+1\\cdot(0,1) $, por lo cual sus coordenadas \n
                             en el conjunto ''', '''$\\gamma$''', ''' son''', ''' $(1,1)_\\gamma$ ''').move_to(3 * UP)
        text4[1].set_color(BLUE_C)
        text4[2].set_color(PURPLE_C)
        text4[4].set_color(BLUE_C)
        text4[6].set_color(BLUE_C)
        text5 = TextMobject('''En general, podemos escribir cualquier elemento en \n
                             las coordenadas canónicas, a las coordenadas ''', '''$\\gamma$''', ''' \n
                            con la siguiente transformación lineal.''').move_to(1 * UP)
        text5[1].set_color(BLUE_C)
        text5_1 = TexMobject(r'''f((x,y)_\beta)=\begin{bmatrix}
                                1 & 0\\
                                1 & 1
                                \end{bmatrix}\begin{bmatrix}
                                x\\
                                y
                                \end{bmatrix}_\beta=\begin{bmatrix}
                                x' \\
                                y'
                                \end{bmatrix}_\gamma  ''').move_to(text5.get_center() + 2 * DOWN)

        linea1 = Arrow([0, -1, 0], [1, -1, 0], **ejes_config).set_color(YELLOW_C)
        linea2 = Arrow([0, -1, 0], [0, 0, 0], **ejes_config).set_color(YELLOW_C)
        Plano = VGroup(linea1, linea2)

        beta1 = Arrow([0, -1, 0], [1, 1 - 1, 0], **ejes_config).set_color(BLUE_C)
        beta2 = Arrow([0, -1, 0], [0, 1 - 1, 0], **ejes_config).set_color(BLUE_C)
        beta = VGroup(beta1, beta2)
        w = Arrow([0, -1, 0], [1, 2 - 1, 0], buff=0).set_color(PURPLE_C)

        self.play(Write(titulo.scale(1.5)))
        self.wait(4)
        self.play(FadeOut(titulo))
        self.play(Write(text1))
        self.wait(6)
        self.play(text1.shift, 3 * UP, runtime=6)
        self.play(ShowCreation(beta))
        self.play(FadeOut(text1))
        self.play(Write(text2))
        self.wait(2)
        self.play(ShowCreation(Plano))
        self.wait(12)
        self.play(FadeOut(text2), FadeOut(Plano))
        self.play(Write(text3))
        self.play(ShowCreation(w))
        self.wait(5.7)
        self.play(FadeOut(text3))
        self.play(Write(text4))
        # ANIMACIÓN DE LA SUMA DE VECTOR
        self.wait(13.2)
        self.play(FadeOut(text4), FadeOut(w), FadeOut(beta))
        self.play(Write(text5))
        self.wait(8.7)
        self.play(Write(text5_1))
        self.wait(8)
        self.play(FadeOut(text5), FadeOut(text5_1))

    def parte2(self):
        ejes_config = {
            "stroke_width": 3,
            "buff": 0,
            "max_tip_length_to_length_ratio": 0.10,
            "max_stroke_width_to_length_ratio": 2,
            "preserve_tip_size_when_scaling": False,
        }

        text6 = TextMobject('''La función lineal "traduce" los vectores en la base''', ''' \n
                            $\\gamma$''', ''' a vectores en la base ''', '''$\\beta$.''')
        text6[1].set_color(YELLOW)
        text6[3].set_color(BLUE_C)
        text7 = TextMobject('''Más aún, debido a que el determinante de la matriz asociada \n
                                 a la función es diferente de 0, la función posee \n
                                 inversa y es biyectiva. ''')
        text8 = TextMobject('''Entonces la función que nos traduce los vectores \n
                                 descritos con el conjunto ''', '''$\beta$ ''', '''a la \n
                                 base ($\\gamma$)es''').move_to(1 * UP)
        text8[1].set_color(BLUE_C)
        text8_1 = TexMobject(r'''f^{-1} ((x,y)_\beta)=\begin{bmatrix}
                                                    1 & 0\\
                                                    -1 & 1
                                                    \end{bmatrix}\begin{bmatrix}
                                                    x\\
                                                    y
                                                    \end{bmatrix}_\beta=\begin{bmatrix}
                                                    x' \\
                                                    y'
                                                    \end{bmatrix}_\gamma ''').move_to(text8.get_center() + 2 * DOWN)
        text9 = TextMobject('''Como habrás notado, en realidad''', ''' $\\gamma$''', ''' es \n
                            una base del plano cartesiano porque \n
                                a) sus elementos son linealmente independientes y \n
                                b) podemos describir cualquier elemento del \n
                                 plano como una combinación de ambos elementos.
                            ''').move_to(2 * UP)
        text9[1].set_color(BLUE_C)
        text10 = TextMobject('''Así que realmente $f$ es una función que traduce \n
                            elementos de la base ''', '''$\\beta$''', ''' a la base''', ''' $\\gamma$ ''').move_to(
            3 * UP)
        text10[1].set_color(YELLOW)
        text10[3].set_color(BLUE_C)
        text11 = TextMobject('''¿Basta dar una función biyectiva para aseverar\n
                                 que es una función de cambio de coordenadas? ''')

        linea1 = Arrow([0, -1, 0], [1, -1, 0], **ejes_config).set_color(YELLOW_C)
        linea2 = Arrow([0, -1, 0], [0, 0, 0], **ejes_config).set_color(YELLOW_C)
        Plano = VGroup(linea1, linea2).move_to(4 * LEFT + 1 * DOWN).scale(3)

        beta1 = Arrow([4, 1, 0], [5, 2, 0], **ejes_config).set_color(BLUE_C)
        beta2 = Arrow([4, 1, 0], [4, 2, 0], **ejes_config).set_color(BLUE_C)
        beta = VGroup(beta1, beta2).scale(3).move_to(1 * DOWN + 4 * RIGHT)

        beta3 = Arrow([0, 1, 0], [1, 2, 0], **ejes_config).set_color(BLUE_C)
        beta4 = Arrow([0, 1, 0], [0, 2, 0], **ejes_config).set_color(BLUE_C)
        beta_1 = VGroup(beta3, beta4).move_to(2 * DOWN).scale(3)

        flecha = Arrow([-0.5, 0, 0], [0.5, 0, 0], buff=0)

        self.play(Write(text6))
        self.wait(8)
        self.play(FadeOut(text6))
        self.play(Write(text7))
        self.wait(12)
        self.play(FadeOut(text7))
        self.play(Write(text8))
        self.play(Write(text8_1))
        self.wait(16)
        self.play(FadeOut(text8), FadeOut(text8_1))
        self.play(Write(text9))
        self.play(ShowCreation(beta_1))
        self.wait(11)
        self.play(FadeOut(text9))
        self.play(Write(text10))
        self.wait(3)
        self.play(ReplacementTransform(beta_1, beta), ShowCreation(Plano), ShowCreation(flecha))
        self.wait(8.7)
        self.play(FadeOut(text10), FadeOut(flecha), FadeOut(Plano), FadeOut(beta))
        self.play(Write(text11))
        self.wait(7.6)
        self.play(FadeOut(text11))

    def parte3(self):
        ejes_config = {
            "stroke_width": 3,
            "buff": 0,
            "max_tip_length_to_length_ratio": 0.10,
            "max_stroke_width_to_length_ratio": 2,
            "preserve_tip_size_when_scaling": False,
        }
        text12 = TextMobject('''No, los cambios de coordenadas deben preservar \n
                                    la estructura algebraica.''').move_to(1 * UP)
        text12_1 = TextMobject('''Consideremos la suma de dos vectores en las \n
                                  coordenadas ''', '''$\\beta$. ''').next_to(text12, DOWN, buff=1)
        text12_1[1].set_color(YELLOW)
        text13 = TextMobject('''Para transformar este vector a las coordenadas ''', '''$\\gamma$''', ''' \n
                                podemos transformar directamente el vector suma a las \n
                                coordenadas ''', '''$\\gamma$. ''').move_to(3 * UP)
        text13[1].set_color(BLUE_C)
        text13[3].set_color(BLUE_C)
        text14 = TextMobject('''O podemos convertir ambos vectores independientemente y \n
                                realizar la suma de los vectores transformados en la base ''',
                             '''$\\gamma$. ''').move_to(3 * UP)
        text14[1].set_color(BLUE_C)
        text15 = TextMobject('''Lo mismo debe ocurrir si multiplicamos un vector \n
                                 por un escalar y lo convertimos de una base a otra. ''').move_to(3 * UP)

        linea1 = Arrow([-6.5, -1, 0], [-1.5, -1, 0], **ejes_config).set_color(YELLOW_C)
        linea2 = Arrow([-4, -3, 0], [-4, 1, 0], **ejes_config).set_color(YELLOW_C)
        Plano = VGroup(linea1, linea2)

        beta1 = Arrow([1.5, -1 - 0.5, 0], [6.5, -1 + 0.5, 0], **ejes_config).set_color(BLUE_C)
        beta2 = Arrow([4, -1 - 2, 0], [4, -1 + 2, 0], **ejes_config).set_color(BLUE_C)
        beta = VGroup(beta1, beta2)

        # Primer vector
        a = 1.5
        b = 0
        vec_1 = Arrow([-4, -1, 0], [a - 4, b - 1, 0], buff=0).set_color(PURPLE_C)
        vec_1label = TexMobject(r"u_\beta").next_to(vec_1, UP, buff=0.2).set_color(PURPLE_C)
        a2 = 0.5
        b2 = 1
        vec_2 = Arrow([-4, -1, 0], [a2 - 4, -1 + b2, 0], buff=0).set_color(TEAL_D)
        vec_2label = TexMobject(r"v_\beta").next_to(vec_2, UP, buff=0.2).set_color(TEAL_D)
        vectores = VGroup(vec_1, vec_2, vec_2label, vec_1label)
        # Vector suma en beta
        vec_suma = Arrow([-4, -1, 0], [a2 - 4 + a, -1 + b2 + b, 0], buff=0).set_color(GOLD_D)
        vec_sumalabel = TexMobject(r"(u+v)_\beta").next_to(vec_suma, UP, buff=0.2).set_color(GOLD_D)
        suma = VGroup(vec_suma, vec_sumalabel)
        flecha = Arrow([-0.7, 0, 0], [0.7, 0, 0])

        # Suma de vector transformado
        vec_suma_t = Arrow([4, -1, 0], [a2 + 4 + a, -1 + b2 + b, 0], buff=0).set_color(GOLD_D)
        vec_suma_tlabel = TexMobject(r"(u+v)_\gamma").next_to(vec_suma_t, UP, buff=0.2).set_color(GOLD_D)
        vec_suma_tG = VGroup(vec_suma_t, vec_suma_tlabel)
        vec_suma_tlabel2 = TexMobject(r"u_\gamma+v_\gamma").next_to(vec_suma_t, UP, buff=0.2).set_color(GOLD_D)
        vec_suma_tG2 = VGroup(vec_suma_t, vec_suma_tlabel2)
        # Vectores transformados
        vec_1t = Arrow([4, -1, 0], [a + 4, b - 1, 0], buff=0).set_color(PURPLE_C)
        vec_1tlabel = TexMobject(r"u_\gamma").next_to(vec_1t, UP, buff=0.2).set_color(PURPLE_C)
        vec_2t = Arrow([4, -1, 0], [a2 + 4, -1 + b2, 0], buff=0).set_color(TEAL_D)
        vec_2tlabel = TexMobject(r"v_\gamma").next_to(vec_2t, UP, buff=0.2).set_color(TEAL_D)
        vectorest = VGroup(vec_1t, vec_2t, vec_2tlabel, vec_1tlabel)

        # Para la multiplicación por escalar

        c = 0.3
        x = 1
        y = 1.5
        vector_1 = Arrow([-4, -1, 0], [x - 4, y - 1, 0], buff=0).set_color(PURPLE_C)
        vector1_label = TexMobject(r"x_\beta").next_to(vector_1, UP, buff=0.2).set_color(PURPLE_C)
        vector = VGroup(vector_1, vector1_label)

        vector_2 = Arrow([-4, -1, 0], [(x * c - 4), (y * c - 1), 0], buff=0).set_color(PURPLE_C)
        vector2_label = TexMobject(r"(kx)_\beta").next_to(vector_2, UP + RIGHT, buff=0.2).set_color(PURPLE_C)
        vector2 = VGroup(vector_2, vector2_label)

        # vector transformado
        vector_1t = Arrow([4, -1, 0], [x + 4, y - 1, 0], buff=0).set_color(PURPLE_C)
        vector1t_label = TexMobject(r"x_\gamma").next_to(vector_1t, UP + RIGHT, buff=0.2).set_color(PURPLE_C)
        vectort = VGroup(vector_1t, vector1t_label)

        vector_2t = Arrow([4, -1, 0], [(x * c + 4), (y * c - 1), 0], buff=0).set_color(PURPLE_C)
        vector2t_label = TexMobject(r"(kx)_\gamma").next_to(vector_2t, UP + RIGHT, buff=0.2).set_color(PURPLE_C)
        vector2t = VGroup(vector_2t, vector2t_label)
        vector2t_label2 = TexMobject(r"k(x)_\gamma").next_to(vector_2t, UP + RIGHT, buff=0.2).set_color(PURPLE_C)
        vectort_2 = VGroup(vector_2t, vector2t_label2)

        self.play(Write(text12[0]))
        self.wait(5.8)
        self.play(Write(text12_1))
        self.wait(5.8)
        self.play(FadeOut(text12[0]))
        self.play(text12_1.shift, 3.5 * UP, runtime=6)
        self.play(ShowCreation(Plano))
        self.play(ShowCreation(vectores))
        self.wait()
        self.play(FadeOut(text12_1))
        self.play(Write(text13))
        self.wait(5)
        self.play(FadeOut(vectores))
        self.play(ShowCreation(vec_suma), Write(vec_sumalabel))
        self.wait(6)
        self.play(ShowCreation(beta))
        self.wait()
        self.play(ShowCreation(flecha))
        self.wait()
        self.play(ShowCreation(vec_suma_tG))
        self.wait(5)
        self.play(FadeOut(text13))
        self.play(Write(text14), FadeOut(vec_suma_tG), FadeOut(vec_suma), FadeOut(vec_sumalabel), FadeOut(flecha))
        self.wait(8.3)
        self.play(ShowCreation(vectores))
        self.wait()
        self.play(ShowCreation(flecha))
        self.wait()
        self.play(ShowCreation(vectorest))
        self.play(ReplacementTransform(vectorest, vec_suma_tG2), ReplacementTransform(vectores, suma))
        self.wait(7)
        self.play(FadeOut(vec_suma_tG2), FadeOut(suma), FadeOut(flecha), FadeOut(text14))

        self.play(Write(text15))
        self.wait(7)
        self.play(ShowCreation(vector))
        self.wait()
        self.play(ShowCreation(flecha))
        self.wait()
        self.play(ShowCreation(vectort))
        self.wait(2)
        self.play(ReplacementTransform(vector, vector2), ReplacementTransform(vectort, vectort_2))
        self.wait(3)
        self.play(FadeOut(vector2), FadeOut(vectort_2))
        self.play(ShowCreation(vector2))
        self.wait()
        self.play(ShowCreation(flecha))
        self.wait()
        self.play(ShowCreation(vector2t))
        self.wait(5)
        self.play(FadeOut(text15), FadeOut(Plano), FadeOut(beta), FadeOut(vector2), FadeOut(vector2t), FadeOut(flecha))

    def parte4(self):
        ejes_config = {
            "stroke_width": 3,
            "buff": 0,
            "max_tip_length_to_length_ratio": 0.10,
            "max_stroke_width_to_length_ratio": 2,
            "preserve_tip_size_when_scaling": False,
        }
        # Parte del diagrama de conmutación
        text16 = TextMobject(''' Es decir, la función debe ser un isomorfismo.''')
        text17 = TextMobject('''En conclusión, para considerar una función $L$ como un \n
                                 cambio de coordenadas, dicha función debe ser \n
                                 biyectiva y cumplir con el diagrama de conmutatividad. ''')
        diagrama = SVGMobject(
            "Diagrama_conmutatividad.svg", fill_color=WHITE, color=WHITE).move_to(1 * DOWN)
        linea1 = Arrow([-6.5, -1, 0], [-1.5, -1, 0], **ejes_config).set_color(YELLOW_C)
        linea2 = Arrow([-4, -3, 0], [-4, 1, 0], **ejes_config).set_color(YELLOW_C)
        Plano = VGroup(linea1, linea2).scale(0.6).move_to(0 * UP + 2.5 * LEFT)

        linea1_2 = Arrow([-6.5, -1, 0], [-1.5, -1, 0], **ejes_config).set_color(YELLOW_C)
        linea2_2 = Arrow([-4, -3, 0], [-4, 1, 0], **ejes_config).set_color(YELLOW_C)
        Plano_2 = VGroup(linea1_2, linea2_2).scale(0.6).move_to(0 * UP + 2.5 * RIGHT)

        linea1_3 = Arrow([-6.5, -1, 0], [-1.5, -1, 0], **ejes_config).set_color(YELLOW_C)
        linea2_3 = Arrow([-4, -3, 0], [-4, 1, 0], **ejes_config).set_color(YELLOW_C)
        Plano_3 = VGroup(linea1_3, linea2_3).scale(0.6).move_to(-3 * UP + 2.5 * LEFT)

        linea1_4 = Arrow([-6.5, -1, 0], [-1.5, -1, 0], **ejes_config).set_color(YELLOW_C)
        linea2_4 = Arrow([-4, -3, 0], [-4, 1, 0], **ejes_config).set_color(YELLOW_C)
        Plano_4 = VGroup(linea1_4, linea2_4).scale(0.6).move_to(-3 * UP + 2.5 * RIGHT)

        espacio = VGroup(Plano, Plano_2, Plano_3, Plano_4)

        # Vectores

        x = Dot(color=YELLOW).move_to(Plano.get_center() + 0.5 * UP - 0.5 * RIGHT)
        xl = TexMobject(r"\vec{x}_\beta").next_to(x, LEFT)
        y = Dot(color=BLUE_E).move_to(Plano.get_center() + 0.7 * UP + 1 * RIGHT)
        yl = TexMobject(r"\vec{y}_\beta").next_to(y, RIGHT)
        vectores1 = VGroup(x, xl, y, yl)

        x_y = Dot(color=GOLD_C).move_to(Plano_2.get_center() + 1.2 * UP + 0.5 * RIGHT)
        x_yl = TexMobject(r"\vec{x}_\beta+\vec{y}_\beta").next_to(x_y, RIGHT)
        vectores2 = VGroup(x_y, x_yl)

        flecha1 = Arrow([-0.2, 0, 0], [0.2, 0, 0]).scale(2).move_to(0.5 * UP)
        suma = TexMobject(r"+").next_to(flecha1, UP, buff=0.1)
        f1 = VGroup(flecha1, suma)

        flecha2 = Arrow([0, 0.2, 0], [0, -0.2, 0]).scale(2).move_to(4 * RIGHT + 1.5 * DOWN)
        L = TexMobject(r"L").next_to(flecha2, RIGHT, buff=0.1)
        L1 = VGroup(flecha2, L)

        x_yTrans = Dot(color=RED).move_to(Plano_4.get_center() - 0.2 * UP + 0.5 * RIGHT)
        x_yTransl = TexMobject(r"\vec{x}_\gamma+\vec{y}_\gamma").next_to(x_yTrans, DOWN, buff=0.1)
        vectores3 = VGroup(x_yTrans, x_yTransl)

        xt = Dot(color=YELLOW).move_to(Plano_3.get_center() + 0.3 * UP - 0.2 * RIGHT)
        xtl = TexMobject(r"\vec{x}_\gamma").next_to(xt, LEFT)
        yt = Dot(color=BLUE_E).move_to(Plano_3.get_center() + 0.7 * UP - 0.3 * RIGHT)
        ytl = TexMobject(r"\vec{y}_\gamma").next_to(yt, RIGHT)
        vectores4 = VGroup(xt, xtl, yt, ytl)

        flecha3 = Arrow([0, 0.2, 0], [0, -0.2, 0]).scale(2).move_to(4 * LEFT + 1.5 * DOWN)
        L_2 = TexMobject(r"L").next_to(flecha3, LEFT, buff=0.1)
        L2 = VGroup(flecha3, L_2)

        flecha4 = Arrow([-0.2, 0, 0], [0.2, 0, 0]).scale(2).move_to(-3 * UP)
        suma_2 = TexMobject(r"+").next_to(flecha4, UP, buff=0.1)
        f2 = VGroup(flecha4, suma_2)

        DIAGRAMA = VGroup(espacio, vectores1, vectores2, f1, L1, vectores3, vectores4, L2, f2)

        # Para la multiplicación por escalar

        mult1 = TexMobject(r"*").move_to(suma)
        mult2 = TexMobject(r"*").move_to(suma_2)

        c = 2.3
        cx = Dot(color=GOLD_C).move_to(Plano_2.get_center() + (0.5 * (c)) * UP + (-0.5 * (c)) * RIGHT)
        cxl = TexMobject(r"k\vec{x}_\beta").next_to(cx, RIGHT)

        cxt = Dot(color=YELLOW).move_to(Plano_4.get_center() + (0.3 * (c)) * UP - (0.2 * (c)) * RIGHT)
        cxtl = TexMobject(r"k\vec{x}_\gamma").next_to(cxt, LEFT)

        Borrar = VGroup(y, yl, yt, ytl)
        Transformar1 = VGroup(suma, suma_2, vectores3, vectores2)
        Transformar2 = VGroup(mult1, mult2, cx, cxl, cxt, cxtl)
        Borrar2 = VGroup(x, xl, xt, xtl, flecha1, L1, L2, flecha4)
        self.play(Write(text16))
        self.wait(6)
        self.play(FadeOut(text16))
        self.play(Write(text17))
        self.play(text17.shift, 2.5 * UP, runtime=6)
        self.play(ShowCreation(DIAGRAMA))
        self.wait(10)
        self.play(FadeOut(Borrar), ReplacementTransform(Transformar1, Transformar2))
        self.wait(10)
        self.play(FadeOut(text17), FadeOut(Transformar2), FadeOut(espacio), FadeOut(Borrar2))

    def construct(self):
        self.parte1()
        self.parte2()
        self.parte3()
        self.parte4()

