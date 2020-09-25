from manimlib.imports import *

#### SUGERENCIA: SIEMPRE QUE CAMBIES LOS VECTORES A VISUALIZAR ###
### CONDISERA QUE EL PLNO ES DE [-7,7]x[-4,4] ####


### CLASES AUXILIARES, NO SON ESCENAS

class Grid(VGroup):
    CONFIG = {
        "height": 6.0,
        "width": 6.0,
    }
    def __init__(self, rows, columns, **kwargs):
        digest_config(self, kwargs, locals())
        super().__init__(**kwargs)
        x_step = self.width / self.columns
        y_step = self.height / self.rows
        for x in np.arange(0, self.width + x_step, x_step):
            self.add(Line(
                [x - self.width / 2., -self.height / 2., 0],
                [x - self.width / 2., self.height / 2., 0],
            ))
        for y in np.arange(0, self.height + y_step, y_step):
            self.add(Line(
                [-self.width / 2., y - self.height / 2., 0],
                [self.width / 2., y - self.height / 2., 0]
            ))
class ScreenGrid(VGroup):
    CONFIG = {
        "rows": 8,
        "columns": 14,
        "height": FRAME_Y_RADIUS * 2,
        "width": 14,
        "grid_stroke": 0.5,
        "grid_color": WHITE,
        "axis_color": RED,
        "axis_stroke": 2,
        "labels_scale": 0.25,
        "labels_buff": 0,
        "number_decimals": 2
    }
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        rows = self.rows
        columns = self.columns
        grid = Grid(width=self.width, height=self.height, rows=rows, columns=columns)
        grid.set_stroke(self.grid_color, self.grid_stroke)
        vector_ii = ORIGIN + np.array((- self.width / 2, - self.height / 2, 0))
        vector_si = ORIGIN + np.array((- self.width / 2, self.height / 2, 0))
        vector_sd = ORIGIN + np.array((self.width / 2, self.height / 2, 0))
        axes_x = Line(LEFT * self.width / 2, RIGHT * self.width / 2)
        axes_y = Line(DOWN * self.height / 2, UP * self.height / 2)
        axes = VGroup(axes_x, axes_y).set_stroke(self.axis_color, self.axis_stroke)
        divisions_x = self.width / columns
        divisions_y = self.height / rows
        directions_buff_x = [UP, DOWN]
        directions_buff_y = [RIGHT, LEFT]
        dd_buff = [directions_buff_x, directions_buff_y]
        vectors_init_x = [vector_ii, vector_si]
        vectors_init_y = [vector_si, vector_sd]
        vectors_init = [vectors_init_x, vectors_init_y]
        divisions = [divisions_x, divisions_y]
        orientations = [RIGHT, DOWN]
        labels = VGroup()
        set_changes = zip([columns, rows], divisions, orientations, [0, 1], vectors_init, dd_buff)
        for c_and_r, division, orientation, coord, vi_c, d_buff in set_changes:
            for i in range(1, c_and_r):
                for v_i, directions_buff in zip(vi_c, d_buff):
                    ubication = v_i + orientation * division * i
                    coord_point = round(ubication[coord], self.number_decimals)
                    label = Text(f"{coord_point}",font="Arial",stroke_width=0).scale(self.labels_scale)
                    label.next_to(ubication, directions_buff, buff=self.labels_buff)
                    labels.add(label)
        self.add(grid, axes, labels)
        
### COMIENZAN ESCENAS

###################################
#### OPERACIONES CON VECTORES #####
###################################

######Hint para crear la animación
###Primero crea una clase con el nombre de animación.
###Luego necesitas crear una "construcción" (función) para que manim ejecute el objeto animación
###Luego tendrás que definir vectores...
###No solo ellos, tambien sus propiedades como en las animaciones anteriores
###Finalmente dile a la computadora cómo deben ser realizadas las animaciones con "self.play[...etc.]"

######¿Qué conclusiones geométricas puedes obtener de ésta animación?


#### Operaciones con vectores representados por flechas ####


# Puedes modificar estos parámetros para probar diferentes vectores y escalares #

a = np.array([1, 1, 0])
b = np.array([-2, 1, 0])
c = -1.5

