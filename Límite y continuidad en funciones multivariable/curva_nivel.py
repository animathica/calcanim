from manimlib.imports import *

#############################
###CONJUNTO DE NIVEL EN R3###
#############################
class ConjNiv_R3(ThreeDScene,Scene):
    def setup(self):
        Scene.setup(self)
        ThreeDScene.setup(self)
        
    def construct(self):

        text_1 = TextMobject("Veamos ahora los conjuntos de nivel de", " $f(x,y) = \\sqrt{x^2+y^2}$").to_edge(DOWN).set_opacity(0)
        text_1[1].set_color(GOLD_E)
        text_1.scale(0.9)

        # Creamos la superficie con f(x,y) = \\sqrt(x^2+y^2)
        superficie = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                np.sqrt(u**2+v**2)
            ]),v_min=-3,v_max=3,u_min=-3,u_max=3,fill_opacity=0.75,checkerboard_colors=[GOLD_E,GOLD_E],
            resolution=(80, 80))

        text_2 = TextMobject("Consideremos", " $c=2$").to_edge(DOWN).set_opacity(0)
        text_2[1].set_color(RED)
        text_3 = TextMobject("Este conjunto estará contenido en $\mathbb{R}^2$").to_edge(DOWN).set_opacity(0)

        #CREAMOS EL PLANO Z=2
        plano_1 = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                2
            ]),v_min=-3,v_max=3,u_min=-3,u_max=3,fill_color=RED,fill_opacity=0.7, checkerboard_colors=[RED,RED],
            resolution=(60, 60))
        
        #EL CONJUNTO DE NIVEL PARA C=2
        circulo_niv2= ParametricFunction(
                lambda u : np.array([
                2*math.cos(u),
                2*math.sin(u),
                2
            ]),color=WHITE,t_min=0,t_max=2*PI,
            )
        
        circulo_niv2_dup= ParametricFunction(
                lambda u : np.array([
                2*math.cos(u),
                2*math.sin(u),
                2
            ]),color=WHITE,t_min=0,t_max=2*PI,
            )

        circulo_niv2_R2= ParametricFunction(
                lambda u : np.array([
                2*math.cos(u),
                2*math.sin(u),
                0
            ]),color=WHITE,t_min=0,t_max=2*PI,
            )  

        conjunto_nivel2 = TexMobject(r"N_2(f) = \{ \vec{x} \in \mathbb{R}^2 \vert \Vert \vec{x} \Vert = 2 \}").shift(2*UP+3*RIGHT).scale(0.7)
        conjunto_nivel2_short = TexMobject(r"N_2(f)").shift(1.75*UP+1.75*RIGHT).scale(0.6)
        text_4 = TextMobject("Repitamos lo anterior ahora con ", "$c = 1$").to_edge(DOWN).set_opacity(0)
        text_4[1].set_color(RED)

        plano_2 = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                1
            ]),v_min=-3,v_max=3,u_min=-3,u_max=3,fill_color=RED,fill_opacity=0.5, checkerboard_colors=[RED,RED],
            resolution=(60, 60))

        circulo_niv1= ParametricFunction(
                lambda u : np.array([
                1*math.cos(u),
                1*math.sin(u),
                1
            ]),color=WHITE,t_min=0,t_max=2*PI,
            )
        circulo_niv1_dup= ParametricFunction(
                lambda u : np.array([
                1*math.cos(u),
                1*math.sin(u),
                1
            ]),color=WHITE,t_min=0,t_max=2*PI,
            )

        circulo_niv1_R2= ParametricFunction(
                lambda u : np.array([
                1*math.cos(u),
                1*math.sin(u),
                0
            ]),color=WHITE,t_min=0,t_max=2*PI,
            )  

        conjunto_nivel1 = TexMobject(r"N_1(f) = \{ \vec{x} \in \mathbb{R}^2 \vert \Vert \vec{x} \Vert = 1 \}").shift(2*DOWN+3*RIGHT).scale(0.7)
        conjunto_nivel1_short = TexMobject(r"N_1(f)").shift(UP+RIGHT).scale(0.6)
        text_5 = TextMobject("¡Los conjuntos de nivel nos ayudan a esbozar la gráfica!").to_edge(DOWN).set_opacity(0).scale(0.8)

        ## Secuencia de la Animación
        axes = ThreeDAxes(x_min=-4,x_max=4,y_min=-4,y_max=4,z_min=-2,z_max=4,num_axis_pieces=40)
        self.set_camera_orientation(phi=75 * DEGREES,theta=-45*DEGREES,distance=100)
        self.add_fixed_in_frame_mobjects(text_1)
        self.play(text_1.set_opacity, 1, runtime  = 2)
        self.play(ShowCreation(axes))
        self.play(ShowCreation(superficie))
        self.wait(5.5)

        #PLANO 1
        self.play(FadeOut(text_1))
        self.add_fixed_in_frame_mobjects(text_2)
        self.play(text_2.set_opacity, 1, runtime  = 2)
        self.play(ShowCreation(plano_1))
        self.wait(2)
        self.move_camera(phi=90 * DEGREES,theta=-90*DEGREES,frame_center=(0.1,0,1))

        self.play(FadeOut(text_2))
        self.add_fixed_in_frame_mobjects(text_3)
        self.play(text_3.set_opacity, 1, runtime  = 2)
        self.wait(4)

        #CONJUNTO DE NIVEL
        self.play(FadeOut(text_3))
        self.move_camera(phi= 0 * DEGREES,theta=-90*DEGREES,run_time=2)
        self.play(ShowCreation(circulo_niv2), runtime = 2)

        self.move_camera(phi=75 * DEGREES,theta=-45*DEGREES,distance=100,run_time=2)
        self.play(ReplacementTransform(circulo_niv2_dup, circulo_niv2_R2))
        self.add_foreground_mobjects(superficie)
        self.play(Write(conjunto_nivel2))

        self.play(FadeOut(superficie), FadeOut(plano_1), FadeOut(circulo_niv2),FadeOut(circulo_niv2_dup))
        self.move_camera(phi= 0 * DEGREES,theta=-90*DEGREES,run_time=2)
        self.wait(5.5)
        self.play(ReplacementTransform(conjunto_nivel2,conjunto_nivel2_short))


        self.move_camera(phi=75 * DEGREES,theta=-45*DEGREES,distance=100, run_time=2)
        self.play(ShowCreation(superficie))
        self.add_fixed_in_frame_mobjects(text_4)
        self.play(text_4.set_opacity, 1, runtime  = 2)
        self.play(ShowCreation(plano_2))
        self.wait(4)
        self.play(FadeOut(text_4))
        self.move_camera(phi= 0 * DEGREES,theta=-90*DEGREES,run_time=3)
        self.play(ShowCreation(circulo_niv1), runtime = 2)
        self.wait()
        self.move_camera(phi=75 * DEGREES,theta=-45*DEGREES,distance=100,run_time=3)
        self.play(ReplacementTransform(circulo_niv1_dup, circulo_niv1_R2))

        self.play(FadeOut(superficie), FadeOut(plano_2), FadeOut(circulo_niv1),FadeOut(circulo_niv1_dup))
        self.move_camera(phi= 0 * DEGREES,theta=-90*DEGREES,run_time=3)
        self.play(Write(conjunto_nivel1_short))
        self.wait(4)

        self.move_camera(phi=75 * DEGREES,theta=-45*DEGREES,distance=100,run_time=3)
        self.play(ShowCreation(superficie),ShowCreation(circulo_niv1),ShowCreation(circulo_niv2))

        self.add_fixed_in_frame_mobjects(text_5)
        self.play(text_5.set_opacity, 1, runtime  = 2)
        self.wait(4)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
        self.wait(2)