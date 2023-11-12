from manimlib.imports import *

#Visualización de Gráficas (Va después de Gráficas)

def Range(in_val,end_val,step=1):
    return list(np.arange(in_val,end_val+step,step))


### VISUALIZACIÓN DE GRÁFICAS (DIVIDO EN 3 CLASES, PERO ES UN SÓLO VIDEO) ###



#EJEMPLO 1 R -> R#
class Visualización_Gráficas_1(GraphScene,Scene):
    def setup(self):
        Scene.setup(self)
        GraphScene.setup(self)

    CONFIG = {
        "y_max" : 20,
        "y_min" : 0,
        "x_max" : 5,
        "x_min" : 0,
        "y_tick_frequency" : 1,
        "x_tick_frequency" : 1,
        "axes_color" : BLUE, 
        "graph_origin" : np.array((-2.5,-3,0))
    }

    def construct (self):
        
        titulo = TextMobject("Visualización de Gráficas").scale(1.5)
        
        text1_1 = TextMobject("Recordemos que dada una función")
        text1_2 = TexMobject(r"f:A \subset \mathbb{R}^{n} \rightarrow \mathbb{R}^{m}",color=YELLOW).next_to(text1_1,DOWN)
        text1_3 = TextMobject("la gráfica de $f$ es subconjunto de ", "$\mathbb{R}^{n+m}$").next_to(text1_2,DOWN)
        text1_3[1].set_color(YELLOW)
        text1 = VGroup(text1_1,text1_2,text1_3).move_to(0.5*UP)
        
        funcion_1 = TexMobject(r"f:A \subset \mathbb{R} \rightarrow \mathbb{R}").move_to(1*DOWN)
        funcion_2 = TexMobject(r"f:A \subset \mathbb{R}^{2} \rightarrow \mathbb{R}").next_to(funcion_1,DOWN)
        funcion_3 = TexMobject(r"f:A \subset \mathbb{R} \rightarrow \mathbb{R}^{2}").next_to(funcion_2,DOWN)
        funciones = VGroup(funcion_1,funcion_2,funcion_3)
        
        text3 = TextMobject("Ahora, veamos algunos ejemplos")

        text4_1 = TextMobject("Consideremos una recta $x=$ ", "$x_0$", ",").move_to(3.3*UP+2.5*RIGHT)
        text4_2 = TextMobject("¿qué pasa si ", "$x_0$", " pertenece al dominio de $f$?").next_to(text4_1,DOWN)
        text4_1[1].set_color(GREEN_E)
        text4_2[1].set_color(GREEN_E)
        text4 = VGroup(text4_1,text4_2).scale(0.8)

        text5 = TextMobject('''Cada recta intersecta a la gráfica\n
                                en un sólo punto ''').move_to(3.3*UP+2.5*RIGHT).scale(0.8)
        text6 = TextMobject('''¿Qué pasará si $x_0$ no pertenece\n
                             al dominio de $f$?''').move_to(3.3*UP+2.5*RIGHT).scale(0.8)
       
        #PRIMERA CAJA
        funciones.bg =SurroundingRectangle(funciones, buff = 0.8*SMALL_BUFF, color=WHITE)
        Caja = VGroup(funciones.bg,funciones)
        
        #CAJA UPPER LEFT PRE EJEMPLO

        funciones_copy_0 = funciones.copy().to_corner(UL)
        funciones_copy_0.bg = SurroundingRectangle(funciones_copy_0, buff = 0.8*SMALL_BUFF, color=WHITE)
        Caja_0 = VGroup(funciones_copy_0.bg,funciones_copy_0)

        #CAJA EJEMPLO 1

        funcion_1_1 = TexMobject(r"f:A \subset \mathbb{R} \rightarrow \mathbb{R}",color=YELLOW)
        funcion_2_1 = TexMobject(r"f:A \subset \mathbb{R}^{2} \rightarrow \mathbb{R}").next_to(funcion_1_1,DOWN)
        funcion_3_1 = TexMobject(r"f:A \subset \mathbb{R} \rightarrow \mathbb{R}^{2}").next_to(funcion_2_1,DOWN)
        funciones_1 = VGroup(funcion_1_1,funcion_2_1,funcion_3_1).to_corner(UL)
        funciones_1.bg =SurroundingRectangle(funciones_1, buff = 0.8*SMALL_BUFF, color=WHITE)
        Caja_1 = VGroup(funciones_1.bg,funciones_1)
       
        #Texto ejemplo función
        ejemplo_1_1 = TexMobject(r"f(x)=x^{2}",color=YELLOW)
        ejemplo_1_2 = TexMobject(r"G_{f}:=\{(x,f(x))\in \mathbb{R}^{2}|x\in[0,4]\}",color=YELLOW).next_to(ejemplo_1_1,DOWN)
        ejemplo_1 = VGroup(ejemplo_1_1,ejemplo_1_2).move_to(2.8*UP+2*RIGHT)
        #OBJETOS PARA EJEMPLO 1
        dot_1_1 = Dot().set_color(WHITE).move_to(np.array((1.1,-1.8,0)))
        dot_1_x1 = Dot().set_color(WHITE).move_to(np.array((1.1,-3,0)))
        dot_1_y1 = Dot().set_color(WHITE).move_to(np.array((-2.5,-1.8,0)))
        linea_1_x1 = DashedLine(dot_1_x1.get_top(),dot_1_1.get_bottom(),buff=0.1)
        linea_1_x1.set_color(WHITE)
        linea_1_y1 = DashedLine(dot_1_y1.get_right(),dot_1_1.get_left(),buff=0.1)
        linea_1_y1.set_color(WHITE)
        text_dot_1_x1 = TexMobject(r"x=2").move_to(dot_1_x1.get_bottom()+0.5*DOWN).scale(0.75)
        text_dot_1_y1 = TexMobject(r"f(2)=4").move_to(dot_1_y1.get_left()+1.2*LEFT).scale(0.75)
        text_dot_1_1 = TexMobject(r"(2,f(2))").move_to(dot_1_1.get_top()+0.4*UP+0.5*LEFT).scale(0.75)
        

        dot_1_2 = Dot().set_color(WHITE).move_to(np.array((2.9,-0.3,0)))
        dot_1_x2 = Dot().set_color(WHITE).move_to(np.array((2.9,-3,0)))
        dot_1_y2 = Dot().set_color(WHITE).move_to(np.array((-2.5,-0.3,0)))
        linea_1_x2 = DashedLine(dot_1_x2.get_top(),dot_1_2.get_bottom(),buff=0.1)
        linea_1_x2.set_color(WHITE)
        linea_1_y2 = DashedLine(dot_1_y2.get_right(),dot_1_2.get_left(),buff=0.1)
        linea_1_y2.set_color(WHITE)
        text_dot_1_x2 = TexMobject(r"x=3").move_to(dot_1_x2.get_bottom()+0.5*DOWN).scale(0.75)
        text_dot_1_y2 = TexMobject(r"f(3)=9").move_to(dot_1_y2.get_left()+1.2*LEFT).scale(0.75)
        text_dot_1_2 = TexMobject(r"(3,f(3))").move_to(dot_1_2.get_top()+0.4*UP+0.5*LEFT).scale(0.75)

        text_dots_1_1 = VGroup(text_dot_1_1,text_dot_1_2)
        text_dots_1_2 = TextMobject('''$(2,f(2))\\in G_{f}$ \n 
                                    $(3,f(3))\\in G_{f}$''').to_edge(LEFT).scale(0.75)
        text_grafica_1 = TexMobject(r"G_{f}",color=YELLOW).move_to(ejemplo_1.get_bottom()+0.75*DOWN+3*RIGHT)

        ###Rectas verticales
        dot_dom_1 = Dot().set_color(GREEN_E).move_to((1.5,-3.0,0))
        dot_dom_2 = Dot().set_color(GREEN_E).move_to((4,-3.0,0))
        dot_func_1 = Dot().move_to((1.5,-1.5,0))
        dot_func_2 = Dot().move_to((4,0.9,0))
        linea_vert_1 = Line((1.5,-3.5,0),(1.5,1.5,0)).set_color(GREEN_E)
        linea_vert_2 = Line((4,-3.5,0),(4,1.5,0)).set_color(GREEN_E)
        RectVert = VGroup(dot_dom_1,dot_dom_2,dot_func_1,dot_func_2,linea_vert_1,linea_vert_2)
        #Secuencia de Animación
        self.play(Write(titulo))
        self.wait(3)
        self.play(FadeOut(titulo))
        self.play(Write(text1))
        self.wait(9)
        self.play(FadeOut(text1))
        self.play(Write(text3))
        self.wait(3)
        self.play(Write(funciones))
        self.wait(0.5)
        self.play(ShowCreation(funciones.bg))
        self.wait(0.5)
        self.play(FadeOut(text3))
        self.play(ReplacementTransform(Caja,Caja_0))
        #EJEMPLO 1
        self.play(ReplacementTransform(Caja_0,Caja_1))
        self.setup_axes(animate=True)
        graph = self.get_graph(lambda x : x**2, 
                                    color = YELLOW,
                                    x_min = 0, 
                                    x_max = 4
                                    )
        self.play(FadeIn(ejemplo_1))
        self.play(FadeIn(dot_1_1),FadeIn(dot_1_x1),FadeIn(text_dot_1_x1),FadeIn(dot_1_y1),FadeIn(text_dot_1_y1))
        self.wait(2)
        self.play(ShowCreation(linea_1_x1),ShowCreation(linea_1_y1))
        self.play(FadeIn(text_dot_1_1))
        self.wait(2)
        self.play(FadeIn(dot_1_2),FadeIn(dot_1_x2),FadeIn(text_dot_1_x2),FadeIn(dot_1_y2),FadeIn(text_dot_1_y2))
        self.wait(2)
        self.play(ShowCreation(linea_1_x2),ShowCreation(linea_1_y2))
        self.play(FadeIn(text_dot_1_2))
        self.wait(2)
        self.play(FadeOut(text_dot_1_x1),FadeOut(text_dot_1_x2),FadeOut(text_dot_1_y1),FadeOut(text_dot_1_y2))
        self.play(ReplacementTransform(text_dots_1_1,text_dots_1_2))
        self.wait(3)
        self.play(FadeOut(linea_1_x1),FadeOut(linea_1_x2),FadeOut(linea_1_y1),FadeOut(linea_1_y2),FadeOut(dot_1_x1),FadeOut(dot_1_x2),FadeOut(dot_1_y1),FadeOut(dot_1_y2))
        self.play(
            ShowCreation(graph),
            run_time = 3
        )
        self.play(FadeIn(text_grafica_1))
        self.wait()
        self.play(FadeOut(ejemplo_1),FadeOut(dot_1_1),FadeOut(dot_1_2),FadeOut(text_dots_1_2))
        self.play(Write(text4))
        self.wait(6.5)
        self.play(FadeIn(dot_dom_1))
        self.play(ShowCreation(linea_vert_1))
        self.play(FadeOut(text4))
        self.play(FadeIn(text5))
        self.wait(5)
        self.play(FadeIn(dot_func_1))
        self.play(FadeIn(dot_dom_2))
        self.play(ShowCreation(linea_vert_2))
        self.play(FadeIn(dot_func_2))
        self.wait(2.5)
        self.play(FadeOut(RectVert))
        self.play(FadeOut(text5))
        self.play(FadeIn(text6))
        self.wait(7)
        self.play(FadeOut(text_grafica_1),FadeOut(self.axes),FadeOut(graph),FadeOut(text6))

