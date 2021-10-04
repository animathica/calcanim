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
        a = 2
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
        b = 2
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
                                es la reflexión de la gráfica de $f_0$ respecto al plano $yz$.''').move_to(2.5 * UP)
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

        axes = ThreeDAxes()
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

        superficie7 = superficie_5()
        superficie7_reflejadayz = superficie_5_reflejada()
        superficie8 = superficie_5_reflejada1()

        superficie9 = superficie_6()
        superficie10 = superficie_6_1()
        superficie11 = superficie_6_2()

        self.play(Write(titulo))
        self.wait(6)
        self.play(FadeOut(titulo))
        self.set_camera_orientation(0.7 * np.pi / 2, 0.25 * np.pi, distance=12)
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
        self.play(ShowCreation(superficie7))
        self.wait()
        self.play(FadeOut(t_8))
        self.add_fixed_in_frame_mobjects(t_9)
        self.play(Write(t_9))
        self.wait(5)
        # Superficie reflejada 2
        self.wait(3)
        self.play(ReplacementTransform(superficie7, superficie7_reflejadayz))
        self.wait(4)
        self.play(FadeOut(t_9))
        self.add_fixed_in_frame_mobjects(t_10)
        self.play(Write(t_10))
        self.wait(11)
        self.play(ReplacementTransform(superficie7_reflejadayz, superficie8))
        self.wait(5)
        self.play(FadeOut(t_10))
        self.play(FadeOut(superficie8))
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

#####################################################################################
#############  Límite de cocientes de funciones de dos variables ####################
#####################################################################################


#Definición de las superficies
class superficie2_1_1(ParametricSurface):
    def __init__(self, **kwargs):
        kwargs = {
        "u_min": -3,
        "u_max": -0.3,
        "v_min": -3,
        "v_max": -0.3,
        "checkerboard_colors": [ORANGE]
        }
        ParametricSurface.__init__(self, self.func, **kwargs)
    def func(self, x, y):
        return np.array([x,y,1/(x*y)])

class superficie2_1_2(ParametricSurface):
    def __init__(self, **kwargs):
        kwargs = {
        "u_min": 3,
        "u_max": 0.3,
        "v_min": 3,
        "v_max": 0.3,
        "checkerboard_colors": [ORANGE]
        }
        ParametricSurface.__init__(self, self.func, **kwargs)
    def func(self, x, y):
        return np.array([x,y,1/(x*y)])
class superficie2_1_3(ParametricSurface):
    def __init__(self, **kwargs):
        kwargs = {
        "u_min": -3,
        "u_max": -0.3,
        "v_min": 3,
        "v_max": 0.3,
        "checkerboard_colors": [ORANGE]
        }
        ParametricSurface.__init__(self, self.func, **kwargs)
    def func(self, x, y):
        return np.array([x,y,1/(x*y)])
class superficie2_1_4(ParametricSurface):
    def __init__(self, **kwargs):
        kwargs = {
        "u_min": 3,
        "u_max": 0.3,
        "v_min": -3,
        "v_max": -0.3,
        "checkerboard_colors": [ORANGE]
        }
        ParametricSurface.__init__(self, self.func, **kwargs)
    def func(self, x, y):
        return np.array([x,y,1/(x*y)])
#Segunda superficie del video
##############
class superficie2_2_1(ParametricSurface):
    def __init__(self, **kwargs):
        kwargs = {
        "u_min": -3.5,
        "u_max": -0.0001,
        "v_min": -3.5,
        "v_max": -0.0001,
        "checkerboard_colors": [BLUE_E]
        }
        ParametricSurface.__init__(self, self.func, **kwargs)
    def func(self, x, y):
        return np.array([x,y,2*(x*y)/(x**2+y**2) ])
class superficie2_2_2(ParametricSurface):
    def __init__(self, **kwargs):
        kwargs = {
        "u_min": 3.5,
        "u_max": 0.0001,
        "v_min": 3.5,
        "v_max": 0.0001,
        "checkerboard_colors": [BLUE_E]
        }
        ParametricSurface.__init__(self, self.func, **kwargs)
    def func(self, x, y):
        return np.array([x,y,2*(x*y)/(x**2+y**2) ])

class superficie2_2_3(ParametricSurface):
    def __init__(self, **kwargs):
        kwargs = {
        "u_min": -3.5,
        "u_max": -0.0001,
        "v_min": 3.5,
        "v_max": 0.0001,
        "checkerboard_colors": [BLUE_E]
        }
        ParametricSurface.__init__(self, self.func, **kwargs)
    def func(self, x, y):
        return np.array([x,y,2*(x*y)/(x**2+y**2) ])

class superficie2_2_4(ParametricSurface):
    def __init__(self, **kwargs):
        kwargs = {
        "u_min": 3.5,
        "u_max": 0.0001,
        "v_min": -3.5,
        "v_max": -0.0001,
        "checkerboard_colors": [BLUE_E]
        }
        ParametricSurface.__init__(self, self.func, **kwargs)
    def func(self, x, y):
        return np.array([x,y,2*(x*y)/(x**2+y**2) ])

class superficie2_3(ParametricSurface):
    def __init__(self, **kwargs):
        kwargs = {
        "u_min": -3,
        "u_max": 3,
        "v_min": -3,
        "v_max": 3,
        "fill_color": BLUE_C,
        "pre_function_handle_to_anchor_scale_factor": 0.0000001,
        "fill_opacity": 1.0,
        "checkerboard_colors": [BLUE_C, BLUE_D],
        "stroke_color": LIGHT_GREY,
        "pre_function_handle_to_anchor_scale_factor": 0.00001
        }
        ParametricSurface.__init__(self, self.func, **kwargs)
    def func(self, x, y):

        return np.array([x,y,0])
def curva(t):
    return np.array([t**3,t,1])
def curva1(t):
    return np.array([t**3,t,0])
#cuarta superficie
class superficie2_4_1(ParametricSurface):
    def __init__(self, **kwargs):
        kwargs = {
        "u_min": -2.7,
        "u_max": -0.3,
        "v_min": -2.7,
        "v_max": 2.7,
        "checkerboard_colors": [BLUE_E]
        }
        ParametricSurface.__init__(self, self.func, **kwargs)
    def func(self, x, y):
       return np.array([x,y,1/(2*x)**2])
class superficie2_4_2(ParametricSurface):
    def __init__(self, **kwargs):
        kwargs = {
        "u_min": 0.3,
        "u_max": 2.7,
        "v_min": -2.7,
        "v_max": 2.7,
        "checkerboard_colors": [BLUE_E]
        }
        ParametricSurface.__init__(self, self.func, **kwargs)
    def func(self, x, y):
       return np.array([x,y,1/(2*x)**2])
class superficie2_4_3(ParametricSurface):
    def __init__(self, **kwargs):
        kwargs = {
        "u_min": 0.2,
        "u_max": 4,
        "v_min": 0.2,
        "v_max": 4,
        "checkerboard_colors": [BLUE_E]
        }
        ParametricSurface.__init__(self, self.func, **kwargs)
    def func(self, x, y):
       return np.array([x,y,((x-y)**2)**(1/2)/(x+y)**2])

class superficie2_4_4(ParametricSurface):
    def __init__(self, **kwargs):
        kwargs = {
        "u_min": -0.2,
        "u_max": -3,
        "v_min": -0.2,
        "v_max": -3,
        "checkerboard_colors": [BLUE_E]
        }
        ParametricSurface.__init__(self, self.func, **kwargs)
    def func(self, x, y):
       return np.array([x,y,((x-y)**2)**(1/2)/(x+y)**2])

class Limite_de_cocientes_de_dos_variables (ThreeDScene):
    ### Parte 1 de la animación
    def parte0 (self):
        titulo=TextMobject('''Límite de Cocientes \n
                                de Funciones de Dos Variables''').scale(1.5)
        text1=TextMobject(''' Cuando trabajamos con límites en funciones de $\\mathbb{R}^{2}\\rightarrow\\mathbb{R}$ ''','''\n
                                la cosa se pone interesante debido a que en este''','''\n
                                  caso tenemos diversas maneras de analizar  \n
                                 el límite: métrica, direcciones, curvas, sucesiones.''')
        text2=TextMobject('''Así, para argumentar que existe o no el límite,''','''\n
                                 esto se complica, en comparación con el caso''','''\n
                                    en que la variable es real.''')
        text3=TextMobject('''Pero no todo está perdido, hay diversos detalles \n
                                con los que podemos argumentar si el \n
                                 límite existe o no.''')
        text4=TextMobject('''Ilustremos esto con algunos ejemplos.''')

        self.play(Write(titulo))
        self.wait(5)
        self.play(FadeOut(titulo))
        self.play(Write(text1[0]))
        self.play(Write(text1[1]))
        self.play(Write(text1[2]))
        self.wait(11)
        self.play(FadeOut(text1))
        self.play(Write(text2[0]))
        self.play(Write(text2[1]))
        self.play(Write(text2[2]))
        self.wait(13.5)
        self.play(FadeOut(text2))
        self.play(Write(text3))
        self.wait(10)
        self.play(FadeOut(text3))
        self.play(Write(text4))
        self.wait(7)
        self.play(FadeOut(text4))
        self.wait()
    def parte1 (self):
        text5=TextMobject('''Sea $f:\\mathbb{R}^{2}-\\{(x,y)\\in \\mathbb{R}^{2}:x=0\\ \\text{ó}\\ y=0\\}\\rightarrow\\mathbb{R}$''',''' $$f(x,y)=\\frac{1}{xy}$$ ''')
        t_5_1=TextMobject('''$$f(x,y)=\\frac{1}{xy}$$''').move_to(3*UP)
        t_5_1.bg = SurroundingRectangle(t_5_1, color=WHITE, fill_color=BLACK, fill_opacity=1)
        text5_1=VGroup(t_5_1.bg,t_5_1)
        t_6=TextMobject('''Si nos acercamos al origen en la dirección \n
                                dada por la recta identidad, la función \n
                                diverge a $\\infty$.''' ).move_to(3*DOWN)
        t_6.bg = SurroundingRectangle(t_6, color=WHITE, fill_color=BLACK, fill_opacity=1)
        text6=VGroup(t_6.bg,t_6)
        text6_1=TextMobject('''El límite con una sucesión. ''').move_to(3*UP)
        text6_1_1=TextMobject('''Coordenadas iguales y positivas. ''').move_to(2.5*UP)

        g_text6_1=  VGroup(text6_1,text6_1_1)
        g_text6_1.bg = SurroundingRectangle(g_text6_1, color=WHITE, fill_color=BLACK, fill_opacity=1)
        g2_text6_1=VGroup(g_text6_1.bg,g_text6_1)

        text6_1_2=TextMobject('''Ahora con coordenadas iguales y negativas. ''').move_to(2.5*UP)
        t_6_2=TextMobject('''Con límite direccional. ''').move_to(3*UP)
        t_6_2.bg=SurroundingRectangle(t_6_2, color=WHITE, fill_color=BLACK, fill_opacity=1)
        text6_2=VGroup(t_6_2.bg,t_6_2)


        g_text6_1_2=  VGroup(text6_1,text6_1_2)
        g_text6_1_2.bg = SurroundingRectangle(g_text6_1_2, color=WHITE, fill_color=BLACK, fill_opacity=1)
        g2_text6_1_2=VGroup(g_text6_1.bg,g_text6_1)

        #objetos
        axes=ThreeDAxes()
        #Definimos la superficies por partes por la discontinuidad
        superficie1_1=superficie2_1_1()
        superficie1_2=superficie2_1_2()
        superficie1_3=superficie2_1_3()
        superficie1_4=superficie2_1_4()
        superficie=VGroup(superficie1_1,superficie1_2,superficie1_3,superficie1_4)
        ## Movimiento para la primer convergencia en función +1/xy
        #para z>0
        #Pueden cambiarse los valores n1_1,n1_2, t1_1,t1_1f,t1_2,t1_2f
        #Para cambiar los limites en los cuales se muestran los límites con sucesiones y direccionales
        n1_1= 17 +17
        cjto1_1 = []
        for i in range(2,n1_1):
            if i<= 17:
                x = -3+(0.1*i)
            if i > 17:
                x= -3+(0.1*17)+((i-17)*0.06)
            cjto1_1.append((x,x,1/(x*x)))##Puede cambiarse el conjunto de puntos a una forma general (x,y,1/(x*y))
            #siempre y cuando sólo implemente la variable x para modificar el movimiento de la sucesión
        n1_2= 17+17
        cjto1_2 = []
        for i in range(2,n1_2):
            if i<=17:
                x = 3-(0.1*i)
            if i>17:
                x = 3-(0.1*17)-((i-17)*0.06)
            cjto1_2.append((x,x,1/(x*x)))##Puede cambiarse el conjunto de puntos a una forma general (x,y,1/(x*y))
            #siempre y cuando sólo implemente la variable x para modificar el movimiento de la sucesión
        #Con sucesiones
        Elementos1_1 = [Dot(color=RED).set_color(RED_E).move_to(i) for i in cjto1_1]
        Elementos11 = VGroup(*Elementos1_1)
        Elementos1_2 = [Dot(color=RED).set_color(RED_E).move_to(i) for i in cjto1_2]
        Elementos12 = VGroup(*Elementos1_2)



        ##
        #Con limite direccional
        t1_1=ValueTracker(-3)
        punto_convergencia1=Sphere(radius=0.05, fill_opacity=1, fill_color = RED).move_to([-3,-3,1/(9)])
        t1_1f=-0.45
        def mov_sup1 (obj):
            t = t1_1.get_value()
            punto_convergencia1.become(Sphere(radius=0.05, fill_opacity=1, fill_color = RED).move_to([t,t,t**(-2)]))##Puede cambiarse el conjunto de puntos a una forma general (x,y,1/(x*y))
            #siempre y cuando sólo implemente la variable x para modificar el movimiento del límite direccional

        punto_convergencia1.add_updater(mov_sup1)

        #Movimiento del punto en la recta identidad parte positiva
        t1_2=ValueTracker(3)
        punto_convergencia2=Sphere(radius=0.05, fill_opacity=1, fill_color = RED).move_to([3,3,1/(9)])
        t1_2f=0.3
        def mov_sup2 (obj):
            t = t1_2.get_value()
            punto_convergencia2.become(Sphere(radius=0.05, fill_opacity=1, fill_color = RED).move_to([t,t,t**(-2)]))##Puede cambiarse el conjunto de puntos a una forma general (x,y,1/(x*y))
            #siempre y cuando sólo implemente la variable x para modificar el movimiento del límite direccional

        punto_convergencia2.add_updater(mov_sup2)


        #Pueden modificarles los runtime que aparece para mostrar más rápido o lento el movimiento del límite de la sucesión
        self.play(Write(text5))
        self.wait(7)
        self.play(FadeOut(text5))
        self.set_camera_orientation(0.7*np.pi/2, 1*np.pi,distance=12)
        self.play(ShowCreation(axes))
        self.play(ShowCreation(superficie))
        self.add_fixed_in_frame_mobjects(text5_1)
        self.play(Write(text5_1))
        self.wait(4)
        self.play(FadeOut(text5_1))
        self.add_fixed_in_frame_mobjects(text6)
        self.play(Write(text6))
        self.wait(11)
        self.play(FadeOut(text6))

        
        self.add_fixed_in_frame_mobjects(g2_text6_1)
        self.play(Write(g2_text6_1))
        self.play(ShowCreation(Elementos11), run_time=10)
        self.wait()
        self.play(FadeOut(Elementos11),FadeOut(g2_text6_1))
        #Con limite direccional
        self.add_fixed_in_frame_mobjects(text6_2)
        self.play(Write(text6_2))
        self.add(punto_convergencia1)
        self.play(t1_1.set_value, t1_1f,run_time=10)
        self.wait()
        self.play(FadeOut(text6_2),FadeOut(punto_convergencia1))
        self.move_camera(0.7*np.pi/2, 0*np.pi,distance=12)
        self.add_fixed_in_frame_mobjects(g2_text6_1_2)
        self.play(Write(g2_text6_1_2))
        
        self.play(ShowCreation(Elementos12), run_time=10)
        self.wait()
        self.play(FadeOut(Elementos12),FadeOut(g2_text6_1_2))
        self.add_fixed_in_frame_mobjects(text6_2)
        self.play(Write(text6_2))
        self.add(punto_convergencia2)
        self.play(t1_2.set_value, t1_2f,run_time=10)
        self.wait()
        self.play(FadeOut(superficie),FadeOut(axes),
                    FadeOut(text6_2),FadeOut(punto_convergencia2))
        self.wait()
    def parte2 (self):
        text7=TextMobject('''Sin embargo, si nos acercamos por la recta menos \n
                                identidad, la función diverge a $-\\infty$.''')
        text7_1=TextMobject('''El límite con una sucesión. ''').move_to(3*UP)
        text7_1_1=TextMobject('''Primera coordenada positiva y segunda negativa. ''').move_to(2.5*UP)
        text7_1_2=TextMobject('''Primera coordenada negativa y segunda positiva. ''').move_to(2.5*UP)
        t_7_2=TextMobject('''Con límite direccional. ''').move_to(3*UP)
        t_7_2.bg = SurroundingRectangle(t_7_2, color=WHITE, fill_color=BLACK, fill_opacity=1)
        text7_2 = VGroup(t_7_2.bg,t_7_2)

        g_text7_1_1 = VGroup(text7_1,text7_1_1)
        g_text7_1_1.bg = SurroundingRectangle(g_text7_1_1, color=WHITE, fill_color=BLACK, fill_opacity=1)
        g2_text7_1_1 = VGroup(g_text7_1_1.bg,g_text7_1_1)

        g_text7_1_2 = VGroup(text7_1,text7_1_2)
        g_text7_1_2.bg = SurroundingRectangle(g_text7_1_2, color=WHITE, fill_color=BLACK, fill_opacity=1)
        g2_text7_1_2 = VGroup(g_text7_1_2.bg,g_text7_1_2)

        g_text7_1_3 = VGroup(t_7_2,text7_1_2)
        g_text7_1_3.bg = SurroundingRectangle(g_text7_1_3, color=WHITE, fill_color=BLACK, fill_opacity=1)
        g2_text7_1_3 = VGroup(g_text7_1_3.bg,g_text7_1_3)


        #objetos
        axes=ThreeDAxes()
        #Definimos la superficies por partes por la discontinuidad
        superficie1_1=superficie2_1_1()
        superficie1_2=superficie2_1_2()
        superficie1_3=superficie2_1_3()
        superficie1_4=superficie2_1_4()
        superficie=VGroup(superficie1_1,superficie1_2,superficie1_3,superficie1_4)

        #Analogo a la parte anterior pueden moficiarse los valores n's y t's así como los conjuntos de posiciones para modificar el movimiento de las sucesiones y límites direccionales
        #z<0
        #Con sucesiones
        n1_3= 17 +17
        cjto1_3 = []
        for i in range(2,n1_3):
            if i<= 17:
                x = -3+(0.1*i)
            if i > 17:
                x= -3+(0.1*17)+((i-17)*0.06)
            cjto1_3.append((x,-x,-1/(x**2)))
        n1_4= 17+17
        cjto1_4 = []
        for i in range(2,n1_4):
            if i<=17:
                x = 3-(0.1*i)
            if i>17:
                x = 3-(0.1*17)-((i-17)*0.06)
            cjto1_4.append((x,-x,-1/(x**2)))

        Elementos1_3 = [Dot(color=RED).set_color(RED_E).move_to(i) for i in cjto1_3]
        Elementos13 = VGroup(*Elementos1_3)
        Elementos1_4 = [Dot(color=RED).set_color(RED_E).move_to(i) for i in cjto1_4]
        Elementos14 = VGroup(*Elementos1_4)
        #Con limite direccional
        #Con limite direccional
        t1_1=ValueTracker(-3)
        punto_convergencia1=Sphere(radius=0.05, fill_opacity=1, fill_color = RED).move_to([-3,-3,1/(9)])
        t1_1f=-0.45
        def mov_sup1 (obj):
            t = t1_1.get_value()
            punto_convergencia1.become(Sphere(radius=0.05, fill_opacity=1, fill_color = RED).move_to([t,-t,-t**(-2)]))

        punto_convergencia1.add_updater(mov_sup1)

        #Movimiento del punto en la recta identidad parte positiva
        t1_2=ValueTracker(3)
        punto_convergencia2=Sphere(radius=0.05, fill_opacity=1, fill_color = RED).move_to([3,3,1/(9)])
        t1_2f=0.3
        def mov_sup2 (obj):
            t = t1_2.get_value()
            punto_convergencia2.become(Sphere(radius=0.05, fill_opacity=1, fill_color = RED).move_to([t,-t,-t**(-2)]))
        punto_convergencia2.add_updater(mov_sup2)

        #Animación
        self.add_fixed_in_frame_mobjects(text7)
        self.play(Write(text7))
        self.wait(10)
        self.play(FadeOut(text7))
        self.set_camera_orientation(0.7*np.pi/2, 0.50*np.pi,distance=12)
        self.play(ShowCreation(axes))
        self.play(ShowCreation(superficie))

        self.add_fixed_in_frame_mobjects(g2_text7_1_1)
        self.play(Write(g2_text7_1_1))
        self.play(ShowCreation(Elementos13), run_time=10)
        self.wait()
        self.play(FadeOut(Elementos13),FadeOut(g2_text7_1_1))

        self.add_fixed_in_frame_mobjects(text7_2)
        self.play(Write(text7_2))
        self.add(punto_convergencia1)
        self.play(t1_1.set_value, t1_1f,run_time=10)
        self.play(FadeOut(punto_convergencia1),FadeOut(text7_2))
        self.move_camera(0.7*np.pi/2, 1.35*np.pi,distance=12)

        self.add_fixed_in_frame_mobjects(g2_text7_1_2)
        self.play(Write(g2_text7_1_2))
        self.play(ShowCreation(Elementos14), run_time=10)
        self.wait()
        self.play(FadeOut(Elementos14),FadeOut(g2_text7_1_2))
        self.add_fixed_in_frame_mobjects(g2_text7_1_3)

        self.play(Write(g2_text7_1_3))
        self.add(punto_convergencia2)
        self.play(t1_2.set_value, t1_2f,run_time=10)
        self.play(FadeOut(punto_convergencia2),FadeOut(g2_text7_1_3),
                FadeOut(axes),FadeOut(superficie))
        self.wait()

    def parte3 (self):
        text8=TextMobject('''Veamos otro ejemplo.''')
        t_9=TextMobject('''Sea $f:\\mathbb{R}^{2}-{\\vec{0}}\\rightarrow\\mathbb{R}$ \n
                                $f(x,y)=\\frac{2xy}{x^2+y^2}$''').move_to(3*UP)
        t_9.bg = SurroundingRectangle(t_9, color=WHITE, fill_color=BLACK, fill_opacity=1)
        text9 = VGroup(t_9.bg,t_9)
        t_10=TextMobject('''Notemos que si nos aproximamos al origen en el \n
                                dominio en las direcciones canónicas entonces \n
                                el límite es 0.''').move_to(3*DOWN)
        t_10.bg = SurroundingRectangle(t_10, color=WHITE, fill_color=BLACK, fill_opacity=1)
        text10 = VGroup(t_10.bg,t_10)
        t_11=TextMobject('''Ahora tomemos la dirección dada por la recta \n
                                identidad y veamos qué ocurre.''').move_to(3*UP)
        t_11.bg = SurroundingRectangle(t_11, color=WHITE, fill_color=BLACK, fill_opacity=1)
        text11 = VGroup(t_11.bg,t_11)
        t_12 = TextMobject('''Notamos que en este caso el límite es diferente \n
                                    de 0.''').move_to(3*UP)
        t_12.bg = SurroundingRectangle(t_12, color=WHITE, fill_color=BLACK, fill_opacity=1)
        text12 = VGroup(t_12.bg,t_12)
        #Puede cambiarse t1_t y t1_1f para cambiar el intervalo donde se obtendrá la derivada direccional
        t1_1=ValueTracker(-3)
        punto_convergencia1=Sphere(radius=0.05, fill_opacity=1, fill_color = RED).move_to([-3,-3,1/(9)])
        t1_1f=-0.45
        def mov_sup1 (obj):
            t = t1_1.get_value()
            punto_convergencia1.become(Sphere(radius=0.05, fill_opacity=1, fill_color = RED).move_to([t,t,t**(-2)]))

        punto_convergencia1.add_updater(mov_sup1)

        #Objetos
        axes=ThreeDAxes()
        superficie1_1=superficie2_2_1()
        superficie1_2=superficie2_2_2()
        superficie1_3=superficie2_2_3()
        superficie1_4=superficie2_2_4()
        superficie=VGroup(superficie1_1,superficie1_2,superficie1_3,superficie1_4)

        #Limite en direcciónes canónicas
        #Puede cambiarse las n's para cambiar el intervalo donde se obtendrá la derivada direccional
        n1_1= 15
        cjto1_1 = []
        cjto1_2 = []
        for i in range(1,n1_1):
            y1=3-i*(0.2)
            x1=0
            x=-3+i*(0.2)
            y=0
            cjto1_2.append((x1,y1,2*x1*y1/(x1**2+y1**2)))
            cjto1_1.append((x,y,2*x*y/(x**2+y**2)))

        #Con sucesiones
        Elementos1_1 = [Dot(color=RED).set_color(RED_E).move_to(i) for i in cjto1_1]
        Elementos1_2 = [Dot(color=RED).set_color(RED_E).move_to(i) for i in cjto1_2]
        Elementos1 = VGroup(*Elementos1_1,*Elementos1_2)


        #Con sucesiones
        Elementos1_1 = [Dot(color=RED).set_color(RED_E).move_to(i) for i in cjto1_1]
        Elementos1_2 = [Dot(color=RED).set_color(RED_E).move_to(i) for i in cjto1_2]
        Elementos1 = VGroup(*Elementos1_1,*Elementos1_2)

        #Limite en dirección de la identidad
        n1_2=15
        cjto1_3 = []
        cjto1_4 = []
        for i in range(1,n1_2):
            x2=3-i*(0.2)
            x3=-3+i*(0.2)
            cjto1_3.append((x2,x2,2*x2*x2/(x2**2+x2**2)))
            cjto1_4.append((x3,x3,2*x3*x3/(x3**2+x3**2)))
        Elementos1_3 = [Dot(color=RED).set_color(RED_E).move_to(i) for i in cjto1_3]
        Elementos1_4 = [Dot(color=RED).set_color(RED_E).move_to(i) for i in cjto1_4]
        Elementos2 = VGroup(*Elementos1_3,*Elementos1_4)


        #Animación
        self.add_fixed_in_frame_mobjects(text8)
        self.play(Write(text8))
        self.wait(4.5)
        self.play(FadeOut(text8))
        self.set_camera_orientation(0.7*np.pi/2, (-1.4)*np.pi,distance=12)
        self.play(ShowCreation(axes))
        self.play(ShowCreation(superficie))
        self.add_fixed_in_frame_mobjects(text9)
        self.play(Write(text9))
        self.wait(5)
        self.play(FadeOut(text9))
        self.add_fixed_in_frame_mobjects(text10)
        self.play(Write(text10))
        self.wait(4)
        self.play(ShowCreation(Elementos1),runtime=15)
        self.wait(1.5)
        self.play(FadeOut(text10),FadeOut(Elementos1))
        self.add_fixed_in_frame_mobjects(text11)
        self.play(Write(text11))
        self.wait(4)
        self.play(ShowCreation(Elementos2),runtime=15)
        self.wait()
        self.play(FadeOut(text11),FadeOut(Elementos2))
        self.add_fixed_in_frame_mobjects(text12)
        self.play(Write(text12))
        self.wait(7.5)
        self.play(FadeOut(text12),FadeOut(axes),FadeOut(superficie))

    def parte4 (self):
        text13=TextMobject('''Entonces con esto comprobamos que a veces no \n
                                 es suficiente analizar la función en \n
                                      las direcciones canónicas.''')
        text14=TextMobject('''Sin embargo, como es de esperar, \n
                                si encontramos dos direcciones donde el \n
                                límite difiere, entonces podemos concluir \n
                                    que el límite no existe.''')
        text15=TextMobject('''Es posible que si nos acercamos al punto del\n
                                 dominio en cualquier dirección, el límite sea\n
                                 el mismo, pero puede que la función no tenga límite. ''')
        t_15_1=TextMobject('''Por ejemplo, $f(x,y)=1$ si $y=x^3$ y $f(x,y)=0$ en otro caso''').move_to(3*UP)
        t_15_1.bg = SurroundingRectangle(t_15_1, color=WHITE, fill_color=BLACK, fill_opacity=1)
        text15_1 = VGroup(t_15_1.bg,t_15_1)
        t_15_2=TextMobject(''' $f$ no tiene límite en $\\vec{0}$, aunque sí existen \n
                                todos los límites direccionales en el punto.''').move_to(3*UP)
        t_15_2.bg = SurroundingRectangle(t_15_2, color=WHITE, fill_color=BLACK, fill_opacity=1)
        text15_2 = VGroup(t_15_2.bg,t_15_2)
        text16=TextMobject("¿Cómo argumentamos entonces cuando el límite sí existe?").move_to(2*UP)
        text16_1=TextMobject("Una manera es usando la definición, o sea, la métrica.").move_to(1*UP)
        text17=TextMobject("Pero también podemos usar criterios de comparación.").move_to(0*DOWN)
        text18=TextMobject('''Podemos analizar los órdenes de magnitud de los''').move_to(1*DOWN)
        text18_1=TextMobject('''términos de la función''').move_to(2*DOWN)


        axes=ThreeDAxes()
        superficie=superficie2_3()
        f = ParametricFunction(curva,t_min=-(3**(1/3)),t_max=3**(1/3),color=BLUE_D)
        f1 = ParametricFunction(curva1,t_min=-(3**(1/3)),t_max=3**(1/3),color=BLACK)

        t1_1=ValueTracker(-3)
        t1_1f=-0.2
        punto1=Dot(radius=0.1, fill_opacity=1, fill_color = RED).move_to([0,-3,0])
        punto2=Dot(radius=0.1, fill_opacity=1, fill_color = RED).move_to([-3,0,0])
        punto3=Dot(radius=0.1, fill_opacity=1, fill_color = RED).move_to([0,3,0])
        punto4=Dot(radius=0.1, fill_opacity=1, fill_color = RED).move_to([3,0,0])
        punto5=Dot(radius=0.1, fill_opacity=1, fill_color = RED).move_to([3,-3,0])
        punto6=Dot(radius=0.1, fill_opacity=1, fill_color = RED).move_to([-3,3,0])


        def mov_sup1 (obj):
            t = t1_1.get_value()
            punto1.become(Dot(radius=0.1, fill_opacity=1, fill_color = RED).move_to([0,t,0]))
            punto2.become(Dot(radius=0.1, fill_opacity=1, fill_color = RED).move_to([t,0,0]))
            punto3.become(Dot(radius=0.1, fill_opacity=1, fill_color = RED).move_to([0,-t,0]))
            punto4.become(Dot(radius=0.1, fill_opacity=1, fill_color = RED).move_to([-t,0,0]))
            punto5.become(Dot(radius=0.1, fill_opacity=1, fill_color = RED)).move_to([-t,t,0])
            punto6.become(Dot(radius=0.1, fill_opacity=1, fill_color = RED)).move_to([t,-t,0])


        punto1.add_updater(mov_sup1)
        punto2.add_updater(mov_sup1)
        punto3.add_updater(mov_sup1)
        punto4.add_updater(mov_sup1)
        punto5.add_updater(mov_sup1)
        punto6.add_updater(mov_sup1)
        puntos=VGroup(punto1,punto2,punto3,punto4,punto5,punto6)


        #Animación
        self.add_fixed_in_frame_mobjects(text13)
        self.play(Write(text13))
        self.wait(9)
        self.play(FadeOut(text13))
        self.add_fixed_in_frame_mobjects(text14)
        self.play(Write(text14))
        self.wait(10)
        self.play(FadeOut(text14))
        self.add_fixed_in_frame_mobjects(text15)
        self.play(Write(text15))
        self.wait(12)
        self.play(FadeOut(text15))
        self.set_camera_orientation(0.7*np.pi/2, 0.25*np.pi,distance=12)
        self.play(ShowCreation(axes))
        self.add_fixed_in_frame_mobjects(text15_1)
        self.play(Write(text15_1))
        self.wait(6)
        self.play(ShowCreation(superficie))
        self.play(ShowCreation(f),ShowCreation(f1))
        self.wait(2)
        self.play(FadeOut(text15_1))
        self.add_fixed_in_frame_mobjects(text15_2)
        self.play(Write(text15_2))
        self.wait(5)
        self.play(ShowCreation(puntos))
        self.play(t1_1.set_value, t1_1f,run_time=10)
        self.play(FadeOut(text15_2),FadeOut(axes),FadeOut(superficie),FadeOut(f),
                    FadeOut(f1),FadeOut(puntos))
        self.add_fixed_in_frame_mobjects(text16)
        self.play(Write(text16))
        self.add_fixed_in_frame_mobjects(text16_1)
        self.play(Write(text16_1))
        self.add_fixed_in_frame_mobjects(text17)
        self.play(Write(text17))
        self.add_fixed_in_frame_mobjects(text18)
        self.play(Write(text18))
        self.add_fixed_in_frame_mobjects(text18_1)
        self.play(Write(text18_1))
        self.wait(15)
        self.play(FadeOut(text17),FadeOut(text16),FadeOut(text16_1),FadeOut(text18),FadeOut(text18_1))

    def parte5 (self):
        t_19=TextMobject('''Por ejemplo $f:\\mathbb{R}^{2}-{\\vec{0}}\\rightarrow\\mathbb{R}$\n
                                 $f(x,y)=\\frac{1}{(x+y)^{2}}$''').move_to(3*DOWN)
        t_19.bg = SurroundingRectangle(t_19, color=WHITE, fill_color=BLACK, fill_opacity=1)
        text19 = VGroup(t_19.bg,t_19)
        t_20=TextMobject('''Cuando nos vamos acercando a $\\vec{0}$, \n
                                esta función diverge.''').move_to(3*DOWN)
        t_20.bg = SurroundingRectangle(t_20, color=WHITE, fill_color=BLACK, fill_opacity=1)
        text20 = VGroup(t_20.bg,t_20)
        text21=TextMobject('''Sin embargo no nos pasa \n
                                como en el primer ejemplo, ''','''\n
                                que la función diverge\n
                                 hacia $\\infty$ o $-\\infty$ dependiendo \n
                                 de la dirección\n
                                  que escogemos;''','''\n
                                 en este caso sólo diverge a $\\infty$, \n
                                lo cual se puede demostrar sin mucha \n
                                dificultad porque el numerador es una \n
                                constante y el denominador tiende a \n
                                cero con valores positivos.''')
        text22=TextMobject('''Ahora piensa en la función $f(x,y)=\\frac{|x+y|}{(x+y)^2}$''')
        text23=TextMobject('''Tiende a infinito en el origen,''',''' porque el cuadrado en el \n
                                 denominador afecta a las dos variables,''',''' lo que nos da \n
                                 una valor mucho más pequeño que $|x+y|$ conforme ambas \n
                                  variables tienden a cero.''')#.move_to(2*DOWN)

        axes=ThreeDAxes()
        superficie21=superficie2_4_1()#superficie2_4_1()
        superficie22=superficie2_4_2()

        superficie=VGroup(superficie21,superficie22).rotate(-1.25*np.pi,axis=IN)

        t1_1=ValueTracker(-2)
        t1_1f=-0.3
        punto2=Sphere(radius=0.05, fill_opacity=1, checkerboard_colors=[RED_D, RED_C],fill_color = BLUE_E).move_to([-2,-2,1/(6)**2])

        def mov_sup1 (obj):
            t = t1_1.get_value()
            punto2.become(Sphere(radius=0.05, fill_opacity=1, checkerboard_colors=[RED_D, RED_C],fill_color = BLUE_E).move_to([-t,-t,1/(t+t)**2]).rotate(-1.25*np.pi,axis=IN))

        punto2.add_updater(mov_sup1)

        ##animación
        self.set_camera_orientation(0.7*np.pi/2, 0.65*np.pi,distance=12)
        self.play(ShowCreation(axes))
        self.add_fixed_in_frame_mobjects(text19)
        self.play(Write(text19))
        self.wait(5)
        self.play(ShowCreation(superficie))
        self.wait()
        self.play(FadeOut(text19))
        self.add_fixed_in_frame_mobjects(text20)
        self.play(Write(text20))
        self.wait(7)
        self.play(ShowCreation(punto2))
        self.play(t1_1.set_value, t1_1f,run_time=10)
        self.play(FadeOut(punto2),FadeOut(text20),FadeOut(axes),FadeOut(superficie))
        self.add_fixed_in_frame_mobjects(text21[0])
        self.play(Write(text21[0]))
        self.add_fixed_in_frame_mobjects(text21[1])
        self.play(Write(text21[1]))
        self.add_fixed_in_frame_mobjects(text21[2])
        self.play(Write(text21[2]))
        self.wait(20)
        self.play(FadeOut(text21))
        self.add_fixed_in_frame_mobjects(text22)
        self.play(Write(text22))
        self.wait(10)
        self.play(FadeOut(text22))
        self.add_fixed_in_frame_mobjects(text23[0])
        self.play(Write(text23[0]))
        self.add_fixed_in_frame_mobjects(text23[1])
        self.play(Write(text23[1]))
        self.add_fixed_in_frame_mobjects(text23[2])
        self.play(Write(text23[2]))
        self.wait(17)
        self.play(FadeOut(text23))

    def construct (self):
        ### ANIMACIÓN PARA LAS DIFERENTES PARTES ###
        self.parte0()
        self.parte1()
        self.parte2()
        self.parte3()
        self.parte4()
        self.parte5()

#############################################################
############## Planos y su inclinación #####################
###########################################################
#anexado el 17/03/2021


class Planos(ThreeDScene):

    def l_1(self, t):
        return np.array([t, 0,5*t])
    def l_2(self, t):
        return np.array([0,t,3*t])
    def Plano(self,x,y):
        return np.array([x,y,5*x+ 3*y])


    def construct(self):

        ###Texto
        titulo = TextMobject('''Planos y Su Inclinación''').scale(1.5)
        t_1 = TextMobject('''En $\\mathbb{R}^3$ un plano puede ser descrito como \n
        una superficie lisa, sin subidas ni bajadas. ''')
        t_2 = TextMobject('''Algunos planos son gráficas de funciones de $\\mathbb{R}^2$ en $\\mathbb{R},$''')
        t_3 = TextMobject('''$ f(x,y) = ax + by  \\mbox{ con } a,b \\in \\mathbb{R},$''')
        t_4 = TextMobject('''Cualquier plano no vertical intersecta  \n
        a los planos $xz$ y $yz$ en dos rectas, ''')
        t_5 = TextMobject('''cada una en los planos respectivos \n
        son de pendiente $a$ y $b$.''')
        t_6 = TextMobject('''Veamos a que nos referimos con esto gráficamente.''')
        t_7 = TextMobject('''Tomemos una recta ''', '''$\\mathcal{L}_1$''', ''' en el plano $xz$ de pediente 5 ''').to_edge(UP)
        t_7.set_color_by_tex_to_color_map({'''$\\mathcal{L}_1$''': TEAL})
        t_7_bg = SurroundingRectangle(t_7, color=WHITE, fill_color=BLACK, fill_opacity=1)
        t_8 = TextMobject('''y otra recta ''','''$\\mathcal{L}_2$''', ''' en el plano $yz$ de pendiente 3.''').to_edge(UP)
        t_8.set_color_by_tex_to_color_map({'''$\\mathcal{L}_2$''': RED})
        t_8_bg = SurroundingRectangle(t_8, color=WHITE, fill_color=BLACK, fill_opacity=1)
        t_9 = TextMobject('''Ahora observemos que el plano \n
        $f(x,y) = 5x + 3x$ \n
        contiene a ambas rectas.''').to_edge(UP)
        t_9_bg = SurroundingRectangle(t_9, color=WHITE, fill_color=BLACK, fill_opacity=1)
        t_10 = TextMobject('''Este plano es el único que contiene \n
        ambas rectas y por lo tanto ''').to_edge(UP)
        t_10_bg = SurroundingRectangle(t_10, color=WHITE, fill_color=BLACK, fill_opacity=1)
        t_11 = TextMobject('''este plano queda totalmente \n
        caracterizado por estas.''').to_edge(UP)
        t_11_bg = SurroundingRectangle(t_11, color=WHITE, fill_color=BLACK, fill_opacity=1)
        t_12 = TextMobject(''' En particular la inclinación \n
        del plano queda determinada  \n
        por el vector ''','''$(5,3)$''',''',''').to_edge(UP)
        t_12_bg = SurroundingRectangle(t_12, color=WHITE, fill_color=BLACK, fill_opacity=1)
        t_12.set_color_by_tex_to_color_map({'''$(5,3)$''': GREEN})
        t_13 = TextMobject('''es decir por la \n
        inclinación de las rectas. ''').to_edge(UP)
        t_13_bg = SurroundingRectangle(t_13, color=WHITE, fill_color=BLACK, fill_opacity=1)
        t_14 = TextMobject('''Se puede demostrar que $f:\\mathbb{R}^2\\rightarrow\\mathbb{R}$ es lineal \n
        si y sólo si $f(x,y)=ax+by=(a,b)\\cdot (x,y)$. ''')
        t_15 = TextMobject('''Las gráficas de estas funciones corresponden a todos los \n
        planos no verticales en $\\mathbb{R}^3$ que pasan por el origen.''')
        t_16 = TextMobject('''¿Qué pasa con los planos que no pasan por el origen?''')
        t_17 = TextMobject('''¿Cómo aplica este concepto de inclinación \n
         para el caso de un plano tangente?''')







        ### Objetos

        axes = ThreeDAxes(x_min = -4, x_max = 4, y_min = -4, y_max=4, z_min=-4, z_max=4 ,num_axis_pieces= 4)
        recta_1 = ParametricFunction(self.l_1, color=TEAL, t_min= -2,t_max=2)
        recta_2 = ParametricFunction(self.l_2, color=RED, t_min=-2,t_max=2)
        plano = ParametricSurface(self.Plano, fill_color=PURPLE_E, checkerboard_colors= [PURPLE_D, PURPLE_E], fill_opacity=0.6 ,u_min=-2, u_max =2,v_min=-2, v_max=2)
        inclinacion=Vector(direction=[5,3,0], color=GREEN)




        ###Grupos

        Group_1 = VGroup(recta_1)
        Group_2 = VGroup(recta_2)
        Group_3 = VGroup(plano)



        ### Animaciones
        self.begin_ambient_camera_rotation(rate=0.2)
        self.add_fixed_in_frame_mobjects(titulo)
        self.play(Write(titulo))
        self.wait(1)
        self.play(FadeOut(titulo))
        self.add_fixed_in_frame_mobjects(t_1)
        self.play(Write(t_1))
        self.wait(5)
        self.play(FadeOut(t_1))
        self.add_fixed_in_frame_mobjects(t_2)
        self.play(Write(t_2))
        self.wait(3)
        self.play(FadeOut(t_2))
        self.add_fixed_in_frame_mobjects(t_3)
        self.play(Write(t_3))
        self.wait(1.5)
        self.play(FadeOut(t_3))
        self.add_fixed_in_frame_mobjects(t_4)
        self.play(Write(t_4))
        self.wait(4)
        self.play(FadeOut(t_4))
        self.add_fixed_in_frame_mobjects(t_5)
        self.play(Write(t_5))
        self.wait(3)
        self.play(FadeOut(t_5))
        self.add_fixed_in_frame_mobjects(t_6)
        self.play(Write(t_6))
        self.wait(5)
        self.play(FadeOut(t_6))
        self.set_camera_orientation(phi=45*DEGREES,theta=55*DEGREES)
        self.play(LaggedStart(ShowCreation(axes)))
        self.add_fixed_in_frame_mobjects(t_7_bg, t_7)
        self.play(Write(t_7_bg), Write(t_7))
        self.play(LaggedStart(ShowCreation(Group_1)))
        self.play(FadeOut(t_7), FadeOut(t_7_bg))
        self.wait(5)
        self.add_fixed_in_frame_mobjects(t_8_bg, t_8)
        self.play(Write(t_8_bg), Write(t_8))
        self.play(LaggedStart(ShowCreation(Group_2)))
        self.play(FadeOut(t_8), FadeOut(t_8_bg))
        self.wait(5.5)
        self.add_fixed_in_frame_mobjects(t_9_bg, t_9)
        self.play(Write(t_9_bg), Write(t_9))
        self.play(LaggedStart(ShowCreation(Group_3)))
        self.play(FadeOut(t_9), FadeOut(t_9_bg))
        self.wait(5)
        self.add_fixed_in_frame_mobjects(t_10_bg, t_10)
        self.play(Write(t_10_bg), Write(t_10))
        self.wait(6)
        self.play(FadeOut(t_10), FadeOut(t_10_bg))
        self.add_fixed_in_frame_mobjects(t_11_bg, t_11)
        self.play(Write(t_11_bg), Write(t_11))
        self.wait(5.5)
        self.play(FadeOut(t_11), FadeOut(t_11_bg))
        self.add_fixed_in_frame_mobjects(t_12_bg, t_12)
        self.play(Write(t_12_bg), Write(t_12))
        self.play(FadeIn(inclinacion))
        self.wait(5)
        self.play(FadeOut(t_12), FadeOut(t_12_bg))
        self.add_fixed_in_frame_mobjects(t_13_bg, t_13)
        self.play(Write(t_13_bg), Write(t_13))
        self.wait(5)
        self.play(FadeOut(t_13), FadeOut(t_13_bg))
        self.play(FadeOut(Group_1), FadeOut(Group_2), FadeOut(Group_3), FadeOut(axes), FadeOut(inclinacion))
        self.add_fixed_in_frame_mobjects(t_14)
        self.play(Write(t_14))
        self.wait(5.5)
        self.play(FadeOut(t_14))
        self.add_fixed_in_frame_mobjects(t_15)
        self.play(Write(t_15))
        self.wait(7)
        self.play(FadeOut(t_15))
        self.add_fixed_in_frame_mobjects(t_16)
        self.play(Write(t_16))
        self.wait(5)
        self.play(FadeOut(t_16))
        self.add_fixed_in_frame_mobjects(t_17)
        self.play(Write(t_17))
        self.wait(5)
        self.play(FadeOut(t_17))

###########################################################################
############### Teorema de la función implícita ###########################
###########################################################################
#13/06/2021
class Teorema_de_la_funcion_implicita (ThreeDScene,Scene):
    def setup(self):
        Scene.setup(self)
        ThreeDScene.setup(self)

    def acomodar_textos(self,objeto):
        self.add_fixed_in_frame_mobjects(objeto)
        self.play(Write(objeto))
    def parte1(self):
        titulo=TextMobject('''Teorema de la función \n
                                implícita en funciones de \n 
                                $\\mathbb{R}^2\\to\\mathbb{{R}}$''').scale(2)
        text1=TextMobject('''Sea $f:D \\subset \\mathbb{R}^2\\to \\mathbb{R}$, $D$ abierto y $f \\in C^1_D$.\n
                                Sea $(x_0,y_0)\\in D$ y $f(x_0,y_0)=k$ para alguna $k\\in \\mathbb{R}$ y\n
                                $\\frac{\\partial f}{\\partial y}(x_0,y_0) \\neq 0$ entonces para alguna $\\epsilon>0$ \n
                                $\\exists !$ tal que $g:V_\\epsilon(x_0)\\to \\mathbb{R}$ acotada, $g\\in C^1_{V_\\epsilon(x_0)}$ y \n
                                $f(x,g(x))=k$ para toda $x\\in V_\\epsilon(x_0)$.\n
                                Además $$g'(x)=\\frac{-\\frac{\\partial f}{\\partial x}  (x,g(x))}{\\frac{\\partial f}{\\partial y} (x,g(x))}.$$''')
        text1_1=TextMobject('''Este teorema nos dice que en estas condiciones \n
                                    el conjunto de nivel que corresponde \n
                                    a $k=f(x_0,y_0)$ es localmente una curva \n
                                    suave dada por la gráfica de $g$ y además la \n
                                    derivada de $g$ está en términos de las parciales de $f$. ''')
        text2=TextMobject('''Considera la función $f(x,y)=x^2-y$ y su curva de nivel 0. ''').move_to(3*UP)
        text2.bg=SurroundingRectangle(text2,color=WHITE,fill_color=BLACK,fill_opacity=1)
        text3=TextMobject('''Nota que \n
                             $\\frac{\\partial f}{\\partial y}(x,y)=-1 $ ''').move_to(-3*UP)
        text3.bg=SurroundingRectangle(text3,color=WHITE,fill_color=BLACK,fill_opacity=1)
        text4=TextMobject('''Puedes comprobar que en cualquier punto se cumplen\n
                                 las condiciones del teorema de la  \n
                                 función implícita.''').move_to(-2*UP)
        text4.bg=SurroundingRectangle(text4,color=WHITE,fill_color=BLACK,fill_opacity=1)
        text5=TextMobject('''Observa que la curva de nivel, en términos de \n
                                la variable $x$, queda descrita como $y(x)=g(x)=x^2$.''').move_to(3*UP)
        text5.bg=SurroundingRectangle(text5,color=WHITE,fill_color=BLACK,fill_opacity=1)
        text6=TextMobject(''' Sin embargo, no siempre se puede encontrar \n
                                explícitamente a la función $g$, porque no \n
                                siempre se puede despejar la $y$ en términos \n
                                de la $x$ en la ecuación $f(x,y)=k$. ''')
        
        
        axes = ThreeDAxes(y_max=3)
    
        superficie1 = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                u**2-v
            ]),v_min=-3,v_max=3,u_min=-3,u_max=3,fill_opacity=0.75,checkerboard_colors=[GOLD_E,GOLD_E])
            
        curva1=ParametricFunction(
                lambda u : np.array([
                u,
                u**2,
                0
            ]),color=WHITE,t_min=-1.5,t_max=1.5,
            )

        self.play(Write(titulo))
        self.wait(9)
        self.play(FadeOut(titulo))
        self.play(Write(text1))
        self.wait(64)
        self.play(FadeOut(text1))
        self.acomodar_textos(text1_1)
        self.wait(21)
        self.play(FadeOut(text1_1))
        self.acomodar_textos(text2.bg)
        self.acomodar_textos(text2)
        self.set_camera_orientation(phi=75 * DEGREES,theta=-45*DEGREES,distance=100)
        self.play(ShowCreation(axes))
        self.play(ShowCreation(superficie1))
        self.wait()
        self.play(ShowCreation(curva1))
        self.wait(11)
        self.play(FadeOut(text2),FadeOut(text2.bg))
        self.acomodar_textos(text3.bg)
        self.acomodar_textos(text3)
        self.wait(11)
        self.play(FadeOut(text3),FadeOut(text3.bg))
        self.acomodar_textos(text4.bg)
        self.acomodar_textos(text4)
        self.wait(11)
        self.play(FadeOut(text4),FadeOut(text4.bg))
        self.play(FadeOut(superficie1))
        self.move_camera(phi= 0 * DEGREES,theta=-90*DEGREES,run_time=2)
        self.acomodar_textos(text5.bg)
        self.acomodar_textos(text5)
        self.wait(13)
        self.play(FadeOut(text5),FadeOut(curva1),FadeOut(axes),FadeOut(text5.bg))
        self.acomodar_textos(text6)
        self.wait(16)
        self.play(FadeOut(text6))
    
    def parte2(self):
        text8_1=TextMobject('''Por ejemplo; sea $D=\\{(x,y)\\in\\mathbb{R}^2|x> 0, \\ y> 0\\}$ y \n
                                 $f:D \\to\\mathbb{R}$, $f(x,y)=x^y+y^{xy}$ ''').move_to(3*DOWN)
        text8_1.bg=SurroundingRectangle(text8_1,color=WHITE,fill_color=BLACK,fill_opacity=1)
        text8_2=TextMobject('''Puedes comprobar que dicha función es de clase $C^1_D$. ''').move_to(3*DOWN)
        text8_2.bg=SurroundingRectangle(text8_2,color=WHITE,fill_color=BLACK,fill_opacity=1)
        text8_3=TextMobject('''Así mismo considera la curva de nivel 2 y el punto (1,1) \n
                                 que pertenece a ella. ''').move_to(3*DOWN)
        text8_3.bg=SurroundingRectangle(text8_3,color=WHITE,fill_color=BLACK,fill_opacity=1)                        
        text8_4=TextMobject('''La parcial con respecto a $y$ de dicha función es
                                $$\\frac{\\partial x^y+y^{xy}}{\\partial y}=x^ylog(x)+xy^{xy}(log(y)+1)$$ ''').move_to(2*DOWN)
        text8_4.bg=SurroundingRectangle(text8_4,color=WHITE,fill_color=BLACK,fill_opacity=1)
        text8_5=TextMobject(''' La cual al evaluarse en el punto (1,1) es diferente de 0.''').move_to(3*DOWN)
        text8_5.bg=SurroundingRectangle(text8_5,color=WHITE,fill_color=BLACK,fill_opacity=1)
        text8_6=TextMobject('''Debido a lo anterior se cumplen las condiciones del \n
                                teorema de la función implícita para el punto (1,1).''').move_to(3*DOWN)
        text8_6.bg=SurroundingRectangle(text8_6,color=WHITE,fill_color=BLACK,fill_opacity=1)
        text8_7=TextMobject('''Entonces se puede describir la curva de nivel 2, \n
                                    alrededor del punto (1,1), como una función g(x)=y. ''').move_to(3*DOWN)
        text8_7.bg=SurroundingRectangle(text8_7,color=WHITE,fill_color=BLACK,fill_opacity=1)
        nota=TextMobject('''NOTA: La curva de nivel mostrada es un  \n
                                    boceto, puedes utilizar  \n
                                    calculadoras gráficas para observar \n
                                    la curva detalladamente. ''').scale(0.7).move_to(2.5*UP+3.35*LEFT)
        text8_8=TextMobject(''' Sin embargo no es posible despejar la variable $y$ \n
                                    de la ecuación $x^y+y^{xy}=2$''').move_to(3*DOWN)
        text8_8.bg=SurroundingRectangle(text8_8,color=WHITE,fill_color=BLACK,fill_opacity=1)
        text8_9=TextMobject('''Con el ejemplo anterior apreciamos que existen funciones \n
                                 en las cuales no es posible despejar la variable $y$ de \n
                                 la ecuación $f(x,y)=k$, pero con el teorema de \n
                                 la función implícita podemos asegurar que dicha curva \n
                                  se puede describir como la gráfica de una función $g(x)=y$.''')
        axes=ThreeDAxes(y_max=3.5)
        superficie8=ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                (u**v)+(v**(u*v))
            ]),v_min=0.1,v_max=2.55,u_min=0.1,u_max=2.55,fill_opacity=0.75,checkerboard_colors=[GOLD_E,GOLD_E])
        punto_1=Dot(radius=0.1,color=RED).move_to([1,1,2])
        punto_2=Dot(radius=0.1,color=RED).move_to([1,1,2])
        

        curva_nivel= SVGMobject("desmos-graph2.svg",color=BLACK,stroke_color=BLUE).scale(2.3).move_to([2.3,2.5,2])
        curva_nivel_label=TexMobject(r"g(x)=y",color=BLUE).move_to([2,1.5,0])
        rectangulo = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                2
            ]),v_min=0,v_max=3,u_min=0,u_max=3,fill_color=RED,fill_opacity=0.7, checkerboard_colors=[RED,RED])
        
        self.set_camera_orientation(phi=75 * DEGREES,theta=-85*DEGREES,distance=100)
        self.play(ShowCreation(axes))
        self.acomodar_textos(text8_1.bg)
        self.acomodar_textos(text8_1)
        self.wait(26)
        self.play(ShowCreation(superficie8))
        self.wait()
        self.play(FadeOut(text8_1),FadeOut(text8_1.bg))
        self.acomodar_textos(text8_2.bg)
        self.acomodar_textos(text8_2)
        self.wait(12)
        self.play(FadeOut(text8_2),FadeOut(text8_2.bg))
        self.acomodar_textos(text8_3.bg)
        self.acomodar_textos(text8_3)
        self.play(ShowCreation(punto_1))
        self.wait()
        self.play(ShowCreation(rectangulo))
        self.wait(8)
        self.play(FadeOut(text8_3),FadeOut(text8_3.bg))
        self.acomodar_textos(text8_4.bg)
        self.acomodar_textos(text8_4)
        self.wait(22)
        self.play(FadeOut(text8_4),FadeOut(text8_4.bg))
        self.acomodar_textos(text8_5.bg)
        self.acomodar_textos(text8_5)
        self.wait(9)
        self.play(FadeOut(text8_5),FadeOut(text8_5.bg))
        self.acomodar_textos(text8_6.bg)
        self.acomodar_textos(text8_6)
        self.wait(10)
        self.play(FadeOut(text8_6),FadeOut(text8_6.bg))
        self.acomodar_textos(text8_7.bg)
        self.acomodar_textos(text8_7)
        self.play(FadeOut(superficie8),FadeOut(rectangulo),FadeOut(punto_1),ShowCreation(punto_2))
        self.move_camera(phi= 0 * DEGREES,theta=-90*DEGREES,distance=100,run_time=2)
        self.play(ShowCreation(curva_nivel),FadeOut(punto_2))
        self.play(ShowCreation(punto_2))
        self.acomodar_textos(nota)
        self.acomodar_textos(curva_nivel_label)
        self.wait(13)
        self.play(FadeOut(text8_7),FadeOut(text8_7.bg))
        self.acomodar_textos(text8_8.bg)
        self.acomodar_textos(text8_8)
        self.wait(15)
        self.play(FadeOut(axes),FadeOut(text8_8),FadeOut(text8_8.bg),FadeOut(curva_nivel),FadeOut(punto_2),FadeOut(curva_nivel_label),FadeOut(nota))
        self.acomodar_textos(text8_9)
        self.wait(28)
        self.play(FadeOut(text8_9))

    
    def parte3(self):
        
        text9=TextMobject('''Veamos otro ejemplo.''')
        text10=TextMobject(''' Considera $f(x,y)=y^3-x^9$ y su curva de nivel 0.''').move_to(3*UP)
        text10.bg=SurroundingRectangle(text10,color=WHITE,fill_color=BLACK,fill_opacity=1)
        text11=TextMobject(''' Si bien $\\frac{\\partial f}{\\partial y}(x,y)=3y^2$ y \n
                                 $\\frac{\\partial f}{\\partial y}(0,0)=0$, puedes observar \n 
                                 que la expresión $g(x)=y(x)=x^3$ describe a la curva de nivel.''').move_to(-2.5*UP)
        text11.bg=SurroundingRectangle(text11,color=WHITE,fill_color=BLACK,fill_opacity=1)
        text12=TextMobject('''Lo que nos dice que no se vale el regreso del Teorema.''')
        axes=ThreeDAxes(y_max=3)

        superficie3 = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                v**3-u**9
            ]),v_min=-2,v_max=2,u_min=-1.6,u_max=1.6,fill_opacity=0.75,checkerboard_colors=[GOLD_E,GOLD_E])
            
        curva3=ParametricFunction(
                lambda u : np.array([
                u,
                u**3,
                0
            ]),color=WHITE,t_min=-1.26,t_max=1.26,
            )
        
        self.play(Write(text9))
        self.wait(5)
        self.play(FadeOut(text9))
        self.set_camera_orientation(phi=75 * DEGREES,theta=15*DEGREES,distance=100)
        self.play(ShowCreation(axes))
        self.acomodar_textos(text10.bg)
        self.acomodar_textos(text10)
        self.wait()
        self.play(ShowCreation(superficie3))
        self.wait()
        self.play(ShowCreation(curva3))
        self.wait(10)
        self.play(FadeOut(text10),FadeOut(text10.bg))
        self.acomodar_textos(text11.bg)
        self.acomodar_textos(text11)
        self.play(FadeOut(superficie3))
        self.move_camera(phi= 0 * DEGREES,theta=-90*DEGREES,run_time=2)
        self.wait(24)
        self.play(FadeOut(text11),FadeOut(text11.bg),FadeOut(curva3),FadeOut(axes))
        self.acomodar_textos(text12)
        self.wait(6)
        self.play(FadeOut(text12))

    def parte4(self):
        text13=TextMobject('''Ahora considera la función $\gamma(x,y)=xy$. ''').move_to(3*UP)
        text13.bg=SurroundingRectangle(text13,color=WHITE,fill_color=BLACK,fill_opacity=1)
        text14=TextMobject('''Notarás que la curva de nivel 0 de la función corresponde \n
                                        a los ejes $x$ y $y$.''').move_to(3*DOWN)
        text14.bg=SurroundingRectangle(text14,color=WHITE,fill_color=BLACK,fill_opacity=1)
        text15=TextMobject('''Además debido a que \n
                                $\\frac{\\partial \\gamma}{\\partial y}=x. $''').move_to(3*UP)
        text15.bg=SurroundingRectangle(text15,color=WHITE,fill_color=BLACK,fill_opacity=1)
        text16=TextMobject('''En los puntos de la curva de nivel en el eje $y$ la parcial \n
                                se anula y no es posible aplicar el teorema de \n
                                 la función implícita.''').move_to(2.5*UP)
        text16.bg=SurroundingRectangle(text16,color=WHITE,fill_color=BLACK,fill_opacity=1)
        text17=TextMobject('''¿Qué ocurre si $\\frac{\\partial f}{\\partial x}(x,y)\\neq 0$?''',''' \n
                                Enuncia el Teorema de la función implícita correspondiente.''')
        text18=TextMobject('''Observa que en el caso del ejemplo $\\gamma(x,y)=xy$, \n
                                en el origen tenemos un punto crítico y por tanto no \n
                                existe ninguna de las funciones implícitas para describir \n
                                a la curva de nivel de manera local.''').move_to(2.7*DOWN)
        text18.bg=SurroundingRectangle(text18,color=WHITE,fill_color=BLACK,fill_opacity=1)
        

        axes=ThreeDAxes()
        
        superficie4 = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                u*v
            ]),v_min=-3,v_max=3,u_min=-3,u_max=3,fill_opacity=0.75,checkerboard_colors=[GOLD_E,GOLD_E])
        curva4_1=ParametricFunction(
                lambda u : np.array([
                u,
                0,
                0
            ]),color=RED,t_min=-3,t_max=3,
            )
        curva4_2=ParametricFunction(
                lambda u : np.array([
                0,
                u,
                0
            ]),color=RED,t_min=-3,t_max=3,
            )    
        curva4=VGroup(curva4_1,curva4_2)
        
        punto_critico=Dot(radius=0.1,color=RED).move_to([0,0,0])

        self.set_camera_orientation(phi=75 * DEGREES,theta=-45*DEGREES,distance=100)
        self.play(ShowCreation(axes))
        self.acomodar_textos(text13.bg)
        self.acomodar_textos(text13)
        self.wait(10)
        self.play(ShowCreation(superficie4))
        self.begin_ambient_camera_rotation(rate=0.03)
        self.play(FadeOut(text13),FadeOut(text13.bg))
        self.acomodar_textos(text14.bg)
        self.acomodar_textos(text14)
        self.wait(3)
        self.play(ShowCreation(curva4))
        self.wait(4)
        self.play(FadeOut(text14),FadeOut(text14.bg))
        self.acomodar_textos(text15.bg)
        self.acomodar_textos(text15)
        self.wait(8)
        self.play(FadeOut(text15),FadeOut(text15.bg))
        self.acomodar_textos(text16.bg)
        self.acomodar_textos(text16)
        self.wait(12)
        self.play(FadeOut(text16),FadeOut(text16.bg),FadeOut(axes),FadeOut(curva4),FadeOut(superficie4))
        self.stop_ambient_camera_rotation()
        self.set_camera_orientation(phi=75 * DEGREES,theta=-45*DEGREES,distance=100)
        self.acomodar_textos(text17[0])
        self.wait()
        self.acomodar_textos(text17[1])
        self.wait(15)
        self.play(FadeOut(text17))
        self.play(ShowCreation(axes),ShowCreation(superficie4))
        self.acomodar_textos(text18.bg)
        self.acomodar_textos(text18)
        self.play(ShowCreation(punto_critico))
        self.wait(17)
        self.play(FadeOut(text18),FadeOut(text18.bg),FadeOut(axes),FadeOut(superficie4),FadeOut(punto_critico))
    def parte5 (self):
        text18=TextMobject('''Geométricamente el teorema de la función implícita \n
                             dice que si $\\nabla f(x_0,y_0)$ no es horizontal, \n
                             $\\frac{\\partial f}{\\partial y}(x_0,y_0)\\neq 0$, ''',''' \n
                             es decir no es paralelo al eje $x$ entonces podemos \n
                             describir un sector de la curva de nivel $k$,\n
                              alrededor de $(x_0,y_0)$  como la gráfica de una \n
                              función de la forma $y=g(x)$.''')  
        text18[0].move_to(3.1*UP)
        text18[1].move_to(2.5*DOWN)
        text19=TextMobject('''Y si el vector $\\nabla f(x_0,y_0)$ no es vertical 
                                $\\frac{\\partial g}{\\partial x}(x_0,y_0)\\neq 0$, \n
                                es decir no es paralelo al eje $y$, entonces un sector de la\n
                                curva de nivel $k$ de $f$ alrededor del punto $(x_0,y_0)$ se\n
                                puede ver como la gráfica de una función de la forma $x=h(y).$''').move_to(-2.8*DOWN).scale(0.8)
        text19.bg=SurroundingRectangle(text19,color=WHITE,fill_color=BLACK,fill_opacity=1)
        text20=TextMobject('''Un corolario del Teorema de la función implícita es \n
                                que el gradiente es ortogonal a la curva de nivel.''').move_to(3*DOWN)
        text20.bg=SurroundingRectangle(text20,color=WHITE,fill_color=BLACK,fill_opacity=1)
        text21=TextMobject('''Con los ejemplos anteriores sólo se consideró el teorema de \n
                                 la función implícita en funciones de $\\mathbb{R}^2\\to\\mathbb{R}$, \n
                                 sin embargo el teorema es generalizable a \n
                                 funciones de $\\mathbb{R}^m\\times\\mathbb{R}^n\\to\\mathbb{R}$.''')
        
        
        axes=ThreeDAxes(x_max=4.8,y_max=3,x_min=-4.8,y_min=-4.8,)


        #Curva ilustrativa
        curva=ParametricFunction(
                lambda u : np.array([
                u,
                1.5*np.cos(u/2)**(1/3),
                0
            ]),color=WHITE,t_min=-4.5,t_max=4.5,
            )    
         
        curva_ejem1=DashedVMobject(curva,y_tick_frequency=0.02, x_tick_frequency=0.02)

        #Primer gradiente
        #Se pueden modificar los parámetros a y b
        a=1
        b=1.5*np.cos(a/2)**(1/3)
        x0=np.array([a,b,0])
        x0_dot=Dot(color=RED).move_to(x0)
        grad1_vec=Arrow([a,b,0],[(-0.25*np.sin(a/2))/(np.cos(a/2)**(2/3))     ,-1,0],buff=0,color=BLUE_C)
        grad1_label=TexMobject(r"\nabla f(\vec{x}_0)").next_to(grad1_vec,LEFT,buff=0.5)
        grad1=VGroup(grad1_vec,grad1_label)
        #Tamaño de la vecindad
        #Se puede modificar el parámetro v para tener una vecidad diferente
        v=1.5
        curva_1=ParametricFunction(
                lambda u : np.array([
                u,
                1.5*np.cos(u/2)**(1/3),
                0
            ]),color=PINK,t_min=a-v,t_max=a+v,
            )   
        curva1_label=TexMobject(r"g(x)").next_to(curva_1,UP,buff=0.3).set_color(PINK)
        curva1=VGroup(curva_1,curva1_label)

        
        ######## Para la segunda sección
        #Primer gradiente
        #Se pueden modificar los parámetroa a2 y b2
        a2=2.5
        b2=1.5*np.cos(a2/2)**(1/3)
        x02=np.array([a2,b2,0])
        x02_dot=Dot(color=RED).move_to(x02)
        grad2_vec=Arrow([a2,b2,0],[(-0.25*np.sin(a2/2))/(np.cos(a2/2)**(2/3))     ,-1,0],buff=0,color=BLUE_C)
        grad2_label=TexMobject(r"\nabla f(\vec{p}_0)").next_to(grad2_vec,DOWN+LEFT,buff=0.3)
        grad2=VGroup(grad2_vec,grad2_label)
        #seccion de curva de subrirá
        #Tamaño de la vecindad
        #También se puede moficar  v2
        v2=1.5
        curva_2=ParametricFunction(
                lambda u : np.array([
                u,
                1.5*np.cos(u/2)**(1/3),
                0
            ]),color=PINK,t_min=a2-v2,t_max=a2+v2,
            )   
        curva2_label=TexMobject(r"h(y)").next_to(curva_2,RIGHT,buff=0.3).set_color(PINK)
        curva2=VGroup(curva_2,curva2_label)

        #Visualicación del corolario
        curva_3=ParametricFunction(
                lambda u : np.array([
                u,
                np.cos(u**2),
                0
            ]),color=WHITE,t_min=-4,t_max=4,
            )   
        #Se pueden modificar los parámetros x1 y x2, para cambiar donde se evalua inicialmente el gradiente, ambos valores deben ser iguales
        x1=ValueTracker(-1.5)
        x2=-1.5
        y1=np.cos(x2**2)
        punto=Dot(color=RED).move_to([x2,y1,0])
        gradiente1=Arrow([x2,y1,0],[2*x2*np.sin(x2**2)+x2,1+y1,0],buff=0,color=PINK)
        def GRADIENTE(obj):
            x=x1.get_value()
            y=np.cos(x**2)
            punto.become(Dot(color=RED).move_to([x,y,0]))
            gradiente1.become(Arrow([x,y,0],[2*x*np.sin(x**2)+x,1+y,0],buff=0,color=RED))
        punto.add_updater(GRADIENTE)
        gradiente1.add_updater(GRADIENTE)

        self.set_camera_orientation(phi=0 * DEGREES,theta=-90*DEGREES,distance=200)
        self.play(ShowCreation(axes))
        self.play(ShowCreation(curva_ejem1))
        self.acomodar_textos(text18)
        self.wait()
        self.play(ShowCreation(x0_dot))
        self.play(ShowCreation(grad1))
        self.wait()
        self.play(ShowCreation(curva1))
        self.wait(28)
        self.play(FadeOut(curva1),FadeOut(grad1),FadeOut(x0_dot),FadeOut(text18))
        self.acomodar_textos(text19.bg)
        self.acomodar_textos(text19)
        self.wait()
        self.play(ShowCreation(x02_dot))
        self.play(ShowCreation(grad2))
        self.wait()
        self.play(ShowCreation(curva2))
        self.wait(25)
        self.play(FadeOut(curva2),FadeOut(grad2),FadeOut(x02_dot),FadeOut(text19),FadeOut(text19.bg),FadeOut(curva_ejem1))
        self.acomodar_textos(text20.bg)
        self.acomodar_textos(text20)
        self.wait(11)
        self.play(ShowCreation(curva_3))
        self.play(ShowCreation(punto),ShowCreation(gradiente1))
        self.wait()
        #Se puede cambiar el valor 1.5 por otro. Este permite tener el último valor donde se evalua el gradiente
        self.play(x1.set_value,1.5,run_time=15)
        self.play(FadeOut(text20),FadeOut(text20.bg),FadeOut(curva_3),FadeOut(punto),FadeOut(gradiente1),FadeOut(axes),FadeOut(punto))
        self.acomodar_textos(text21)
        self.wait(18)
        self.play(FadeOut(text21))
    def parte6(self):
        text22=TextMobject('''Veamos un ejemplo de ello.''')
        text23=TextMobject('''Considera la función $\\beta(x,y,z)=x^2+y+z$.''').move_to(-1*DOWN)
        text24=TextMobject('''Como seguramente sabrás, es complicado graficar \n
                                en 4 dimensiones, así que limitémonos a graficar \n
                                    la superficie de nivel 0.''').next_to(text23,DOWN,buff=0.1)
        text25=TextMobject('''Podemos describir la superficie de nivel con \n
                                la función $z=-x^2-y$.''').move_to(3*DOWN)
        text25.bg=SurroundingRectangle(text25,color=WHITE,fill_color=BLACK,fill_opacity=1)
        text26=TextMobject('''Incluso podemos dejar la superficie de \n
                                    nivel en términos de $y$.''').move_to(-3.3*DOWN)
        text26.bg=SurroundingRectangle(text26,color=WHITE,fill_color=BLACK,fill_opacity=1)
        text27=TextMobject('''Con esto, notamos que el teorema de la función \n
                                    implícita nos permite afirmar cuándo podemos describir el \n
                                conjunto de nivel $k$ de una función en términos de algunas \n
                                variables de la función en puntos no críticos.''')
        
        axes=ThreeDAxes()
        superficie1 = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                -u**2-v
            ]),v_min=-3,v_max=3,u_min=-3,u_max=3,fill_opacity=0.75,checkerboard_colors=[GOLD_E,GOLD_E])
        self.acomodar_textos(text22)
        self.wait(6)
        self.play(FadeOut(text22))
        self.set_camera_orientation(phi=75 * DEGREES,theta=-45*DEGREES,distance=100)
        self.acomodar_textos(text23)
        self.acomodar_textos(text24)
        self.wait(20)
        self.play(FadeOut(text24))
        self.play(text23.shift,2.7*UP,run_time=3)
        self.play(ShowCreation(axes))
        self.play(ShowCreation(superficie1))
        self.begin_ambient_camera_rotation(rate=0.3)
        self.acomodar_textos(text25.bg)
        self.acomodar_textos(text25)
        self.wait(13)
        self.play(FadeOut(text25),FadeOut(text25.bg),FadeOut(text23))
        self.acomodar_textos(text26.bg)
        self.acomodar_textos(text26)
        self.wait(9)
        self.play(FadeOut(axes),FadeOut(superficie1),FadeOut(text26),FadeOut(text26.bg))
        self.acomodar_textos(text27)
        self.wait(16)
        self.play(FadeOut(text27))

    def construct(self):
        self.parte1()
        self.parte2()
        self.parte3()
        self.parte4()
        self.parte5()
        self.parte6()

