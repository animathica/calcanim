from manimlib.imports import *

##################################################################
#################### Máximos y Mínimos ##########################
##################################################################

class maximos_minimos (ThreeDScene, Scene):
    def setup(self):
        Scene.setup(self)
        ThreeDScene.setup(self)
    def FadeOutWrite3D(self,objeto1,objeto2):
        self.play(FadeOut(objeto1))
        self.acomodar_textos(objeto2)
    def acomodar_textos(self,objeto):
        self.add_fixed_in_frame_mobjects(objeto)
        self.play(Write(objeto))
    def punto3D(self):
        bola = ParametricSurface(
            lambda u, v: np.array([
                0.075*np.cos(v) * np.sin(u),
            0.075*np.sin(v) * np.sin(u),
            0.075*np.cos(u)
            ]),v_min=0,v_max=TAU,u_min=0.001,u_max=PI-0.001,
            resolution=(24,24),fill_opacity=1,stroke_color=RED,fill_color=RED)
        return bola
    def get_vector_field(self,campo):
            self.vector_field = VectorField(
                campo,
                #Ajuste de propiedades del campo:
                x_min=-3,
                x_max=3,
                y_min=-2,
                y_max=2,
                delta_x=0.25,
                delta_y=0.25,
                # length_func=linear,
                length_func=lambda norm: 0.5 * sigmoid(norm),
                colors=[GREEN],
            )
            return self.vector_field
    def superficie(self):
        superficie = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                u**3-v**3+3*u*v
            ]),v_min=-2,v_max=1.5,u_min=-1.5,u_max=2,fill_color=PURPLE_E,fill_opacity=0.75,
            resolution=(30, 30))
        return superficie
    def superficie2(self):
        superficie = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                u**4+v**4
            ]),v_min=-1.4,v_max=1.4,u_min=-1.4,u_max=1.4,fill_color=PURPLE_E,fill_opacity=0.75,
            resolution=(30, 30))
        return superficie
    
    def PrimeraEscena(self):
        titulo = TextMobject('''Matriz hessiana\n
                                y puntos críticos''').scale(1.5)
        texto_1 = TextMobject("Consideremos la siguiente función").move_to(UP)
        texto_2_1 = TexMobject(r"f:\mathbb{R}^2\to\mathbb{R}").next_to(texto_1, DOWN)
        texto_2_2 = TexMobject(r"f(x,y)=x^3-y^3+3xy").next_to(texto_2_1, DOWN)
        texto_2 = VGroup(texto_2_1,texto_2_2)
        texto_3 = TextMobject("La gráfica de $f$ es una superficie en $\mathbb{R}^3$").move_to(UP)

        #Objetos
        axes = ThreeDAxes(x_min=-2.5,x_max=2.5,y_min=-2.5,y_max=2.5,z_min=-1,z_max=3,num_axis_pieces= 30)
        superficie = self.superficie()

        #Animaciones
        self.play(Write(titulo))
        self.wait(3)
        self.FadeOutWrite3D(titulo,texto_1)
        self.wait(3)
        self.play(Write(texto_2))
        self.wait(5)
        self.play(FadeOut(texto_1))
        self.play(Write(texto_3))
        self.wait(5)
        self.play(FadeOut(texto_2_1),FadeOut(texto_3))
        self.play(
            texto_2_2.shift,+4.3*LEFT
        )
        self.add_fixed_in_frame_mobjects(texto_2_2)
        self.wait(0.5)
        self.move_camera(phi=70 * DEGREES,theta=120*DEGREES,frame_center=(0,0,1))
        self.play(ShowCreation(axes))
        self.play(ShowCreation(superficie))
        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(4)
        self.stop_ambient_camera_rotation()
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
        self.move_camera(phi=0,theta=-90*DEGREES,frame_center=(0,0,0))
    
    def SegundaEscena(self):
        texto_1 = TextMobject("Consideremos el campo gradiente de la función $f$").move_to(UP)
        texto_2_1 = TexMobject(r"\nabla f:\mathbb{R}^2\to\mathbb{R}^2").next_to(texto_1, DOWN)
        texto_2_2 = TexMobject(r"\nabla f(x,y)=(3y+3x^2,3x-3y^2)").next_to(texto_2_1, DOWN)
        texto_2_2_copy = texto_2_2.copy().move_to(3*DOWN)
        texto_2_2.bg = SurroundingRectangle(
            texto_2_2_copy, color=WHITE, fill_color=BLACK, fill_opacity=1
        )
        caja_texto_2_2 = VGroup(texto_2_2.bg,texto_2_2_copy)
        texto_2 = VGroup(texto_2_1,texto_2_2)
        texto_3 = TextMobject('''Se dice que un punto $(x_0,y_0)$ del dominio de $f$ \n
                                es un punto crítico si $\\nabla f(x_0,y_0)=\\Vec{0}$''').move_to(3*UP)
        texto_3.bg = SurroundingRectangle(
            texto_3, color=WHITE, fill_color=BLACK, fill_opacity=1
        )
        caja_texto_3 = VGroup(texto_3.bg, texto_3)
        texto_4 = TextMobject("Es decir, si sus derivadas parciales son igual a cero").move_to(3*UP)
        texto_4.bg = SurroundingRectangle(
            texto_4, color=WHITE, fill_color=BLACK, fill_opacity=1
        )
        caja_texto_4 = VGroup(texto_4.bg, texto_4)
        texto_5 = TextMobject("En el ejemplo, el punto $(0,0)$ es un punto crítico de $f$").move_to(3*UP)
        texto_5.bg = SurroundingRectangle(
            texto_5, color=WHITE, fill_color=BLACK, fill_opacity=1
        )
        caja_texto_5 = VGroup(texto_5.bg, texto_5)
        
        #Objetos

        axes = NumberPlane(
            x_min = -3.5,
            x_max = 3.5,
            y_min = -2.5,
            y_max = 2.5
        )
        punto_critico = Dot(color=RED)

        #Campo Gradiente de f
        def campo(point):
            x, y = point[:2]
            return (3*y+3*x**2) * RIGHT + (3*x-3*y**2) * UP
        campo = self.get_vector_field(campo)

        #Animacion
        self.play(Write(texto_1))
        self.wait(5)
        self.play(Write(texto_2))
        self.wait(8)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
        self.play(ShowCreation(axes))
        self.play(ShowCreation(campo))
        self.play(ShowCreation(caja_texto_2_2))
        self.wait(4)
        self.play(ShowCreation(caja_texto_3))
        self.wait(9)
        self.play(FadeOut(caja_texto_3))
        self.play(ShowCreation(caja_texto_4))
        self.wait(6)
        self.play(FadeOut(caja_texto_4))
        self.play(ShowCreation(caja_texto_5))
        self.wait(7)
        self.play(FadeIn(punto_critico))
        self.wait(2)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
    
    def TercerEscena(self):
        texto_1 = TextMobject(''' Ahora aproximamos el campo gradiente de $f$ alrededor \n
                                 de $(0,0)$, utilizando su derivada $D(\\nabla f)$ ''')
        texto_2 = TextMobject(''' La matriz asociada a $D(\\nabla f)$ se llama matriz hessiana.\n
                                  Definimos entonces $H_f(x,y)=D(\\nabla f)(x,y)$''')
        texto_3 = TextMobject("En el ejemplo,").move_to(1.5*UP)
        texto_4 = TexMobject(r""" H_f(x,y)= \begin{pmatrix} 6x & 3 \\ 3 & -6y \end{pmatrix} """)
        texto_5 = TextMobject("En particular sobre el punto $(0,0)$,").move_to(1.5*UP)
        texto_6 = TexMobject(r""" H_f(0,0)= \begin{pmatrix} 0 & 3 \\ 3 & 0 \end{pmatrix}, """)
        texto_6_1 = TextMobject("donde $\\text{det}(H_f(0,0))< 0$").move_to(1.5*DOWN)
        texto_7 = TextMobject("Veamos cómo la hessiana aproxima al campo gradiente de $f$")
        texto_7_1 = TexMobject(r"H_f(0,0)\begin{pmatrix} x \\ y \end{pmatrix}=\begin{pmatrix} 3y \\ 3x \end{pmatrix}").move_to(3*DOWN)
        texto_7_1.bg = SurroundingRectangle(
            texto_7_1, color=WHITE, fill_color=BLACK, fill_opacity=1
        )
        caja_texto_7_1 = VGroup(texto_7_1.bg, texto_7_1)
        texto_8 = TextMobject("Como $f\\in C^2$, $\\nabla f\\in C^1$ y $\\text{det}(H_f(0,0))\\neq 0$").move_to(3*UP)
        texto_8.bg = SurroundingRectangle(
            texto_8, color=WHITE, fill_color=BLACK, fill_opacity=1
        )
        caja_texto_8 = VGroup(texto_8.bg, texto_8)
        texto_9 = TextMobject(''' a partir de la hessiana podemos conocer el comportamiento \n 
                                cualitativo de $\\nabla f$ alrededor del punto crítico $(0,0)$ ''').move_to(3*UP)
        texto_9.bg = SurroundingRectangle(
            texto_9, color=WHITE, fill_color=BLACK, fill_opacity=1
        )
        caja_texto_9 = VGroup(texto_9.bg, texto_9) 
        texto_10 = TextMobject('''En el ejemplo, el campo gradiente y el campo de la Hessiana \n
                                  en el origen, tienen un punto silla en el origen, es decir, \n
                                  cerca del origen hay flechas que apuntan hacia él pero \n
                                  también flechas que se alejan de él''').scale(0.8).to_edge(UP)
        texto_10.bg = SurroundingRectangle(
            texto_10, color=WHITE, fill_color=BLACK, fill_opacity=1
        )
        caja_texto_10 = VGroup(texto_10.bg,texto_10)
        texto_11 = TextMobject('''Las flechas que están sobre la recta menos identidad y \n
                                  cerca del origen, apuntan hacia el origen para ambos \n 
                                  campos, esto es como en una singularidad estable.''').scale(0.8).to_edge(UP)
        texto_11.bg = SurroundingRectangle(
            texto_11, color=WHITE, fill_color=BLACK, fill_opacity=1
        )
        caja_texto_11 = VGroup(texto_11.bg,texto_11)
        texto_12 = TextMobject('''Mientras que, cerca del origen, sobre la recta identidad \n
                                  las flechas siempre se alejan del origen, es decir, es \n
                                  como una singularidad inestable.''').scale(0.8).to_edge(UP)
        texto_12.bg = SurroundingRectangle(
            texto_12, color=WHITE, fill_color=BLACK, fill_opacity=1
        )
        caja_texto_12 = VGroup(texto_12.bg,texto_12)
        texto_13 = TextMobject('''Por esto es que se conluye que en el origen hay \n
                                  un punto silla.''').to_edge(UP)
        texto_13.bg = SurroundingRectangle(
            texto_13, color=WHITE, fill_color=BLACK, fill_opacity=1
        )
        caja_texto_13 = VGroup(texto_13.bg,texto_13)
        #Objetos
        # Ejes gradiente
        axes = NumberPlane(
            x_min = -3.5,
            x_max = 3.5,
            y_min = -2.5,
            y_max = 2.5
        )\
            .scale(0.85)\
            .move_to(3.5*LEFT)
        # Ejes aprox Hessiana
        axes2 = NumberPlane(
            x_min = -3.5,
            x_max = 3.5,
            y_min = -2.5,
            y_max = 2.5
        )\
            .scale(0.85)\
            .move_to(3.5*RIGHT)
        # Campo gradiente
        def campo_grad(point):
            x, y = point[:2]
            return (3*y+3*x**2) * RIGHT + (3*x-3*y**2) * UP
        campograd = self.get_vector_field(campo_grad)\
            .scale(0.85)\
            .move_to(3.5*LEFT)
        label1 = TextMobject('''Campo \n 
                                gradiente''',color=BLUE).scale(0.6)
        label1.bg = SurroundingRectangle(label1,color=WHITE,fill_color=BLACK,fill_opacity=1)
        label1_caja = VGroup(label1.bg,label1).move_to((-4,-2.5,0))
        # Campo Gradiente de f aproximado por hessiana
        def campo(point):
            x, y = point[:2]
            return 3*y * RIGHT + 3*x * UP
        campo = self.get_vector_field(campo)\
            .scale(0.85)\
            .move_to(3.5*RIGHT)
        label2 = TextMobject('''Campo de la \n 
                                Hessiana''',color=BLUE).scale(0.6)
        label2.bg = SurroundingRectangle(label2,color=WHITE,fill_color=BLACK,fill_opacity=1)
        label2_caja = VGroup(label2.bg,label2).move_to((4,-2.5,0))

        identidad = ParametricFunction(
            lambda t : np.array([t,t,0]),
            t_min = -2,
            t_max = 2,
            color = YELLOW
        )
        menos_identidad = ParametricFunction(
            lambda t : np.array([t,-t,0]),
            t_min = -2,
            t_max = 2,
            color = RED
        )
        identidad2 = ParametricFunction(
            lambda t : np.array([t,t,0]),
            t_min = -2,
            t_max = 2,
            color = YELLOW
        )
        menos_identidad2 = ParametricFunction(
            lambda t : np.array([t,-t,0]),
            t_min = -2,
            t_max = 2,
            color = RED
        )
        identidad.scale(0.85).move_to(3.5*LEFT)
        menos_identidad.scale(0.85).move_to(3.5*LEFT)
        identidad2.scale(0.85).move_to(3.5*RIGHT)
        menos_identidad2.scale(0.85).move_to(3.5*RIGHT)
        rectas = VGroup(identidad,identidad2,menos_identidad,menos_identidad2)
        
        #Animacion
        self.play(Write(texto_1))
        self.wait(7)
        self.FadeOutWrite3D(texto_1,texto_2)
        self.wait(5)
        self.FadeOutWrite3D(texto_2,texto_3)
        self.wait(5)
        self.play(Write(texto_4))
        self.wait(2)
        self.FadeOutWrite3D(texto_3,texto_5)
        self.wait(4)
        self.play(ReplacementTransform(texto_4,texto_6))
        self.wait(4)
        self.play(Write(texto_6_1))
        self.wait(4)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
        self.play(Write(texto_7))
        self.wait(5)
        self.play(FadeOut(texto_7))
        self.play(ShowCreation(axes),ShowCreation(axes2))
        self.play(ShowCreation(campo),ShowCreation(campograd),Write(label1_caja),Write(label2_caja))
        self.play(ShowCreation(caja_texto_7_1))
        self.wait(3)
        self.play(ShowCreation(caja_texto_8))
        self.wait(7)
        self.play(FadeOut(caja_texto_8))
        self.play(ShowCreation(caja_texto_9))
        self.wait(9)
        self.play(FadeOut(caja_texto_9))
        self.play(ShowCreation(caja_texto_10))
        self.play(Write(rectas))
        self.wait(10)
        self.play(FadeOut(caja_texto_10))
        self.play(ShowCreation(caja_texto_11))
        self.wait(10)
        self.play(FadeOut(caja_texto_11))
        self.play(ShowCreation(caja_texto_12))
        self.wait(10)
        self.play(FadeOut(caja_texto_12))
        self.play(ShowCreation(caja_texto_13))
        self.wait(5)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
    
    def CuartaEscena (self):
        texto_1 = TextMobject(''' En este caso $\\text{det}(H_f(0,0))< 0$, por lo tanto,\n
                                     el punto $(0,0)$ es un punto silla de $f$ ''').move_to(3*UP)
        texto_1.bg = SurroundingRectangle(
            texto_1, color=WHITE, fill_color=BLACK, fill_opacity=1
        )
        caja_texto_1 = VGroup(texto_1.bg, texto_1)                             
        texto_2 = TextMobject(''' En general, dado un campo escalar $f:A\\subset\\mathbb{R}^2\\to\\mathbb{R}$ de \n
                                 clase $C^2$,  con un punto crítico $\\Vec{x_0}$ en el interior de $A$ y \n
                                $H_f(\\Vec{x_0})$ la matriz hessiana en $\\Vec{x_0}$,''').move_to(2*UP)
        texto_3 = TextMobject(''' i) Si $\\text{det}(H_f(\\Vec{x_0}))< 0$, $\\Vec{x_0}$ es un punto silla''').next_to(texto_2,1.5*DOWN)
        texto_4 = TextMobject(''' ii) Si $\\text{det}(H_f(\\Vec{x_0}))> 0$ y $\dfrac{\\partial^2 f}{\\partial x^2}(\\Vec{x_0})>0$, $f(x_0)$ es un mínimo local''').next_to(texto_3,1*DOWN)                       
        texto_5 = TextMobject(''' iii) Si $\\text{det}(H_f(\\Vec{x_0}))> 0$ y $\dfrac{\\partial^2 f}{\\partial x^2}(\\Vec{x_0})<0$, $f(x_0)$ es un máximo local''').next_to(texto_4,1*DOWN)          
        texto_6 = TextMobject(''' iv) Si $\\text{det}(H_f(\\Vec{x_0}))= 0$, este criterio no es aplicable''').next_to(texto_5,1*DOWN)          

        #Objetos
        axes = ThreeDAxes(x_min=-2.5,x_max=2.5,y_min=-2.5,y_max=2.5,z_min=-1,z_max=3,num_axis_pieces= 30)
        superficie = self.superficie()
        punto = self.punto3D()

        #Animacion
        self.move_camera(phi=70 * DEGREES,theta=120*DEGREES,frame_center=(0,0,1))
        self.play(ShowCreation(axes))
        self.play(ShowCreation(superficie))
        self.wait()
        self.play(FadeIn(punto))
        self.acomodar_textos(caja_texto_1)
        self.wait(8)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
        self.move_camera(phi=0,theta=-90*DEGREES,frame_center=(0,0,0))
        self.play(Write(texto_2))
        self.wait(12)
        self.play(Write(texto_3))
        self.wait(5)
        self.play(Write(texto_4))
        self.wait(7)
        self.play(Write(texto_5))
        self.wait(7)
        self.play(Write(texto_6))
        self.wait(5)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
    
    def QuintaEscena (self):
        texto_1 = TextMobject(''' Ahora consideremos una superficie dada por \n
                                la gráfica de la siguiente función ''').move_to(1.5*UP)
        texto_2_1 = TexMobject(r"f:\mathbb{R}^2\to\mathbb{R}")
        texto_2_2 = TexMobject(r"f(x,y)=x^4+y^4").next_to(texto_2_1,DOWN)
        texto_2 = VGroup(texto_2_1, texto_2_2)
        texto_3 = TextMobject(''' Podemos obtener el campo gradiente, así como\n
                             la matriz hessiana de la función $f$''').move_to(1.5*UP)
        texto_4 = TexMobject(r"\nabla f(x,y)=(4x^3,4y^3)")
        texto_5 = TexMobject(r""" H_f(x,y)= \begin{pmatrix} 12x^2 & 0 \\ 0 & 12y^2 \end{pmatrix} """).next_to(texto_4,DOWN)
        texto_6 = TextMobject(''' Obsérvese que en el punto $(0,0)$ \n 
                                hay un punto crítico de $f$ ''').move_to(1.5*UP)
        texto_7 = TextMobject(''' Pero en $(0,0)$ la hessiana se vuelve ''').move_to(1.5*UP)
        texto_8 = TexMobject(r""" H_f(0,0)= \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix} """).next_to(texto_4,DOWN)
        texto_9 = TextMobject(''' En este caso la matriz hessiana no nos permite clasificar el \n
                                punto crítico, por lo tanto el criterio no es siempre aplicable. ''')
        #Objetos
        axes = ThreeDAxes(x_min=-2.5,x_max=2.5,y_min=-2.5,y_max=2.5,z_min=-1,z_max=3,num_axis_pieces= 30)
        superficie = self.superficie2()
        #Animacion
        self.play(Write(texto_1))
        self.wait(6)
        self.play(Write(texto_2))
        self.wait(5)
        self.play(FadeOut(texto_2_1),FadeOut(texto_1))
        self.play(
            texto_2_2.shift,+4*LEFT+1.5*UP
        )
        self.add_fixed_in_frame_mobjects(texto_2_2)
        self.wait(0.5)
        self.move_camera(phi=85 * DEGREES,theta=120*DEGREES,frame_center=(0,0,1))
        self.play(ShowCreation(axes))
        self.play(ShowCreation(superficie))
        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(4)
        self.stop_ambient_camera_rotation()
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
        self.move_camera(phi=0,theta=-90*DEGREES,frame_center=(0,0,0))
        self.play(Write(texto_3))
        self.wait(7)
        self.play(Write(texto_4))
        self.wait(6)
        self.play(Write(texto_5))
        self.wait(6)
        self.play(FadeOut(texto_3))
        self.play(Write(texto_6))
        self.wait(6)
        self.play(FadeOut(texto_6))
        self.play(Write(texto_7))
        self.wait(3)
        self.play(ReplacementTransform(texto_5,texto_8))
        self.wait(2)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
        self.play(Write(texto_9))
        self.wait(9)
        self.play(FadeOut(texto_9))
    
    def construct(self):
        self.PrimeraEscena()
        self.SegundaEscena()
        self.TercerEscena()
        self.CuartaEscena()
        self.QuintaEscena()
