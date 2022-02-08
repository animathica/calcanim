from manimlib.imports import *

###################################
#### EJEMPLOS DE SUCESIONES #####
###################################

class Ejemplos_Sucesiones(Scene):
    def construct(self):

        plano = NumberPlane()

        title = TextMobject(r"Visualizando", r" Sucesiones").scale(1.5)
        title[1].set_color(YELLOW)
        converg = TextMobject(r"Veamos algunos ejemplos de", r" sucesiones convergentes.")
        converg[1].set_color(ORANGE)
        
        ## Ejemplos de sucesiones convergentes 
        
        ## Primer ejemplo ##

        ejem1 = TexMobject(r"X_n=\left(\frac{6}{n},0\right)")
        ejem1.bg=SurroundingRectangle(ejem1, color=WHITE, fill_color=BLACK, fill_opacity=1) 
        ej1=VGroup(ejem1.bg,ejem1) 

        suce1 = []
        for n in range(1,101): #LOS VALORES DE N VAN DESDE EL 1 AL 100
            x_n = Dot(point=np.array([6/n,0,0]),radius=0.05,color=RED)
            suce1.append(x_n)
        sucesion1 = VGroup(*suce1)

        preg1 = TextMobject("¿Cuál es el límite de esta sucesión?")
        preg2 = TextMobject("Demuéstralo usando la definición.")
        
        ## Segundo ejemplo ##

        eje2=TextMobject("Observemos un segundo ejemplo:")
        
        ejem2 = TexMobject(r"X_n=\left(\cos\left(\frac{1}{n}\right),e^{1/n}\right)")
        ejem2.bg=SurroundingRectangle(ejem2, color=WHITE, fill_color=BLACK, fill_opacity=1)
        ej2 = VGroup(ejem2.bg, ejem2)

        suce2 = []
        for n in range(1,101):
            x_n = Dot(point=np.array([np.cos(1/n),np.exp(1/n),0]),radius=0.04,color=PINK) 
            suce2.append(x_n)
        sucesion2 = VGroup(*suce2)

        preg1 = TextMobject("¿Cuál es el límite de esta sucesión?")
        preg2 = TextMobject("Demuéstralo usando la definición.")


        #Ejemplos de sucesiones NO convergentes
        
        diverg = TextMobject(r"Ahora, visualicemos una", r" sucesión no convergente:")
        diverg[1].set_color(YELLOW)
        
       ## Tercer ejemplo ##

        ejem3 = TexMobject(r"X_n=\left(\frac{n}{10},\frac{1}{n}\right)")
        ejem3.bg=SurroundingRectangle(ejem3, color=WHITE, fill_color=BLACK, fill_opacity=1)
        ej3 = VGroup(ejem3.bg, ejem3)

        suce3 = []
        for n in range(1,101):
            x_n = Dot(point=np.array([n/10,1/n,0]),radius=0.05,color=YELLOW)
            suce3.append(x_n)
        sucesion3 = VGroup(*suce3)

        ## Cuarto ejemplo ##
        
        eje4=TextMobject("Veamos un último ejemplo:")
        
        ejem4 = TexMobject(r"X_n=\left(e^{n/50}\cos\left(\frac{n}{5}\right),e^{n/50}\sin\left(\frac{n}{5}\right)\right)")
        ejem4.bg=SurroundingRectangle(ejem4, color=WHITE, fill_color=BLACK, fill_opacity=1)
        ej4 = VGroup(ejem4.bg, ejem4)
        
        suce4 = []
        for n in range(1,101):
            x_n = Dot(point=np.array([np.exp(n/50)*np.cos(n/5),np.exp(n/50)*np.sin(n/5),0]),radius=0.05,color=GREEN_SCREEN)
            suce4.append(x_n)
        sucesion4 = VGroup(*suce4)

        preg_1 = TextMobject('''¿Cómo demostrarías que el límite de esta sucesión no existe? \n
                                Usa la definición.''')
        preg_2 = TextMobject('''Usando lo que sabes de sucesiones en $\\mathbb{R}$, \n
                                        ¿de qué otro modo probarías la convergencia, \n
                                        o no convergencia, de una sucesión?  ''')
        
        #Reproduciendo las animaciones
        self.play(Write(title))
        self.wait()
        self.play(ReplacementTransform(title,converg))
        self.wait(2)
        self.play(FadeOut(converg)) 
        self.play(ShowCreation(plano),run_time=0.5)
        self.play(GrowFromCenter(ej1)) 
        self.wait(1) 
        self.play(ApplyMethod(ej1.to_edge,UP)) 
        self.play(Write(sucesion1),run_time=3) 
        self.wait()
        self.play(FadeOut(ej1),FadeOut(plano),FadeOut(sucesion1))
        self.play(Write(eje2))  
        self.wait() 
        self.play(FadeOut(eje2))
        self.play(ShowCreation(plano),run_time=0.5)
        self.play(GrowFromCenter(ej2))
        self.wait(1)
        self.play(ApplyMethod(ej2.to_edge,DOWN))
        self.play(Write(sucesion2),run_time=3)
        self.wait(0.5)
        self.play(FadeOut(plano),FadeOut(sucesion2))
        self.play(ApplyMethod(ej2.to_edge,UP))
        self.play(Write(preg1))
        self.wait(1.5)
        self.play(FadeOut(ej2))
        self.play(ReplacementTransform(preg1,preg2))
        self.wait(10)
        self.play(FadeOut(preg2))
        self.wait() 
        self.play(Write(diverg))
        self.wait()
        self.play(FadeOut(diverg))
        self.play(ShowCreation(plano),run_time=0.5)
        self.play(GrowFromCenter(ej3))
        self.wait(1)
        self.play(ApplyMethod(ej3.to_edge,UP))
        self.play(Write(sucesion3),run_time=3)
        self.wait()
        self.play(FadeOut(ej3),FadeOut(plano),FadeOut(sucesion3))
        self.play(Write(eje4))
        self.wait()
        self.play(ShrinkToCenter(eje4))
        self.play(ShowCreation(plano),run_time=0.5)
        self.play(GrowFromCenter(ej4))
        self.wait(1)
        self.play(ApplyMethod(ej4.to_edge,UP))
        self.play(Write(sucesion4),run_time=3) 
        self.wait()
        self.play(FadeOut(plano),FadeOut(sucesion4))
        self.play(ApplyMethod(ej4.to_edge,UP))
        self.play(Write(preg_1))
        self.wait(2)
        self.play(FadeOut(ej4))
        self.play(ReplacementTransform(preg_1,preg_2))
        self.wait(7)
        self.play(FadeOut(preg_2))