from manimlib.imports import *

##Teorema del valor intermedio, sin corregir
class TeoValorIntermedio_1(Scene):
    def construct(self):

        titulo=TextMobject('''Teoremas Fuertes de Continuidad''',''' \n
                        Teorema del Valor Intermedio''').scale(1.5)#.move_to(1*UP)
        text_1_1=TextMobject('''Sea $f:A\\subset\\mathbb{R}^{n}\\rightarrow\\mathbb{R}$ ''','''continua''',''' en A.''').shift(UP*1.8)
        text_1_2 = TextMobject('''Sea A ''','''conexo''',''' y $\\vec{x}_1,\\vec{x}_2\\in A$''').next_to(text_1_1,DOWN)
        text_1_3 = TextMobject(''' tales que $f(\\vec{x}_1)<f(\\vec{x}_2)$.''').next_to(text_1_2,DOWN)
        text_1_4 = TextMobject('''Si $c\\in\\mathbb{R}$ es tal que $f(\\vec{x}_1)<c<f(\\vec{x}_2)$,''').next_to(text_1_3,DOWN)
        text_1_5 = TextMobject('''entonces existe $\\vec{x}$ tal que $f(\\vec{x})=c$ ''').next_to(text_1_4,DOWN)
        text_1_1[1].set_color(PURPLE_B)
        text_1_1[3].set_color(ORANGE)
        text1 = VGroup(text_1_1,text_1_2,text_1_3,text_1_4,text_1_5)
        text_2=TextMobject( "Veamos algunos ejemplos que ilustran este teorema")

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
        self.play(ReplacementTransform(text1,text_2))
        self.wait(4)
        self.play(FadeOut(text_2))


