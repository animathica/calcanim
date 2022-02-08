from manimlib.imports import *

##########################################
#### TEOREMA DE RECTÁNGULOS ANIDADOS #####
##########################################

#Definimos un Dot con métodos específicos para la escena de RectangulosAnidados
class BCustomDot(Dot):
    def custom_method(self, color):
        self.set_color(color)
        self.scale(5)
        return self

    def other_method(self):
        self.scale(1/7)
        return self
    
class RectangulosAnidados(Scene):
    def construct(self):
        titulo= TextMobject(r"El Teorema de los", r" Rectángulos Anidados").scale(1.2)
        titulo[1].set_color(ORANGE)
        
        #Definición de un rectángulo 
        def_rect_a = TexMobject(r"\text{Dados los intervalos cerrados } I_i=[a_i,b_i],\ a_i\leq b_i\ \forall i \in (1...n)").scale(0.9).shift(2*UP)
        def_rect_b = TextMobject(r"definimos un", r" rectángulo", r" en", " $\\mathbb{R}^n$", r" de la siguiente forma:").scale(0.9).shift(UP)
        def_rect_b[1].set_color(ORANGE)
        def_rect_b[3].set_color(ORANGE)
        def_rect_c = TexMobject(r"R = [a_1,b_1]\times[a_2,b_2]\times ... \times[a_n,b_n]").next_to(def_rect_b,1.5*DOWN).scale(0.9).set_color(ORANGE)
        def_rect_d = TextMobject(r"y su", r" diagonal", r" como:").next_to(def_rect_c,1.5*DOWN).scale(0.9)
        def_rect_d[1].set_color(YELLOW)
        def_rect_e = TexMobject(r"diag(R) = \Vert (b_1,b_2,...,b_n)-(a_1,a_2,...,a_n) \Vert").next_to(def_rect_d,1.5*DOWN).scale(0.9).set_color(YELLOW)
        def_rect = VGroup(def_rect_a,def_rect_b,def_rect_c, def_rect_d, def_rect_e)
        #Rectángulo en R2
        enr2 = TextMobject("Visualicemos lo anterior en $\\mathbb{R}^2$").to_edge(UP)  
        ab_eje_x = VGroup(TexMobject(r"a_1").shift(2.3*LEFT),TexMobject(r"b_1").shift(2.3*RIGHT))
        ab_eje_y = VGroup(TexMobject(r"a_2").shift(2.3*DOWN),TexMobject(r"b_2").shift(2.3*UP))
        linea_ejex = DashedLine(start = (-2,0,0), end = (2,0,0))
        linea_ejey = DashedLine(start = (0,-2,0), end = (0,2,0))
        ejes = VGroup(ab_eje_x,ab_eje_y,linea_ejex,linea_ejey)
        #Ejes y rectángulo
        text_R = TexMobject(r"R = [a_1,b_1]\times[a_2,b_2]").move_to(enr2).set_color(ORANGE)
        text_diagR = TexMobject(r"diag(R) = \Vert (b_1,b_2)-(a_1,a_2) \Vert").move_to(enr2).set_color(YELLOW)

        R = Square(side_length = 4.0, color = ORANGE)
        R.set_fill(ORANGE, opacity=0.5)
        diagR = DoubleArrow(start = (2,2,0), end = (-2,-2,0), stroke_width = 2, color=YELLOW).scale(1.1)
        diagR.set_fill(YELLOW, opacity=0.5)

        al_teorema = TextMobject('''Procedamos a enunciar \n
                                 el teorema: ''').shift(3*RIGHT)
        #Teorema
        teo_1a = TextMobject(r"Sea", " $\{R_k\}$", r" una sucesión").shift(3*RIGHT+2*UP)
        teo_1a[1].set_color(ORANGE)
        teo_1b = TextMobject("de rectángulos anidados").next_to(teo_1a,DOWN)
        teo_1c = TexMobject(r"(R_{k+1} \subset R_k \ \forall k \in \mathbb{N})").next_to(teo_1b,2*DOWN).set_color(RED)
        teo_1 = VGroup(teo_1a, teo_1b, teo_1c)


        ## Secuencia de rectángulos anidados (construye la tuya!)
        color_seq = [ORANGE, YELLOW, BLUE , GREEN, PINK, RED]
        rec_seq = []
        for i in range (2,50):
            rec_seq.append(Square(side_length = 4/i, color = color_seq[i % 6]).set_fill(color_seq[i % 5],\
                 opacity=0.3).shift(3*LEFT))
        rect_group = VGroup(*rec_seq)

        teo_2a = TextMobject("Si además, se tiene que").move_to(teo_1a)
        teo_2b = TexMobject(r"\lim_{k\to \infty}diag(R_k) = 0").next_to(teo_2a,DOWN).set_color(YELLOW)
        teo_2 = VGroup(teo_2a,teo_2b)

        ## Sequencia de diagonales
        diag_seq =  []
        for i in range(1, 50):
            diag_seq.append(DoubleArrow(start = (2/i,2/i,0), end = (-2/i,-2/i,0),tip_length = 0.2, stroke_width = 2, color = YELLOW ).scale(1.1).shift(3*LEFT))
        diag_group = VGroup(*diag_seq)

        conclu_a = TextMobject("Entonces,").move_to(teo_1b)
        conclu_b = TexMobject(r"\cap_{k=1}^{\infty}R_k = \{\vec{x}_0\}").next_to(conclu_a,DOWN).set_color(ORANGE)
        conclu = VGroup(conclu_a,conclu_b).shift(2*DOWN)
        x0 = BCustomDot().shift(3*LEFT)

        #Ojo: Esta parte puede causar problemas por el "¿"
        puedes = TextMobject("¿Puedes hacer otra sucesión de rectángulos anidados?").shift(UP)
        otra_pregunta = TextMobject("¿Qué pasa si los intervalos no son cerrados?").shift(DOWN)

        #Secuencia de animación: Rectángulos anidados
        self.play(Write(titulo))
        self.wait()
        self.play(FadeOut(titulo))
        self.play(Write(def_rect_a))
        self.wait()
        self.play(Write(def_rect_b))
        self.wait()
        self.play(Write(def_rect_c))
        self.wait()
        self.play(Write(def_rect_d),Write(def_rect_e))
        self.wait(3)
        self.play(FadeOut(def_rect))
        self.wait()
        self.play(Write(enr2))
        self.wait()
        self.play(ShowCreation(ejes))
        self.play(ReplacementTransform(enr2,text_R))
        self.wait()
        self.play(ShowCreation(R, run_time = 2.0))
        self.wait(1.8)
        self.play(ReplacementTransform(text_R,text_diagR))
        self.wait()
        self.play(ShowCreation(diagR))
        self.wait()
        self.play(FadeOut(diagR))
        self.play(ejes.shift, 3*LEFT, R.shift, 3*LEFT)
        self.play(ReplacementTransform(text_diagR,al_teorema))
        self.wait(3)
        self.play(FadeOut(al_teorema))
        self.play(Write(teo_1))
        self.wait()
        self.play(ShowIncreasingSubsets(rect_group, run_time=4.0))
        self.wait()
        self.play(FadeOut(teo_1))
        self.wait()
        self.play(Write(teo_2))
        self.wait()
        self.play(ShowIncreasingSubsets(diag_group, run_time=4.0))
        self.wait()
        self.play(Write(conclu))
        self.play(FadeOut(diag_group))
        self.play(ApplyMethod(x0.custom_method, WHITE))
        self.play(ApplyMethod(x0.other_method))
        self.wait(2)
        self.play(FadeOut(teo_2),FadeOut(conclu), FadeOut(ejes), FadeOut(R), FadeOut(rect_group),\
            FadeOut(x0))
        self.play(Write(puedes))
        self.wait()
        self.play(Write(otra_pregunta))
        self.wait(2)
        self.play(FadeOut(puedes),FadeOut(otra_pregunta))