from manimlib.imports import *

# Cuando el lim es igual a infinito
class superficie3(ParametricSurface):
    def __init__(self, **kwargs):
        kwargs = {
        "u_min": -3,
        "u_max": 3,
        "v_min": -3,
        "v_max": 3,
        "checkerboard_colors": [BLUE_E]
        }
        ParametricSurface.__init__(self, self.func, **kwargs)

    def func(self, x, y):
        return np.array([x,y,(x*x)+(y*y)-1]) 
class superficie4(ParametricSurface):
    def __init__(self, **kwargs):
        kwargs = {
        "u_min": 0.1,
        "u_max": 5,
        "v_min": 0.1,
        "v_max": 5,
        "checkerboard_colors": [GREEN_B]
        }
        ParametricSurface.__init__(self, self.func, **kwargs)

    def func(self, x, y):
        return np.array([x,y,1+(1/((x*x)+(y*y)))])
        
class LimitesRnaR (ThreeDScene):
    def construct(self):
        titulo=TextMobject('''Divergencia a Infinito de Funciones \n
                            de $\\mathbb{R}^{n}\\rightarrow\\mathbb{R}$ en Infinito''').scale(1.5)

        text1=TextMobject('''Sea $f:\\mathbb{R}^{n}\\rightarrow\\mathbb{R}$''').move_to(2*UP)
        text2=TexMobject(r"lím_{\vec{x}\rightarrow\infty}f(\vec{x})=\infty^{+} \leftrightarrow\forall\ M\in\mathbb{R}").move_to(0.8*UP)
        text3=TextMobject('''$\\exists\\delta>0$ tal que si $\\vec{x}\\in B^{c}_{\\delta}(\\vec{0})$ ''' ).move_to(0.5*DOWN)
        text4=TexMobject(r'''\implies f(\vec{x})>M''').move_to(1.6*DOWN)
        text5=TextMobject("Veamos el siguiente ejemplo para aterrizar lo anterior.")
        text6=TextMobject('''Tomemos el paraboloide:\n
                                $f(x,y)=y^{2}+x^{2}-1$''')
        
        self.play(Write(titulo))
        self.wait(5.3)
        self.play(FadeOut(titulo))
        self.play(Write(text1))
        self.play(Write(text2))
        self.play(Write(text3))
        self.play(Write(text4))
        self.wait(8)
        self.play(FadeOut(text1),FadeOut(text2),FadeOut(text3),FadeOut(text4))
        self.play(Write(text5))
        self.wait(5)
        self.play(FadeOut(text5))
        self.play(Write(text6))
        self.wait(3.8)
        self.play(FadeOut(text6))
        self.custom_method()


    def custom_method(self):
        axes=ThreeDAxes()
        superficie=superficie3()
        superficie.set_opacity(0.8)
        text1=TexMobject(r'''f(x,y)=y^{2}+x^{2}-1''')
        text1.to_corner(UL)        
        text2=TextMobject('''Tomemos M=0''')
        text2.to_corner(UL)    
        text3=TextMobject('''Tomamos $\\delta$''')
        text3.to_corner(UL)
        
        text4=TextMobject('''Veremos que la imagen de los puntos que no \n
                            están en la bola, son mayor a M''')
        text4.to_corner(UL)
        text5=TextMobject('''Podemos realizar lo mismo con cualquier M$\\in\\mathbb{R}$''')
        text5.to_corner(UL)
        text6=TextMobject('''Por lo cual notaremos que la función diverge a $+\\infty$ \n
                             cuando $\\vec{x}\\rightarrow\\infty$.''')
        text6.to_corner(UL)
       # text7=TextMobject('''¿Se te ocurre como modificar la definición \n
        #                        cuando la función diverge a $\\infty^{-}$''')
        M=0
        r=M+1.4
        #cilindro = ParametricSurface(
       #     lambda u, v: np.array([
       #         r*np.cos(TAU * v),
       #         r*np.sin(TAU * v),
       #         2*u
       #     ]),
       #     resolution=(6, 32)).fade(0.1).set_opacity(0.4)
       # cilindro.set_color(RED_C).move_to(M*IN)
        #cilindro.set_opacity(0.4)
        M1=-0.5
        r1=M1+1.5
        #cilindro1 = ParametricSurface(
        #    lambda u, v: np.array([
        #        r1*np.cos(TAU * v),
        #        r1*np.sin(TAU * v),
        #        4*u
        #    ]),
        #    resolution=(6, 32)).fade(0.1).set_opacity(0.4)
        #cilindro1.set_color(RED_C).move_to((M1/2)*IN)
       # cilindro2.set_opacity(0.4)
        
        #bola1=Circle(radius=r1,color=RED,color_opacity=1).move_to(M1*OUT)
        bola1=Circle(radius=r1,color=RED,color_opacity=1)
       
        #plano1=Rectangle(height=3, width=5,color=PURPLE_C,fill_color=PURPLE_C,fill_opacity=0.4,
        #                        color_opacity=0.4 ).move_to(M*OUT)
        bola=Circle(radius=r,color=RED,color_opacity=1).move_to(M*OUT)
        linealabel=TexMobject(r'''\delta''').next_to(bola,RIGHT,buff=0.5).set_color(RED_C).rotate(PI/2,axis=RIGHT).scale(2)
        linea=Line((0,0,0),(r,0,0),stroke_width=3,color=RED_C) 

        def puntosEnSuperficie(rad,lim,num):
            puntosDom = []
            puntosSur = []
            for i in range(num):
                azar = np.random.uniform(-lim,lim, (1,2))[0]
                if ((rad < np.sqrt(azar[0]**2 + azar[1]**2)) and not (azar[0]<0 and azar[1]>0)):
                    puntosDom.append(Dot(np.array([azar[0], azar[1],0]), color = PURPLE))
                    puntosSur.append(Dot(superficie.func(azar[0], azar[1]), color = RED))
            return puntosDom, puntosSur

        puntosD1, puntosS1 = puntosEnSuperficie(r, 3, 6000)
        puntosD2, puntosS2 = puntosEnSuperficie(r1, r, 3000)

        GPuntosD1 = VGroup(*puntosD1)
        GPuntosS1 = VGroup(*puntosS1)
        GPuntosD2 = VGroup(*puntosD2)
        GPuntosS2 = VGroup(*puntosS2)

    ###Animacion
        self.set_camera_orientation(0.8*np.pi/2, -0.25*np.pi,distance=15)
        self.begin_ambient_camera_rotation(rate=0.001)
        self.play(ShowCreation(axes))
        self.add_fixed_in_frame_mobjects(text1)
        self.play(Write(text1))
        self.play(ShowCreation(superficie))
        self.wait(2)
        self.play(FadeOut(text1))
        self.add_fixed_in_frame_mobjects(text2)
        self.play(Write(text2))
        #self.play(ShowCreation(plano1))
        self.wait(2.75)
        self.play(FadeOut(text2))
        self.add_fixed_in_frame_mobjects(text3)
        self.play(Write(text3))
        self.play(ShowCreation(linea))
        self.play(Write(linealabel))
        self.play(ShowCreation(bola))
        self.play(FadeOut(linea),FadeOut(linealabel))
        self.play(FadeOut(text3))
        self.add_fixed_in_frame_mobjects(text4)
        self.play(Write(text4))
        self.play(FadeIn(GPuntosD1))
        self.play(FadeIn(GPuntosS1))
        #self.play(ShowCreation(cilindro))
        self.wait(8.3)
        self.play(FadeOut(text4))
        self.add_fixed_in_frame_mobjects(text5)
        self.play(Write(text5))
        ##self.play(plano1.shift,M1*OUT,runtime=1.5)
        self.play(ReplacementTransform(bola,bola1))
        self.wait()
        self.play(FadeIn(GPuntosD2))
        self.play(FadeIn(GPuntosS2))
        #self.play(ReplacementTransform(cilindro,cilindro1))
        self.wait(4.6)
        self.play(FadeOut(text5))
        self.add_fixed_in_frame_mobjects(text6)
        self.play(Write(text6))
        self.wait(6.5)
        self.play(FadeOut(axes),FadeOut(text6),FadeOut(superficie),FadeOut(bola1),
                FadeOut(GPuntosD1),FadeOut(GPuntosS1),FadeOut(GPuntosD2),FadeOut(GPuntosS2))