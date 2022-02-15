from manimlib.imports import *

#############################################################
############## Planos y su inclinación #####################
###########################################################
#anexado el 11/11/2021


class Planos(ThreeDScene):

    def l_1(self, t):
        return np.array([t, 0,5*t])
    def l_2(self, t):
        return np.array([0,t,3*t])
    def Plano(self,x,y):
        return np.array([x,y,5*x+ 3*y])


    def construct(self):

        ###Texto
        titulo = TextMobject('''Planos y Su Inclinación''').scale(1.5)
        t_1 = TextMobject('''En $\\mathbb{R}^3$ un plano puede ser descrito como \n
        una superficie lisa, sin subidas ni bajadas. ''')
        t_2 = TextMobject('''Algunos planos son gráficas de funciones de $\\mathbb{R}^2$ en $\\mathbb{R},$ \n
                            $ f(x,y) = ax + by  \\mbox{ con } a,b \\in \\mathbb{R}.$''')
        t_3 = TextMobject('''Cualquier plano no vertical intersecta  \n
        a los planos $xz$ y $yz$ en dos rectas, \n
        cada una en los planos respectivos \n
        son de pendiente $a$ y $b$.''')
        t_4 = TextMobject('''Veamos a que nos referimos con esto gráficamente.''')
        t_5 = TextMobject('''Tomemos una recta ''', '''$\\mathcal{L}_1$''', ''' en el plano $xz$ de pediente 5. ''').to_edge(UP)
        t_5.set_color_by_tex_to_color_map({'''$\\mathcal{L}_1$''': TEAL})
        t_5_bg = SurroundingRectangle(t_5, color=WHITE, fill_color=BLACK, fill_opacity=1)
        t_6 = TextMobject('''Y otra recta ''','''$\\mathcal{L}_2$''', ''' en el plano $yz$ de pendiente 3.''').to_edge(UP)
        t_6.set_color_by_tex_to_color_map({'''$\\mathcal{L}_2$''': RED})
        t_6_bg = SurroundingRectangle(t_6, color=WHITE, fill_color=BLACK, fill_opacity=1)
        t_7 = TextMobject('''Ahora observemos que el plano \n
        $f(x,y) = 5x + 3x$ \n
        contiene a ambas rectas.''').to_edge(UP)
        t_7_bg = SurroundingRectangle(t_7, color=WHITE, fill_color=BLACK, fill_opacity=1)
        t_8 = TextMobject('''Este plano es el único que contiene ambas rectas y \n
        por lo tanto este plano queda totalmente \n
        caracterizado por estas.''').to_edge(UP)
        t_8_bg = SurroundingRectangle(t_8, color=WHITE, fill_color=BLACK, fill_opacity=1)
        t_9 = TextMobject(''' En particular la inclinación del plano queda determinada por el \n
        vector ''','''$(5,3)$''',''', es decir por la inclinación de las rectas. ''').to_edge(UP)
        t_9_bg = SurroundingRectangle(t_9, color=WHITE, fill_color=BLACK, fill_opacity=1)
        t_9.set_color_by_tex_to_color_map({'''$(5,3)$''': GREEN})
        t_10 = TextMobject('''Se puede demostrar que $f:\\mathbb{R}^2\\rightarrow\\mathbb{R}$ es lineal \n
        si y sólo si $f(x,y)=ax+by=(a,b)\\cdot (x,y)$. ''')
        t_11 = TextMobject('''Las gráficas de estas funciones corresponden a todos los \n
        planos no verticales en $\\mathbb{R}^3$ que pasan por el origen.''')
        t_12 = TextMobject('''¿Qué pasa con los planos que no pasan por el origen?''')
        t_13 = TextMobject('''¿Cómo aplica este concepto de inclinación \n
         para el caso de un plano tangente?''')







        ### Objetos

        axes = ThreeDAxes(x_min = -4, x_max = 4, y_min = -4, y_max=4, z_min=-4, z_max=4 ,num_axis_pieces= 4)
        recta_1 = ParametricFunction(self.l_1, color=TEAL, t_min= -2,t_max=2)
        recta_2 = ParametricFunction(self.l_2, color=RED, t_min=-2,t_max=2)
        plano = ParametricSurface(self.Plano, fill_color=PURPLE_E, checkerboard_colors= [PURPLE_D, PURPLE_E], fill_opacity=0.6 ,u_min=-2, u_max =2,v_min=-2, v_max=2)
        inclinacion=Vector(direction=[5,3,0], color=GREEN)




        ###Grupos

        Group_1 = VGroup(recta_1)
        Group_2 = VGroup(recta_2)
        Group_3 = VGroup(plano)



        ### Animaciones
        self.begin_ambient_camera_rotation(rate=0.2)
        self.add_fixed_in_frame_mobjects(titulo)
        self.play(Write(titulo))
        self.wait(5)
        self.play(FadeOut(titulo))
        self.add_fixed_in_frame_mobjects(t_1)
        self.play(Write(t_1))
        self.wait(12)
        self.play(FadeOut(t_1))
        self.add_fixed_in_frame_mobjects(t_2)
        self.play(Write(t_2))
        self.wait(10)
        self.play(FadeOut(t_2))
        self.add_fixed_in_frame_mobjects(t_3)
        self.play(Write(t_3))
        self.wait(15)
        self.play(FadeOut(t_3))
        self.add_fixed_in_frame_mobjects(t_4)
        self.play(Write(t_4))
        self.wait(8)
        self.play(FadeOut(t_4))
        self.set_camera_orientation(phi=45*DEGREES,theta=55*DEGREES)
        self.play(LaggedStart(ShowCreation(axes)))
        self.add_fixed_in_frame_mobjects(t_5_bg, t_5)
        self.play(Write(t_5_bg), Write(t_5))
        self.play(LaggedStart(ShowCreation(Group_1)))
        self.wait(8)
        self.play(FadeOut(t_5), FadeOut(t_5_bg))
        self.wait(3)
        self.add_fixed_in_frame_mobjects(t_6_bg, t_6)
        self.play(Write(t_6_bg), Write(t_6))
        self.play(LaggedStart(ShowCreation(Group_2)))
        self.wait(8)
        self.play(FadeOut(t_6), FadeOut(t_6_bg))
        self.wait(2)
        self.add_fixed_in_frame_mobjects(t_7_bg, t_7)
        self.play(Write(t_7_bg), Write(t_7))
        self.play(LaggedStart(ShowCreation(Group_3)))
        self.wait(15)
        self.play(FadeOut(t_7), FadeOut(t_7_bg))
        self.wait(5)
        self.add_fixed_in_frame_mobjects(t_8_bg, t_8)
        self.play(Write(t_8_bg), Write(t_8))
        self.wait(18)
        self.play(FadeOut(t_8), FadeOut(t_8_bg))
        self.add_fixed_in_frame_mobjects(t_9_bg, t_9)
        self.play(Write(t_9_bg), Write(t_9))
        self.play(FadeIn(inclinacion))
        self.wait(18)
        self.play(FadeOut(t_9), FadeOut(t_9_bg))
        self.play(FadeOut(Group_1), FadeOut(Group_2), FadeOut(Group_3), FadeOut(axes), FadeOut(inclinacion))
        self.add_fixed_in_frame_mobjects(t_10)
        self.play(Write(t_10))
        self.wait(10)
        self.play(FadeOut(t_10))
        self.add_fixed_in_frame_mobjects(t_11)
        self.play(Write(t_11))
        self.wait(10)
        self.play(FadeOut(t_11))
        self.add_fixed_in_frame_mobjects(t_12)
        self.play(Write(t_12))
        self.wait(8)
        self.play(FadeOut(t_12))
        self.add_fixed_in_frame_mobjects(t_13)
        self.play(Write(t_13))
        self.wait(10)
        self.play(FadeOut(t_13))
