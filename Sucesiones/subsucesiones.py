from manimlib.imports import *

###################################
####     SUBSUCESIONES      #####
###################################

class Subsucesiones(MovingCameraScene,Scene):
    def setup(self):
        Scene.setup(self)
        MovingCameraScene.setup(self)
    def construct(self):
        plano = NumberPlane()
        title = TextMobject('''Subsucesiones''').set_color(YELLOW).scale(1.5)
        text2 = TexMobject(r"\text{1) }", r"\forall j\in\mathbb{N},", r"x_{k_j}", r"\in", r"\{X_k\}")
        text2[2].set_color(GREEN)
        text2[4].set_color(ORANGE)
        text1_1=TexMobject(r"\text{Considera una sucesión }", r"\{X_k\}", r"\text{, decimos que}")
        text1_2=TexMobject(r"\{X_{k_j}\}", r"\text{ es una subsucesión de }", r"\{X_k\}", r"\text{ si}").next_to(text1_1,DOWN)
        text1_1[1].set_color(ORANGE)
        text1_2[2].set_color(ORANGE)
        text1_2[0].set_color(GREEN)
        text1=VGroup(text1_1,text1_2).next_to(text2,UP)
        text3 = TextMobject('''2) Si $j<l$, entonces $k_j<k_l$''').next_to(text2,DOWN)
        text4 = TexMobject(r"\text{Considera la sucesión }", r"\{X_k\}", r"=\left(\dfrac{k}{5},\dfrac{k}{5}\right)")
        text4[1].set_color(YELLOW)

        self.play(Write(title))
        self.wait()
        self.play(ReplacementTransform(title,text1))
        self.wait(6)
        self.play(Write(text2))
        self.wait(1)
        self.play(Write(text3))
        self.wait(3)
        self.play(FadeOut(text1),FadeOut(text3),ReplacementTransform(text2,text4))
        self.wait(1.5)
        self.play(FadeOut(text4))
        self.wait(6)
        self.play(ShowCreation(plano))

        suce = []
        sub = []
        for n in range(1,21):
            x_n = Dot(point=((n/5,n/5,0)),color=YELLOW)
            x_n_label = TexMobject("x_{"+str(n)+"}",color=WHITE).scale(0.6).next_to(x_n,DOWN)
            x_n_label.shift(0.1*UP)
            x_n_label.bg = SurroundingRectangle(x_n_label,color=WHITE,fill_color=BLACK,fill_opacity=1)
            x_n_label_group = VGroup(x_n_label.bg,x_n_label)
            self.add(x_n,x_n_label_group)
            self.wait(0.2)
            self.remove(x_n_label_group)
            suce.append(x_n)
        sucesion = VGroup(*suce)
        self.wait()

        text5 = TexMobject(r"\text{Si consideramos ahora la subsucesión }", r"\{X_{k_j}\}", r"=\left(\dfrac{2j}{5},\dfrac{2j}{5})",color=WHITE).shift(3*DOWN) 
        text5[1].set_color(PINK)
        text5.bg = SurroundingRectangle(text5,color=WHITE,fill_color=BLACK,fill_opacity=1)
        text5.group = VGroup(text5.bg,text5)

        self.play(FadeIn(text5.group))

        for j in range(1,11):
            x_n_j = Dot(point=((2*j/5,2*j/5,0)),color=PINK)
            x_n_j_label = TexMobject("x_{k_"+str(j)+"}",color=WHITE).scale(0.6).next_to(x_n_j,DOWN) #CAMBIO DE ÍNDICES.
            x_n_j_label.shift(0.1*UP)
            x_n_j_label.bg = SurroundingRectangle(x_n_j_label,color=WHITE,fill_color=BLACK,fill_opacity=1)
            x_n_j_label.group = VGroup(x_n_j_label.bg,x_n_j_label)
            self.add(x_n_j,x_n_j_label.group)
            self.wait(0.5)
            self.remove(x_n_j_label.group)
            sub.append(x_n_j)
        subsucesion = VGroup(*sub)
        self.wait()

        text6 = TexMobject(r"\text{Claramente se cumple que para toda } j\in\mathbb{N},", r"x_{k_j}", r"\in", r"\{X_k\}",color=WHITE).shift(3*DOWN)
        text6[1].set_color(PINK)
        text6[3].set_color(YELLOW)
        text6.bg = SurroundingRectangle(text6,color=WHITE,fill_color=BLACK,fill_opacity=1)
        text6.group = VGroup(text6.bg,text6)

        text7_1=TexMobject(r"\text{Notemos que los términos 2 y 4 de la subsucesión }", r"\{X_{k_j}\}",color=WHITE)
        text7_2=TexMobject(r"\text{coinciden con los términos 4 y 8 de la sucesión }", r"\{X_k\}",color=WHITE).next_to(text7_1,DOWN)
        text7_1[1].set_color(PINK)
        text7_2[1].set_color(YELLOW)
        text7=VGroup(text7_1,text7_2)
        text7.shift(3*DOWN).scale(0.8)
       
        text7.bg = SurroundingRectangle(text7,color=WHITE,fill_color=BLACK,fill_opacity=1)
        text7.group = VGroup(text7.bg,text7)

        punto_1 = Dot(point=((4/5,4/5,0)),color=RED,radius=0.15)
        punto_1_label = TexMobject("x_4,\\ x_{k_2}",color=WHITE).scale(0.6).next_to(punto_1,DOWN)
        punto_1_label.bg = SurroundingRectangle(punto_1_label,color=WHITE,fill_color=BLACK,fill_opacity=1)
        punto_1_label.group = VGroup(punto_1_label.bg,punto_1_label)
        punto_2 = Dot(point=((8/5,8/5,0)),color=RED,radius=0.15)
        punto_2_label = TexMobject("x_8,\\ x_{k_4}",color=WHITE).scale(0.6).next_to(punto_2,DOWN)
        punto_2_label.bg = SurroundingRectangle(punto_2_label,color=WHITE,fill_color=BLACK,fill_opacity=1)
        punto_2_label.group = VGroup(punto_2_label.bg,punto_2_label)
        puntos = VGroup(punto_1_label.group,punto_2_label.group)

        text8 = TextMobject('''Veamos que con $j=2$ y $l=4$, tenemos $k_j=4$ y $k_l=8$. \n
                            Con esto, se cumple que: $j<l\\Rightarrow k_j<k_l$; así, \n
                            ¿cómo puedes demostrar que en efecto es subsucesión?''',color=WHITE).shift(3*DOWN).scale(0.8)
        text8.bg = SurroundingRectangle(text8,color=WHITE,fill_color=BLACK,fill_opacity=1)
        text8.group = VGroup(text8.bg,text8)

        text9_1=TexMobject(r"\text{Si en la sucesión }", r"\{X_{k_j}\}", r"\text{ apareciera primero }", r"x_{k_8}", r"\text{ y después }", r"x_{k_4},",color=WHITE)
        text9_2=TexMobject(r"\text{ya no sería una subsucesión de }", r"\{X_k\}", r"\text{; basta que una pareja no cumpla}",color=WHITE).next_to(text9_1,DOWN)
        text9_3=TexMobject(r"\text{el orden requerido para que no sea subsucesión.}",color=WHITE).next_to(text9_2,DOWN)
        text9_1[1].set_color(PINK)
        text9_2[1].set_color(YELLOW)
        text9=VGroup(text9_1,text9_2,text9_3).shift(2*DOWN).scale(0.8)

        text9.bg = SurroundingRectangle(text9,color=WHITE,fill_color=BLACK,fill_opacity=1)
        text9.group = VGroup(text9.bg,text9)

        self.play(ReplacementTransform(text5.group,text6.group))
        self.wait(6)
        self.play(ReplacementTransform(text6.group,text7.group))
        self.wait(8)
        self.play(Write(punto_1),Write(punto_2),FadeIn(puntos))
        self.wait()
        self.play(ReplacementTransform(text7.group,text8.group))
        self.wait(16)
        self.play(ReplacementTransform(text8.group,text9.group))
        self.wait(16)