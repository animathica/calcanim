from manimlib.imports import *

#####################################################################################
#############  Límite de cocientes de funciones de dos variables ####################
#####################################################################################

#Definición de las superficies
# 1/xy
class superficie2_1_1(ParametricSurface):
    # x<0,y<0
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
    # x>0,y>0
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
    # x<0,y>0
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
    # x>0,y<0
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
# 2xy/(x^2+y^2)
class superficie2_2_1(ParametricSurface):
    # x<0,y<0
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
    # x>0,y>0
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
    # x<0,y>0
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
    # x>0,y<0
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

#Plano que se usa para limites direcc
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
        "checkerboard_colors": [BLUE_C, BLUE_D],#que coincida con el color de la curva
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
# 1/(x+y)^2 Se rota en la animación, con lo que queda como debería
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

#quinta superficie
# |x-y|/(x+y)^2
# No aparece la gráfica en el video
class superficie2_4_3(ParametricSurface):
    def __init__(self, **kwargs):
        kwargs = {
        "u_min": 0.2,
        "u_max": 3,
        "v_min": 0.2,
        "v_max": 3,
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
        text1=TextMobject('''Si estamos analizando el límite de un cociente \n
                             de dos funciones de varias variables, en caso \n
                             de que ambas tengan límite y el del denominador \n
                             sea diferente de cero, ya sabemos que el límite \n
                             del cociente es el cociente de los límites.''')
        text2=TextMobject('''¿Qué pasa en otras situaciones? \n
                             Veamos algunos ejemplos.''')
        text3=TextMobject('''Tengamos presente que en este caso hay \n
                             diversas maneras de analizar el límite: \n
                             métrica, límite direccional, límite por \n
                             trayectorias o con suscesiones.''')

        self.play(Write(titulo))
        self.wait(1)
        self.play(FadeOut(titulo))
        self.play(Write(text1),run_time=3)
        self.wait(5)
        self.play(FadeOut(text1))
        self.play(Write(text2))
        self.wait(2)
        self.play(FadeOut(text2))
        self.play(Write(text3))
        self.wait(5)
        self.play(FadeOut(text3))

    def parte1 (self):
        text5=TextMobject('''Sea $f:\\mathbb{R}^{2}-\\{(x,y)\\in \\mathbb{R}^{2}:x=0\\ \\text{ó}\\ y=0\\}\\rightarrow\\mathbb{R}$''',''' $$f(x,y)=\\frac{1}{xy}$$ ''')
        t_5_1=TextMobject('''$$f(x,y)=\\frac{1}{xy}$$''').move_to(3*UP)
        t_5_1.bg = SurroundingRectangle(t_5_1, color=WHITE, fill_color=BLACK, fill_opacity=1)
        text5_1=VGroup(t_5_1.bg,t_5_1)
        t_6=TextMobject('''Notamos que en este ejemplo el numerador es constante \n
                           y el denominador tiende a cero conforme la variable \n
                           tiende a $\\vec{0}$. ¿El límite de $f$ diverge a infinito?''' ).move_to(3*DOWN).scale(0.7)
        t_6.bg = SurroundingRectangle(t_6, color=WHITE, fill_color=BLACK, fill_opacity=1)
        text6=VGroup(t_6.bg,t_6)
        
        text6_1=TextMobject('''Si nos acercamos al origen por la dirección dada \n
                               por la recta identidad, la función diverge a $\\infty$.''').move_to(3*UP)
        text6_1.bg = SurroundingRectangle(text6_1, color=WHITE, fill_color=BLACK, fill_opacity=1)
        g2_text6_1=VGroup(text6_1.bg,text6_1)

        #objetos
        ejes = ThreeDAxes(x_min = -5, x_max = 5, y_min = -5, y_max = 5,z_min=-4,z_max=4)
        x_label = TexMobject(r"x").scale(0.75).move_to((5.5,0.3,0))
        y_label = TexMobject(r"y").scale(0.75).move_to((0.3,5.5,0))
        axes = VGroup(ejes,x_label,y_label)
        #Definimos la superficies por partes por la discontinuidad
        superficie1_1=superficie2_1_1()
        superficie1_2=superficie2_1_2()
        superficie1_3=superficie2_1_3()
        superficie1_4=superficie2_1_4()
        superficie=VGroup(superficie1_1,superficie1_2,superficie1_3,superficie1_4)

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

        self.play(Write(text5))
        self.wait(7)
        self.play(FadeOut(text5))
        self.move_camera(phi=80*DEGREES,theta=30*DEGREES,frame_center=(0,0,2))
        self.play(ShowCreation(axes))
        self.play(ShowCreation(superficie))
        self.add_fixed_in_frame_mobjects(text5_1)
        self.play(Write(text5_1))
        self.wait(2)
        self.add_fixed_in_frame_mobjects(text6)
        self.play(Write(text6))
        self.wait(5)
        self.play(FadeOut(text5_1),FadeOut(text6))

        self.add_fixed_in_frame_mobjects(g2_text6_1)
        self.play(Write(g2_text6_1))
        #Con limite direccional
        self.add(punto_convergencia2,punto_convergencia1)
        self.play(t1_2.set_value, t1_2f,t1_1.set_value,t1_1f,run_time=6)
        #self.play(t1_1.set_value, t1_1f,run_time=6)
        self.wait()
        self.play(*[FadeOut(obj) for obj in self.mobjects])
        
    def parte2 (self):
        text7=TextMobject('''Sin embargo, si nos acercamos por la recta menos \n
                                identidad, la función diverge a $-\\infty$.''')


        #objetos
        ejes = ThreeDAxes(x_min = -5, x_max = 5, y_min = -5, y_max = 5,z_min=-4,z_max=4)
        x_label = TexMobject(r"x").scale(0.75).move_to((5.5,0.3,0))
        y_label = TexMobject(r"y").scale(0.75).move_to((0.3,5.5,0))
        axes = VGroup(ejes,x_label,y_label)
        #Definimos la superficies por partes por la discontinuidad
        superficie1_1=superficie2_1_1()
        superficie1_2=superficie2_1_2()
        superficie1_3=superficie2_1_3()
        superficie1_4=superficie2_1_4()
        superficie=VGroup(superficie1_1,superficie1_2,superficie1_3,superficie1_4)

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
        self.wait(5)
        self.play(FadeOut(text7))
        #self.set_camera_orientation(0.7*np.pi/2, 0.50*np.pi,distance=12)
        self.move_camera(phi=70*DEGREES,theta=(30-45)*DEGREES,frame_center=(0,0,-1))
        self.play(ShowCreation(axes))
        self.play(ShowCreation(superficie))

        self.add(punto_convergencia2,punto_convergencia1)
        self.play(t1_2.set_value, t1_2f,t1_1.set_value,t1_1f,run_time=6)
        self.play(FadeOut(punto_convergencia2),FadeOut(punto_convergencia1))

        self.play(*[FadeOut(obj) for obj in self.mobjects])

    def partesucesiones (self):
        t_1 = TextMobject('''De acuerdo al Teorema de límite de funciones con \n
                             límites direccionales, podemos concluir que $f$ \n
                             diverge en $\\vec{0}$ pero no diverge a infinito en \n
                             ese punto.''')
        t_2 = TextMobject('''Podemos verificar lo anterior usando límite con \n
                             sucesiones''')
        t_3 = TextMobject('''Como hay dos sucesiones que convergen al origen \n
                             en el dominio, cuyas imágenes divergen a más y \n
                             menos infinito respectivamente, concluimos que \n
                             el límite en el punto $(0,0)$ no existe y no \n
                             diverge a infinito ni a menos infinito.''')
        
        ## Objetos

        ejes = ThreeDAxes(x_min = -5, x_max = 5, y_min = -5, y_max = 5,z_min=-4,z_max=4)
        x_label = TexMobject(r"x").scale(0.75).move_to((5.5,0.3,0))
        y_label = TexMobject(r"y").scale(0.75).move_to((0.3,5.5,0))
        axes = VGroup(ejes,x_label,y_label)
        #Definimos la superficies por partes por la discontinuidad
        superficie1_1=superficie2_1_1()
        superficie1_2=superficie2_1_2()
        superficie1_3=superficie2_1_3()
        superficie1_4=superficie2_1_4()
        superficie=VGroup(superficie1_1,superficie1_2,superficie1_3,superficie1_4)
        ## Movimiento para la primer convergencia en función +1/xy
        #para z>0
        #Pueden cambiarse los valores n1_2,n1_4
        #Para cambiar los limites en los cuales se muestran los límites con sucesiones
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
        Elementos1_2 = [Dot(color=RED).set_color(RED_E).move_to(i) for i in cjto1_2]
        Elementos12 = VGroup(*Elementos1_2)
        #z<0
        #Con sucesiones
        n1_4= 17+17
        cjto1_4 = []
        for i in range(2,n1_4):
            if i<=17:
                x = 3-(0.1*i)
            if i>17:
                x = 3-(0.1*17)-((i-17)*0.06)
            cjto1_4.append((x,-x,-1/(x**2)))

        Elementos1_4 = [Dot(color=RED).set_color(RED_E).move_to(i) for i in cjto1_4]
        Elementos14 = VGroup(*Elementos1_4)

        ## Para la animación de sucesiones

        self.add_fixed_in_frame_mobjects(t_1)
        self.play(Write(t_1))
        self.wait(4)
        self.play(FadeOut(t_1))
        self.add_fixed_in_frame_mobjects(t_2)
        self.play(Write(t_2))
        self.wait(2)
        self.play(FadeOut(t_2))
        self.move_camera(phi=80*DEGREES,theta=30*DEGREES,frame_center=(0,0,2))
        self.play(Write(axes,run_time=0.5))
        self.play(ShowCreation(superficie))
        # sucesion sobre recta identidad
        self.play(ShowCreation(Elementos12), run_time=6)
        self.wait()
        self.play(FadeOut(Elementos12))
        #sucesion sobre recta menos identidad
        self.move_camera(phi=80*DEGREES,theta=(30-45)*DEGREES,frame_center=(0,0,-1))
        self.play(ShowCreation(Elementos14), run_time=6)
        self.wait()
        self.play(FadeOut(Elementos14))
        self.play(*[FadeOut(obj) for obj in self.mobjects])
        self.add_fixed_in_frame_mobjects(t_3)
        self.play(Write(t_3))
        self.wait(6)
        self.play(FadeOut(t_3))

    def parte3 (self):
        text8=TextMobject('''Veamos otro ejemplo.''')
        t_9=TextMobject('''Sea $f:\\mathbb{R}^{2}-{\\vec{0}}\\rightarrow\\mathbb{R}$ \n
                                $f(x,y)=\\frac{2xy}{x^2+y^2}$''').move_to(3*DOWN)
        t_9.bg = SurroundingRectangle(t_9, color=WHITE, fill_color=BLACK, fill_opacity=1)
        text9 = VGroup(t_9.bg,t_9)
        t9_5 = TextMobject('''En este ejemplo tanto la función del numerador como \n
                              la del denominador convergen a cero en el origen. ¿Qué \n
                              pasa con el cociente?''').scale(0.7).move_to(3*DOWN)
        t9_5.bg = SurroundingRectangle(t9_5,color=WHITE,fill_color=BLACK,fill_opacity=1)
        text9_5 = VGroup(t9_5.bg,t9_5)
        t_10=TextMobject('''Notemos que si nos aproximamos al origen en el \n
                                dominio en las direcciones canónicas entonces \n
                                el límite es 0.''').move_to(3*DOWN).scale(0.7)
        t_10.bg = SurroundingRectangle(t_10, color=WHITE, fill_color=BLACK, fill_opacity=1)
        text10 = VGroup(t_10.bg,t_10)
        t_11=TextMobject('''Ahora tomemos la dirección dada por la recta \n
                                identidad y veamos qué ocurre.''').move_to(3*DOWN)
        t_11.bg = SurroundingRectangle(t_11, color=WHITE, fill_color=BLACK, fill_opacity=1)
        text11 = VGroup(t_11.bg,t_11)
        t_12 = TextMobject('''Notamos que en este caso el límite es 1 y es diferente \n
                                    de 0.''').move_to(3*DOWN)
        t_12.bg = SurroundingRectangle(t_12, color=WHITE, fill_color=BLACK, fill_opacity=1)
        text12 = VGroup(t_12.bg,t_12)
        text13 = TextMobject('''Como ya sabemos, si encontramos dos direcciones donde los \n
                                límites direccionales difieren, entonces podemos concluir \n
                                que el límite no existe.''')

        #Objetos
        ejes = ThreeDAxes(x_min = -4.5, x_max = 4.5, y_min = -4.5, y_max = 4.5,z_min=-1.5,z_max=4)
        x_label = TexMobject(r"x").scale(0.75).move_to((5,0.3,0))
        y_label = TexMobject(r"y").scale(0.75).move_to((0.3,5,0))
        axes = VGroup(ejes,x_label,y_label)
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
            x=3-i*(0.2)
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
        self.wait(2)
        self.play(FadeOut(text8))
        self.set_camera_orientation(0.7*np.pi/2,(-1.4)*np.pi-90*DEGREES,distance=12)
        self.play(ShowCreation(axes))
        self.play(ShowCreation(superficie))
        self.add_fixed_in_frame_mobjects(text9)
        self.play(Write(text9))
        self.wait(5)
        self.play(FadeOut(text9))
        self.add_fixed_in_frame_mobjects(text9_5)
        self.play(Write(text9_5))
        self.wait(4)
        self.play(FadeOut(text9_5))
        self.add_fixed_in_frame_mobjects(text10)
        self.play(Write(text10))
        self.wait(5)
        self.play(ShowCreation(Elementos1),runtime=10)
        self.wait()
        self.play(FadeOut(text10),FadeOut(Elementos1))
        self.add_fixed_in_frame_mobjects(text11)
        self.play(Write(text11))
        self.wait(2)
        self.play(ShowCreation(Elementos2),runtime=10)
        self.play(FadeOut(text11))
        self.add_fixed_in_frame_mobjects(text12)
        self.play(Write(text12))
        self.wait(3)
        self.play(FadeOut(text12),FadeOut(axes),FadeOut(superficie),FadeOut(Elementos2))
        self.add_fixed_in_frame_mobjects(text13)
        self.play(Write(text13))
        self.wait(4)
        self.play(FadeOut(text13))

    def parte4 (self):
        t_19=TextMobject('''Consideremos $f:\\mathbb{R}^{2}-{\\vec{0}}\\rightarrow\\mathbb{R}$\n
                            $f(x,y)=\\frac{1}{(x+y)^{2}}$''').move_to(3*DOWN)
        t_19.bg = SurroundingRectangle(t_19, color=WHITE, fill_color=BLACK, fill_opacity=1)
        text19 = VGroup(t_19.bg,t_19)
        t_20=TextMobject('''Nuevamente tenemos una función donde el numerador es \n
                            constante y el denominador tiende a cero en el origen.''').move_to(3*DOWN)
        t_20.bg = SurroundingRectangle(t_20, color=WHITE, fill_color=BLACK, fill_opacity=1)
        text20 = VGroup(t_20.bg,t_20)
        t21 = TextMobject('''Sin embargo, cuando nos vamos acercando a $\\vec{0}$, esta \n
                             función tiene un comportamiento diferente al del primer \n
                             ejemplo.''').move_to(3*DOWN).scale(0.8)
        t21.bg = SurroundingRectangle(t21, color=WHITE, fill_color=BLACK, fill_opacity=1)
        text21 = VGroup(t21.bg,t21)
        t22 = TextMobject('''En este caso $f$ diverge a $\\infty$, lo cual se puede \n
                             demostrar sin mucha dificultad porque el numerador \n
                             es una constante y el denominador tiende a cero con \n
                             valores positivos.''').move_to(3*DOWN).scale(0.8)
        t22.bg = SurroundingRectangle(t22, color=WHITE, fill_color=BLACK, fill_opacity=1)
        text22 = VGroup(t22.bg,t22)
        text23 = TextMobject('''De hecho, usando la métrica se puede demostrar \n
                                fácilmente que si en un cociente el numerador es \n
                                constante, el denominador tiende a cero en un \n
                                punto y además es positivo, entonces el cociente \n
                                diverge a infinito en el punto.''')

        ejes = ThreeDAxes(x_min = -4.5, x_max = 4.5, y_min = -4.5, y_max = 4.5,z_min=-1.5,z_max=4)
        x_label = TexMobject(r"x").scale(0.75).move_to((5,0.3,0))
        y_label = TexMobject(r"y").scale(0.75).move_to((0.3,5,0))
        axes = VGroup(ejes,x_label,y_label)
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
        self.set_camera_orientation(0.7*np.pi/2, 0.65*np.pi-180*DEGREES,distance=12)
        self.play(ShowCreation(axes))
        self.add_fixed_in_frame_mobjects(text19)
        self.play(Write(text19))
        self.wait(4)
        self.play(ShowCreation(superficie))
        self.wait()
        self.play(FadeOut(text19))
        self.add_fixed_in_frame_mobjects(text20)
        self.play(Write(text20))
        self.wait(4)
        self.play(FadeOut(text20))
        self.add_fixed_in_frame_mobjects(text21)
        self.play(Write(text21),run_time=2)
        self.wait(2)
        self.play(ShowCreation(punto2))
        self.play(t1_1.set_value, t1_1f,run_time=10)
        self.play(FadeOut(text21),FadeOut(punto2))
        self.add_fixed_in_frame_mobjects(text22)
        self.play(Write(text22))
        self.wait(5)
        self.play(*[FadeOut(obj) for obj in self.mobjects])
        self.add_fixed_in_frame_mobjects(text23)
        self.play(Write(text23))
        self.wait(8)
        self.play(FadeOut(text23))

    def parte5(self):
        text1 = TextMobject('''También podemos usar criterios de comparación \n
                               analizando los órdenes de magnitud de las funciones \n
                               en el cociente''')
        text2 = TextMobject('''La función \n
                               $f(x,y)=\\dfrac{x^2+y^2}{\\sin^2(x^2+y^2)}$ \n
                               tiende a infinito en el origen.''').move_to(2*UP)
        text3 = TextMobject('''Pues al considerar $r^2=x^2+y^2$, cerca del origen \n
                               obtenemos''').next_to(text2,DOWN)
        text4 = TexMobject(r"\dfrac{r^2}{\sin^2(r^2)}\approx\dfrac{r^2}{r^4}=\dfrac{1}{r^2}").next_to(text3,DOWN)

        self.add_fixed_in_frame_mobjects(text1)
        self.play(Write(text1))
        self.wait(3)
        self.play(FadeOut(text1))
        self.add_fixed_in_frame_mobjects(text2)
        self.play(Write(text2))
        self.wait(2)
        self.add_fixed_in_frame_mobjects(text3)
        self.play(Write(text3))
        self.wait(2)
        self.add_fixed_in_frame_mobjects(text4)
        self.play(Write(text4))
        self.wait(3)
        self.play(*[FadeOut(obj) for obj in self.mobjects])

    def construct (self):
        ### ANIMACIÓN PARA LAS DIFERENTES PARTES ###
        self.parte0()
        self.parte1()
        self.parte2()
        self.partesucesiones()
        self.parte3()
        self.parte4()
        self.parte5()