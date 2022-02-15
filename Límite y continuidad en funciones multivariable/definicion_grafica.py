from manimlib.imports import *

###Definición de Gráficas###

class Definicion_Graficas(GraphScene,Scene):
    def setup(self):
        Scene.setup(self)
        GraphScene.setup(self)
    
    CONFIG = {
        "x_min": -1,
        "x_max": 4,
        "x_axis_width": 5,
        "x_tick_frequency": 1,
        "x_leftmost_tick": None,  # Change if different from x_min
        "x_labeled_nums": [1,2,3],
        "x_axis_label": "$x$",
        "y_min": -1.5,
        "y_max": 5,
        "y_axis_height": 4,
        "y_tick_frequency": 1,
        "y_bottom_tick": None,  # Change if different from y_min
        "y_labeled_nums": [-1,1,3,5],
        "y_axis_label": "$y$",
        "axes_color": GREY,
        "graph_origin": 2.7 * DOWN + 1.8*LEFT,
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

        #Textos
        titulo = TextMobject("Gráficas de Funciones").scale(1.5)
        
        text_1 = TextMobject("Consideremos la siguiente función:").move_to(3.2*UP)
        ejemplo_1_1 = TexMobject(r"f:[0,3]\subset\mathbb{R}\rightarrow\mathbb{R}")
        ejemplo_1_2 = TexMobject(r"f(x)=5-2x").next_to(ejemplo_1_1,DOWN)
        ejemplo_1 = VGroup(ejemplo_1_1,ejemplo_1_2).next_to(text_1,1.5*DOWN)
        
        text_2_1 = TextMobject("La función $f$ nos permite definir relaciones entre pares")
        text_2_2 = TextMobject("correspondientes del ", "dominio"," y el ","contradominio").next_to(text_2_1,DOWN)
        text_2_2[1].set_color(BLUE_E)
        text_2_2[3].set_color(RED_E)
        text_2 = VGroup(text_2_1,text_2_2).move_to(text_1.get_center())

        text_3_1 = TextMobject("Para cada elemento del ", "dominio", " de $f$")
        text_3_2 = TextMobject("corresponde un sólo elemento del ", "contradominio").next_to(text_3_1,DOWN)
        text_3_1[1].set_color(BLUE_E)
        text_3_2[1].set_color(RED_E)
        text_3 = VGroup(text_3_1,text_3_2).move_to(text_1.get_center())

        text_4_1 = TextMobject("Consideremos las parejas ordenadas")
        text_4_2 = TextMobject("$($", "$x$", " , ", "$f(x)$","$)$, con ", "$x$", " en el dominio de $f$").next_to(text_4_1,DOWN)
        text_4_2[1].set_color(BLUE_E)
        text_4_2[3].set_color(RED_E)
        text_4_2[5].set_color(BLUE_E)
        text_4 = VGroup(text_4_1,text_4_2).move_to(text_1.get_center())

        text_5 = TextMobject("Definimos la ", "gráfica", " de $f$ como el siguiente conjunto:").move_to(3.2*UP)
        text_5[1].set_color(YELLOW_E)
        text_6 = TexMobject(r"G_f:=\{(x,f(x))\in \mathbb{R}^2|x\in[0,3] \}",color= YELLOW_E).next_to(text_5,1*DOWN)
        def_graf = VGroup(text_5,text_6)

        text_7_1 = TextMobject("En general, dada una función $f:A\\subset\\mathbb{R}^n\\rightarrow\\mathbb{R}^m$,")
        text_7_2 = TextMobject("se define la ", "gráfica"," de $f$ de la siguiente forma:" ).next_to(text_7_1,DOWN)
        text_7_2[1].set_color(YELLOW_E)
        text_7 = VGroup(text_7_1,text_7_2).move_to(text_1.get_center()+1*DOWN)

        def_1 = TexMobject(r"G_f:=\{ (x_1,...,x_n,f_1(\vec{x}),...,f_m(\vec{x}))\in\mathbb{R}^{n+m}|\vec{x}=(x_1,...x_n)\in A \}").scale(0.95)
        text_8 = TextMobject("Es decir, ").next_to(def_1,1.5*DOWN)
        def_2 = TexMobject(r"G_f:=\{(\vec{x},f(\vec{x}))\in \mathbb{R}^{n+m}| \vec{x}\text{ en el domino de } f \}").next_to(text_8,1.5*DOWN)
        dt = VGroup(text_8,def_2)
        #RECTAS REALES
        numberline_1 = NumberLine(x_min=0,x_max=4,unit_size=0.75,include_numbers=True,
                                include_tip=True,number_scale_val=0.6,lable_direction=1.2*DOWN).move_to(4.4*LEFT+0.5*UP)
        numberline_2 = NumberLine(x_min=-2,x_max=4,unit_size=0.5,include_numbers=True,
                                numbers_to_show=[-1,1,3],include_tip=True,number_scale_val=0.6,label_direction=1.2*DOWN,numbers_with_elongated_ticks=[]).move_to(4.4*RIGHT+0.5*UP)
        text_numberline_1 = TextMobject("Dominio ($x$)",color=BLUE_E).scale(0.75).move_to(numberline_1.get_bottom()+0.4*DOWN)
        text_numberline_2 = TextMobject("Contradominio (f$(x)$)",color=RED_E).scale(0.75).move_to(numberline_2.get_bottom()+0.4*DOWN)

        #PAREJAS DE PUNTOS X - F(X)

        punto_dom_1 = Dot(color=BLUE_E).move_to((-5.11,0.63,0))
        punto_dom_2 = Dot(color=BLUE_E).move_to((-4.36,0.63,0))
        punto_dom_3 = Dot(color=BLUE_E).move_to((-3.62,0.63,0))
        punto_contra_1 = Dot(color=RED_E).move_to((5.4,0.665,0))
        punto_contra_2 = Dot(color=RED_E).move_to((4.4,0.665,0))
        punto_contra_3 = Dot(color=RED_E).move_to((3.4,0.665,0))

        text_punto_dom_1 = TexMobject(r"x=1",color=BLUE_E).scale(0.75).next_to(text_numberline_1,1.5*DOWN)
        text_punto_dom_2 = TexMobject(r"x=2",color=BLUE_E).scale(0.75).next_to(text_punto_dom_1,1.5*DOWN)
        text_punto_dom_3 = TexMobject(r"x=3",color=BLUE_E).scale(0.75).next_to(text_punto_dom_2,1.5*DOWN)
        text_punto_contra_1 = TexMobject(r"f(1)=3",color=RED_E).scale(0.75).next_to(text_numberline_2,1.5*DOWN)
        text_punto_contra_2 = TexMobject(r"f(2)=1",color=RED_E).scale(0.75).next_to(text_punto_contra_1,1.5*DOWN)
        text_punto_contra_3 = TexMobject(r"f(3)=-1",color=RED_E).scale(0.75).next_to(text_punto_contra_2,1.5*DOWN)
        
        text_puntos = VGroup(text_punto_dom_1,text_punto_dom_2,text_punto_dom_3,text_punto_contra_1,
                            text_punto_contra_2,text_punto_contra_3,text_numberline_1,text_numberline_2)
        #Lineas para puntos

        linea_dom_1 = Line(punto_dom_1.get_center(),ejemplo_1_2.get_left(),color=BLUE_E,path_arc=-0.5)
        linea_dom_2 = Line(punto_dom_2.get_center(),ejemplo_1_2.get_left(),color=BLUE_E,path_arc=-0.5)
        linea_dom_3 = Line(punto_dom_3.get_center(),ejemplo_1_2.get_left(),color=BLUE_E,path_arc=-0.5)
        linea_contra_1 = Line(ejemplo_1_2.get_right(),punto_contra_1.get_center(),color=RED_E,path_arc=-0.5)
        linea_contra_2 = Line(ejemplo_1_2.get_right(),punto_contra_2.get_center(),color=RED_E,path_arc=-0.5)
        linea_contra_3 = Line(ejemplo_1_2.get_right(),punto_contra_3.get_center(),color=RED_E,path_arc=-0.5)

        #GRUPOS PARA FADE OUT
        dom_contra_1 = VGroup(punto_dom_1,punto_contra_1,linea_dom_1,linea_contra_1)
        dom_contra_2 = VGroup(punto_dom_2,punto_contra_2,linea_dom_2,linea_contra_2)
        dom_contra_3 = VGroup(punto_dom_3,punto_contra_3,linea_dom_3,linea_contra_3)
        

        #secuencia de Animaciones

        self.play(Write(titulo))
        self.wait(3)
        self.play(FadeOut(titulo))
        self.play(Write(text_1))
        self.play(Write(ejemplo_1))
        self.wait(10)
        self.play(FadeOut(text_1),FadeOut(ejemplo_1_1))
        self.play(ShowCreation(numberline_1),ShowCreation(numberline_2))
        self.play(Write(text_numberline_1),Write(text_numberline_2))
        self.play(Write(text_2))
        self.wait(7.625)
        self.play(FadeOut(text_2))
        self.play(Write(text_3))
        self.wait(6.875)

        self.play(FadeIn(punto_dom_1),FadeIn(text_punto_dom_1))
        self.play(FadeIn(linea_dom_1))
        self.play(FadeIn(linea_contra_1))
        self.play(FadeIn(punto_contra_1),FadeIn(text_punto_contra_1))
        self.play(FadeOut(dom_contra_1))

        self.play(FadeIn(punto_dom_2),FadeIn(text_punto_dom_2))
        self.play(FadeIn(linea_dom_2))
        self.play(FadeIn(linea_contra_2))
        self.play(FadeIn(punto_contra_2),FadeIn(text_punto_contra_2))
        self.play(FadeOut(dom_contra_2))

        self.play(FadeIn(punto_dom_3),FadeIn(text_punto_dom_3))
        self.play(FadeIn(linea_dom_3))
        self.play(FadeIn(linea_contra_3))
        self.play(FadeIn(punto_contra_3),FadeIn(text_punto_contra_3))
        self.play(FadeOut(dom_contra_3))

        self.wait(0.5)

        self.play(FadeOut(numberline_1),FadeOut(numberline_2),FadeOut(text_3))
        self.play(
                text_puntos.shift,1.7*UP
        )

        #COMIENZA ESCENA CON LOS EJES

        self.setup_axes(animate=True)
        #Función
        f = lambda x: 5-2*x
        graph = self.get_graph(
            f, 
            color = YELLOW_E,
            x_min=0,
            x_max=3
        )
        #Coordenadas y Puntos
        coord_1 = TexMobject(r"(",r"1",r",",r"3",r")").scale(0.75).move_to(0.7*UP+.6*RIGHT)
        coord_1[1].set_color(BLUE_E)
        coord_1[3].set_color(RED_E)
        coord_2 = TexMobject(r"(",r"2",r",",r"1",r")").scale(0.75).next_to(coord_1,1.5*DOWN)
        coord_2[1].set_color(BLUE_E)
        coord_2[3].set_color(RED_E)
        coord_3 = TexMobject(r"(",r"3",r",",r"-1",r")").scale(0.75).next_to(coord_2,1.5*DOWN)
        coord_3[1].set_color(BLUE_E)
        coord_3[3].set_color(RED_E)
        #Grupos para el ReplacementT
        pre_coord_1 = VGroup(text_punto_dom_1,text_punto_contra_1)
        pre_coord_2 = VGroup(text_punto_dom_2,text_punto_contra_2)
        pre_coord_3 = VGroup(text_punto_dom_3,text_punto_contra_3)

        punto_graph_1 = Dot(color=GREEN_E).move_to(self.coords_to_point(1,f(1)))
        punto_graph_2 = Dot(color=GREEN_E).move_to(self.coords_to_point(2,f(2)))
        punto_graph_3 = Dot(color=GREEN_E).move_to(self.coords_to_point(3,f(3)))
        puntos_graph = VGroup(punto_graph_1,punto_graph_2,punto_graph_3)

        self.play(Write(text_4))
        self.wait(8)
        self.play(ReplacementTransform(pre_coord_1,coord_1))
        self.play(FadeIn(punto_graph_1))
        self.play(coord_1.move_to,self.coords_to_point(0.8,f(1)+0.5))
        self.wait(0.5)

        self.play(ReplacementTransform(pre_coord_2,coord_2))
        self.play(FadeIn(punto_graph_2))
        self.play(coord_2.move_to,self.coords_to_point(2.5,f(2)+0.5))
        self.play(ReplacementTransform(pre_coord_3,coord_3))
        self.play(FadeIn(punto_graph_3))
        self.play(coord_3.move_to,self.coords_to_point(3.8,f(3)))
        self.play(FadeOut(text_4))
        self.play(Write(text_5))
        self.wait(5.375)
        self.play(Write(text_6))
        self.wait(8.75)
        self.play(FadeOut(text_numberline_1),FadeOut(text_numberline_2))
        self.play(FadeOut(coord_1),FadeOut(coord_2),FadeOut(coord_3))
        self.play(ShowCreation(graph))
        self.wait(5)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
        self.wait()
        self.play(Write(text_7))
        self.wait(10)
        self.play(Write(def_1))
        self.wait(13)
        self.play(Write(dt))
        self.wait(13)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )