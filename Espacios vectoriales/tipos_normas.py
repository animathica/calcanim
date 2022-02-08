from manimlib.imports import *

#####################################
#### DIFERENTES TIPOS DE NORMAS #####
#####################################

class Normas(Scene):
    def construct(self):
        plano = NumberPlane()
        intro1 = TextMobject("Veremos como se ve un c\\'{i}rculo unitario")
        intro2 = TexMobject(r"\text{utilizando diferentes normas en }\mathbb{R}^2")
        intro2.next_to(intro1, DOWN)
        intro = VGroup(intro1, intro2)
        circ1 = TextMobject("Recordemos que la definici\\'{o}n de una circunferencia es")
        circ2 = TexMobject(r"\mathbb{S}^1=\{x\in\mathbb{R}^2 : \Vert x \Vert =1\}")
        circ2.next_to(circ1, DOWN)
        circ = VGroup(circ1, circ2)

        self.play(Write(intro))
        self.wait(2)
        self.play(ReplacementTransform(intro,circ))
        self.wait(2)
        self.play(FadeOut(circ))

        #### Norma 1 ####

        title1 = TextMobject("Norma 1")
        norm1 = TexMobject(r"\Vert x \Vert_1=\vert x_1 \vert + \vert x_2 \vert")
        norm1.next_to(title1,DOWN)
        Group1 = VGroup(title1,norm1)
        Group1.scale(0.75)
        Group1.set_color(RED)
        fig1 = Square(side_length=np.sqrt(2),color=RED)
        fig1.rotate(PI/4)

        self.play(Write(Group1))
        self.wait()
        self.play(ApplyMethod(Group1.to_edge,UP))
        self.play(ShowCreation(plano))
        self.play(ShowCreation(fig1))
        self.wait(2)
        self.play(ApplyMethod(Group1.move_to,np.array([-5,3,0])))

        #### Norma 2 ####

        title2 =TextMobject("Norma 2")
        norm2 = TexMobject(r"\Vert x \Vert_2=\left(x_1^2 + x_2^2 \right)^{1/2}")
        norm2.next_to(title2,DOWN)
        Group2 = VGroup(title2,norm2)
        Group2.scale(0.75)
        Group2.set_color(YELLOW)
        fig2 = Circle(radius=1,color=YELLOW)

        self.play(Write(Group2))
        self.wait()
        self.play(ApplyMethod(Group2.to_edge,UP))
        self.play(ShowCreation(fig2))
        self.wait(2)
        self.play(ApplyMethod(Group2.move_to,np.array([5,3,0])))

        #### Norma infinito ####

        title3 = TextMobject("Norma infinito")
        norminfty = TexMobject(r"\Vert x \Vert_{\infty} = \max\{\vert x_i \vert : i \in \{1,2\}\}")
        norminfty.next_to(title3,DOWN)
        Group3 = VGroup(title3,norminfty)
        Group3.scale(0.75)
        Group3.set_color(GREEN_SCREEN)
        fig3 = Square(side_length=2,color=GREEN_SCREEN)

        self.play(Write(Group3))
        self.wait()
        self.play(ApplyMethod(Group3.to_edge,UP))
        self.play(ShowCreation(fig3))
        self.wait(2)
        self.remove(Group1,Group2,Group3,plano,fig1,fig2,fig3)
        
        #### Norma p ####

        intro1 = TextMobject("Podemos definir una norma similar a las anteriores")
        intro2 = TexMobject(r"\text{para cada } p\in\mathbb{R},\ p\geq 1")
        intro2.next_to(intro1,DOWN)
        intro = VGroup(intro1,intro2)
        titlep = TexMobject(r"\text{Norma } p")
        normp = TexMobject(r"\Vert x \Vert_p = \left(\sum_{i=1}^n \vert x_i \vert ^p \right)^{1/p}")
        normp.next_to(titlep,DOWN)
        Groupp = VGroup(titlep,normp)
        text = TextMobject("Veamos que pasa cuando $p$ crece en $\\mathbb{R}$")

        self.play(Write(intro))
        self.wait(2)
        self.play(ReplacementTransform(intro,Groupp))
        self.wait(2)
        self.play(FadeOut(Groupp))
        self.play(Write(text))
        self.play(FadeOut(text))
        self.play(ShowCreation(plano))
        self.play(FadeIn(Group3),ShowCreation(fig3))
        self.play(ApplyMethod(Group3.to_edge,DOWN))

        n = 1

        while n<10:
            valor_sig = TexMobject(r"p="+str(n))
            valor_sig.to_edge(UP)
            self.add(valor_sig)
            D = []
            j=0
            dj=1/16
            while j<1:
                dot1 = Dot(radius=0.05,color=PINK)
                dot1_2 = Dot(radius=0.05,color=PINK)
                dot1.move_to(np.array([j,(1-j**n)**(1/n),0]))
                dot1_2.move_to(np.array([(1-j**n)**(1/n),j,0]))
                #self.add(dot1,dot1_2)
                #self.wait(0.05)
                D.append(dot1)
                D.append(dot1_2)
                j=j+dj
            j=1
            while j>0:
                dot2 = Dot(radius=0.05,color=PINK)
                dot2_2 = Dot(radius=0.05,color=PINK)
                dot2.move_to(np.array([j,-(1-j**n)**(1/n),0]))
                dot2_2.move_to(np.array([-(1-j**n)**(1/n),j,0]))
                #self.add(dot2,dot2_2)
                #self.wait(0.05)
                D.append(dot2)
                D.append(dot2_2)
                j=j-dj
            j=0
            while j>-1:
                dot3 = Dot(radius=0.05,color=PINK)
                dot3_2 = Dot(radius=0.05,color=PINK)
                dot3.move_to(np.array([j,-(1-(-j)**n)**(1/n),0]))
                dot3_2.move_to(np.array([-(1-(-j)**n)**(1/n),j,0]))
                #self.add(dot3,dot3_2)
                #self.wait(0.05)
                D.append(dot3)
                D.append(dot3_2)
                j=j-dj
            j=-1
            while j<0:
                dot4 = Dot(radius=0.05,color=PINK)
                dot4_2 = Dot(radius=0.05,color=PINK)
                dot4.move_to(np.array([j,(1-(-j)**n)**(1/n),0]))
                dot4_2.move_to(np.array([(1-(-j)**n)**(1/n),j,0]))
                #self.add(dot4,dot4_2)
                #self.wait(0.05)
                D.append(dot4)
                D.append(dot4_2)
                j=j+dj
            puntos = VGroup(*D)
            self.add(puntos)
            self.wait(0.5)
            for i in D:
                self.remove(i)
            self.remove(valor_sig)
            n=round(n + 0.2, 1)
        self.remove(plano,Group3,fig3)
        
        conclus1 = TextMobject("Vemos que tiende al ``c\\'{i}rculo'' que resulta de usar")
        conclus2 = TextMobject("la norma infinito, de ah\\'{i} su nombre.").next_to(conclus1,DOWN)
        conclus = VGroup(conclus1,conclus2)
        ejer = TextMobject("Puedes cambiar el código para verlo con más valores de $p$")

        self.play(Write(ejer))
        self.wait(2)
        self.play(FadeOut(ejer))
        self.play(Write(conclus))
        self.wait(2)
        self.play(FadeOut(conclus))