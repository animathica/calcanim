from manimlib.imports import *

class TeoFubini(ThreeDScene):
    def parte1(self):
        title = TextMobject("Teorema de Fubini")
        t1 = TextMobject('''La mayoría de nosotros hemos calculado volúmenes \n
                            utilizando fórmulas geométricas básicas.''')
        t2 = TextMobject('''El volumen de un prisma rectangular, por \n
                            ejemplo, se puede calcular multiplicando la \n
                            longitud, el ancho y la altura.''')
        t3 = TextMobject('''Seguramente, son familiares las fórmulas para \n
                            hallar el volumen de una esfera, un cono o \n
                            una pirámide''').shift(2*UP)
        t4 = TextMobject('''Aunque algunas de estas fórmulas se obtuvieron \n
                            utilizando solo geometría, todas se pueden \n
                            obtener mediante integración.''')
        t5 = TextMobject('''Para facilitar el cálculo del volumen bajo \n
                            una función determinada, existen resultados que \n
                            permiten calcular las integrales de varias \n
                            variables mediante varias integrales de funciones \n
                            de una variable.''')
        t6 = TextMobject('''Uno de estos resultados es el corolario de un \n
                            conocido teorema, el teorema de Fubini.''')

        a1 = TexMobject(r"V=\frac{4}{3}\pi r^3",color=BLUE).scale(0.7)
        a2 = TexMobject(r"V=\frac{1}{3}\pi r^2h",color=RED).scale(0.7)
        a3 = TexMobject(r"V=\frac{1}{3}Ah",color=YELLOW).scale(0.7)

        # Para los SVG cambiar la ruta, los SVG están en la misma carpeta que este codigo
        esf = Sphere(radius=1.5,fill_opacity=0.6).shift(3.5*LEFT+1*DOWN)
        con = SVGMobject("C:\manim\manim-master\manim-master\Cono.svg",color=WHITE,fill_color=RED).shift(1.5*DOWN).scale(1.5)
        pir = SVGMobject("C:\manim\manim-master\manim-master\Basic_pyramid.svg",color=WHITE,fill_color=YELLOW).shift(3.5*RIGHT+1*DOWN).scale(1.5)

        a1.next_to(esf,DOWN)
        a2.next_to(con,DOWN)
        a3.next_to(pir,DOWN)

        self.write_wait_fade(title)
        self.write_wait_fade(t1,3)
        self.write_wait_fade(t2,4)
        self.play(Write(t3))
        self.play(DrawBorderThenFill(esf),Write(a1))
        self.play(DrawBorderThenFill(con),Write(a2))
        self.play(DrawBorderThenFill(pir),Write(a3))
        self.wait()
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.write_wait_fade(t4,3)
        self.write_wait_fade(t5,5)
        self.write_wait_fade(t6,3)

    def parte2(self):
        t1 = TextMobject('''Considerando $R\\subset\\mathbb{R}^2$ un rectángulo descompuesto \n
                            como producto cartesiano de dos intervalos $A_1=[a,b]$ \n
                            y $A_2=[c,d]$, es decir, $R=A_1\\times A_2$''').scale(0.8)
        t2 = TextMobject('''Y $f:R\\to\\mathbb{R}$ una función continua e integrable, el corolario \n
                            del Teorema de Fubini asegura que''').shift(UP)
        t3 = TexMobject(r"\int\int_R f=\int_a^b\int_c^d f(x,y)dydx=\int_c^d\int_a^b f(x,y)dxdy").next_to(t2,DOWN)

        centro = np.array([-3.5,-2.75,0])
        a = np.array([2,0,0])
        a_label = TexMobject("a").move_to(a+centro).shift(0.3*DOWN)
        b = np.array([5,0,0])
        b_label = TexMobject("b").move_to(b+centro).shift(0.3*DOWN)
        c = np.array([0,2,0])
        c_label = TexMobject("c").move_to(c+centro+0.3*LEFT)
        d = np.array([0,3.5,0])
        d_label = TexMobject("d").move_to(d+centro+0.3*LEFT)
        rect = Rectangle(height=1.5,width=3,color=RED,fill_color=RED,fill_opacity=0.6)
        ab = Line(start=a+centro,end=b+centro,color=RED)
        cd = Line(start=c+centro,end=d+centro,color=RED)
        axes = Axes(x_min = -0.5, x_max = 6, y_min = -0.5, y_max = 5,center_point=centro)
        x_label = TexMobject(r"x").scale(0.75).move_to(np.array((6.1,-0.3,0))+centro)
        y_label = TexMobject(r"y").scale(0.75).move_to(np.array((-0.3,5.1,0))+centro)
        ejes = VGroup(axes,x_label,y_label)
        gpo = VGroup(rect,ab,cd,ejes,a_label,b_label,c_label,d_label).shift(0.5*RIGHT+0.5*DOWN)

        self.play(Write(t1))
        self.wait(3)
        self.play(ApplyMethod(t1.to_edge,UP))
        self.play(Write(ejes))
        self.play(Write(a_label),Write(b_label),Write(c_label),Write(d_label))
        self.play(ShowCreation(ab),ShowCreation(cd))
        self.play(ShowCreation(rect))
        self.wait()
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.play(Write(t2))
        self.play(Write(t3))
        self.wait(5)
        self.play(*[FadeOut(mob) for mob in self.mobjects])

    def parte3(self):
        t1 = TextMobject('''Para comprender mejor el teorema enunciado,\n
                            consideremos el sólido delimitado por arriba con \n
                            la gráfica de $f$, por abajo con el rectángulo $R$ \n
                            en el plano $xy$ y a los lados por segmentos \n
                            de planos verticales que intersectan a la frontera\n
                            de $R$ y al borde de la gráfica de $f$, con $f$ \n
                            dada por''').to_edge(UP)
        t2 = TexMobject(r"f(x,y)=x^2+y^2").next_to(t1,DOWN)
        t3 = TextMobject('''Definimos el rectangulo \n 
                            $R$ en $\\mathbb{R}^2$''').shift(0.5*UP)
        t4 = TexMobject(r"R=[0,1]\times[0,1]").next_to(t3,DOWN)
        t34 = VGroup(t3,t4)
        t34_fin = self.rectangulo_texto(t34).to_edge(LEFT).scale(0.8)
        t5 = TextMobject('''Es claro que los elementos \n 
                            de $R$ los podemos \n
                            escribir como pares \n 
                            $(x,y)$ donde $x\\in A_1$, $y\\in A_2$.''')
        t5_fin = self.rectangulo_texto(t5).to_edge(LEFT).scale(0.8)
        t6 = TextMobject('''A las funciones definidas \n 
                            en $R$, podemos escribirlas \n
                            como $z=f(x,y)$''')
        t6_fin = self.rectangulo_texto(t6).to_edge(LEFT).scale(0.8)
        t7 = TextMobject('''Notemos que fijando $x\\in A_1$,\n 
                            podemos considerar \n
                            la función $f_x:A_2\\to R$ \n 
                            definida por $f_x(y)=f(x,y)$ \n
                            donde $x$ es una constante \n
                            y la variable es $y\in A_2$.''')
        t7_fin = self.rectangulo_texto(t7).to_edge(LEFT).scale(0.8)
        t8 = TextMobject('''Así, la integral \n 
                            $\\int_{A_2}f_x(y)dy$ es el área bajo \n
                            la curva en el corte de \n 
                            la superficie al fijar $x$''')
        t8_fin = self.rectangulo_texto(t8).to_edge(LEFT).scale(0.8)
        nota1 = TextMobject('''Nota que el corte es \n 
                               paralelo al plano $yz$''').scale(0.6).to_corner(RIGHT+DOWN)
        t9 = TextMobject('''Entonces al tomar una \n 
                            partición del intervalo $A_1$, \n
                            y fijar una $\\xi_i$ en el \n
                            subintervalo $[x_i,x_{i+1}]$
                            $$\\left(\\int_{A_2}f_{\\xi_i} (y)dy\\right)(x_{i+1}-x_i)$$
                            es un volumen que aproxima \n 
                            el volumen bajo la \n
                            superficie en el rectángulo \n 
                            $[x_i,x_{i+1}]\\times A_2$.''')
        t9_fin = self.rectangulo_texto(t9).to_edge(LEFT).scale(0.7)
        t10 = TextMobject('''Luego, definiendo $F(x)=\\int_{A_2} f_x(y)dy$, obtenemos \n
                             que el volumen bajo $f$ está dado por:
                             $$V=\\lim_{n\\to\\infty}\\sum_{i=1}^n F(\\xi_i)(x_{i+1}-x_i)$$
                             $$V=\\int_{A_1}\\int_{A_2}f(x,y)dydx=\\int_0^1\\int_0^1(x^2+y^2)dydx$$''')
        t10_fin = self.rectangulo_texto(t10)
        
        ejes = ThreeDAxes(
            x_min = -3, 
            x_max = 3, 
            y_min = -3, 
            y_max = 3,
            z_min = -0.5,
            z_max = 5,
            axis_config = {
                "line_frequency" : 2
            },
            z_axis_config = {
                "line_frequency" : 2
            }
            )
        x_label = TexMobject(r"x").scale(0.75).move_to((2.5,0.3,0))
        y_label = TexMobject(r"y").scale(0.75).move_to((0.3,2.5,0))
        axes = VGroup(ejes,x_label,y_label)
        paraboloide = ParametricSurface(
            lambda u,v: np.array([
                u,
                v,
                u**2+v**2
            ]),u_min=0,u_max=2,v_min=0,v_max=2
        )
        rect = Rectangle(height=2,width=2,color=RED,fill_color=RED,fill_opacity=0.6).shift(UP+RIGHT)
        xy = np.array([1,1,0])
        fxy = np.array([0,0,xy[0]**2+xy[1]**2])
        fixxed_x = 1
        line_dom = Line(start=np.array([fixxed_x,0,0]),end=np.array([fixxed_x,2,0]))
        f_x = ParametricFunction(lambda t: np.array([fixxed_x,t,fixxed_x**2+t**2]),t_min=0,t_max=2,color=YELLOW)
        curve2 = ParametricFunction(lambda t: np.array([fixxed_x,t,0]),t_min=0,t_max=2)
        long = 0.2
        x_apoyo = fixxed_x+long
        f_x_apoyo = ParametricFunction(lambda t: np.array([x_apoyo,t,fixxed_x**2+t**2]),t_min=0,t_max=2,color=PINK)
        curve3 = ParametricFunction(lambda t: np.array([x_apoyo,t,0]),t_min=0,t_max=2)
        particion = VGroup(*self.particion1(long))
        reg1 = self.get_region(0, 2, f_x, curve2)
        reg2 = self.get_region(0, 2, f_x_apoyo, curve3)
        reg3 = self.get_region(0 ,2 , f_x, f_x_apoyo)

        self.play(Write(t1))
        self.acomodar_textos(t2)
        self.wait(14)
        self.play(FadeOut(t1))
        self.play(ApplyMethod(t2.to_edge,LEFT))
        self.move_camera(phi=70*DEGREES,theta=60*DEGREES-90*DEGREES,frame_center=(0,0,2.5))
        self.play(Write(axes))
        self.play(ShowCreation(paraboloide))
        self.play(FadeOut(t2))
        self.acomodar_textos_wait(t34_fin,4)
        self.play(ShowCreation(rect))
        self.remove(paraboloide)
        self.add(paraboloide)
        self.play(FadeOut(t34_fin))
        self.acomodar_textos_wait(t5_fin,3)
        self.play(FadeOut(t5_fin))
        self.acomodar_textos_wait(t6_fin,2)
        self.play(FadeOut(t6_fin))
        self.acomodar_textos_wait(t7_fin,4)
        self.play(Write(line_dom))
        self.play(Write(f_x))
        self.wait()
        self.play(FadeOut(t7_fin))
        self.acomodar_textos_wait(t8_fin,3)
        self.play(ShowCreation(reg1))        
        self.acomodar_textos(nota1)
        self.play(FadeOut(t8_fin))
        self.play(FadeOut(nota1))
        self.acomodar_textos_wait(t9_fin,6)
        self.play(ShowCreation(particion))
        self.play(ShowCreation(reg2))
        self.play(ShowCreation(reg3))        
        self.wait(5)
        self.play(FadeOut(t9_fin))
        self.acomodar_textos_wait(t10_fin,12)
        self.play(FadeOut(t10_fin),FadeOut(reg1),FadeOut(reg2),FadeOut(reg3),FadeOut(particion),FadeOut(f_x),FadeOut(line_dom))

    def parte4(self):
        t7 = TextMobject('''Por otro lado, si fijamos $y\\in A_2$,\n 
                            podemos considerar \n
                            la función $f_y:A_1\\to R$ \n 
                            definida por $f_y(x)=f(x,y)$ \n
                            donde $y$ es una constante \n
                            y la variable es $x\in A_1$.''')
        t7_fin = self.rectangulo_texto(t7).to_edge(LEFT).scale(0.8)
        t8 = TextMobject('''Así, la integral \n 
                            $\\int_{A_1}f_y(x)dx$ es el área bajo \n
                            la curva en el corte de \n 
                            la superficie al fijar $y$''')
        t8_fin = self.rectangulo_texto(t8).to_edge(LEFT).scale(0.8)
        nota1 = TextMobject('''Nota que el corte es \n 
                               paralelo al plano $xz$''').scale(0.6).to_corner(RIGHT+DOWN)
        t9 = TextMobject('''Entonces al tomar una \n 
                            partición del intervalo $A_2$, \n
                            y fijar una $\\zeta_i$ en el \n
                            subintervalo $[y_i,y_{i+1}]$
                            $$\\left(\\int_{A_1}f_{\\zeta_i}(x)dx\\right)(y_{i+1}-y_i)$$
                            es un volumen que aproxima \n 
                            el volumen bajo la \n
                            superficie en el rectángulo \n 
                            $A_1 \\times[y_i,y_{i+1}]$.''')
        t9_fin = self.rectangulo_texto(t9).to_edge(LEFT).scale(0.7)
        t10 = TextMobject('''Así, si $G(y)=\\int_{A_1} f_y(x)dx$, obtenemos \n
                             que el volumen bajo $f$ está dado por: 
                             $$V=\\lim_{n\\to\\infty}\\sum_{i=1}^n G(\\zeta_i)(y_{i+1}-y_{i})$$
                             $$V=\\int_{A_2}\\int_{A_1}f(x,y)dxdy=\\int_0^1\\int_0^1(x^2+y^2)dxdy$$''')
        t10_fin = self.rectangulo_texto(t10)
        t1 = TextMobject('''Resolviendo las integrales:''').shift(1.5*UP)
        t2 = TexMobject(r"V=\int_{0}^{1}\int_{0}^1 (x^2+y^2) dy dx= \int_{0}^{1} \int_{0}^1 (x^2 + y^2 ) dx dy").next_to(t1,DOWN)
        t3 = TextMobject('''notamos que el volumen del sólido delimitado por $R$ \n
                            y acotado superiormente por $f(x,y)$ es dos tercios, $V=\\frac{2}{3}$.''').next_to(t2,DOWN)
        tgpo = VGroup(t1,t2,t3)

        xy = np.array([1,1,0])
        fxy = np.array([0,0,xy[0]**2+xy[1]**2])
        fixxed_y = 1
        line_dom = Line(start=np.array([0,fixxed_y,0]),end=np.array([2,fixxed_y,0]))
        f_y = ParametricFunction(lambda t: np.array([t,fixxed_y,fixxed_y**2+t**2]),t_min=0,t_max=2,color=YELLOW)
        curve2 = ParametricFunction(lambda t: np.array([t,fixxed_y,0]),t_min=0,t_max=2)
        long = 0.2
        y_apoyo = fixxed_y+long
        f_y_apoyo = ParametricFunction(lambda t: np.array([t,y_apoyo,fixxed_y**2+t**2]),t_min=0,t_max=2,color=PINK)
        curve3 = ParametricFunction(lambda t: np.array([t,y_apoyo,0]),t_min=0,t_max=2)
        particion = VGroup(*self.particion2(long))
        reg1 = self.get_region(0, 2, f_y, curve2)
        reg2 = self.get_region(0, 2, f_y_apoyo, curve3)
        reg3 = self.get_region(0 ,2 , f_y, f_y_apoyo)

        self.acomodar_textos_wait(t7_fin,4)
        self.play(Write(line_dom))
        self.play(Write(f_y))
        self.wait()
        self.play(FadeOut(t7_fin))
        self.acomodar_textos_wait(t8_fin,3)
        self.play(ShowCreation(reg1))        
        self.acomodar_textos(nota1)
        self.play(FadeOut(t8_fin))
        self.play(FadeOut(nota1))
        self.acomodar_textos_wait(t9_fin,6)
        self.play(ShowCreation(particion))
        self.play(ShowCreation(reg2))
        self.play(ShowCreation(reg3))        
        self.wait(5)
        self.play(FadeOut(t9_fin))
        self.acomodar_textos_wait(t10_fin,12)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.move_camera(phi=0*DEGREES,theta=-90*DEGREES,frame_center=(0,0,0))
        self.write_wait_fade(tgpo,10)

    def parte5(self):
        t1 = TextMobject('''Recordemos que lo anterior es un corolario del \n
                            teorema de Fubini.''')
        t2 = TextMobject('''El teorema en sí, considera un caso más general, \n
                            el caso donde la función no necesariamente \n
                            es continua. ''')
        t3 = TextMobject('''Su enunciado es el siguiente:''').to_edge(UP)
        t4 = TextMobject('''Sea  R  $\subset \mathbb{R}^2$ un rectángulo descompuesto \n
                            como producto cartesiano de dos intervalos $A_1 =[a,b]$, \n
                            $A_2=[c,d] $ $\subset \mathbb{R}$, es decir,''').next_to(t3,DOWN)
        t5 = TexMobject(r"R = A_1 \times A_2, \hspace{0.3 cm} R \subset \mathbb{R}^2,").next_to(t4,DOWN)
        t6 = TextMobject('''$f: R \\longrightarrow \\mathbb{R}$ una función integrable. Si las funciones \n
                            $I(x)$ y $S(x)$, definidas a continuación, son integrables sobre $A_1$''').next_to(t5,DOWN)
        t7 = TexMobject(
            r"I(x)=\lefteqn{\int_{A_2} f(x,y)}\lefteqn{\hspace{0.0ex}\rule[-2.25ex]{1.1ex}{.05ex}}\phantom{\int_{A_2} f(x,y)}dy, \quad S(x)=\lefteqn{\int^{A_2} f(x,y)}\lefteqn{\hspace{1.3ex}\rule[ 3.35ex]{1.1ex}{.05ex}} \hspace{0.1 cm}\phantom{\int^{A_2} f(x,y)}dy ."
            ).next_to(t6,DOWN)
        t8 = TextMobject('''Entonces, 
                            $$\int_R f = \int_{A_1} I(x) \mathrm{d}x =  \int_{A_1} S(x) \mathrm{d}x $$''').next_to(t7,DOWN)
        gpo = VGroup(t3,t4,t5,t6,t7,t8).scale(0.8).to_edge(UP)
        
        self.write_wait_fade(t1,3)
        self.write_wait_fade(t2,5)
        self.play(Write(t3))
        self.play(Write(t4))
        self.wait()
        self.play(Write(t5))
        self.wait()
        self.play(Write(t6))
        self.wait()
        self.play(Write(t7))
        self.wait()
        self.play(Write(t8))
        self.wait(20)
        self.play(FadeOut(gpo))

    def construct(self):
        self.parte1()
        self.parte2()
        self.parte3()
        self.parte4()
        self.parte5()

    def acomodar_textos(self,obj):
        self.add_fixed_in_frame_mobjects(obj)
        self.play(Write(obj))
    
    def acomodar_textos_wait(self,obj,time=1):
        self.add_fixed_in_frame_mobjects(obj)
        self.play(Write(obj))
        self.wait(time)

    def write_wait_fade(self,obj,time=1):
        self.play(Write(obj))
        self.wait(time)
        self.play(FadeOut(obj))

    def rectangulo_texto(self,obj):
        rect = SurroundingRectangle(obj,color=WHITE,fill_color=BLACK,fill_opacity=1)
        grupo = VGroup(rect,obj)
        return grupo

    def get_region(self, x_min, x_max, curve1, curve2, **kwargs):
        x_vals = np.arange(x_min, x_max, 0.1)
        c1_points = [
            curve1.get_point_from_function(x) for x in x_vals
        ]
        c2_points = [
            curve2.get_point_from_function(x) for x in x_vals
        ]
        c2_points.reverse()
        points = c1_points + c2_points
        region = Polygon(
            *points,
            stroke_width=0.5,
            fill_color=PINK,
            fill_opacity=0.5
        )
        return region

    def particion1(self,longitud):
        particion = []
        valores = np.arange(longitud/2,2-longitud/2,longitud)
        for i in valores:
            rect = Rectangle(width=longitud,height=2,color=GREEN,fill_opacity=0,stroke_width=1)
            rect.move_to([i,1,0])
            particion.append((rect))
        return particion

    def particion2(self,longitud):
        particion = []
        valores = np.arange(longitud/2,2-longitud/2,longitud)
        for i in valores:
            rect = Rectangle(width=2,height=longitud,color=GREEN,fill_opacity=0,stroke_width=1)
            rect.move_to([1,i,0])
            particion.append((rect))
        return particion