#############################
###### ¿GRÁFICAS EN R4? #######
#############################
class grafica_r4(ThreeDScene):

    def get_numer_labels_to_numberline(self,number_line,x_max=None,x_min=0,buff=0.2,step_label=1,**tex_kwargs):
        labels = VGroup()
        x_max = number_line.x_max
        for x in range(x_min,x_max+1,step_label):
            x_label = TexMobject(f"{x}",**tex_kwargs)
            # See manimlib/mobject/number_line.py CONFIG dictionary
            x_label.next_to(number_line.number_to_point(x),DOWN,buff=buff)
            labels.add(x_label)
        return labels

    def get_number_line_group(self,label,x_max,unit_size,v_tracker,step_label=1,**number_line_config):
        number_label = TexMobject(label)
        arrow = Arrow(UP,DOWN,buff=0).set_height(0.5)
        number_line = NumberLine(
            x_min=0,
            x_max=x_max,
            unit_size=unit_size,
            numbers_with_elongated_ticks=[],
            **number_line_config
            )
        labels = self.get_numer_labels_to_numberline(number_line,step_label=step_label,height=0.2)
        arrow.next_to(number_line.number_to_point(0),UP,buff=0)
        label = VGroup(arrow,number_label)
        number_label.next_to(arrow,UP,buff=0.1)
        numer_group = VGroup(label,number_line,labels)
        label.add_updater(lambda mob: mob.next_to(number_line.number_to_point(v_tracker.get_value()),UP,buff=0))

        return numer_group

    def construct(self):

        axis_config = {
            "x_min" : -4,
            "x_max" : 4,
            "y_min" : -4,
            "y_max" : 4,
            "z_min" : -4,
            "z_max" : 4,
            "x_labeled_nums": [i for i in range(-4,-5)],
            "y_labeled_nums": [i for i in range(-4,-5)]
        }

        axis_config2 = {
            "x_min" : -4,
            "x_max" : 4,
            "y_min" : -4,
            "y_max" : 4,
            "z_min" : -4,
            "z_max" : 4
        }

        reglaf = TextMobject("$f(x,y,z) = \\lVert (x,y,z) \\rVert$").to_corner(UL)
        reglaf.bg = SurroundingRectangle(reglaf,color=WHITE,fill_color=BLACK,fill_opacity=1)
        reglaf.group = VGroup(reglaf.bg,reglaf)

        ejes = ThreeDAxes(**axis_config)
        ejes.add(ejes.get_axis_labels())
        ejes.axis_labels[0].rotate(PI/2,axis=RIGHT)
        ejes.axis_labels[1].rotate(PI/2,axis=RIGHT)

        ejes2 = ThreeDAxes(**axis_config2).shift(3*LEFT).scale(0.5)

        esf2 = Sphere(resolution=(30,30), radius=3, opacity=100).set_color(GREEN_E).move_to(ejes2.get_center()).scale(0.5)

        fle = Arrow(start=(-1,0,0),end=(1,0,0),color=WHITE).shift(0.3*RIGHT)
        ffl = TexMobject(r"f").next_to(fle,DOWN)
        flecha = VGroup(ffl,fle)

        rad = ValueTracker(0)
        esf = Sphere(resolution=(30,30), radius=rad.get_value()).set_color_by_gradient(BLUE, BLUE_D, PURPLE, PURPLE_D)
        def upd_for_sphere(obj):
            c = obj
            radius = rad.get_value()
            new_c = Sphere(resolution=(50,50),radius = radius).set_color_by_gradient("#ca31e8", "#b55eff", "#3986ff")
            c.become(new_c)

        text_1 = TextMobject("Cuando $f(x,y,z)=t=$")
        fx_tex = DecimalNumber(rad.get_value()).next_to(text_1,RIGHT)
        def upd_for_decimal(obj):
            obj.set_value(rad.get_value())
            self.add_fixed_in_frame_mobjects(obj)
        Group1 = VGroup(fx_tex,text_1).to_corner(DR)
        Group1.bg = SurroundingRectangle(Group1,color=WHITE,fill_color=BLACK,fill_opacity=1)
        Group2 = VGroup(Group1.bg,text_1)

        fx_number_line_group = self.get_number_line_group(
            "t",3,1,step_label=1,v_tracker=fx_tex,
            tick_frequency=1
            )
        fx_number_line_group.to_corner(DL)

        num_lin = NumberLine(x_min=0,x_max=3,tick_frequency=1)
        n_l_lab = self.get_numer_labels_to_numberline(num_lin,step_label=1,height=0.2)
        n_l = VGroup(num_lin,n_l_lab).shift(2.2*RIGHT)
        linea = Line(start=(-1.5,0,0),end=(1.5,0,0),color=MAROON,width=9, stroke_width=9).move_to(n_l.get_center()).shift(0.10*UP)

        title = TextMobject('''¿Gráficas en $\\mathbb{R}^4$?''').scale(1.5)
        t_1 = TextMobject('''Puede que hayas escuchado que sólo\\\\
                             se pueden graficar funciones tales que sus gráficas\\\\
                             son subconjuntos de $\\mathbb{R}^2$ o $\\mathbb{R}^3$, \\\\
                             veamos...''')
        t_2 = TextMobject('''Considera ''','''$f(x,y,z)$''','''$ = \\lVert (x,y,z) \\rVert$,\\\\''','''
                             entonces la gráfica de $f$ es \\\\''','''
                             $Gr(f)$''','''$=\\{(x,y,z,f(x,y,z))\\in\\mathbb{R}^4|(x,y,z)\\in D\\}$, \\\\
                             donde ''','''$D$''',''' es el ''','''dominio''',''' de ''','''$f$''','''.''')
        t_2[1].set_color(RED)
        t_2[4].set_color_by_gradient(BLUE, BLUE_D, PURPLE, PURPLE_D)
        t_2[-6].set_color(GREEN_D)
        t_2[-4].set_color(GREEN_D)
        t_2_1 = VGroup(t_2[0],t_2[1],t_2[2])
        t_2_2 = VGroup(t_2[3],t_2[4],t_2[5],t_2[6],t_2[7],t_2[8],t_2[9],t_2[10],t_2[11])
        t_3_1 = TextMobject('''Si tomamos ''','''$D$''',''' como la esfera compacta rellena \\\\
                             de radio 3 con centro en el origen,''').to_edge(UP)
        t_3_2 = TextMobject('''tenemos que ''','''$f$''','''$:$''','''$D$''','''$\\subset \\mathbb{R}^3\\rightarrow \\mathbb{R}$, \\\\''','''
                             entonces ''','''$Im(f)$''','''$=[0,3]$.''').to_edge(DOWN)
        t_3_1[1].set_color(GREEN_D)
        t_3_2[3].set_color(GREEN_D)
        t_3_2[-2].set_color(MAROON)
        t_3 = VGroup(t_3_1,t_3_2)
        t_4 = TextMobject('''Para la gráfica tomamos cuatro ejes: $x,y,z,t$\\\\''','''
                             donde los ejes $x,y,z$ los usamos de manera estándar\\\\
                             para representar a los puntos del ''','''dominio''',''' de $f$\\\\''','''
                             y el ''','''eje $t$''',''' lo usaremos para las ''','''imágenes''',''' de $f$ \\\\
                             de la siguiente manera:''')
        t_4[2].set_color(GREEN_D)
        t_4[5].set_color(TEAL)
        t_4[-2].set_color(MAROON)
        t_4_1 = VGroup(t_4[1],t_4[2],t_4[3])
        t_4_2 = VGroup(t_4[4],t_4[5],t_4[6],t_4[7],t_4[8])
        t_5 = TextMobject('''Generamos un video, en el cual,\\\\
                             en el ''','''eje del tiempo $t$''',''' representamos los valores de ''','''$f$''','''.''')
        t_5[1].set_color(TEAL)
        t_5[-2].set_color(RED)
        t_6 = TextMobject('''De esta manera \\\\
                             $C_t=\\{(x,y,z)\\in D|f(x,y,z)=t\\in [0,3]\\}$, \\\\
                             es un conjunto de nivel de $f$,\\\\
                             que en este caso es una ''','''superficie de nivel.''')
        t_6[1].set_color(ORANGE)
        t_7 = TextMobject('''Para cada valor de $t$,\\\\
                             podemos representar en el video esta \\\\
                             ''','''superficie de nivel''',''' muy conocida:''')
        t_7[1].set_color(ORANGE)
        t_8 = TextMobject('''Es una esfera hueca, compacta, \\\\
                             con centro en el origen y radio $\\sqrt{t}$.''')
        t_9 = TextMobject('''Finalmente juntamos estas ''','''superficies de nivel''',''' \\\\ 
                             en nuestro video y obtenemos la gráfica.\\\\
                             ¡La ''','''gráfica de $f$''',''' es un sólido en $\\mathbb{R}^4$!''')
        t_9[1].set_color(ORANGE)
        t_9[3].set_color_by_gradient(BLUE, PURPLE)

        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))
        self.play(Write(t_1))
        self.wait(9)
        self.play(ReplacementTransform(t_1,t_2))
        self.wait(6)
        self.wait(10)
        self.play(ReplacementTransform(t_2,t_3_1))
        self.play(Write(t_3_2))
        self.play(ShowCreation(ejes2))
        self.play(Write(n_l))
        self.add_foreground_mobjects(esf2)
        self.play(ShowCreation(esf2))
        self.wait(4)
        
        self.play(Write(flecha))
        self.play(Write(linea))
        self.wait(4)
        self.remove_foreground_mobjects(esf2)
        self.play(FadeOut(ejes2),FadeOut(esf2),FadeOut(n_l),FadeOut(linea),FadeOut(flecha))

        self.play(ReplacementTransform(t_3,t_4))
        self.wait(4)
        self.wait(6.5)
        self.wait(6)
        self.play(ReplacementTransform(t_4,t_5))
        self.wait(6.5)
        self.play(ReplacementTransform(t_5,t_6))
        self.wait(8.5)
        self.play(ReplacementTransform(t_6,t_7))
        self.wait(6.5)
        self.play(ReplacementTransform(t_7,t_8))
        self.wait(6)
        self.play(ReplacementTransform(t_8,t_9))
        self.wait(8.5)
        self.play(FadeOut(t_9))

        self.set_camera_orientation(phi=0.8*np.pi/2, theta=1.75*np.pi, distance=20) 
        self.play(ShowCreation(ejes))
        self.add_fixed_in_frame_mobjects(reglaf.group)
        self.play(Write(reglaf.group))
        self.add_fixed_in_frame_mobjects(Group2)
        fx_tex.add_updater(upd_for_decimal)
        self.play(Write(Group2),Write(fx_tex))
        self.add_fixed_in_frame_mobjects(fx_number_line_group)
        self.play(Write(fx_number_line_group))
        self.play(ShowCreation(esf))
        esf.add_updater(upd_for_sphere)
        self.wait()
        self.play(rad.set_value,3,run_time=4)
        self.wait()
        self.play(rad.set_value,0,run_time=4)
        self.wait()
        self.play( *[FadeOut(mob)for mob in self.mobjects] )
        
