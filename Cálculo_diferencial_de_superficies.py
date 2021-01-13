from manimlib.imports import *

#####################################################################################
###### Composición de una superficie con funciones lineales y traslaciones ##########
#####################################################################################
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
        r=0.2
        return np.array([u,v,r*np.sin(7*(v+u))]) 
        #return np.array([r*np.cos(u)*np.cos(v),r*np.cos(v)*np.sin(u),r*np.sin(v)]) 
        #return np.array([0.6*x,0.6*y,0.6*((x*np.cos(y))**2+(y/np.sin(x))**2)]) 
#esferas
class superficie_2(ParametricSurface):
    def __init__(self, **kwargs):
        kwargs = {
        "u_min": 0,
        "u_max": 2*np.pi,
        "v_min": 0,
        "v_max": 2*np.pi,
        "checkerboard_colors": [BLUE_E]
        }
        ParametricSurface.__init__(self, self.func, **kwargs)
    def func(self, u, v):
        r=1
        return np.array([r*np.cos(u)*np.cos(v),r*np.cos(v)*np.sin(u),r*np.sin(v)]) 
#Esferas
class superficie_3(ParametricSurface):
    def __init__(self, **kwargs):
        kwargs = {
        "u_min": 0,
        "u_max": 2*np.pi,
        "v_min": 0,
        "v_max": 2*np.pi,
        "checkerboard_colors": [BLUE_E]
        }
        ParametricSurface.__init__(self, self.func, **kwargs)
    def func(self, u, v):
        r=1
        k=0.1
        return np.array([r*np.cos(u)*np.cos(v),r*np.cos(v)*np.sin(u),k*r*np.sin(v)]) 
class superficie_4(ParametricSurface):
    def __init__(self, **kwargs):
        kwargs = {
        "u_min": 0,
        "u_max": 2*np.pi,
        "v_min": 0,
        "v_max": 2*np.pi,
        "checkerboard_colors": [BLUE_E]
        }
        ParametricSurface.__init__(self, self.func, **kwargs)
    def func(self, u, v):
        r=1
        k=2
        return np.array([r*np.cos(u)*np.cos(v),r*np.cos(v)*np.sin(u),k*r*np.sin(v)]) 
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
        return np.array([x,y,(np.sin(3*(x+y))+y)*0.3])
        #[y,x,x**3+(x*y**2)+np.cos(x)]) 

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
        return np.array([x,y,(np.sin(3*(x-y))-y)*0.3]) 

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
        return np.array([x,y,(np.sin(3*(-x+y))+y)*0.3]) 

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
        a=0
        b=0
        return np.array([x+a,y+b,x**2+(y**2*(np.sin(y)**2))]) 

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
        a=2
        b=0
        return np.array([x+a,y+b,x**2+(y**2*(np.sin(y)**2))])

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
        a=0
        b=2
        return np.array([x+a,y+b,x**2+(y**2*(np.sin(y)**2))])


