from mnaimlib.imports import *

###################################################
######### VECTOR PROYECCIÓN DE X SOBRE Y  #########
###################################################

class Proyeccion (ThreeDScene):

    def acomodar_textos(self,objeto):
        self.add_fixed_in_frame_mobjects(objeto)
        self.play(Write(objeto))

    def construct(self):
        grid = NumberPlane()

        #X1,X2,X3,Y1,Y2,Y3 PUEDEN MODIFICARSE PARA PROBAR CON OTROS VECTORES
        x1=0
        x2=3
        x3=0
        
        y1=1
        y2=1
        y3=2

        Vx=Arrow((0, 0, 0), x1 * RIGHT + x2*UP, buff=0,color=BLUE_C)
        Vxlabel=TexMobject("\\vec{x}").set_color(BLUE_C)
        Vxlabel.move_to(Vx.get_end()+0.5*LEFT)
        Vy=Arrow((0, 0, 0), y1 * RIGHT + y2*UP, buff=0,color=YELLOW_C)
        Vylabel=TexMobject("\\vec{y}").set_color(YELLOW_C)
        Vy1=Vy.copy()
        Vylabel.move_to(Vy.get_end()+0.5*RIGHT-0.3*UP)
        escalar=(((x1*y1)+(x2*y2))/((y1*y1)+(y2*y2)))
        vec=Arrow((0, 0, 0), (y1*escalar) * RIGHT + (y2*escalar)*UP, buff=0,
                            color=PURPLE_B)
        veclabel=TexMobject("\\vec{z}").set_color(PURPLE_B)
        veclabel.move_to(vec.get_end()+0.5*LEFT)
        linea = DashedLine((y1*escalar,y2*escalar,0),(x1,x2,0),dash_length=0.1,
        positive_space_ratio=0.5,stroke_width=3,color="#88FF00")

        escalar1=(((x1*y1)+(x2*y2))/((x1*x1)+(x2*x2)))
        vec1=Arrow((0, 0, 0), (x1*escalar1) * RIGHT + (x2*escalar1)*UP, buff=0,
                            color=RED)
        linea1 = DashedLine((x1*escalar1,x2*escalar1,0),(y1,y2,0),dash_length=0.1,
        positive_space_ratio=0.5,stroke_width=3,color=WHITE)
       

        titulo=TextMobject("Vector Proyección").scale(1.5)
        text=TextMobject('''Tomemos dos vectores en \\\\ 
                            el plano cartesiano''')
        text.bg = SurroundingRectangle(text,color=WHITE,fill_color=BLACK,fill_opacity=1)
        text.group = VGroup(text.bg,text).shift(2 * DOWN +3*LEFT)
        text1=TextMobject('''Podemos representar geométricamente\n
                            la proyección de''',''' $\\vec{x}$''',''' sobre''',''' $\\vec{y}$''',''' como''',
                            ''' $\\vec{z}$''').move_to(text.get_center()+1*RIGHT)
        text1.bg = SurroundingRectangle(text1,color=WHITE,fill_color=BLACK,fill_opacity=1)
        text1.group = VGroup(text1.bg,text1).move_to(text.get_center()+1*RIGHT)
        text1[1].set_color(BLUE_C)
        text1[3].set_color(YELLOW_C)
        text1[5].set_color(PURPLE_B)

        text2=TextMobject('''Notemos que con la sombra de ''','''$\\vec{x}$''',''' sobre la recta que \n
                            genera ''','''$\\vec{y}$''',''' obtenemos el ''','''vector proyección''','''.''')
        text2[1].set_color(BLUE_C)
        text2[3].set_color(YELLOW)
        text2[5].set_color(PURPLE_C)
        text2.bg = SurroundingRectangle(text2,color=WHITE,fill_color=BLACK,fill_opacity=1)
        text2.group = VGroup(text2.bg,text2)
        text2.group.move_to(2*DOWN)
        text3=TextMobject('''Además de que la ''','''proyección de $\\vec{y}$ sobre $\\vec{x} $''',''' \\\\
                            es diferente a la ''','''proyección de $\\vec{x}$ sobre $\\vec{y}$''')
        text3.bg = SurroundingRectangle(text3,color=WHITE,fill_color=BLACK,fill_opacity=1)
        text3.group = VGroup(text3.bg,text3)
        text3.group.move_to(-2*UP)
        text3[1].set_color(RED)
        text3[3].set_color(PURPLE_B)
        Def=TextMobject('''La ''','''proyección''',''' de ''','''$\\vec{x}$''',''' sobre\n
                            ''','''$\\vec{y}$''',''' se define como:''') #Revisar que este bien dicho
        Def[1].set_color(GREEN_D)
        Def[3].set_color(BLUE)
        Def[5].set_color(YELLOW)
        Def_copy=Def.copy()
        Def_copy.move_to(2.5*UP)
        Def1=TextMobject('''$Proy_{\\vec{y}}(\\vec{x}):=\\frac{\\vec{x}\\cdot\\vec{y}}{\\vec{y}\\cdot\\vec{y}} \\vec{y}$''')
        Def1[0][0].set_color(GREEN_D)
        Def1[0][1].set_color(GREEN_D)
        Def1[0][2].set_color(GREEN_D)
        Def1[0][3].set_color(GREEN_D)
        Def1_1=Def1.copy().move_to(2.5*UP)
        text4=TextMobject('''Veamos un último ejemplo, agregándole una coordenada \n
                                en ''','''z''',''' a los vectores anteriores''')
        text4[1].set_color(PURPLE_B)
                                
        #Animacion2d
        self.play(Write(titulo))
        self.wait()
        self.play(FadeOut(titulo))
        self.play(Write(grid))
        self.wait()
        self.play(Write(text.group))
        self.play(ShowCreation(Vx),Write(Vxlabel))
        self.play(ShowCreation(Vy),Write(Vylabel))
        self.wait(2)
        self.play(ReplacementTransform(text.group,text1.group))
        self.wait()
        self.play(ShowCreation(linea))
        self.wait(2)
        self.play(ShowCreation(vec),Write(veclabel))
        self.wait()
        self.play(ReplacementTransform(text1.group,text2.group))
        self.wait(7)
        self.play(ReplacementTransform(text2.group,text3.group))
        self.play(ReplacementTransform(linea,linea1),FadeIn(Vy1))
        self.play(ShowCreation(vec1))
        self.wait(2)
        self.play(FadeOut(Vx),FadeOut(Vy),FadeOut(linea1),
                  FadeOut(Vxlabel),FadeOut(Vylabel),FadeOut(veclabel),FadeOut(Vy1))
        self.wait()
        self.play(FadeOut(grid),FadeOut(text3.group),
                 FadeOut(vec),FadeOut(vec1)
        )
        self.wait()
        self.play(Write(Def))
        self.wait(3)
        self.play(ReplacementTransform(Def,Def_copy))
        self.play(Write(Def1))
        self.wait(3.5)
        self.play(FadeOut(Def_copy))
        self.wait()
        self.play(ReplacementTransform(Def1,Def1_1))
        self.play(Write(text4))
        self.wait(5)
        self.play(FadeOut(text4),FadeOut(Def1_1))
        self.wait()
        
        
        #CÓDIGO PARA LA ANIMACION 3D
        axes = ThreeDAxes()

        Vx3d=Arrow((0, 0, 0), x1 * RIGHT + x2*UP+x3*OUT,buff=0,color=BLUE)
        Vx3dlabel=TexMobject("\\vec{x}",color=BLUE_C)
        Vx3dlabel.move_to(3*UP+5*LEFT)
        #Vy3d=Arrow((0, 0, 0), y1 * RIGHT + y2*UP+y3*OUT,buff=0,color=YELLOW)
        Vy3d=Line((0, 0, 0), y1 * RIGHT + y2*UP+y3*OUT,buff=0,color=YELLOW)

        Vy3da = ArrowTip(start_angle=Vy3d.get_angle(), color=YELLOW).move_to(y1 * RIGHT + y2*UP+y3*OUT)

        Vy3d.group = VGroup(Vy3d,Vy3da)

        Vy3dlabel=TexMobject("\\vec{y}",color=YELLOW)
        Vy3dlabel.move_to(2.5*UP+5*LEFT)
        Plabel=TextMobject('''Proyección''',''' de $\\vec{y}$ \n
                            sobre $\\vec{x}$''').shift(0.25*DOWN)
        Plabel[0].set_color(RED)
        Plabel.move_to(1.7*UP+5*LEFT)
        escalar3d=(((x1*y1)+(x2*y2)+(x3*y3))/((x1*x1)+(x2*x2)+(x3*x3)))
        vec3d=Arrow((0, 0, 0), (x1*escalar3d) * RIGHT + (x2*escalar3d)*UP+((x3*escalar3d))*OUT,buff=0,color=RED)
        linea3d = DashedLine((y1,y2,y3),(x1*escalar3d,x2*escalar3d,x3*escalar3d),dash_length=0.1,
        positive_space_ratio=0.5,stroke_width=3,color="#88FF00")
        text5=TextMobject('''Modifica el código para probar con nuevos vectores \n
                             y perspectivas en la animación en $\\mathbb{R}^{3}$''')

        #Se puede cambiar la siguiente linea para modificar la posición de la camara
        self.set_camera_orientation(phi=80 * DEGREES,theta=45*DEGREES,distance=6)           
        self.play(ShowCreation(axes)) 
        self.play(ShowCreation(Vx3d),run_time=0.75)
        self.acomodar_textos(Vx3dlabel)
        #self.add_fixed_in_frame_mobjects(Vx3dlabel)
        self.play(ShowCreation(Vy3d.group),run_time=0.75)
        self.acomodar_textos(Vy3dlabel)
        #self.add_fixed_in_frame_mobjects(Vy3dlabel)
        self.play(ShowCreation(linea3d))
        self.play(ShowCreation(vec3d))
        self.acomodar_textos(Plabel)
        #self.add_fixed_in_frame_mobjects(Plabel)
        #inicia movimiento de la camara, se puede cambiar la velocidad con rate
        self.begin_ambient_camera_rotation(rate=0.5)
        self.wait(4)
        self.play(FadeOut(axes),FadeOut(Vy3d.group),FadeOut(Vx3d),
                    FadeOut(Vy3dlabel),FadeOut(Vx3dlabel),
                    FadeOut(Plabel),FadeOut(vec3d),FadeOut(linea3d))
        self.add_fixed_in_frame_mobjects(text5)
        
        self.wait(2)
        self.play(FadeOut(text5))