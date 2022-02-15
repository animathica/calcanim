from manimlib.imports import *

##############################################################################
##################### Teoremas de diferenciabilidad ##########################
##############################################################################

# Anexado el 07 de julio de 2021.
# Corregido el 13 de noviembre de 2021.
    
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
                            de $f$ en $\\vec{x}_{0}$. Particularmente existen todas las parciales.''').next_to(text2, 2*DOWN)
        
        text3.set_color_by_tex('''Teorema 2. ''', color = BLUE)
        
        text4 = TextMobject('''Para mostrar que el recíproco del ''', '''Teorema 2''', ''' no es cierto,\n
                            tomemos la siguiente función.''').move_to(3*UP)
        
        text4.set_color_by_tex('''Teorema 2''', color = BLUE)
        
        func1 = TextMobject('''$f(x,y)=\\frac{x^{2}y}{x^{4}+y^{2}}$ si $(x, y)\\neq(0,0)$ y''').move_to(2.8*DOWN)
        
        func1.scale(0.8)
        
        func2 = TextMobject('''$f(x,y)=0$ si $(x, y)=(0,0)$.''').next_to(func1, 0.8*DOWN)
        
        func2.scale(0.8)
        
        text5_1 = TextMobject('''Aplicando la definición de derivada direccional, para cualquier $\\vec{u} = (u_{1}, u_{2})$''').move_to(2.7*DOWN)
        
        text5_1.scale(0.7)
        
        text5_2 = TextMobject('''$$\\text{tal que }||\\vec{u}|| = 1,\\text{ } D_{\\vec{u}}f(0, 0) = \\lim_{h\\to 0} \\frac{f(\\vec{x}_{0}+h\\vec{u})-f(\\vec{x}_{0})}{h} = \\lim_{h\\to 0} \\frac{u_{1}^{2}u_{2}}{h^{2}u_{1}^{4}+u_{2}^{2}}.$$''').next_to(text5_1, 0.2*DOWN)
        
        text5_2.scale(0.7)
        
        text6 = TextMobject('''Si $u_{2}\\neq 0$, entonces $D_{\\vec{u}}f(0,0)=\\frac{u_{1}^{2}}{u_{2}}$.''').move_to(3*DOWN)
        
        text6.scale(0.8)
        
        text7 = TextMobject('''Por otro lado, si $u_{2} = 0$, entonces $\\vec{u} = (1,0)$ y $D_{\\vec{u}}f(0,0) = 0$.''').move_to(3*DOWN)
        
        text7.scale(0.8)
        
        text8 = TextMobject('''Es decir, existen todas las derivadas direccionales de $f$ en $(0,0)$.''').move_to(3*DOWN)
        
        text8.scale(0.8)
        
        text9_1 = TextMobject('''Sin embargo, si nos acercamos a $(0,0)$ por los puntos de la forma $(t,t^{2})$ con''').move_to(2.8*DOWN)
        
        text9_1.scale(0.6)
        
        text9_2 = TextMobject('''$$t\\in\\mathbb{R}\\backslash{}\\{(0, 0)\\},\\text{ encontraremos que}\\lim_{(t, t^{2})\\to (0,0)}f(t,t^{2})=\\frac{1}{2},\\text{ por lo que }f\\text{ no es continua en }(0, 0).$$''').next_to(text9_1, 0.2*DOWN)
        
        text9_2.scale(0.6)
        
        text10 = TextMobject('''Como $f$ no es continua en $(0,0)$, por el ''', '''Teorema 1''', ''',\n
                              $f$ no es diferenciable en $(0, 0)$.''').move_to(3*DOWN)
        
        text10.scale(0.8)
        
        text10.set_color_by_tex('''Teorema 1''', color = BLUE)
        
        text11 = TextMobject('''Ahora consideremos un cono,\n
                              cuya regla de correspondencia es $f(x,y)=||(x,y)||$.''').move_to(3*UP)
        
        text12 = TextMobject('''Recordemos que $f$ es continua para todo $(x,y)\\in\\mathbb{R}^{2}$,\n
                              en particular para $(0,0)$.''').move_to(3*DOWN)
        
        text12.scale(0.8)
        
        text13 = TextMobject('''Sin embargo, para cualquier $\\vec{u}=(u_{1},u_{2})$ tal que $||\\vec{u}||=1$, 
                              $$\\lim_{h\\to 0}\\frac{f(\\vec{x}_{0}+h\\vec{u})-f(\\vec{x}_{0})}{h}=\\lim_{h\\to 0}\\frac{|h|}{h},\\text{ de forma que } D_{\\vec{u}}f(0,0)\\text{ no existe.}$$''').move_to(3*DOWN)
        
        text13.scale(0.8)
        
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
        self.play(Write(title), run_time = 3)
        self.wait(3)
        self.play(FadeOut(title))
        
        self.play(Write(text1), run_time = 3)
        self.wait(3)
        self.play(Write(text2), run_time = 3)
        self.wait(3)
        self.play(Write(text3), run_time = 6)
        self.wait(5)
        self.play(*[FadeOut(mob)for mob in self.mobjects])
        
        self.set_camera_orientation(np.pi/4, 0*np.pi)
        self.add_fixed_in_frame_mobjects(gpo_4)
        self.play(Write(gpo_4), run_time = 3)
        self.wait(3)
        self.play(ShowCreation(axes), ShowCreation(superficie), run_time = 2)
        self.wait()
        self.add_fixed_in_frame_mobjects(func1)
        self.play(Write(func1))
        self.add_fixed_in_frame_mobjects(func2)
        self.play(Write(func2))
        self.wait(3)
        self.play(FadeOut(func1), FadeOut(func2))
        self.play(ShowCreation(Dirs))
        self.add_fixed_in_frame_mobjects(text5_1)
        self.play(Write(text5_1), run_time = 3)
        self.add_fixed_in_frame_mobjects(text5_2)
        self.play(Write(text5_2), run_time = 3)
        self.wait(5)
        self.play(FadeOut(text5_1), FadeOut(text5_2))
        self.play(FadeOut(Dir2), FadeOut(Dir4), FadeOut(Dir5), FadeOut(Dir6), FadeOut(Dir8))
        self.add_fixed_in_frame_mobjects(text6)
        self.play(Write(text6))
        self.wait(3)
        self.play(FadeOut(text6))
        self.play(FadeOut(Dir1), FadeOut(Dir3), FadeOut(Dir7))
        self.play(ShowCreation(Dir5))
        self.add_fixed_in_frame_mobjects(text7)
        self.play(Write(text7), run_time = 3)
        self.wait(3)
        self.play(FadeOut(text7), FadeOut(Dir5))
        self.add_fixed_in_frame_mobjects(text8)
        self.play(Write(text8))
        self.wait(3)
        self.play(FadeOut(text8))
        self.play(ShowCreation(dashed_curva))
        self.add_fixed_in_frame_mobjects(text9_1)
        self.play(Write(text9_1), run_time = 3)
        self.add_fixed_in_frame_mobjects(text9_2)
        self.play(Write(text9_2), run_time = 4)
        self.wait(5)
        self.play(FadeOut(text9_1), FadeOut(text9_2), FadeOut(dashed_curva))
        self.add_fixed_in_frame_mobjects(text10)
        self.play(Write(text10), run_time = 3)
        self.wait(5)
        self.play(FadeOut(text10))
        self.play(*[FadeOut(mob)for mob in self.mobjects])
        
        self.set_camera_orientation(0.7*np.pi/2, 0.25*np.pi)
        self.add_fixed_in_frame_mobjects(gpo_11)
        self.play(Write(gpo_11), run_time = 3)
        self.wait(3)
        graf_cono = VGroup(axes, cono, Dirs)
        graf_cono.move_to(ORIGIN)
        self.play(ShowCreation(axes), ShowCreation(cono))
        self.wait(3)
        self.add_fixed_in_frame_mobjects(text12)
        self.play(Write(text12))
        self.wait(3)
        self.play(FadeOut(text12))
        self.play(ShowCreation(Dirs), FadeOut(Dir4))
        self.add_fixed_in_frame_mobjects(text13)
        self.play(Write(text13), run_time = 4)
        self.wait(5)
        self.play(FadeOut(text13))
        self.play(FadeOut(Dir1), FadeOut(Dir2), FadeOut(Dir3), FadeOut(Dir5), FadeOut(Dir6), FadeOut(Dir7) ,FadeOut(Dir8) )
        self.add_fixed_in_frame_mobjects(text14)
        self.play(Write(text14))
        self.wait(3)
        self.play(FadeOut(text14))
        self.add_fixed_in_frame_mobjects(text15)
        self.play(Write(text15))
        self.wait(3)
        self.play(*[FadeOut(mob)for mob in self.mobjects])
        
        self.set_camera_orientation(phi = 0, theta = -90*DEGREES)
        self.play(Write(text16))
        self.wait(3)
        self.play(Write(text17), run_time = 8)
        self.wait(8)
        self.play(*[FadeOut(mob)for mob in self.mobjects])
