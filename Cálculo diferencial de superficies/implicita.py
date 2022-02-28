from manimlib.imports import *

###########################################################################
############### Teorema de la función implícita ###########################
###########################################################################
#Las siguientes funciones se utilizan dentro de la clase Teorema_de_la_funcion_implicita
def coord(x,y,z=0):
            return np.array([x,y,z])

def getX(mob):
    return mob.get_center()[0]

def getY(mob):
    return mob.get_center()[1]
class PathScene(Scene):
    CONFIG = {
        "camera_config":{"background_color": BLACK},
        "x_coords":[0,  1, 3,  -2, -3],
        "y_coords":[3, -2, 1, 2.5, -1]
    }
    def setup(self):
        self.screen_grid = ScreenGrid()
        self.tuples = list(zip(self.x_coords,self.y_coords))

        dots = self.get_all_mobs()
        self.add(self.screen_grid,dots)

    def get_dots(self,coords):
        dots = VGroup(*[Dot(coord(x,y)) for x,y in coords])
        return dots

    def get_all_mobs(self):
        dots = self.get_dots(self.tuples)
        return dots

xx=[2.00000000000000,1.99207006212753,
    1.96794109295076,
    1.96428571428571,
    1.94739846925784,
    1.94739846925784,
    1.92857142857142,
    1.92440134478322,
    1.87105423624390,
    1.85714285714285,
    1.83539741249945,
    1.81204498588724,
    1.78571428571428,
    1.75404377978701,
    1.74307925957247,
    1.71428571428571,
    1.69657552835420,
    1.64624899944313,
    1.64285714285714,
    1.64086274978969,
    1.63443890852586,
    1.57142857142857,
    1.54263111889459,
    1.53212513682558,
    1.52254656812741,
    1.52254656812741,
    1.47940156120402,
    1.46428571428571,
    1.42950221218403,
    1.42883060321954,
    1.42857142857142,
    1.42788754464271,
    1.37875672480703,
    1.35714285714285,
    1.33070322461569,
    1.28993627730946,
    1.28571428571428,
    1.28438916458831,
    1.28221929258889,
    1.24999999999999,
    1.23923665792363,
    1.22225596305606,
    1.21428571428571,
    1.19529277869152,
    1.17857142857142,
    1.16889046760885,
    1.15332193803279,
    1.14285714285714,
    1.12084800770305,
    1.11290509377722,
    1.10714285714285,
    1.07715091128091,
    1.07400738470829,
    1.07142857142857,
    1.03706292642433,
    1.03632973210253,
    1.03571428571428,
    1.00000000000000,
    1.00000000000000,
    1.00000000000000,
    0.96549573309241,
    0.96487988722524,
    0.96428571428571,
    0.93317625629596,
    0.93097409934218,
    0.92857142857143,
    0.92857142857143,
    0.90274170190213,
    0.89818419293179,
    0.89285714285714,
    0.88220102502493,
    0.87395239171894,
    0.86648692314929,
    0.85714285714286,
    0.84661846468597,
    0.83547483276687,
    0.82142857142857,
    0.82059206701824,
    0.81866751893126,
    0.80612861998206,
    0.79565111698159,
    0.78571428571429,
    0.77721462292128,
    0.77176047063615,
    0.75000000000000,
    0.74927326252558,
    0.74886617223303,
    0.74716692368269,
    0.72672031723563,
    0.72175641350309,
    0.71428571428571,
    0.70542500420538,
    0.69511992317336,
    0.68486228444107,
    0.67857142857143,
    0.66947460409628,
    0.64936920414801,
    0.64570349727188,
    0.64466542795625,
    0.64285714285714,
    0.61990961993818,
    0.60851782102455,
    0.59620956726482,
    0.57745378643870,
    0.57446454996523,
    0.57341827395765,
    0.57142857142857,
    0.55057075097090,
    0.54190303053693,
    0.53571428571429,
    0.52893520303760,
    0.51989191284756,
    0.51098191811807,
    0.50768759309396,
    0.50000000000000,
    0.48700313599182,
    0.48192435409066,
    0.47174626879381,
    0.46739023694332,
    0.45458937936551,
    0.44773454351703,
    0.43082281147161,
    0.42997864965176]

