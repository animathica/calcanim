from manimlib.imports import *

## Grid para algunas de las animaciones

class Grid(VGroup):
    CONFIG = {
        "height": 6.0,
        "width": 6.0,
    }

    def __init__(self, rows, columns, **kwargs):
        digest_config(self, kwargs, locals())
        super().__init__(**kwargs)

        x_step = self.width / self.columns
        y_step = self.height / self.rows

        for x in np.arange(0, self.width + x_step, x_step):
            self.add(Line(
                [x - self.width / 2., -self.height / 2., 0],
                [x - self.width / 2., self.height / 2., 0],
            ))
        for y in np.arange(0, self.height + y_step, y_step):
            self.add(Line(
                [-self.width / 2., y - self.height / 2., 0],
                [self.width / 2., y - self.height / 2., 0]
            ))

class ScreenGrid(VGroup):
    CONFIG = {
        "rows": 8,
        "columns": 14,
        "height": FRAME_Y_RADIUS * 2,
        "width": 14,
        "grid_stroke": 0.5,
        "grid_color": WHITE,
        "axis_color": RED,
        "axis_stroke": 2,
        "labels_scale": 0.25,
        "labels_buff": 0,
        "number_decimals": 2
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        rows = self.rows
        columns = self.columns
        grid = Grid(width=self.width, height=self.height, rows=rows, columns=columns)
        grid.set_stroke(self.grid_color, self.grid_stroke)

        vector_ii = ORIGIN + np.array((- self.width / 2, - self.height / 2, 0))
        vector_si = ORIGIN + np.array((- self.width / 2, self.height / 2, 0))
        vector_sd = ORIGIN + np.array((self.width / 2, self.height / 2, 0))

        axes_x = Line(LEFT * self.width / 2, RIGHT * self.width / 2)
        axes_y = Line(DOWN * self.height / 2, UP * self.height / 2)

        axes = VGroup(axes_x, axes_y).set_stroke(self.axis_color, self.axis_stroke)

        divisions_x = self.width / columns
        divisions_y = self.height / rows

        directions_buff_x = [UP, DOWN]
        directions_buff_y = [RIGHT, LEFT]
        dd_buff = [directions_buff_x, directions_buff_y]
        vectors_init_x = [vector_ii, vector_si]
        vectors_init_y = [vector_si, vector_sd]
        vectors_init = [vectors_init_x, vectors_init_y]
        divisions = [divisions_x, divisions_y]
        orientations = [RIGHT, DOWN]
        labels = VGroup()
        set_changes = zip([columns, rows], divisions, orientations, [0, 1], vectors_init, dd_buff)
        for c_and_r, division, orientation, coord, vi_c, d_buff in set_changes:
            for i in range(1, c_and_r):
                for v_i, directions_buff in zip(vi_c, d_buff):
                    ubication = v_i + orientation * division * i
                    coord_point = round(ubication[coord], self.number_decimals)
                    label = Text(f"{coord_point}",font="Arial",stroke_width=0).scale(self.labels_scale)
                    label.next_to(ubication, directions_buff, buff=self.labels_buff)
                    labels.add(label)

        self.add(grid, axes, labels)

#Define la sucesión mostrada en Definicion_Sucesiones y Definicion_Limite_Sucesiones:
n_sup = 150
cjto_pts_sucesion = []

for i in range(1,n_sup):
    x = 1/(0.2*i)
    y = 1/(0.2*i)
    cjto_pts_sucesion.append((x,y,0))

n_sup_1 = 30
cjto_pts_sucesion_1 = []
for i in range(1,n_sup_1):
    x_1 = (np.exp(i/20))*(np.cos(0.7*i))
    y_1 = (np.exp(i/20))*(np.sin(0.7*i))
    cjto_pts_sucesion_1.append((x_1,y_1,0))

###################################
#### DEFINICIÓN DE SUCESIONES #####
###################################
    
class Definicion_Sucesiones(Scene):
    def construct(self):

        ##texto:
        t_1 = TextMobject(''' \\textquestiondown Recuerdas la definici\\'{o}n de sucesiones en $\\mathbb{R}?$ ''')
        t_2 = TextMobject('''Una sucesi\\'{o}n es una funci\\'{o}n de: \n
                            $\\mathbb{N}\\rightarrow\\mathbb{R}$ ''')
        t_3 = TextMobject('''Nota que es distinto hablar del conjunto \n
                            que contiene a todos los \n
                            elementos de dicha sucesi\\'{o}n:\n
                            $\{ x_n \}$, \n
                            donde $x_n = s(n)$ y \n
                            donde $s$ es la funci\\'{o}n.''')
        t_4 = TextMobject(''' \\textexclamdown Bueno! Pues es an\\'{a}logo para \n
                            sucesiones de $\\mathbb{R}^n$. ''')
        t_5 = TextMobject('''Recuerda que un vector en $\\mathbb{R}^n$, \n
                            se ve de la siguiente forma: \n
                            $(x_1,x_2,\\dots,x_n)$, donde $x_i\\in \\mathbb{R}$, \n
                            para cualquier $i\\in \{ 1,\\dots, n \}$''')
        t_6 = TextMobject('''Por lo que para definir una sucesi\\'{o}n \n
                            en $\\mathbb{R}^n$  \n
                            basta definir una sucesi\\'{o}n para \n
                            cada entrada vectorial, es decir: \n
                            $\\vec{s}: \\mathbb{N}\\rightarrow \\mathbb{R}^n$ ''')
        t_7 = TextMobject('''O sea que: \n
                            $\\vec{s}(n) = (s_1(n),s_2(n),\\dots, s_n(n))$ \n
                            Donde $s_i$ es una sucesi\\'{o}n en $\\mathbb{R}$.''')
        t_8 = TextMobject('''Por ejemplo en $\\mathbb{R}^2$, tomemos: \n
                            $\\vec{s}(n) = ((e^{-n})\\cos(n),(e^{-n})\\sin(n))$''')
        t_9 = TextMobject('''Pintemos las parejas de la sucesi\\'{o}n en el plano:''')



        ##mas
        grid = NumberPlane()
        Elementos = [Dot(point=i).set_color(RED_E) for i in cjto_pts_sucesion_1]
        Elementos_Y = [Dot(point=i).set_color(YELLOW_E) for i in cjto_pts_sucesion_1]

        Elementos_t = [TexMobject('\\vec{s}_{%i}' % i).next_to(Elementos[i], 0.08*DOWN).set_color(YELLOW_E) for i in range(0, n_sup_1 - 1)]

        Elementos_g = VGroup(*Elementos)
        Elementos_g_Y = VGroup(*Elementos_Y)
        Elementos_t_g = VGroup(*Elementos_t)



        ##animación:
        self.play(Write(t_1))
        self.wait(2.2)
        self.play(ReplacementTransform(t_1, t_2))
        self.wait(4.3)
        self.play(ReplacementTransform(t_2, t_3))
        self.wait(11.5)
        self.play(ReplacementTransform(t_3, t_4))
        self.wait(6)
        self.play(ReplacementTransform(t_4, t_5))
        self.wait(13)
        self.play(ReplacementTransform(t_5, t_6))
        self.wait(13)
        self.play(ReplacementTransform(t_6, t_7))
        self.wait(10)
        self.play(ReplacementTransform(t_7, t_8))
        self.wait(12)
        self.play(ReplacementTransform(t_8, t_9))
        self.wait(4)
        self.play(ReplacementTransform(t_9, grid))
        self.wait()
        self.play(Write(Elementos_g),
                  Write(Elementos_t_g), run_time=6.35)
        self.wait()
        self.play(FadeOut(Elementos_t_g), ReplacementTransform(Elementos_g, Elementos_g_Y))
        self.wait(3.5)
        self.play(FadeOut(grid),FadeOut(Elementos_g_Y))
    
###################################
#### DEF LÍMITE DE SUCESIONES #####
###################################

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


###################################
####     TEOREMA PUENTE      #####
###################################

class Teo_Puente(Scene):
    def construct(self):

        plano = NumberPlane()

        title = TextMobject('''Teorema Puente''')
        title.scale(1.2)
        title.set_color(YELLOW)
        intro = TextMobject('''El teorema dice:''').shift(2 * UP)
        teo1 = TexMobject(
            r'''\text{Sea } \{X_n\}\subset\mathbb{R}^m\text{ sucesi\'{o}n. } \forall k\in\{1,...,m\} \lim_{n\to\infty}X_{n,k}=L_k''')
        teo2 = TexMobject(r'''\Longleftrightarrow \lim_{n\to\infty} X_{n}=L=(L_1,...,L_k,...,L_m)''')
        teo2.next_to(teo1, DOWN)
        teo = VGroup(teo1, teo2)
        ejemplos = TextMobject("Veamos algunos ejemplos de su aplicación")



        ## Primer ejemplo ##

        ejem1 = TexMobject(r'''X_n=\left(\frac{6}{n},0\right)''').shift(1.5 * UP)
        desc1 = TexMobject(r'''\Rightarrow X_{n,1}=\frac{6}{n}\quad X_{n,2}=0''')
        teoapl1 = TexMobject(
            r'''\lim_{n\to\infty}\frac{6}{n}=0,\ \lim_{n\to\infty}0=0\Rightarrow\lim_{n\to\infty}X_n=(0,0)''').shift(
            1.5 * DOWN)
        vis = TextMobject('''Veamos esta sucesi\\'{o}n''')
        ejem1.set_color(RED)
        ejem1.bg = SurroundingRectangle(ejem1, color=RED, fill_color=BLACK,
                                         fill_opacity=1)
        Group11 = VGroup(ejem1.bg, ejem1)



        suce1 = []
        for n in range(1, 101):
            x_n = Dot(point=np.array([6 / n, 0, 0]), radius=0.05, color=RED)
            suce1.append(x_n)
        sucesion1 = VGroup(*suce1)



        ## Segundo ejemplo ##

        ejem2 = TexMobject(r'''X_n  =\left(\frac{n}{10},\frac{1}{n}\right)''').shift(1.5 * UP)
        desc2 = TexMobject(r'''\Rightarrow X_{n,1}=\frac{n}{10}\quad X_{n,2}=\frac{1}{n}''')
        teoapl2 = TexMobject(
            r'''\nexists\lim_{n\to\infty}\frac{n}{10} \Rightarrow \nexists\lim_{n\to\infty}X_n''').shift(1.5 * DOWN)
        vis = TextMobject('''Veamos esta sucesi\\'{o}n''')
        ejem2.set_color(YELLOW_E)
        ejem2.bg = SurroundingRectangle(ejem2, color=YELLOW_E, fill_color=BLACK,
                                        fill_opacity=1)
        Group12 = VGroup(ejem2.bg, ejem2)



        suce2 = []
        for n in range(1, 101):
            x_n = Dot(point=np.array([n / 10, 1 / n, 0]), radius=0.05, color=YELLOW_E)
            suce2.append(x_n)
        sucesion2 = VGroup(*suce2)



        ## Desaf\\'{i}o ##

        desa1 = TextMobject('''Es tu turno de usar el teorema''')
        desa2 = TextMobject('''Demuestra el valor del l\\'{i}mite de la siguiente sucesi\\'{o}n. Usa \n 
                                la definici\\'{o}n e int\\'{e}ntalo despu\\'{e}s usando el teorema puente:''').shift(UP)
        desa = TexMobject(r'''X_n=\left(6\frac{(-1)^n}{n},\frac{4}{n}\right)''').shift(DOWN)
        desa.set_color(ORANGE)
        desa.bg = SurroundingRectangle(desa, color=ORANGE, fill_color=BLACK,
                                        fill_opacity=1)
        Group13 = VGroup(desa.bg, desa)



        suce5 = []
        for n in range(1, 101):
            x_n = Dot(point=np.array([6 * (-1) ** n / n, 4 / n, 0]), radius=0.05, color=ORANGE)
            suce5.append(x_n)
        sucesion5 = VGroup(*suce5)



        #animación

        self.play(Write(title))
        self.wait(2)
        self.play(ReplacementTransform(title, intro), Write(teo))
        self.wait(20)
        self.play(FadeOut(intro), FadeOut(teo))
        self.play(Write(ejemplos))
        self.wait(3.2)

        self.play(ReplacementTransform(ejemplos, ejem1))
        self.wait(2.5)
        self.play(Write(desc1))
        self.wait(7)
        self.play(Write(teoapl1))
        self.wait(10)
        self.play(ReplacementTransform(desc1, vis), FadeOut(teoapl1))
        self.wait(2)
        self.play(Transform(ejem1, Group11))
        self.play(ApplyMethod(Group11.to_edge, UP), FadeOut(vis))
        self.add_foreground_mobjects(Group11)

        self.play(ShowCreation(plano), run_time=0.5)
        self.play(Write(sucesion1), run_time=5)
        self.wait(3)
        self.play(FadeOut(Group11), FadeOut(plano), FadeOut(sucesion1))

        self.play(Write(ejem2))
        self.wait(2.5)
        self.play(Write(desc2))
        self.wait(2)
        self.play(Write(teoapl2))
        self.wait(7)
        self.play(ReplacementTransform(desc2, vis), FadeOut(teoapl2))
        self.wait(2)
        self.play(Transform(ejem2, Group12))
        self.play(ApplyMethod(Group12.to_edge, UP), FadeOut(vis))
        self.add_foreground_mobjects(Group12)

        self.play(ShowCreation(plano), run_time=0.5)
        self.play(Write(sucesion2), run_time=5)
        self.wait(3)
        self.play(FadeOut(Group12), FadeOut(plano), FadeOut(sucesion2))

        self.play(Write(desa1))
        self.wait(2.5)
        self.play(FadeOut(desa1), Write(desa2), Write(desa))
        self.wait(15)
        self.play(Transform(desa, Group13))
        self.play(FadeOut(desa2), ApplyMethod(Group13.to_edge, UP))
        self.add_foreground_mobjects(Group13)

        self.play(ShowCreation(plano), run_time=0.5)
        self.play(Write(sucesion5), run_time=5)
        self.wait(4)
        self.play(FadeOut(plano), FadeOut(sucesion5), FadeOut(Group13))

###################################
#### SUCESIONES DE CAUCHY     #####
###################################

#Definimos un Dot con métodos específicos para la escena de Suc. de Cauchy
class ACustomDot(SmallDot):
    def custom_method(self, color):
        self.set_color(color)
        self.scale(5)
        self.scale(3/5)
        return self
    def inverse_method(self):
        self.set_color(GREY)
        self.scale(1/3)
        return self

#define la sucesión para usar definicion_sucesiones y definicion de limite:
n_sup = 150
cjto_pts_sucesion = []

for i in range(1,n_sup):
    x = 1/(0.2*i)
    y = 1/(0.2*i)
    cjto_pts_sucesion.append((x,y,0))

n_sup_1 = 30
cjto_pts_sucesion_1 = []
for i in range(1,n_sup_1):
    x_1 = (np.exp(i/20))*(np.cos(0.7*i))
    y_1 = (np.exp(i/20))*(np.sin(0.7*i))
    cjto_pts_sucesion_1.append((x_1,y_1,0))


class SucesionDeCauchy(MovingCameraScene, Scene):
    # Necesario para que funcione la herencia doble
    def setup(self):
        Scene.setup(self)
        MovingCameraScene.setup(self)
    def construct(self):
        # Primero guardamos el estado original de la cámara
        self.camera_frame.save_state()
        plano = NumberPlane()
        titu = TextMobject("Sucesiones de Cauchy")
        bas1 = TextMobject("Revisemos la definición de una sucesión de Cauchy")
        bas2 = TextMobject("de forma geométrica.").set_color(YELLOW).next_to(bas1,DOWN)
        bas = VGroup(bas1,bas2)
        675
        suc = TexMobject(r"\text{Sea}\ \{x_n\}\ \text{una sucesión}").shift(3*LEFT+UP)
        xn = TexMobject(r"\{x_n\}=\{\frac{1}{n},\frac{1}{n}\}").shift(4*RIGHT+UP)
        # Definición en puntos de la sucesión 
        points = []
        for n in range(1,1500):
            points.append(ACustomDot(point=np.array([10/n, 10/(n), 0.0]), color = GREY).scale(1.2))
        group = VGroup(*points)

        #Definición de los puntos pequeños
        smolpoints = []
        for n in range(1,1500):
            smolpoints.append(ACustomDot(point=np.array([10/n, 10/(n), 0.0]),color = GREY).scale(0.1))
        group2 = VGroup(*smolpoints)
        
        circ_text = TexMobject(r"\text{Consideremos un círculo de diámetro}\ \varepsilon").scale(0.1).shift(0.62*UP)

        circulo1 = Circle(radius = 0.3).move_to(points[50])

        amarillo_t1 = TextMobject("A partir de cierto punto, llamémosle").move_to(circ_text).scale(0.11)
        amarillo_t2 = TexMobject(r"\vec{x}_N").scale(0.09).next_to(amarillo_t1).set_color(YELLOW).shift(0.22*LEFT)
        amarillo = VGroup(amarillo_t1,amarillo_t2)

        posteriores_t1 = TextMobject("cualesquiera dos términos posteriores").move_to(circ_text).scale(0.10).shift(0.1*LEFT)
        posteriores_t2 = TexMobject(r"\vec{x}_k, \vec{x}_l").scale(0.1).next_to(posteriores_t1).set_color(BLUE).shift(0.22*LEFT)
        posteriores_t3 = TexMobject(r"\text{distan entre sí menos que}\ \varepsilon").scale(0.1).next_to(posteriores_t1,0.15*DOWN)
        posteriores = VGroup(posteriores_t1,posteriores_t2,posteriores_t3)

        mates_1 = TexMobject(r"\text{Esto es:}\ \forall\ k,l > N, d(\vec{x}_k,\vec{x}_l)<\varepsilon").move_to(circ_text).scale(0.10).shift(0.1*LEFT)
        mates_2 = TexMobject(r" ").scale(0.08).next_to(posteriores_t1,0.15*DOWN).shift(0.22*LEFT)
        mates = VGroup(mates_1,mates_2)

        sipodemos_1 = TexMobject(r"\text{Si podemos hacer esto tomando}\ \varepsilon>0").move_to(circ_text).scale(0.10)
        sipodemos_2 = TextMobject("tan pequeño como queramos...").scale(0.1).next_to(sipodemos_1,0.15*DOWN)
        sipodemos = VGroup(sipodemos_1, sipodemos_2)

        #Definición de los puntos MAS pequeños
        smolerpoints = []
        for n in range(1,1500):
            smolerpoints.append(ACustomDot(point=np.array([10/n, 10/(n), 0.0]),color = GREY).scale(0.001))
        group3 = VGroup(*smolpoints)

        circulo2 = Circle(radius = 0.147).move_to(points[100])
        circulos = VGroup(circulo1,circulo2)
        entonces = TextMobject("¡Entonces tenemos una sucesión de Cauchy!").scale(0.05).shift(0.3*UP)

        defform1 = TexMobject(r"\text{Sea}\ \{\vec{x}_n\}\ \text{una sucesión, decimos que es de Cauchy si:}").shift(3*UP)
        defform2 = TexMobject(r"\text{para todo}\ \varepsilon>0").set_color(RED).shift(2*UP+2*LEFT)
        defform3 = TexMobject(r"\text{existe}\ N \in \mathbb{N}").set_color(YELLOW).next_to(defform2,RIGHT)
        defform4 = TexMobject(r"\text{tal que si}\ k,l > N, \Rightarrow d(\vec{x}_k,\vec{x}_l)<\varepsilon").set_color(BLUE).shift(UP)

        #Secuencia de la animación: Suc. de Cauchy
        self.play(Write(titu))
        self.wait()
        self.play(FadeOutAndShift(titu)) 
        self.play(Write(bas))
        self.wait()
        self.play(FadeOut(bas))
        self.add(plano)
        self.play(ShowCreation(plano, runtime = 1))
        self.play(Write(suc))
        self.play(ShowIncreasingSubsets(group, run_time=2.0), Write(xn))
        self.wait(2)
        # Zoom de la cámara
        self.play(FadeOut(suc), FadeOut(xn))
        self.play(
            # Establecemos tamaño refiriendo a un objeto
            self.camera_frame.set_width,bas2.get_width()*0.4,
            # Movemos la cámara a un objeto
            self.camera_frame.move_to,points[40],
            ReplacementTransform(group, group2))
        ###
        self.wait()
        self.play(Write(circ_text))
        self.wait()
        self.play(ShowCreation(circulo1))
        self.wait(2)
        self.play(FadeOut(circ_text))
        self.play(Write(amarillo))
        self.play(ApplyMethod(points[23].custom_method, YELLOW))
        self.wait(2)
        self.play(FadeOut(amarillo))
        self.play(Write(posteriores))
        self.play(ApplyMethod(points[24].custom_method, BLUE), ApplyMethod(points[50].custom_method, BLUE))
        self.wait(2)
        self.play(ApplyMethod(points[100].custom_method, BLUE), ApplyMethod(points[50].inverse_method))
        self.wait(2)
        self.play(ApplyMethod(points[500].custom_method, BLUE), ApplyMethod(points[100].inverse_method))
        self.wait(2)
        self.play(ApplyMethod(points[1498].custom_method, BLUE), ApplyMethod(points[500].inverse_method))
        self.wait(2)
        self.play(ReplacementTransform(posteriores,mates))
        self.wait(9)
        self.play(FadeOut(mates))
        self.play(Write(sipodemos),ApplyMethod(points[1498].inverse_method),ApplyMethod(points[24].inverse_method), ApplyMethod(points[23].inverse_method))
        self.wait()
        self.play(FadeOut(sipodemos))
        # Segundo zoom de la cámara
        self.play(
            # Nuevo ancho
            self.camera_frame.set_width,bas2.get_width()*0.2,
            # Nueva posición
            self.camera_frame.move_to,points[80],
            ReplacementTransform(group, group3))
        ###
        self.wait()
        self.play(ShowCreation(circulo2))
        self.wait()
        self.play(ApplyMethod(points[48].custom_method, YELLOW))
        self.wait()
        self.play(ApplyMethod(points[49].custom_method, BLUE), ApplyMethod(points[60].custom_method,BLUE))
        self.wait(2)
        self.play(ApplyMethod(points[100].custom_method, BLUE), ApplyMethod(points[60].inverse_method))
        self.wait()
        self.play(Write(entonces))
        self.wait()
        self.play(FadeOut(circulos),FadeOut(group3),FadeOut(entonces),ApplyMethod(points[100].custom_method, BLACK),
        ApplyMethod(points[48].custom_method, BLACK),ApplyMethod(points[49].custom_method, BLACK),
        ApplyMethod(points[60].custom_method, BLACK),FadeOut(plano))
        # Regresamos a la posición de cámara original
        self.play(Restore(self.camera_frame))
        self.wait()
        self.play(Write(defform1))
        self.play(Write(defform2))
        self.wait(5)
        self.play(Write(defform3))
        self.wait(3)
        self.play(Write(defform4))
        self.wait(7)
        self.play(FadeOut(defform1), FadeOut(defform2), FadeOut(defform3), FadeOut(defform4))

###################################
#### SUCESIONES ACOTADAS    #####
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

###################################
#### TEOREMA RECTÁNGULOS ANIDADOS #####
###################################

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

###################################
#### TEOREMA BOLZANO WEIERSTRASS #####
###################################

#Definimos un Dot con métodos específicos para la escena de BolzanoWeierstrass
class CCustomDot(Dot):
    def custom_method(self, color):
        self.set_color(color)
        self.scale(5)
        return self

    def other_method(self):
        self.scale(1 / 5)
        return self

    def small_method(self, color):
        self.set_color(color)
        self.scale(1.5)
        return self

class BolzanoWeierstrass(Scene):
    def construct(self):
        titulo = TextMobject("El Teorema de Bolzano-Weierstrass").scale(1.5)
        teorema_1 = TexMobject(r"\text{Toda sucesi\'{o}n}\ ", r"\text{acotada}\ ", r"\text{en}\  \mathbb{R}^n")
        teorema_2 = TextMobject(r"\text{tiene una}", r" subsucesi\'{o}n convergente.").next_to(teorema_1, DOWN)
        teorema = VGroup(teorema_1, teorema_2)
        teorema_1[1].set_color(YELLOW)
        teorema_2[1].set_color(RED)
        plano = NumberPlane()

        suc_acot = TexMobject(r"\text{Sea}\ \{\vec{x}_n\}\ \text{una sucesi\'{o}n}\ ", r"\text{acotada}",
                              r"\text{ por M}").to_edge(UP)
        suc_acot[1].set_color(YELLOW)
        suc_acot.bg = SurroundingRectangle(suc_acot, color=WHITE, fill_color=BLACK, fill_opacity=1)
        group_acot = VGroup(suc_acot.bg, suc_acot)  #####imp

        # Construyendo una subsucesi'{o}n acotada: "Infinidad" de puntos
        points_infinite_values = []
        for n in range(3, 1500):
            points_infinite_values.append(CCustomDot(
                point=np.array([np.sqrt(2) * np.power(-1, n) * (n) / (n + 3), np.sqrt(2) * (n) / (n + 3), 0.0]),
                color=GREY).scale(0.7))
        group2 = VGroup(*points_infinite_values)

        # C'{i}rculo y "emes"
        circulo = Circle(radius=np.sqrt(np.power(np.sqrt(2), 2) + np.power(np.sqrt(2), 2))).set_color(YELLOW)
        M_der = TexMobject("M").scale(0.75).move_to((2.4, 0, 0))
        M_izq = TexMobject("-M").scale(0.75).move_to((-2.4, 0, 0))
        M_arb = TexMobject("M").scale(0.75).move_to((0, 2.2, 0))
        M_abj = TexMobject("-M").scale(0.75).move_to((0, -2.2, 0))
        emes = VGroup(M_der, M_izq, M_arb, M_abj)
        # Rect'{a}ngulo R1
        el_rect = TextMobject(r"\text{Acotemos la sucesi\'{o}n con un rect\'{a}ngulo de lado 2M:} ",
                              r"\text{$R$}").to_edge(UP).scale(0.8)
        el_rect[1].set_color(YELLOW)
        R = Rectangle(height=2 * np.sqrt(np.power(np.sqrt(2), 2) + np.power(np.sqrt(2), 2)),
                      width=2 * np.sqrt(np.power(np.sqrt(2), 2) + np.power(np.sqrt(2), 2))).set_color(YELLOW)

        # Rect'{a}ngulo R2
        subrect_1a = TextMobject(r"\text{Tomemos un subrect\'{a}ngulo con una cantidad infinita}").to_edge(UP)
        subrect_1b = TexMobject(r"\text{de t\'{e}rminos de la sucesi\'{o}n: } ", r"\text{$R_1$}").next_to(subrect_1a,
                                                                                                         DOWN)
        subrect_1b[1].set_color(ORANGE)
        cuadrante_dR1 = TexMobject(r"\text{Notemos que}\ ", r"R_1\ ", r"\text{es un cuadrante de}\ ", r"R").to_edge(
            DOWN)
        cuadrante_dR1[1].set_color(ORANGE)
        cuadrante_dR1[3].set_color(YELLOW)
        subrect_1 = VGroup(subrect_1a, subrect_1b).scale(0.8)
        R1 = Rectangle(height=2, width=2).move_to((1, 1, 0)).set_color(ORANGE)

        # Rect'{a}ngulo R3
        subrect_2a = TextMobject(r"\text{Nuevamente tomemos un subrect\'{a}ngulo que sea un cuadrante del}").to_edge(
            UP).scale(0.8)
        subrect_2b = TextMobject(r"\text{anterior con infinitos t\'{e}rminos de la sucesi\'{o}n:} ",
                                 r"\text{$R_2$}").next_to(subrect_2a, DOWN).scale(0.8)
        subrect_2b[1].set_color(GREEN)
        subrect_2 = VGroup(subrect_2a, subrect_2b)
        R2 = Rectangle(height=1, width=1).move_to((1.5, 1.5, 0)).set_color(GREEN)

        # Rect'{a}ngulos siguientes
        subrects_a = TextMobject(r"\text{Repetimos infinitas veces, siempre tomando un subrect\'{a}ngulo}").to_edge(
            UP).scale(0.8)
        subrects_b = TextMobject(r"\text{con una cantidad infinita de t\'{e}rminos de la sucesi\'{o}n}").next_to(
            subrects_a, DOWN).scale(0.8)
        subrects = VGroup(subrects_a, subrects_b)

        R3 = Rectangle(height=0.5, width=0.5).move_to((1.25, 1.25, 0)).set_color(BLUE)
        R4 = Rectangle(height=0.25, width=0.25).move_to((1.375, 1.375, 0)).set_color(PURPLE)
        R5 = Rectangle(height=0.125, width=0.125).move_to((1.4375, 1.4375, 0)).set_color(PINK)
        R6 = Rectangle(height=0.0625, width=0.0625).move_to((1.46875, 1.46875, 0)).set_color(TEAL)

        Rects = VGroup(R, R1, R2, R3, R4, R5, R6)

        # Observaciones acerca de los rect'{a}ngulos
        notas_rect_0 = TextMobject(r"\text{Tenemos una sucesi\'{o}n de rect\'{a}ngulos anidados que cumplen:}").to_edge(
            UP).scale(0.8)
        notas_rect_1 = TexMobject(r"1)\ R_{k+1} \subset R_{k}").next_to(notas_rect_0, 5 * DOWN).shift(2 * RIGHT).scale(
            0.8)
        notas_rect_2 = TexMobject(r"2)\ diag(R_{k})= \frac{\sqrt{2}M}{2^{k-1}}").next_to(notas_rect_1, DOWN).scale(0.8)
        notas_rect_3 = TexMobject(r"3)\ R_{k+1}\ \text{tiene infinitos puntos de}\ \{\vec{x}_n\}").next_to(notas_rect_2,
                                                                                                           1.5 * DOWN).scale(
            0.8).shift(1 * RIGHT)

        # Refer'{e}ncia a los rect'{a}ngulos anidados
        TRA_a = TextMobject("Gracias a las observaciones 1 y 2, y al teorema ").move_to(notas_rect_0)
        TRA_b = TextMobject(r"\text{de los rect\'{a}ngulos anidados, existe} ", "$\\cap_{k=1}^{\\infty}R_k =$",
                            " $\\vec{x}_0$").next_to(TRA_a, DOWN)
        TRA_b[2].set_color(BLUE)
        TRA = VGroup(TRA_a, TRA_b).scale(0.9)

        construyamos_0 = TextMobject(r"\text{Construyamos una subsucesi\'{o}n}").shift(3 * RIGHT + UP)
        construyamos_1 = TextMobject("que converge a ", "$\\vec{x}_0$").next_to(construyamos_0, DOWN)
        construyamos_1[1].set_color(BLUE)
        construyamos = VGroup(construyamos_0, construyamos_1).scale(0.9)

        subsuc = TextMobject(r"\text{La observaci\'{o}n 3 nos permite tomar}").scale(0.8).shift(3 * RIGHT + UP)

        # Construyendo la subsucesi'{o}n
        subsuc_1 = TexMobject(r"\vec{x}_{n_1}", r"\in R_1").shift(3 * RIGHT)
        subsuc_1[0].set_color(RED)

        subsuc_2a = TexMobject(r"\vec{x}_{n_2}", r"\in R_2").shift(3 * RIGHT)
        subsuc_2a[0].set_color(RED)
        subsuc_2b = TexMobject(r"\text{tomando } n_2>n_1").next_to(subsuc_2a, 1.5 * DOWN).scale(0.9)
        subsuc_2 = VGroup(subsuc_2a, subsuc_2b)

        subsuc_3a = TexMobject(r"\vec{x}_{n_3}", r"\in R_3").shift(3 * RIGHT)
        subsuc_3a[0].set_color(RED)
        subsuc_3b = TexMobject(r"\text{tomando } n_3>n_2").next_to(subsuc_3a, 1.5 * DOWN).scale(0.9)
        subsuc_3 = VGroup(subsuc_3a, subsuc_3b)

        subsuc_ka = TexMobject(r"\vec{x}_{n_k}", r"\in R_k").shift(3 * RIGHT)
        subsuc_ka[0].set_color(RED)
        subsuc_kb = TexMobject(r"\text{tomando } n_k>n_{k-1}").next_to(subsuc_3a, 1.5 * DOWN).scale(0.9)
        subsuc_k = VGroup(subsuc_ka, subsuc_kb)

        casi_conclu_a = TextMobject("De esta forma").move_to(construyamos_1).shift(3 * UP)
        casi_conclu_b = TexMobject(r"0\leq d(\vec{x}_{n_k},\vec{x}_0)\leq \frac{\sqrt{2}M}{2^{k-1}}").next_to(
            casi_conclu_a, DOWN)
        casi_conclu = VGroup(casi_conclu_a, casi_conclu_b).scale(0.9)

        pre_conclu_a = TexMobject(r"\text{y como } \lim_{k \to \infty} \frac{\sqrt{2}M}{2^{k-1}} = 0").move_to(
            notas_rect_3).shift(2 * UP)
        pre_conclu_b = TexMobject(r" \Rightarrow \lim_{k \to \infty} d(\vec{x}_{n_k},\vec{x}_0) = 0").next_to(
            pre_conclu_a, DOWN)
        pre_conclu = VGroup(pre_conclu_a, pre_conclu_b).scale(0.8)

        conclu_a = TextMobject("Tenemos").move_to(notas_rect_3).scale(0.9)
        conclu_b = TexMobject(r"\lim_{k \to \infty} \{\vec{x}_{n_k}\} = \vec{x}_0").next_to(conclu_a, 1.6 * DOWN)
        conclu_c = TextMobject("nuestra ", r"\text{subsucesi\'{o}n convergente.}").next_to(conclu_b, 1.3 * DOWN)
        conclu_c[1].set_color(RED)
        conclu_rect = Rectangle(color=RED, width=1.2 * conclu_b.get_width(),
                                height=1.3 * conclu_b.get_height()).move_to(conclu_b)
        conclu = VGroup(conclu_a, conclu_b, conclu_c, conclu_rect)

        # Secuencia de la animación: Teorema de Bolzano-Weierstrass
        self.play(Write(titulo))
        self.wait()
        self.play(FadeOut(titulo))
        self.play(Write(teorema))
        self.wait(2)
        self.play(FadeOut(teorema))
        self.play(ShowCreation(plano))
        self.play(Write(group_acot))
        self.play(ShowIncreasingSubsets(group2, run_time=2.0))
        self.play(ShowCreation(circulo), ShowCreation(emes))
        self.wait()
        self.play(ReplacementTransform(group_acot, el_rect), FadeOut(plano))
        self.wait(2)
        self.play(ShowCreation(R), FadeOut(circulo))
        self.wait(2)
        self.play(ReplacementTransform(el_rect, subrect_1), Write(cuadrante_dR1))
        self.wait(3)
        self.play(ShowCreation(R1))
        self.wait(3)
        self.play(ReplacementTransform(subrect_1, subrect_2), FadeOut(cuadrante_dR1))
        self.wait(2)
        self.play(ShowCreation(R2))
        self.wait(6)
        self.play(ReplacementTransform(subrect_2, subrects))
        self.wait(2)
        self.play(ShowCreation(R3))
        self.play(ShowCreation(R4))
        self.play(ShowCreation(R5))
        self.play(ShowCreation(R6))
        self.wait()
        self.play(FadeOut(subrects))
        self.play(emes.shift, 3 * LEFT, group2.shift, 3 * LEFT, R.shift, 3 * LEFT, R1.shift, 3 * LEFT, \
                  R2.shift, 3 * LEFT, R3.shift, 3 * LEFT, R4.shift, 3 * LEFT, R5.shift, 3 * LEFT, R6.shift, 3 * LEFT
                  )  # Mover toda la construcción a la izquierda
        self.play(FadeOut(emes))
        self.play(Write(notas_rect_0))
        self.wait(2)
        self.play(Write(notas_rect_1))
        self.wait(2)
        self.play(Write(notas_rect_2))
        self.wait(2)
        self.play(Write(notas_rect_3))
        self.wait(4)
        self.play(FadeOut(notas_rect_1), FadeOut(notas_rect_2), FadeOut(notas_rect_3),
                  ReplacementTransform(notas_rect_0, TRA))
        self.wait(2)
        self.play(ApplyMethod(points_infinite_values[1495].custom_method, BLUE))
        self.play(ApplyMethod(points_infinite_values[1495].other_method, run_time=1.5))
        self.wait(2)
        self.play(Write(construyamos))
        self.wait(2)
        self.play(FadeOut(TRA), construyamos.shift, 2 * UP)
        self.wait(2)
        self.play(Write(subsuc), Write(subsuc_1))
        self.play(ApplyMethod(points_infinite_values[1].custom_method, RED))
        self.play(ApplyMethod(points_infinite_values[1].other_method))
        self.wait(2)
        self.play(FadeOut(subsuc))
        self.play(ReplacementTransform(subsuc_1, subsuc_2), ApplyMethod(points_infinite_values[7].custom_method, RED))
        self.play(ApplyMethod(points_infinite_values[7].other_method))
        self.wait(2)
        self.play(ReplacementTransform(subsuc_2, subsuc_3), ApplyMethod(points_infinite_values[51].custom_method, RED))
        self.play(ApplyMethod(points_infinite_values[51].other_method))
        self.wait(2)
        self.play(ReplacementTransform(subsuc_3, subsuc_k), ApplyMethod(points_infinite_values[799].custom_method, RED))
        self.play(ApplyMethod(points_infinite_values[799].other_method))
        self.play(FadeOut(subsuc_k), FadeOut(construyamos))
        self.play(Write(casi_conclu))
        self.wait(8)
        self.play(Write(pre_conclu))
        self.wait(11)
        self.play(Write(conclu))
        self.wait(4)
        self.play(FadeOut(casi_conclu), FadeOut(pre_conclu), FadeOut(Rects), FadeOut(group2))
        self.play(conclu.move_to, (0, 0, 0))
        self.wait(2)
        self.play(FadeOut(conclu))
