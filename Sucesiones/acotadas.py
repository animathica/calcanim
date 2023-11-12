from manimlib.imports import *

###################################
####   SUCESIONES ACOTADAS    #####
###################################

class Sucesiones_Acotadas(Scene):
    def construct(self):
        plano = NumberPlane()
        title = TextMobject('''Sucesiones acotadas''')
        text1 = TextMobject('''Considera la siguiente sucesión''').shift(UP)

        self.play(Write(title))
        self.wait(6)
        self.play(ReplacementTransform(title,text1))

        ejem1 = TexMobject(r"X_n=\left(3e^{-n/30}\cos\left(\frac{n}{5}\right),3e^{-n/30}\sin\left(\frac{n}{5}\right)\right)").next_to(text1,DOWN)
        
        self.play(Write(ejem1))
        self.wait()
        self.play(FadeOut(text1),FadeOut(ejem1))

        suce1 = []
        for n in range(1,151):
            x_n = Dot(point=np.array([3*np.exp(-n/30)*np.cos(n/5),3*np.exp(-n/30)*np.sin(n/5),0]),color=ORANGE)
            suce1.append(x_n)
        sucesion1 = VGroup(*suce1)

        self.play(ShowCreation(plano),run_time=0.5)
        self.play(Write(sucesion1),run_time=10)
        self.wait()
        self.play(FadeOut(plano),FadeOut(sucesion1),run_time=0.5)

        text2 = TextMobject('''Piensa en lo que representaría geométricamente \n
                                que una sucesión fuera acotada''')
        text3 = TextMobject('''Considera una bola de radio $M=3$ centrada en el origen''')
        bola = Circle(radius=3,color=RED)

        self.play(Write(text2))
        self.wait(5)
        self.play(ReplacementTransform(text2,text3))
        self.wait(5)
        self.play(FadeOut(text3))
        self.play(ShowCreation(plano),run_time=0.5)
        self.play(FadeIn(bola),Write(sucesion1))
        self.wait()

        text4 = TextMobject('''Puedes ver que se cumple \n
                            $\\{X_n\\}\\subset B_{M}(\\bar{0})$''',color=BLACK).scale(0.6)
        text4.bg = SurroundingRectangle(text4,color=RED,fill_color=WHITE,fill_opacity=1)
        text4.group = VGroup(text4.bg,text4).move_to(np.array([-4.5,3,0]))

        self.play(FadeIn(text4.group))
        self.wait(7)
        self.play(FadeOut(plano),FadeOut(sucesion1),FadeOut(bola),FadeOut(text4.group))

        text5 = TextMobject('''Y justo con esto es como se define sucesión acotada''')
        text6 = TextMobject('''Decimos que $\\{X_n\\}$ es acotada si existe $M\\in\\mathbb{R}^+$ \n
                            tal que $\\{X_n\\}\\subset B_{M}(\\bar{0})$''')
        text7 = TextMobject('''Intenta demostrar que la sucesión $X_n=(n,n)$ NO es acotada\n
                                usando la definición anterior (su negación)''')

        self.play(Write(text5))
        self.wait(4)
        self.play(ReplacementTransform(text5,text6))
        self.wait(9)
        self.play(ReplacementTransform(text6,text7))
        self.wait(5)
        self.play(FadeOut(text7))