yy=[0.562054465601987,
    0.563498633556105,
    0.567773192763522,
    0.568324200689500,
    0.571428571428571,
    0.574180132361668,
    0.574742244379767,
    0.575598655216774,
    0.585339950529616,
    0.588385766451898,
    0.593174016071968,
    0.597759271601533,
    0.602820284306861,
    0.611186636929868,
    0.614063597570377,
    0.620908624852905,
    0.625146956925632,
    0.639465286271150,
    0.640251303357088,
    0.640862749789693,
    0.642857142857142,
    0.661125955591523,
    0.671654595391113,
    0.674982279682725,
    0.678571428571428,
    0.686444533487128,
    0.693687275489738,
    0.699899330840044,
    0.714285714285714,
    0.714544888933829,
    0.714661117598423,
    0.714969598214431,
    0.735899581949889,
    0.745545648794911,
    0.759274653187123,
    0.781492294119102,
    0.783693602800151,
    0.784389164588318,
    0.785714285714285,
    0.804035939530145,
    0.810665229352203,
    0.821428571428571,
    0.826353452187920,
    0.838149921548666,
    0.850159859732127,
    0.857142857142857,
    0.867607652318510,
    0.875726066144871,
    0.892857142857142,
    0.898619379491512,
    0.903437250946083,
    0.928571428571428,
    0.931150241851151,
    0.933338278908915,
    0.964285714285714,
    0.964901160673967,
    0.965495755036350,
    0.999999999999999,
    1.000000000000000,
    1.000000000000000,
    1.035714285714280,
    1.036308458653810,
    1.036308458653810,
    1.071428571428570,
    1.073831242199320,
    1.076549922093520,
    1.093011781629230,
    1.107142857142850,
    1.112469907217500,
    1.118931454279400,
    1.132201025024930,
    1.142857142857140,
    1.152201208863570,
    1.164345187294420,
    1.178571428571420,
    1.192617689909730,
    1.213078301405520,
    1.214285714285710,
    1.217046766783020,
    1.217046766783020,
    1.249999999999990,
    1.264447966331650,
    1.277214622921280,
    1.285714285714280,
    1.319585332903460,
    1.320701833954150,
    1.321428571428570,
    1.324261647745880,
    1.357142857142850,
    1.364613556360230,
    1.377663592364780,
    1.392857142857140,
    1.409405637459070,
    1.428571428571420,
    1.439588220876590,
    1.455188889810560,
    1.493487938709130,
    1.499999999999990,
    1.501808285099100,
    1.505199493278960,
    1.548481048509600,
    1.571428571428570,
    1.596209567264820,
    1.636831927847010,
    1.642857142857140,
    1.644846845386220,
    1.649114513152530,
    1.693427893828040,
    1.714285714285710,
    1.728377518993640,
    1.743220917323310,
    1.765822372866720,
    1.785714285714280,
    1.793401878808240,
    1.812558211379150,
    1.844145993134670,
    1.857142857142850,
    1.885396588349040,
    1.895961665514740,
    1.928571428571420,
    1.947734543517020,
    1.997748617099810,
    2.000000000000000]
VALORES=[]
for i in range(0,122):
    VALORES.append([xx[i],yy[i],2])

