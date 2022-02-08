from manimlib.imports import *

######################################################
##### Curvas no rectificables ########################
######################################################

class Curvas_No_Rectificables(GraphScene,Scene):
    def setup(self):
        Scene.setup(self)
        GraphScene.setup(self)
    def FadeOutWrite(self,objeto1,objeto2):
        self.play(FadeOut(objeto1))
        self.play(Write(objeto2))
    def particiones(self):
        Grupo_1 = Dot(radius=0)
        numberline_1 = NumberLine(x_min=0,x_max=(2/PI)+0.127,unit_size=6, tick_frequency=(2/(5*PI)),
                                include_tip=True,number_scale_val=0.6,numbers_with_elongated_ticks=[0,2/PI]).move_to(3.5*RIGHT+0.7*DOWN).set_color(BLUE)
        for j in range(4,12):
            conj_puntos_particion = []
            conj_evaluacion_particion = []
            conj_poligonal_particion = []

            for i in range(0,j-1):
                punto_dom = Dot(radius=0.05).move_to(numberline_1.get_left()+(1/(PI*(0.5+i)))*6*RIGHT)
                conj_puntos_particion.append(punto_dom)
                punto_eval = Dot(radius=0.05).move_to(((1/(PI*(0.5+i)))*4-4.5,1.5*math.sin((PI*(0.5+i)))-0.7,0))
                conj_evaluacion_particion.append(punto_eval)
                if (i<j-2):
                    linea_poligonal = Line(((1/(PI*(0.5+i)))*4-4.5,1.5*math.sin((PI*(0.5+i)))-0.7,0),((1/(PI*(0.5+i+1)))*4-4.5,1.5*math.sin((PI*(0.5+i+1)))-0.7,0))
                    conj_poligonal_particion.append(linea_poligonal)
            
            ##### Primer elemento de la partición
            punto_dom = Dot(radius=0.05).move_to(numberline_1.get_left())
            conj_puntos_particion.append(punto_dom)
            punto_eval = Dot(radius=0.05).move_to(((-4.5,-0.7,0)))
            conj_evaluacion_particion.append(punto_eval)
            linea_poligonal = Line(((1/(PI*(0.5+j-2)))*4-4.5,1.5*math.sin((PI*(0.5+j-2)))-0.7,0),(-4.5,-0.7,0))
            conj_poligonal_particion.append(linea_poligonal)

            ####Conjuntos con elementos
            puntos_particion = VGroup(*conj_puntos_particion)
            puntos_evaluacion_particion = VGroup(*conj_evaluacion_particion)
            poligonal_particion = VGroup(*conj_poligonal_particion)

            ####Animaciones con poligonal
            focus_poligonal = []
            for i in range(0,j-1):
                focus_poligonal.append(FadeToColor(poligonal_particion[i],RED,rate_func=there_and_back))

            Grupo = VGroup(puntos_particion,puntos_evaluacion_particion)
            self.play(ShowCreation(Grupo))
            
            Grupo_1 = VGroup(puntos_evaluacion_particion,poligonal_particion)
            self.play(LaggedStart(*focus_poligonal),run_time=2.0)
            self.play(FadeOut(Grupo_1))
            
    CONFIG = {
        "x_min": -0.25,
        "x_max": 1,
        "x_axis_width": 5,
        "x_tick_frequency": 10,
        "x_leftmost_tick": None,  # Change if different from x_min
        "x_labeled_nums": [],
        "x_axis_label": "$x$",
        "y_min": -1.5,
        "y_max": 1.5,
        "y_axis_height": 3*1.5,
        "y_tick_frequency": 0.5,
        "y_bottom_tick": None,  # Change if different from y_min
        "y_labeled_nums": [-1,1],
        "y_axis_label": "$y$",
        "axes_color": BLUE,
        "graph_origin": 4.5*LEFT+0.7*DOWN,
        "exclude_zero_label": True,
        "default_graph_colors": [BLUE, GREEN, YELLOW],
        "default_derivative_color": GREEN,
        "default_input_color": YELLOW,
        "default_riemann_start_color": BLUE,
        "default_riemann_end_color": GREEN,
        "area_opacity": 0.8,
        "num_rects": 50,
        "num_graph_anchor_points": 30000
    }
    def construct(self):
        titulo = TextMobject("Curvas No Rectificables").scale(1.5) 
        text_1 = TextMobject('''Sea $\\sigma : [0,\\infty)\\rightarrow \\mathbb{R}^2$\n
                                $\\sigma (t)=\\left( t,\\sin{\\dfrac{1}{t}} \\right), t>0$\n
                                 $\\sigma (0)=(0,0)$''')
        funcion_1 = TexMobject(r"""\sigma (t)=\left( t,\sin{\dfrac{1}{t}} \right), t>0\\
                                \sigma (0)=(0,0)""").set_color(YELLOW).scale(0.7).move_to(2.9*DOWN)
        text_2 = TextMobject(''' En general, una curva en $\\mathbb{R}^n$,  $\\sigma: A\\subset\\mathbb{R}\\rightarrow\\mathbb{R}^n$\n
                                 es rectificable si $\\forall$  $a,b\\in A, a<b$, \n
                                $\\sigma$ es rectificable en $[a,b]$''').move_to(3*UP)
        text_3 = TextMobject("Consideremos $A=\\left[ 0,\\dfrac{2}{\\pi} \\right]$").move_to(3*UP)
        text_4 = TextMobject("Veremos que $\\sigma$ no es rectificable en $A$").move_to(3*UP)

        text_5 = TextMobject('''Sea $t_n=\\dfrac{1}{\\pi(1/2+k-n)}$, $n=1,...,k$,\n 
                                con $k\\in\\mathbb{N}$ fijo, y $t_0=0.$''').move_to(2.5*UP)
        text_5_2 = TextMobject("donde $\\sin{\\dfrac{1}{t_n}}=(-1)^{k-n}$").move_to(3*UP)
        text_5_1 = TextMobject("En el ejemplo, tomamos $k=3$").move_to(3*UP)
        text_tn = TexMobject(r"""t_n=\dfrac{1}{\pi(1/2+k-n)},\quad n=1,...,k\\
                             t_0=0""").scale(0.7).move_to(0.75*UP+3.5*RIGHT)
        text_6 = TextMobject('''Sea $\\mathcal{S}$ una partición de $A$\n 
                                $\\mathcal{S}:=\\{t_0,t_1,...,t_k\\}$''' ).move_to(3*UP)
        text_7 = TextMobject('''$\\mathcal{S}$ genera una poligonal $\\mathcal{P}$ con los puntos\n
                                 $\\sigma_{\\mathcal{P}}:=\\{ \\sigma(t_0),...,\\sigma(t_k) \\}$''').move_to(3*UP)
        text_8 = TextMobject('''Obsérvese que $\\left|\\sin\\dfrac{1}{t_n}-\\sin\\dfrac{1}{t_{n-1}}\\right|=2$, $n=2,...,k$''').move_to(3*UP)
        text_9 = TextMobject('''Entonces, $\\left\\Vert \\sigma(t_n)-\\sigma(t_{n-1}) \\right\\Vert > 2$, $n=2,...,k$''').move_to(3*UP)
        text_10 = TextMobject('''Por lo tanto, \n
                                $\\text{long}(C)>d(\\mathcal{P})=\\sum_{n=1}^{k}\\left\\Vert\\sigma(t_n)-\\sigma(t_{n-1})\\right\\Vert >\\sum_{n=2}^k 2,$\n
                                con $C=\\text{Im}(\\sigma).$''').move_to(3.0*UP)
        text_11 = TextMobject('''La serie $\\sum_{n=2}^{\\infty}2$ diverge, entonces para toda $M>0$, \n
                                podemos definir una partición $\\mathcal{P}$ de $A$,\n
                                tal que $d(\\mathcal{P})>M$. ''').move_to(2.7*UP)
        text_13 = TextMobject('''Por lo tanto, decimos que $\\sigma$ no es rectificable en $A$\n
                                y por ende no es rectificable en $(0,\\infty)$''').move_to(3*UP)
        
        ####Objetos
        
        ####Punto en dominio 2/pi
        text_punto_dom_1 = TexMobject(r"\dfrac{2}{\pi}").scale(0.7).move_to((-4.5+(2/PI)*4,-0.7-0.9,0))
        linea_punto_dom_1 = Line((-4.5+(2/PI)*4,-0.7-0.25,0),(-4.5+(2/PI)*4,-0.7+.25,0))
        punto_dom_1 = VGroup(text_punto_dom_1,linea_punto_dom_1)

        #### Recta real de particiones
        numberline_1 = NumberLine(x_min=0,x_max=(2/PI)+0.127,unit_size=6, tick_frequency=(2/(5*PI)),
                                include_tip=True,number_scale_val=0.6,numbers_with_elongated_ticks=[0,2/PI]).move_to(3.5*RIGHT+0.7*DOWN).set_color(BLUE)
        etiqueta_numberline_1 = TexMobject(r"t").move_to(numberline_1.get_right()+0.4*UP)
        etiqueta_numberline_2 = TexMobject(r"\dfrac{2}{\pi}").move_to(numberline_1.get_left()+0.7*DOWN+(2/PI)*6*RIGHT).scale(0.7)
        etiqueta_numberline_3 = TexMobject(r"0").move_to(numberline_1.get_left()+0.4*DOWN).scale(0.7)
        etiquetas_numberline = VGroup(etiqueta_numberline_1,etiqueta_numberline_2,etiqueta_numberline_3)

        ###Recta vertical de longitud 2
        recta_hor_1 = DashedLine((-4.5,-1.5-0.7,0),(-1.5,-1.5-0.7,0))
        recta_hor_2 = DashedLine((-4.5,1.5-0.7,0),(-1.5,1.5-0.7,0))
        recta_vert = DashedLine((-1.5,-1.5-0.7,0),(-1.5,1.5-0.7,0))
        rectas =  VGroup(recta_vert,recta_hor_1,recta_hor_2)

        
     
        ##########Particiones, Evaluaciones y poligonal con 4 elementos#########
        ####En esta función se generan los puntos de la partición en el dominio, puntos de evaluación, sus poligonales y puntos en diagrama de longitudes para la partición de 5 elementos
        #### La razón por la que este caso no se trató con la función particiones(), es que con estos conjuntos se aplicarán otras animaciones, así como textos particulares
        conj_puntos_particion = []
        conj_evaluacion_particion = []
        conj_poligonal_particion = []
        j = 4
        for i in range(0,j-1):
            punto_dom = Dot(radius=0.05).move_to(numberline_1.get_left()+(1/(PI*(0.5+i)))*6*RIGHT)
            conj_puntos_particion.append(punto_dom)
            punto_eval = Dot(radius=0.05).move_to(((1/(PI*(0.5+i)))*4-4.5,1.5*math.sin((PI*(0.5+i)))-0.7,0))
            conj_evaluacion_particion.append(punto_eval)
            if (i<j-2):
                linea_poligonal = Line(((1/(PI*(0.5+i)))*4-4.5,1.5*math.sin((PI*(0.5+i)))-0.7,0),((1/(PI*(0.5+i+1)))*4-4.5,1.5*math.sin((PI*(0.5+i+1)))-0.7,0))
                conj_poligonal_particion.append(linea_poligonal)
            
            ##### Primer elemento de la partición
        punto_dom = Dot(radius=0.05).move_to(numberline_1.get_left())
        conj_puntos_particion.append(punto_dom)
        punto_eval = Dot(radius=0.05).move_to(((-4.5,-0.7,0)))
        conj_evaluacion_particion.append(punto_eval)
        linea_poligonal = Line(((1/(PI*(0.5+j-2)))*4-4.5,1.5*math.sin((PI*(0.5+j-2)))-0.7,0),(-4.5,-0.7,0))
        conj_poligonal_particion.append(linea_poligonal)

        ####Conjuntos con elementos
        puntos_particion = VGroup(*conj_puntos_particion)
        puntos_evaluacion_particion = VGroup(*conj_evaluacion_particion)
        poligonal_particion = VGroup(*conj_poligonal_particion)

        ####Animaciones con poligonal
        focus_poligonal_1 = []
        for i in range(0,j-1):
            focus_poligonal_1.append(FadeToColor(poligonal_particion[i],RED,rate_func=there_and_back))
        focus_poligonal_2 = []
        for i in range(0,j-1):
            focus_poligonal_2.append(FadeToColor(poligonal_particion[i],RED,rate_func=there_and_back))

        ####Etiquetas en particion
        t_0 = TexMobject(r"t_0").scale(0.7).move_to(conj_puntos_particion[3].get_top()+0.4*UP)
        t_1 = TexMobject(r"t_1").scale(0.7).move_to(conj_puntos_particion[2].get_top()+0.4*UP)
        t_2 = TexMobject(r"t_2").scale(0.7).move_to(conj_puntos_particion[1].get_top()+0.4*UP)
        t_3 = TexMobject(r"t_3").scale(0.7).move_to(conj_puntos_particion[0].get_top()+0.4*UP)
        etiquetas_particiones = VGroup(t_0,t_1,t_2,t_3)

        ###ANIMACIONES
        self.play(Write(titulo))
        self.wait(3)
        self.FadeOutWrite(titulo,text_1)
        self.wait(13.25)
        self.play(ReplacementTransform(text_1,funcion_1))
        self.setup_axes(animate=True)
        #Función

        f = lambda x: math.sin(1/x)
        graph = self.get_graph(
            f, 
            color = YELLOW,
            x_min = 0.00005,
            x_max = 1
        )

        self.play(Write(graph),run_time=3)
        self.wait()
        self.play(Write(text_2))
        self.wait(13.75)
        self.FadeOutWrite(text_2,text_3)
        self.wait(5)
        self.play(Write(punto_dom_1))
        self.play(ShowCreation(numberline_1))
        self.play(Write(etiquetas_numberline))
        self.wait()
        self.FadeOutWrite(text_3,text_4)
        self.wait(5)
        self.FadeOutWrite(text_4,text_5)
        self.wait(11.25)
        self.play(ShowCreation(puntos_particion))
        self.play(ReplacementTransform(text_5,text_tn))
        self.play(Write(text_5_2))
        self.wait(6.875)
        self.FadeOutWrite(text_5_2,text_5_1)
        self.wait(4.6)
        self.FadeOutWrite(text_5_1,text_6)
        self.wait(6.125)
        self.play(Write(etiquetas_particiones))
        self.FadeOutWrite(text_6,text_7)
        self.wait(7.25)
        self.play(ShowCreation(puntos_evaluacion_particion))
        self.play(Write(poligonal_particion),run_time=3)
        self.play(FadeOut(graph))
        self.wait()
        self.play(FadeIn(graph))
        self.FadeOutWrite(text_7,text_8)
        self.wait(9.875)
        self.play(ShowCreation(recta_vert))
        self.play(ShowCreation(recta_hor_1))
        self.play(ShowCreation(recta_hor_2))
        self.FadeOutWrite(text_8,text_9)
        self.wait(15.5)
        self.play(Succession(*focus_poligonal_2),run_time=3)
        self.FadeOutWrite(text_9,text_10)
        self.wait(12.5)
        self.play(LaggedStart(*focus_poligonal_1),run_time=3)
        self.wait()
        self.play(FadeOut(etiquetas_particiones),FadeOut(puntos_particion),FadeOut(poligonal_particion),FadeOut(puntos_evaluacion_particion),FadeOut(rectas))
        self.FadeOutWrite(text_10,text_11)
        self.wait(12.5)
        self.play(FadeOut(text_11))
        self.particiones()
        self.play(Write(text_13))
        self.wait(9.5)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )