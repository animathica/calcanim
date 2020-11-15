from manimlib.imports import *

###Superficies para la clase TeoValorMedio


class TeoValorMedio_1(Scene):
    def construct(self):

        titulo=TextMobject('''Teoremas fuertes de continuidad''',''' \n
                        Teorema del valor medio''').scale(1.5)#.move_to(1*UP)
        text_1=TextMobject('''Sea $f:A\\subset\\mathbb{R}^{n}\\rightarrow\\mathbb{R}$ continua en A.''','''\n
                                Sea $B\\subset A$ conexo y $\\vec{x}_1,\\vec{x}_2\\in B$ ''','''\n
                                tales que $f(\\vec{x}_1)<f(\\vec{x}_2)$.''','''\n
                                Si $c\\in\\mathbb{R}$ es tal que $f(\\vec{x}_1)<c<f(\\vec{x}_2)$,''','''\n
                                 entonces existe $\\vec{x}$ tal que $f(\\vec{x})=c$ ''')               
        text_2=TextMobject( "Veamos algunos ejemplos que ilustren este teorema")

        self.play(Write(titulo[0]))
        self.wait(4)
        self.play(Write(titulo[1]))
        self.wait(4)
        self.play(FadeOut(titulo))
        self.play(Write(text_1[0]))
        self.wait(4)
        self.play(Write(text_1[1]))
        self.wait(5)
        self.play(Write(text_1[2]))
        self.wait(4)
        self.play(Write(text_1[3]))
        self.wait(6)
        self.play(Write(text_1[4]))
        self.wait(4)
        self.play(ReplacementTransform(text_1,text_2))
        self.wait(4)
        self.play(FadeOut(text_2))