class Composicion_de_Superficie_Con_Funciones(ThreeDScene):
    def construct (self):
        titulo=TextMobject('''Traslaciones y homotecias \n
                                en superficies''')
        #Cambiar función de superficie
        text1=TextMobject('''Tomemos $f(x,y)=(0.2\sin(7*(x+y)))$''')
        text2=TextMobject('''Una translación vertical de la superficie es de \n
                            la forma: $f(x,y)+k$''').move_to(3*UP)
        text3=TextMobject('''Por ejemplo: $f(x,y)-2$ ''').move_to(3*UP)
        text4=TexMobject(r"f(x,y)+3").move_to(3*UP)
        text5=TextMobject('''También podemos multiplicar superficies por un escalar, \n
                                    es decir: $kf(x,y)$.''').move_to(3*UP)
        text6=TextMobject('''Si $k=0.1$, la gráfica se encoje verticalmente hacia el plano \n
                                del dominio $xy$''').move_to(3*UP)
        text7=TextMobject('''Si $k=2$, la gráfica se estira verticalmente \n
                                alejando los puntos del plano $xy$ ''').move_to(3*UP)
        text8=TextMobject('''También podemos reflejar superficies.''').move_to(3*UP)
        text8_1=TextMobject('''Si $k=-1$, la gráfica de $kf(x,y)$ es la reflexión de la gráfica \n
                                de $f$ respecto al plano $xy$. ''').move_to(3*UP)
        text9=TextMobject('''Para reflejar respecto al plano $yz$, ''').move_to(3*UP)
        text9_1=TextMobject('''tomamos la función $f(x,-y)$.''').move_to(text9.get_center()+0.5*DOWN)
        text10=TextMobject('''Mientras que la gráfica de $f(-x,-y)$ es una \n
                                    reflexión respecto al eje vertical. ''').move_to(3*UP)
        text11=TextMobject('''¿Qué pasa con $f(k(x,y))$, con $k\\in\\mathbb{R}$? ''')
        ###HAY QUE VER SI CON F SE NOTA LA HOMOTECIA HORIZONTAL, POR LA SIMETRÍA DEL PARABOLOIDE NO SE VA A NOTAR EL CAMBIO MUCHO.
        text12=TextMobject('''También podemos hacer traslaciones horizontales. Por ejemplo:''').move_to(3*UP)
        text13=TextMobject('''$g(x,y)=x^{2}+y^{2}\\sin^{2}(y)$''').move_to(3*DOWN)
        text14=TextMobject('''La gráfica de $g((x,y)+(2,0))$ se ve: ''').move_to(3*DOWN)
        text15=TextMobject('''Pero la de $g((x,y)+(0,2))$: ''').move_to(3*DOWN)
        text16=TextMobject('''Modifica el código para crear más ejemplos''')

        axes=ThreeDAxes()
        #Superficies
        superficie1=superficie_1()
        fondo=Rectangle(height=1, width=10,fill_opacity=1,fill_color=BLACK).move_to(text11)

        #Parámetros que se pueden cambiar
        k1=-2
        superficie2=superficie_1().move_to([0,0,k1])
        k2=3
        superficie3=superficie_1().move_to([0,0,3])
        superficie4=superficie_2()
        superficie5=superficie_3()
        superficie6=superficie_4()

        superficie7=superficie_5()
        superficie7_reflejadayz=superficie_5_reflejada()
        superficie8=superficie_5_reflejada1()

        superficie9=superficie_6()
        superficie10=superficie_6_1()
        superficie11=superficie_6_2()


        #Updaters
        #def mov1 (obj):
         #   t = k1u.get_value()
         #   superficie1.become(superficie2)
        #superficie1.add_updater(mov1)                        
        #animación
        self.play(Write(titulo))
        self.wait(6)
        self.play(FadeOut(titulo))
        self.set_camera_orientation(0.7*np.pi/2, 0.25*np.pi,distance=12)
        self.add_fixed_in_frame_mobjects(text1)
        self.play(Write(text1))
        self.wait(4)
        self.play(text1.shift,3*UP,runtime=3)
        self.play(ShowCreation(axes))
        self.play(ShowCreation(superficie1)) 
        self.wait(3)       
        self.play(FadeOut(text1))
        self.add_fixed_in_frame_mobjects(text2)
        self.play(Write(text2))
        self.wait(8)
        self.play(FadeOut(text2))
        self.add_fixed_in_frame_mobjects(text3)        
        self.play(Write(text3))
        self.wait(5)
        self.play(ReplacementTransform(superficie1,superficie2))
        self.wait(5)
        self.play(FadeOut(text3))
        self.add_fixed_in_frame_mobjects(text4)        
        self.play(Write(text4))
        #Movimiento de superficie
        self.wait(5)
        self.play(ReplacementTransform(superficie2,superficie3))
        self.wait(6)
        self.play(FadeOut(text4))
        self.play(FadeOut(superficie3))
        self.add_fixed_in_frame_mobjects(text5)        
        self.play(Write(text5))
        self.wait(7)
        self.play(ShowCreation(superficie4))
        self.wait(4)
        self.play(FadeOut(text5))
        self.add_fixed_in_frame_mobjects(text6)        
        self.play(Write(text6))
        self.wait(6)
        self.play(ReplacementTransform(superficie4,superficie5))
        self.wait(6)
        self.play(FadeOut(text6))
        self.add_fixed_in_frame_mobjects(text7)        
        self.play(Write(text7))
        self.wait(9)
        self.play(ReplacementTransform(superficie5,superficie6))
        self.wait(5)
        self.play(FadeOut(text7))
        self.play(FadeOut(superficie6))
        self.add_fixed_in_frame_mobjects(text8)        
        self.play(Write(text8))
        self.wait(4)
        ##Superficie reflejada
        self.play(ShowCreation(superficie7))
        self.wait()
        self.play(FadeOut(text8))
        self.add_fixed_in_frame_mobjects(text9)        
        self.play(Write(text9))
        self.wait(5)
        #Superficie reflejada 2
        self.add_fixed_in_frame_mobjects(text9_1)        
        self.play(Write(text9_1))
        self.wait(3)
        self.play(ReplacementTransform(superficie7,superficie7_reflejadayz))
        self.wait(4)
        self.play(FadeOut(text9),FadeOut(text9_1))
        self.add_fixed_in_frame_mobjects(text10)        
        self.play(Write(text10))
        self.wait(11)
        self.play(ReplacementTransform(superficie7_reflejadayz,superficie8))
        self.wait(5)
        self.play(FadeOut(text10))
        self.play(FadeOut(superficie8))
        self.add_fixed_in_frame_mobjects(fondo)
        self.add_fixed_in_frame_mobjects(text11)        
        self.play(Write(text11),ShowCreation(fondo))
        self.wait(8)
        self.play(FadeOut(text11),FadeOut(fondo))
        self.add_fixed_in_frame_mobjects(text12)        
        self.play(Write(text12))
        self.wait(7)
        self.play(FadeOut(text12))
        self.add_fixed_in_frame_mobjects(text13)        
        self.play(Write(text13))
        self.wait(6)
        self.play(ShowCreation(superficie9))
        self.wait(5)
        self.play(FadeOut(text13))
        self.add_fixed_in_frame_mobjects(text14)        
        self.play(Write(text14))
        self.wait(7)
        self.play(ReplacementTransform(superficie9,superficie10))
        self.wait(5)
        self.play(FadeOut(text14))
        self.add_fixed_in_frame_mobjects(text15)        
        self.play(Write(text15))
        self.wait(6)
        self.play(ReplacementTransform(superficie10,superficie11))
        self.wait(5)
        self.play(FadeOut(text15),FadeOut(axes),FadeOut(superficie11))
        self.add_fixed_in_frame_mobjects(text16)        
        self.play(Write(text16))
        self.wait(8)
        self.play(FadeOut(text16))