#### considera que el plano es [-7,7]x[-4,4] ####

text_pos = np.array([-4, 2.6, 0])


class Opera(Scene):
    def construct(self):
        plano = NumberPlane()

        vec1 = Vector(direction=a, color=RED)
        vec1_name = TexMobject("a")
        vec1_name.next_to(vec1.get_corner(RIGHT + UP), RIGHT)
        vec2 = Vector(direction=b, color=GOLD_E)
        vec2_name = TexMobject("b")
        vec2_name.next_to(vec2.get_corner(LEFT + UP), LEFT)

        #### Suma ####

        vecsum = Vector(direction=a + b, color=GREEN_SCREEN)
        vecsum_name = TexMobject("a+b").set_color(GREEN_SCREEN)
        vecsum_name.next_to(vecsum, LEFT)
        suma1 = TextMobject("Podemos ver la suma de dos")
        suma2 = TextMobject("vectores con flechas")
        suma2.next_to(suma1, DOWN)
        suma = VGroup(suma1, suma2)
        suma.scale(0.75)

        suma.bg = SurroundingRectangle(suma, color=WHITE, fill_color=BLACK,
                                         fill_opacity=1)
        Group11 = VGroup(suma.bg, suma)
        #### Multiplicar por escalar ####
        vecesc = Vector(direction=c * a, color=RED)
        vecesc_name = TexMobject(str(c) + "a")
        vecesc_name.next_to(vecesc, DOWN)
        esc1 = TextMobject("Tambi\\'{e}n podemos multiplicar")
        esc2 = TextMobject("vectores por un escalar del campo")
        esc2.next_to(esc1, DOWN)
        esc = VGroup(esc1, esc2)
        esc.scale(0.75)
        valor = TexMobject(r"\text{En este caso el escalar es}" + str(c))
        valor.scale(0.75)
        valor.move_to(text_pos)

        esc.bg = SurroundingRectangle(esc, color=WHITE, fill_color=BLACK,
                                       fill_opacity=1)
        Group12 = VGroup(esc.bg, esc)

        valor.bg = SurroundingRectangle(valor, color=WHITE, fill_color=BLACK,
                                      fill_opacity=1)
        Group13 = VGroup(valor.bg, valor)
        #### Desafíos ####
        ejem = TextMobject("Puedes modificar los vectores y el escalar para probar tus propios ejemplos,").scale(0.75)
        ejem2 = TextMobject("encontrar\\'{a}s m\\'{a}s informaci\\'{o}n en el c\\'{o}digo de este video.").scale(0.75)
        ejem2.next_to(ejem, DOWN)

        #Animación
        #Animación suma
        self.play(FadeIn(Group11))
        self.play(ApplyMethod(Group11.move_to, text_pos))
        self.play(ShowCreation(plano))
        self.play(ShowCreation(vec1), ShowCreation(vec2), Write(vec1_name), Write(vec2_name))
        self.wait()
        self.play(ApplyMethod(vec2.move_to, a + b / 2), ApplyMethod(vec2_name.move_to, a + b / 2))
        self.wait()
        self.play(ShowCreation(vecsum), Write(vecsum_name))
        self.wait()
        self.play(FadeOut(vec1), FadeOut(vec2), FadeOut(vecsum), FadeOut(plano), FadeOut(Group11), FadeOut(vec1_name),
                  FadeOut(vec2_name), FadeOut(vecsum_name))
        #Animación escalar
        self.play(Write(Group12))
        self.play(ApplyMethod(Group12.move_to, text_pos))
        self.play(ShowCreation(plano))
        self.play(ShowCreation(vec1), Write(vec1_name))
        self.wait()
        self.play(ReplacementTransform(Group12, Group13))
        self.play(ReplacementTransform(vec1, vecesc), ReplacementTransform(vec1_name, vecesc_name))
        self.wait(2)
        self.play(FadeOut(plano), FadeOut(vecesc_name), FadeOut(Group13), FadeOut(vecesc))
        #Animación desafíos     
        self.play(Write(ejem), Write(ejem2))
        self.wait(3)
        self.play(FadeOut(ejem), FadeOut(ejem2))
        