class TeoValorIntermedio_2(GraphScene):
    CONFIG = {
            "x_min" : -2,
            "x_max" : 2,
            "y_min" : -2,
            "y_max" : 2,
            "graph_origin" : ORIGIN +1*DOWN,
            "function_color" : BLUE_C ,
            "axes_color" : YELLOW_C,
            "x_labeled_nums" :range(-1,1,1),
 
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
        text2=TextMobject('''Tomemos $\\vec{x}_1=0$ y $\\vec{x}_2=0.8128$''',''' \n
                            Además $f(\\vec{x}_1)=0$ y $f(\\vec{x}_2)=1.8764$.''').move_to(3.3*UP)
        text3=TextMobject('''Y escojamos c=1''').move_to(3.5*UP)
        text4=TextMobject('''Podemos apreciar que $\\Vec{x}=0.8960$ cumple que\n
                             $f(\\Vec{x})=c=1$ ''').move_to(3*UP)
        text5=TextMobject('''Además si tomamos $B=[0,1], \ \\Vec{x},\\Vec{x}_1,\\Vec{x}_2\\in B$. \n
                    Por lo cual se comple el teorema del valor medio.''').move_to(3.3*UP)
        text6=TextMobject('''Sin embargo en B, $\\Vec{x}$, no es el único \n
                                elemento que satisface que $f(\\Vec{x})=1$''').move_to(3.3*UP)
        text6_1=TextMobject('''También $f(\\vec{x}')=1$''' ).move_to(3*UP)
        text7=TextMobject('''¿Esto contradice el teorema del valor intermedio?''','''\n
                             ¡NO! por que el teorema del valor medio no nos \n
                             dice que $\\Vec{x}$ es único. '''  )#.move_to(3*UP)
        text8=TextMobject('''Veamos un último ejemplo''')
        
        #Se puede modifica x2,x1,x_p y x_pp para cambiar los puntos que se representan en la función, tambien se puede cambiar c
        x2=0.8012888224891
        fx2=np.exp(x2*x2)*np.sin(10*x2)
        vec_x2 = Dot(color=RED).move_to((self.coords_to_point(x2,fx2)))#(0.8128+2.47)*RIGHT+(1.8764-0.1)*UP)
        x1=0
        fx1=np.exp(x1*x1)*np.sin(10*x1)
        vec_x1 = Dot(color=RED).move_to(self.coords_to_point(0,fx1))#(0)*RIGHT+(0-1)*UP)
        vec_x2_label=TexMobject(r"f(\Vec{x}_2)").next_to(vec_x2,RIGHT,buff=0.2)
        vec_x1_label=TexMobject(r"f(\Vec{x}_1)").next_to(vec_x1,UP,buff=0.3)
        puntos=VGroup(vec_x2,vec_x1,vec_x2_label,vec_x1_label)
        c=Dot(color=ORANGE).move_to(self.coords_to_point(0,1))## se puede cambiar la corrdenada (0,1)
        c_label=TextMobject("c").next_to(c,LEFT,buff=0.1)
        x_p=0.186#2785740061
        fx_p=np.exp(x_p*x_p)*np.sin(10*x_p)
        vec_x_p=Dot(color=GREEN).move_to(self.coords_to_point(x_p,fx_p))#(0.3528+2.47)*RIGHT+(0.45-0.1)*UP)
        x_pp=0.89
        label_x_p=TexMobject(r"f(\vec{x})").next_to(vec_x_p,RIGHT,buff=0.1)
        fx_pp=np.exp(x_pp*x_pp)*np.sin(10*x_pp)
        vec_x_pp=Dot(color=GREEN).move_to(self.coords_to_point(x_pp,fx_pp))
        label_x_pp=TexMobject(r"f(\vec{x}')").next_to(vec_x_pp)
        puntos=VGroup(vec_x2,vec_x1,vec_x2_label,vec_x1_label,c,vec_x_p,c_label,vec_x_pp,label_x_pp)
        rec=Rectangle(height=FRAME_HEIGHT,width=FRAME_WIDTH,color=BLACK,fill_color=BLACK, fill_opacity=1)
        
        self.play(Write(text1))
        self.wait(3)
        self.play(ShowCreation(func_graph))
        self.play(FadeOut(text1[0]),text1[1].shift,7*DOWN,runtime=1.5)
        self.play(Write(text2[0]))
        self.wait(3)
        self.play(ShowCreation(vec_x1))
        self.play(Write(vec_x1_label))
        self.play(ShowCreation(vec_x2))
        self.play(Write(vec_x2_label))
        self.play(Write(text2[1]))
        self.wait(5)
        self.play(FadeOut(text2))
        self.play(Write(text3))
        self.play(ShowCreation(c))
        self.play(Write(c_label))
        self.wait(3)
        self.play(FadeOut(text3))
        self.play(Write(text4))
        self.play(ShowCreation(vec_x_p),Write(label_x_p))
        self.wait(6)
        self.play(ReplacementTransform(text4,text5))
        self.wait(7)
        self.play(FadeOut(label_x_p))
        self.play(ReplacementTransform(text5,text6))
        #self.play(ShowCreation(vec_x_pp))
        self.wait(7)
        self.play(ReplacementTransform(text6,text6_1))
        self.play(ShowCreation(vec_x_pp))
        self.play(ReplacementTransform(label_x_p,label_x_pp))
        self.wait(3)
        self.play(FadeOut(text6_1),FadeOut(text1[1]),FadeOut(puntos))
        self.play(FadeOut(func_graph))
        self.play(GrowFromCenter(rec))
        self.play(Write(text7[0]))
        self.wait(4)
        self.play(Write(text7[1]))
        self.wait(7)
        self.play(ReplacementTransform(text7,text8))
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

class TeoValorMedio_3 (ThreeDScene):
    def construct(self):
        text2=TextMobject('''Sea $f(x,y)=x^{2}+y^{2}-2$''').move_to(3*UP)
        text2.to_corner(DL)
        text3=TextMobject('''Y sea $\\Vec{x}_1=(0,0),\\Vec{x}_2=(2,0)$\n''',
                                    '''y c=0''')
        text3.to_corner(DL)
        text4=TextMobject('''Se puede comprobar que $f(\\Vec{x}_1)<0<f(\\Vec{x}_2)$''')
        text4.to_corner(DL)
        text5=TextMobject('''Si tomamos $\\vec{x}=(x,y)$ tal que $||\\vec{x}||^{2}=2$ \n
                        Se cumple que $f(\\vec{x})=0$''')
        text5.to_corner(DL)
        text6=TextMobject('''Si tomamos $\\vec{x}$ tal que $||\\vec{x}||=2$ \n''',
                            '''se cumple que $f(\\vec{x})$=0''')
        text6.to_corner(DL)
        text6_1=TextMobject('''Por lo cual se cumple el teorema del valor intermedio.''')
        text6_1.to_corner(DL)

        superficie=sup(color=BLUE_C,fill_opacity=0.5)
        axes = ThreeDAxes()
        #Se puede cambiar x1,x1,x2,y2 para cambiar lospuntos referentes al valor extremo
        x1=0
        y1=-0
        f_1=Dot(color=PURPLE_C).move_to([x1,y1,x1**2+y1**2-2])
        f_1_label=TexMobject(r"\vec{x}_1").rotate(PI/2,axis=RIGHT).move_to(f_1.get_center()+0.4*DOWN).set_color(PURPLE_C).scale(1.5)
        x2=2
        y2=0
        f_2=Dot(color=RED).move_to([x2,y2,x2**2+y2**2-2])
        f_2_label=TexMobject(r"\vec{x}_2").rotate(PI/2,axis=RIGHT).move_to(f_2.get_center()+0.4*RIGHT ).set_color(RED).scale(1.5)
        #Tambien se puede cambiar el radio de la bola y su posición
        bola=Circle(radius=(2**(1/2)),color=RED).move_to([0,0,0])
        G1=VGroup(f_1,f_1_label,f_2,f_2_label)


        self.set_camera_orientation(0.8*np.pi/2, -0.25*np.pi,distance=20)           
        self.add_fixed_in_frame_mobjects(text2)
        self.play(Write(text2))
        self.wait(4)
        self.play(ShowCreation(axes))
        self.play(ShowCreation(superficie),fill_opacity=0.5)
        self.play(FadeOut(text2))
        self.add_fixed_in_frame_mobjects(text3[0])
        self.play(Write(text3[0]))
        self.play(ShowCreation(f_1),Write(f_1_label))
        self.play(Write(f_2_label),ShowCreation(f_2))
        self.wait(5)
        self.add_fixed_in_frame_mobjects(text3[1])
        self.play(Write(text3[1]))
        self.wait(3)
        self.play(FadeOut(text3))
        self.add_fixed_in_frame_mobjects(text4)
        self.play(Write(text4))
        self.wait()
        self.play(FadeOut(text4))
        self.add_fixed_in_frame_mobjects(text5)
        self.play(Write(text5))
        self.wait()
        self.play(FadeOut(text5))
        self.add_fixed_in_frame_mobjects(text6)
        self.play(Write(text6))
        self.wait()
        self.play(ShowCreation(bola))
        self.play(FadeOut(text6))
        self.add_fixed_in_frame_mobjects(text6_1)
        self.play(Write(text6_1))
        self.wait(3)
        self.play(FadeOut(text6_1),FadeOut(superficie),FadeOut(axes),FadeOut(G1),FadeOut(bola))
