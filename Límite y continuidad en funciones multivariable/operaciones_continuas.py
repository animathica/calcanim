from manimlib.imports import *

class Operaciones_continuidad(ThreeDScene):
    def acomodar_textos(self,objeto):
        self.add_fixed_in_frame_mobjects(objeto)
        self.play(Write(objeto))
    def acomodar_puntos(self,objeto):
        self.add_fixed_in_frame_mobjects(objeto)
        self.add(objeto)

    # Definimos las funciones a utilizar (las que vamos a graficar)
    # Puedes cambiar estas funciones con las que se te ocurra
    # Son funciones de R  a R2, y estamos obteniendo sus gráficas
    # por lo que la primer entrada siempre debe ser lo que parametriza
    # la función, es decir, la variable independiente 
    def helicoide(self,t):
        return [t,np.cos(5*t),np.sin(5*t)] #f(t)=(cos(5t),sin(5t))
    
    def identidad(self,t):
        return [t,t,t] #g(t)=(t,t)
    
    def func_suma(self,t):
        return [t,t+np.cos(5*t),t+np.sin(5*t)] #(f+g)(t)=(t+cos(5t),t+sin(5t))
    
    def func_por_escalar(self,t):
        k = 3 #Cambiar esta constante hará que se cambie la gráfica de k*f, también debes cambiarla en construct
        return [t,k*np.cos(5*t),k*np.sin(5*t)] #(k*f)(t)=(kcos(5t),ksin(5t))
    
    def func_prod_int(self,t):
        return[t,2*t**2+t*np.cos(5*t)+t*np.sin(5*t),0] #(f\cdot g)(t)=2t^2+tcos(5t)+tsin(5t)
    # Aquí se realiza la animación
    def construct(self):
        k = 3 #Cambia también esta constante al mismo valor que la de la función
        title = TextMobject('''Continuidad: Teoremas de Operaciones''').scale(1.5)
        t_1 = TextMobject('''Sean $f,g:D\\subseteq\\mathbb{R}^n\\longrightarrow\\mathbb{R}^m$, ''','''$x_0$''','''$\\in D$ \n
                            $f$ y $g$ ''','''continuas''',''' en ''','''$x_0$''',''' entonces:''').shift(2*UP)
        t_1.set_color_by_tex_to_color_map({
            '''continuas''': BLUE,
            '''$x_0$''': PURPLE_B
        })
        t_2 = TextMobject('''1) $f+g$ es ''','''continua''',''' en ''','''$x_0$''').next_to(t_1,DOWN,buff=1.2)
        t_2.set_color_by_tex_to_color_map({
            '''continua''': BLUE,
            '''$x_0$''': PURPLE_B
        })
        t_3 = TextMobject('''2) Sea $k\\in\\mathbb{R}$, $kf$ es ''','''continua''',''' en ''','''$x_0$''').next_to(t_2,DOWN)
        t_3.set_color_by_tex_to_color_map({
            '''continua''': BLUE,
            '''$x_0$''': PURPLE_B
        })
        t_4 = TextMobject('''3) $f\\cdot g$ es ''','''continua''',''' en ''','''$x_0$''').next_to(t_3,DOWN)
        t_4.set_color_by_tex_to_color_map({
            '''continua''': BLUE,
            '''$x_0$''': PURPLE_B
        })
        Nota = TextMobject('''Nota: la tercera operación es un producto interior \\\\
                            Si $m=1$ se trata de producto de reales''').scale(0.75).to_edge(DOWN)
        t_5 = TextMobject('''Veamos algunos ejemplos...''')
        reglaf = TextMobject('''$f(t)$''','''$=(\cos(5t),\sin(5t))$''').scale(0.85).to_corner(LEFT+UP).shift(1*RIGHT)
        reglaf.set_color_by_tex_to_color_map({
            '''$f(t)$''': RED
        })
        reglaf.bg = SurroundingRectangle(reglaf,color=WHITE,fill_color=BLACK,fill_opacity=1)
        reglag = TextMobject('''$g(t)$''','''$=(t,t)$''').scale(0.85).to_corner(LEFT+UP).shift(2*RIGHT)
        reglag.set_color_by_tex_to_color_map({
            '''$g(t)$''': TEAL_D
        })
        reglag.bg = SurroundingRectangle(reglag,color=WHITE,fill_color=BLACK,fill_opacity=1)
        t_6 = TextMobject('''$f$''',''' y ''','''$g$''',''' son funciones ''','''continuas''',''' \n
                            en ''','''$t_0=0$''',''', ¿puedes demostrarlo?''').scale(0.85).to_corner(LEFT+UP)
        t_6.set_color_by_tex_to_color_map({
            '''continuas''': BLUE,
            '''$f$''': RED,
            '''$g$''': TEAL_D,
            '''$t_0=0$''': YELLOW
        })
        t_6.bg = SurroundingRectangle(t_6,color=WHITE,fill_color=BLACK,fill_opacity=1)
        t_7 = TextMobject('''Entonces $f+g$ también es \n
                            ''','''continua''',''' en ''','''$t_0$''').scale(0.85).to_corner(LEFT+UP)
        t_7.set_color_by_tex_to_color_map({
            '''continua''': BLUE,
            '''$t_0$''': YELLOW
        })
        t_7.bg = SurroundingRectangle(t_7,color=WHITE,fill_color=BLACK,fill_opacity=1)
        reglafmasg = TextMobject('''$(f+g)(t)$''','''$=(t+\cos(5t),t+\sin(5t))$''').scale(0.85).to_corner(LEFT+UP)
        reglafmasg.set_color_by_tex_to_color_map({
            '''$(f+g)(t)$''': PINK
        })
        reglafmasg.bg = SurroundingRectangle(reglafmasg,color=WHITE,fill_color=BLACK,fill_opacity=1)
        t_8 = TextMobject('''Si tomamos $k=$'''+str(k)+''', \n
                            $kf$ también es ''','''continua''',''' en ''','''$t_0$''').scale(0.85).to_corner(LEFT+UP).shift(0.4*RIGHT)
        t_8.set_color_by_tex_to_color_map({
            '''continua''': BLUE,
            '''$t_0$''': YELLOW
        })
        t_8.bg = SurroundingRectangle(t_8,color=WHITE,fill_color=BLACK,fill_opacity=1)
        reglakf = TexMobject(r"("+str(k)+r"f)(t)=("+str(k)+r"\cos(5t),"+str(k)+r"\sin(5t))").scale(0.85).to_corner(LEFT+UP).shift(0.4*RIGHT)
        reglakf.bg = SurroundingRectangle(reglakf,color=WHITE,fill_color=BLACK,fill_opacity=1)
        for i in range(0,7):
            reglakf[0][i].set_color(ORANGE)
        t_9 = TextMobject('''Por último, al tomar el producto punto de ''','''$f$''',''' y ''','''$g$''',''', la función \n
                            resultante es también ''','''continua''',''' en ''','''$t_0$''')
        t_9.set_color_by_tex_to_color_map({
            '''$f$''': RED,
            '''$g$''': TEAL_D,
            '''continua''': BLUE,
            '''$t_0$''': YELLOW
        })
        reglafpuntog = TextMobject('''$(f\cdot g)(t)$''','''$=2t^2+t\cos(5t)+t\sin(5t)$''').scale(0.85).to_corner(LEFT+UP)
        reglafpuntog.set_color_by_tex_to_color_map({
            '''$(f\cdot g)(t)$''': GREEN_D
        })
        reglafpuntog.bg = SurroundingRectangle(reglafpuntog,color=WHITE,fill_color=BLACK,fill_opacity=1)
        
        # Ejes en 3D
        axis_config = {
            "x_min" : -6,
            "x_max" : 6,
            "y_min" : -6,
            "y_max" : 6,
            "z_min" : -6,
            "z_max" : 6,
        }
        ejes = ThreeDAxes(**axis_config)
        # Ejes en 2D
        ejes2 = Axes(
            x_min=-6,
            x_max=6,
            y_min=-3.5,
            y_max=3.5
        )
        # Funciones que se van a utilizar
        tmin = -6
        tmax = 6
        f = ParametricFunction(self.helicoide,t_min=tmin,t_max=tmax,color=RED).set_shade_in_3d(True)
        g = ParametricFunction(self.identidad,t_min=tmin,t_max=tmax,color=TEAL_D).set_shade_in_3d(True)
        fmasg = ParametricFunction(self.func_suma,t_min=tmin,t_max=tmax,color=PINK).set_shade_in_3d(True)
        kf = ParametricFunction(self.func_por_escalar,t_min=tmin,t_max=tmax,color=ORANGE).set_shade_in_3d(True)
        fpuntog = ParametricFunction(self.func_prod_int,t_min=-1.3,t_max=1.3,color=GREEN_D).set_shade_in_3d(True)
        dot1 = Dot(point=(0,1,0),color=YELLOW,radius=0.1) 
        dot2 = Dot(point=(0,0,0),color=YELLOW,radius=0.1)
        dot3 = Dot(point=(0,1,0),color=YELLOW,radius=0.1)
        dot4 = Dot(point=(0,k,0),color=YELLOW,radius=0.1)
        dot5 = Dot(point=(0,0,0),color=YELLOW,radius=0.1)
        ### Grupos ###
        Group1 = VGroup(t_1,t_2,t_3,t_4,Nota)
        ### Animación ###
        self.play(Write(title))
        self.wait()
        self.play(FadeOutAndShiftDown(title))
        self.play(Write(t_1))
        self.wait(8)
        self.play(Write(t_2))
        self.wait(3)
        self.play(Write(t_3))
        self.wait(3.25)
        self.play(Write(t_4))
        self.wait(3.25)
        self.play(Write(Nota))
        self.wait(2.75)
        self.play(FadeOut(Group1))
        self.play(Write(t_5))
        self.wait(2)
        self.play(FadeOut(t_5))

        self.set_camera_orientation(phi=115*DEGREES,theta=-65*DEGREES)
        self.play(ShowCreation(ejes))
        self.begin_ambient_camera_rotation(rate=0.07)
        self.acomodar_textos(reglaf.bg)
        self.acomodar_textos(reglaf)
        self.add_foreground_mobjects(reglaf.bg)
        self.add_foreground_mobjects(reglaf)
        self.play(ShowCreation(f),run_time=2)
        self.wait(2.5)
        self.play(FadeOut(reglaf),FadeOut(reglaf.bg))
        self.remove_foreground_mobjects(reglaf.bg)
        self.remove_foreground_mobjects(reglaf)
        self.acomodar_textos(reglag.bg)
        self.acomodar_textos(reglag)
        self.add_foreground_mobjects(reglag.bg)
        self.add_foreground_mobjects(reglag)
        self.play(ShowCreation(g),run_time=2)
        self.wait(2.5)
        self.play(FadeOut(reglag),FadeOut(reglag.bg))
        self.remove_foreground_mobjects(reglag.bg)
        self.remove_foreground_mobjects(reglag)
        self.acomodar_textos(t_6.bg)
        self.acomodar_textos(t_6)
        self.add_foreground_mobjects(t_6.bg)
        self.add_foreground_mobjects(t_6)
        self.add(dot1,dot2)
        self.wait(4.5)
        self.remove(dot1,dot2)
        self.play(FadeOut(f),FadeOut(g),FadeOut(t_6),FadeOut(t_6.bg))
        self.remove_foreground_mobjects(t_6.bg)
        self.remove_foreground_mobjects(t_6)
        self.acomodar_textos(t_7.bg)
        self.acomodar_textos(t_7)
        self.add_foreground_mobjects(t_7.bg)
        self.add_foreground_mobjects(t_7)
        self.wait(4.5)
        self.play(FadeOut(t_7),FadeOut(t_7.bg))
        self.remove_foreground_mobjects(t_7.bg)
        self.remove_foreground_mobjects(t_7)
        self.acomodar_textos(reglafmasg.bg)
        self.acomodar_textos(reglafmasg)
        self.add_foreground_mobjects(reglafmasg.bg)
        self.add_foreground_mobjects(reglafmasg)
        self.play(ShowCreation(fmasg),run_time=2)
        self.add(dot3)
        self.wait(6)
        self.remove(dot3)
        self.play(FadeOut(fmasg),FadeOut(reglafmasg),FadeOut(reglafmasg.bg))
        self.remove_foreground_mobjects(reglafmasg.bg)
        self.remove_foreground_mobjects(reglafmasg)
        self.acomodar_textos(t_8.bg)
        self.acomodar_textos(t_8)
        self.add_foreground_mobjects(t_8.bg)
        self.add_foreground_mobjects(t_8)
        self.wait(4.5)
        self.play(FadeOut(t_8),FadeOut(t_8.bg))
        self.remove_foreground_mobjects(t_8.bg)
        self.remove_foreground_mobjects(t_8)
        self.acomodar_textos(reglakf.bg)
        self.acomodar_textos(reglakf)
        self.add_foreground_mobjects(reglakf.bg)
        self.add_foreground_mobjects(reglakf)
        self.play(ShowCreation(kf),run_time=2)
        self.add(dot4)
        self.wait(2)
        self.remove(dot4)
        self.play(FadeOut(reglakf.bg),FadeOut(reglakf),FadeOut(kf),FadeOut(ejes))
        self.remove_foreground_mobjects(reglakf.bg)
        self.remove_foreground_mobjects(reglakf)
        self.stop_ambient_camera_rotation()
        self.set_camera_orientation(phi=0,theta=-90*DEGREES)
        self.play(Write(t_9))
        self.wait(8)
        self.play(FadeOutAndShiftDown(t_9))
        self.play(ShowCreation(ejes2))
        self.play(FadeIn(reglafpuntog.bg))
        self.play(Write(reglafpuntog))
        self.add_foreground_mobjects(reglafpuntog.bg)
        self.add_foreground_mobjects(reglafpuntog)
        self.play(ShowCreation(fpuntog))
        self.add(dot5)
        self.wait(4)
        self.play(FadeOut(ejes2),FadeOut(reglafpuntog),FadeOut(fpuntog),FadeOut(dot5))
        self.remove_foreground_mobjects(reglafpuntog.bg)
        self.remove_foreground_mobjects(reglafpuntog)