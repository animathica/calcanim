from manimlib.imports import *

#############################################
#### DEFiNICIÓN DE LÍMITE DE SUCESIONES #####
##############################################

class Definicion_Limite_Sucesiones(MovingCameraScene, Scene):
    def setup(self):
        Scene.setup(self)
        MovingCameraScene.setup(self)

    def construct(self):
        titulo=TextMobject('''Límite de sucesiones.''').scale(1.5)
        definicion = TextMobject('''Definición:''')
        def_1 = TexMobject('\\lim_{n\\rightarrow\\infty}\\vec{x}_n = \\vec{x}_0')
        def_2 = TexMobject('\\Leftrightarrow')
        def_3 = TexMobject(
            '\\forall r>0 \ \\exists \ N\\in \\mathbb{N} \ tq \ \\forall n>N \ \\vec{x} \\in \\mathbb{B}_{r}(\\vec{x}_0)')

        def_1.move_to((0, 1, 0))
        def_2.move_to((0, 0, 0))
        def_3.move_to((0, -1, 0))
        definicion.move_to((0,2.2,0))

        gpo_1 = VGroup(definicion,def_1, def_2, def_3)

        text_1 = TextMobject(r"\text{Pero... \textquestiondown qu\'{e} nos dice geom\'{e}tricamente esta definici\'{o}n?}")

        grid = NumberPlane()

        text_2 = TexMobject(r"\text{Consideremos la siguiente sucesión en el plano: }", r"\vec{x}_n=(\frac{1}{n}, \frac{1}{n})",color=WHITE).scale(0.5).to_edge(LEFT+2*UP)

        text_3 = TexMobject(r"\text{Recuerda que es una funci\'{o}n de }", r"\mathbb{N}\rightarrow\mathbb{R}^{2}",color=WHITE).next_to(text_2,0.5*DOWN).scale(0.5)

        text_3_1 = TexMobject(r"\text{Supongamos que queremos probar que el l\'{i}mite es el vector }", r"(0,0).}",color=WHITE).next_to(text_3,0.7*DOWN).scale(0.5)

        text_2[1].set_color(ORANGE)
        text_3[1].set_color(ORANGE)
        text_3_1[1].set_color(ORANGE)

        text_c = VGroup(text_2,text_3,text_3_1)

        text_c.bg = SurroundingRectangle(text_c, color=WHITE, fill_color=BLACK, fill_opacity=1)

        gpo_2 = VGroup(text_c.bg,text_c)

        puntos_objetos = []
        puntos_objetos_1 = []

        for i in cjto_pts_sucesion:
            punto_i = Dot(point=i, radius=0.025)
            punto_i_1 = Dot(point=i, radius=0.001)
            puntos_objetos.append(punto_i)
            puntos_objetos_1.append(punto_i_1)

        gpo_4 = VGroup(*puntos_objetos)
        gpo_4_1 = VGroup(*puntos_objetos_1)

        circulo = Circle(radius=0.5)
        circulo_t = TextMobject(r"\text{Entonces damos a la bola de radio \'{e}psilon...}" , '''($\\epsilon$)''') \
            .set_color(RED) \
            .move_to((-0.55, -0.8, 0))

        radio = Brace(circulo, RIGHT)
        radio_t = TextMobject('$2\\epsilon$') \
            .next_to(radio.get_center(), RIGHT, buff=0.2)

        text_4_1 = TexMobject(r"\text{Recordando de la definición: }", r"\forall r >0 \exists N \in \mathbb{N} \text{ tq. } \forall n > N, \vec{x} \in \mathbb{B}_{r}(\vec{x}_0),",color=WHITE)
        text_4_2 = TexMobject(r"\text{en este caso }", r"\vec{x}_0=(0,0)",color=WHITE).next_to(text_4_1,DOWN)
        text_4_1[1].set_color(ORANGE)
        text_4_2[1].set_color(ORANGE)
        text_4 =VGroup(text_4_1,text_4_2)
        text_4.bg = SurroundingRectangle(text_4, color=WHITE, fill_color=BLACK, fill_opacity=1)

        gpo_5 = VGroup(text_4.bg, text_4).scale(0.4) \
            .move_to((0, -1, 0))

        text_5=TextMobject('''Esta $N$ debe ser tal que todos los elementos de la sucesión \n
                                inmediatos después del $N$-ésimo elemento, están dentro \n
                                de la bola de radio r ''')
        text_5.bg = SurroundingRectangle(text_5, color=WHITE, fill_color=BLACK, fill_opacity=1)

        gpo_6 = VGroup(text_5.bg, text_5).scale(0.4) \
            .move_to((0, -1.25, 0))

        N_esimo_pto = Dot(point=gpo_4[14].get_center(), radius=0.01, color=YELLOW)
        N_m_u_esimo_pto = Dot(point=gpo_4[13].get_center(), radius=0.01, color=YELLOW)

        text_6 = TextMobject('''Nota cómo estos dos puntos podrían ser el $N$-ésimo, \n
                                ya que todos los siguientes puntos de la sucesión \n
                                están dentro de la bola de radio r ''')
        
        text_6.bg = SurroundingRectangle(text_6, color=WHITE, fill_color=BLACK, fill_opacity=1)

        gpo_7 = VGroup(text_6.bg, text_6).scale(0.04) \
            .move_to((1 / (2 * np.sqrt(2)), 1 / (2 * np.sqrt(2)) + 0.07, 0))

        dentro_bola_antes_dentro = [i for i in puntos_objetos_1[15:]]
        dentro_bola_despues_dentro = [Dot(point=i.get_center(), radius=0.01, color=BLUE) for i in puntos_objetos_1[15:]]
        dentro_bola_antes_fuera = [i for i in puntos_objetos_1[0:13]]
        dentro_bola_despues_fuera = [Dot(point=i.get_center(), radius=0.01, color=ORANGE) for i in
                                     puntos_objetos_1[0:13]]

        dentro_bola_g_antes_dentro = VGroup(*dentro_bola_antes_dentro)
        dentro_bola_g_despues_dentro = VGroup(*dentro_bola_despues_dentro)
        dentro_bola_g_antes_fuera = VGroup(*dentro_bola_antes_fuera)
        dentro_bola_g_despues_fuera = VGroup(*dentro_bola_despues_fuera)


        text_7 = TextMobject('''Por último, nota cómo hay solamente una cantidad finita \n
                                fuera de la bola y una cantidad infinita numerable dentro \n
                                de la bola, ¿cómo puedes probar esto?''')

        text_7.bg = SurroundingRectangle(text_7, color=WHITE, fill_color=BLACK, fill_opacity=10)

        gpo_8 = VGroup(text_7.bg, text_7).scale(0.25) \
            .move_to((0, 1.5, 0))

        ###animación
        self.play(Write(titulo))
        self.wait(1.5)
        self.play(FadeOut(titulo))
        self.play(Write(gpo_1))
        self.wait(15)
        self.play(ReplacementTransform(gpo_1, text_1))
        self.wait()
        self.play(FadeOut(text_1))
        self.wait()
        self.play(Write(grid))
        self.wait()
        #### aquí se empiezan a poner las cajitas
        self.play(Write(gpo_2))
        self.wait(11)
        self.play(Write(gpo_4), run_time=3)
        self.wait()
       
       
       #entoces damos la bola ...
        self.play(Write(circulo_t))
        self.wait()
        self.play(FadeOut(circulo_t),
                  self.camera_frame.scale, 0.25,
                  self.camera_frame.move_to, (0, 0, 0))
        self.wait()
        self.play(Write(circulo), )
        self.wait()
        self.play(Write(radio), Write(radio_t))
        self.wait()
        self.play(FadeOut(radio), FadeOut(radio_t))
        self.wait()
        self.play(FadeOut(gpo_2))
        self.play(self.camera_frame.scale, 2)
        self.wait()
        self.play(Write(gpo_5))
        self.wait(7)
        self.play(ReplacementTransform(gpo_5, gpo_6))
        self.wait(5.5)
        self.play(FadeOut(gpo_6), self.camera_frame.scale, 0.075
                  , self.camera_frame.move_to, (0.35, 0.35, 0)
                  , ReplacementTransform(gpo_4, gpo_4_1))
        self.wait()
        self.play(ReplacementTransform(gpo_4_1[14], N_esimo_pto),
                  ReplacementTransform(gpo_4_1[13], N_m_u_esimo_pto))
        self.wait()
        self.play(Write(gpo_7))
        self.wait(9)
        self.play(self.camera_frame.scale, 10, FadeOut(gpo_7))
        self.play(ReplacementTransform(dentro_bola_g_antes_dentro, dentro_bola_g_despues_dentro),
                  )
        self.wait()
        self.play(Write(gpo_8))
        self.wait(11)
        self.play(ReplacementTransform(dentro_bola_g_antes_fuera, dentro_bola_g_despues_fuera))
        self.wait(5)
        self.play(FadeOut(gpo_8),FadeOut(grid),FadeOut(circulo),FadeOut(dentro_bola_g_despues_fuera),
                    FadeOut(dentro_bola_g_despues_dentro),FadeOut(N_esimo_pto),FadeOut(N_m_u_esimo_pto))