class Teorema_de_la_funcion_implicita (ThreeDScene,Scene):
    def setup(self):
        Scene.setup(self)
        ThreeDScene.setup(self)
    def acomodar_textos(self,objeto):
        self.add_fixed_in_frame_mobjects(objeto)
        self.play(Write(objeto))
    def Primera_escena(self):
        titulo=TextMobject('''Teorema de la función \n
                                implícita en funciones de \n 
                                $\\mathbb{R}^2\\to\\mathbb{{R}}$''').scale(2)
        text1=TextMobject('''Sea $f:D \\subset \\mathbb{R}^2\\to \\mathbb{R}$, $D$ abierto y $f \\in C^1_D$.\n
                                Sea $(x_0,y_0)\\in D$ y $f(x_0,y_0)=k$ para alguna $k\\in \\mathbb{R}$ y\n
                                $\\frac{\\partial f}{\\partial y}(x_0,y_0) \\neq 0$, entonces para alguna $\\epsilon>0$ \n
                                $\\exists !$ tal que $g:V_\\epsilon(x_0)\\to \\mathbb{R}$ es acotada, $g\\in C^1_{V_\\epsilon(x_0)}$ y \n
                                $f(x,g(x))=k$ para toda $x\\in V_\\epsilon(x_0)$.\n
                                Además $$g'(x)=\\frac{-\\frac{\\partial f}{\\partial x}  (x,g(x))}{\\frac{\\partial f}{\\partial y} (x,g(x))}.$$''')
        text1_1=TextMobject('''Este teorema nos dice que en estas condiciones \n
                                    el conjunto de nivel que corresponde \n
                                    a ''','''$k=f(x_0,y_0)$''',''' es localmente una curva \n
                                    suave dada por la gráfica de ''','''$g$''',''' y además la \n
                                    derivada de ''' ,'''$g$''',''' está en términos de las parciales de''',''' $f$. ''')
        text1_1.set_color_by_tex_to_color_map({
            '''$k=f(x_0,y_0)$''': YELLOW,
            '''$g$''': YELLOW,
            ''' $f$''': ORANGE
        })
        text2=TextMobject('''Considera la función''',''' $f(x,y)=x^2-y$ ''','''y su ''','''curva de nivel 0''','''. ''').move_to(-3.5*UP)
        text2.set_color_by_tex_to_color_map({
            '''' $f(x,y)=x^2-y$ ''': PURPLE_C,
            '''curva de nivel 0''': TEAL_E
        })
        text2.bg=SurroundingRectangle(text2,color=WHITE,fill_color=BLACK,fill_opacity=1)
        text3=TextMobject('''Nota que \n
                             $\\frac{\\partial f}{\\partial y}(x,y)=-1 $ ''').move_to(-3*UP)
        text3.bg=SurroundingRectangle(text3,color=WHITE,fill_color=BLACK,fill_opacity=1)
        text4=TextMobject('''Puedes comprobar que en cualquier punto se cumplen\n
                                 las condiciones del ''','''teorema de la  \n
                                 función implícita.''').move_to(-2.5*UP)
        #######
        text4.set_color_by_tex_to_color_map({
            '''teorema de la  \n
                                 función implícita.''': ORANGE
        })
        ####
        text4.bg=SurroundingRectangle(text4,color=WHITE,fill_color=BLACK,fill_opacity=1)
        text5=TextMobject('''Observa que la ''','''curva de nivel''',''', en términos de \n
                                la variable $x$, queda descrita como ''','''$y(x)=g(x)=x^2$''','''.''').move_to(-3*UP)
        text5.set_color_by_tex_to_color_map({
            '''$y(x)=g(x)=x^2$''':  TEAL_E,
            '''curva de nivel''': TEAL_E,
        })
        text5.bg=SurroundingRectangle(text5,color=WHITE,fill_color=BLACK,fill_opacity=1)
        text6=TextMobject(''' Sin embargo, no siempre se puede encontrar \n
                                explícitamente a la función ''','''$g$''',''', porque no \n
                                siempre se puede despejar la $y$ en términos \n
                                de la $x$ en la ecuación ''','''$f(x,y)=k$''','''. ''')
        text6.set_color_by_tex_to_color_map({
            '''$g$''': TEAL_E,
            '''$f(x,y)=k$''': PURPLE_C
        })
        
        
        ejes = ThreeDAxes(y_max=3)
        eje_x=TexMobject(r"x").move_to(6*RIGHT).scale(1.5)
        eje_y=TexMobject(r"y").move_to(3.5*UP).scale(1.5)
        axes=VGroup(ejes,eje_x,eje_y)
        superficie1 = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                u**2-v
            ]),v_min=-3,v_max=2,u_min=-3,u_max=2,fill_opacity=0.75,checkerboard_colors=[PURPLE_A,PURPLE_A])#.resolution=(50, 50)
            
        curva1=ParametricFunction(
                lambda u : np.array([
                u,
                u**2,
                0
            ]),color=TEAL_E,t_min=-1.5,t_max=1.5,
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
    
    def Segunda_escena(self):
        text8_1=TextMobject('''Por ejemplo; sea ''','''$D=\\{(x,y)\\in\\mathbb{R}^2|x> 0, \\ y> 0\\}$''',''' y \n
                                 $f:D \\to\\mathbb{R}$, ''','''$f(x,y)=x^y+y^{xy}$ ''').move_to(3*DOWN)
        text8_1.set_color_by_tex_to_color_map({
            '''$f(x,y)=x^y+y^{xy}$ ''': BLUE_D,
            '''$D=\\{(x,y)\\in\\mathbb{R}^2|x> 0, \\ y> 0\\}$''': ORANGE
        })
        text8_1.bg=SurroundingRectangle(text8_1,color=WHITE,fill_color=BLACK,fill_opacity=1)
        text8_2=TextMobject('''Puedes comprobar que dicha función es de clase ''','''$C^1_D$''','''. ''').move_to(3*DOWN)
        text8_2.set_color_by_tex_to_color_map({
            '''$C^1_D$''': YELLOW
        })
        text8_2.bg=SurroundingRectangle(text8_2,color=WHITE,fill_color=BLACK,fill_opacity=1)
        text8_3=TextMobject('''Así mismo considera la ''','''curva de nivel 2''',''' y el punto ''','''(1,1)''',''' \n
                                 que pertenece a ella. ''').move_to(3*DOWN)
        text8_3.set_color_by_tex_to_color_map({
            '''curva de nivel 2''': ORANGE,
            '''(1,1)''': PINK
        })
        text8_3.bg=SurroundingRectangle(text8_3,color=WHITE,fill_color=BLACK,fill_opacity=1)                        
        text8_4=TextMobject('''La parcial con respecto a $y$ de dicha función es
                                $$\\frac{\\partial (x^y+y^{xy})}{\\partial y}=x^ylog(x)+xy^{xy}(log(y)+1)$$ ''').move_to(2*DOWN)
        text8_4.bg=SurroundingRectangle(text8_4,color=WHITE,fill_color=BLACK,fill_opacity=1)
        text8_5=TextMobject(''' La cual al evaluarse en el punto ''','''(1,1)''',''' es diferente de 0.''').move_to(3*DOWN)
        text8_5.set_color_by_tex_to_color_map({
            '''(1,1)''':PINK
        })
        text8_5.bg=SurroundingRectangle(text8_5,color=WHITE,fill_color=BLACK,fill_opacity=1)
        text8_6=TextMobject('''Debido a lo anterior se cumplen las condiciones del \n
                                ''','''teorema de la función implícita''',''' para el punto ''','''(1,1)''','''.''').move_to(3*DOWN)
        text8_6.set_color_by_tex_to_color_map({
            '''teorema de la función implícita''':YELLOW,
            '''(1,1)''':PINK
        })
        text8_6.bg=SurroundingRectangle(text8_6,color=WHITE,fill_color=BLACK,fill_opacity=1)
        text8_7=TextMobject('''Entonces se puede describir la ''','''curva de nivel 2''',''', \n
                                    alrededor del punto ''','''(1,1)''',''', como una función ''','''g(x)=y''','''. ''').move_to(3*DOWN)
        text8_7.set_color_by_tex_to_color_map({
            '''curva de nivel 2''':ORANGE,
            '''(1,1)''':PINK,
            '''g(x)=y''':ORANGE
        })
        text8_7.bg=SurroundingRectangle(text8_7,color=WHITE,fill_color=BLACK,fill_opacity=1)
        text8_8=TextMobject(''' Sin embargo no es posible despejar la variable $y$ \n
                                    de la ecuación ''','''$x^y+y^{xy}=2$''').move_to(3*DOWN)
        text8_8.set_color_by_tex_to_color_map({
            '''$x^y+y^{xy}=2$''': ORANGE
        })
        text8_8.bg=SurroundingRectangle(text8_8,color=WHITE,fill_color=BLACK,fill_opacity=1)
        text8_9=TextMobject('''Con el ejemplo anterior apreciamos que existen funciones \n
                                 en las cuales no es posible despejar la variable $y$ de \n
                                 la ecuación ''','''$f(x,y)=k$''',''', pero con el ''','''teorema de \n
                                    la función implícita podemos asegurar que dicha curva \n
                                  se puede describir como la gráfica de una función $g(x)=y$.''')
        #Quite coma despues de BLUE_D
        text8_9.set_color_by_tex_to_color_map({
            '''$f(x,y)=k$''':BLUE_D 
        })
        #text8_9.bg=SurroundingRectangle(text8_9,fill_color=BLACK, stroke_color=BLACK,fill_opacity=1)
        ejes=ThreeDAxes(y_min=-2,y_max=3,x_max=3,x_min=-2,z_max=2.5)
        eje_x=TexMobject(r"x").move_to(3.5*RIGHT).scale(1.5)
        eje_y=TexMobject(r"y").move_to(3.5*UP).scale(1.5)
        axes=VGroup(ejes,eje_x,eje_y)
        superficie8=ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                (u**v)+(v**(u*v))
            ]),v_min=0.08,v_max=2.15,u_min=0.08,u_max=2,fill_opacity=0.75,checkerboard_colors=[BLUE_D,BLUE_D])
        punto_1=Dot(radius=0.1,color=PINK).move_to([1,1,2])
        punto_2=Dot(radius=0.1,color=PINK).move_to([1,1,2])
        

       
        #curva_nivel= SVGMobject("desmos-graph2.svg",color=BLACK,stroke_color=BLUE).scale(2.3).move_to([2.3,2.5,2])
        curva_nivel_label=TexMobject(r"g(x)=y",color=ORANGE).move_to([2,1.5,0]).scale(0.8)
        rectangulo = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                2
            ]),v_min=0,v_max=3,u_min=0,u_max=2,fill_color=RED,fill_opacity=0.7, checkerboard_colors=[RED,RED])
        ############# Para anexar los puntos
        VALORES_OBJ=[]
        for i in VALORES:
            punto_i = Dot(point=i, radius=0.05,color=ORANGE)
            VALORES_OBJ.append(punto_i)

        
        grafica=VGroup(*VALORES_OBJ)

        path = VMobject()
        path.set_points_smoothly([*[coord(x,y) for x in xx for y in yy]])
        self.set_camera_orientation(phi=75 * DEGREES,theta=-80*DEGREES,distance=10)
        #self.set_camera_orientation(phi=75 * DEGREES,theta=-160*DEGREES,distance=4)
        self.play(ShowCreation(axes))
        self.acomodar_textos(text8_1.bg)
        self.acomodar_textos(text8_1)
        self.wait()
        self.play(ShowCreation(superficie8))
       
        self.wait(26)
        self.play(FadeOut(text8_1),FadeOut(text8_1.bg))
        self.acomodar_textos(text8_2.bg)
        self.acomodar_textos(text8_2)
        self.wait(12)
        self.play(FadeOut(text8_2),FadeOut(text8_2.bg))
        self.acomodar_textos(text8_3.bg)
        self.acomodar_textos(text8_3)
        self.play(ShowCreation(grafica))
        self.wait()
        self.play(ShowCreation(punto_1))
        #self.play(ShowCreation(rectangulo))
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
        
        self.play(FadeOut(punto_2))
        self.play(ShowCreation(punto_2))
        self.acomodar_textos(curva_nivel_label)
        self.wait(13)
        self.play(FadeOut(text8_7),FadeOut(text8_7.bg))
        self.acomodar_textos(text8_8.bg)
        self.acomodar_textos(text8_8)
        self.wait(15)
        self.play(FadeOut(axes),FadeOut(text8_8),FadeOut(text8_8.bg),FadeOut(grafica),FadeOut(punto_2),FadeOut(curva_nivel_label))
        
        self.acomodar_textos(text8_9)
        self.wait(28)
        self.play(FadeOut(text8_9))
    
        

    
    def Tercera_escena(self):
        
        text9=TextMobject('''Veamos otro ejemplo.''')
        text10=TextMobject(''' Considera ''','''$f(x,y)=y^3-x^9$''',''' y su ''','''curva de nivel 0''','''.''').move_to(3*UP)
        text10.set_color_by_tex_to_color_map({
            '''$f(x,y)=y^3-x^9$''': BLUE_D,
            '''curva de nivel 0''': ORANGE
        })
        text10.bg=SurroundingRectangle(text10,color=WHITE,fill_color=BLACK,fill_opacity=1)
        text11=TextMobject(''' Si bien $\\frac{\\partial f}{\\partial y}(x,y)=3y^2$ y \n
                                 $\\frac{\\partial f}{\\partial y}(0,0)=0$, puedes observar \n 
                                 que la expresión ''','''$g(x)=y(x)=x^3$''',''' describe a la ''','''curva de nivel''','''.''').move_to(-2.7*UP)
        text11.set_color_by_tex_to_color_map({
            '''$g(x)=y(x)=x^3$''': ORANGE,
            '''curva de nivel''': ORANGE
        })
        text11.bg=SurroundingRectangle(text11,color=WHITE,fill_color=BLACK,fill_opacity=1)
        text12=TextMobject('''Lo que nos dice que no se vale el regreso del ''','''Teorema''','''.''')
        text12.set_color_by_tex_to_color_map({
            '''Teorema''': YELLOW
        })

        ejes=ThreeDAxes(y_max=3,y_min=-3)
        eje_x=TexMobject(r"x").move_to(6*RIGHT).scale(1.5)
        eje_y=TexMobject(r"y").move_to(3.5*UP).scale(1.5)
        axes=VGroup(ejes,eje_x,eje_y)

        superficie3 = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                v**3-u**9
            ]),v_min=-2,v_max=2,u_min=-1.6,u_max=1.6,fill_opacity=0.75,checkerboard_colors=[BLUE_D,BLUE_D])
            
        curva3=ParametricFunction(
                lambda u : np.array([
                u,
                u**3,
                0
            ]),color=ORANGE,t_min=-1.26,t_max=1.26,
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

    def Cuarta_escena(self):
        text13=TextMobject('''Ahora considera la función ''','''$\gamma(x,y)=xy$''','''. ''').move_to(3*UP)
        text13.set_color_by_tex_to_color_map({
            '''$\gamma(x,y)=xy$''': MAROON_B
        })
        text13.bg=SurroundingRectangle(text13,color=WHITE,fill_color=BLACK,fill_opacity=1)
        text14=TextMobject('''Notarás que la ''','''curva de nivel 0''',''' de la función corresponde \n
                                        a los ejes $x$ y $y$.''').move_to(3*DOWN)
        text14.set_color_by_tex_to_color_map({
            '''curva de nivel 0''': BLUE_D
        })
        text14.bg=SurroundingRectangle(text14,color=WHITE,fill_color=BLACK,fill_opacity=1)
        text15=TextMobject('''Además debido a que \n
                                $\\frac{\\partial \\gamma}{\\partial y}=x. $''').move_to(3*UP)
        text15.bg=SurroundingRectangle(text15,color=WHITE,fill_color=BLACK,fill_opacity=1)
        
        #text16=TextMobject('''En los puntos de la ''','''curva de nivel''',''' en el eje $y$ la parcial \n
        #                        se anula y no es posible aplicar el''',''' teorema de \n
        #                        la función implícita''','''.''').move_to(2.5*UP)
        #text16.set_color_by_tex_to_color_map({
        #    '''curva de nivel''': BLUE_D,
        #    '''teorema de la función implícita''': YELLOW
        #})
        
        text16=TextMobject('''En los puntos del eje $y$, $\\frac{\\partial \\gamma}{\\partial y} = \\frac{\\partial \\gamma}{\\partial x} = 0$, no podemos usar \n
                            el Teorema de la Función Implícita, además la curva de \n
                            nivel cero es una recta vertical y no puede ser la gráfica\n
                             de una función g(x)=y.''','''.''').move_to(2.5*UP)
       
        text16.bg=SurroundingRectangle(text16,color=WHITE,fill_color=BLACK,fill_opacity=1)
        text17=TextMobject('''¿Qué ocurre si $\\frac{\\partial f}{\\partial x}(x,y)\\neq 0$?''',''' \n
                                Enuncia el Teorema de la función implícita correspondiente.''')
        text18=TextMobject('''Observa que en el caso del ejemplo ''','''$\\gamma(x,y)=xy$''',''', \n
                                en el origen tenemos un ''','''punto crítico,''',''' por el cual  \n
                                pasa ''','''la curva de nivel $0$''',''' de ''','''$\\gamma$.''').move_to(-2.7*DOWN)
        text18_2=TextMobject(''' Dicha ''','''curva de nivel 0''',''' es la intersección de dos \n
                                  rectas: una vertical y una horizontal.''').move_to(3*DOWN)
        text18_2.set_color_by_tex_to_color_map({
            '''curva de nivel''': BLUE_D
        })
        
        text18_2.bg=SurroundingRectangle(text18_2,color=WHITE,fill_color=BLACK,fill_opacity=1)
        text18.set_color_by_tex_to_color_map({
            '''$\\gamma(x,y)=xy$''': MAROON_B,
            '''punto crítico''': RED,
            '''curva de nivel''': BLUE_D,
            '''$\\gamma$.''': MAROON_B

        })
        text18.bg=SurroundingRectangle(text18,color=WHITE,fill_color=BLACK,fill_opacity=1)
        text18_1=TextMobject('''Y no se puede describir la ''','''curva de nivel''',''' \n
                                como la gráfica de una función de ninguna de las variables \n
                                en términos de la otra.''').move_to(3*DOWN)
        text18_1.set_color_by_tex_to_color_map({
            '''curva de nivel''': BLUE_D

        })
        text18_1.bg=SurroundingRectangle(text18_1,color=WHITE,fill_color=BLACK,fill_opacity=1)
        ejes=ThreeDAxes()
        eje_x=TexMobject(r"x").move_to(6*RIGHT).scale(1.5)
        eje_y=TexMobject(r"y").move_to(6*UP).scale(1.5)
        axes=VGroup(ejes,eje_x,eje_y)
        
        superficie4 = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                u*v
            ]),v_min=-3,v_max=3,u_min=-3,u_max=3,fill_opacity=0.75,checkerboard_colors=[MAROON_B,MAROON_B])
        curva4_1=ParametricFunction(
                lambda u : np.array([
                u,
                0,
                0
            ]),color=BLUE_D,t_min=-3,t_max=3,
            )
        curva4_2=ParametricFunction(
                lambda u : np.array([
                0,
                u,
                0
            ]),color=BLUE_D,t_min=-3,t_max=3,
            )    
        curva4=VGroup(curva4_1,curva4_2)
        
        punto_critico=Dot(radius=0.2,color=RED).move_to([0,0,0])

        self.set_camera_orientation(phi=75 * DEGREES,theta=-45*DEGREES,distance=100)
        self.play(ShowCreation(axes))
        self.acomodar_textos(text13.bg)
        self.acomodar_textos(text13)
        self.play(ShowCreation(superficie4))
        self.wait(10)
        self.begin_ambient_camera_rotation(rate=0.02)
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
        self.play(ShowCreation(curva4))
        #acomodar tiempos
        self.play(ShowCreation(punto_critico))
        self.wait(10)
        self.acomodar_textos(text18_2.bg)
        self.acomodar_textos(text18_2)
        self.wait(12)
        self.play(FadeOut(text18_2),FadeOut(text18_2.bg),FadeOut(text18),FadeOut(text18.bg))
        self.acomodar_textos(text18_1.bg)
        self.acomodar_textos(text18_1)
        self.wait(15)
        self.play(FadeOut(axes),FadeOut(superficie4),FadeOut(punto_critico),FadeOut(curva4),FadeOut(text18_1),FadeOut(text18_1.bg))
        
    def Quinta_escena(self):
        text18_0=TextMobject('''Geométricamente el teorema de la función implícita \n
                             dice que si ''','''$\\nabla f(x_0,y_0)$''',''' no es horizontal, \n
                             $\\frac{\\partial f}{\\partial y}(x_0,y_0)\\neq 0$''',''',''')
        text18_0.set_color_by_tex_to_color_map({
            '''$\\nabla f(x_0,y_0)$''': ORANGE
        })
        text18_0.move_to(3*UP).scale(0.8)
        text18_0.bg=SurroundingRectangle(text18_0,color=WHITE,fill_color=BLACK,fill_opacity=1)  

        text18_1=TextMobject('''es decir no es paralelo al eje $x$ entonces podemos \n
                             describir un sector de la ''','''curva de nivel $k$''',''',\n
                              alrededor de ''','''$(x_0,y_0)$''','''  como la gráfica de una \n
                              función de la forma ''','''$y=g(x)$.''')  
        text18_1.set_color_by_tex_to_color_map({
            '''curva de nivel $k$''': TEAL_C,
            '''$y=g(x)$.''': PINK,
            '''$(x_0,y_0)$''':YELLOW})
        text18_1.move_to(2.5*DOWN).scale(0.8)
        text18_1.bg=SurroundingRectangle(text18_1,color=WHITE,fill_color=BLACK,fill_opacity=1)
        text18=VGroup(text18_0,text18_1)
        text18.bg=VGroup(text18_0.bg,text18_1.bg)

        text19=TextMobject('''Y si el vector ''','''$\\nabla f(x_0',y_0')$''',''' no es vertical, entonces
                                $\\frac{\\partial f}{\\partial x}(x_0',y_0')\\neq 0$, \n
                                es decir no es paralelo al eje $y$, entonces un sector de la\n
                                ''','''curva de nivel $k$''',''' de $f$ alrededor del punto ''','''$(x_0',y_0')$''',''' se\n
                                puede ver como la gráfica de una función de la forma ''','''$x=h(y).$''').move_to(-2.8*DOWN).scale(0.8)
        text19.set_color_by_tex_to_color_map({
            '''$\\nabla f(x_0',y_0')$''': ORANGE,
            '''curva de nivel $k$''': TEAL_C,
            '''$(x_0',y_0')$''': YELLOW,
            '''$x=h(y).$''':PURPLE_C
        })
        text19.bg=SurroundingRectangle(text19,color=WHITE,fill_color=BLACK,fill_opacity=1)
        text20=TextMobject('''Un corolario del ''','''Teorema de la función implícita''',''' es \n
                                que el gradiente es ortogonal a la ''','''curva de nivel''','''.''').move_to(3*DOWN)
        text20.set_color_by_tex_to_color_map({
            '''Teorema de la función implícita''':TEAL_B
        })
        text20.set_color_by_tex_to_color_map({
            '''Teorema de la función implícita''': YELLOW
        })
        text20.bg=SurroundingRectangle(text20,color=WHITE,fill_color=BLACK,fill_opacity=1)
        text21=TextMobject('''Con los ejemplos anteriores sólo se consideró el Teorema de \n
                                 la función implícita en funciones de $\\mathbb{R}^2\\to\\mathbb{R}$, \n
                                 sin embargo el teorema es generalizable a \n
                                 funciones de $\\mathbb{R}^n\\to\\mathbb{R}$.''')
        
        
        ejes=ThreeDAxes(x_max=4.8,y_max=3,x_min=-4.8,y_min=-4.8)
        eje_x=TexMobject(r"x").move_to(5*RIGHT).scale(1)
        eje_y=TexMobject(r"y").move_to(3.5*UP).scale(1.5)
        axes=VGroup(ejes,eje_x,eje_y)


        #Objetos para el primer ejemplo
        curva=ParametricFunction(
                lambda u : np.array([
                u,
                1.5*np.cos(u/2)**(1/3),
                0
            ]),color=TEAL_C,t_min=-4.5,t_max=4.5,
            )    
         
        curva_ejem1=DashedVMobject(curva,y_tick_frequency=0.02, x_tick_frequency=0.02)
        curva_ejem1_label=TexMobject(r"f(x,y)=k").move_to(1*UP+4*LEFT).scale(0.7).set_color(TEAL_C)

        
        #Se puede modificar los parámetros a y b para modificar el punto (a,b)=(x0,y0)
        a=1
        b=1.5*np.cos(a/2)**(1/3)
        x0=np.array([a,b,0])
        x0_dot=Dot(color=YELLOW).move_to(x0)
        x0_dot_label=TexMobject(r"(x_0,y_0)").set_color(YELLOW).scale(0.5).next_to(x0_dot,0.9*RIGHT+DOWN,buff=0.1)
        x0_group=VGroup(x0_dot,x0_dot_label)
        grad1_vec=Arrow([a,b,0],[(-0.25*np.sin(a/2))/(np.cos(a/2)**(2/3))     ,-1,0],buff=0,color=ORANGE)
        grad1_label=TexMobject(r"\nabla f(x_0,y_0)").next_to(grad1_vec,0.7*DOWN+0.1*LEFT,buff=-0.3).set_color(ORANGE).scale(0.7)
        grad1=VGroup(grad1_vec,grad1_label)
        
        #Se puede modificar el parámetro v para tener una vecidad diferente y con ello cambiar la longitud de la funcion
        #g(x) en el ejemplo
        v=1.5
        curva_1=ParametricFunction(
                lambda u : np.array([
                u,
                1.5*np.cos(u/2)**(1/3),
                0
            ]),color=PURPLE_C,t_min=a-v,t_max=a+v,
            )   
        curva1_label=TexMobject(r"g(x)").next_to(curva_1,UP,buff=0.1).set_color(PINK).scale(0.8)
        curva1=VGroup(curva_1,curva1_label)

        
        #Objetos para el segundo ejemplo
        #Se pueden modificar los parámetroa a2 y b2 para cambiar el punto (x0,y0) del segundo ejemplo
        a2=2.5
        b2=1.5*np.cos(a2/2)**(1/3)
        x02=np.array([a2,b2,0])
        x02_dot=Dot(color=YELLOW).move_to(x02)
        x02_dot_label=TexMobject(r"(x_0',y_0')").scale(0.5).next_to(x02_dot,RIGHT+UP,buff=0.1).set_color(YELLOW)
        x02_group=VGroup(x02_dot,x02_dot_label)
        grad2_vec=Arrow([a2,b2,0],[(-0.25*np.sin(a2/2))/(np.cos(a2/2)**(2/3))     ,-1,0],buff=0,color=ORANGE)
        grad2_label=TexMobject(r"\nabla f(x_0',y_0')").next_to(grad2_vec,DOWN+LEFT,buff=-0.3).set_color(ORANGE).scale(0.7)
        grad2=VGroup(grad2_vec,grad2_label)
    
        #Se puede moficar v2 para modificar el la longitud en x de la curva h(y)
        v2=1.3
        curva_2=ParametricFunction(
                lambda u : np.array([
                u,
                1.5*np.cos(u/2)**(1/3),
                0
            ]),color=PURPLE_E,t_min=a2-v2,t_max=a2+v2,
            )   
        curva2_label=TexMobject(r"h(y)").next_to(curva_2,RIGHT,buff=0.3).set_color(PURPLE_E).scale(0.8)
        curva2=VGroup(curva_2,curva2_label)

        #Visualicación del corolario
        curva_3=ParametricFunction(
                lambda u : np.array([
                u,
                np.cos(u**2),
                0
            ]),color=TEAL_B,t_min=-4,t_max=4,
            )   
        curva_3_nombre=TexMobject(r"f(x,y)=\cos(x^2)-y=0").set_color(TEAL_B).move_to(3.5*UP+4*LEFT).scale(0.8)
        #Se pueden modificar los parámetros x1 y x2, para cambiar donde se evalua inicialmente el gradiente, 
        #ambos valores deben ser iguales
        x1=ValueTracker(-1.5)
        x2=-1.5
        y1=np.cos(x2**2)
        punto=Dot(color=RED).move_to([x2,y1,0])
        gradiente1=Arrow([x2,y1,0],[2*x2*np.sin(x2**2)+x2,1+y1,0],buff=0,color=RED)
        #gradiente1_label=TexMobject(r"\nabla(f(x,y)=0)").set_color(RED).next_to(gradiente1,LEFT+UP,buff=-0.3).scale(0.7)
        gradiente1_label=TexMobject(r"\nabla(f(x,y))").set_color(RED).next_to(gradiente1,LEFT+UP,buff=-0.3).scale(0.7)
        def GRADIENTE(obj):
            x=x1.get_value()
            y=np.cos(x**2)
            punto.become(Dot(color=RED).move_to([x,y,0]))
            gradiente1.become(Arrow([x,y,0],[2*x*np.sin(x**2)+x,1+y,0],buff=0,color=RED))
            gradiente1_label.become(TexMobject(r"\nabla(f(x,y)=0)").set_color(RED).next_to(gradiente1,UP+RIGHT*(x/((x**2))**(1/2)),buff=-0.3).scale(0.7))
    
        punto.add_updater(GRADIENTE)
        gradiente1.add_updater(GRADIENTE)
        gradiente1_label.add_updater(GRADIENTE)

        self.set_camera_orientation(phi=0 * DEGREES,theta=-90*DEGREES,distance=200)
        self.play(ShowCreation(axes))
        self.play(ShowCreation(curva_ejem1),ShowCreation(curva_ejem1_label))
        self.acomodar_textos(text18.bg)
        self.acomodar_textos(text18)
        self.wait()
        self.play(ShowCreation(x0_group))
        self.play(ShowCreation(grad1))
        self.wait()
        self.play(ShowCreation(curva1))
        self.wait(28)
        self.play(FadeOut(curva1),FadeOut(grad1),FadeOut(x0_group),FadeOut(text18),FadeOut(text18.bg))

        self.acomodar_textos(text19.bg)
        self.acomodar_textos(text19)
        self.wait()
        self.play(ShowCreation(x02_group))
        self.play(ShowCreation(grad2))
        self.wait()
        self.play(ShowCreation(curva2))
        self.wait(25)
        self.play(FadeOut(curva2),FadeOut(grad2),FadeOut(x02_group),FadeOut(text19),FadeOut(text19.bg),FadeOut(curva_ejem1),FadeOut(curva_ejem1_label))
        self.acomodar_textos(text20.bg)
        self.acomodar_textos(text20)
        self.wait(11)
        self.play(ShowCreation(curva_3))
        self.acomodar_textos(curva_3_nombre)
        self.play(ShowCreation(punto),ShowCreation(gradiente1))
        self.add_fixed_in_frame_mobjects(gradiente1_label)
        self.wait()
        #Se puede cambiar el valor 1.5 por otro. Este permite tener el último valor donde se evalua el gradiente, debe ser mayor a x2 y x1
        self.play(x1.set_value,1.5,run_time=15)
        self.play(FadeOut(text20),FadeOut(text20.bg),FadeOut(curva_3),FadeOut(punto),FadeOut(gradiente1),FadeOut(axes),FadeOut(punto),FadeOut(curva_3_nombre),FadeOut(gradiente1_label))
        self.acomodar_textos(text21)
        self.wait(18)
        self.play(FadeOut(text21))
    def Sexta_escena(self):
        text22=TextMobject('''Veamos un ejemplo de ello.''')
        text23=TextMobject('''Considera la función ''','''$\\beta(x,y,z)=x^2+y+z$''','''.''').move_to(-1*DOWN)
        text23.set_color_by_tex_to_color_map({
            '''$\\beta(x,y,z)=x^2+y+z$''':BLUE_D
        })
        text24=TextMobject('''Como seguramente sabrás, es complicado graficar \n
                                en 4 dimensiones, así que limitémonos a graficar \n
                                    ''','''la superficie de nivel 0''','''.''').next_to(text23,DOWN,buff=0.1)
        text24.set_color_by_tex_to_color_map({
            '''la superficie de nivel 0''':GOLD_E
        })
        text24_1=TexMobject(r"\beta(x,y,z)=x^2+y+z=0").move_to(3*UP).set_color(GOLD_E)
        text24_1.bg=SurroundingRectangle(text24_1,color=WHITE,fill_color=BLACK,fill_opacity=1)
        text25=TextMobject('''Podemos describir la superficie de nivel con \n
                                la función $z=-x^2-y$.''').move_to(3*DOWN)
        text25.bg=SurroundingRectangle(text25,color=WHITE,fill_color=BLACK,fill_opacity=1)
        text26=TextMobject('''Incluso podemos expresar la superficie \n
                                    despejando la variable $y$.''').move_to(-3.3*DOWN)
        #text26=TextMobject('''Incluso podemos dejar la superficie de \n
        #                            nivel en términos de $y$.''').move_to(-3.3*DOWN)
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
        self.play(FadeOut(text24), FadeOut(text23))
        self.acomodar_textos(text24_1.bg)
        self.acomodar_textos(text24_1)
        
        self.play(ShowCreation(axes))
        self.play(ShowCreation(superficie1))
        self.begin_ambient_camera_rotation(rate=0.03)
        self.acomodar_textos(text25.bg)
        self.acomodar_textos(text25)
        self.wait(13)
        self.play(FadeOut(text25),FadeOut(text25.bg),FadeOut(text24_1),FadeOut(text24_1.bg))
        self.acomodar_textos(text26.bg)
        self.acomodar_textos(text26)
        self.wait(9)
        self.play(FadeOut(axes),FadeOut(superficie1),FadeOut(text26),FadeOut(text26.bg))
        self.acomodar_textos(text27)
        self.wait(16)
        self.play(FadeOut(text27))

    def construct(self):
        self.Primera_escena()
        self.Segunda_escena()
        self.Tercera_escena()
        self.Cuarta_escena()
        self.Quinta_escena()
        self.Sexta_escena()
