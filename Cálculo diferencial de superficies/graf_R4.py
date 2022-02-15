from manimlib.imports import *

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
        self.wait(7)
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
        self.wait(19)
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
