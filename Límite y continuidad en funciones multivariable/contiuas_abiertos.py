from manimlib.imports import *

class FunContinuasEnAbiertos (Scene):
    def construct(self):
        titulo=TextMobject('''Funciones Continuas y Abiertos''').scale(1.5)
        titulo1=TextMobject('''La imagen inversa de un abierto,\n
                                 bajo una función continua,\n 
                                     es un abierto''').move_to(-0.5*UP).scale(1.5)
        text1=TextMobject('''Tomemos la función ''',''' $f(x,y)=(x^{2},y)$''','''$ \ , \  (x,y)\\in\\mathbb{R}^{2}$''').move_to(1*UP)
        text2=TextMobject('''Notemos que $Im(f)={(x,z)\\in\\mathbb{R}^2|x\\geq 0}$ y''').move_to(0*UP)
        
        text3=TextMobject(''' $f(x,y)$ es continua en  $\\mathbb{R}^{2}$''').move_to(1*DOWN)
        text4=TextMobject('''Ahora tomemos un abierto en el contradominio de f \n
                            $U\\subset\\mathbb{R}^{2}$''').move_to(2.3*UP)
        text5=TextMobject('''Tomemos la imagen inversa de U''').move_to(text4)
        text6=TextMobject(''' $f^{-1}(U)$\n
                           $\\leftarrow$ ''').move_to(-1*UP)
        text7=TextMobject('''Lo mismo ocurre con cualquier abierto de $\\mathbb{R}^{2}$''').move_to(text5)
        text8=TextMobject(''' $f^{-1}(A)$\n
                           $\\leftarrow$ ''').move_to(-1*UP)

        textf=TextMobject('''$f:\\mathbb{R}^{n}\\rightarrow\\mathbb{R}^{m}$\n''',
                               '''f es continua en $\\bf{TODO}$ $\\mathbb{R}^{n}$\n
                                si solo si para todo \n  ''',    
                               '''$ U\\subset\\mathbb{R}^{m}$ abierto \n
                                   se cumple que $f^{-1}(U)$ es abierto ''')
        textf1=TextMobject(''' Lo mismo ocurre si el dominio de $f$ es abierto,\n 
                                      ''',''' ¿qué pasa si no lo es? \n
                                      ''',''' Investiga sobre topología relativa.''')
        textf2=TextMobject('''También puedes modificar el código para ver más \n
                                ejemplos con cajas''')
        linea1=Arrow((-6,-4,0),(-0.5,-4,0),stroke_width=6,color=WHITE,buff=0)
        linea2=Arrow((-3.5,-7,0),(-3.5,0,0),stroke_width=6,color=WHITE,buff=0)
        G1=VGroup(linea1,linea2).move_to(-2.5*UP+3.5*LEFT)

        linea3=Arrow((0.5,-4,0),(6,-4,0),stroke_width=6,color=WHITE,buff=0)
        linea4=Arrow((3,-7,0),(3,0,0),stroke_width=6,color=WHITE,buff=0)
        G2=VGroup(linea3,linea4).move_to(3.5*RIGHT-2.5*UP)

        #Pueden cambiar estos parametros para cambiar la caja de la imagen inversa
        r1=1#altura
        r2=1.5#ancho
    
        caja1=Rectangle(height=r1, width=r2,fill_color=YELLOW_C,color=YELLOW_C ,fill_opacity=1,buff=0).move_to((3.7+(-r2/2))*LEFT-2.5*UP)
        
        caja2=Rectangle(height=r1, width=r2*r2,fill_color=PURPLE_C,color=PURPLE_C ,fill_opacity=1,buff=0).move_to((3.3+r2*r2/2)*RIGHT+-2.5*UP)
        caja2label=TextMobject("U").next_to(caja2)
        #Tambien se puede cambiar r3 y r4 para cambiar los tamaños de la caja en el 2do ejemplo
        r3=2#altura
        r4=2#ancho
        #posiciones de la caja, por si se quiere
        #usar una caja que no este esquinada y elevada en y en el segundo ejemplo
        y=0

        caja3=Rectangle(height=r3, width=(r4/3),fill_color=YELLOW_C,color=YELLOW_C ,fill_opacity=1,buff=0).move_to((4.7)*LEFT+(-3+(r3/2))*UP)
        
        caja5=Rectangle(height=r3, width=(r4/3),fill_color=YELLOW_C,color=YELLOW_C ,fill_opacity=1,buff=0).move_to((2.8)*LEFT+(-3+(r3/2))*UP)

        caja4=Rectangle(height=r3, width=(r4/2)**2,fill_color=PURPLE_C,color=PURPLE_C ,fill_opacity=1,buff=0).move_to((3.8+((((r4/2)**2)/2)))*RIGHT+(-3+(r3/2))*UP)
        caja4label=TextMobject("A").next_to(caja4)

        punto=np.array([1,-4,0])
        

        ### Animación
        self.play(Write(titulo))
        self.wait()
        self.play(titulo.shift,2*UP,runtime=1.5)
        self.wait(2)
        self.play(Write(titulo1))        
        self.wait(5)
        self.play(FadeOut(titulo),FadeOut(titulo1))
        self.play(Write(text1))
        self.wait(6)
        self.play(Write(text2))
        self.wait(3)
        self.play(Write(text3))
        self.wait(4)
        self.play(FadeOut(text1[0]),FadeOut(text2),FadeOut(text3),FadeOut(text1[2]))
        self.play(text1[1].shift,2.5*UP+1.2*LEFT,runtime=1.5)
        self.play(ShowCreation(G1),ShowCreation(G2))
        self.play(Write(text4))
        self.wait(6)
        self.play(ShowCreation(caja2),Write(caja2label))
        self.play(ReplacementTransform(text4,text5))
        self.wait(3)
        self.play(Write(text6))
        self.wait()
        self.play(ShowCreation(caja1))
        self.play(ReplacementTransform(text5,text7))
        self.wait(5)
        self.play(ReplacementTransform(caja2,caja4),ReplacementTransform(caja2label,caja4label))
        self.play(ReplacementTransform(text6,text8))
        self.play(ReplacementTransform(caja1,caja3))
        self.play(ShowCreation(caja5))
        self.wait()
        self.play(FadeOut(caja3),FadeOut(caja4),FadeOut(caja5),FadeOut(G1),FadeOut(G2),FadeOut(text8),FadeOut(text1[1]),
                     FadeOut(text7),FadeOut(caja4label)   )
        self.play(Write(textf[0]))
        self.wait(5)
        self.play(Write(textf[1]))
        self.wait()
        self.play(Write(textf[2]))
        self.wait(5)
        self.play(FadeOut(textf))
        self.play(Write(textf1[0]))
        self.wait(5)
        self.play(Write(textf1[1]))
        self.wait(2)
        self.play(Write(textf1[2]))
        self.wait(3)
        self.play(ReplacementTransform(textf1,textf2))
        self.wait(5)
        self.play(FadeOut(textf2))