#########################
#### CONMUTATIVIDAD #####
#########################

class Conmutatividad(Scene):
    def construct(self):
        grid = ScreenGrid()
        v_x = Arrow((0, 0, 0), 2 * RIGHT + UP, buff=0)
        v_y = Arrow((0, 0, 0), RIGHT - 2 * UP, buff=0)
        v_z = Arrow((0, 0, 0), LEFT + 0.5 * UP, buff=0)
        suma_t_1 = TextMobject('Sumemos el vector:' + ' $\\vec{x}+\\vec{y}$')
        suma_t_2 = TextMobject('Sumemos el vector:' + ' $\\vec{y}+\\vec{x}$')
        prop_1 = TextMobject('''Observemos la primera propiedad: \n 
                                la conmutatividad.''')
        prop_1.set_color(GREEN).move_to((-3, 3, 0))
        suma_t_1.move_to((-3, 2, 0))
        suma_t_1[0][16:18].set_color(RED)
        suma_t_1[0][19:].set_color(ORANGE)
        suma_t_2.move_to((-3, 1, 0))
        suma_t_2[0][19:].set_color(RED)
        suma_t_2[0][16:18].set_color(ORANGE)
        v_x_t = TextMobject('$\\vec{x}$')
        v_y_t = TextMobject('$\\vec{y}$')
        v_z_t = TextMobject('$\\vec{z}$')
        v_x_t.move_to(v_x.get_end() + RIGHT * 0.3)
        v_y_t.next_to(v_y.get_end() + RIGHT * 0.1)
        v_z_t.next_to(v_y.get_end() + RIGHT * 0.1)
        gpo_x = VGroup(v_x, v_x_t)
        gpo_y = VGroup(v_y, v_y_t)
        gpo_z = VGroup(v_z, v_z_t)
        gpo_x.set_color(RED)
        gpo_y.set_color(ORANGE)
        v_y_mov = Arrow(v_x.get_end(), v_x.get_end() + v_y.get_end(), buff=0)
        v_y_mov_t = TextMobject('$\\vec{y}$')
        v_y_mov_t.move_to(v_y_mov.get_end() + RIGHT * 0.3)
        gpo_y_mov = VGroup(v_y_mov, v_y_mov_t)
        v_x_mov = Arrow(v_y.get_end(), v_y.get_end() + v_x.get_end(), buff=0)
        v_x_mov_t = TextMobject('$\\vec{x}$')
        v_x_mov_t.move_to(v_x_mov.get_end() + RIGHT * 0.3)
        gpo_x_mov = VGroup(v_x_mov, v_x_mov_t)
        gpo_y_mov.set_color(ORANGE)
        gpo_x_mov.set_color(RED)
        v_x_mov = Arrow(v_x)
        v_x_mov_t = TextMobject('$\\vec{x}$')
        v_x_mov_t.move_to(v_x.get_end() + RIGHT * 0.3)
        suma_x_y = Arrow((0, 0, 0), v_y_mov.get_end(), buff=0)
        gpo_y_1 = gpo_y.copy()
        Text_f = TextMobject(''' Nota que en realidad lo que nos dice es que \n
                                 no importa el camino que elijas, siempre llegas a ROMA \n
                                 o en este caso, \n
                                 el punto en el espacio vectorial. ''')
        Text_f.move_to((-3.3, -1.5, 0)) \
            .scale(0.56)
        ####################################################################
        prop_1.bg = SurroundingRectangle(prop_1, color=WHITE, fill_color=BLACK,
                                      fill_opacity=1)
        Group11 = VGroup(prop_1.bg, prop_1)
        suma_t_1.bg = SurroundingRectangle(suma_t_1, color=WHITE, fill_color=BLACK,
                                         fill_opacity=1)
        Group12 = VGroup(suma_t_1.bg, suma_t_1)
        suma_t_2.bg = SurroundingRectangle(suma_t_2, color=WHITE, fill_color=BLACK,
                                           fill_opacity=1)
        Group13 = VGroup(suma_t_2.bg, suma_t_2)
        Text_f.bg = SurroundingRectangle(Text_f, color=WHITE, fill_color=BLACK,
                                           fill_opacity=1)
        Group14 = VGroup(Text_f.bg, Text_f)
        self.play(Write(grid))
        self.play(Write(Group11))
        self.wait(2)
        self.play(FadeOut(Group11))
        self.wait()
        self.play(Write(v_x), Write(v_y), Write(v_x_t), Write(v_y_t))
        self.wait()
        self.play(Write(Group12))
        self.wait()
        self.play(ReplacementTransform(gpo_y, gpo_y_mov))
        self.wait()
        self.play(Write(suma_x_y))
        self.wait()
        self.play(Write(Group13))
        self.play(ReplacementTransform(gpo_y_mov, gpo_y_1),
                  ReplacementTransform(gpo_x, gpo_x_mov))
        self.wait()
        self.play(Write(Group14))
        self.wait()


