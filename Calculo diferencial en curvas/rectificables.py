from manimlib.imports import *

######################################################
##### Curvas rectificables ###########################
######################################################

#-------------Fuciones auxiliares para la función partición_círculo-------------
def set_angs():
    return [0, 1*2*np.pi/3.0, 2*2*np.pi/3.0, 3*2*np.pi/3.0]
def partir(angulos,j):
    left = 0
    right = left+1
    for iteracion in range(1,j):
        index = 2*iteracion-1
        angulos.insert(index,(angulos[left]+angulos[right])/2.0)
        left = 2*iteracion
        right = left+1
    return angulos
#-------------Fución utilizada en la clase Curvas_Rectificables-----------------
def particion_circulo(n):
    '''
    INPUT:
        Esta función recibe el número de puntos, n, que se le agregan a la 
    partición inicial [0, 1*2*np.pi/3.0, 2*2*np.pi/3.0, 3*2*np.pi/3.0]. De manera
    que al círculo se le van agragando puntos al círculo en sentido antihorario.
    n es un entero que va de [0,21], pero se puede generalizar a más puntos.

    OUTPUT:
        Devuelve la partición en forma de un array
    
    No modificar los valores aquí dados, a menos que se necesite generalizar el
    algoritmo.
    '''
    angs = set_angs()
    for num_puntos in range(n+1):
        for i in range(1,num_puntos+2):
            if num_puntos<=3:
                angs = set_angs()
                angs = partir(angs, i)
            elif 3<num_puntos<=9:
                angs = set_angs()
                angs = partir(angs, 4)
                angs = partir(angs, i-3)
            elif 9<num_puntos<=21:
                angs = set_angs()
                angs = partir(angs, 4)
                angs = partir(angs, 7)
                angs = partir(angs, i-9)
    return angs