##############################################################################
############### Plano tangente y derivadas direccionales #####################
##############################################################################

# Anexado el 07 de Julio de 2021.

class Superficie1(ParametricSurface):

    def __init__(self, **kwargs):
        kwargs = {"u_min": -3,
                  "u_max": 3,
                  "v_min": -3,
                  "v_max": 3,
                  "checkerboard_colors": [GREEN]}
        ParametricSurface.__init__(self, self.func, **kwargs)
    
    # Parametrización de la superficie
    def func(self, u, v):
        return np.array([u, v, (u**2 - v**2)/4])
    
class Superficie2(ParametricSurface):

    def __init__(self, **kwargs):
        kwargs = {"u_min": -2.8,
                  "u_max": 2.8,
                  "v_min": -2,
                  "v_max": 2.8,
                  "checkerboard_colors": [ORANGE]}
        ParametricSurface.__init__(self, self.func, **kwargs)
    
    # Parametrización de la superficie
    def func(self, u, v):
        return np.array([u, v, (-(u**2+v**2)/3+2)*(u**2-v**2)/4])
    
class Superficie3(ParametricSurface):

    def __init__(self, **kwargs):
        kwargs = {"u_min": -3,
                  "u_max": 3,
                  "v_min": -3,
                  "v_max": 3,
                  "checkerboard_colors": [BLUE]}
        ParametricSurface.__init__(self, self.func, **kwargs)
    
    # Parametrización de la superficie
    def func(self, u, v):
        return np.array([u, v, (u**2 - v**2)/4])
    
class Paraboloide1(ParametricSurface):

    def __init__(self, **kwargs):
        kwargs = {"u_min": 0,
                  "u_max": 2,
                  "v_min": 0,
                  "v_max": 2*np.pi,
                  "checkerboard_colors": [BLUE]}
        ParametricSurface.__init__(self, self.func, **kwargs)
    
    # Parametrización del paraboloide
    def func(self, r, theta):
        u, v = r*np.cos(theta), r*np.sin(theta)
        return np.array([u, v, (u**2+v**2)/2])
    
class Paraboloide2(ParametricSurface):

    def __init__(self, **kwargs):
        kwargs = {"u_min": 0,
                  "u_max": 3,
                  "v_min": 0,
                  "v_max": 2*np.pi,
                  "checkerboard_colors": [BLUE]}
        ParametricSurface.__init__(self, self.func, **kwargs)
    
    # Parametrización del paraboloide
    def func(self, r, theta):
        u, v = r*np.cos(theta), r*np.sin(theta)
        return np.array([u, v, -(u**2+v**2)/3+2])

class Plano1(ParametricSurface):

    def __init__(self, **kwargs):
        kwargs = {"u_min": -1.3,
                  "u_max": 1.3,
                  "v_min": -1.3,
                  "v_max": 1.3,
                  "checkerboard_colors": [GOLD]}
        ParametricSurface.__init__(self, self.func, **kwargs)
    
    # Parametrización del plano
    def func(self, u, v):
        return np.array([u, v, np.sqrt(2)*u+np.sqrt(2)*v])

