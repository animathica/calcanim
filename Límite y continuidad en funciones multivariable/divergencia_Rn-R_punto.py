from manimlib.imports import *

class ThreeDSurface(ParametricSurface):

    def __init__(self, **kwargs):
        kwargs = {
        "u_min": 0.1,
        "u_max": 5,
        "v_min": 0.1,
        "v_max": 5,
        #"checkerboard_colors": [BLUE_D]
        #"fill_color": BLUE_D,
        "fill_opacity": 1.0,
        #"checkerboard_colors": [BLUE_D, RED_E]
       
       # "should_make_jagged": True
        }
        ParametricSurface.__init__(self, self.func, **kwargs)

    def func(self, x, y):
        return np.array([x,y,(1/(x+y))])

class LimitesR2_a_R_1 (ThreeDScene):
    def construct(self):
        titulo=TextMobject('''Divergencia a Infinito de Funciones de\n
                                $\\mathbb{R}^{n}\\rightarrow\\mathbb{R}$\n
                                en un Punto $a$''').scale(1.5)
        text=TextMobject(''' En el caso de funciones de:\n
                            $\\mathbb{R}^{n}\\rightarrow\\mathbb{R},$''')
        text_1=TextMobject('''donde $n\\in\\lbrace 1,2,3...\\rbrace$''').move_to(text.get_center()+1*DOWN)
        G1=VGroup(text,text_1)
        Def=TextMobject('''Sea una función $f:D\\subseteq\\mathbb{R}^{n}\\rightarrow\\mathbb{R}$''').shift(1.5*UP)
        Def1=TextMobject('''Y sea $\\vec{a}\\in D$''').shift(0.6*UP)
        Def2=TexMobject(r''' \lim_{x \to \vec{a}}f(\vec{x})=\infty\iff\forall M\in\mathbb{R}''').shift(0.5*DOWN)
        #En el video la definción dice limite al infinito, pero ya lo corregí para que sea el limite cuando x tiende a a
        Def3=TextMobject('''$\\exists \\ \\delta>0$ tal que si $\\vec{x}\\in \\left( B_{\\delta}(\\vec{a})\\setminus\\vec{a}\\right) \\cap
                                D\\implies f(\\vec{x})>M$''').shift(1.5*DOWN)
        text_2=TextMobject('''Veamos el siguiente ejemplo''')
        text1=TexMobject(r"f:D\subset\mathbb{R}^2\rightarrow\mathbb{R}").shift(2.5*UP)
        text1_1=TexMobject(r"D=\lbrace (x,y)|x,y\in\mathbb{R}^{+}-\lbrace 0 \rbrace \rbrace").shift(1.25*UP)
        text2=TexMobject(r"f(x,y)=\frac{1}{x+y}").shift(-.1*UP)
        text3=TextMobject('''Veamos el límite cuando:''').shift(-1*UP)
        text4=TextMobject("(x,y)$\\rightarrow\\vec{0}=(0,0)$").shift(-1.8*UP)
        
        
        #ANIMACION
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
        self.wait(19)
        self.play(FadeOut(Def),FadeOut(Def1),FadeOut(Def2),FadeOut(Def3))
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
        self.wait(16)
        self.play(FadeOut(text4),FadeOut(text3),FadeOut(text2),FadeOut(text1_1),
                    FadeOut(text1))
        self.wait()
        self.custom_method()
  
    def custom_method (self):
        axes = ThreeDAxes()
        surface = ThreeDSurface()
        text4=TextMobject('''Tomemos  M=1''')
        M=TextMobject("M").move_to(1*UP+0.3*LEFT)
        text4.to_corner(UL)
        text5=TextMobject('''Si tomamos''',''' $\\delta=0.5$''')
        text5[1].set_color("#88FF00")
        text5.to_corner(UL)
        text6=TextMobject('''La imagen de los puntos en D  \n
                            y la bola son mayores a 1''')
        text6.to_corner(UL)
        text7=TextMobject('''Es posible verificar lo anterior \n
                            a través de operaciones\n
                            algebraicas.''')
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

        #ANIMACION
        self.set_camera_orientation(0.8*np.pi/2, -0.25*np.pi,distance=4)           
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
        self.play(ShowCreation(linea),Write(text5_1))
        self.wait()
        self.play(FadeOut(text5))
        self.play(FadeOut(linea),FadeOut(text5_1))
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
        self.add_fixed_in_frame_mobjects(text8)
        self.play(Write(text8))
        self.wait(13)
        self.play(FadeOut(text8))