#########################
#### ASOCIATIVIDAD #####
#########################

class Asociatividad(Scene):
    def construct(self):
        grid = ScreenGrid()
        ###vectores:
        x = Arrow((0, 0, 0), (3, 2, 0), buff=0)
        y = Arrow((0, 0, 0), (1, 2, 0), buff=0)
        z = Arrow((0, 0, 0), (1, -2, 0), buff=0)
        ###suma (x+y)+z
        y_mov_a_x = Arrow(x.get_end(), x.get_end() + y.get_end(), buff=0)
        x_mas_y = Arrow((0, 0, 0), y_mov_a_x.get_end(), buff=0)
        z_mov_a_x_mas_y = Arrow(x_mas_y.get_end(), x_mas_y.get_end() + z.get_end(), buff=0)
        x_mas_y_mas_z = Arrow((0, 0, 0), z_mov_a_x_mas_y.get_end(), buff=0)
        ###suma x+(y+z)
        z_mov_a_y = Arrow(y.get_end(), y.get_end() + z.get_end(), buff=0)
        y_mas_z = Arrow((0, 0, 0), z_mov_a_y.get_end(), buff=0)
        y_mas_z_mov_a_x = Arrow(x.get_end(), x.get_end() + y_mas_z.get_end(), buff=0)
        x_mas_y_mas_z_1 = Arrow((0, 0, 0), y_mas_z_mov_a_x.get_end(), buff=0)
        ###texto:
        t_1 = TextMobject(''' Segunda propiedad: \n
                              Asociatividad. ''')
        t_2 = TextMobject(''' Hagamos: $(\\vec{x}+\\vec{y})+\\vec{z}$ ''')
        t_3 = TextMobject(''' Hagamos: $\\vec{x}+(\\vec{y}+\\vec{z})$ ''')
        t_4 = TextMobject('$(\\vec{x}+\\vec{y})$')
        t_5 = TextMobject('$(\\vec{x}+\\vec{y})+\\vec{z}$')
        t_6 = TextMobject('$(\\vec{y}+\\vec{z})$')
        t_7 = TextMobject('$\\vec{x}+(\\vec{y}+\\vec{z})$')
        t_8 = TextMobject('$\\vec{x}$')
        t_9 = TextMobject('$\\vec{y}$')
        t_10 = TextMobject('$\\vec{z}$')
        t_11 = TextMobject('''Nota como es casi lo misma idea geométrica \n
                              que el hecho de hacer la conmutación, es tomar \n
                              distintos caminos para llegar al mismo vector \n
                              en el espacio vectorial; dados tres vectores distintos.''')
        ###grupos:
        gpo_1 = VGroup(x, t_8)
        gpo_2 = VGroup(y, t_9)
        gpo_3 = VGroup(z, t_10)
        gpo_4 = VGroup(x_mas_y, t_4)
        gpo_5 = VGroup(x_mas_y_mas_z, t_5)
        gpo_6 = VGroup(y_mas_z, t_6)
        gpo_7 = VGroup(x_mas_y_mas_z_1, t_7)
        ###posiciones texto y colores:
        t_11.move_to((0, -2, 0)) \
            .scale(0.85)
        t_1.move_to((-3, 3, 0)) \
            .set_color(GREEN)
        t_2.next_to(t_1, DOWN)
        t_3.next_to(t_2, DOWN)
        t_4.next_to(x_mas_y.get_center(), UP + LEFT)
        t_5.next_to(x_mas_y_mas_z.get_center(), DOWN + RIGHT)
        t_6.next_to(y_mas_z.get_center(), DOWN)
        t_7.next_to(x_mas_y_mas_z_1.get_center(), DOWN * 2)
        t_8.next_to(x.get_end(), UP)
        t_9.next_to(y.get_end(), DOWN)
        t_10.next_to(z.get_end(), DOWN)
        gpo_4.set_color(ORANGE)
        gpo_5.set_color(RED)
        gpo_7.set_color(PURPLE)
        gpo_2_1 = gpo_2.copy()
        gpo_3_1 = gpo_3.copy()
        t_1.bg = SurroundingRectangle(t_1, color=WHITE, fill_color=BLACK,
                                         fill_opacity=1)  # Contorno del rectángulo
        Group11 = VGroup(t_1.bg, t_1)  # Order matters
        t_2.bg = SurroundingRectangle(t_2, color=WHITE, fill_color=BLACK,
                                      fill_opacity=1)
        Group12 = VGroup(t_2.bg, t_2)
        t_3.bg = SurroundingRectangle(t_3, color=WHITE, fill_color=BLACK,
                                      fill_opacity=1)
        Group13 = VGroup(t_3.bg, t_3)
        t_11.bg = SurroundingRectangle(t_11, color=WHITE, fill_color=BLACK,
                                      fill_opacity=1)
        Group111 = VGroup(t_11.bg, t_11)
        ###animación:
        self.play(Write(grid))
        self.wait()
        self.play(Write(Group11))
        self.wait(2)
        self.play(FadeOut(Group11))
        self.play(Write(gpo_1), Write(gpo_2), Write(gpo_3))
        self.wait()
        self.play(Write(Group12))
        self.wait()
        self.play(ReplacementTransform(gpo_2, y_mov_a_x))
        self.wait()
        self.play(Write(gpo_4))
        self.wait()
        self.play(ReplacementTransform(gpo_3, z_mov_a_x_mas_y), FadeOut(gpo_1), FadeOut(y_mov_a_x))
        self.wait()
        self.play(Write(gpo_5))
        self.wait()
        self.play(FadeOut(gpo_4), FadeOut(z_mov_a_x_mas_y), FadeOut(y_mov_a_x),
                  FadeOut(gpo_5), Write(gpo_2_1), Write(gpo_1), Write(gpo_3_1))
        self.wait()
        self.play(Write(Group13))
        self.wait()
        self.play(ReplacementTransform(gpo_3_1, z_mov_a_y))
        self.wait()
        self.play(Write(gpo_6))
        self.wait()
        self.play(ReplacementTransform(gpo_6, y_mas_z_mov_a_x), FadeOut(gpo_2_1), FadeOut(z_mov_a_y))
        self.wait()
        self.play(Write(gpo_7))
        self.wait()
        self.play(Write(Group111))
        self.wait(6)
        self.play(FadeOut(Group111), FadeOut(Group12), FadeOut(Group13))
        self.wait(2)
       
    
#####################################
#### DISTRIBUCION SUMA ESCALARES #####
#####################################

class Distribucion_Suma_Escalares(Scene):
    def construct(self):
        ###vectores:
        grid = NumberPlane()
        k = float(input('dame a k entre 0 y 1 \n'))
        j = float(input('dame a j entre 0 y 1 \n'))
        x = Arrow((0, 0, 0), (2, -1, 0), buff=0)
        k_m_j_x = Arrow((0, 0, 0), (k + j) * x.get_end(), buff=0)
        kx = Arrow((0, 0, 0), k * x.get_end(), buff=0)
        jx = Arrow((0, 0, 0), j * x.get_end(), buff=0)
        kx_m_jx = Arrow((0, 0, 0), kx.get_end() + jx.get_end(), buff=0)
        ###texto
        prop = TextMobject('Distribuir el producto de suma de escalares con un vector.')
        k_m_j_x_t = TexMobject('(k+j)\\vec{x}')
        kx_m_jx_t = TexMobject('k\\vec{x}+j\\vec{x}')
        kx_t = TexMobject('k\\vec{x}')
        jx_t = TexMobject('j\\vec{x}')
        t_1 = TextMobject('''Nota que esta propiedad es encontrar \n
                                de vuelta otros caminitos para \n
                                llegar a un mismo vector dentro del \n
                                espacio vectorial, s\\'{o}lo que a diferencia \n
                                de las propiedades dados 3 vectores \n
                                ahora usamos un solo vector y dos escalares, \n
                                estamos haciendo como un ``escalamiento'' de caminos. ''')
        t_2 = TextMobject('''Se te ocurre c\\'{o}mo realizar la animaci\\'{o}n para la propiedad:
                                $$k(\\vec{x}+\\vec{y}) = k\\vec{x}+k\\vec{y}, \ k\in \mathbb{R}$$''')
        t_3 = TextMobject(''' Checa la parte inmediata despu\\'{e}s \n
                                 de la clase de \n
                                 \\textit{distribucion$\\_$suma$\\_$escalares} \n
                                 en el archivo de animaciones para\n
                                 espacios vectoriales \n
                                 para una idea de como realizar dicha animaci\\'{o}n.''')
        ###grupos:
        gpo_1 = VGroup(k_m_j_x, k_m_j_x_t)
        gpo_2 = VGroup(kx_m_jx, kx_m_jx_t)
        gpo_3 = VGroup(kx, kx_t)
        gpo_4 = VGroup(jx, jx_t)
        ###propiedades:
        prop.move_to((0, 2.5, 0)) \
            .set_color(GREEN)
        gpo_3.set_color(YELLOW_E)
        gpo_2.set_color(GREEN_C)
        t_2.set_color(YELLOW_E)
        jx.set_color(BLUE_D)
        jx_t.set_color(BLUE_A)
        k_m_j_x_t.next_to(k_m_j_x.get_end(), RIGHT)
        kx_m_jx_t.next_to(kx_m_jx.get_end(), RIGHT)
        kx_t.next_to(kx.get_end(), RIGHT)
        jx_t.next_to(kx.get_end(), RIGHT)
        ###animacion
        prop.bg = SurroundingRectangle(prop, color=WHITE, fill_color=BLACK,
                                         fill_opacity=1)
        Group11 = VGroup(prop.bg, prop)
        self.play(Write(grid), Write(Group11))
        self.wait()
        self.play(Write(gpo_1))
        self.wait()
        self.play(FadeOut(gpo_1))
        self.play(Write(gpo_3))
        self.wait()
        self.play(FadeOut(kx_t))
        self.play(Write(gpo_4))
        self.wait()
        self.play(FadeOut(kx))
        self.play(FadeOut(gpo_4))
        self.play(Write(gpo_2))
        self.wait()
        self.play(FadeOut(gpo_2), FadeOut(grid), FadeOut(Group11))
        self.wait(1.5)
        self.play(Write(t_1))
        self.wait(12)
        self.play(FadeOut(t_1))
        self.wait()
        self.play(Write(t_2))
        self.wait(7)
        self.play(FadeOut(t_2))
        self.wait()
        self.play(Write(t_3))
        self.wait(4)

       
#########################
#### INVERSO ADITIVO #####
#########################

class Inverso_Aditivo(Scene):
    def construct(self):
        ###vectores
        grid = NumberPlane()
        x = Arrow((0, 0, 0), (1, 2, 0), buff=0)
        menos_x = Arrow((0, 0, 0), -1 * x.get_end(), buff=0)
        x_proy_y = Arrow((0, 0, 0), (0, -1 * x.get_end()[1], 0), buff=0)
        x_proy_x = Arrow((0, 0, 0), (-1 * x.get_end()[0], 0, 0), buff=0)
        mx_proy_y = Arrow((0, 0, 0), (0, x.get_end()[1], 0), buff=0)
        mx_proy_x = Arrow((0, 0, 0), (x.get_end()[0], 0, 0), buff=0)
        ###texto
        x_t = TextMobject('$\\vec{x} = (x_1,x_2)$')
        xpy_t = TextMobject('$Proj_{(0,1)}(-\\vec{x}) = (-x_1,0)$')
        xpx_t = TextMobject('$Proj_{(1,0)}(-\\vec{x}) = (0,-x_2)$')
        menosx_t = TextMobject('$-\\vec{x} = (-x_1,-x_2)$')
        prop = TextMobject('Inverso Aditivo.')
        t_1 = TextMobject('''Para el vector $\\vec{x}$ \n
                             existe el vector $-\\vec{x}$ \n
                             tal que hace: \n
                             $\\vec{x}+(-\\vec{x}) = \\vec{0}$.''')
        t_2 = TextMobject(''' Que notemos \n 
                              que geom\\'{e}tricamente:\n
                              hay que "voltear" \n
                              respecto al origen \n
                              al vector $\\vec{x}$.''')
        t_0 = TextMobject(''' fij\\'{e}monos en el siguiente vector \n
                             y sus componentes. ''')
        t_2.bg = SurroundingRectangle(t_2, color=WHITE, fill_color=BLACK,
                                      fill_opacity=1)
        Group14 = VGroup(t_2.bg, t_2)
        ###gpos
        gpo_x = VGroup(x, x_t)
        gpo_menos_x = VGroup(menos_x, menosx_t)
        gpo_text_proy = VGroup(xpy_t, xpx_t)
        gpo_x_proy_y = VGroup(x_proy_y, xpy_t)
        gpo_x_proy_x = VGroup(x_proy_x, xpx_t)
        gpo_x_proy = VGroup(mx_proy_y, mx_proy_x)
        mgpo_x_proy = VGroup(x_proy_y, x_proy_x)
        gpo_Fade = VGroup(gpo_text_proy, mgpo_x_proy, Group14)
        ###propiedades:
        xpy_t.set_color(YELLOW_D)
        xpx_t.set_color(YELLOW_D)
        x_proy_y.set_color(YELLOW_E)
        x_proy_x.set_color(YELLOW_E)
        mx_proy_y.set_color(YELLOW_E)
        mx_proy_x.set_color(YELLOW_E)
        prop.move_to((-3, 2.5, 0))
        prop.set_color(GREEN)
        t_0.move_to((-3, 2.5, 0))
        t_0.set_color(GREEN)
        x_t.next_to(x.get_end(), RIGHT, buff=0.4)
        menosx_t.next_to(menos_x.get_end(), DOWN)
        xpy_t.next_to(x_proy_y.get_end(), RIGHT)
        xpx_t.next_to(x_proy_x.get_end(), UP)
        t_1.move_to((4, -0.5, 0)) \
            .scale(0.8)
        Group14.move_to((-4, -0.75, 0)) \
            .scale(0.8)
        ###animación:
        prop.bg = SurroundingRectangle(prop, color=WHITE, fill_color=BLACK,
                                      fill_opacity=1)
        Group11 = VGroup(prop.bg, prop)
        t_0.bg = SurroundingRectangle(t_0, color=WHITE, fill_color=BLACK,
                                       fill_opacity=1)
        Group12 = VGroup(t_0.bg, t_0)
        t_1.bg = SurroundingRectangle(t_1, color=WHITE, fill_color=BLACK,
                                      fill_opacity=1)
        Group13 = VGroup(t_1.bg, t_1)
        self.play(Write(Group11), Write(grid))
        self.wait(0.5)
        self.play(FadeOut(Group11))
        self.play(Write(Group12))
        self.wait(1.3)
        self.play(Write(gpo_x))
        self.play(FadeOut(Group12))
        self.play(Write(gpo_x_proy))
        self.wait(1.3)
        self.play(FadeOut(gpo_x))
        self.play(Write(mgpo_x_proy))
        self.play(FadeOut(gpo_x_proy))
        self.play(Write(gpo_text_proy))
        self.wait()
        self.play(Write(Group13))
        self.wait(2.5)
        self.play(Write(Group14), Write(gpo_menos_x), FadeOut(Group13))
        self.wait(2.5)
        self.play(FadeOut(gpo_Fade))
        self.play(Write(gpo_x))