class Curvas_Rectificables(GraphScene,Scene):
    def setup(self):
        Scene.setup(self)
        GraphScene.setup(self)
    def FadeOutWrite(self,objeto1,objeto2):
        self.play(FadeOut(objeto1))
        self.play(Write(objeto2))
    ###### la función particiones lo que hace es generar particiones, puntos de evaluación, poligonales, puntos en el diagrama de longitud y corre las animaciones correspondientes.
    def particiones(self):
        numberline_1 = NumberLine(x_min=0,x_max=2*PI+1,unit_size=0.75).move_to(2.8*LEFT+3*DOWN)
        distancias_poligonales_2 =[]
        arrow = Arrow((-1.2,1,0),(0.0,1,0)).set_color(RED)

        dot_4 = Dot(color=RED,radius=0.05).move_to((1.5,-2+0.40,0))
        dist_4 = TexMobject(r"d(\mathcal{P})=7.79").move_to((-0.8,1.5,0)).scale(0.7).set_color(RED_E)

        dot_5 = Dot(color=RED,radius=0.05).move_to((2,-2+1.40,0))
        dist_5 = TexMobject(r"d(\mathcal{P}')=8.19").move_to((-0.8,1.5,0)).scale(0.7).set_color(RED_E)

        dot_6 = Dot(color=RED,radius=0.05).move_to((2.5,-2+2.4,0))
        dist_6 = TexMobject(r"d(\mathcal{P}')=8.59").move_to((-0.8,1.5,0)).scale(0.7).set_color(RED_E)

        dot_7 = Dot(color=RED,radius=0.05).move_to((3,-2+3.2,0))
        dist_7 = TexMobject(r"d(\mathcal{P}')=9.0").move_to((-0.8,1.5,0)).scale(0.7).set_color(RED_E)

        dot_8 = Dot(color=RED,radius=0.05).move_to((3.5,-2+3.40,0))
        dist_8 = TexMobject(r"d(\mathcal{P}')=9.05").move_to((-0.8,1.5,0)).scale(0.7).set_color(RED_E)

        dot_9 = Dot(color=RED,radius=0.05).move_to((4,-2+3.55,0))
        dist_9 = TexMobject(r"d(\mathcal{P}')=9.10").move_to((-0.8,1.5,0)).scale(0.7).set_color(RED_E)

        dot_10 = Dot(color=RED,radius=0.05).move_to((4.5,-2+3.70,0))
        dist_10 = TexMobject(r"d(\mathcal{P}')=9.15").move_to((-0.8,1.5,0)).scale(0.7).set_color(RED_E)

        dot_11 = Dot(color=RED,radius=0.05).move_to((5,-2+3.80,0))
        dist_11 = TexMobject(r"d(\mathcal{P}')=9.21").move_to((-0.8,1.5,0)).scale(0.7).set_color(RED_E)

        dot_12 = Dot(color=RED,radius=0.05).move_to((5.5,-2+3.90,0))
        dist_12 = TexMobject(r"d(\mathcal{P}')=9.26").move_to((-0.8,1.5,0)).scale(0.7).set_color(RED_E)

        dot_13 = Dot(color=RED,radius=0.05).move_to((6,-2+4.0,0))
        dist_13 = TexMobject(r"d(\mathcal{P}')=9.31").move_to((-0.8,1.5,0)).scale(0.7).set_color(RED_E)

        dots = [dot_4, dot_5, dot_6, dot_7, dot_8, dot_9, dot_10, dot_11, dot_12, dot_13]
        dists = [dist_4, dist_5, dist_6, dist_7, dist_8, dist_9, dist_10, dist_11, dist_12, dist_13]
        Grupo_1 = VGroup(Dot(radius=0).move_to(3*LEFT))

        for j in range(10):
            
            conj_puntos_particion = []
            conj_evaluacion_particion = []
            conj_poligonal_particion = []
            suma_distancias = 0

            particion = particion_circulo(j)
            for i in range(len(particion)):
                punto_dom = Dot().move_to(numberline_1.get_left()+particion[i]*0.75*RIGHT)
                conj_puntos_particion.append(punto_dom)
                punto_eval = Dot().move_to((1.5*np.cos(particion[i])-3,1.5*np.sin(particion[i]),0))
                conj_evaluacion_particion.append(punto_eval)
                if i<(len(particion)-1):
                    linea_poligonal = Line((1.5*np.cos(particion[i])-3,1.5*np.sin(particion[i]),0),(1.5*np.cos(particion[i+1])-3,1.5*np.sin(particion[i+1]),0))
                    conj_poligonal_particion.append(linea_poligonal)
                    suma_distancias += np.linalg.norm(np.array((1.5*np.cos(particion[i])-3,1.5*np.sin(particion[i]),0))-\
                                                    np.array((1.5*np.cos(particion[i+1])-3,1.5*np.sin(particion[i+1]),0)))
        ####Conjuntos con elementos
            puntos_particion = VGroup(*conj_puntos_particion)
            puntos_evaluacion_particion = VGroup(*conj_evaluacion_particion)
            poligonal_particion = VGroup(*conj_poligonal_particion)
            distancias_poligonales_2.append(suma_distancias)

        ####Animaciones con poligonal
            focus_poligonal_1 = []
            for i in range(0,len(poligonal_particion)):
                focus_poligonal_1.append(FadeToColor(poligonal_particion[i],RED,rate_func=there_and_back))
            focus_poligonal_2 = []
            for i in range(0,len(poligonal_particion)):
                focus_poligonal_2.append(FadeToColor(poligonal_particion[i],RED,rate_func=there_and_back))
        ####Ejecución de Animaciones        
            Grupo = VGroup(puntos_particion,puntos_evaluacion_particion,poligonal_particion)
            self.play(ReplacementTransform(Grupo_1,Grupo))
            
            self.play(ShowCreation(arrow))
            self.play(FadeIn(dots[j]),FadeIn(dists[j]))
            self.play(FadeOut(dists[j]))

            Grupo_1 = VGroup(puntos_particion,puntos_evaluacion_particion,poligonal_particion)
            self.play(LaggedStart(*focus_poligonal_2),run_time=2)
        self.play(FadeOut(arrow))
    CONFIG = {
        "x_min": -2,
        "x_max": 2,
        "x_axis_width": 4,
        "x_tick_frequency": 0.5,
        "x_leftmost_tick": None,  # Change if different from x_min
        "x_labeled_nums": [],
        "x_axis_label": "$x$",
        "y_min": -2,
        "y_max": 2,
        "y_axis_height": 4,
        "y_tick_frequency": 0.5,
        "y_bottom_tick": None,  # Change if different from y_min
        "y_labeled_nums": [],
        "y_axis_label": "$y$",
        "axes_color": BLUE,
        "graph_origin": 3*LEFT,
        "exclude_zero_label": True,
        "default_graph_colors": [BLUE, GREEN, YELLOW],
        "default_derivative_color": GREEN,
        "default_input_color": YELLOW,
        "default_riemann_start_color": BLUE,
        "default_riemann_end_color": GREEN,
        "area_opacity": 0.8,
        "num_rects": 50,
    }
    def construct(self):
        ####TEXTOS
        titulo = TextMobject("Curvas Rectificables").scale(1.5)
        text_1 = TextMobject('''Sea $\\gamma$ una curva en $\\mathbb{R}^n$\n
                                $\\gamma: A\\subset\\mathbb{R}\\rightarrow\\mathbb{R}^n$''')
        text_2 = TextMobject('''Como ejemplo, tomemos la curva \n
                                $\\gamma : A=[0,2\\pi]\\rightarrow\\mathbb{R}^2$ \n
                             $\\gamma(t)=\\dfrac{3}{2}(\\cos{(t)},\\sin{(t)})$''')
        funcion_1 = TextMobject('''$\\gamma : A=[0,2\\pi]\\rightarrow\\mathbb{R}^2$\n
                                    $\\gamma(t)=\\dfrac{3}{2}(\\cos{(t)},\\sin{(t)})$''').set_color(YELLOW).scale(0.6).move_to(5.3*LEFT+1.9*UP)
        text_3 = TextMobject('''El dominio de la curva $\\gamma$ es el intervalo $A=[a,b]=[0,2\\pi]\\subset \\mathbb{R}$ ''').move_to(3*UP)
        text_4 = TextMobject('''Definimos una partición $\\mathcal{S}$ de $A$ como ''').move_to(3*UP)
        text_5 = TexMobject(r'''\mathcal{S}:=\{a = t_0, t_1, t_2, ... , t_m = b\}\subset A ''').move_to(3*UP)
        text_6 = TextMobject('''En el ejemplo, sea $\\mathcal{S}:=\\{0 = t_0, t_1, t_2, t_3 = 2\\pi\\}$ ''').move_to(3*UP)
        text_7 = TextMobject('''Como $\\mathcal{S}\subset A$, entonces podemos definir la \n 
                                siguiente sucesión finita de puntos del contradominio de $\\gamma$''').move_to(3.2*UP)
        text_8 = TexMobject(r'''\gamma_{\mathcal{S}}:=\{ \gamma (a)=\gamma (t_0), \gamma (t_1), \gamma (t_2), ..., \gamma (b)=\gamma (t_m) \} ''').move_to(3*UP)
        text_9 = TextMobject("Obsérvese que en el ejemplo, $\\gamma(t_0)=\\gamma(t_m)$").move_to(3*UP)
        text_10 = TextMobject('''A partir de $\gamma_{\mathcal{S}}$ se define una poligonal\n
                                 $\\mathcal{P}$ con vértices en cada punto de $\\gamma_{\\mathcal{S}}$''').move_to(3.2*UP)
        text_11 = TextMobject('''La longitud $d(\\mathcal{P})$ de la poligonal se define como la\n
                                    suma de las longitudes de cada segmento de recta:''').move_to(3.2*UP)
        text_12 = TexMobject(r'''d(\mathcal{P})=\sum_{i=1}^m \left\Vert \gamma(t_i)-\gamma(t_{i-1}) \right\Vert''').move_to(3.2*UP)
        text_12_1 = TextMobject('''En el ejemplo, para esta partición, $d(\\mathcal{P})=7.79$ ''').move_to(3.2*UP)
        text_13 = TextMobject('''Consideremos un refinamiento $\\mathcal{S}'$ de la partición $\\mathcal{S}$  ''').move_to(3.2*UP)
        text_14 = TextMobject('''A partir de $\\mathcal{S}'$ definimos otra poligonal $\\mathcal{P}'$ ''').move_to(3.2*UP)
        text_15 = TextMobject(''' Por ser $\\mathcal{P}'$ refinamiento de $\mathcal{P}$, $d(\mathcal{P}')\geq d(\mathcal{P})$''').move_to(3.2*UP)
        text_15_1 = TextMobject(''' En el ejemplo, para esta partición, $d(\\mathcal{P}')=8.19$''').move_to(3.2*UP)
        text_16_1 = TextMobject("Consideremos el conjunto").move_to(3.6*UP)
        text_16_2 = TextMobject("$L:=\\{ d(\\mathcal{P}) | \\text{$\\mathcal{P}$ es una poligonal sobre $\\gamma$} \}$").move_to(2.9*UP)
        text_16 = VGroup(text_16_1,text_16_2)
        text_17 = TextMobject('''Decimos que $\\gamma$ es una curva rectificable\n
                                 si $L$ es un conjunto acotado superiormente ''').move_to(3.2*UP)
        text_18 = TextMobject(''' Además, $\\text{sup}(L)= \\text{ longitud de curva $\\gamma$}$''').move_to(3.2*UP)
        text_18_0 = TextMobject(''' Para curvas suaves, $\\text{sup}(L)=\\displaystyle\\int_{a}^{b}\\left\\Vert \\gamma'(t) \\right\\Vert dt$''').move_to(3.2*UP)
        text_18_1 = TextMobject("En el ejemplo, $\\text{sup}(L)=3\\pi$").move_to(3.2*UP)
        text_19 = TextMobject(''' En general, una curva en $\\mathbb{R}^n$,  $\\gamma: A\\subset\\mathbb{R}\\rightarrow\\mathbb{R}^n$\n
                                 es rectificable si $\\forall$  $a,b\\in A, a<b$, \n
                                $\\gamma$ es rectificable en $[a,b]$''')
        ###OBJETOS

        #Función
        curva_1 = ParametricFunction(
                lambda u : np.array([
                1.5*math.cos(u),
                1.5*math.sin(u),
                0
            ]),color=YELLOW,t_min=0,t_max=2*PI,
            ).move_to(3*LEFT)
        
        
        #Numberline de Dominio
        numberline_1 = NumberLine(x_min=0,x_max=2*PI+1,unit_size=0.75, tick_frequency=PI/2,
                                include_tip=True,number_scale_val=0.6,numbers_with_elongated_ticks=[0,2*PI],lable_direction=1.2*DOWN).move_to(2.8*LEFT+3*DOWN).set_color(BLUE)
        etiqueta_numberline_1 = TexMobject(r"t").move_to(numberline_1.get_right()+0.4*UP)
        etiqueta_numberline_2 = TexMobject(r"2\pi").move_to(numberline_1.get_right()+0.4*DOWN+0.75*LEFT)
        etiqueta_numberline_3 = TexMobject(r"0").move_to(numberline_1.get_left()+0.4*DOWN)
        etiqueta_numberline_4 = TexMobject(r"\pi").move_to(numberline_1.get_center()+0.4*DOWN+0.4*LEFT)
        etiquetas_numberline = VGroup(etiqueta_numberline_1,etiqueta_numberline_2,etiqueta_numberline_3,etiqueta_numberline_4)
        
        ##########Particiones, Evaluaciones y poligonal con 4 elementos#########
        ####En esta función se generan los puntos de la partición en el dominio, puntos de evaluación, sus poligonales y puntos en diagrama de longitudes para la partición de 4 elementos
        #### La razón por la que este caso no se trató con la función particiones(), es que con estos conjuntos se aplicarán otras animaciones, así como textos particulares
        distancias_poligonales_1 =[]

        conj_puntos_particion_1 = []
        conj_evaluacion_particion_1 = []
        conj_poligonal_particion_1 = []
        suma_distancias_1 = 0

        particion = particion_circulo(0) ##Se añadirán cero puntos al triángulo inscrito
        for i in range(len(particion)):
            punto_dom = Dot().move_to(numberline_1.get_left()+particion[i]*0.75*RIGHT)
            conj_puntos_particion_1.append(punto_dom)
            punto_eval = Dot().move_to((1.5*np.cos(particion[i])-3,1.5*np.sin(particion[i]),0))
            conj_evaluacion_particion_1.append(punto_eval)
            if i<(len(particion)-1):
                linea_poligonal = Line((1.5*np.cos(particion[i])-3,1.5*np.sin(particion[i]),0),(1.5*np.cos(particion[i+1])-3,1.5*np.sin(particion[i+1]),0))
                conj_poligonal_particion_1.append(linea_poligonal)
                suma_distancias_1 += np.linalg.norm(np.array((1.5*np.cos(particion[i])-3,1.5*np.sin(particion[i]),0))-\
                                                    np.array((1.5*np.cos(particion[i+1])-3,1.5*np.sin(particion[i+1]),0)))
        ####Conjuntos con elementos
        puntos_particion_1 = VGroup(*conj_puntos_particion_1)
        puntos_evaluacion_particion_1 = VGroup(*conj_evaluacion_particion_1)
        poligonal_particion_1 = VGroup(*conj_poligonal_particion_1)
        distancias_poligonales_1.append(suma_distancias_1)
        
        ####Animaciones con poligonal
        focus_poligonal_1_1 = []
        for i in range(0,len(conj_poligonal_particion_1)):
            focus_poligonal_1_1.append(FadeToColor(poligonal_particion_1[i],RED,rate_func=there_and_back))
        focus_poligonal_1_2 = []
        for i in range(0,len(conj_poligonal_particion_1)):
            focus_poligonal_1_2.append(FadeToColor(poligonal_particion_1[i],RED,rate_func=there_and_back))

        ##########Particiones, Evaluaciones y poligonal con 5 elementos#########
        ####En esta función se generan los puntos de la partición en el dominio, puntos de evaluación, sus poligonales y puntos en diagrama de longitudes para la partición de 5 elementos
        #### La razón por la que este caso no se trató con la función particiones(), es que con estos conjuntos se aplicarán otras animaciones, así como textos particulares
        conj_puntos_particion_2 = []
        conj_evaluacion_particion_2 = []
        conj_poligonal_particion_2 = []
        suma_distancias_2 = 0

        particion = particion_circulo(1) ##Se añadirán cero puntos al triángulo inscrito
        for i in range(len(particion)):
            punto_dom = Dot().move_to(numberline_1.get_left()+particion[i]*0.75*RIGHT)
            conj_puntos_particion_2.append(punto_dom)
            punto_eval = Dot().move_to((1.5*np.cos(particion[i])-3,1.5*np.sin(particion[i]),0))
            conj_evaluacion_particion_2.append(punto_eval)
            if i<(len(particion)-1):
                linea_poligonal = Line((1.5*np.cos(particion[i])-3,1.5*np.sin(particion[i]),0),(1.5*np.cos(particion[i+1])-3,1.5*np.sin(particion[i+1]),0))
                conj_poligonal_particion_2.append(linea_poligonal)
                suma_distancias_2 += np.linalg.norm(np.array((1.5*np.cos(particion[i])-3,1.5*np.sin(particion[i]),0))-\
                                                    np.array((1.5*np.cos(particion[i+1])-3,1.5*np.sin(particion[i+1]),0)))
        ####Conjuntos con elementos
        puntos_particion_2 = VGroup(*conj_puntos_particion_2)
        puntos_evaluacion_particion_2 = VGroup(*conj_evaluacion_particion_2)
        poligonal_particion_2 = VGroup(*conj_poligonal_particion_2)
        poligonal_particion_2_copy = poligonal_particion_2.copy()
        distancias_poligonales_1.append(suma_distancias_2)
        
        ####Animaciones con poligonal
        focus_poligonal_2_1 = []
        for i in range(0,len(conj_poligonal_particion_1)):
            focus_poligonal_1_1.append(FadeToColor(poligonal_particion_1[i],RED,rate_func=there_and_back))
        focus_poligonal_2_2 = []
        for i in range(0,len(conj_poligonal_particion_1)):
            focus_poligonal_1_2.append(FadeToColor(poligonal_particion_1[i],RED,rate_func=there_and_back))
               
        #### Diagrama de distancias
        #### Los labels y líneas fueron creados aquí mismo con iteraciones for
        EjeY_1 = Arrow(start = (-1,-1,0), end = (-1,4.8,0), stroke_width = 2).set_color(BLUE)
        EjeX_1 = Arrow(start = (-2,0,0), end = (5.0,0,0), stroke_width = 2).set_color(BLUE)
        label_x = TextMobject("Elementos de Partición $\\mathcal{P}$").shift(1.75*RIGHT+0.75*DOWN).scale(0.5)
        label_y = TextMobject("$d(\\mathcal{P})$").move_to(1.75*UP+2.0*LEFT).rotate_in_place(90*DEGREES).scale(0.5)
        etiquetas_eje_x = []
        for i in range(4,14):
            line_x = Line((0.5+0.5*(i-4)-1,-0.05,0),(0.5+0.5*(i-4)-1,0.05,0))
            lable_line_x = TexMobject(round(i,2)).move_to(line_x.get_bottom()+0.25*DOWN).scale(0.6)
            both_1 = VGroup(line_x,lable_line_x)
            etiquetas_eje_x.append(both_1)
        etiquetas_eje_y = []
        for i in range(4,12):
            line_y = Line((-0.05-1,0.2+0.5*(i-4),0),(0.05-1,0.2+0.5*(i-4),0))
            label_line_y = TexMobject(round(7.7+(i-4)*0.2,3)).scale(0.6).move_to(line_y.get_left()+0.35*LEFT)
            both_2 = VGroup(line_y,label_line_y)
            etiquetas_eje_y.append(both_2)
        line_3pi = Line((2-1-0.05,-0.6+0.5*(9.5-4),0),(2-1+0.05,-0.6+0.5*(9.5-4),0))
        label_line_3pi = TexMobject(r"3\pi").scale(0.8).move_to(line_3pi.get_left()+0.4*LEFT+0.1*UP).set_color(YELLOW)
        Ejes_1 = VGroup(EjeX_1, EjeY_1,label_x,label_y,*etiquetas_eje_x,*etiquetas_eje_y).shift(2*RIGHT+2*DOWN)
        recta_3pi = Line((2-1,-0.6+0.5*(9.5-4),0),(6, -0.6+0.5*(9.5-4),0)).set_color(YELLOW)
        ###Puntos en diagrama
        arrow = Arrow((-1.2,1,0),(0.0,1,0)).set_color(RED)
        dot_1 = Dot(color=RED,radius=0.05).move_to((2.5-1,-2.0+0.40,0))
        dist_1 = TexMobject(r"d(\mathcal{P})=7.79").move_to((-0.8,1.5,0)).scale(0.7).set_color(RED_E)
        dot_2 = Dot(color=RED,radius=0.05).move_to((3-1,-2+1.40,0))
        dist_2 = TexMobject(r"d(\mathcal{P}')=8.19").move_to((-0.8,1.5,0)).scale(0.7).set_color(RED_E)
        
        ####ANIMACIONES
        self.play(Write(titulo))
        self.wait(2.75)
        self.FadeOutWrite(titulo,text_1)
        self.wait(6.875)
        self.FadeOutWrite(text_1,text_2)
        self.wait(10)
        self.play(ReplacementTransform(text_2,funcion_1))
        self.setup_axes(animate=True)
        self.wait()
        self.play(ShowCreation(curva_1))
        self.wait()
        self.play(Write(text_3))
        self.wait(9.5)
        self.play(ShowCreation(numberline_1))
        self.play(FadeIn(etiquetas_numberline))
        self.wait()
        self.FadeOutWrite(text_3,text_4)
        self.wait(4.5)
        self.FadeOutWrite(text_4,text_5)
        self.wait(6.9)
        self.FadeOutWrite(text_5,text_6)
        self.play(FadeIn(puntos_particion_1))
        self.wait(3)
        self.FadeOutWrite(text_6,text_7)
        self.wait(7.25)
        self.FadeOutWrite(text_7,text_8)
        self.wait(8.3)
        self.play(Write(puntos_evaluacion_particion_1))
        self.FadeOutWrite(text_8,text_9)
        self.wait(7.6)
        self.FadeOutWrite(text_9,text_10)
        self.wait(5.75)
        self.play(Write(poligonal_particion_1),run_time=3)
        self.FadeOutWrite(text_10,text_11)
        self.wait(7.6)
        self.play(Succession(*focus_poligonal_1_1),run_time=3) ##LINEA 11
        self.FadeOutWrite(text_11,text_12)
        self.wait(7.25)
        self.play(Write(Ejes_1),run_time=3)
        self.wait(6.5)
        self.FadeOutWrite(text_12,text_12_1)
        self.wait(5.3)
        self.play(LaggedStart(*focus_poligonal_1_2),run_time=2) ##LINEA 12
        self.play(ShowCreation(arrow))
        self.play(FadeIn(dot_1),FadeIn(dist_1))
        self.wait(0.5)
        self.play(LaggedStart(*focus_poligonal_1_2),run_time=2) ##LINEA 12
        self.play(FadeOut(dist_1))
        self.play(FadeOut(arrow))
        self.play(FadeOut(poligonal_particion_1))
        self.FadeOutWrite(text_12_1,text_13)
        self.wait(5.3)
        self.play(ReplacementTransform(puntos_particion_1,puntos_particion_2))
        self.wait(0.5)
        self.play(ReplacementTransform(puntos_evaluacion_particion_1,puntos_evaluacion_particion_2))
        self.FadeOutWrite(text_13,text_14)
        self.wait(5.3)
        self.play(Write(poligonal_particion_2),run_time=3)
        self.FadeOutWrite(text_14,text_15)
        self.wait(5.7)
        self.play(ReplacementTransform(poligonal_particion_2,poligonal_particion_1))
        self.play(ReplacementTransform(poligonal_particion_1,poligonal_particion_2_copy))
        self.FadeOutWrite(text_15,text_15_1)
        self.wait(5.7)
        self.play(LaggedStart(*focus_poligonal_2_2),run_time=2) ##LINEA 12
        self.play(ShowCreation(arrow))
        self.play(FadeIn(dot_2),FadeIn(dist_2))
        self.wait(2)
        self.play(FadeOut(dist_2))
        self.play(FadeOut(arrow))
        self.play(FadeOut(puntos_particion_2),FadeOut(puntos_evaluacion_particion_2),FadeOut(poligonal_particion_2_copy))
        self.FadeOutWrite(text_15_1,text_16)
        self.wait(6.8)
        self.play(FadeOut(text_16_1))
        self.play(ShowCreation(arrow))
        self.particiones()
        self.play(FadeOut(arrow))
        self.FadeOutWrite(text_16_2,text_17)
        self.wait(8)
        self.play(ShowCreation(recta_3pi))
        self.FadeOutWrite(text_17,text_18)
        self.wait(5)
        self.FadeOutWrite(text_18,text_18_0)
        self.wait(10)
        self.FadeOutWrite(text_18_0,text_18_1)
        self.wait(4.6)
        self.play(Write(line_3pi))
        self.play(Write(label_line_3pi))
        self.wait(2)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
        self.play(Write(text_19))
        self.wait(13)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )

