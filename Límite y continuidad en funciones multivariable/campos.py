from manimlib.imports import *

########################
##LIMITES DE R2 A R2####
########################

#Funciones de R2 A R2
# Definimos los campos vectoriales
def campo(point):
    x,y=point[:2]
    return (-((1/(y*y*y*y*y)))*RIGHT+x*UP)
def campo2(point):
    x,y=point[:2]
    return (-(y)*RIGHT+x*UP)

class LimiteR2aR2(Scene):

    def construct(self):
        
        titulo=TextMobject('''Ejemplo de \n
                                Límite en Campos''').scale(1.5)


        text=TextMobject('''Consideremos la función:''')
        text1=TexMobject(r"f(x,y)=(-y,x)")
        text1_bg=SurroundingRectangle(text1, color=WHITE, fill_color=BLACK, fill_opacity=1)
        text1_rect=VGroup(text1_bg, text1)
        text2=TextMobject(''' Es posible mostrar que esta función tiene límite \n
                                en todo $\\mathbb{R}^{2}$''').to_corner(UL)
        text2_rect=VGroup(SurroundingRectangle(text2, color=WHITE, fill_color=BLACK, fill_opacity=1), text2)
        
        text2_1=TextMobject('''En particular, cuando $(x,y) \\rightarrow (0,0)$, el límite es (0,0)''').to_corner(UL)
        text2_1_rect=VGroup(SurroundingRectangle(text2_1, color=WHITE, fill_color=BLACK, fill_opacity=1), text2_1)

        text3=TextMobject('''Podemos ver lo anterior gráficamente de \n
                                la siguiente manera''').to_corner(UL).to_corner(UL)
        text3_rect=VGroup(SurroundingRectangle(text3, color=WHITE, fill_color=BLACK, fill_opacity=1), text3)
        text4=TextMobject("Sea $\\varepsilon<0$. Si escogemos una bola de radio", " $\\delta$").to_corner(UL)
        text4[1].set_color(GREEN)
        text4_rect=VGroup(SurroundingRectangle(text4, color=WHITE, fill_color=BLACK, fill_opacity=1), text4)
        text5=TextMobject("Podemos encontrar una bola, de radio $\\varepsilon$, tal que la",  ''' norma de\n
                            la imagen de los puntos''', ''' dentro de la misma'''   ).to_edge(UP)
        text5[1].set_color(RED)
        text5_rect=VGroup(SurroundingRectangle(text5, color=WHITE, fill_color=BLACK, fill_opacity=1), text5)

        text6=TextMobject('''Estén a una distancia menor a''',''' $\\delta$''').to_edge(UP)
        text6[1].set_color(GREEN)
        text6_rect=VGroup(SurroundingRectangle(text6, color=WHITE, fill_color=BLACK, fill_opacity=1), text6)
        text7=TextMobject('''Es posible hacer lo anterior con cualquier $\\delta$''')
        text7_rect=VGroup(SurroundingRectangle(text7, color=WHITE, fill_color=BLACK, fill_opacity=1), text7)

        text8=TextMobject('''Una función $f:A\subset\\mathbb{R}^{n}\\rightarrow\\mathbb{R}^{m}$''').move_to(2.8*UP)
        text8_1=TextMobject('''tiene límite en $\\vec{x}_0$ y es $\\vec{l}$ si:''').move_to(1.5*UP)
        text8_2=TexMobject(r"\forall\varepsilon>0\ \exists\delta>0 \ tq \ si\ ||\vec{x}-\vec{x_0}||<\delta")
        text8_3=TexMobject(r"(\vec{x}\in A\setminus\lbrace\vec{x_0}\rbrace) \ \text{entonces} \ ||f(\vec{x})-\vec{l}||<\varepsilon").move_to(1.5*DOWN)
        G1=VGroup(text8,text8_1,text8_2,text8_3)

        #Se puede cambiar delta y x para modificar las bolas
        delta=2.1
        x=0
        delta1=Line((0,0,0),(0,delta,0),color=GREEN,stroke_width=3)
        bola=Circle(radius=delta,color=GREEN).move_to(x*RIGHT)
        bola1=Circle(radius=delta-0.05,color=WHITE)
        bola_1=Circle(radius=delta+1,color=GREEN).move_to(x*RIGHT)
        bola1_1=Circle(radius=delta+1-0.05,color=WHITE)

        axes=Axes()
        # Se crea el campo vectorial con la funcion
        campo_2 = VectorField(campo2, x_min=-8,x_max=8,y_min=-6,y_max=6,
            delta_x=0.5, delta_y=0.5,length_func= lambda norm: 0.5 * sigmoid(norm), colors=[BLUE])

        imagen1=Vector(direction=(1,0.36,0),stroke_width=2, max_tip_length_to_length_ratio=0.15, color=RED)
        imagen2=Vector(direction=(.7,1.3,0),stroke_width=2, max_tip_length_to_length_ratio=0.1, color=RED)
        imagen3=Vector(direction=(-0.36,1,0),stroke_width=2, max_tip_length_to_length_ratio=0.15, color=RED)
        imagen4=Vector(direction=(-1.65,0.1,0),stroke_width=2, max_tip_length_to_length_ratio=0.1, color=RED)
        imagen5=Vector(direction=(-1.35,-0.85,0),stroke_width=2, max_tip_length_to_length_ratio=0.1, color=RED)
        imagen6=Vector(direction=(1.35,-1.3,0),stroke_width=2, max_tip_length_to_length_ratio=0.1, color=RED) 
        imagen=VGroup(imagen1, imagen2, imagen3, imagen4, imagen5, imagen6)

        imagen1_c=Vector(direction=(1.8,1.4,0),stroke_width=2, max_tip_length_to_length_ratio=0.08, color=RED)
        imagen2_c=Vector(direction=(1.7,2.35,0),stroke_width=2, max_tip_length_to_length_ratio=0.07, color=RED)
        imagen3_c=Vector(direction=(-1.4,1.8,0),stroke_width=2, max_tip_length_to_length_ratio=0.08, color=RED)
        imagen4_c=Vector(direction=(-2.7,1.1,0),stroke_width=2, max_tip_length_to_length_ratio=0.07, color=RED)
        imagen5_c=Vector(direction=(-2.3,-1.9,0),stroke_width=2, max_tip_length_to_length_ratio=0.07, color=RED)
        imagen6_c=Vector(direction=(1.4,-2.35,0),stroke_width=2, max_tip_length_to_length_ratio=0.08, color=RED)
        imagen_c=VGroup(imagen1_c, imagen2_c, imagen3_c, imagen4_c, imagen5_c, imagen6_c)
    

        self.play(Write(titulo))
        self.wait(3.5)
        self.play(FadeOut(titulo))
        self.play(Write(text))
        self.wait(1.125)
        self.play(text.shift, 1.5*UP, runtime=1.5)
        self.play(Write(text1))
        self.wait(3)
        self.play(FadeOut(text))
        self.play(ReplacementTransform(text1, text1_rect))
        self.add_foreground_mobjects(text1_rect)
        self.play(Write(axes),text1_rect.shift,3*UP+4*LEFT,runtime=1.5)
       # Dibujamos el campo vectorial 
        self.play(*[GrowArrow(vec) for vec in campo_2],runtime=20)
        self.wait()
        self.play(ReplacementTransform(text1_rect,text2_rect))
        self.add_foreground_mobjects(text2_rect)
        self.wait(4.2)
        self.play(ReplacementTransform(text2_rect,text2_1_rect))
        self.wait(4.2)
        self.play(FadeOut(text2_1_rect))
        self.play(Write(text3_rect))
        self.wait(3.5)
        self.play(ReplacementTransform(text3_rect,text4_rect))
        self.wait(4.2)
        self.play(ShowCreation(delta1))
        self.play(ShowCreation(bola))
        self.play(ReplacementTransform(text4_rect,text5_rect))
        self.wait(8)
        self.play(ShowCreation(bola1))
        self.wait()
        self.play(*[GrowArrow(img) for img in imagen])
        self.wait()
        self.play(ReplacementTransform(text5_rect,text6_rect))
        self.wait(2.7)
        self.play(ReplacementTransform(text6_rect,text7_rect))
        self.add_foreground_mobjects(text7_rect)
        self.play(ReplacementTransform(bola,bola_1))
        self.play(ReplacementTransform(bola1,bola1_1))
        self.wait(3)
        self.play(ReplacementTransform(imagen,imagen_c))
        self.wait(2)
        self.play(FadeOut(imagen_c), FadeOut(campo_2),FadeOut(bola1_1),FadeOut(bola_1),
                    FadeOut(axes),FadeOut(text7_rect),FadeOut(delta1))
        self.play(Write(text8))
        self.play(Write(text8_1))
        self.play(Write(text8_2))
        self.play(Write(text8_3))
        self.wait(11.25)
        self.play(FadeOut(G1))
        self.wait()
        self.custom_method()

    def custom_method(self):
                     
        text=TextMobject('''Consideremos ahora la función:''')
        text1=TexMobject(r"f(x,y)=\left({\frac{-1}{y^{5}}},x\right)")
        text1_rect=VGroup(SurroundingRectangle(text1, color=WHITE, fill_color=BLACK, fill_opacity=1), text1)
        text2=TextMobject(''' Es posible demostrar que esta función no tiene\n
                                límite en cualquier punto de la forma (x,0)''').move_to(
                                    text1.get_center()-2*UP)
        text2_rect=VGroup(SurroundingRectangle(text2, color=WHITE, fill_color=BLACK, fill_opacity=1), text2)
        text3=TextMobject('''Podemos ver lo anterior gráficamente de \n
                                la siguiente manera''').to_corner(UL)
        text3_rect=VGroup(SurroundingRectangle(text3, color=WHITE, fill_color=BLACK, fill_opacity=1), text3)
        text4=TextMobject('''La imagen de la función\n
                            siempre está creciendo en el eje x''').to_corner(UL)
        text4_rect=VGroup(SurroundingRectangle(text4, color=WHITE, fill_color=BLACK, fill_opacity=1), text4)
        text5=TextMobject('''¿Se te ocurre como demostrar que la función anterior\n
                                no tiene límite?''')
        axes=Axes() 
        # Se crea el campo vectorial con la función CurlFunc
        campo_1 = VectorField(campo, x_min=-8,x_max=8,y_min=-6,y_max=6,
            delta_x=0.45, delta_y=0.45,length_func= lambda norm: 0.49 * sigmoid(norm) )
       
    
        self.play(Write(text))
        self.wait(1.5)
        self.play(text.shift, 2*UP, runtime=1.5)
        self.play(Write(text1))
        self.wait(3.375)
        self.play(FadeOut(text))
        self.play(ReplacementTransform(text1, text1_rect))
        self.add_foreground_mobjects(text1_rect)
        self.play(Write(axes),text1_rect.shift,3*UP+4*LEFT,runtime=1.5)
       # Dibujamos el campo vectorial 
        self.play(*[GrowArrow(vec) for vec in campo_1],runtime=20)
        self.wait(1.2)
        self.play(Write(text2_rect))
        self.add_foreground_mobjects(text2_rect)
        self.wait(6)
        self.play(FadeOut(text1_rect),FadeOut(text2_rect))
        self.play(Write(text3_rect))
        self.wait(3.375)
        self.play(ReplacementTransform(text3_rect,text4_rect))
        self.wait(4.5)
        self.play(FadeOut(text4_rect))
        self.play(FadeOut(axes),FadeOut(campo_1))
        self.play(Write(text5))
        self.wait(4.5)
        self.play(FadeOut(text5))