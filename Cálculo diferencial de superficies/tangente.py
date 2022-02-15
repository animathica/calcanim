from manimlib.imports import *

##############################################################################
############### Plano tangente y derivadas direccionales #####################
##############################################################################

# Corregido el 15-02-2022


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
    
    def parte1(self):
        
        # Textos de la primera sección
        text1 = TextMobject('''Consideremos estas dos superficies.''').move_to(3*UP)
        
        text2 = TextMobject('''Notemos que una es ``suave'' en el origen, \n
                            mientras que la otra tiene un ``pico''.''').move_to(3*UP)
        
        text3 = TextMobject('''¿Qué significa esto matemáticamente hablando?''').move_to(3*UP)
        
        text4_1 = TextMobject('''Definición 1.''', ''' Sean $f:U\\subset\\mathbb{R}^{2}\\to\\mathbb{R}$ y $(x_{0},y_{0}) \\in U \\cap U'$, f es\n
                              diferenciable en $(x_{0},y_{0})$ si y solo si existe $(m_{1},m_{2})\\in\\mathbb{R}^{2}$ tal que''').move_to(UP)
        
        text4_1.set_color_by_tex('''Definición 1.''', color = TEAL)
        
        text4_1.scale(0.9)
        
        text4_2 = TextMobject('''$$\\lim_{(h_{1},h_{2})\\to(0,0)}\\dfrac{f((x_{0},y_{0})+(h_{1},h_{2}))-(f(x_{0},y_{0})+(m_{1},m_{2})\\cdot(h_{1},h_{2}))}{||(h_{1},h_{2})||}=0.$$''').next_to(text4_1, 2*DOWN)
        
        text4_2.scale(0.8)
        
        text5_1 = TextMobject('''Haciendo el cambio de variables $h_{1}=x-x_{0}$ y $h_{2}=y-y_{0}$,''').move_to(3*UP)
               
        text5_2 = TextMobject('''$$\\lim_{(x,y)\\to(x_{0},y_{0})}\\dfrac{f((x_{0},y_{0})+(x-x_{0},y-y_{0}))-(f(x_{0},y_{0})+(m_{1},m_{2})\\cdot(x-x_{0},y-y_{0}))}{||(x-x_{0},y-y_{0})||}=0.$$''').next_to(text5_1, 2*DOWN)
    
        text5_2.scale(0.7)
    
        text6_1 = TextMobject('''Desarrollando la expresión anterior,''').next_to(text5_2, 2*DOWN)
    
        text6_2 = TextMobject('''$$\\lim_{(x,y)\\to(x_{0},y_{0})}\\dfrac{f(x,y)-(f(x_{0},y_{0})+m_{1}(x-x_{0})+m_{2}(y-y_{0}))}{||(x-x_{0},y-y_{0})||}=0.$$''').next_to(text6_1, 2*DOWN)
    
        text6_2.scale(0.7)
    
        text7 = TextMobject('''Intuitivamente, $(m_{1},m_{2})$ nos da la inclinación del plano\n
                              que más se parece a la función en $(x_{0}, y_{0})$.''').next_to(text6_2, 3*DOWN)
        
        text8 = TextMobject('''Primero observemos que la gráfica de $m_{1}x+m_{2}y$\n
                              nos da un plano que contiene al origen.''').move_to(3*DOWN)
        
        func_text = TextMobject('''$f(x,y)=\\frac{x^{2}+y^{2}}{2}$''')
        
        func_text.scale(0.7)
        
        func_text.move_to(5*RIGHT+2*UP)
        
        punto_text = TextMobject('''$(x_{0},y_{0})=(\\sqrt{2},\\sqrt{2})$''')
        
        punto_text.scale(0.7)
        
        punto_text.next_to(func_text, DOWN)
        
        text9 = TextMobject('''Si a dicho plano lo trasladamos a $(x_{0},y_{0},f(x_{0},y_{0}))$, obtendremos\n
                              el plano tangente a la superficie en ese mismo punto.''').move_to(3*DOWN)
                              
        text9.scale(0.9)
        
        text10 = TextMobject('''Definición 2.''', ''' Sea $f:U\\subset\\mathbb{R}^{2}\\to\\mathbb{R}$ diferenciable en \n
                               $(x_{0},y_{0})\\in U \\cap U'$, decimos que el plano que tiene como\n
                               ecuación $f(x_{0},y_{0})+m_{1}(x-x_{0})+m_{2}(y-y_{0})$ es el plano\n
                               tangente a la gráfica de $f$ en el punto $(x_{0},y_{0},f(x_{0},y_{0}))$,\n
                               donde $(m_{1},m_{2})$ es el vector que cumple la ''', '''Definición 1.''')
                    
        text10.set_color_by_tex('''Definición 2.''', color = TEAL)
        text10.set_color_by_tex('''Definición 1.''', color = TEAL)
        
        text11 = TextMobject('''De manera general, para $f:U\\subset\\mathbb{R}^n\\to\\mathbb{R}$, $f$ es diferenciable\n
                               en $\\vec{x}_{0}\\in U\\cap U'$ si y solo si existe $\\vec{m}\\in\\mathbb{R}^n$ tal que
                               $$\\lim_{\\vec{h}\\to\\vec{0}}\\dfrac{f\\left(\\vec{x}_0+\\vec{h}\\right)-\\left(f(\\vec{x}_0)+\\vec{m}\\cdot\\vec{h}\\right)}{||\\vec{h}||}=0.$$''')
        
        text12 = TextMobject('''Por lo tanto, podemos decir que $f$ es diferenciable en $\\vec{x}_{0}$ si y\n
                               solo si el plano tangente a la función en $(\\vec{x}_{0},f(\\vec{x}_{0}))$ es una\n
                               buena aproximación para la función alrededor de ese punto.''').move_to(UP)
                               
        text13 = TextMobject('''Pero, ''', '''¿cómo podemos encontrar al vector $\\vec{m}$?''').next_to(text12, 3*DOWN)
        
        text13.set_color_by_tex('''¿cómo podemos encontrar al vector $\\vec{m}$?''', color = TEAL)
        
        # Recuadros para algunos textos
        text1.bg = SurroundingRectangle(text1, color = WHITE, fill_color = BLACK, fill_opacity = 1)
        gpo1 = VGroup(text1.bg, text1)
        
        text2.bg = SurroundingRectangle(text2, color = WHITE, fill_color = BLACK, fill_opacity = 1)
        gpo2 = VGroup(text2.bg, text2)
        
        text3.bg = SurroundingRectangle(text3, color = WHITE, fill_color = BLACK, fill_opacity = 1)
        gpo3 = VGroup(text3.bg, text3)
        
        text8.bg = SurroundingRectangle(text8, color = WHITE, fill_color = BLACK, fill_opacity = 1)
        gpo8 = VGroup(text8.bg, text8)
        
        text9.bg = SurroundingRectangle(text9, color = WHITE, fill_color = BLACK, fill_opacity = 1)
        gpo9 = VGroup(text9.bg, text9)
        
        # Ejes utilizados en la animación
        axis_config = {"dimension": 3,
                        "x_min": -3,
                        "x_max": 3,
                        "y_min": -3,
                        "y_max": 3,
                        "z_min": -1,
                        "z_max": 2,
                        "light_source": 9*DOWN + 7*LEFT + 10*OUT}
        
        axes = ThreeDAxes(**axis_config)
        axes_c = ThreeDAxes(**axis_config)
        axes_p = ThreeDAxes(**axis_config)
        
        # Superficies utilizadas en la animación
        cono = Cono().set_shade_in_3d(True)
        graf_cono = VGroup(axes_c, cono)
        graf_cono.move_to(2*RIGHT+2*DOWN)
        
        paraboloide1 = Paraboloide1().set_shade_in_3d(True)
        graf_parab = VGroup(axes_p, paraboloide1)
        graf_parab.move_to(2*LEFT+2*UP)
        
        plano1 = Plano1().set_shade_in_3d(True)
        
         # Plano tangente y derivabilidad
        self.set_camera_orientation(0.7*np.pi/2, 0.25*np.pi)
        self.add_fixed_in_frame_mobjects(gpo1)
        self.play(Write(gpo1))
        self.play(ShowCreation(graf_cono))
        self.play(ShowCreation(graf_parab))
        self.wait()
        self.play(FadeOut(gpo1))
        self.add_fixed_in_frame_mobjects(gpo2)
        self.play(Write(gpo2))
        self.wait(2)
        self.play(FadeOut(gpo2))
        self.add_fixed_in_frame_mobjects(gpo3)
        self.play(Write(gpo3))
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        self.set_camera_orientation(phi = 0, theta = -90*DEGREES)
        self.play(Write(text4_1))
        self.wait(8)
        self.play(Write(text4_2))
        self.wait(8)
        self.play(FadeOut(text4_1), FadeOut(text4_2))
        self.play(Write(text5_1))
        self.wait(2)
        self.play(Write(text5_2), run_time = 3)
        self.wait(5)
        self.play(Write(text6_1))
        self.wait(2)
        self.play(Write(text6_2), run_time = 3)
        self.wait(5)
        self.play(Write(text7), run_time = 3)
        self.wait(5)
        self.play(*[FadeOut(mob)for mob in self.mobjects])
        
        self.set_camera_orientation(0.7*np.pi/2, 0.25*np.pi)
        self.add_fixed_in_frame_mobjects(gpo8)
        self.play(Write(gpo8))
        self.play(ShowCreation(axes))
        self.add_fixed_in_frame_mobjects(func_text, punto_text)
        self.play(Write(func_text), Write(punto_text))
        self.play(ShowCreation(Paraboloide1().set_shade_in_3d(True)))
        self.play(ShowCreation(plano1))
        self.wait()
        self.play(FadeOut(gpo8))
        self.add_fixed_in_frame_mobjects(gpo9)
        self.play(Write(gpo9), run_time = 3)
        self.play(ApplyMethod(plano1.move_to, [np.sqrt(2), np.sqrt(2), 2]))
        self.wait()
        self.move_camera(85*DEGREES, -40*DEGREES, frame_center = (0,0,0), run_time = 2)
        self.wait()
        self.play(*[FadeOut(mob)for mob in self.mobjects])
        
        self.set_camera_orientation(phi = 0, theta = -90*DEGREES)
        self.play(Write(text10), run_time = 5)
        self.wait(10)
        self.play(FadeOut(text10))
        self.play(Write(text11), run_time = 3)
        self.wait(10)
        self.play(FadeOut(text11))
        self.play(Write(text12), run_time = 3)
        self.wait(10)
        self.play(Write(text13))
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])
    
    def parte2(self):
          
        # Textos de la segunda sección
        subtitle1 = TextMobject('''Derivadas direccionales''').scale(1.5)

        text1 = TextMobject('''Consideremos $f:U\\subset\\mathbb{R}^{2}\\to\\mathbb{R}$ y tomemos\n
                              $\\vec{x}_{0}\\in U$ y $\\vec{u}\\in\\mathbb{R}^{n}$ tal que $||\\vec{u}||=1$.''').move_to(3*UP) 
                            
        text2 = TextMobject('''La función $f$ es derivable en el punto $\\vec{x}_{0}$ en la dirección
                            $$\\text{del vector }\\vec{u}\\text{ si }\\lim_{h\\to 0}\\frac{f(\\vec{x}_{0}+h\\vec{u})-f(\\vec{x}_{0})}{h}\\text{ existe.}$$''')
                            
        text3 = TextMobject('''Al valor de dicho límite se le denota por ''', '''$D_{\\vec{u}}f(\\vec{x_{0}})$.''').move_to(2*DOWN)
        
        text3.set_color_by_tex('''$D_{\\vec{u}}f(\\vec{x_{0}})$.''', color = TEAL)
        
        text4 = TextMobject('''¿Qué similitudes y diferencias encuentras\n
                              entre la definición anterior y la definición\n
                              de derivabilidad para funciones de $\\mathbb{R}$ en $\\mathbb{R}$?''').move_to(2.8*UP)
        
        text5 = TextMobject('''En general, $D_{\\vec{u}}f(\\vec{x_{0}})$ es una medida de la\n
                            razón de cambio instantánea de la función $f$,\n
                            partiendo del vector $\\vec{x}_{0}$ y en la dirección de $\\vec{u}$.''')
        
        text6 = TextMobject('''La derivada direccional tiene una\n
                              interpretación geométrica útil.''').move_to(2.3*DOWN)
        
        text7 = TextMobject('''La siguiente función $f$ es derivable en\n
                              el punto $(0,2)$ en la dirección $\\left(-\\frac{1}{\\sqrt{2}},\\frac{1}{\\sqrt{2}}\\right)$.''').move_to(3*UP)
        
        func_text2 = TextMobject('''$f(x,y)=-\\frac{x^2 + y^2}{3}+2$''').move_to(3*DOWN-3.5*RIGHT)
                            
        text8 = TextMobject('''Al intersecar la gráfica de $f$ con el plano perpendicular a $XY$ que contiene\n
                            a la recta $\\vec{x}_{0}+h\\vec{u}=(0,2)+h\\left(-\\frac{1}{\\sqrt{2}},\\frac{1}{\\sqrt{2}}\\right)$, $h\\in\\mathbb{R}$, se obtiene una curva.''').move_to(3*UP)
        
        text8.scale(0.8)

        text9 = TextMobject('''$D_{\\vec{u}}f(0,2) = -\\frac{2\\sqrt{2}}{3}$ es la pendiente de la recta \n 
                                tangente a la curva en el punto $\\left(0,2,\\frac{2}{3}\\right)$.''').move_to(3*UP) 
        
        text10 = TextMobject('''Es decir, la derivada direccional coincide con la pendiente\n
                              de la recta tangente en el corte correspondiente.''').move_to(3*UP)
                             
        text11 = TextMobject('''Muchas de las propiedades que cumplen las\n
                              derivadas de funciones de $\\mathbb{R}$ en $\\mathbb{R}$, las conservan\n 
                              de cierta forma las derivadas direccionales, como\n
                              las relacionadas con la aritmética de funciones.''')
                             
        text12 = TextMobject('''Por ejemplo, si tenemos dos funciones tales que\n
                                $D_{\\vec{u}}f(\\vec{x_{0}})$ y $D_{\\vec{u}}g(\\vec{x_{0}})$ existe, entonces $D_{\\vec{u}}(fg)(\\vec{x_{0}})$ existe y además''',
                                '''$$D_{\\vec{u}}(fg)(\\vec{x_{0}}) = f(\\vec{x}_{0})D_{\\vec{u}}g(\\vec{x_{0}}) + g(\\vec{x}_{0})D_{\\vec{u}}f(\\vec{x_{0}}).$$''')
        
        text12.set_color_by_tex('''$$D_{\\vec{u}}(fg)(\\vec{x_{0}}) = f(\\vec{x}_{0})D_{\\vec{u}}g(\\vec{x_{0}}) + g(\\vec{x}_{0})D_{\\vec{u}}f(\\vec{x_{0}}).$$''', color = TEAL)
        
        text13 = TextMobject('''Para ver lo anterior, consideremos los mismos $f$, $\\vec{u}$ y $\\vec{x}_{0}$,\n
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
                
        # Recuadros para algunos textos
        text7.bg = SurroundingRectangle(text7, color = WHITE, fill_color = BLACK, fill_opacity = 1)
        gpo7 = VGroup(text7.bg, text7)
        
        text8.bg = SurroundingRectangle(text8, color = WHITE, fill_color = BLACK, fill_opacity = 1)
        gpo8 = VGroup(text8.bg, text8)
        
        text9.bg = SurroundingRectangle(text9, color = WHITE, fill_color = BLACK, fill_opacity = 1)
        gpo9 = VGroup(text9.bg, text9)
        
        text10.bg = SurroundingRectangle(text10, color = WHITE, fill_color = BLACK, fill_opacity = 1)
        gpo10 = VGroup(text10.bg, text10)
        
        text13.bg = SurroundingRectangle(text13, color = WHITE, fill_color = BLACK, fill_opacity = 1)
        gpo13 = VGroup(text13.bg, text13)
        
        # Ejes utilizados en la animación
        axis_config = {"dimension": 3,
                        "x_min": -4,
                        "x_max": 4,
                        "y_min": -4,
                        "y_max": 4,
                        "z_min": -1,
                        "z_max": 3,
                        "light_source": 9*DOWN + 7*LEFT + 10*OUT}
        
        axes = ThreeDAxes(**axis_config)
        axes_f = ThreeDAxes(**axis_config)
        axes_g = ThreeDAxes(**axis_config)
        
        # Superficies utilizadas en la animación
        plano2 = Plano2().set_shade_in_3d(True)
        paraboloide2 = Paraboloide2().set_shade_in_3d(True)
        superficie1 = Superficie1().set_shade_in_3d(True)
        superficie2 = Superficie2().set_shade_in_3d(True)
        
        # Otros objetos necesarios para la animación
        x_0, y_0 = 0, 2
        z_0 = self.paraboloide2(x_0, y_0)
        
        punto1 = Dot(color = YELLOW).move_to([x_0, y_0, 0]).set_shade_in_3d(True)
        direc = Vector(direction = [-1/np.sqrt(2), 1/np.sqrt(2), 0], buff = 0.075).set_color(YELLOW)
        
        curva1 = ParametricFunction(self.curva1, t_min = 1-np.sqrt(7)/np.sqrt(2), t_max = 1+np.sqrt(7)/np.sqrt(2), color = BLUE)
        curva2 = ParametricFunction(self.curva2, t_min = -0.802328, t_max = 2.6980, color = ORANGE)
        
        tangente1 = ParametricFunction(self.tangente1, t_min = -np.sqrt(2), t_max = 5/(4*np.sqrt(2)), color = PURPLE)
        tangente2 = ParametricFunction(self.tangente2, t_min = -np.sqrt(2), t_max = 1/np.sqrt(2), color = PURPLE)
        
        # Derivadas direccionales
        self.play(Write(subtitle1))
        self.wait()
        self.play(FadeOut(subtitle1))

        self.play(Write(text1))
        self.wait(3)
        self.play(Write(text2), run_time = 3)
        self.wait(5)
        self.play(Write(text3))
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])
        self.play(Write(text4), run_time = 3)
        self.wait(5)
        self.play(Write(text5), run_time = 3)
        self.wait(5)
        self.play(Write(text6))
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        self.set_camera_orientation(0.7*np.pi/2, 0.25*np.pi)
        self.add_fixed_in_frame_mobjects(gpo7, func_text2)
        self.play(Write(gpo7), Write(func_text2), run_time = 3)
        self.play(ShowCreation(axes))
        self.play(ShowCreation(punto1), ShowCreation(direc))
        self.wait()
        self.play(ApplyMethod(punto1.move_to, [x_0, y_0, self.paraboloide2(x_0, y_0)]))
        self.play(ApplyMethod(direc.move_to, [x_0-1/(2*np.sqrt(2)), y_0+1/(2*np.sqrt(2)), self.paraboloide2(x_0, y_0)]))
        self.play(ShowCreation(paraboloide2))
        self.wait()
        self.play(FadeOut(gpo7))
        self.add_fixed_in_frame_mobjects(gpo8)
        self.play(Write(gpo8), run_time = 3)
        self.wait()
        self.play(FadeOut(direc), ShowCreation(plano2))
        self.play(ShowCreation(curva1), FadeOut(paraboloide2))
        self.move_camera(90*DEGREES, 45*DEGREES, frame_center = (0,0,0), run_time = 3)
        self.wait()
        self.play(FadeOut(gpo8))
        self.add_fixed_in_frame_mobjects(gpo9)
        self.play(Write(gpo9))
        self.play(ShowCreation(tangente1))
        self.wait(2)
        self.play(FadeOut(gpo9))
        self.add_fixed_in_frame_mobjects(gpo10)
        self.play(Write(gpo10), run_time = 3)
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])
        
        self.set_camera_orientation(phi = 0, theta = -90*DEGREES)
        self.play(Write(text11), run_time = 4)
        self.wait(10)
        self.play(FadeOut(text11))
        self.play(Write(text12), run_time = 3)
        self.wait(10)
        self.play(*[FadeOut(mob)for mob in self.mobjects])
        
        self.set_camera_orientation(0.7*np.pi/2, 0.25*np.pi)
        self.add_fixed_in_frame_mobjects(gpo13)
        self.play(Write(gpo13))
        self.wait(3)
        graf_f = VGroup(axes_f, paraboloide2)
        graf_f.move_to(2.5*RIGHT+2*DOWN)
        graf_f.scale(0.8)
        graf_g = VGroup(axes_g, superficie1)
        graf_g.move_to(1.5*LEFT+3*UP)
        graf_g.scale(0.8)
        self.play(ShowCreation(graf_f), ShowCreation(graf_g))
        self.wait(2)
        self.play(FadeOut(graf_f), FadeOut(graf_g))
        self.play(ShowCreation(axes), ShowCreation(superficie2))
        self.wait()
        self.play(ShowCreation(plano2))
        self.play(ShowCreation(curva2), FadeOut(superficie2))
        self.move_camera(90*DEGREES, 45*DEGREES, frame_center = (0,0,0), run_time = 3)
        self.add_fixed_in_frame_mobjects(f_text, g_text)
        self.play(Write(f_text), Write(g_text))
        self.wait(3)
        self.add_fixed_in_frame_mobjects(df_text, dg_text)
        self.play(Write(df_text), Write(dg_text))
        self.wait(3)
        self.add_fixed_in_frame_mobjects(dfg_text)
        self.play(Write(dfg_text))
        self.wait(3)
        self.play(ShowCreation(tangente2))
        self.wait()
        self.play(*[FadeOut(mob)for mob in self.mobjects])    
    
    def parte3(self):

        # Textos de la última sección
        subtitle2 = TextMobject('''Derivadas parciales''').scale(1.5)

        text1 = TextMobject('''Sea $f:U\\subset\\mathbb{R}^2\\to\\mathbb{R}$, fijémonos en un punto\n
                              $\\vec{x}_0\\in U$ y el respectivo valor para $f(\\vec{x}_0)$.''').move_to(3*UP)
        
        func_text3 = TextMobject('''$f(x)=\\frac{x^2-y^2}{4}$''').move_to(2.5*DOWN-3.2*RIGHT)

        text2 = TextMobject('''Podemos obtener las derivadas direccionales de\n
                              $f$ en $\\vec{x}_0$ en una multitud de direcciones.''').move_to(3*UP)
        
        text3 = TextMobject('''Particularmente nos podemos fijar en aquellas en las que se\n
                              utiliza una dirección canónica dada por $\\vec{e}_1$ o por $\\vec{e}_2$.''').move_to(3*UP)
        
        text4 = TextMobject('''Tomemos la derivada en la dirección $\\vec{e}_1$.''').move_to(3*UP)
                              
        text5_1 = TextMobject('''A esta la podemos ver de la forma''').move_to(2*UP)
        
        text5_2 = TextMobject('''$$D_{\\vec{e}_1}f(\\vec{x}_0)=\\lim_{h\\to 0}\\dfrac{f(\\vec{x}_0+h \\ \\ \\vec{e}_1 \\ \\ )-f(\\vec{x_0})}{h}.$$''').next_to(text5_1, 2*DOWN)
        
        text6_1 = TextMobject('''Recordando que $\\vec{e}_1=(1,0)$,''').move_to(2*UP)
        
        text6_2 = TextMobject('''$$D_{\\vec{e}_1}f(\\vec{x}_0)=\\lim_{h\\to 0}\\dfrac{f(\\vec{x}_0+h(1,0))-f(\\vec{x_0})}{h}.$$''').next_to(text6_1, 2*DOWN)
        
        text6_3 = TextMobject('''$$D_{\\vec{e}_1}f(\\vec{x}_0)=\\lim_{h\\to 0}\\dfrac{f(\\vec{x}_0+(h,0))-f(\\vec{x_0})}{h}.$$''').next_to(text6_1, 2*DOWN)
        
        text7 = TextMobject('''A este caso particular de la derivada direccional se le\n
                                conoce como derivada parcial de $f$ con respecto a $x$.''').next_to(text6_3, 3*DOWN)
        
        text8 = TextMobject('''Se representa de la forma''',
                              '''$$\\dfrac{\\partial f}{\\partial x}(\\vec{x}_0)=\\lim_{h\\to0}\\dfrac{f(\\vec{x}_0+h\\vec{e}_1)-f(\\vec{x}_0)}{h}.$$''').move_to(2*UP)
        
        text8.set_color_by_tex('''$$\\dfrac{\\partial f}{\\partial x}(\\vec{x}_0)''', color = TEAL)
        
        text9 = TextMobject('''Análogamente, tenemos''',
                              '''$$\\dfrac{\\partial f}{\\partial y}(\\vec{x}_0)=\\lim_{h\\to0}\\dfrac{f(\\vec{x}_0+h\\vec{e}_2)-f(\\vec{x}_0)}{h}.$$''').next_to(text8, 2*DOWN)

        text9.set_color_by_tex('''$$\\dfrac{\\partial f}{\\partial y}(\\vec{x}_0)''', color = TEAL)
                                      
        text10 = TextMobject('''En general, si $f:U\\subset\\mathbb{R}^n\\to\\mathbb{R}$, $\\vec{x}_0\\in U$, para cada\n
                              $$i\\in\\{1,...,n\\}\\text{ se tiene }\\dfrac{\\partial f}{\\partial x_i}(\\vec{x}_0)=\\lim_{h\\to0}\\dfrac{f(\\vec{x}_0+h\\vec{e}_i)-f(\\vec{x}_0)}{h}.$$''')
            
        text11 = TextMobject('''$\\frac{\\partial f}{\\partial x_i}(\\vec{x}_{0})$ es la pendiente de la recta tangente\n
                                a $f$ en $\\vec{x}_0$ en la $i-$ésima dirección canónica.''').move_to(3*UP)
                                
        text12 = TextMobject('''De esta forma se puede ver a $\\frac{\\partial f}{\\partial x_i}$ como la derivada\n
                                de $f$ en el $i-$ésimo corte canónico.''').move_to(3*UP)
        
        text13 = TextMobject('''Al vector $\\left(\\frac{\\partial f}{\\partial x_1}(\\vec{x}_0),...,\\frac{\\partial f}{\\partial x_n}(\\vec{x}_0)\\right)$ se le llama\n
                                gradiente de $f$ en $\\vec{x}_0$, representado como $\\nabla f(x_0)$,\n
                                y es la mejor aproximación lineal a $f$ en el punto $\\vec{x}_{0}$.''')
        
        text14 = TextMobject('''Por lo tanto, si una función $f$ es diferenciable en $\\vec{x}_{0}$,\n
                                ¡el vector $\\vec{m}$ que buscamos y que cumple la ''', '''Definición 1''', '''\n
                                es ''', '''$\\vec{m}=\\nabla f(\\vec{x}_{0})$''','''$=\\left(\\frac{\\partial f}{\\partial x_1}(\\vec{x}_{0}),...,\\frac{\\partial f}{\\partial x_n}(\\vec{x}_{0})\\right)$!''')
        
        text14.set_color_by_tex('''Definición 1''', color = TEAL)
        text14.set_color_by_tex('''$\\vec{m}=\\nabla f(\\vec{x}_{0})$''', color = TEAL)
        
        text15 = TextMobject('''Adicionalmente, el gradiente tiene\n
                                un par de usos importantes.''').move_to(UP)
 	
        text16 = TextMobject('''En primer lugar, si $f$ es diferenciable, el\n
                                gradiente nos permite expresar sus derivadas\n
                                direccionales como $D_{\\vec{u}}f(\\vec{x_{0}})=\\nabla f(\\vec{x}_0)\\cdot\\vec{u}$.''').next_to(text15, 3*DOWN)
        
        text17 = TextMobject('''En segundo lugar, el gradiente apunta en la\n
                                dirección y sentido de máximo crecimiento de la superficie,\n
                                como consecuencia de que $D_{\\vec{u}}f(\\vec{x}_0)=||\\nabla f(\\vec{x}_0)||\\cdot\\cos\\theta$,\n
                                donde $\\theta$ es el ángulo entre el gradiente y $\\vec{u}$.''').move_to(UP)
        
        text18 = TextMobject('''Por lo mismo, en el sentido contrario del gradiente\n
                                se obtiene el máximo decrecimiento de $f$.''').next_to(text17, 3*DOWN)
        
        text19 = TextMobject('''Regresemos a la función $f(x,y)=-\\frac{x^{2}+y^{2}}{3}+2$,\n
                                donde $\\nabla f(x,y)=\\left(-\\frac{2x}{3},-\\frac{2y}{3}\\right)$.''').move_to(3*UP)
        
        text20_1 = TextMobject('''$\\nabla f(0,2)\\cdot\\left(-\\frac{1}{\\sqrt{2}},\\frac{1}{\\sqrt{2}}\\right)=-\\frac{2\\sqrt{2}}{3}$, que es el valor que obtuvimos inicialmente''').move_to(3*DOWN)
        
        text20_1.scale(0.7)
        
        text20_2 = TextMobject('''para la derivada de $f$ en $(0,2)$ y en la dirección $\\left(-\\frac{1}{\\sqrt{2}},\\frac{1}{\\sqrt{2}}\\right)$.''').move_to(3*DOWN)
        
        text20_2.scale(0.7)
        
        text21 = TextMobject('''Al recorrer el dominio hacia el origen desde $(0,2)$, la superficie crece con mayor inclinación, pues $\\nabla f(0,2)=\\left(0,-\\frac{4}{3}\\right)$.''').move_to(3*DOWN)
        
        text21.scale(0.7)
        
        text22 = TextMobject('''Al hacerlo, el punto en la gráfica va subiendo\n
                             la superficie como si fuera un monte.''').move_to(3*DOWN)
        
        text22.scale(0.7)
        
        text23 = TextMobject('''Si usamos la derivada direccional, al tomar $\\vec{u}=(0,-1)$, obtenemos la inclinación de la superficie en la dirección y sentido del gradiente desde el punto $(0,2)$, la cual es $\\frac{4}{3}$.''').move_to(3.2*DOWN)
        
        text23.scale(0.6)
        
        text24 = TextMobject('''En cambio, al alejarnos del origen sobre el eje Y desde el punto $(0,2)$, la superficie va de bajada.''').move_to(3*DOWN)
        
        text24.scale(0.7)
        
        text25 = TextMobject('''Además, en esa dirección y sentido está la mayor inclinación hacia abajo, porque el gradiente de $f$ en $(0,2)$ apunta hacia el origen.''').move_to(3*DOWN)
        
        text25.scale(0.7)
        
        text26 = TextMobject('''Es decir, si elegimos $\\vec{u}=(0,1)$, entonces en $(0,2)$, $\\vec{u}$ va en la misma dirección del gradiente, pero en sentido contrario.''').move_to(3*DOWN)
        
        text26.scale(0.7)
        
        text27 = TextMobject('''Como la superficie va de bajada, la derivada direccional es negativa y es el menor valor posible en este punto; tal derivada es $-\\frac{4}{3}$.''').move_to(3*DOWN)
        
        text27.scale(0.6)
        
        # Recuadros para algunos textos
        text1.bg = SurroundingRectangle(text1, color = WHITE, fill_color = BLACK, fill_opacity = 1)
        gpo1 = VGroup(text1.bg, text1)
        
        text2.bg = SurroundingRectangle(text2, color = WHITE, fill_color = BLACK, fill_opacity = 1)
        gpo2 = VGroup(text2.bg, text2)
        
        text3.bg = SurroundingRectangle(text3, color = WHITE, fill_color = BLACK, fill_opacity = 1)
        gpo3 = VGroup(text3.bg, text3)
        
        text4.bg = SurroundingRectangle(text4, color = WHITE, fill_color = BLACK, fill_opacity = 1)
        gpo4 = VGroup(text4.bg, text4)
        
        text11.bg = SurroundingRectangle(text11, color = WHITE, fill_color = BLACK, fill_opacity = 1)
        gpo11 = VGroup(text11.bg, text11)
        
        text12.bg = SurroundingRectangle(text12, color = WHITE, fill_color = BLACK, fill_opacity = 1)
        gpo12 = VGroup(text12.bg, text12)
        
        text19.bg = SurroundingRectangle(text19, color = WHITE, fill_color = BLACK, fill_opacity = 1)
        gpo19 = VGroup(text19.bg, text19)
        
        # Ejes utilizados en la animación     
        axis_config = {"dimension": 3,
                        "x_min": -3.5,
                        "x_max": 3.5,
                        "y_min": -3.5,
                        "y_max": 3.5,
                        "z_min": -2,
                        "z_max": 3,
                        "light_source": 9*DOWN + 7*LEFT + 10*OUT}
        
        axis_config2 = {"dimension": 3,
                        "x_min": -4,
                        "x_max": 4,
                        "y_min": -4,
                        "y_max": 4,
                        "z_min": -1,
                        "z_max": 3,
                        "light_source": 9*DOWN + 7*LEFT + 10*OUT}
        
        axes = ThreeDAxes(**axis_config)
        axes2 = ThreeDAxes(**axis_config2)
        
        # Superficies utilizadas en la animación
        plano3 = Plano3().set_shade_in_3d(True)        
        superficie3 = Superficie3().set_shade_in_3d(True)

        # Otros objetos necesarios para la animación        
        x_1, y_1 = 0, 0
        z_1 = self.superficie3(x_1, y_1)        
        punto2 = Dot(color=YELLOW).move_to([x_1, y_1, z_1]).set_shade_in_3d(True)        
        
        curva3 = ParametricFunction(self.curva3, t_min = -2.7, t_max = 2.7, color = BLUE)
        tangente3 = ParametricFunction(self.tangente3, t_min = -2.7, t_max = 2.7, color = PURPLE)
     
        recorrido_a_1 = DashedVMobject(ParametricFunction(self.recorrido, t_min = 2, t_max = 0, color = GREEN_E))
        recorrido_a_2 = DashedVMobject(ParametricFunction(self.recorrido, t_min = 2, t_max = 0, color = GREEN_E))
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
        
        # Derivadas parciales
        self.set_camera_orientation(phi = 0, theta = -90*DEGREES)
        self.play(Write(subtitle2))
        self.wait()
        self.play(FadeOut(subtitle2))
        
        self.set_camera_orientation(0.7*np.pi/2, 0.25*np.pi)
        self.add_fixed_in_frame_mobjects(gpo1)
        self.play(Write(gpo1))
        self.play(ShowCreation(axes))
        self.add_fixed_in_frame_mobjects(func_text3)
        self.play(Write(func_text3))
        self.play(ShowCreation(superficie3))
        self.play(ShowCreation(punto2))
        self.wait()
        self.play(FadeOut(gpo1))
        self.add_fixed_in_frame_mobjects(gpo2)
        self.play(Write(gpo2))
        self.play(ShowCreation(circulo))
        circulo.add_updater(upd_for_circle)
        self.play(rad.set_value, 1, rate_func = linear)
        self.play(ShowCreation(Dirs))
        self.wait()
        self.play(FadeOut(gpo2))
        self.add_fixed_in_frame_mobjects(gpo3)
        self.play(Write(gpo3))
        self.play(FadeOut(Dirs), ReplacementTransform(dir6, dir6_r), ReplacementTransform(dir8, dir8_r))
        self.wait(3)
        self.play(FadeOut(gpo3), run_time = 2)
        self.add_fixed_in_frame_mobjects(gpo4)
        self.play(Write(gpo4))
        self.play(FadeOut(dir6_r), ReplacementTransform(dir8_r, dir8_y))
        self.wait()
        self.play(FadeOut(gpo4))
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        self.set_camera_orientation(phi = 0, theta = -90*DEGREES)
        self.play(Write(text5_1))
        self.play(Write(text5_2))
        self.wait(5)
        self.play(ReplacementTransform(text5_1, text6_1))
        self.wait()
        self.play(ReplacementTransform(VGroup(text5_2[0][24], text5_2[0][25], text5_2[0][26]), VGroup(text6_2[0][24], text6_2[0][25], text6_2[0][26], text6_2[0][27], text6_2[0][28])))
        self.wait()
        self.play(ReplacementTransform(VGroup(text5_2[0][23], text6_2[0][24], text6_2[0][25], text6_2[0][26], text6_2[0][27], text6_2[0][28]), VGroup(text6_3[0][23], text6_3[0][24], text6_3[0][25], text6_3[0][26], text6_3[0][27])))
        self.wait()
        self.play(Write(text7))
        self.wait(3)
        self.play(*[FadeOut(mob)for mob in self.mobjects])
        self.play(Write(text8))
        self.wait(3)
        self.play(Write(text9))
        self.wait(3)
        self.play(FadeOut(text8), FadeOut(text9))
        self.play(Write(text10))
        self.wait(3)
        self.play(FadeOut(text10))

        self.set_camera_orientation(0.7*np.pi/2, 0.25*np.pi)
        self.play(ShowCreation(axes))
        self.play(ShowCreation(superficie3), ShowCreation(punto2), ShowCreation(dir8_y))
        self.add_fixed_in_frame_mobjects(gpo11)
        self.play(Write(gpo11))
        self.wait()
        self.play(ShowCreation(plano3), FadeOut(dir8_y))
        self.wait()
        self.play(ShowCreation(curva3), FadeOut(superficie3))
        self.wait()
        self.move_camera(phi = 90*DEGREES, theta = 90*DEGREES, gamma = 0*DEGREES, frame_center = (0,0,0), run_time = 2)
        self.wait()
        self.play(ShowCreation(tangente3))
        self.wait()
        self.play(FadeOut(gpo11))
        self.add_fixed_in_frame_mobjects(gpo12)
        self.play(Write(gpo12))
        self.wait(4)
        self.play(*[FadeOut(mob)for mob in self.mobjects])
        
        self.set_camera_orientation(phi = 0, theta = -90*DEGREES)
        self.play(Write(text13), run_time = 3)
        self.wait(6)
        self.play(FadeOut(text13))
        self.play(Write(text14), run_time = 3)
        self.wait(6)
        self.play(FadeOut(text14))
        self.play(Write(text15))
        self.wait()
        self.play(Write(text16), run_time = 3)
        self.wait(6)
        self.play(FadeOut(text15), FadeOut(text16))
        self.play(Write(text17), run_time = 4)
        self.wait(6)
        self.play(Write(text18))
        self.wait(3)
        self.play(*[FadeOut(mob)for mob in self.mobjects])
        
        self.set_camera_orientation(0.7*np.pi/2, 0.25*np.pi)
        self.play(ShowCreation(axes2))
        self.play(ShowCreation(Paraboloide2().set_shade_in_3d(True)))
        self.add_fixed_in_frame_mobjects(gpo19)
        self.play(Write(gpo19))
        self.wait(5)
        self.add_fixed_in_frame_mobjects(text20_1)
        self.play(Write(text20_1))
        self.wait(2)
        self.play(FadeOut(text20_1))
        self.add_fixed_in_frame_mobjects(text20_2)
        self.play(Write(text20_2))
        self.wait(2)
        self.play(FadeOut(text20_2))
        self.add_fixed_in_frame_mobjects(text21)
        self.play(Write(text21), run_time = 3)
        self.wait(5)
        self.play(FadeOut(text21))
        self.add_fixed_in_frame_mobjects(text22)
        self.play(Write(text22))
        self.wait()
        self.play(Uncreate(recorrido_a_1), run_time = 3)
        self.play(ShowCreation(recorrido_a_2), run_time = 0)
        self.play(FadeOut(text22))
        self.add_fixed_in_frame_mobjects(text23)
        self.play(Write(text23), run_time = 3)
        self.wait(5)
        self.play(FadeOut(text23))
        self.add_fixed_in_frame_mobjects(text24)
        self.play(Write(text24))
        self.play(ShowCreation(recorrido_b), run_time = 3)
        self.wait(5)
        self.play(FadeOut(text24))
        self.add_fixed_in_frame_mobjects(text25)
        self.play(Write(text25), run_time = 3)
        self.wait(5)
        self.play(FadeOut(text25))
        self.add_fixed_in_frame_mobjects(text26)
        self.play(Write(text26))
        self.wait(6)
        self.play(FadeOut(text26))
        self.add_fixed_in_frame_mobjects(text27)
        self.play(Write(text27), run_time = 3)
        self.wait(8)
        self.play(FadeOut(text27))
        self.wait()
        self.play(*[FadeOut(mob)for mob in self.mobjects])
    
    def construct(self):
        
        # Textos de la animación
        title = TextMobject('''Plano tangente y\n
                            derivadas direccionales''').scale(1.5)
        
        # Escena
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))
        
        self.parte1()
        self.parte2()
        self.parte3()