class Plano2(ParametricSurface):

    def __init__(self, **kwargs):
        kwargs = {"u_min": -1,
                  "u_max": 3,
                  "v_min": -1,
                  "v_max": 1.5,
                  "checkerboard_colors": [GOLD]}
        ParametricSurface.__init__(self, self.func, **kwargs)
    
    # Parametrización del plano
    def func(self, u, v):
        return np.array([u, 2-u, v])
    
class Plano3(ParametricSurface):

    def __init__(self, **kwargs):
        kwargs = {"u_min": -1.7,
                  "u_max": 2,
                  "v_min": -2.7,
                  "v_max": 2.7,
                  "checkerboard_colors": [GOLD]}
        ParametricSurface.__init__(self, self.func, **kwargs)
    
    # Parametrización del plano
    def func(self, u, v):
        return np.array([v, 0, u])

class Cono(ParametricSurface):

    def __init__(self, **kwargs):
        kwargs = {"u_min": 0,
                  "u_max": 1,
                  "v_min": 0,
                  "v_max": 2*np.pi,
                  "checkerboard_colors": [RED]}
        ParametricSurface.__init__(self, self.func, **kwargs)
    
    # Parametrización del cono
    def func(self, u, v):
        x, y = 2*u*np.cos(v), 2*u*np.sin(v)
        return np.array([x, y, 2*u])

class Plano_tangente(ThreeDScene):
    
    def paraboloide2(self, x, y):
        return -(x**2+y**2)/3+2
    
    def superficie2(self, x, y):
        return (-(x**2+y**2)/3+2)*(x**2-y**2)/4
    
    def superficie3(self, x, y):
        return (x**2-y**2)/4

    def curva1(self, t):
        return (t, 2-t, self.paraboloide2(t, 2-t))
    
    def curva2(self, t):
        return (t, 2-t, self.superficie2(t, 2-t))
    
    def curva3(self,t):
        return (t, 0, self.superficie3(t, 0))
    
    def tangente1(self,t):
        return (t/np.sqrt(2), 2-t/np.sqrt(2), 2/3+2*t*np.sqrt(2)/3)
    
    def tangente2(self,t):
        return (t/np.sqrt(2), 2-t/np.sqrt(2), -2/3-t*np.sqrt(2)/3)
    
    def tangente3(self,t):
        return (t, 0, 0)
    
    def recorrido(self, t):
        return (0, t, self.paraboloide2(0, t))
    
    def construct(self):
        
        # Textos de la animación
        title = TextMobject('''Plano tangente y\n
                            derivadas direccionales''').scale(1.5)
        
        # Textos de la primera sección
        text1_1 = TextMobject('''Consideremos estas dos superficies.''').move_to(3*UP)
        
        text2_1 = TextMobject('''Notemos que una es ``suave'' en el origen, \n
                            mientras que la otra tiene un ``pico''.''').move_to(3*UP)
        
        text3_1 = TextMobject('''¿Qué significa esto matemáticamente hablando?''').move_to(3*UP)
        
        text4_1_1 = TextMobject('''Definición 1.''', ''' Sean $f:U\\subset\\mathbb{R}^{2}\\to\\mathbb{R}$ y $(x_{0},y_{0}) \\in U \\cap U'$, f es\n
                              diferenciable en $(x_{0},y_{0})$ si y solo si existe $(m_{1},m_{2})\\in\\mathbb{R}^{2}$ tal que''').move_to(UP)
        
        text4_1_1.set_color_by_tex('''Definición 1.''', color = TEAL)
        
        text4_1_1.scale(0.9)
        
        text4_2_1 = TextMobject('''$$\\lim_{(h_{1},h_{2})\\to(0,0)}\\dfrac{f((x_{0},y_{0})+(h_{1},h_{2}))-(f(x_{0},y_{0})+(m_{1},m_{2})\\cdot(h_{1},h_{2}))}{||(h_{1},h_{2})||}=0.$$''').next_to(text4_1_1, 2*DOWN)
        
        text4_2_1.scale(0.8)
        
        text5_1_1 = TextMobject('''Haciendo el cambio de variables $h_{1}=x-x_{0}$ y $h_{2}=y-y_{0}$,''').move_to(3*UP)
               
        text5_2_1 = TextMobject('''$$\\lim_{(x,y)\\to(x_{0},y_{0})}\\dfrac{f((x_{0},y_{0})+(x-x_{0},y-y_{0}))-(f(x_{0},y_{0})+(m_{1},m_{2})\\cdot(x-x_{0},y-y_{0}))}{||(x-x_{0},y-y_{0})||}=0.$$''').next_to(text5_1_1, 2*DOWN)
    
        text5_2_1.scale(0.7)
    
        text6_1_1 = TextMobject('''Desarrollando la expresión anterior,''').next_to(text5_2_1, 2*DOWN)
    
        text6_2_1 = TextMobject('''$$\\lim_{(x,y)\\to(x_{0},y_{0})}\\dfrac{f(x,y)-(f(x_{0},y_{0})+m_{1}(x-x_{0})+m_{2}(y-y_{0}))}{||(x-x_{0},y-y_{0})||}=0.$$''').next_to(text6_1_1, 2*DOWN)
    
        text6_2_1.scale(0.7)
    
        text7_1 = TextMobject('''Intuitivamente, $(m_{1},m_{2})$ nos da la inclinación del plano\n
                              que más se parece a la función en $(x_{0}, y_{0})$.''').next_to(text6_2_1, 3*DOWN)
        
        text8_1 = TextMobject('''Primero observemos que la gráfica de $m_{1}x+m_{2}y$\n
                              nos da un plano que contiene al origen.''').move_to(3*DOWN)
        
        func_text = TextMobject('''$f(x,y)=\\frac{x^{2}+y^{2}}{2}$''')
        
        func_text.scale(0.7)
        
        func_text.move_to(5*RIGHT+2*UP)
        
        punto_text = TextMobject('''$(x_{0},y_{0})=(\\sqrt{2},\\sqrt{2})$''')
        
        punto_text.scale(0.7)
        
        punto_text.next_to(func_text, DOWN)
        
        text9_1 = TextMobject('''Si a dicho plano lo trasladamos a $(x_{0},y_{0},f(x_{0},y_{0}))$, obtendremos\n
                              el plano tangente a la superficie en ese mismo punto.''').move_to(3*DOWN)
                              
        text9_1.scale(0.9)
        
        text10_1 = TextMobject('''Definición 2.''', ''' Sea $f:U\\subset\\mathbb{R}^{2}\\to\\mathbb{R}$ diferenciable en \n
                               $(x_{0},y_{0})\\in U \\cap U'$, decimos que el plano que tiene como\n
                               ecuación $f(x_{0},y_{0})+m_{1}(x-x_{0})+m_{2}(y-y_{0})$ es el plano\n
                               tangente a la gráfica de $f$ en el punto $(x_{0},y_{0},f(x_{0},y_{0}))$,\n
                               donde $(m_{1},m_{2})$ es el vector que cumple la ''', '''Definición 1.''')
                    
        text10_1.set_color_by_tex('''Definición 2.''', color = TEAL)
        text10_1.set_color_by_tex('''Definición 1.''', color = TEAL)
        
        text11_1 = TextMobject('''De manera general, para $f:U\\subset\\mathbb{R}^n\\to\\mathbb{R}$, $f$ es diferenciable\n
                               en $\\vec{x}_{0}\\in U\\cap U'$ si y solo si existe $\\vec{m}\\in\\mathbb{R}^n$ tal que
                               $$\\lim_{\\vec{h}\\to\\vec{0}}\\dfrac{f\\left(\\vec{x}_0+\\vec{h}\\right)-\\left(f(\\vec{x}_0)+\\vec{m}\\cdot\\vec{h}\\right)}{||\\vec{h}||}=0.$$''')
        
        text12_1 = TextMobject('''Por lo tanto, podemos decir que $f$ es diferenciable en $\\vec{x}_{0}$ si y\n
                               solo si el plano tangente a la función en $(\\vec{x}_{0},f(\\vec{x}_{0}))$ es una\n
                               buena aproximación para la función alrededor de ese punto.''').move_to(UP)
                               
        text13_1 = TextMobject('''Pero, ''', '''¿cómo podemos encontrar al vector $\\vec{m}$?''').next_to(text12_1, 3*DOWN)
        
        text13_1.set_color_by_tex('''¿cómo podemos encontrar al vector $\\vec{m}$?''', color = TEAL)
        
        # Textos de la segunda sección
        subtitle1 = TextMobject('''Derivadas direccionales''').scale(1.5)

        text1_2 = TextMobject('''Consideremos $f:U\\subset\\mathbb{R}^{2}\\to\\mathbb{R}$ y tomemos\n
                              $\\vec{x}_{0}\\in U$ y $\\vec{u}\\in\\mathbb{R}^{n}$ tal que $||\\vec{u}||=1$.''').move_to(3*UP) 
                            
        text2_2 = TextMobject('''La función $f$ es derivable en el punto $\\vec{x}_{0}$ en la dirección
                            $$\\text{del vector }\\vec{u}\\text{ si }\\lim_{h\\to 0}\\frac{f(\\vec{x}_{0}+h\\vec{u})-f(\\vec{x}_{0})}{h}\\text{ existe.}$$''')
                            
        text3_2 = TextMobject('''Al valor de dicho límite se le denota por ''', '''$D_{\\vec{u}}f(\\vec{x_{0}})$.''').move_to(2*DOWN)
        
        text3_2.set_color_by_tex('''$D_{\\vec{u}}f(\\vec{x_{0}})$.''', color = TEAL)
        
        text4_2 = TextMobject('''¿Qué similitudes y diferencias encuentras\n
                              entre la definición anterior y la definición\n
                              de derivabilidad para funciones de $\\mathbb{R}$ en $\\mathbb{R}$?''').move_to(3*UP)
        
        text5_2 = TextMobject('''En general, $D_{\\vec{u}}f(\\vec{x_{0}})$ es una medida de la\n
                            razón de cambio instantánea de la función $f$,\n
                            partiendo del vector $\\vec{x}_{0}$ y en la dirección de $\\vec{u}$.''')
        
        text6_2 = TextMobject('''La derivada direccional tiene una\n
                              interpretación geométrica útil.''').move_to(2*DOWN)
        
        text7_2 = TextMobject('''La siguiente función $f$ es derivable en\n
                              el punto $(0,2)$ en la dirección $\\left(-\\frac{1}{\\sqrt{2}},\\frac{1}{\\sqrt{2}}\\right)$.''').move_to(3*UP)
        
        func_text2 = TextMobject('''$f(x,y)=-\\frac{x^2 + y^2}{3}+2$''').move_to(3*DOWN-3.5*RIGHT)
                            
        text8_2 = TextMobject('''Al intersecar la gráfica de $f$ con el plano perpendicular a $XY$ que contiene\n
                            a la recta $\\vec{x}_{0}+h\\vec{u}=(0,2)+h\\left(-\\frac{1}{\\sqrt{2}},\\frac{1}{\\sqrt{2}}\\right)$, $h\\in\\mathbb{R}$, se obtiene una curva.''').move_to(3*UP)
        
        text8_2.scale(0.8)

        text9_2 = TextMobject('''$D_{\\vec{u}}f(0,2) = -\\frac{2\\sqrt{2}}{3}$ es la pendiente de la recta \n 
                                tangente a la curva en el punto $\\left(0,2,\\frac{2}{3}\\right)$.''').move_to(3*UP) 
        
        text10_2 = TextMobject('''Es decir, la derivada direccional coincide con la pendiente\n
                              de la recta tangente en el corte correspondiente.''').move_to(3*UP)
                             
        text11_2 = TextMobject('''Muchas de las propiedades que cumplen las\n
                              derivadas de funciones de $\\mathbb{R}$ en $\\mathbb{R}$, las conservan\n 
                              de cierta forma las derivadas direccionales, como\n
                              las relacionadas con la aritmética de funciones.''')
                             
        text12_2 = TextMobject('''Por ejemplo, si tenemos dos funciones tales que\n
                                $D_{\\vec{u}}f(\\vec{x_{0}})$ y $D_{\\vec{u}}g(\\vec{x_{0}})$ existen, $D_{\\vec{u}}(fg)(\\vec{x_{0}})$ existe y además''',
                                '''$$D_{\\vec{u}}(fg)(\\vec{x_{0}}) = f(\\vec{x}_{0})D_{\\vec{u}}g(\\vec{x_{0}}) + g(\\vec{x}_{0})D_{\\vec{u}}f(\\vec{x_{0}}).$$''')
        
        text12_2.set_color_by_tex('''$$D_{\\vec{u}}(fg)(\\vec{x_{0}}) = f(\\vec{x}_{0})D_{\\vec{u}}g(\\vec{x_{0}}) + g(\\vec{x}_{0})D_{\\vec{u}}f(\\vec{x_{0}}).$$''', color = TEAL)
        
        text13_2 = TextMobject('''Para ver lo anterior, consideremos los mismos $f$, $\\vec{u}$ y $\\vec{x}_{0}$,\n
                                y tomemos $g(x, y) = \\frac{x^{2}-y^{2}}{4}$.''').move_to(3*UP) 
        
        f_text = TextMobject('''$f(0,2)=\\frac{2}{3}$''').move_to(4*LEFT+2*DOWN)
        g_text = TextMobject('''$g(0,2)=-1$''').next_to(f_text, DOWN)
        
        f_text.scale(0.8)
        g_text.scale(0.8)
        
        df_text = TextMobject('''$D_{\\vec{u}}f(0,2)=-\\frac{2\\sqrt{2}}{3}$''').move_to(2*DOWN)
        dg_text = TextMobject('''$D_{\\vec{u}}g(0,2)=-\\frac{\\sqrt{2}}{2}$''').next_to(df_text, DOWN)       
        dfg_text = TextMobject('''$D_{\\vec{u}}(fg)(0,2)=\\frac{\\sqrt{2}}{3}$''').move_to(4*RIGHT+2*DOWN)
        
        df_text.scale(0.8)
        dg_text.scale(0.8)
        dfg_text.scale(0.8)
        
        # Textos de la última sección
        subtitle2 = TextMobject('''Derivadas parciales''').scale(1.5)

        text1_3 = TextMobject('''Sea $f:U\\subset\\mathbb{R}^2\\to\\mathbb{R}$, fijémonos en un punto\n
                              $\\vec{x}_0\\in U$ y el respectivo valor para $f(\\vec{x}_0)$.''').move_to(3*UP)
        
        func_text3 = TextMobject('''$f(x)=\\frac{x^2-y^2}{4}$''').move_to(2.5*DOWN-3.2*RIGHT)

        text2_3 = TextMobject('''Podemos obtener las derivadas direccionales de\n
                              $f$ en $\\vec{x}_0$ en una multitud de direcciones.''').move_to(3*UP)
        
        text3_3 = TextMobject('''Particularmente nos podemos fijar en aquellas en las que se\n
                              utiliza una dirección canónica dada por $\\vec{e}_1$ o por $\\vec{e}_2$.''').move_to(3*UP)
        
        text4_3 = TextMobject('''Tomemos la derivada en la dirección $\\vec{e}_1$.''').move_to(3*UP)
                              
        text5_1_3 = TextMobject('''A esta la podemos ver de la forma''').move_to(2*UP)
        
        text5_2_3 = TextMobject('''$$D_{\\vec{e}_1}f(\\vec{x}_0)=\\lim_{h\\to 0}\\dfrac{f(\\vec{x}_0+h \\ \\ \\vec{e}_1 \\ \\ )-f(\\vec{x_0})}{h}.$$''').next_to(text5_1_3, 2*DOWN)
        
        text6_1_3 = TextMobject('''Recordando que $\\vec{e}_1=(1,0)$,''').move_to(2*UP)
        
        text6_2_3 = TextMobject('''$$D_{\\vec{e}_1}f(\\vec{x}_0)=\\lim_{h\\to 0}\\dfrac{f(\\vec{x}_0+h(1,0))-f(\\vec{x_0})}{h}.$$''').next_to(text6_1_3, 2*DOWN)
        
        text6_3_3 = TextMobject('''$$D_{\\vec{e}_1}f(\\vec{x}_0)=\\lim_{h\\to 0}\\dfrac{f(\\vec{x}_0+(h,0))-f(\\vec{x_0})}{h}.$$''').next_to(text6_1_3, 2*DOWN)
        
        text7_3 = TextMobject('''A este caso particular de la derivada direccional se le\n
                                conoce como derivada parcial de $f$ con respecto a $x$.''').next_to(text6_3_3, 3*DOWN)
        
        text8_3 = TextMobject('''Se representa de la forma''',
                              '''$$\\dfrac{\\partial f}{\\partial x}(\\vec{x}_0)=\\lim_{h\\to0}\\dfrac{f(\\vec{x}_0+h\\vec{e}_1)-f(\\vec{x}_0)}{h}.$$''').move_to(2*UP)
        
        text8_3.set_color_by_tex('''$$\\dfrac{\\partial f}{\\partial x}(\\vec{x}_0)''', color = TEAL)
        
        text9_3 = TextMobject('''Análogamente, tenemos''',
                              '''$$\\dfrac{\\partial f}{\\partial y}(\\vec{x}_0)=\\lim_{h\\to0}\\dfrac{f(\\vec{x}_0+h\\vec{e}_2)-f(\\vec{x}_0)}{h}.$$''').next_to(text8_3, 2*DOWN)

        text9_3.set_color_by_tex('''$$\\dfrac{\\partial f}{\\partial y}(\\vec{x}_0)''', color = TEAL)
                                      
        text10_3 = TextMobject('''En general, si $f:U\\subset\\mathbb{R}^n\\to\\mathbb{R}$, $\\vec{x}_0\\in U$, para cada\n
                              $$i\\in\\{1,...,n\\}\\text{ se tiene }\\dfrac{\\partial f}{\\partial x_i}(\\vec{x}_0)=\\lim_{h\\to0}\\dfrac{f(\\vec{x}_0+h\\vec{e}_i)-f(\\vec{x}_0)}{h}.$$''')
            
        text11_3 = TextMobject('''$\\frac{\\partial f}{\\partial x_i}(\\vec{x}_{0})$ es la pendiente de la recta tangente\n
                               a $f$ en $\\vec{x}_0$ en la $i-$ésima dirección canónica.''').move_to(3*UP)
                                
        text12_3 = TextMobject('''De esta forma se puede ver a $\\frac{\\partial f}{\\partial x_i}$ como la derivada\n
                               de $f$ en el $i-$ésimo corte canónico.''').move_to(3*UP)
        
        text13_3 = TextMobject('''Al vector $\\left(\\frac{\\partial f}{\\partial x_1}(\\vec{x}_0),...,\\frac{\\partial f}{\\partial x_n}(\\vec{x}_0)\\right)$ se le llama\n
                                gradiente de $f$ en $\\vec{x}_0$, representado como $\\nabla f(x_0)$,\n
                                y es la mejor aproximación lineal a $f$ en el punto $\\vec{x}_{0}$.''')
        
        text14_3 = TextMobject('''Por lo tanto, si una función $f$ es diferenciable en $\\vec{x}_{0}$,\n
                               ¡el vector $\\vec{m}$ que buscamos y que cumple la ''', '''Definición 1''', '''\n
                               es ''', '''$\\vec{m}=\\nabla f(\\vec{x}_{0})$''','''$=\\left(\\frac{\\partial f}{\\partial x_1}(\\vec{x}_{0}),...,\\frac{\\partial f}{\\partial x_n}(\\vec{x}_{0})\\right)$!''')
        
        text14_3.set_color_by_tex('''Definición 1''', color = TEAL)
        text14_3.set_color_by_tex('''$\\vec{m}=\\nabla f(\\vec{x}_{0})$''', color = TEAL)
        
        text15_3 = TextMobject('''Adicionalmente, el gradiente tiene\n
                               un par de usos importantes.''').move_to(UP)
	
        text16_3 = TextMobject('''En primer lugar, si $f$ es diferenciable, el\n
                               gradiente nos permite expresar sus derivadas\n
                               direccionales como $D_{\\vec{u}}f(\\vec{x_{0}})=\\nabla f(\\vec{x}_0)\\cdot\\vec{u}$.''').next_to(text15_3, 3*DOWN)
        
        text17_3 = TextMobject('''En segundo lugar, el gradiente apunta en la\n
                               dirección y sentido de máxima razón de cambio, como\n
                               como consecuencia de que $D_{\\vec{u}}f(\\vec{x}_0)=||\\nabla f(\\vec{x}_0)||\\cdot\\cos\\theta$,\n
                               donde $\\theta$ es el ángulo entre el gradiente y $\\vec{u}$.''').move_to(UP)
        
        text18_3 = TextMobject('''Por lo mismo, en el sentido contrario del gradiente\n
                               se obtiene el máximo decrecimiento de $f$.''').next_to(text17_3, 3*DOWN)
        
        text19_3 = TextMobject('''Regresemos a la función $f(x,y)=-\\frac{x^{2}+y^{2}}{3}+2$,\n
                               donde $\\nabla f(x,y)=\\left(\\frac{-2x}{3},\\frac{-2y}{3}\\right)$.''').move_to(3*UP)
        
        text20_1_3 = TextMobject('''$\\nabla f(0,2)\\cdot\\left(-\\frac{1}{\\sqrt{2}},\\frac{1}{\\sqrt{2}}\\right)=-\\frac{2\\sqrt{2}}{3}$, que es el valor que obtuvimos''').move_to(3*DOWN)
        
        text20_1_3.scale(0.8)
        
        text20_2_3 = TextMobject('''inicialmente para la derivada de $f$ en $(0,2)$ y en la dirección $\\left(-\\frac{1}{\\sqrt{2}},\\frac{1}{\\sqrt{2}}\\right)$.''').move_to(3*DOWN)
        
        text20_2_3.scale(0.8)
        
        text21_3 = TextMobject('''Al recorrer el dominio hacia abajo desde $(0,2)$, la superficie crece con mayor inclinación como si estuviéramos en un monte; la pendiente al subir es de $\\frac{16}{9}$.''').move_to(3.5*DOWN)
        
        text21_3.scale(0.8)
        
        text22_3 = TextMobject('''En cambio, al avanzar hacia arriba en el dominio desde el punto $(0,2)$, la superficie va de bajada con una pendiente de $-\\frac{16}{9}$, que es la menor inclinación.''').move_to(3.5*DOWN)
        
        text22_3.scale(0.8)        
        
        # Recuadros para algunos textos
        text1_1.bg = SurroundingRectangle(text1_1, color = WHITE, fill_color = BLACK, fill_opacity = 1)
        gpo1_1 = VGroup(text1_1.bg, text1_1)
        
        text2_1.bg = SurroundingRectangle(text2_1, color = WHITE, fill_color = BLACK, fill_opacity = 1)
        gpo2_1 = VGroup(text2_1.bg, text2_1)
        
        text3_1.bg = SurroundingRectangle(text3_1, color = WHITE, fill_color = BLACK, fill_opacity = 1)
        gpo3_1 = VGroup(text3_1.bg, text3_1)
        
        text8_1.bg = SurroundingRectangle(text8_1, color = WHITE, fill_color = BLACK, fill_opacity = 1)
        gpo8_1 = VGroup(text8_1.bg, text8_1)
        
        text9_1.bg = SurroundingRectangle(text9_1, color = WHITE, fill_color = BLACK, fill_opacity = 1)
        gpo9_1 = VGroup(text9_1.bg, text9_1)
        
        text7_2.bg = SurroundingRectangle(text7_2, color = WHITE, fill_color = BLACK, fill_opacity = 1)
        gpo7_2 = VGroup(text7_2.bg, text7_2)
        
        text8_2.bg = SurroundingRectangle(text8_2, color = WHITE, fill_color = BLACK, fill_opacity = 1)
        gpo8_2 = VGroup(text8_2.bg, text8_2)
        
        text9_2.bg = SurroundingRectangle(text9_2, color = WHITE, fill_color = BLACK, fill_opacity = 1)
        gpo9_2 = VGroup(text9_2.bg, text9_2)
        
        text10_2.bg = SurroundingRectangle(text10_2, color = WHITE, fill_color = BLACK, fill_opacity = 1)
        gpo10_2 = VGroup(text10_2.bg, text10_2)
        
        text13_2.bg = SurroundingRectangle(text13_2, color = WHITE, fill_color = BLACK, fill_opacity = 1)
        gpo13_2 = VGroup(text13_2.bg, text13_2)
        
        text1_3.bg = SurroundingRectangle(text1_3, color = WHITE, fill_color = BLACK, fill_opacity = 1)
        gpo1_3 = VGroup(text1_3.bg, text1_3)
        
        text2_3.bg = SurroundingRectangle(text2_3, color = WHITE, fill_color = BLACK, fill_opacity = 1)
        gpo2_3 = VGroup(text2_3.bg, text2_3)
        
        text3_3.bg = SurroundingRectangle(text3_3, color = WHITE, fill_color = BLACK, fill_opacity = 1)
        gpo3_3 = VGroup(text3_3.bg, text3_3)
        
        text4_3.bg = SurroundingRectangle(text4_3, color = WHITE, fill_color = BLACK, fill_opacity = 1)
        gpo4_3 = VGroup(text4_3.bg, text4_3)
        
        text11_3.bg = SurroundingRectangle(text11_3, color = WHITE, fill_color = BLACK, fill_opacity = 1)
        gpo11_3 = VGroup(text11_3.bg, text11_3)
        
        text12_3.bg = SurroundingRectangle(text12_3, color = WHITE, fill_color = BLACK, fill_opacity = 1)
        gpo12_3 = VGroup(text12_3.bg, text12_3)
        
        text19_3.bg = SurroundingRectangle(text19_3, color = WHITE, fill_color = BLACK, fill_opacity = 1)
        gpo19_3 = VGroup(text19_3.bg, text19_3) 
        
        # Ejes utilizados en la animación
        axis_config_1 = {"dimension": 3,
                        "x_min": -3,
                        "x_max": 3,
                        "y_min": -3,
                        "y_max": 3,
                        "z_min": -1,
                        "z_max": 2,
                        "light_source": 9*DOWN + 7*LEFT + 10*OUT}
        
        axis_config_2 = {"dimension": 3,
                        "x_min": -4,
                        "x_max": 4,
                        "y_min": -4,
                        "y_max": 4,
                        "z_min": -1,
                        "z_max": 3,
                        "light_source": 9*DOWN + 7*LEFT + 10*OUT}
        
        axis_config_3 = {"dimension": 3,
                       "x_min": -3.5,
                       "x_max": 3.5,
                       "y_min": -3.5,
                       "y_max": 3.5,
                       "z_min": -2,
                       "z_max": 3,
                       "light_source": 9*DOWN + 7*LEFT + 10*OUT}
        
        axes_1 = ThreeDAxes(**axis_config_1)
        axes_c = ThreeDAxes(**axis_config_1)
        axes_p = ThreeDAxes(**axis_config_1)
        
        axes_2 = ThreeDAxes(**axis_config_2)
        axes_f = ThreeDAxes(**axis_config_2)
        axes_g = ThreeDAxes(**axis_config_2)
        
        axes_3 = ThreeDAxes(**axis_config_3)
        
        # Superficies utilizadas en la animación
        cono = Cono().set_shade_in_3d(True)
        graf_cono = VGroup(axes_c, cono)
        graf_cono.move_to(2*RIGHT+2*DOWN)
        
        paraboloide1 = Paraboloide1().set_shade_in_3d(True)
        graf_parab = VGroup(axes_p, paraboloide1)
        graf_parab.move_to(2*LEFT+2*UP)
        
        plano1 = Plano1().set_shade_in_3d(True)
        plano2 = Plano2().set_shade_in_3d(True)
        plano3 = Plano3().set_shade_in_3d(True)
        
        paraboloide2 = Paraboloide2().set_shade_in_3d(True)
        superficie1 = Superficie1().set_shade_in_3d(True)
        superficie2 = Superficie2().set_shade_in_3d(True)
        
        superficie3 = Superficie3().set_shade_in_3d(True)

        # Otros objetos necesarios para la animación
        x_0, y_0 = 0, 2
        z_0 = self.paraboloide2(x_0, y_0)
        
        x_1, y_1 = 0, 0
        z_1 = self.superficie3(x_1, y_1)
        
        punto1 = Dot(color = YELLOW).move_to([x_0, y_0, 0]).set_shade_in_3d(True)
        direc = Vector(direction = [-1/np.sqrt(2), 1/np.sqrt(2), 0], buff = 0.075).set_color(YELLOW)
        
        punto2 = Dot(color=YELLOW).move_to([x_1, y_1, z_1]).set_shade_in_3d(True)

        curva1 = ParametricFunction(self.curva1, t_min = 1-np.sqrt(7)/np.sqrt(2), t_max = 1+np.sqrt(7)/np.sqrt(2), color = BLUE)
        curva2 = ParametricFunction(self.curva2, t_min = -0.802328, t_max = 2.6980, color = ORANGE)
        curva3 = ParametricFunction(self.curva3, t_min = -2.7, t_max = 2.7, color = BLUE)
        
        tangente1 = ParametricFunction(self.tangente1, t_min = -np.sqrt(2), t_max = 5/(4*np.sqrt(2)), color = PURPLE)
        tangente2 = ParametricFunction(self.tangente2, t_min = -np.sqrt(2), t_max = 1/np.sqrt(2), color = PURPLE)
        tangente3 = ParametricFunction(self.tangente3, t_min = -2.7, t_max = 2.7, color = PURPLE)
     
        recorrido_a = DashedVMobject(ParametricFunction(self.recorrido, t_min = 2, t_max = 0, color = GREEN_E))
        recorrido_b = DashedVMobject(ParametricFunction(self.recorrido, t_min = 2, t_max = 3, color = RED_E))
         
        circulo = Circle(radius = 0.01, color = PURPLE).move_to(punto2.get_center())

        # Función que cambia el tamaño de un círculo
        rad = ValueTracker(0.01)
        def upd_for_circle(obj):
            c = obj
            new_c = Circle(radius = rad.get_value(), color = PURPLE).move_to(punto2.get_center())
            c.become(new_c)

        # Flechas para las derivadas direccionales
        dir1 = Arrow((0,0,0), (1/np.sqrt(2), -1/np.sqrt(2), 0), buff = 0.075)
        dir2 = Arrow((0,0,0), (1/np.sqrt(2), 1/np.sqrt(2), 0), buff = 0.075)
        dir3 = Arrow((0,0,0), (-1/np.sqrt(2), -1/np.sqrt(2), 0), buff = 0.075)
        dir4 = Arrow((0,0,0), (-1/np.sqrt(2), 1/np.sqrt(2), 0), buff = 0.075)
        dir5 = Arrow((0,0,0), (0, -1, 0), buff = 0.075)
        dir6 = Arrow((0,0,0), (0, 1, 0), buff = 0.075)
        dir6_r = dir6.copy().set_color(RED)
        dir7 = Arrow((0,0,0), (-1, 0, 0), buff = 0.075)
        dir8 = Arrow((0,0,0), (1, 0, 0), buff = 0.075)
        dir8_r = dir8.copy().set_color(RED)
        dir8_y = dir8.copy().set_color(YELLOW)
        Dirs = VGroup(dir1, dir2, dir3, dir4, dir5, dir6, dir7, dir8)
        Dirs.set_color(PURPLE)
        
        # Escena
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))
        
        # Plano tangente y derivabilidad
        self.set_camera_orientation(0.7*np.pi/2, 0.25*np.pi)
        self.add_fixed_in_frame_mobjects(gpo1_1)
        self.play(Write(gpo1_1))
        self.play(ShowCreation(graf_cono))
        self.play(ShowCreation(graf_parab))
        self.wait()
        self.play(FadeOut(gpo1_1))
        self.add_fixed_in_frame_mobjects(gpo2_1)
        self.play(Write(gpo2_1))
        self.wait(2)
        self.play(FadeOut(gpo2_1))
        self.add_fixed_in_frame_mobjects(gpo3_1)
        self.play(Write(gpo3_1))
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        self.set_camera_orientation(phi = 0, theta = -90*DEGREES)
        self.play(Write(text4_1_1))
        self.wait(8)
        self.play(Write(text4_2_1))
        self.wait(8)
        self.play(FadeOut(text4_1_1), FadeOut(text4_2_1))
        self.play(Write(text5_1_1))
        self.wait(2)
        self.play(Write(text5_2_1))
        self.wait(5)
        self.play(Write(text6_1_1))
        self.wait(2)
        self.play(Write(text6_2_1))
        self.wait(5)
        self.play(Write(text7_1))
        self.wait(5)
        self.play(*[FadeOut(mob)for mob in self.mobjects])
        
        self.set_camera_orientation(0.7*np.pi/2, 0.25*np.pi)
        self.add_fixed_in_frame_mobjects(gpo8_1)
        self.play(Write(gpo8_1))
        self.play(ShowCreation(axes_1))
        self.add_fixed_in_frame_mobjects(func_text, punto_text)
        self.play(Write(func_text), Write(punto_text))
        self.play(ShowCreation(Paraboloide1().set_shade_in_3d(True)))
        self.play(ShowCreation(plano1))
        self.wait()
        self.play(FadeOut(gpo8_1))
        self.add_fixed_in_frame_mobjects(gpo9_1)
        self.play(Write(gpo9_1))
        self.play(ApplyMethod(plano1.move_to, [np.sqrt(2), np.sqrt(2), 2]))
        self.wait()
        self.move_camera(85*DEGREES, -40*DEGREES, frame_center = (0,0,0), run_time = 2)
        self.wait()
        self.play(*[FadeOut(mob)for mob in self.mobjects])
        
        self.set_camera_orientation(phi = 0, theta = -90*DEGREES)
        self.play(Write(text10_1))
        self.wait(15)
        self.play(FadeOut(text10_1))
        self.play(Write(text11_1))
        self.wait(10)
        self.play(FadeOut(text11_1))
        self.play(Write(text12_1))
        self.wait(10)
        self.play(Write(text13_1))
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])
        
        # Derivadas direccionales
        self.play(Write(subtitle1))
        self.wait()
        self.play(FadeOut(subtitle1))

        self.play(Write(text1_2))
        self.wait(3)
        self.play(Write(text2_2))
        self.wait(5)
        self.play(Write(text3_2))
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])
        self.play(Write(text4_2))
        self.wait(5)
        self.play(Write(text5_2))
        self.wait(5)
        self.play(Write(text6_2))
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        self.set_camera_orientation(0.7*np.pi/2, 0.25*np.pi)
        self.add_fixed_in_frame_mobjects(gpo7_2, func_text2)
        self.play(Write(gpo7_2), Write(func_text2))
        self.play(ShowCreation(axes_2))
        self.play(ShowCreation(punto1), ShowCreation(direc))
        self.wait()
        self.play(ApplyMethod(punto1.move_to, [x_0, y_0, self.paraboloide2(x_0, y_0)]))
        self.play(ApplyMethod(direc.move_to, [x_0-1/(2*np.sqrt(2)), y_0+1/(2*np.sqrt(2)), self.paraboloide2(x_0, y_0)]))
        self.play(ShowCreation(paraboloide2))
        self.wait()
        self.play(FadeOut(gpo7_2))
        self.add_fixed_in_frame_mobjects(gpo8_2)
        self.play(Write(gpo8_2))
        self.wait()
        self.play(FadeOut(direc), ShowCreation(plano2))
        self.play(ShowCreation(curva1), FadeOut(paraboloide2))
        self.move_camera(90*DEGREES, 45*DEGREES, frame_center = (0,0,0), run_time = 2)
        self.wait()
        self.play(FadeOut(gpo8_2))
        self.add_fixed_in_frame_mobjects(gpo9_2)
        self.play(Write(gpo9_2))
        self.play(ShowCreation(tangente1))
        self.wait(2)
        self.play(FadeOut(gpo9_2))
        self.add_fixed_in_frame_mobjects(gpo10_2)
        self.play(Write(gpo10_2))
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])
        
        self.set_camera_orientation(phi = 0, theta = -90*DEGREES)
        self.play(Write(text11_2))
        self.wait(10)
        self.play(FadeOut(text11_2))
        self.play(Write(text12_2))
        self.wait(10)
        self.play(*[FadeOut(mob)for mob in self.mobjects])
        
        self.set_camera_orientation(0.7*np.pi/2, 0.25*np.pi)
        self.add_fixed_in_frame_mobjects(gpo13_2)
        self.play(Write(gpo13_2))
        graf_f = VGroup(axes_f, paraboloide2)
        graf_f.move_to(2.5*RIGHT+2*DOWN)
        graf_f.scale(0.8)
        graf_g = VGroup(axes_g, superficie1)
        graf_g.move_to(1.5*LEFT+3*UP)
        graf_g.scale(0.8)
        self.play(ShowCreation(graf_f), ShowCreation(graf_g))
        self.wait()
        self.play(FadeOut(graf_f), FadeOut(graf_g))
        self.play(ShowCreation(axes_2), ShowCreation(superficie2))
        self.wait()
        self.play(ShowCreation(plano2))
        self.play(ShowCreation(curva2), FadeOut(superficie2))
        self.move_camera(90*DEGREES, 45*DEGREES, frame_center = (0,0,0), run_time = 2)
        self.add_fixed_in_frame_mobjects(f_text, g_text)
        self.play(Write(f_text), Write(g_text))
        self.add_fixed_in_frame_mobjects(df_text, dg_text)
        self.play(Write(df_text), Write(dg_text))
        self.add_fixed_in_frame_mobjects(dfg_text)
        self.play(Write(dfg_text))
        self.play(ShowCreation(tangente2))
        self.wait()
        self.play(*[FadeOut(mob)for mob in self.mobjects])
        
        # Derivadas parciales
        self.set_camera_orientation(phi = 0, theta = -90*DEGREES)
        self.play(Write(subtitle2))
        self.wait()
        self.play(FadeOut(subtitle2))
        
        self.set_camera_orientation(0.7*np.pi/2, 0.25*np.pi)
        self.add_fixed_in_frame_mobjects(gpo1_3)
        self.play(Write(gpo1_3))
        self.play(ShowCreation(axes_3))
        self.add_fixed_in_frame_mobjects(func_text3)
        self.play(Write(func_text3))
        self.play(ShowCreation(superficie3))
        self.play(ShowCreation(punto2))
        self.wait()
        self.play(FadeOut(gpo1_3))
        self.add_fixed_in_frame_mobjects(gpo2_3)
        self.play(Write(gpo2_3))
        self.play(ShowCreation(circulo))
        circulo.add_updater(upd_for_circle)
        self.play(rad.set_value, 1, rate_func = linear)
        self.play(ShowCreation(Dirs))
        self.wait()
        self.play(FadeOut(gpo2_3))
        self.add_fixed_in_frame_mobjects(gpo3_3)
        self.play(Write(gpo3_3))
        self.play(FadeOut(Dirs), ReplacementTransform(dir6, dir6_r), ReplacementTransform(dir8, dir8_r))
        self.wait(3)
        self.play(FadeOut(gpo3_3))
        self.add_fixed_in_frame_mobjects(gpo4_3)
        self.play(Write(gpo4_3))
        self.play(FadeOut(dir6_r), ReplacementTransform(dir8_r, dir8_y))
        self.wait()
        self.play(FadeOut(gpo4_3))
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        self.set_camera_orientation(phi = 0, theta = -90*DEGREES)
        self.play(Write(text5_1_3))
        self.play(Write(text5_2_3))
        self.wait(5)
        self.play(ReplacementTransform(text5_1_3, text6_1_3))
        self.wait()
        self.play(ReplacementTransform(VGroup(text5_2_3[0][24], text5_2_3[0][25], text5_2_3[0][26]), VGroup(text6_2_3[0][24], text6_2_3[0][25], text6_2_3[0][26], text6_2_3[0][27], text6_2_3[0][28])))
        self.wait()
        self.play(ReplacementTransform(VGroup(text5_2_3[0][23], text6_2_3[0][24], text6_2_3[0][25], text6_2_3[0][26], text6_2_3[0][27], text6_2_3[0][28]), VGroup(text6_3_3[0][23], text6_3_3[0][24], text6_3_3[0][25], text6_3_3[0][26], text6_3_3[0][27])))
        self.wait()
        self.play(Write(text7_3))
        self.wait(3)
        self.play(*[FadeOut(mob)for mob in self.mobjects])
        self.play(Write(text8_3))
        self.wait(3)
        self.play(Write(text9_3))
        self.wait(3)
        self.play(FadeOut(text8_3), FadeOut(text9_3))
        self.play(Write(text10_3))
        self.wait(3)
        self.play(FadeOut(text10_3))

        self.set_camera_orientation(0.7*np.pi/2, 0.25*np.pi)
        self.play(ShowCreation(axes_3))
        self.play(ShowCreation(superficie3), ShowCreation(punto2), ShowCreation(dir8_y))
        self.add_fixed_in_frame_mobjects(gpo11_3)
        self.play(Write(gpo11_3))
        self.wait()
        self.play(ShowCreation(plano3), FadeOut(dir8_y))
        self.wait()
        self.play(ShowCreation(curva3), FadeOut(superficie3))
        self.wait()
        self.move_camera(phi = 90*DEGREES, theta = 90*DEGREES, gamma = 0*DEGREES, frame_center = (0,0,0), run_time = 2)
        self.wait()
        self.play(ShowCreation(tangente3))
        self.wait()
        self.play(FadeOut(gpo11_3))
        self.add_fixed_in_frame_mobjects(gpo12_3)
        self.play(Write(gpo12_3))
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])
        
        self.set_camera_orientation(phi = 0, theta = -90*DEGREES)
        self.play(Write(text13_3))
        self.wait(6)
        self.play(FadeOut(text13_3))
        self.play(Write(text14_3))
        self.wait(6)
        self.play(FadeOut(text14_3))
        self.play(Write(text15_3))
        self.wait()
        self.play(Write(text16_3))
        self.wait(6)
        self.play(FadeOut(text15_3), FadeOut(text16_3))
        self.play(Write(text17_3))
        self.wait(8)
        self.play(Write(text18_3))
        self.wait(3)
        self.play(*[FadeOut(mob)for mob in self.mobjects])
        
        self.set_camera_orientation(0.7*np.pi/2, 0.25*np.pi)
        self.play(ShowCreation(axes_2))
        self.play(ShowCreation(Paraboloide2().set_shade_in_3d(True)))
        self.add_fixed_in_frame_mobjects(gpo19_3)
        self.play(Write(gpo19_3))
        self.wait(3)
        self.add_fixed_in_frame_mobjects(text20_1_3)
        self.play(Write(text20_1_3))
        self.wait()
        self.play(FadeOut(text20_1_3))
        self.add_fixed_in_frame_mobjects(text20_2_3)
        self.play(Write(text20_2_3))
        self.wait()
        self.play(FadeOut(text20_2_3))
        self.add_fixed_in_frame_mobjects(text21_3)
        self.play(Write(text21_3))
        self.play(ShowCreation(recorrido_a))
        self.wait(5)
        self.play(FadeOut(text21_3), FadeOut(text21_3))
        self.add_fixed_in_frame_mobjects(text22_3)
        self.play(Write(text22_3))
        self.play(ShowCreation(recorrido_b))
        self.wait(5)

