from manimlib.imports import *

#####################################################################################
###### Composición de una superficie con funciones lineales y traslaciones ##########
#####################################################################################

##########esferas
class superficie_1(ParametricSurface):
    def __init__(self, **kwargs):
        kwargs = {
            "u_min": -2,
            "u_max": 2,
            "v_min": -2,
            "v_max": 2,
            "checkerboard_colors": [BLUE_E]
        }
        ParametricSurface.__init__(self, self.func, **kwargs)

    def func(self, u, v):
        # Se puede modificar para cambiar el radio de la esfera
        r = 0.2
        return np.array([u, v, r * np.sin(7 * (v + u))])


class superficie_2(ParametricSurface):
    def __init__(self, **kwargs):
        kwargs = {
            "u_min": 0,
            "u_max": 2 * np.pi,
            "v_min": 0,
            "v_max": np.pi,
            "checkerboard_colors": [BLUE_E]
        }
        ParametricSurface.__init__(self, self.func, **kwargs)

    def func(self, u, v):
        # Se puede modificar para cambiar el radio de la esfera
        r = 1
        return np.array([r * np.cos(u) * np.cos(v), r * np.cos(v) * np.sin(u), r * np.sin(v)])


class superficie_3(ParametricSurface):
    def __init__(self, **kwargs):
        kwargs = {
            "u_min": 0,
            "u_max": 2 * np.pi,
            "v_min": 0,
            "v_max": np.pi,
            "checkerboard_colors": [BLUE_E]
        }
        ParametricSurface.__init__(self, self.func, **kwargs)

    def func(self, u, v):
        # Se puede modificar para cambiar el radio de la esfera
        r = 1
        # Se puede modificar para cambiar la transformación
        k = 0.1
        return np.array([r * np.cos(u) * np.cos(v), r * np.cos(v) * np.sin(u), k * r * np.sin(v)])


class superficie_4(ParametricSurface):
    def __init__(self, **kwargs):
        kwargs = {
            "u_min": 0,
            "u_max": 2 * np.pi,
            "v_min": 0,
            "v_max": np.pi,
            "checkerboard_colors": [BLUE_E]
        }
        ParametricSurface.__init__(self, self.func, **kwargs)

    def func(self, u, v):
        # Se puede modificar para cambiar el radio de la esfera
        r = 1
        # Se puede modificar para cambiar la transformación
        k = 2
        return np.array([r * np.cos(u) * np.cos(v), r * np.cos(v) * np.sin(u), k * r * np.sin(v)])
    #### segundo ejemplo


class superficie_5(ParametricSurface):
    def __init__(self, **kwargs):
        kwargs = {
            "u_min": -2.5,
            "u_max": 2.5,
            "v_min": -2.5,
            "v_max": 2.5,
            "checkerboard_colors": [BLUE_E]
        }
        ParametricSurface.__init__(self, self.func, **kwargs)

    def func(self, x, y):
        return np.array([x, y, (np.sin(3 * (x + y)) + y) * 0.3])


class superficie_5_reflejada(ParametricSurface):
    def __init__(self, **kwargs):
        kwargs = {
            "u_min": -2.5,
            "u_max": 2.5,
            "v_min": -2.5,
            "v_max": 2.5,
            "checkerboard_colors": [BLUE_E]
        }
        ParametricSurface.__init__(self, self.func, **kwargs)

    def func(self, x, y):
        return np.array([x, y, (np.sin(3 * (x - y)) - y) * 0.3])


class superficie_5_reflejada1(ParametricSurface):
    def __init__(self, **kwargs):
        kwargs = {
            "u_min": -2.5,
            "u_max": 2.5,
            "v_min": -2.5,
            "v_max": 2.5,
            "checkerboard_colors": [BLUE_E]
        }
        ParametricSurface.__init__(self, self.func, **kwargs)

    def func(self, x, y):
        return np.array([x, y, (np.sin(3 * (-x + y)) + y) * 0.3])

    #### tercer ejemplo


class superficie_6(ParametricSurface):
    def __init__(self, **kwargs):
        kwargs = {
            "u_min": -1.5,
            "u_max": 1.5,
            "v_min": -1.5,
            "v_max": 1.5,
            "checkerboard_colors": [BLUE_E]
        }
        ParametricSurface.__init__(self, self.func, **kwargs)

    def func(self, x, y):
        # Se puede cambiar a y b para modificar la translación
        a = 0
        b = 0
        return np.array([x + a, y + b, x ** 2 + (y ** 2 * (np.sin(y) ** 2))])


class superficie_6_1(ParametricSurface):
    def __init__(self, **kwargs):
        kwargs = {
            "u_min": -1.5,
            "u_max": 1.5,
            "v_min": -1.5,
            "v_max": 1.5,
            "checkerboard_colors": [BLUE_E]
        }
        ParametricSurface.__init__(self, self.func, **kwargs)

    def func(self, x, y):
        # Se puede cambiar a y b para modificar la translación
        a = -2 
        b = 0
        return np.array([x + a, y + b, x ** 2 + (y ** 2 * (np.sin(y) ** 2))])


class superficie_6_2(ParametricSurface):
    def __init__(self, **kwargs):
        kwargs = {
            "u_min": -1.5,
            "u_max": 1.5,
            "v_min": -1.5,
            "v_max": 1.5,
            "checkerboard_colors": [BLUE_E]
        }
        ParametricSurface.__init__(self, self.func, **kwargs)

    def func(self, x, y):
        # Se puede cambiar a y b para modificar la translación
        a = 0
        b = -2
        return np.array([x + a, y + b, x ** 2 + (y ** 2 * (np.sin(y) ** 2))])


class Composicion_de_Superficie_Con_Funciones(ThreeDScene):
    def construct(self):
        titulo = TextMobject('''Traslaciones y Homotecias \n
                                en Superficies''').scale(1.5)
        # Cambiar función de superficie
        text1 = TextMobject('''Tomemos $f(x,y)=0.2\sin[7(x+y)]$''')
        text2 = TextMobject('''Una translación vertical de la superficie es de \n
                            la forma: $f(x,y)+k$''').move_to(3 * UP)
        text2.bg = SurroundingRectangle(text2, color=WHITE, fill_color=BLACK, fill_opacity=1)
        t_2=VGroup(text2.bg,text2)
        text3 = TextMobject('''Por ejemplo: $f(x,y)-2$ ''').move_to(3 * UP)
        text3.bg = SurroundingRectangle(text3, color=WHITE, fill_color=BLACK, fill_opacity=1)
        t_3=VGroup(text3.bg,text3)
        text4 = TexMobject(r"f(x,y)+3").move_to(2.7 * UP)
        text4.bg = SurroundingRectangle(text4, color=WHITE, fill_color=BLACK, fill_opacity=1)
        t_4=VGroup(text4.bg,text4)
        text5 = TextMobject('''También podemos multiplicar superficies por un escalar, \n
                                    es decir: $kf(x,y)$.''').move_to(3 * UP)
        text5.bg = SurroundingRectangle(text5, color=WHITE, fill_color=BLACK, fill_opacity=1)           
        t_5=VGroup(text5.bg,text5)                  
        text6 = TextMobject('''Si $k=0.1$, la gráfica se encoje verticalmente hacia el plano \n
                                del dominio $xy$''').move_to(2.8 * UP)
        text6.bg = SurroundingRectangle(text6, color=WHITE, fill_color=BLACK, fill_opacity=1) 
        t_6=VGroup(text6.bg,text6)                       
        text7 = TextMobject('''Si $k=2$, la gráfica se estira verticalmente \n
                                alejando los puntos del plano $xy$ ''').move_to(3 * UP)
        text7.bg = SurroundingRectangle(text7, color=WHITE, fill_color=BLACK, fill_opacity=1)
        t_7=VGroup(text7.bg,text7)
        text8 = TextMobject('''También podemos reflejar superficies.\n
                            Sea $f_0(x,y)=[\sin(3(x+y))+y]0.3$''').move_to(3 * UP)
        text8.bg = SurroundingRectangle(text8, color=WHITE, fill_color=BLACK, fill_opacity=1)
        t_8=VGroup(text8.bg,text8)
        text8_1 = TextMobject('''Si $k=-1$, la gráfica de $kf_0(x,y)$ es la reflexión de la gráfica \n
                                de $f_0$ respecto al plano $yz$. ''').move_to(3 * UP)
        text9 = TextMobject('''Si tomamos $f_1(x,y)=f_0(x,-y)$, la gráfica de $f_1$ \n
                                es la reflexión de la gráfica de $f_0$ respecto al plano $xz$.''').move_to(2.5 * UP)
        text9.bg = SurroundingRectangle(text9, color=WHITE, fill_color=BLACK, fill_opacity=1)
        t_9=VGroup(text9.bg,text9)
        text10 = TextMobject('''Mientras que la gráfica de $f_2(x,y)=f_1(-x,-y)$ es una \n
                                    reflexión de la gráfica de $f_1$ respecto al eje vertical. ''').move_to(3 * UP)
        text10.bg = SurroundingRectangle(text10, color=WHITE, fill_color=BLACK, fill_opacity=1)
        t_10=VGroup(text10.bg,text10)
        text11 = TextMobject('''¿Qué pasa con $f(k(x,y))$, con $k\\in\\mathbb{R}$? ''')
        text12 = TextMobject('''También podemos hacer traslaciones horizontales. \n
                                    Por ejemplo:''').move_to(2.7 * UP)
        text12.bg = SurroundingRectangle(text12, color=WHITE, fill_color=BLACK, fill_opacity=1)
        t_12=VGroup(text12.bg,text12)
        text13 = TextMobject('''$g(x,y)=x^{2}+y^{2}\sin^{2}(y)$''').move_to(3 * DOWN)
        text13.bg = SurroundingRectangle(text13, color=WHITE, fill_color=BLACK, fill_opacity=1)
        t_13=VGroup(text13.bg,text13)
        text14 = TextMobject('''La gráfica de $g((x,y)+(2,0))$ se ve: ''').move_to(3 * DOWN)
        text14.bg = SurroundingRectangle(text14, color=WHITE, fill_color=BLACK, fill_opacity=1)
        t_14=VGroup(text14.bg,text14)
        text15 = TextMobject('''Pero la de $g((x,y)+(0,2))$: ''').move_to(3 * DOWN)
        text15.bg = SurroundingRectangle(text15, color=WHITE, fill_color=BLACK, fill_opacity=1)
        t_15=VGroup(text15.bg,text15)
        text16 = TextMobject('''Modifica el código para crear más ejemplos.''')

        ejes = ThreeDAxes(x_max=4.7,y_max=4.5)
        eje_x = TexMobject(r"x").move_to(5.1*RIGHT).scale(1.3)
        eje_y = TexMobject(r"y",fill_color=BLACK).move_to(5*UP).scale(1.3)
        axes = VGroup(ejes,eje_x,eje_y)
        # Superficies
        superficie1 = superficie_1()
        fondo = Rectangle(height=1, width=10, fill_opacity=1, fill_color=BLACK).move_to(text11)

        # Parámetros que se pueden cambiar
        k1 = -2
        superficie2 = superficie_1().move_to([0, 0, k1])
        k2 = 3
        superficie3 = superficie_1().move_to([0, 0, k2])
        superficie4 = superficie_2()
        superficie5 = superficie_3()
        superficie6 = superficie_4()
       
        
        #    
        r1=1
        k1=2

       
       
        superficie7 = superficie_5()
        superficie7_1= ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                (np.sin(3 * (u + v)) + v) * 0.3
            ]),v_min=-2.5,v_max=-1.5,u_min=-2.5,u_max=-1.5,fill_opacity=1,checkerboard_colors=[RED,RED])
        superficie7_2= ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                (np.sin(3 * (u + v)) + v) * 0.3
            ]),v_min=-2.5,v_max=-1.5,u_min=2.5,u_max=1.5,fill_opacity=1,checkerboard_colors=[TEAL_D,TEAL_D])
        superficie7_3= ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                (np.sin(3 * (u + v)) + v) * 0.3
            ]),v_min=2.5,v_max=1.5,u_min=-2.5,u_max=-1.5,fill_opacity=1,checkerboard_colors=[PURPLE_E,PURPLE_E])
        superficie7_4= ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                (np.sin(3 * (u + v)) + v) * 0.3
            ]),v_min=2.5,v_max=1.5,u_min=2.5,u_max=1.5,fill_opacity=1,checkerboard_colors=[PINK,PINK])


        
        superficie7_reflejadayz = superficie_5_reflejada()
        superficie7_reflejadayz1= ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                (np.sin(3 * (u - v)) - v) * 0.3
            ]),v_min=-2.5,v_max=-1.5,u_min=-2.5,u_max=-1.5,fill_opacity=1,checkerboard_colors=[PURPLE_E,PURPLE_E])#PINK
        superficie7_reflejadayz2= ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                (np.sin(3 * (u - v)) - v) * 0.3
            ]),v_min=-2.5,v_max=-1.5,u_min=2.5,u_max=1.5,fill_opacity=1,checkerboard_colors=[PINK,PINK])#PURPLE_E
        superficie7_reflejadayz3= ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                (np.sin(3 * (u - v)) - v) * 0.3
            ]),v_min=2.5,v_max=1.5,u_min=-2.5,u_max=-1.5,fill_opacity=1,checkerboard_colors=[RED,RED])#TEAL_D
        superficie7_reflejadayz4= ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                (np.sin(3 * (u - v)) - v) * 0.3
            ]),v_min=2.5,v_max=1.5,u_min=2.5,u_max=1.5,fill_opacity=1,checkerboard_colors=[TEAL_D,TEAL_D])#RED
        

        superficie8 = superficie_5_reflejada1()
        superficie7_reflejada1= ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                (np.sin(3 * (-u + v)) + v) * 0.3
            ]),v_min=-2.5,v_max=-1.5,u_min=-2.5,u_max=-1.5,fill_opacity=1,checkerboard_colors=[TEAL_D,TEAL_D],resolution=(10,10))#tEAL
        superficie7_reflejada2= ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                (np.sin(3 * (-u + v)) + v) * 0.3
            ]),v_min=-2.5,v_max=-1.5,u_min=2.5,u_max=1.5,fill_opacity=1,checkerboard_colors=[RED,RED])#,resolution=(10,10))#RED
        superficie7_reflejada3= ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                (np.sin(3 * (-u + v)) + v) * 0.3
            ]),v_min=2.5,v_max=1.5,u_min=-2.5,u_max=-1.5,fill_opacity=1,checkerboard_colors=[PINK,PINK])#,resolution=(10,10))#pink
        superficie7_reflejada4= ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                (np.sin(3 * (-u + v)) + v) * 0.3
            ]),v_min=2.5,v_max=1.5,u_min=2.5,u_max=1.5,fill_opacity=1,checkerboard_colors=[PURPLE_E,PURPLE_E],resolution=(7,7))#PURPLE

        superficie9 = superficie_6()
        superficie10 = superficie_6_1()
        superficie11 = superficie_6_2()


        
        self.play(Write(titulo))
        self.wait(6)
        self.play(FadeOut(titulo))
        self.set_camera_orientation(0.7 * np.pi / 2, -0.35 * np.pi, distance=12)
        self.add_fixed_in_frame_mobjects(text1)
        self.play(Write(text1))
        self.wait(4)
        self.play(text1.shift, 3 * UP, runtime=3)
        self.play(ShowCreation(axes))
        self.play(ShowCreation(superficie1))
        self.wait(3)
        self.play(FadeOut(text1))
        self.add_fixed_in_frame_mobjects(t_2)
        self.play(Write(t_2))
        self.wait(8)
        self.play(FadeOut(t_2))
        self.add_fixed_in_frame_mobjects(t_3)
        self.play(Write(t_3))
        self.wait(5)
        self.play(ReplacementTransform(superficie1, superficie2))
        self.wait(5)
        self.play(FadeOut(t_3))
        self.add_fixed_in_frame_mobjects(t_4)
        self.play(Write(t_4))
        # Movimiento de superficie
        self.wait(5)
        self.play(ReplacementTransform(superficie2, superficie3))
        self.wait(6)
        self.play(FadeOut(t_4))
        self.play(FadeOut(superficie3))
        self.add_fixed_in_frame_mobjects(t_5)
        self.play(Write(t_5))
        self.wait(7)
        self.play(ShowCreation(superficie4))
        self.wait(4)
        self.play(FadeOut(t_5))
        self.add_fixed_in_frame_mobjects(t_6)
        self.play(Write(t_6))
        self.wait(6)
        self.play(ReplacementTransform(superficie4, superficie5))
        self.wait(6)
        self.play(FadeOut(t_6))
        self.add_fixed_in_frame_mobjects(t_7)
        self.play(Write(t_7))
        self.wait(9)
        self.play(ReplacementTransform(superficie5, superficie6))
        self.wait(5)
        self.play(FadeOut(t_7))
        self.play(FadeOut(superficie6))
        self.add_fixed_in_frame_mobjects(t_8)
        self.play(Write(t_8))
        self.wait(4)
        ##Superficie reflejada
        self.play(ShowCreation(superficie7),ShowCreation(superficie7_1),ShowCreation(superficie7_2),ShowCreation(superficie7_3),
                                                    ShowCreation(superficie7_4))
        self.wait()
        self.play(FadeOut(t_8))
        self.add_fixed_in_frame_mobjects(t_9)
        self.play(Write(t_9))
        self.wait(5)
 
        # Superficie reflejada 2
        self.wait(3)
        self.play(ReplacementTransform(superficie7, superficie7_reflejadayz),ReplacementTransform(superficie7_1,superficie7_reflejadayz1),
                    ReplacementTransform(superficie7_2,superficie7_reflejadayz2),ReplacementTransform(superficie7_3,superficie7_reflejadayz3),
                    ReplacementTransform(superficie7_4,superficie7_reflejadayz4))
        self.wait(4)
        self.play(FadeOut(t_9))
        self.add_fixed_in_frame_mobjects(t_10)
        self.play(Write(t_10))
        self.wait(11)
        self.play(ReplacementTransform(superficie7_reflejadayz, superficie8),ReplacementTransform(superficie7_reflejadayz1,superficie7_reflejada1),
                    ReplacementTransform(superficie7_reflejadayz2,superficie7_reflejada2),ReplacementTransform(superficie7_reflejadayz3,superficie7_reflejada3),
                    ReplacementTransform(superficie7_reflejadayz4,superficie7_reflejada4))
        self.wait(5)
        self.play(FadeOut(t_10))
        self.play(FadeOut(superficie8),FadeOut(superficie7_reflejada1),FadeOut(superficie7_reflejada2),FadeOut(superficie7_reflejada3),FadeOut(superficie7_reflejada4))
        self.add_fixed_in_frame_mobjects(fondo)
        self.add_fixed_in_frame_mobjects(text11)

        self.play(Write(text11), ShowCreation(fondo))
        self.wait(8)
        self.play(FadeOut(text11), FadeOut(fondo))
        self.add_fixed_in_frame_mobjects(t_12)
        self.play(Write(t_12))
        self.wait(7)
        self.play(FadeOut(t_12))
        self.add_fixed_in_frame_mobjects(t_13)
        self.play(Write(t_13))
        self.wait(6)
        self.play(ShowCreation(superficie9))
        self.wait(5)
        self.play(FadeOut(t_13))
        self.add_fixed_in_frame_mobjects(t_14)
        self.play(Write(t_14))
        self.wait(7)
        self.play(ReplacementTransform(superficie9, superficie10))
        self.wait(5)
        self.play(FadeOut(t_14))
        self.add_fixed_in_frame_mobjects(t_15)
        self.play(Write(t_15))
        self.wait(6)
        self.play(ReplacementTransform(superficie10, superficie11))
        self.wait(5)
        self.play(FadeOut(t_15), FadeOut(axes), FadeOut(superficie11))
        self.add_fixed_in_frame_mobjects(text16)
        self.play(Write(text16))
        self.wait(8)
        self.play(FadeOut(text16))   