#EJEMPLO 2 R^2 -> R#
class Visualización_Gráficas_2(ThreeDScene,Scene):
    def setup(self):
        Scene.setup(self)
        ThreeDScene.setup(self)
    def acomodar_textos(self,objeto):
        self.add_fixed_in_frame_mobjects(objeto)
        self.play(Write(objeto))
    def FadeOutWrite3D(self,objeto1,objeto2):
        self.play(FadeOut(objeto1))
        self.acomodar_textos(objeto2)
    def punto3D(self):
        bola = ParametricSurface(
            lambda u, v: np.array([
                0.075*np.cos(v) * np.sin(u),
            0.075*np.sin(v) * np.sin(u),
            0.075*np.cos(u)
            ]),v_min=0,v_max=TAU,u_min=0.001,u_max=PI-0.001,
            resolution=(12,24),fill_opacity=1,stroke_color=GREEN_E,fill_color=GREEN_E)
        return bola
    def punto3D_2(self):
        bola = ParametricSurface(
            lambda u, v: np.array([
                0.075*np.cos(v) * np.sin(u),
            0.075*np.sin(v) * np.sin(u),
            0.075*np.cos(u)
            ]),v_min=0,v_max=TAU,u_min=0.001,u_max=PI-0.001,
            resolution=(12,24),fill_opacity=1,stroke_color=GOLD_E,fill_color=GOLD_E)
        return bola
    def construct(self):

        #Caja Ejemplo 1 (Para transición de cajas)
        funcion_1_1 = TexMobject(r"f:A \subset \mathbb{R} \rightarrow \mathbb{R}",color=YELLOW)
        funcion_2_1 = TexMobject(r"f:A \subset \mathbb{R}^{2} \rightarrow \mathbb{R}").next_to(funcion_1_1,DOWN)
        funcion_3_1 = TexMobject(r"f:A \subset \mathbb{R} \rightarrow \mathbb{R}^{2}").next_to(funcion_2_1,DOWN)
        funciones_1 = VGroup(funcion_1_1,funcion_2_1,funcion_3_1).to_corner(UL)
        funciones_1.bg =SurroundingRectangle(funciones_1, buff = 0.8*SMALL_BUFF, color=WHITE)
        Caja_1 = VGroup(funciones_1.bg,funciones_1)

        #CAJA EJEMPLO 2
        funcion_1_2 = TexMobject(r"f:A \subset \mathbb{R} \rightarrow \mathbb{R}")
        funcion_2_2 = TexMobject(r"f:A \subset \mathbb{R}^{2} \rightarrow \mathbb{R}",color=YELLOW).next_to(funcion_1_2,DOWN)
        funcion_3_2 = TexMobject(r"f:A \subset \mathbb{R} \rightarrow \mathbb{R}^{2}").next_to(funcion_2_2,DOWN)
        funciones_2 = VGroup(funcion_1_2,funcion_2_2,funcion_3_2).to_corner(UL)
        funciones_2.bg =SurroundingRectangle(funciones_2, buff = 0.8*SMALL_BUFF, color=WHITE)
        Caja_2 = VGroup(funciones_2.bg,funciones_2)

        #EJEMPLO 2
        
        ejemplo_2_1 = TexMobject(r"f(x,y)=\sin(x)\cos(y)",color=YELLOW)
        ejemplo_2_2 = TexMobject(r"G_{f}:=\{(x,y,f(x,y))\in \mathbb{R}^{3}|(x,y)\in A\}",color=YELLOW).next_to(ejemplo_2_1,DOWN)
        ejemplo_2 = VGroup(ejemplo_2_1,ejemplo_2_2).move_to(3.3*UP+3.6*RIGHT).scale(0.8)
        
        ###Líneas verticales
        text_1 = TextMobject("Consideremos una recta $(x,y,z)=($", "$x_0$",",","$y_0$","$,0)+\\alpha\\hat{z}$, con $\\alpha\\in\\mathbb{R}$").move_to(3.5*UP+2*RIGHT)
        text_1[1].set_color(GREEN_E)
        text_1[3].set_color(GREEN_E)
        text_1_1 = TextMobject("¿qué pasa si ", "$(x_0,y_0)$"," pertence al dominio de $f$?").next_to(text_1,DOWN)
        text_1_1[1].set_color(GREEN_E)
        text_1 = VGroup(text_1,text_1_1).scale(0.7)

        text_2 = TextMobject("La recta intersecta  la gráfica en un sólo punto").move_to(3.3*UP+2*RIGHT).scale(0.6)
        text_3 = TextMobject("¿Qué pasará si ", "$(x_0,y_0)$"," no pertence al dominio de $f$?").move_to(3.3*UP+2*RIGHT).scale(0.6)
        text_3[1].set_color(GREEN_E)
        Superficie = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                np.sin(u)*np.cos(v)
            ]),v_min=-2.5,v_max=4,u_min=-3,u_max=5,checkerboard_colors=[GOLD_E,GOLD_E],
            resolution=(20, 50))
        Superficie2 = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                np.sin(u)*np.cos(v)
            ]),v_min=-2.5,v_max=4,u_min=-3,u_max=5,checkerboard_colors=[GOLD_E,GOLD_E],
            resolution=(20, 50),fill_opacity=0.5)

        axes = ThreeDAxes(x_min=-3,x_max=6,y_min=-3,y_max=6,z_min=-3,z_max=3,num_axis_pieces=40)
        #Creo que es redundante lo del color=WHITE en los Dot, pero no importa
        dot_2_1 = Dot().set_color(RED).move_to(np.array((3*PI/2,2.5,0.8)))
        dot_2_x1 = Dot().set_color(WHITE).move_to(np.array((3*PI/2,0,0)))
        dot_2_y1 = Dot().set_color(WHITE).move_to(np.array((0,2.5,0)))
        dot_2_z1 = Dot().set_color(WHITE).move_to(np.array((0,0,0.8)))
        dot_2_xy1 = Dot().set_color(WHITE).move_to(np.array((3*PI/2,2.5,0)))
        linea_2_x1 = DashedLine(dot_2_x1.get_center(),dot_2_xy1.get_center(),buff=0.1,rate=0.25)
        linea_2_x1.set_color(WHITE)
        linea_2_y1 = DashedLine(dot_2_y1.get_center(),dot_2_xy1.get_center(),buff=0.1)
        linea_2_y1.set_color(WHITE)
        linea_2_z1 = DashedLine(dot_2_z1.get_center(),dot_2_1.get_center(),buff=0.1)
        linea_2_z1.set_color(WHITE)
        linea_2_xy1 = DashedLine(dot_2_xy1.get_center(),dot_2_1.get_center(),buff=0.1)
        linea_2_xy1.set_color(WHITE)
        text_dot_2_x1 = TexMobject(r"x=\frac{3\pi}{2}").move_to(dot_2_x1.get_top()+0.5*UP).scale(0.75)
        text_dot_2_y1 = TexMobject(r"y=2.5").move_to(dot_2_y1.get_left()+1*RIGHT).scale(0.75)
        text_dot_2_z1 = TexMobject(r"f(x,y)=0.8").move_to(dot_2_z1.get_left()+1.5*LEFT).scale(0.75)
        text_dot_2_1 = TexMobject(r"(x,y,f(x,y))",color=RED).move_to(dot_2_1.get_right()+0.8*UP).scale(0.75)
        text_dot_2_xy1 = TexMobject(r"(x,y)\in A").move_to(dot_2_xy1.get_top()+0.5*RIGHT+0.5*UP).scale(0.75)
        gpo_coordxy_2_1 = VGroup(text_dot_2_x1,text_dot_2_y1)
        gpo_coordxyz_2_1 = VGroup(text_dot_2_xy1, text_dot_2_z1)

        text_grafica_2 = TexMobject(r"G_{f}",color=GOLD_E).move_to(4.75*RIGHT+1*DOWN)
        ###Objetos Rectas

        dot_dom_1 = self.punto3D().move_to((PI/2,0,0))
        dot_func_1 = self.punto3D_2().move_to((PI/2,0,1))
        dot_dom_2 = self.punto3D().move_to((0,5,0))
        linea_vert_1 = Line((PI/2,0,-3),(PI/2,0,3)).set_color(GREEN_E)
        linea_vert_2 = Line((0,5,-3),(0,5,3)).set_color(GREEN_E)
        RectVert = VGroup(dot_dom_1,dot_dom_2,dot_func_1,linea_vert_1)


        #EJEMPLO 2
        self.add(Caja_1)
        self.wait(0.5)
        self.play(ReplacementTransform(Caja_1,Caja_2))
        self.add_fixed_in_frame_mobjects(Caja_2)
        self.play(FadeIn(ejemplo_2))
        self.add_fixed_in_frame_mobjects(ejemplo_2)
        self.set_camera_orientation(phi=55 * DEGREES,theta=-50*DEGREES,distance=50)
        self.play(ShowCreation(axes))
        self.wait()        
        self.play(FadeIn(dot_2_x1),FadeIn(text_dot_2_x1))
        self.wait(1.5)
        self.play(FadeIn(dot_2_y1),FadeIn(text_dot_2_y1))
        self.wait(1.5)
        self.play(FadeIn(dot_2_z1),FadeIn(text_dot_2_z1))
        self.wait(1.5)
        self.begin_ambient_camera_rotation(rate=0.04)
        self.play(FadeIn(dot_2_xy1),ReplacementTransform(gpo_coordxy_2_1,text_dot_2_xy1))
        self.play(FadeIn(linea_2_x1))
        self.play(FadeIn(linea_2_y1))
        self.play(FadeIn(dot_2_1))
        self.play(FadeIn(linea_2_xy1),FadeIn(linea_2_z1))
        self.wait(2)
        self.play(ReplacementTransform(gpo_coordxyz_2_1,text_dot_2_1))
        self.wait(3.5)
        self.play(FadeOut(dot_2_xy1),FadeOut(dot_2_x1),FadeOut(dot_2_y1),FadeOut(dot_2_z1),FadeOut(linea_2_x1),FadeOut(linea_2_xy1),FadeOut(linea_2_y1),FadeOut(linea_2_z1),FadeOut(text_dot_2_1))
        self.play(ShowCreation(Superficie))
        self.add_fixed_in_frame_mobjects(text_grafica_2)
        self.wait(23)
        self.stop_ambient_camera_rotation()
        self.play(FadeOut(dot_2_1),FadeOut(text_grafica_2),FadeOut(ejemplo_2))
        self.wait()
        self.acomodar_textos(text_1)
        self.wait(12)
        self.move_camera(phi=75 * DEGREES,theta=-50*DEGREES,distance=50,frame_center=[0,0,1])
        self.play(ReplacementTransform(Superficie,Superficie2))
        self.begin_ambient_camera_rotation(rate=0.04)
        self.play(FadeIn(dot_dom_1))
        self.play(ShowCreation(linea_vert_1))
        self.FadeOutWrite3D(text_1,text_2)
        self.play(FadeIn(dot_func_1))
        self.wait(4.5)
        self.play(FadeOut(dot_dom_1),FadeOut(dot_func_1),FadeOut(linea_vert_1))
        self.FadeOutWrite3D(text_2,text_3)
        self.wait(5)
        self.play(FadeIn(dot_dom_2))
        self.wait(1.5)
        self.play(ShowCreation(linea_vert_2))
        self.stop_ambient_camera_rotation
        self.wait(5)
        self.play(FadeOut(axes),FadeOut(Superficie2),FadeOut(text_3),FadeOut(dot_dom_2),FadeOut(linea_vert_2))



#EJEMPLO 3 R -> R^2#
class Visualización_Gráficas_3(ThreeDScene,Scene):
    def setup(self):
        Scene.setup(self)
        ThreeDScene.setup(self)
    def FadeOutWrite3D(self,objeto1,objeto2):
        self.play(FadeOut(objeto1))
        self.acomodar_textos(objeto2)
    def acomodar_textos(self,objeto):
        self.add_fixed_in_frame_mobjects(objeto)
        self.play(Write(objeto))
    def construct(self):
    

        #CAJA EJEMPLO 2
        funcion_1_2 = TexMobject(r"f:A \subset \mathbb{R} \rightarrow \mathbb{R}")
        funcion_2_2 = TexMobject(r"f:A \subset \mathbb{R}^{2} \rightarrow \mathbb{R}",color=YELLOW).next_to(funcion_1_2,DOWN)
        funcion_3_2 = TexMobject(r"f:A \subset \mathbb{R} \rightarrow \mathbb{R}^{2}").next_to(funcion_2_2,DOWN)
        funciones_2 = VGroup(funcion_1_2,funcion_2_2,funcion_3_2).to_corner(UL)
        funciones_2.bg =SurroundingRectangle(funciones_2, buff = 0.8*SMALL_BUFF, color=WHITE)
        Caja_2 = VGroup(funciones_2.bg,funciones_2)

        #Caja ejemplo 3
        funcion_1_3 = TexMobject(r"f:A \subset \mathbb{R} \rightarrow \mathbb{R}")
        funcion_2_3 = TexMobject(r"f:A \subset \mathbb{R}^{2} \rightarrow \mathbb{R}").next_to(funcion_1_3,DOWN)
        funcion_3_3 = TexMobject(r"f:A \subset \mathbb{R} \rightarrow \mathbb{R}^{2}",color=YELLOW).next_to(funcion_2_3,DOWN)
        funciones_3 = VGroup(funcion_1_3,funcion_2_3,funcion_3_3).to_corner(UL)
        funciones_3.bg =SurroundingRectangle(funciones_3, buff = 0.8*SMALL_BUFF, color=WHITE)
        Caja_3 = VGroup(funciones_3.bg,funciones_3)
       
        text_3 = TextMobject('''No es común en clase graficar funciones de $\\mathbb{R}\\rightarrow\\mathbb{R}^2$\n
                                por la dificultad de hacer los dibujos en pizarrón''')
        text_4 = TextMobject('''Generalmente se trabaja con la imagen de la\n
                                función, dibujando las curvas correspondientes\n
                                 en el plano del contradominio ''')
        text_5 = TextMobject('''En este y otros videos podemos usar\n
                                 la gráfica de este tipo de funciones ''')

        text_6 = TextMobject("Consideremos algunos puntos de la gráfica").move_to(3.3*UP+2*RIGHT).scale(0.8)
        text_7 = TextMobject('''Análogo a los casos anteriores, podemos tomar \n
                                planos paralelos al plano $xy$''').move_to(3.3*UP+2*RIGHT).scale(0.8)
        text_8 = TextMobject('''La intersección de la gráfica con estos\n
                                 planos sólo puede ser un punto''').move_to(3.3*UP+2*RIGHT).scale(0.8)
        text_9 = TextMobject('''Si fuera más de un punto,\n
                                $f$ no sería función''').move_to(3.3*UP+RIGHT).scale(0.8)
        text_10 = TextMobject('''Si la intersección fuera el vacío,\n
                                 el punto correspondiente en el eje t\n
                                 no sería parte del dominio ''').move_to(3.3*UP).scale(0.7)
        #EJEMPLO 3
        
        ejemplo_3_1 = TexMobject(r"f(t)=\frac{t}{4\pi}(\cos(t),\sin(t))",color=YELLOW)
        ejemplo_3_2 = TexMobject(r"G_{f}:=\{(t,f(t))\in \mathbb{R}^{3}|t\in A\}",color=YELLOW).next_to(ejemplo_3_1,DOWN)
        ejemplo_3 = VGroup(ejemplo_3_1,ejemplo_3_2).move_to(3.2*UP).scale(0.65)

        ejemplo_3_10=ejemplo_3.copy().move_to(3.2*UP+4*RIGHT)

        #EJES
        axes_2 = ThreeDAxes(x_min=-3.5,x_max=3.2,y_min=-3.5,y_max=3.5,z_min=0,z_max=5*PI,num_axis_pieces= 30)

        #AQUÍ VAN TODAS LOS PLANOS, PUNTOS Y LA CURVA 
        curva_1 = ParametricFunction(
                lambda u : np.array([
                (u/(4*PI))*math.cos(u),
                (u/(4*PI))*math.sin(u),
                u
            ]),color=YELLOW,t_min=0,t_max=4*PI,
            )  

        plano_1 = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                PI/2
            ]),v_min=-1.5,v_max=1.5,u_min=-1.5,u_max=1.5,fill_color=BLUE_E,fill_opacity=0.25,
            resolution=(1, 1))

        punto_1 = Dot(color=RED).move_to((0,1*1*PI/(8*PI),PI/2))
       
        plano_2 = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                PI
            ]),v_min=-1.5,v_max=1.5,u_min=-1.5,u_max=1.5,fill_color=TEAL_E,fill_opacity=0.25,
            resolution=(1, 1))
       
        punto_2 = Dot(color=RED).move_to((-1*2*PI/(8*PI),0,PI))
       
        plano_3 = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                3*PI/2
            ]),v_min=-1.5,v_max=1.5,u_min=-1.5,u_max=1.5,fill_color=GREEN_E,fill_opacity=0.25,
            resolution=(1, 1))

        punto_3 = Dot(color=RED).move_to((0,-1*3*PI/(8*PI),3*PI/2))

        plano_4 = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                2*PI
            ]),v_min=-1.5,v_max=1.5,u_min=-1.5,u_max=1.5,fill_color=YELLOW_E,fill_opacity=0.25,
            resolution=(1, 1))

        punto_4 = Dot(color=RED).move_to((1*4*PI/(8*PI),0,4*PI/2))

        plano_5 = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                5*PI/2
            ]),v_min=-1.5,v_max=1.5,u_min=-1.5,u_max=1.5,fill_color=GOLD_E,fill_opacity=0.25,
            resolution=(1, 1))

        punto_5 = Dot(color=RED).move_to((0,1*5*PI/(8*PI),5*PI/2))

        plano_6 = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                3*PI
            ]),v_min=-1.5,v_max=1.5,u_min=-1.5,u_max=1.5,fill_color=RED_E,fill_opacity=0.25,
            resolution=(1, 1))

        punto_6 = Dot(color=RED).move_to((-1*6*PI/(8*PI),0,6*PI/2))

        plano_7 = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                7*PI/2
            ]),v_min=-1.5,v_max=1.5,u_min=-1.5,u_max=1.5,fill_color=MAROON_E,fill_opacity=0.25,
            resolution=(1, 1))

        punto_7 = Dot(color=RED).move_to((0,-1*7*PI/(8*PI),7*PI/2))

        plano_8 = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                8*PI/2
            ]),v_min=-1.5,v_max=1.5,u_min=-1.5,u_max=1.5,fill_color=PURPLE_E,fill_opacity=0.25,
            resolution=(1, 1))
        
        punto_8 = Dot(color=RED).move_to((1*8*PI/(8*PI),0,8*PI/2))

        plano_9 = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                9*PI/2
            ]),v_min=-1.5,v_max=1.5,u_min=-1.5,u_max=1.5,fill_color=PURPLE_E,fill_opacity=0.25,
            resolution=(1, 1))

        planos = VGroup(plano_1,plano_2,plano_3,plano_4,plano_5,plano_6,plano_7,plano_8)
        puntos = VGroup(punto_1,punto_2,punto_3,punto_4,punto_5,punto_6,punto_7,punto_8)
        #Etiquetas ejes
        #POR EL MOVIMIENTO DE CÁMARA, TUVE QUE HACER VARIOS DEL MISMO
        eje_x_1 = TexMobject(r"x").scale(0.75).move_to((3.2,0.25,0))
        eje_x_2 = TexMobject(r"x").scale(0.75).move_to((-2.6,1,0))
        eje_x_3 = TexMobject(r"x").scale(0.75).move_to((-2.4,0.75,0))
        eje_y_1 = TexMobject(r"y").scale(0.75).move_to((0.3,3.5,0))
        eje_y_2 = TexMobject(r"y").scale(0.75).move_to((1,-3.3,0))
        eje_y_3 = TexMobject(r"y").scale(0.75).move_to((1.3,-3.5,0))
        eje_z_1 = TexMobject(r"t").scale(0.75).move_to((4.7,2,0))
        eje_z_2 = TexMobject(r"t").scale(0.75).move_to((4.7,1.6,0))
        ejes_1 = VGroup(eje_x_1,eje_y_1)
        ejes_2 = VGroup(eje_x_2,eje_y_2,eje_z_1)
        ejes_3 = VGroup(eje_x_3,eje_y_3,eje_z_2)
        
        #Etiquetas Planos
        text_plano_1 = TexMobject(r"t_1").move_to((-3.65,-3,0)).scale(0.75)
        text_plano_2 = TexMobject(r"t_2").move_to((-2.1,-2.4,0)).scale(0.75)
        text_plano_3 = TexMobject(r"t_3").move_to((-0.62,-1.9,0)).scale(0.75)
        text_planos_1 = VGroup(text_plano_1,text_plano_2,text_plano_3)
        text_plano_4 = TexMobject(r"t_4").move_to((0.7,-1.4 ,0)).scale(0.75)
        text_plano_5 = TexMobject(r"t_5").move_to((2,-1,0)).scale(0.75)
        text_plano_6 = TexMobject(r"t_6").move_to((3.15,-0.5,0)).scale(0.75)
        text_plano_7 = TexMobject(r"t_7").move_to((4.25,-0.05,0)).scale(0.75)
        text_plano_8 = TexMobject(r"t_8").move_to((5.2,0.4,0)).scale(0.75)
        text_planos_2 = VGroup(text_plano_4,text_plano_5,text_plano_6,text_plano_7,text_plano_8,text_plano_1,text_plano_2,text_plano_3)
        text_planos_i = TexMobject(r"\forall i, t_i \in A").move_to((4,-2.5,0)).scale(1.25)
        
        
        text_grafica_3 = TexMobject(r"G_{f}",color=YELLOW).move_to(eje_z_2.get_left()+2.5*LEFT)
        
        #EJEMPLO 3
        self.add(Caja_2)
        self.wait(0.5)
        self.play(ReplacementTransform(Caja_2,Caja_3))
        self.add_fixed_in_frame_mobjects(Caja_3)
        self.play(Write(text_3))
        self.wait(9.5)
        self.play(FadeOut(text_3))
        self.play(Write(text_4))
        self.wait(8.5)
        self.play(FadeOut(text_4))
        self.play(Write(text_5))
        self.wait(7.2)
        self.play(FadeOut(text_5))
        self.wait(0.5)
        self.play(FadeIn(ejemplo_3_10))
        self.set_camera_orientation(phi=0)
        self.play(ShowCreation(axes_2),FadeIn(ejes_1))
        self.wait(0.5)
        self.play(ShowCreation(curva_1))
        self.wait(19)
        self.play(FadeOut(ejes_1),FadeOut(ejemplo_3_10))
        self.move_camera(phi=142 * DEGREES,theta=55*DEGREES,gamma=-60*DEGREES,frame_center=(0.5,0,5),run_time=3)
        self.acomodar_textos(ejes_2)
        self.wait(2.5)
        self.acomodar_textos(text_6)
        self.wait(4)
        self.play(FadeOut(curva_1),FadeIn(puntos))
        self.wait(0.5)
        self.play(FadeOut(ejes_2))
        self.move_camera(phi=115*DEGREES,theta=32*DEGREES,gamma=-70*DEGREES,frame_center=(0,-0.1,6),run_time=2)
        self.wait()
        self.FadeOutWrite3D(text_6,text_7)
        self.wait(6.5)
        self.play(FadeIn(plano_1))
        self.acomodar_textos(text_plano_1)
        self.acomodar_textos(text_planos_i)
        self.play(FadeIn(plano_2))
        self.acomodar_textos(text_plano_2)
        self.FadeOutWrite3D(text_7,text_8)
        self.wait(6.5)
        self.play(FadeIn(plano_3))
        self.acomodar_textos(text_plano_3)
        self.play(FadeIn(plano_4))
        self.acomodar_textos(text_plano_4)
        self.FadeOutWrite3D(text_8,text_9)
        self.wait(5.7)        
        self.play(FadeIn(plano_5))
        self.acomodar_textos(text_plano_5)
        self.play(FadeIn(plano_6))
        self.acomodar_textos(text_plano_6)
        self.FadeOutWrite3D(text_9,text_10)
        self.wait(8.75)        
        self.play(FadeIn(plano_7))
        self.acomodar_textos(text_plano_7)
        self.play(FadeIn(plano_8))
        self.acomodar_textos(text_plano_8)
        self.play(FadeIn(plano_9))
        self.play(ShowCreation(curva_1),run_time=2)
        self.wait(2)
        self.play(FadeOut(plano_9))
        self.play(FadeOut(text_planos_2),FadeOut(text_planos_i),FadeOut(text_10))
        self.move_camera(phi=142 * DEGREES,theta=55*DEGREES,gamma=-60*DEGREES,frame_center=(0,-0.8,5),run_time=2)
        self.acomodar_textos(ejes_3) 
        self.wait(2.5)
        self.play(FadeOut(planos))
        self.acomodar_textos(text_grafica_3)
        self.wait(3)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
        self.wait()