##############################################################################
##################### Teoremas de diferenciabilidad ##########################
##############################################################################

# Anexado el 07 de Julio de 2021.
    
class Superficie(ParametricSurface):

    def __init__(self, **kwargs):
        kwargs = {"u_min": -2,
                  "u_max": 2,
                  "v_min": -2,
                  "v_max": 2,
                  "checkerboard_colors": [GREEN]}
        ParametricSurface.__init__(self, self.func, **kwargs)
    
    # Parametrización de la superficie.
    def func(self, u, v):
        if(u == 0 and v == 0):
            return np.array([u, v, 0])
        return np.array([u, v, u**2*v/(u**4+v**2)])
    
class Cono(ParametricSurface):

    def __init__(self, **kwargs):
        kwargs = {"u_min": 0,
                  "u_max": 1,
                  "v_min": 0,
                  "v_max": 2*np.pi,
                  "checkerboard_colors": [TEAL]}
        ParametricSurface.__init__(self, self.func, **kwargs)
    
    # Parametrización del cono.
    def func(self, u, v):
        x, y = 2*u*np.cos(v), 2*u*np.sin(v)
        return np.array([x, y, 2*u])

class Teoremas_diferenciabilidad(ThreeDScene):
    
    def superficie(self, x, y):
        if(x == 0 and y == 0):
            return 0
        return x**2*y/(x**4+y**2)
    
    def trayectoria(self, t):
        return (t, t**2, self.superficie(t, t**2))
    
    def eje_x(self, t):
        return (t, 0, 0)
    
    def eje_y(self, t):
        return (0, t, 0)
    
    def construct(self):
        
        # Textos de la animación.
        title = TextMobject('''Teoremas de diferenciabilidad''').scale(1.5)
        
        text1 = TextMobject('''Veamos algunos teoremas importantes sobre diferenciabilidad.''').move_to(2*UP)
        
        text2 = TextMobject('''Teorema 1. ''', '''Si $f$ es diferenciable en $\\vec{x}_{0}$, \n
                            entonces $f$ es continua en $\\vec{x}_{0}$.''').next_to(text1, 2*DOWN)
        
        text2.set_color_by_tex('''Teorema 1. ''', color = BLUE)
        
        text3 = TextMobject('''Teorema 2. ''', '''Si $f$ es diferenciable en un punto $\\vec{x}_{0}$ en el interior\n
                            del dominio, entonces existen todas las derivadas direccionales\n
                            de $f$ en $\\vec{x}_{0}$. Particularmente existen todas las parciales''').next_to(text2, 2*DOWN)
        
        text3.set_color_by_tex('''Teorema 2. ''', color = BLUE)
        
        text4 = TextMobject('''Para mostrar que el recíproco del ''', '''Teorema 2''', ''' no es cierto,\n
                            tomemos la siguiente función.''').move_to(3*UP)
        
        text4.set_color_by_tex('''Teorema 2''', color = BLUE)
        
        func1 = TextMobject('''$f(x,y)=\\frac{x^{2}y}{x^{4}+y^{2}}$ si $(x, y)\\neq(0,0)$ y''').move_to(3*DOWN)
        func1.scale(0.8)
        
        func2 = TextMobject('''$f(x,y)=0$ si $(x, y)=(0,0)$.''').next_to(func1, DOWN)
        func2.scale(0.8)
        
        text5_1 = TextMobject('''Aplicando la definición de derivada direccional, \n
                              para cualquier $\\vec{u} = (u_{1}, u_{2})$ tal que $||\\vec{u}|| = 1$,''').move_to(3*DOWN)
        
        text5_1.scale(0.8)
        
        text5_2 = TextMobject('''$$D_{\\vec{u}}f(0, 0) = \\lim_{h\\to 0} \\frac{f(\\vec{x}_{0}+h\\vec{u})-f(\\vec{x}_{0})}{h} = \\lim_{h\\to 0} \\frac{u_{1}^{2}u_{2}}{h^{2}u_{1}^{4}+u_{2}^{2}}.$$''').move_to(3*DOWN)
        
        text5_2.scale(0.8)
        
        text6 = TextMobject('''Si $u_{2}\\neq 0$, entonces $D_{\\vec{u}}f(0,0)=\\frac{u_{1}^{2}}{u_{2}}$.''').move_to(3*DOWN)
        
        text6.scale(0.8)
        
        text7 = TextMobject('''Por otro lado, si $u_{2} = 0$, entonces $\\vec{u} = (1,0)$ y $D_{\\vec{u}}f(0,0) = 0$.''').move_to(3*DOWN)
        
        text7.scale(0.8)
        
        text8 = TextMobject('''Es decir, existen todas las derivadas direccionales de $f$ en $(0,0)$.''').move_to(3*DOWN)
        
        text8.scale(0.8)
        
        text9_1 = TextMobject('''Sin embargo, si nos acercamos a $(0,0)$ por los puntos\n
                              de la forma $(t,t^{2})$ con $t \\in\\mathbb{R}\\backslash{}\\{(0, 0)\\}$, encontraremos que''').move_to(3*DOWN)
        
        text9_1.scale(0.8)
        
        text9_2 = TextMobject('''$$\\lim_{(t, t^{2})\\to (0,0)}f(t,t^{2})=\\frac{1}{2}\\text{, por lo que } f \\text{ no es continua en }(0, 0).$$ ''').move_to(3*DOWN)
        
        text9_2.scale(0.8)
        
        text10 = TextMobject('''Como $f$ no es continua en $(0,0)$, por el ''', '''Teorema 1''', ''',\n
                              $f$ no es diferenciable en $(0, 0)$.''').move_to(3*DOWN)
        
        text10.scale(0.8)
        
        text10.set_color_by_tex('''Teorema 1''', color = BLUE)
        
        text11 = TextMobject('''Ahora consideremos un cono,\n
                              cuya regla de correspondencia es $f(x,y)=||(x,y)||$.''').move_to(3*UP)
        
        text12 = TextMobject('''Recordemos que $f$ es continua para todo $(x,y)\\in\\mathbb{R}^{2}$,\n
                              en particular para $(0,0)$.''').move_to(3*DOWN)
        
        text12.scale(0.8)
        
        text13_1 = TextMobject('''Sin embargo, para cualquier $\\vec{u}=(u_{1},u_{2})$ tal que $||\\vec{u}||=1$, 
                              $$\\lim_{h\\to 0}\\frac{f(\\vec{x}_{0}+h\\vec{u})-f(\\vec{x}_{0})}{h}=\\lim_{h\\to 0}\\frac{|h|}{h},$$''').move_to(3*DOWN)
        
        text13_1.scale(0.8)
        
        text13_2 = TextMobject('''de forma que $D_{\\vec{u}}f(0,0)$ no existe.''').move_to(3*DOWN)
        
        text13_2.scale(0.8)
        
        text14 = TextMobject('''Por el ''', '''Teorema 2''', ''', tenemos que $f$ no es diferenciable en $(0,0)$.''').move_to(3*DOWN)
        
        text14.scale(0.8)
        
        text14.set_color_by_tex('''Teorema 2''', color = BLUE)
        
        text15 = TextMobject('''Por lo tanto, el recíproco del ''', '''Teorema 1''', ''' no es válido.''').move_to(3*DOWN)
        
        text15.scale(0.8)
        
        text15.set_color_by_tex('''Teorema 1''', color = BLUE)
        
        text16 = TextMobject('''Por último, enunciemos el siguiente teorema.''').move_to(2*UP)
        
        text17 = TextMobject('''Teorema 3. ''', '''Sean $f:U\\subset\\mathbb{R}^2\\to\\mathbb{R}$ y $(x_{0},y_{0})\\in U$, con $U$ un\n
                             conjunto abierto. Si $\\frac{\\partial f}{\\partial x}$ y $\\frac{\\partial f}{\\partial y}$ existen en $U$ y son continuas\n
                             en $U$, entonces $f$ es diferenciable en $U$. Cuando las parciales\n
                             son continuas en $U$, decimos que $f$ o la superficie\n
                             dada por $f$ es suave o de clase $C^1$.''').next_to(text16, 2*DOWN)
        
        text17.set_color_by_tex('''Teorema 3. ''', color = BLUE)
        
        # Recuadros para algunos textos.
        text4.bg = SurroundingRectangle(text4, color = WHITE, fill_color = BLACK, fill_opacity = 1)
        gpo_4 = VGroup(text4.bg, text4)
        
        text11.bg = SurroundingRectangle(text11, color = WHITE, fill_color = BLACK, fill_opacity = 1)
        gpo_11 = VGroup(text11.bg, text11)
        
        # Otros objetos necesarios para la animación.
        axis_config = {"dimension": 3,
                       "x_min": -3,
                       "x_max": 3,
                       "y_min": -3,
                       "y_max": 3,
                       "z_min": -1,
                       "z_max": 2,
                       "light_source": 9*DOWN + 7*LEFT + 10*OUT}
        
        axes = ThreeDAxes(**axis_config)
        
        superficie = Superficie().set_shade_in_3d(True)
        cono = Cono().set_shade_in_3d(True)

        Dir1 = Arrow((0,0,0), (1/np.sqrt(2), 1/np.sqrt(2), 0), buff = 0.075)
        Dir2 = Arrow((0,0,0), (1/np.sqrt(2),-1/np.sqrt(2), 0), buff = 0.075)
        Dir3 = Arrow((0,0,0), (-1/np.sqrt(2), 1/np.sqrt(2), 0), buff = 0.075)
        Dir4 = Arrow((0,0,0), (-1/np.sqrt(2),-1/np.sqrt(2), 0), buff = 0.075)
        Dir5 = Arrow((0,0,0), (1,0,0), buff = 0.075)
        Dir6 = Arrow((0,0,0),(-1,0,0), buff = 0.075)
        Dir7 = Arrow((0,0,0), (0,1,0), buff = 0.075)
        Dir8 = Arrow((0,0,0),(0,-1,0), buff = 0.075)
        Dirs = VGroup(Dir1, Dir2, Dir3, Dir4, Dir5, Dir6, Dir7, Dir8)
        Dirs.set_color(RED)        

        curva = ParametricFunction(self.trayectoria, t_min = -np.sqrt(2), t_max = np.sqrt(2), color = RED)
        dashed_curva = DashedVMobject(curva)
        
        # Escena
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))
        
        self.play(Write(text1))
        self.wait(2)
        self.play(Write(text2))
        self.wait(2)
        self.play(Write(text3))
        self.wait(3)
        self.play(*[FadeOut(mob)for mob in self.mobjects])
        
        self.set_camera_orientation(np.pi/4, 0*np.pi)
        self.add_fixed_in_frame_mobjects(gpo_4)
        self.play(Write(gpo_4))
        self.play(ShowCreation(axes))
        self.play(ShowCreation(superficie))
        self.add_fixed_in_frame_mobjects(func1)
        self.play(Write(func1))
        self.add_fixed_in_frame_mobjects(func2)
        self.play(Write(func2))
        self.wait(2)
        self.play(FadeOut(func1), FadeOut(func2))
        self.add_fixed_in_frame_mobjects(text5_1)
        self.play(Write(text5_1))
        self.play(ShowCreation(Dirs))
        self.wait(3)
        self.play(FadeOut(text5_1))
        self.add_fixed_in_frame_mobjects(text5_2)
        self.play(Write(text5_2))
        self.wait(3)
        self.play(FadeOut(text5_2))
        self.play(FadeOut(Dir2), FadeOut(Dir4), FadeOut(Dir5), FadeOut(Dir6), FadeOut(Dir8))
        self.add_fixed_in_frame_mobjects(text6)
        self.play(Write(text6))
        self.wait(2)
        self.play(FadeOut(text6))
        self.play(FadeOut(Dir1), FadeOut(Dir3), FadeOut(Dir7))
        self.play(ShowCreation(Dir5))
        self.add_fixed_in_frame_mobjects(text7)
        self.play(Write(text7))
        self.wait(3)
        self.play(FadeOut(text7), FadeOut(Dir5))
        self.add_fixed_in_frame_mobjects(text8)
        self.play(Write(text8))
        self.wait(2)
        self.play(FadeOut(text8))
        self.play(ShowCreation(dashed_curva))
        self.add_fixed_in_frame_mobjects(text9_1)
        self.play(Write(text9_1))
        self.wait(3)
        self.play(FadeOut(text9_1))
        self.add_fixed_in_frame_mobjects(text9_2)
        self.play(Write(text9_2))
        self.wait(3)
        self.play(FadeOut(text9_2), FadeOut(dashed_curva))
        self.add_fixed_in_frame_mobjects(text10)
        self.play(Write(text10))
        self.wait(3)
        self.play(FadeOut(text10))
        self.play(*[FadeOut(mob)for mob in self.mobjects])
        
        self.set_camera_orientation(0.7*np.pi/2, 0.25*np.pi)
        self.add_fixed_in_frame_mobjects(gpo_11)
        self.play(Write(gpo_11))
        graf_cono = VGroup(axes, cono, Dirs)
        graf_cono.move_to(ORIGIN)
        self.play(ShowCreation(axes), ShowCreation(cono))
        self.wait(2)
        self.add_fixed_in_frame_mobjects(text12)
        self.play(Write(text12))
        self.wait(2)
        self.play(FadeOut(text12))
        self.play(ShowCreation(Dirs), FadeOut(Dir4))
        self.add_fixed_in_frame_mobjects(text13_1)
        self.play(Write(text13_1))
        self.wait(5)
        self.play(FadeOut(text13_1))
        self.add_fixed_in_frame_mobjects(text13_2)
        self.play(Write(text13_2))
        self.wait(2)
        self.play(FadeOut(text13_2))
        self.play(FadeOut(Dir1), FadeOut(Dir2), FadeOut(Dir3), FadeOut(Dir5), FadeOut(Dir6), FadeOut(Dir7) ,FadeOut(Dir8) )
        self.add_fixed_in_frame_mobjects(text14)
        self.play(Write(text14))
        self.wait(2)
        self.play(FadeOut(text14))
        self.add_fixed_in_frame_mobjects(text15)
        self.play(Write(text15))
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])
        
        self.set_camera_orientation(phi = 0, theta = -90*DEGREES)
        self.play(Write(text16))
        self.wait(2)
        self.play(Write(text17))
        self.wait(10)
        self.play(*[FadeOut(mob)for mob in self.mobjects])