class TeoValorIntermedio_2(GraphScene):
    CONFIG = {
            "x_min" : -2,
            "x_max" : 2,
            "y_min" : -2,
            "y_max" : 2,
            "graph_origin" : ORIGIN + 0.6*DOWN,
            "function_color" : BLUE_C ,
            "x_axis_label": None,
            "y_axis_label": None
            #"axes_color" : YELLOW_C,
            #"x_labeled_nums" :range(-1,1)
 
                }
    def construct(self):
        ### ¡NO MOVER!
        ###############
        self.setup_axes(animate=True)
        func_graph=self.get_graph(self.func_to_graph,self.function_color) 
        #####################
        ################
        #axes=Axes().move_to(2*DOWN)

        
        text1=TextMobject("Sea ","$f(x)=e^{x^{2}}\sin(10x)$").move_to(3.5*UP)
        for i in range(0,4):
            text1[1][i].set_color(BLUE)
        text1.bg  = SurroundingRectangle(text1,color=WHITE,fill_color=BLACK,fill_opacity=0.75)
        text1.group = VGroup(text1.bg,text1)
        text1[1].bg = SurroundingRectangle(text1[1],color=WHITE,fill_color=BLACK,fill_opacity=0.75).shift(6.85*DOWN)
        text1[1].group = VGroup(text1[1].bg,text1[1])
        text2=TextMobject('''Tomemos $\\vec{x}_1=0$ y $\\vec{x}_2=0.8128$''').move_to(3.3*UP)
        text2.bg  = SurroundingRectangle(text2,color=WHITE,fill_color=BLACK,fill_opacity=0.75)
        text2.group = VGroup(text2.bg,text2)
        text2_1=TextMobject('''Además ''','''$f(\\vec{x}_1)$''','''$=0$ y ''','''$f(\\vec{x}_2)$''','''$=1.8764$''').next_to(text2,DOWN).shift(0.1*UP)
        text2_1[1].set_color(RED)
        text2_1[3].set_color(PINK)
        text2_1.group = VGroup(text2,text2_1)
        text2_1.bg = SurroundingRectangle(text2_1.group,color=WHITE,fill_color=BLACK,fill_opacity=0.75)
        text3=TextMobject('''Y escojamos c=1''').move_to(3.5*UP)
        text3[0][10].set_color(ORANGE)
        text3.bg  = SurroundingRectangle(text3,color=WHITE,fill_color=BLACK,fill_opacity=0.75)
        text3.group = VGroup(text3.bg,text3)
        text4=TextMobject('''Podemos apreciar que $\\Vec{x}_0=0.8960$ cumple que\n''',
                             '''$f(\\Vec{x}_0)$''','''$=$''','''$c$''','''$=1$ ''').move_to(3*UP)
        text4[1].set_color(GREEN)
        text4[3].set_color(ORANGE)
        text4.bg  = SurroundingRectangle(text4,color=WHITE,fill_color=BLACK,fill_opacity=0.75)
        text4.group = VGroup(text4.bg,text4)
        text5=TextMobject('''Además si tomamos $A=\\mathbb{R}, \ \\Vec{x}_0,\\Vec{x}_1,\\Vec{x}_2\\in A$.''').move_to(3.3*UP)
        text5.bg  = SurroundingRectangle(text5,color=WHITE,fill_color=BLACK,fill_opacity=0.75)
        text5.group = VGroup(text5.bg,text5)
        text6=TextMobject('''Sin embargo, en A, $\\Vec{x}_0$ no es el único \n
                                elemento que satisface que $f(\\Vec{x})=1$''').move_to(3.3*UP)
        text6.bg  = SurroundingRectangle(text6,color=WHITE,fill_color=BLACK,fill_opacity=0.75)
        text6.group = VGroup(text6.bg,text6)
        text6_1=TextMobject('''También ''','''$f(\\vec{x}'_0)$''','''$=1$''' ).move_to(3*UP)
        text6_1[1].set_color(GREEN)
        text6_1.bg  = SurroundingRectangle(text6_1,color=WHITE,fill_color=BLACK,fill_opacity=0.75)
        text6_1.group = VGroup(text6_1.bg,text6_1)
        text7=TextMobject('''¿Esto contradice el teorema del valor intermedio?''').shift(0.5*UP)
        text7_1=TextMobject('''¡NO! por que el teorema del valor intermedio no nos \n
                             dice que $\\Vec{x}$ es único. '''  ).next_to(text7,DOWN)#.move_to(3*UP)
        text7.group = VGroup(text7,text7_1)
        text8=TextMobject('''Veamos un último ejemplo''')
        
        #Se puede modifica x2,x1,x_p y x_pp para cambiar los puntos que se representan en la función, tambien se puede cambiar c
        x2=0.8012888224891
        fx2=np.exp(x2*x2)*np.sin(10*x2)
        vec_x2 = Dot(color=PINK).move_to((self.coords_to_point(x2,fx2)))#(0.8128+2.47)*RIGHT+(1.8764-0.1)*UP)
        v_x2 = Dot(color=PINK).move_to((self.coords_to_point(x2,0)))#(0.8128+2.47)*RIGHT+(1.8764-0.1)*UP)
        x1=0
        fx1=np.exp(x1*x1)*np.sin(10*x1)
        vec_x1 = Dot(color=RED).move_to(self.coords_to_point(0,fx1))#(0)*RIGHT+(0-1)*UP)
        v_x1 = Dot(color=RED).move_to(self.coords_to_point(0,0))#(0)*RIGHT+(0-1)*UP)
        #v_x1_label = TexMobject(r"\Vec{x}_2").next_to(v_x2,RIGHT,buff=0.2).set_color(RED)
        #v_x2_label = TexMobject(r"\Vec{x}_2").next_to(v_x2,RIGHT,buff=0.2).set_color(PINK)
        vec_x2_label=TexMobject(r"f(\Vec{x}_2)").next_to(vec_x2,RIGHT,buff=0.2).set_color(PINK).shift(0.3*DOWN)
        vec_x1_label=TexMobject(r"f(\Vec{x}_1)").next_to(vec_x1,UP,buff=0.3).set_color(RED).shift(0.6*RIGHT).shift(0.3*DOWN)
        puntos=VGroup(vec_x2,vec_x1,vec_x2_label,vec_x1_label)
        c=Dot(color=ORANGE).move_to(self.coords_to_point(0,1))## se puede cambiar la corrdenada (0,1)
        c_label=TextMobject("c").next_to(c,LEFT,buff=0.1).set_color(ORANGE)
        x_p=0.186#2785740061
        fx_p=np.exp(x_p*x_p)*np.sin(10*x_p)
        vec_x_p=Dot(color=GREEN).move_to(self.coords_to_point(x_p,fx_p))#(0.3528+2.47)*RIGHT+(0.45-0.1)*UP)
        x_pp=0.8961
        label_x_p=TexMobject(r"f(\vec{x}_0)").next_to(vec_x_p,RIGHT,buff=0.1).set_color(GREEN)
        fx_pp=np.exp(x_pp*x_pp)*np.sin(10*x_pp)
        vec_x_pp=Dot(color=GREEN).move_to(self.coords_to_point(x_pp,fx_pp))
        label_x_pp=TexMobject(r"f(\vec{x}'_0)").next_to(vec_x_pp).set_color(GREEN)
        puntos=VGroup(vec_x2,vec_x1,c,vec_x_p,vec_x_pp)
        rec=Rectangle(height=FRAME_HEIGHT,width=FRAME_WIDTH,color=BLACK,fill_color=BLACK, fill_opacity=1)
        
        self.play(Write(text1.group))
        self.add_foreground_mobjects(text1.group)
        self.wait(3)
        self.play(ShowCreation(func_graph), runtime = 1.5)
        self.remove_foreground_mobjects(text1[0])
        self.play(FadeOut(text1.bg),FadeOut(text1[0]),text1[1].shift,6.85*DOWN,runtime=1.5)
        self.play(Write(text1[1].bg))
        self.play(Write(text2.group))
        self.add_foreground_mobjects(text2)
        self.wait(3)
        #self.play(ShowCreation(v_x1))
        #self.play(Write(v_x1_label))
        #self.play(ShowCreation(v_x2))
        #self.play(Write(v_x2_label))
        self.play(ReplacementTransform(text2.bg,text2_1.bg))
        #self.play(FadeOut(v_x1_label),FadeOut(v_x2_label))
        self.add_foreground_mobjects(text2_1.bg,text2_1,text2)
        self.play(Write(text2_1))
        self.play(ShowCreation(vec_x1))
        self.play(Write(vec_x1_label))
        self.play(ShowCreation(vec_x2))
        self.play(Write(vec_x2_label))
        self.wait(5)
        self.remove_foreground_mobjects(text2_1.bg,text2_1,text2)
        self.play(FadeOut(text2_1.group),FadeOut(text2_1.bg))
        self.play(Write(text3.group))
        self.play(ShowCreation(c))
        self.play(Write(c_label))
        self.play(FadeOut(vec_x1_label),FadeOut(vec_x2_label))
        self.wait(3)
        self.play(FadeOut(text3.group))
        self.play(Write(text4.group))
        self.play(ShowCreation(vec_x_p),Write(label_x_p))
        self.play(FadeOut(c_label))
        self.wait(6)
        self.play(ReplacementTransform(text4.group,text5.group))
        self.wait(7)
        self.play(ReplacementTransform(text5.group,text6.group))
        self.play(ShowCreation(vec_x_pp))
        self.wait(7)
        self.play(ReplacementTransform(text6.group,text6_1.group))
        self.play(ShowCreation(vec_x_pp))
        self.wait()
        self.play(Write(label_x_pp))
        self.play(FadeOut(label_x_p))
        self.wait(3)
        self.remove_foreground_mobjects(text1[1])
        self.play(FadeOut(text6.group),FadeOut(text1[1].group),FadeOut(puntos))
        self.play(FadeOut(func_graph))
        self.play(GrowFromCenter(rec))
        self.play(Write(text7))
        self.wait(4)
        self.play(Write(text7_1))
        self.wait(7)
        self.play(ReplacementTransform(text7.group,text8))
        self.wait(2)
        self.play(FadeOut(text8))


    def func_to_graph(self,x):
        return np.exp(x*x)*np.sin(10*x)


class sup(ParametricSurface):

    def __init__(self, **kwargs):
        kwargs = {
        "u_min": -3,
        "u_max": 3,
        "v_min": -3,
        "v_max": 3,
        "checkerboard_colors": [BLUE_C]
        }
        ParametricSurface.__init__(self, self.func, **kwargs)

    def func(self, x, y):
        return np.array([x,y,x**2+y**2-2])


class TeoValorIntermedio_3 (ThreeDScene):
    CONFIG = {
        "x_axis_label": "$x$",
        "y_axis_label": "$y$"
    }
    def construct(self):

        text2=TextMobject('''Sea $f(x,y)=x^{2}+y^{2}-2$''')
        for i in range(3,9):
            text2[0][i].set_color(BLUE)
        text2_copy = text2.copy()
        text2_copy.to_edge(DOWN)
        text2.bg = SurroundingRectangle(text2_copy,color=WHITE,fill_color=BLACK,fill_opacity=1)
        text2.group = VGroup(text2.bg,text2_copy)
        #text3_0=TextMobject('''Y sea $\\Vec{x}_1=(0,0),\\Vec{x}_2=(2,0)$''').to_edge(DOWN)
        #text3_0.bg = SurroundingRectangle(text3_0,color=WHITE,fill_color=BLACK,fill_opacity=1)
        #text3_0.group = VGroup(text3_0.bg,text3_0)
        #text3_0[0][4].set_color(PURPLE_B)
        #text3_0[0][5].set_color(PURPLE_B)
        #text3_0[0][6].set_color(PURPLE_B)
        #text3_0[0][14].set_color(RED)
        #text3_0[0][15].set_color(RED)
        #text3_0[0][16].set_color(RED)
        text3=TextMobject('''Y sea $\\Vec{x}_1=(0,0),\\Vec{x}_2=(2,0)$''',''' y $c=5$''').to_edge(DOWN)
        text3.bg = SurroundingRectangle(text3,color=WHITE,fill_color=BLACK,fill_opacity=1)
        text3.group = VGroup(text3.bg,text3)
        text3[0][4].set_color(PURPLE_B)
        text3[0][5].set_color(PURPLE_B)
        text3[0][6].set_color(PURPLE_B)
        text3[0][14].set_color(RED)
        text3[0][15].set_color(RED)
        text3[0][16].set_color(RED)
        text4=TextMobject('''Se puede comprobar que ''','''$f(\\Vec{x}_1)$''','''$<0<$''','''$f(\\Vec{x}_2)$''')
        text4.to_edge(DOWN)
        text4.bg = SurroundingRectangle(text4,color=WHITE,fill_color=BLACK,fill_opacity=1)
        text4.group = VGroup(text4.bg,text4)
        text4[1].set_color(PURPLE_B)
        text4[3].set_color(RED)
        text5=TextMobject('''Si tomamos $\\vec{x}=(x,y)$ tal que $||\\vec{x}||^{2}=2$, \\\\''','''se cumple que $f(\\vec{x})=0$.''')
        text5.to_edge(DOWN)
        text5.bg = SurroundingRectangle(text5,color=WHITE,fill_color=BLACK,fill_opacity=1)
        text5.group = VGroup(text5.bg,text5)
        text6=TextMobject('''Si tomamos $\\vec{x}$ tal que $||\\vec{x}||=2$ \n''',
                            '''se cumple que $f(\\vec{x})$=0''')
        text6.to_edge(DOWN)
        text6.bg = SurroundingRectangle(text6,color=WHITE,fill_color=BLACK,fill_opacity=1)
        text6.group = VGroup(text6.bg,text6)
        text6_1=TextMobject('''Por lo cual se cumple el teorema del valor intermedio.''')
        text6_1.to_edge(DOWN)
        text6_1.bg = SurroundingRectangle(text6_1,color=WHITE,fill_color=BLACK,fill_opacity=1)
        text6_1.group = VGroup(text6_1.bg,text6_1)
        text7 = TextMobject('''Como $f$ es continua en un conexo y tiene cambio de signo, \\\\''',
                            '''por el teorema del valor intermedio, \\\\''',
                            '''$f$ tiene raíces en el dominio.''').to_edge(DOWN)
        text7.bg = SurroundingRectangle(text7,color=WHITE,fill_color=BLACK,fill_opacity=1)
        text7.group = VGroup(text7.bg,text7)


        superficie=sup(color=BLUE_C,fill_opacity=0.5)
        axes = ThreeDAxes()
        axes.add(axes.get_axis_labels())
        axes.axis_labels[0].rotate(PI/2,axis=RIGHT)
        axes.axis_labels[1].rotate(PI/2,axis=RIGHT)
        #axes
        #Se puede cambiar x1,x1,x2,y2 para cambiar lospuntos referentes al valor extremo
        x1=0
        y1=0
        f_1=Dot(color=PURPLE_C).move_to([x1,y1,0])
        #xf_1=Dot(color=PURPLE_B).move_to([x1,y1,x1**2+y1**2-2]).set_color(PURPLE_C)
        f_1_label=TexMobject(r"\vec{x}_1").rotate(PI/2,axis=RIGHT).move_to(f_1.get_center()+0.2*UP+0.4*RIGHT).set_color(PURPLE_C).scale(1.5)
        x2=2
        y2=0
        f_2=Dot(color=RED).move_to([x2,y2,0])
        #xf_2=Dot(color=RED).move_to([x2,y2,x2**2+y2**2-2]).set_color(RED)
        f_2_label=TexMobject(r"\vec{x}_2").rotate(PI/2,axis=RIGHT).move_to(f_2.get_center()+0.2*UP+0.4*RIGHT).set_color(RED).scale(1.5)
        #Tambien se puede cambiar el radio de la bola y su posición
        bola=Circle(radius=(2**(1/2)),color=ORANGE).move_to([0,0,0])
        #G1=VGroup(f_1,f_1_label,f_2,f_2_label)
        dots1 = VGroup(f_1,f_2,f_1_label,f_2_label)
        xf_1=Dot(color=PURPLE_B).move_to([x1,y1,x1**2+y1**2-2]).set_color(PURPLE_C)
        xf_2=Dot(color=RED).move_to([x2,y2,x2**2+y2**2-2]).set_color(RED)
        xf_1_label=TexMobject(r"f(\vec{x}_1)").rotate(PI/2,axis=RIGHT).move_to(xf_1.get_center()+1*RIGHT).set_color(PURPLE_C).scale(1.5)
        xf_2_label=TexMobject(r"f(\vec{x}_2 ) ").rotate(PI/2,axis=RIGHT).move_to(xf_2.get_center()+1*RIGHT ).set_color(RED).scale(1.5)
        dots2 = VGroup(xf_1,xf_2,xf_1_label,xf_2_label)

        # Def dot radius = 0.08

        #self.set_camera_orientation(0.8*np.pi/2, -0.25*np.pi,distance=20)         
        self.set_camera_orientation(phi=0.8*np.pi/2, theta=1.75*np.pi, distance=20)  
        self.add_fixed_in_frame_mobjects(text2)
        self.play(Write(text2))
        self.wait(4)
        self.play(ReplacementTransform(text2,text2_copy))
        self.add_foreground_mobject(text2_copy)
        self.add_fixed_in_frame_mobjects(text2_copy,text2.bg)
        self.play(Write(text2.bg))
        #self.wait(4)
        self.play(ShowCreation(axes))
        self.play(ShowCreation(superficie),fill_opacity=0.5)
        self.remove_foreground_mobject(text2_copy)
        self.play(FadeOut(text2.group))
        self.add_foreground_mobject(text3[0])
        self.add_fixed_in_frame_mobjects(text3.bg,text3[0])
        self.play(Write(text3.bg),Write(text3[0]))
        self.play(ShowCreation(f_1),Write(f_1_label))
        self.play(Write(f_2_label),ShowCreation(f_2))
        self.wait(5)
        #self.remove_foreground_mobject(text3_0)
        self.add_fixed_in_frame_mobjects(text3[1],text3.bg)
        #self.play(ReplacementTransform(text3_0.group,text3.group))
        self.add_foreground_mobject(text3[1])
        self.play(Write(text3[1]))
        #self.add_foreground_mobject(text3)
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
        self.add_fixed_in_frame_mobjects(text5[0],text5.bg)
        self.add_foreground_mobject(text5[0])
        self.play(Write(text5.bg),Write(text5[0]))
        self.wait(6.6)
        #self.play(FadeOut(text5))
        self.add_foreground_mobject(text5[1])
        self.add_fixed_in_frame_mobjects(text5[1])
        self.play(Write(text5[1]))
        self.play(ShowCreation(bola))
        self.wait(4.5)
        self.remove_foreground_mobject(text5)
        self.play(FadeOut(text5.group))
        self.add_fixed_in_frame_mobjects(text6_1,text6_1.bg)
        self.add_foreground_mobject(text6_1)
        self.play(Write(text6_1.bg),Write(text6_1))
        self.wait(4.5)
        self.remove_foreground_mobject(text6_1)
        self.play(FadeOut(text6_1.group))
        self.add_fixed_in_frame_mobjects(text7.bg,text7[0])
        self.play(Write(text7.bg),Write(text7[0]))
        self.wait(5.5)
        self.add_fixed_in_frame_mobjects(text7[1])
        self.play(Write(text7[1]))
        self.wait(3)
        self.add_fixed_in_frame_mobjects(text7[2])
        self.play(Write(text7[2]))
        self.wait(3)
        self.play(FadeOut(text7.group),FadeOut(superficie),FadeOut(axes),FadeOut(dots2),FadeOut(bola))