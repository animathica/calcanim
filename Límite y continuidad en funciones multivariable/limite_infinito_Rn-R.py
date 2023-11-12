from manimlib.imports import *

class Limite4_1 (ThreeDScene):
    def construct (self):
        titulo=TextMobject('''Existencia del Límite en Infinito\n
                            de Funciones de $\\mathbb{R}^n$ $\\rightarrow$ $\\mathbb{R}$''').scale(1.5)
        text=TextMobject("Sea $f:\\mathbb{R}^{n}\\rightarrow\\mathbb{R}$").move_to(2.2*UP)
        text1=TexMobject(r"\lim_{\vec{x}\rightarrow\infty}f(\vec{x})=L\leftrightarrow\forall\epsilon>0").move_to(1*UP)
        text2=TexMobject(r"\exists\delta>0 \ tq \ \forall \vec{x}\in B^{c}_{\delta}(\vec{0})").move_to(-0.2*UP)
        text3=TexMobject(r"\implies d(f(\vec{x}),L)<\epsilon").move_to(1.4*DOWN)
        G1=VGroup(text,text1,text2,text3)
        text4=TextMobject('''Veamos el siguiente ejemplo para aterrizar ideas:''')
        text5=TexMobject(r"f:\mathbb{R}^{2}\rightarrow\mathbb{R}")
        text6=TexMobject(r"f(x,y)=1+\frac{1}{x^{2}+y^{2}}").move_to(1.5*DOWN)
        G2=VGroup(text4,text5,text6)

        self.play(Write(titulo))
        self.wait(5.25)
        self.play(FadeOut(titulo))
        self.play(Write(text))
        self.play(Write(text1))
        self.play(Write(text2))
        self.play(Write(text3))
        self.wait(6)
        self.play(FadeOut(G1))
        self.play(Write(text4))
        self.wait(4.6)
        self.play(text4.shift,2*UP,runtime=1.5)
        self.play(Write(text5))
        self.play(Write(text6))
        self.wait(3)
        self.play(FadeOut(G2))
        self.wait()
        self.custom_method()


    def custom_method(self):
        axes=ThreeDAxes()
        superficie=superficie4()
        text1=TexMobject(r'''f(x,y)=1+\frac{1}{x^{2}+y^{2}}''')
        text1.to_corner(UL)       
        text2=TextMobject("Tomemos", " $\epsilon$=0.5")
        text2.to_corner(UL)
        text2[1].set_color(RED)
        text3=TextMobject('''Y notemos que \n 
                            podemos escoger''').to_corner(UL)
        text3_1=TextMobject("una"," $\\delta>0$").move_to(text3.get_center()+1*DOWN)
        text3_1[1].set_color(YELLOW_C)
        text4=TextMobject('''Tal que la imagen de los\n
                             puntos que no \n
                            pertenecen a $ B_{\\delta}(\\vec{0})$,''').to_corner(UL)
        text5=TextMobject('''están a una distancia $\\epsilon$\n
                                de 1.''').to_corner(UL)
        text5_1=TextMobject('''Es posible hacer lo mismo\n  
                            con toda $\\epsilon>0$.''').to_corner(UL)
        text6=TextMobject('''Por lo cual:''').to_corner(UL)
        text7=TexMobject(r"\lim_{\vec{x}\rightarrow\infty}f(\vec{x})=1").move_to(text5.get_center()+1*DOWN)
        
        M=TextMobject("1").move_to(1*UP+0.2*LEFT)

        #epsilons se pueden modificar
        r=0.5
        r1=1
        linea=Line((0,0,1),(0,0,1+r),stroke_width=6,color=RED)
        linea_1=Line((0,0,1),(0,0,1+r1),stroke_width=6,color=RED)
        R=1.7
        R1=R-0.5
        linea1=Line((0,0,0),(R,0,0),stroke_width=6,color=YELLOW_C)
        
        circulo=Circle(radius=R,color=YELLOW_C)
        circulo1=Circle(radius=R1,color=YELLOW_C)
        #cilindro = ParametricSurface(
        #    lambda u, v: np.array([
        #        R*np.cos(TAU * v),
        #        R*np.sin(TAU * v),
        #        4*u
        #    ]),
        #    resolution=(6, 32)).fade(0.1).set_opacity(0.2)
        #cilindro.set_color(YELLOW_C)
        #cilindro1 = ParametricSurface(
        #    lambda u, v: np.array([
        #        R1*np.cos(TAU * v),
        #        R1*np.sin(TAU * v),
        #        4*u
        #    ]),
        #    resolution=(6, 32)).fade(0.1).set_opacity(0.2)
        #cilindro1.set_color(YELLOW_C)

        def puntosEnSuperficie(rad,lim,num):
            puntosDom = []
            puntosSur = []
            for i in range(num):
                azar = lim*np.random.rand(1,2)[0] + 0.1
                if (rad < np.sqrt(azar[0]**2 + azar[1]**2) < lim):
                    puntosDom.append(Dot(np.array([azar[0], azar[1],0]), color = BLUE))
                    puntosSur.append(Dot(superficie.func(azar[0], azar[1]), color = RED))
            return puntosDom, puntosSur

        puntosD1, puntosS1 = puntosEnSuperficie(R, 5, 6000)
        puntosD2, puntosS2 = puntosEnSuperficie(R1, R, 3000)

        GPuntosD1 = VGroup(*puntosD1)
        GPuntosS1 = VGroup(*puntosS1)
        GPuntosD2 = VGroup(*puntosD2)
        GPuntosS2 = VGroup(*puntosS2)

    ###Animacion
        self.set_camera_orientation(0.8*np.pi/2, -0.25*np.pi,distance=12)
        self.begin_ambient_camera_rotation(rate=0.001)
        self.play(ShowCreation(axes))
        self.add_fixed_in_frame_mobjects(text1)
        self.add_fixed_in_frame_mobjects(M)
        self.play(Write(text1))
        self.play(ShowCreation(superficie))
        self.wait()
        self.play(FadeOut(text1))
        self.add_fixed_in_frame_mobjects(text2)
        self.play(Write(text2))
        self.play(ShowCreation(linea))
        self.play(FadeOut(text2))
        self.add_fixed_in_frame_mobjects(text3)
        self.play(Write(text3))
        self.add_fixed_in_frame_mobjects(text3_1)
        self.play(Write(text3_1))
        self.play(ShowCreation(linea1))
        self.play(ShowCreation(circulo))
        self.play(FadeOut(text3),FadeOut(text3_1))
        self.add_fixed_in_frame_mobjects(text4)
        self.play(Write(text4))
        #self.play(ShowCreation(cilindro))
        self.wait()
        self.play(FadeOut(text4))
        self.play(FadeIn(GPuntosD1))
        self.add_fixed_in_frame_mobjects(text5)
        self.play(Write(text5),FadeOut(linea1))
        self.play(FadeIn(GPuntosS1))
        self.play(linea.shift,(R+0.1)*RIGHT,runtime=10)        
        self.wait(6.5)
        self.play(FadeOut(text5))
        self.add_fixed_in_frame_mobjects(text5_1)
        self.play(Write(text5_1))
        self.play(ReplacementTransform(linea,linea_1))
        self.play(ReplacementTransform(circulo,circulo1))
        #self.play(ReplacementTransform(cilindro,cilindro1))
        self.play(FadeIn(GPuntosD2))
        self.play(FadeIn(GPuntosS2))
        self.play(linea_1.shift,(R1+0.1)*RIGHT,runtime=10)
        self.wait(3)
        self.play(FadeOut(text5_1))
        self.add_fixed_in_frame_mobjects(text6)
        self.play(Write(text6))
        self.add_fixed_in_frame_mobjects(text7)
        self.play(Write(text7))
        self.wait(2)
        self.play(FadeOut(text7),FadeOut(text6),FadeOut(axes),FadeOut(M),
                    FadeOut(superficie),FadeOut(linea_1),FadeOut(circulo1),FadeOut(GPuntosD1),
                    FadeOut(GPuntosS1),FadeOut(GPuntosD2),FadeOut(GPuntosS2))