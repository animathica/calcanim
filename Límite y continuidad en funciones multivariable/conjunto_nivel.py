from manimlib.imports import *

########################################
## DEFINICION DE CONJUNTOS DE NIVEL ####
########################################

def Range(in_val,end_val,step=1):
    return list(np.arange(in_val,end_val+step,step))

class ConjNiv_Def(GraphScene,Scene):
    CONFIG = {
        "y_max" : 2,
        "y_min" : -2,
        "x_max" : 4*PI,
        "x_min" : -4*PI,
        "y_tick_frequency" : 0.5,
        "x_tick_frequency" : PI/2,
        "graph_origin" : ORIGIN,
        "y_axis_label": None, # Vamos a poner las labels en el self.setup_axes()
        "x_axis_label": "$x$",
    }
    def construct(self):
        titulo = TextMobject("Conjuntos de Nivel").scale(1.5)

       
        intro_a = TextMobject("Para funciones $f:A\\subset \\mathbb{R}^n \\to \\mathbb{R} $, se").shift(UP)
        intro_b = TextMobject('''define al conjunto de nivel de $f$ como ''').next_to(intro_a,DOWN)
        intro_c = TextMobject("$N_c(f):=\\{ \\vec{x}\\in A| f(\\vec{x})=c\\}$").next_to(intro_b,DOWN)
        intro = VGroup(intro_a,intro_b, intro_c)

       # COMENZAMOS CON LA DEFINICIÓN
       # Conjunto abstracto en R^n
        text_1 = TextMobject("Sea"," A" ," el dominio de una función $f:A\\subset \\mathbb{R}^n \\to \\mathbb{R} $").to_edge(UP)
        text_1[1].set_color(BLUE)

        EjeY_1 = Arrow(start = (0,-1,0), end = (0,4,0), stroke_width = 2)
        EjeX_1 = Arrow(start = (-1,0,0), end = (4,0,0), stroke_width = 2)
        label_Rn = TexMobject(r"\mathbb{R}^n").shift(0.5*RIGHT+0.5*DOWN)
        Ejes_1 = VGroup(EjeX_1, EjeY_1,label_Rn).shift(5*LEFT+2.5*DOWN)
        

        A_svg_1 = SVGMobject('Func_SVGs/enRn.svg').set_height(FRAME_HEIGHT*0.3)
        A_svg_1.set_style(fill_opacity=0.7,stroke_width=0,stroke_opacity=1,fill_color=BLUE)
        A_svg_1.shift(DOWN+3*LEFT)

        # Construimos nuestro eje real sencillo
        text_2 = TextMobject("Consideremos un número real", " $c$", " $\\in \\mathbb{R}$").to_edge(UP)
        text_2[1].set_color(RED_C)

        Linea_Eje_Real = DoubleArrow(start = (-1,0,0), end = (4,0,0), stroke_width = 2, buff = 0.1).shift(2*RIGHT+DOWN)
        ticks = []
        for i in range(20):
            ticks.append(Line(start= (-1+(2*i/10),0.1,0), end = (-1+(2*i/10),-0.1,0),stroke_width = 1).shift(2.6*RIGHT+DOWN))
        label_R =TexMobject(r"\mathbb{R}").shift(1.5*DOWN+2*RIGHT)
        Eje_Real = VGroup(*ticks, Linea_Eje_Real,label_R)

        dot_c = Dot(point = (2.5,0,0), color = RED_C, radius = 0.1).shift(2*RIGHT+DOWN)
        dot_c_dup = Dot(point = (2.5,0,0), color = RED_C, radius = 0.1).shift(2*RIGHT+DOWN)
        label_c = TextMobject("c").set_color(RED_C).next_to(dot_c,1.5*DOWN)
        punto_c = VGroup(dot_c,label_c)

        text_3a = TextMobject("Si tomamos todos los puntos ","$\\vec{x}_i$ ",  "en ", "A", " que al aplicarles la función").to_edge(UP)
        text_3a[3].set_color(BLUE)
        text_3b = TextMobject("toman el valor de", " $c$").next_to(text_3a,DOWN) 
        text_3b[1].set_color(RED_C)
        text_3 = VGroup(text_3a, text_3b).scale(0.9)

        pto_cn1 = Dot(point = (0,0,0)).shift(DOWN+3*LEFT)
        pto_cn1_dup = Dot(point = (0,0,0)).shift(DOWN+3*LEFT)
        pto_cn2 = Dot(point = (0.3,0.1,0)).shift(DOWN+3*LEFT)
        pto_cn2_dup = Dot(point = (0.3,0.1,0)).shift(DOWN+3*LEFT)
        pto_cn3 = Dot(point = (-0.5,0.2,0)).shift(DOWN+3*LEFT)
        pto_cn3_dup = Dot(point = (-0.5,0.2,0)).shift(DOWN+3*LEFT)

        conjniv = VGroup(pto_cn1,pto_cn2, pto_cn3)
        conjniv_dup = VGroup(pto_cn1_dup,pto_cn2_dup, pto_cn3_dup)

        f_arrow = Arrow(start_point = LEFT, end_point = RIGHT+2*DOWN, buff = 0.1)
        f_label = TexMobject(r"f").next_to(f_arrow, UP)
        f = VGroup(f_arrow, f_label)

        text_4a = TextMobject("Entonces el conjunto de puntos $\\vec{x}_i$ es el ").to_edge(UP)
        text_4b = TextMobject("conjunto de nivel $c$ de nuestra función: $N_c(f)$").next_to(text_4a,DOWN)
        text_4 = VGroup(text_4a,text_4b).scale(0.9)

        def_conjniv = TexMobject(r"N_c(f):=\{\vec{x}\in A \vert f(\vec{x}) = c \}").to_edge(UP)
        def_conjniv1 = TextMobject("O, usando la definición de imagen inversa, ").to_edge(UP)
        def_conjniv2 = TexMobject("N_c(f):= f^{-1}(\\{c\\})").next_to(def_conjniv1,DOWN)
        def_conjniv_group = VGroup(def_conjniv1, def_conjniv2)

        text5 = TextMobject("Veamos un ejemplo")

        ### Secuencia de la animación HASTA ANTES DE DECLARAR LOS EJES
        self.play(Write(titulo))
        self.wait(1.15)
        self.play(FadeOut(titulo))
        self.play(Write(intro_a))
        self.play(Write(intro_b))
        self.play(Write(intro_c))
        self.wait(8)
        self.play(FadeOut(intro))
        self.play(Write(text_1),FadeIn(Ejes_1),FadeIn(A_svg_1))
        self.play(FadeIn(Eje_Real))
        self.wait(4.5)
        self.play(FadeIn(punto_c),ReplacementTransform(text_1,text_2))
        self.wait(3.5)
        self.play(ReplacementTransform(text_2,text_3))
        self.play(ShowCreation(conjniv), ShowCreation(f))
        self.wait(7.7)
        self.play(Transform(conjniv_dup,dot_c_dup), runtime = 3)
        self.wait(2)
        self.play(ReplacementTransform(text_3, text_4))
        self.wait(7)
        self.play(ReplacementTransform(text_4,def_conjniv))
        self.wait(4)
        self.play(ReplacementTransform(def_conjniv, def_conjniv_group))
        self.wait(4)
        self.play(FadeOut(punto_c),FadeOut(conjniv_dup),FadeOut(conjniv),FadeOut(A_svg_1),FadeOut(f),
        FadeOut(Ejes_1),FadeOut(Eje_Real))
        self.wait()
        self.play(FadeOut(def_conjniv_group))
        self.play(Write(text5))
        self.wait(2.5)
        self.play(FadeOut(text5))
        """
        A partir de este punto tengo que romper el esquema tradicional de sólo instanciar objetos
        antes de la secuencia de animación. Esto tengo que hacerlo para poder utilizar el método
        coords_to_point() que solo funciona después de declarar los ejes. Si declaro los ejes
        en la sección de objetos, aparecen en toda la animación.
        """

        ##La línea que lo cambia todo (agrega los ejes a la escena)
        self.setup_axes()
        line_1 = Line (start = self.coords_to_point(-4*PI, 1), end = self.coords_to_point(4*PI, 1), stroke_width = 2, color = RED)
        # Ejemplo de funciones R -> R
        text_6 = TextMobject("Obtengamos el conjunto de nivel 1 de ","$f(x) = \\sin(x)$").to_edge(UP).scale(0.8)
        text_6[1].set_color(GREEN)
        text_7 = TextMobject("Este conjunto estará contenido en $\\mathbb{R}$").to_edge(UP).scale(0.8)
        text_8 = TexMobject(r"N_1(f) = \left\{\frac{\pi}{2}+2k\pi \vert k \in \mathbb{Z} \right\}").to_edge(UP).shift(0.5*UP).scale(0.8)
        graph_dotlines = []
        for i in range(-2,2):
            graph_dotlines.append(DashedLine(start = self.coords_to_point((PI/2)+i*2*PI,0), end = self.coords_to_point((PI/2)+i*2*PI,1)))
        Dotlines = VGroup(*graph_dotlines)

        graph_dots =[]
        gdots_dup = []
        GREEN_dots = []
        for i in range(-2,2):
            graph_dots.append(Dot(point = self.coords_to_point((PI/2)+i*2*PI,0), radius = 0.1))
            gdots_dup.append(Dot(point = self.coords_to_point((PI/2)+i*2*PI,0), radius = 0.1))
            GREEN_dots.append(Dot(point = self.coords_to_point((PI/2)+i*2*PI,1), radius = 0.1, color = GREEN))
        GraphDots = VGroup(*graph_dots)
        GDotsDup = VGroup(*gdots_dup)
        GREENDots = VGroup(*GREEN_dots)

        text_9 = TextMobject("Pues para todo $x \in N_c(f)$, se tiene que $\\sin(x) = 1$").to_edge(UP).scale(0.9)


        """
        DECLARO TODOS LOS OBJETOS EN ESTA SECCIÓN, Y DEPUÉS SIGO CON EL ESQUEMA HABITUAL
        """ 

        ### Secuencia de la animación DESPUÉS DE DECLARAR LOS EJES
        self.play(
            *[Write(objeto)
            for objeto in [
                    self.y_axis,
                    self.x_axis,
                    self.x_axis_labels,
                ]
            ],
            run_time=2
        )
        plotSin = self.get_graph(lambda x : np.sin(x), 
                                    color = GREEN,
                                    x_min=-4*PI,
                                    x_max=4*PI,
                                )
        self.play(ShowCreation(plotSin),run_time = 3)
        self.play(Write(text_6))
        self.wait(4.5)
        self.play(ShowCreation(line_1))
        self.wait()
        self.wait(2)
        self.play(ReplacementTransform(text_6,text_7))
        self.wait(3.25)
        self.play(ReplacementTransform(text_7,text_8))
        self.play(ShowCreation(Dotlines))
        self.wait(4)
        self.play(ShowCreation(GraphDots))
        self.wait(2)
        self.play(text_8.shift, 6*DOWN+3*LEFT, runtime = 2)
        self.wait(1.5)
        self.play(Write(text_9))
        self.wait(6)
        self.play(Transform(GDotsDup,GREENDots), runtime = 4)
        self.wait(3)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
        self.wait()

    """
    AQUI SE CONFIGURAN LOS EJES A DETALLE, NO FORMA PARTE DE LA ANIMACIÓN.
    """ 
    def setup_axes(self):
        GraphScene.setup_axes(self)
        # Para cambiar el ancho de los ejes
        self.x_axis.set_stroke(width=2)
        self.y_axis.set_stroke(width=2)
        # Etiquetas en Y
        self.y_axis.label_direction = 0.5*RIGHT+0.5*UP
        self.y_axis.add_numbers(*[-1,1])
        #Lo siguiente es para generar las etiquetas en X automáticamente
        init_val_x = -7*PI/2
        step_x = 2*PI
        end_val_x = 5*PI/2
        # Esta función global nos genera una lista de puntos
        values_decimal_x=Range(init_val_x,end_val_x,step_x)
        self.x_axis_labels = VGroup()
        # Los textos que vamos a escribir
        list_x=TexMobject("-\\frac{7\\pi}{2}", #   -5pi/2
                            "-\\frac{3\\pi}{2}", #   -3pi/2
                            "\\frac{\\pi}{2}", #     pi/2
                            "\\frac{5\\pi}{2}" #     3pi/2
                          )
        #Creamos una lista de tuplas, el valor y el símbolo correspondiente
        values_x = [(i,j)
            for i,j in zip(values_decimal_x,list_x)
        ]
        
        for x_val, x_tex in values_x:
            x_tex.scale(0.5)
            if x_val == -PI or x_val == PI: #if x is equals -pi or pi
                x_tex.next_to(self.coords_to_point(x_val, 0), 2*DOWN) #Put 2*Down
            else: # In another case
                x_tex.next_to(self.coords_to_point(x_val, 0), DOWN)
            self.x_axis_labels.add(x_tex)