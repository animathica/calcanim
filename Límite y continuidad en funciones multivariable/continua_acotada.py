from manimlib.imports import *

## Teorema fuerte: Continuas son acotadas en compactos ##

class Continua_y_acotada(Scene):
    def construct(self):
        # Textos
        #title = TextMobject('''Continua en compactos implica acotada''').scale(1.5)
        title = TextMobject('''Teorema Fuerte: \n
                            Funciones Continuas son \n
                            Acotadas en Compactos''').scale(1.5)
        t1 = TextMobject('''$f:A\\subset\\mathbb{R}^n\\to\\mathbb{R}^m$ es ''','''acotada''',''' si \n
                            $f(A)\\subset\\mathbb{R}^m$ es ''','''acotada''')
        t1.set_color_by_tex_to_color_map({
            '''acotada''': PURPLE_B
        })
        t2 = TextMobject('''Teniendo en cuenta la definición anterior consideremos el \n 
                            conjunto ''','''$A$''','''$ =[0,\\ 1.5]\\times[0,2]$ en $\\mathbb{R}^2$''')
        t2[1].set_color(RED)
        t3 = TextMobject('''Recuerda que este conjunto es ''','''compacto''').next_to(t2,DOWN).scale(0.85).shift(2.5*UP)
        t3[1].set_color(ORANGE)
        t4 = TextMobject('''Toma la función $f:A\\to\\mathbb{R}^2$ dada por $f(x,y)=(x^2,y^2)$, \n 
                            ¿cuál es la ''','''imagen''',''' de ''','''$A$''',''' bajo $f$?''').scale(1.17)
        t4[1].set_color(BLUE)
        t4[3].set_color(RED)
        t5 = TextMobject('''$f$ es ''','''continua''',''' y $f(A)$ es un conjunto ''','''acotado''','''. \n
                            Intenta demostrar ambas afirmaciones.''').scale(1.17)
        t5[1].set_color(GREEN_D)
        t5[3].set_color(PURPLE_B)
        t6 = TextMobject('''El resultado que vimos, es uno de los teoremas importantes \n
                            de continuidad, y dice lo siguiente:''').shift(UP*0.75)
        t7 = TextMobject('''Si $F:K\\subset\\mathbb{R}^n\\to\\mathbb{R}^m$ es ''','''continua''',''' y $K$ ''','''compacto''',''' \n
                            entonces $F$ es ''','''acotada''').next_to(t6,DOWN*1)
        t7[-1].set_color(PURPLE_B)
        t7[1].set_color(GREEN_D)
        t7[3].set_color(ORANGE)
        
        # Ejes
        ejes1 = Axes(x_min=-0.5,x_max=5,y_min=-0.5,y_max=4).move_to((-6+2.25,-3+1.75,0))
        ejes2 = Axes(x_min=-0.5,x_max=5,y_min=-0.5,y_max=4).move_to((1.5+2.25,-3+1.75,0))
        
        # Objetos
        compacto = Rectangle(height=1.5,width=2,color=RED,fill_color=RED,fill_opacity=0.8).move_to((-5,-2.25,0))
        imagen = Rectangle(height=2.25,width=4,color=BLUE,fill_color=BLUE,fill_opacity=0.8).move_to((3.5,-1.875,0))
        flecha = Arrow(start=(-1,0,0),end=(1,0,0),color=WHITE)
        f = TexMobject(r"f(x,y)").next_to(flecha,DOWN).shift(0.25*DOWN)

        # Grupos
        Grupo0 = VGroup(t2,t3)
        Grupo1 = VGroup(t4,t5).to_edge(UP).scale(0.7)
        Grupo2 = VGroup(flecha,f)
        Grupo3 = VGroup(ejes1,ejes2,compacto,imagen,Grupo2,t5)


        # Animación

        self.play(Write(title))
        self.wait(3.25)
        self.play(ReplacementTransform(title,t1))
        self.wait(7.5)
        self.play(ReplacementTransform(t1,t2))
        self.wait(5)
        self.play(ApplyMethod(t2.scale,0.85))
        self.play(ApplyMethod(t2.to_edge,UP))
        self.wait()
        self.play(ShowCreation(ejes1))
        self.play(ShowCreation(compacto))
        self.wait()
        self.play(Write(t3))
        self.wait(3)
        self.play(FadeOut(t3))
        self.play(ReplacementTransform(t2,t4))
        self.wait(7)
        self.play(Write(Grupo2))
        self.play(ShowCreation(ejes2))
        self.play(ShowCreation(imagen))
        self.wait()
        self.play(ReplacementTransform(t4,t5))
        self.wait(7)
        self.play(FadeOut(Grupo3))
        self.play(Write(t6))
        self.wait(5)
        self.play(Write(t7))
        self.wait(5)
        self.play(FadeOut(t6),FadeOut(t7))