from manimlib.imports import *

###################################
#### DEFINICIÓN DE SUCESIONES #####
###################################
    
class Definicion_Sucesiones(Scene):
    def construct(self):

        ##texto:
        t_1 = TextMobject(''' \\textquestiondown Recuerdas la definici\\'{o}n de sucesiones en $\\mathbb{R}?$ ''')
        t_2 = TextMobject('''Una sucesi\\'{o}n es una funci\\'{o}n de: \n
                            $\\mathbb{N}\\rightarrow\\mathbb{R}$ ''')
        t_3 = TextMobject('''Nota que es distinto hablar del conjunto \n
                            que contiene a todos los \n
                            elementos de dicha sucesi\\'{o}n:\n
                            $\{ x_n \}$, \n
                            donde $x_n = s(n)$ y \n
                            donde $s$ es la funci\\'{o}n.''')
        t_4 = TextMobject(''' \\textexclamdown Bueno! Pues es an\\'{a}logo para \n
                            sucesiones de $\\mathbb{R}^n$. ''')
        t_5 = TextMobject('''Recuerda que un vector en $\\mathbb{R}^n$, \n
                            se ve de la siguiente forma: \n
                            $(x_1,x_2,\\dots,x_n)$, donde $x_i\\in \\mathbb{R}$, \n
                            para cualquier $i\\in \{ 1,\\dots, n \}$''')
        t_6 = TextMobject('''Por lo que para definir una sucesi\\'{o}n \n
                            en $\\mathbb{R}^n$  \n
                            basta definir una sucesi\\'{o}n para \n
                            cada entrada vectorial, es decir: \n
                            $\\vec{s}: \\mathbb{N}\\rightarrow \\mathbb{R}^n$ ''')
        t_7 = TextMobject('''O sea que: \n
                            $\\vec{s}(n) = (s_1(n),s_2(n),\\dots, s_n(n))$ \n
                            Donde $s_i$ es una sucesi\\'{o}n en $\\mathbb{R}$.''')
        t_8 = TextMobject('''Por ejemplo en $\\mathbb{R}^2$, tomemos: \n
                            $\\vec{s}(n) = ((e^{-n})\\cos(n),(e^{-n})\\sin(n))$''')
        t_9 = TextMobject('''Pintemos las parejas de la sucesi\\'{o}n en el plano:''')



        ##mas
        grid = NumberPlane()
        Elementos = [Dot(point=i).set_color(RED_E) for i in cjto_pts_sucesion_1]
        Elementos_Y = [Dot(point=i).set_color(YELLOW_E) for i in cjto_pts_sucesion_1]

        Elementos_t = [TexMobject('\\vec{s}_{%i}' % i).next_to(Elementos[i], 0.08*DOWN).set_color(YELLOW_E) for i in range(0, n_sup_1 - 1)]

        Elementos_g = VGroup(*Elementos)
        Elementos_g_Y = VGroup(*Elementos_Y)
        Elementos_t_g = VGroup(*Elementos_t)



        ##animación:
        self.play(Write(t_1))
        self.wait(2.2)
        self.play(ReplacementTransform(t_1, t_2))
        self.wait(4.3)
        self.play(ReplacementTransform(t_2, t_3))
        self.wait(11.5)
        self.play(ReplacementTransform(t_3, t_4))
        self.wait(6)
        self.play(ReplacementTransform(t_4, t_5))
        self.wait(13)
        self.play(ReplacementTransform(t_5, t_6))
        self.wait(13)
        self.play(ReplacementTransform(t_6, t_7))
        self.wait(10)
        self.play(ReplacementTransform(t_7, t_8))
        self.wait(12)
        self.play(ReplacementTransform(t_8, t_9))
        self.wait(4)
        self.play(ReplacementTransform(t_9, grid))
        self.wait()
        self.play(Write(Elementos_g),
                  Write(Elementos_t_g), run_time=6.35)
        self.wait()
        self.play(FadeOut(Elementos_t_g), ReplacementTransform(Elementos_g, Elementos_g_Y))
        self.wait(3.5)
        self.play(FadeOut(grid),FadeOut(Elementos_g_Y))