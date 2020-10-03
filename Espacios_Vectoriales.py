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
        
#########################
#### BASES #####
#########################

class Bases(Scene):
    def construct(self):
        grid = NumberPlane()

        ###texto:

        t_1 = TextMobject('Idea intuitiva de lo que significa una base.')
        t_2 = TextMobject('Pensemos en el plano cartesiano...')
        t_3 = TextMobject('y en la base usual...')
        t_4 = TextMobject('''la can\\'{o}nica.''')
        t_5 = TexMobject('\\xi = \{ \\vec{e}_1, \\vec{e}_2 \} = \{ (1,0), (0,1) \}')
        t_6 = TextMobject('''Supongamos que queremos "caracterizar" \n
                             el vector $\\vec{x} = (1,2)$, con la base $\\xi$.''')
        t_7 = TextMobject('''Es claro que: \n
                             $\\vec{x} = 1\\cdot(1,0)+2\\cdot(0,1) = (1,2)$''')
        t_8 = TextMobject('''Que geom\\'{e}tricamente es...''')
        t_9 = TextMobject('''Solamente caminar una vez por el camino fijado \n
                             por el vector $\\vec{e}_1=(1,0)$ y luego caminar dos  \n
                             veces por el camino fijado por $\\vec{e}_2=(0,1)$.''')
        t_9.move_to((0, -1.3, 0))
        t_10 = TextMobject('''Ahora supongamos que tenemos la base: \n
                              $\\gamma = \{ (2,1),(1,-1) \}$''')
        t_11 = TextMobject('''Sabemos que... \n
                              $\\vec{x} = 1\cdot(2,1)+(-1)\cdot(1,-1)$''')
        t_12 = TextMobject('''¿Pero geom\\'{e}tricamente qu\\'{e} es esta combinaci\\'{o}n lineal?''')
        t_13 = TextMobject('''¡Claro! Solamente es tomar un camino distinto \n
                              dado por esta base \n
                              para llegar al mismo vector $\\vec{x}$ \n
                              en el espacio vectorial $\\mathbb{R}^2$.''')

        ###vectores:

        e_1 = Arrow((0, 0, 0), (1, 0, 0), buff=0)
        e_2 = Arrow((0, 0, 0), (0, 1, 0), buff=0)
        e_2_mov_e_1 = Arrow(e_1.get_end(), (1, 2, 0), buff=0)

        v_1 = Arrow((0, 0, 0), (2, 1, 0), buff=0)
        v_2 = Arrow((0, 0, 0), (1, -1, 0), buff=0)
        v_1_mov_v_1 = Arrow(v_1.get_end(), (1, 2, 0), buff=0)

        ###propiedades

        e_1.set_color(YELLOW_E)
        e_2.set_color(YELLOW_E)
        e_2_mov_e_1.set_color(YELLOW_E)
        t_5.set_color(YELLOW_E)
        t_7.set_color(BLUE)
        t_9.set_color(YELLOW_E)
        t_10.set_color(YELLOW_E)

        t_9.bg = SurroundingRectangle(t_9, color=WHITE, fill_color=BLACK,
                                      fill_opacity=1)
        Group19 = VGroup(t_9.bg, t_9)

        ###animacion:

        self.play(Write(t_1))
        self.wait()
        self.play(ReplacementTransform(t_1, t_2))
        self.wait(2)
        self.play(ReplacementTransform(t_2, t_3))
        self.wait()
        self.play(ReplacementTransform(t_3, t_4))
        self.wait()
        self.play(ReplacementTransform(t_4, t_5))
        self.wait(3)
        self.play(ReplacementTransform(t_5, t_6))
        self.wait(4)
        self.play(ReplacementTransform(t_6, t_7))
        self.wait(4)
        self.play(ReplacementTransform(t_7, t_8))
        self.wait()
        self.play(FadeOut(t_8), Write(grid))
        self.wait()
        self.play(Write(e_1), Write(e_2))
        self.wait()
        self.play(ReplacementTransform(e_2, e_2_mov_e_1), Write(Group19))
        self.wait(4)
        self.play(FadeOut(e_2_mov_e_1), FadeOut(grid), FadeOut(Group19), FadeOut(e_1), Write(t_10))
        self.wait(3)
        self.play(ReplacementTransform(t_10, t_11))
        self.wait(3)
        self.play(ReplacementTransform(t_11, t_12))
        self.wait(2)
        self.play(FadeOut(t_12), Write(grid))
        self.wait()
        self.play(Write(v_1), Write(v_2))
        self.wait()
        self.play(ReplacementTransform(v_2, v_1_mov_v_1))
        self.wait()
        self.play(ReplacementTransform(VGroup(v_1_mov_v_1, grid, v_1), t_13))
        self.wait(3)

##############################
#### NORMA Y PROPIEDADES #####
##############################

### Modifica estos vectores visualizar la primera propiedad, NO se dibujan partiendo del origen
v1 = np.array([2, 1, 0])
v2 = np.array([4, 2, 0])
v3 = np.array([-1, 2, 0])
v4 = np.array([3, 0, 0])

####

# Puedes cambiar estos vectores por otros  para visualizar la
# Desigualdad del tri'angulo y la propiedad de multiplicacion por escalar

avec = np.array([1, 1, 0])
bvec = np.array([4, -2, 0])
lamb = 1.5

## (NO MODIFICAR)
anorm = np.linalg.norm(avec)
bnorm = np.linalg.norm(bvec)
sumnorm = np.linalg.norm(avec + bvec)
nv1 = round(np.linalg.norm(v1), 3)
nv2 = round(np.linalg.norm(v2), 3)
nv3 = round(np.linalg.norm(v3), 3)
nv4 = round(np.linalg.norm(v4), 3)


class Propiedades_Norma(Scene):
    def construct(self):
        ### Titulo y definici'on ###

        titulo = TextMobject("La norma y sus propiedades").scale(1.2)
        deftex = TexMobject(
            r"\text{Se definió la norma euclidiana de un vector}\ \vec{x} \in \mathbb{R}^n\ \text{como}:").shift(
            2 * UP)
        defn = TexMobject(r"\Vert \vec{x} \Vert:= \sqrt{x_1^2+x_2^2+x_3^2+...+x_n^2}")
        longi = TextMobject("Esta cantidad representa la \"longitud\" de un vector").shift(2 * DOWN)
        def2d = TexMobject(r"\text{Consideremos el caso}\ \vec{x} \in \mathbb{R}^2").shift(2 * UP)
        d2d = TexMobject(r"\Vert \vec{x} \Vert := \sqrt{x_1^2+x_2^2}")
        vamo = TextMobject("Adelante veremos tres propiedades fundamentales").shift(2 * DOWN)
        segslide = VGroup(def2d, d2d, vamo)

        self.play(Write(titulo))
        self.wait(1.2)
        self.play(FadeOut(titulo))
        self.play(Write(deftex), Write(defn), Write(longi))
        self.wait(9)
        self.play(ReplacementTransform(deftex, def2d), ReplacementTransform(defn, d2d),
                  ReplacementTransform(longi, vamo))
        self.wait(8)
        self.play(FadeOut(segslide))
        self.wait()

        ### PRIMERA PROPIEDAD ###

        prop1 = TexMobject(
            r"\Vert \vec{x} \Vert \geq 0\  \forall \vec{x} \in \mathbb{R}^2\ \text{y}\ \Vert \vec{x} \Vert = 0 \Leftrightarrow \vec{x}=\vec{0}").to_edge(
            DOWN)
        prop1.bg = SurroundingRectangle(prop1, color=WHITE, fill_color=BLACK,
                                        fill_opacity=1)
        Group11 = VGroup(prop1.bg, prop1)
        plano = NumberPlane()
        vc1 = Vector(direction=v1, color=GREEN).move_to(np.array([-3, -2, 0]))
        vc2 = Vector(direction=v2, color=PURPLE).move_to(np.array([-4, 1, 0]))
        vc3 = Vector(direction=v3, color=YELLOW_E).move_to(np.array([4, --2, 0]))
        vc4 = Vector(direction=v4, color=ORANGE).move_to(np.array([2, 0, 0]))
        dot = Dot((0, 0, 0), color=WHITE, radius=0.15)
        cdot = Dot((0, 0, 0), color=BLACK)
        ddot = VGroup(dot, cdot)

        vc1_l = TexMobject(r"\vec{x}").next_to(vc1.get_center(), UP)
        vc2_l = TexMobject(r"\vec{y}").next_to(vc2.get_center(), UP)
        vc3_l = TexMobject(r"\vec{z}").next_to(vc3.get_center(), UP)
        vc4_l = TexMobject(r"\vec{w}").next_to(vc4.get_center(), UP)
        zero_dot = TexMobject(r"\vec{0}").next_to(dot.get_center(), UP + LEFT)

        vcts = VGroup(vc1, vc2, vc3, vc4, ddot)
        labels = VGroup(vc1_l, vc2_l, vc3_l, vc4_l, zero_dot)

        normies = TextMobject("Veamos las normas de los vectores:").to_edge(UP)
        vc1_n = Vector(direction=np.array([np.linalg.norm(v1), 0, 0]), color=GREEN).shift(4 * LEFT + 0.5 * UP)
        vc2_n = Vector(direction=np.array([np.linalg.norm(v2), 0, 0]), color=PURPLE).shift(4 * LEFT)
        vc3_n = Vector(direction=np.array([np.linalg.norm(v3), 0, 0]), color=YELLOW_E).shift(4 * LEFT + 0.5 * DOWN)
        vc4_n = Vector(direction=np.array([np.linalg.norm(v4), 0, 0]), color=ORANGE).shift(4 * LEFT + DOWN)

        bracv1 = Brace(vc1_n, UP)
        normv1 = TexMobject(r"\Vert \vec{x} \Vert =" + str(nv1)).next_to(bracv1, UP)
        brac1 = VGroup(bracv1, normv1)
        bracv2 = Brace(vc2_n, UP)
        normv2 = TexMobject(r"\Vert \vec{y} \Vert =" + str(nv2)).next_to(bracv2, UP)
        brac2 = VGroup(bracv2, normv2)
        bracv3 = Brace(vc3_n, UP)
        normv3 = TexMobject(r"\Vert \vec{z} \Vert =" + str(nv3)).next_to(bracv3, UP)
        brac3 = VGroup(bracv3, normv3)
        bracv4 = Brace(vc4_n, UP)
        normv4 = TexMobject(r"\Vert \vec{w} \Vert =" + str(nv4)).next_to(bracv4, UP)
        brac4 = VGroup(bracv4, normv4)
        normdot = TexMobject(r"\Vert \vec{0} \Vert = 0").next_to(ddot, DOWN)

        obse1 = TextMobject("Todos estos vectores tuvieron").shift(3 * LEFT + UP)
        obse2 = TextMobject("una norma mayor a cero.").next_to(obse1, DOWN)
        obse = VGroup(obse1, obse2)
        obscero = TexMobject(r"\text{Ahora para el vector}\ \vec{0}").to_edge(UP)
        unico = TextMobject("¡Es el único cuya norma se anula!").shift(0.5 * UP)



        self.add(plano)
        self.play(ShowCreation(plano, runtime=2))
        self.play(Write(Group11))
        self.play(ShowCreation(vcts, runtime=2), Write(labels))
        self.wait(2)
        self.play(FadeOut(plano))
        self.wait()
        self.play(Write(normies), FadeOut(labels))
        self.play(ddot.shift, 0.5 * UP + 4 * RIGHT,
                  run_time=1,
                  path_arc=1)
        self.wait()
        self.play(ReplacementTransform(vc1, vc1_n), ReplacementTransform(vc2, vc2_n), ReplacementTransform(vc3, vc3_n),
                  ReplacementTransform(vc4, vc4_n))
        self.play(ShowCreation(brac1))
        self.wait()
        self.play(FadeOut(vc1_n), ReplacementTransform(brac1, brac2))
        self.wait(1.3)
        self.play(FadeOut(vc2_n), ReplacementTransform(brac2, brac3))
        self.wait(1.3)
        self.play(FadeOut(vc3_n), ReplacementTransform(brac3, brac4))
        self.wait(1.3)
        self.play(FadeOut(vc4_n), FadeOut(brac4))
        self.wait(1.3)
        self.play(Write(obse))
        self.wait(1.5)
        self.play(ReplacementTransform(normies, obscero), FadeOut(obse))
        self.play(ddot.shift, 4 * LEFT)
        self.wait()
        self.play(Transform(dot, cdot), ShowCreation(normdot))
        self.wait(2)
        self.play(Transform(obscero, unico))
        self.wait(2)
        self.play(FadeOut(cdot), FadeOut(normdot), FadeOut(obscero))
        self.play(Group11.shift, 3.5 * UP, runtime=1.5)
        self.wait(2.2)
        self.play(FadeOut(Group11))

        ### SEGUNDA PROPIEDAD ###
        prop2 = TexMobject(r" \Vert \lambda \vec{x} \Vert = \vert \lambda \vert \Vert \vec{x} \Vert").to_edge(
            DOWN).scale(1.2)
        plano = NumberPlane()
        vec1 = Vector(direction=avec, color=GREEN)
        vec1_name = TexMobject(r"\vec{x}").next_to(vec1.get_center(), DOWN)
        vecesc = Vector(direction=lamb * avec, color=GREEN)
        vecesc_name = TexMobject(str(lamb) + r"\vec{x}").next_to(vecesc.get_center(), DOWN + RIGHT)
        avs = Vector(direction=-lamb * avec, color=PURPLE)
        avs_name = TexMobject(str(-1 * lamb) + r"\vec{x}").next_to(avs.get_center(), DOWN + RIGHT)
        lanorma = TextMobject("Consideremos solamente la \"longitud\" de ambos vectores").shift(3 * UP).scale(0.9)

        acostado1 = Vector(direction=np.array([np.linalg.norm(lamb * avec), 0, 0]), color=GREEN).shift(4 * LEFT + UP)
        acostado2 = Vector(direction=np.array([np.linalg.norm(-lamb * avec), 0, 0]), color=PURPLE).shift(4 * LEFT)
        abrace1 = Brace(acostado1, UP)
        abrace2 = Brace(acostado2, DOWN)
        abraces = VGroup(abrace1, abrace2)
        abracetex1 = TexMobject(r"\Vert" + str(lamb) + r"\vec{x} \Vert =" + str(lamb) + r"\Vert \vec{x} \Vert").next_to(
            abrace1, UP)
        abracetex2 = TexMobject(
            r"\Vert" + str(-lamb) + r" \vec{x}\Vert = " + str(lamb) + r"\Vert \vec{x} \Vert").next_to(abrace2, DOWN)
        abracetexs = VGroup(abracetex1, abracetex2)

        obs = TextMobject("Observemos que si el escalar es ").shift(3 * RIGHT + UP).scale(0.75)
        obs1 = TextMobject("negativo, se vuelve positivo.").next_to(obs, DOWN).scale(0.75)
        obs2 = TextMobject("Si es positivo, mantiene su signo.").next_to(obs1, DOWN).scale(0.75)
        observs = VGroup(obs, obs1, obs2)
        asimero = TextMobject("¡Así actúa la función valor absoluto!").move_to(obs).scale(0.9).shift(
            DOWN)

        Lam = TextMobject("Sobre la norma de un escalar por un vector").scale(1.2)

        prop2.bg = SurroundingRectangle(prop2, color=WHITE, fill_color=BLACK,
                                        fill_opacity=1)
        Group12 = VGroup(prop2.bg, prop2)

        self.play(FadeIn(Lam))
        self.wait(1.3)
        self.play(FadeOut(Lam))

        self.play(ShowCreation(plano, runtime=2))
        self.play(Write(Group12))
        self.wait(2)
        self.play(ShowCreation(vec1), Write(vec1_name))
        self.wait()
        self.play(ReplacementTransform(vec1, vecesc), ReplacementTransform(vec1_name, vecesc_name), ShowCreation(avs),
                  Write(avs_name))
        self.wait()
        self.play(FadeOut(plano))
        self.wait()
        self.play(Write(lanorma))
        self.wait()
        self.play(FadeOut(vecesc_name), FadeOut(avs_name), FadeOut(lanorma))
        self.play(Transform(vecesc, acostado1), Transform(avs, acostado2), ShowCreation(abraces, runtime=1),
                  Write(abracetexs))
        self.wait(2)
        self.play(Write(observs))
        self.wait(3.2)
        self.play(FadeOut(observs))
        self.play(Write(asimero))
        self.wait()
        self.play(FadeOut(asimero))
        self.play(
            prop2.shift, UP * 3.5 + RIGHT * 3,
            run_time=1,
            path_arc=2
        )
        self.wait(2)
        self.play(FadeOut(abracetexs), FadeOut(abraces), FadeOut(acostado1), FadeOut(vecesc), FadeOut(avs),
                  FadeOut(Group12))
        self.wait()

        #### TERCERA PROPIEDAD: DESIGUALDAD DEL TRIANGULO ####
        prop3 = TexMobject(r" \Vert \vec{x} + \vec{y}\Vert \leq \Vert \vec{x} \Vert+\Vert \vec{y} \Vert").shift(
            2 * DOWN).scale(1.2)
        plano = NumberPlane()
        vector1 = Vector(direction=avec, color=GREEN).shift(2.5 * LEFT)
        vector2 = Vector(direction=bvec, color=BLUE).move_to(avec + bvec / 2).shift(2.5 * LEFT)
        vecsum = Vector(direction=avec + bvec, color=YELLOW_E).shift(2.5 * LEFT)
        vector1_label = TexMobject(r"\vec{x}").next_to(vector1.get_center(), UP)
        vector2_label = TexMobject(r"\vec{y}").next_to(vector2.get_center(), UP)
        vecsum_label = TexMobject(r"\vec{x}+\vec{y}").next_to(vecsum.get_center(), DOWN)
        labels = VGroup(vector1_label, vector2_label, vecsum_label)

        tvector1 = Vector(direction=np.array([anorm, 0, 0]), color=GREEN).shift(3.5 * LEFT + UP)
        tvector2 = Vector(direction=np.array([bnorm, 0, 0]), color=BLUE).shift(
            3.5 * LEFT + UP + np.array([anorm, 0, 0]))
        tvecsum = Vector(direction=np.array([sumnorm, 0, 0]), color=YELLOW_E).shift(3.5 * LEFT + 0.5 * UP)
        tvectors = VGroup(tvector1, tvector2, tvecsum)

        brace1 = Brace(tvector1, UP)
        brace2 = Brace(tvector2, UP)
        bracesum = Brace(tvecsum, DOWN)
        lnorm1 = TexMobject(r"\Vert \vec{x} \Vert").next_to(brace1.get_center(), UP)
        lnorm2 = TexMobject(r"\Vert \vec{y} \Vert").next_to(brace2.get_center(), UP)
        lnormsum = TexMobject(r"\Vert \vec{x} + \vec{y} \Vert").next_to(bracesum.get_center(), DOWN)
        braces = VGroup(brace1, brace2, bracesum)
        lnorms = VGroup(lnorm1, lnorm2, lnormsum)
        laigualdad = TextMobject("(La igualdad se da cuando los tres vectores son colineales)").shift(3 * DOWN).scale(
            0.8)
        preguntaa = TextMobject("¿Puedes pensar en la relación entre norma y producto interno?").scale(0.9).shift(
            UP)
        preguntab = TextMobject("¿Se te ocurre otra forma distinguir que vector es más \"largo\"?").scale(
            0.9).shift(DOWN)
        edita = TextMobject("Edita el c\\'{o}digo para visualizar con m\\'{a}s vectores")


        Des = TextMobject("Desigualdad del tri\\'{a}ngulo para vectores").scale(1.2)

        self.play(FadeIn(Des))
        self.wait(1.3)
        self.play(Write(prop3))
        self.wait(0.7)
        self.play(FadeOut(Des))
        self.play(ShowCreation(vector1), ShowCreation(vector2))
        self.play(GrowArrow(vecsum), Write(labels))
        self.wait(4)
        self.play(Transform(vector1, tvector1), Transform(vector2, tvector2), Transform(vecsum, tvecsum),
                  FadeOut(labels))
        self.play(ShowCreation(braces))
        self.wait(2)
        self.play(Write(lnorms))
        self.play(prop3.shift, 0.7*UP, runtime=1)
        self.play(Write(laigualdad))
        self.wait(3)
        self.play(FadeOut(lnorms), FadeOut(braces), FadeOut(prop3), FadeOut(vector1), FadeOut(vector2), FadeOut(vecsum),
                  FadeOut(laigualdad))
        self.play(Write(preguntaa), Write(preguntab))
        self.wait(3)
        self.play(FadeOut(preguntaa), FadeOut(preguntab))
        self.wait()
        self.play(Write(edita))

        
 
##################################
#### DIFERENTES NORMAS EN R^N #####
##################################

class Normas(Scene):
    def construct(self):
        plano = NumberPlane()
        intro1 = TextMobject("Veremos como se ve un c\\'{i}rculo unitario")
        intro2 = TexMobject(r"\text{utilizando diferentes normas en }\mathbb{R}^2")
        intro2.next_to(intro1, DOWN)
        intro = VGroup(intro1, intro2)
        circ1 = TextMobject("Recordemos que la definici\\'{o}n de una circunferencia es")
        circ2 = TexMobject(r"\mathbb{S}^1=\{x\in\mathbb{R}^2 : \Vert x \Vert =1\}")
        circ2.next_to(circ1, DOWN)
        circ = VGroup(circ1, circ2)

        self.play(Write(intro))
        self.wait(2)
        self.play(ReplacementTransform(intro,circ))
        self.wait(2)
        self.play(FadeOut(circ))

        #### Norma 1 ####

        title1 = TextMobject("Norma 1")
        norm1 = TexMobject(r"\Vert x \Vert_1=\vert x_1 \vert + \vert x_2 \vert")
        norm1.next_to(title1,DOWN)
        Group1 = VGroup(title1,norm1)
        Group1.scale(0.75)
        Group1.set_color(RED)
        fig1 = Square(side_length=np.sqrt(2),color=RED)
        fig1.rotate(PI/4)

        self.play(Write(Group1))
        self.wait()
        self.play(ApplyMethod(Group1.to_edge,UP))
        self.play(ShowCreation(plano))
        self.play(ShowCreation(fig1))
        self.wait(2)
        self.play(ApplyMethod(Group1.move_to,np.array([-5,3,0])))

        #### Norma 2 ####

        title2 =TextMobject("Norma 2")
        norm2 = TexMobject(r"\Vert x \Vert_2=\left(x_1^2 + x_2^2 \right)^{1/2}")
        norm2.next_to(title2,DOWN)
        Group2 = VGroup(title2,norm2)
        Group2.scale(0.75)
        Group2.set_color(YELLOW)
        fig2 = Circle(radius=1,color=YELLOW)

        self.play(Write(Group2))
        self.wait()
        self.play(ApplyMethod(Group2.to_edge,UP))
        self.play(ShowCreation(fig2))
        self.wait(2)
        self.play(ApplyMethod(Group2.move_to,np.array([5,3,0])))

        #### Norma infinito ####

        title3 = TextMobject("Norma infinito")
        norminfty = TexMobject(r"\Vert x \Vert_{\infty} = \max\{\vert x_i \vert : i \in \{1,2\}\}")
        norminfty.next_to(title3,DOWN)
        Group3 = VGroup(title3,norminfty)
        Group3.scale(0.75)
        Group3.set_color(GREEN_SCREEN)
        fig3 = Square(side_length=2,color=GREEN_SCREEN)

        self.play(Write(Group3))
        self.wait()
        self.play(ApplyMethod(Group3.to_edge,UP))
        self.play(ShowCreation(fig3))
        self.wait(2)
        self.remove(Group1,Group2,Group3,plano,fig1,fig2,fig3)
        
        #### Norma p ####

        intro1 = TextMobject("Podemos definir una norma similar a las anteriores")
        intro2 = TexMobject(r"\text{para cada } p\in\mathbb{R},\ p\geq 1")
        intro2.next_to(intro1,DOWN)
        intro = VGroup(intro1,intro2)
        titlep = TexMobject(r"\text{Norma } p")
        normp = TexMobject(r"\Vert x \Vert_p = \left(\sum_{i=1}^n \vert x_i \vert ^p \right)^{1/p}")
        normp.next_to(titlep,DOWN)
        Groupp = VGroup(titlep,normp)
        text = TextMobject("Veamos que pasa cuando $p$ crece en $\\mathbb{R}$")

        self.play(Write(intro))
        self.wait(2)
        self.play(ReplacementTransform(intro,Groupp))
        self.wait(2)
        self.play(FadeOut(Groupp))
        self.play(Write(text))
        self.play(FadeOut(text))
        self.play(ShowCreation(plano))
        self.play(FadeIn(Group3),ShowCreation(fig3))
        self.play(ApplyMethod(Group3.to_edge,DOWN))

        n = 1

        while n<10:
            valor_sig = TexMobject(r"p="+str(n))
            valor_sig.to_edge(UP)
            self.add(valor_sig)
            D = []
            j=0
            dj=1/16
            while j<1:
                dot1 = Dot(radius=0.05,color=PINK)
                dot1_2 = Dot(radius=0.05,color=PINK)
                dot1.move_to(np.array([j,(1-j**n)**(1/n),0]))
                dot1_2.move_to(np.array([(1-j**n)**(1/n),j,0]))
                #self.add(dot1,dot1_2)
                #self.wait(0.05)
                D.append(dot1)
                D.append(dot1_2)
                j=j+dj
            j=1
            while j>0:
                dot2 = Dot(radius=0.05,color=PINK)
                dot2_2 = Dot(radius=0.05,color=PINK)
                dot2.move_to(np.array([j,-(1-j**n)**(1/n),0]))
                dot2_2.move_to(np.array([-(1-j**n)**(1/n),j,0]))
                #self.add(dot2,dot2_2)
                #self.wait(0.05)
                D.append(dot2)
                D.append(dot2_2)
                j=j-dj
            j=0
            while j>-1:
                dot3 = Dot(radius=0.05,color=PINK)
                dot3_2 = Dot(radius=0.05,color=PINK)
                dot3.move_to(np.array([j,-(1-(-j)**n)**(1/n),0]))
                dot3_2.move_to(np.array([-(1-(-j)**n)**(1/n),j,0]))
                #self.add(dot3,dot3_2)
                #self.wait(0.05)
                D.append(dot3)
                D.append(dot3_2)
                j=j-dj
            j=-1
            while j<0:
                dot4 = Dot(radius=0.05,color=PINK)
                dot4_2 = Dot(radius=0.05,color=PINK)
                dot4.move_to(np.array([j,(1-(-j)**n)**(1/n),0]))
                dot4_2.move_to(np.array([(1-(-j)**n)**(1/n),j,0]))
                #self.add(dot4,dot4_2)
                #self.wait(0.05)
                D.append(dot4)
                D.append(dot4_2)
                j=j+dj
            puntos = VGroup(*D)
            self.add(puntos)
            self.wait(0.5)
            for i in D:
                self.remove(i)
            self.remove(valor_sig)
            n=round(n + 0.2, 1)
        self.remove(plano,Group3,fig3)
        
        conclus1 = TextMobject("Vemos que tiende al ``c\\'{i}rculo'' que resulta de usar")
        conclus2 = TextMobject("la norma infinito, de ah\\'{i} su nombre.").next_to(conclus1,DOWN)
        conclus = VGroup(conclus1,conclus2)
        ejer = TextMobject("Puedes cambiar el código para verlo con más valores de $p$")

        self.play(Write(ejer))
        self.wait(2)
        self.play(FadeOut(ejer))
        self.play(Write(conclus))
        self.wait(2)
        self.play(FadeOut(conclus))
       
        
##############################
#### PROD. INTERIOR Y NORMA #####
##############################

class Producto_Interior(Scene):
    def construct(self):
        # signif = TextMobject("El significado geom\\'{e}trico del producto interno")
        titulo = TextMobject("Aspectos geom\\'{e}tricos del producto interno").scale(1.2)

        self.play(Write(titulo))
        self.wait()
        self.play(FadeOut(titulo))

        tomemos = TextMobject("Consideremos dos vectores en el plano").shift(2 * DOWN)
        vecx_label = TexMobject(r"\vec{x}")
        vecy_label = TexMobject(r"\vec{y}")
        vecx = Vector(direction=np.array([3, 3, 0]), color=BLUE).shift(2 * LEFT)
        vecy = Vector(direction=np.array([5, 0, 0]), color=GREEN).shift(2 * LEFT)
        vecx_label.next_to(vecx, LEFT).shift(RIGHT)
        vecy_label.next_to(vecy, DOWN)

        self.play(Write(tomemos))
        self.play(GrowArrow(vecx), GrowArrow(vecy))
        self.play(Write(vecx_label), Write(vecy_label))
        self.wait(3)

        lambdukis = TexMobject(
            r"\text{¿Qué valor de}\ \lambda\ \text{hace a}\ \vec{y}\ \text{y}\ \vec{x}-\lambda\vec{y}\ \text{perpendiculares?}")
        lambdukis.move_to(tomemos)
        vecesp = Vector(direction=3 * UP).shift(1 * RIGHT)
        vecesp_label = TexMobject(r'\vec{x}-\lambda\vec{y}').next_to(vecesp, RIGHT)
        ylambd = Vector(direction=3 * RIGHT).shift(2 * LEFT).set_color(YELLOW)
        ylambd_label = TexMobject(r"\lambda\vec{y}").move_to(vecy_label)
        self.play(FadeOut(tomemos))
        self.play(Write(lambdukis))
        self.wait(5)
        self.play(Transform(vecy_label, ylambd_label))
        self.play(Write(vecesp_label), GrowArrow(vecesp), GrowArrow(ylambd))
        self.wait(2)
        self.play(FadeOut(vecx), FadeOut(vecx_label), FadeOut(vecy),
                  FadeOut(vecy_label), FadeOut(ylambd), FadeOut(ylambd_label), FadeOut(lambdukis),
                  FadeOut(vecesp), FadeOut(vecesp_label))
        self.wait(3)

        recordemos = TextMobject('Para responder a esta pregunta, basta recordar que').shift(2 * UP)
        norm = TexMobject(r' \Vert \vec{x} \Vert = \sqrt{x_1^2+x_2^2}')
        denota = TexMobject(r'\text{representa la longitud del vector}\ \vec{x}').shift(2 * DOWN)
        grupo1 = VGroup(recordemos, norm, denota)
        pitagoras = TextMobject("Utilicemos el Teorema de Pit\\'{a}goras en nuestro tri\\'{a}ngulo").shift(2 * DOWN)
        normx = TexMobject(r'\Vert \vec{x} \Vert').move_to(vecx_label)
        normlam = TexMobject(r'\Vert \lambda\vec{y} \Vert').move_to(ylambd_label).shift(0.5 * LEFT)
        normesp = TexMobject(r'\Vert \vec{x}-\lambda\vec{y} \Vert').move_to(vecesp_label)
        pitriangulo = TexMobject(
            r"\Vert \lambda\vec{y} \Vert^2+\Vert \vec{x}-\lambda\vec{y} \Vert^2 = \Vert \vec{x} \Vert^2 ")
        pitriangulo.move_to(pitagoras)
        desa = TextMobject("Desarrollando esto, llegamos a la siguiente ecuaci\\'{o}n").move_to(pitriangulo).shift(DOWN)

        self.play(Write(recordemos), Write(norm), Write(denota))
        self.wait(7)
        self.play(FadeOut(recordemos), FadeOut(norm), FadeOut(denota))
        self.play(Write(pitagoras), GrowArrow(ylambd), GrowArrow(vecesp), GrowArrow(vecx))
        self.play(Write(normx), Write(normesp), Write(normlam))
        self.wait(3)
        self.play(Transform(pitagoras, pitriangulo))
        self.wait(4)
        self.play(Write(desa))
        self.wait(3)
        self.play(FadeOut(pitagoras), FadeOut(desa),
                  FadeOut(vecesp), FadeOut(normesp), FadeOut(vecx), FadeOut(normx), FadeOut(ylambd), FadeOut(normlam))
        self.wait()

        ec1 = TexMobject(r"2\lambda^2(y_1^2+y_2^2)-2\lambda(x_1y_1+x_2y_2)=0").shift(2 * UP)
        cuyo = TextMobject("Cuya soluci\\'{o}n distinta de cero es:")
        solu = TexMobject(r"\lambda = \frac{x_1y_1+x_2y_2}{\Vert \vec{y} \Vert^2}").shift(2 * DOWN)

        self.play(Write(ec1))
        self.wait(8)
        self.play(Write(cuyo))
        self.wait(3)
        self.play(Write(solu))
        self.wait(8)
        self.play(FadeOut(ec1), FadeOut(cuyo))
        self.play(
            solu.shift, UP * 5,
            run_time=1,
            path_arc=2
        )
        self.wait(2)

        xperp = Vector(direction=np.array([0, 3, 0]), color=BLUE).shift(LEFT + DOWN)
        yperp = Vector(direction=np.array([3, 0, 0]), color=GREEN).shift(LEFT + DOWN)
        kepasa = TextMobject("¿Qu\\'{e} pasa si los vectores \\textbf{ya} son perpendiculares?").shift(2.5 * DOWN)
        xperp_label = TexMobject(r"\vec{x}").next_to(xperp.get_center(), LEFT)
        yperp_label = TexMobject(r"\vec{y}").next_to(yperp.get_center(), DOWN)
        dadocaso = TexMobject(r"\text{En dado caso},\ \lambda = 0").move_to(kepasa)
        self.play(GrowArrow(xperp), GrowArrow(yperp), Write(xperp_label), Write(yperp_label), Write(kepasa))
        self.wait(5)
        self.play(Transform(kepasa, dadocaso))
        self.wait(2.4)
        self.play(FadeOut(xperp), FadeOut(xperp_label), FadeOut(yperp_label), FadeOut(yperp), FadeOut(kepasa))
        self.wait()

        newsolu = TexMobject(r"\lambda = \frac{x_1y_1+x_2y_2}{\Vert \vec{y} \Vert^2}= 0 \Rightarrow x_1y_1+x_2y_2 = 0")
        cond = TexMobject(r"(\text{Si}\ \vec{y} \neq 0)").shift(2 * DOWN)

        self.play(Transform(solu, newsolu))
        self.play(Write(cond))
        self.wait(8)
        self.play(FadeOut(solu), FadeOut(cond))

        textprodint = TextMobject("Si recordamos:").shift(2 * UP)
        prodint = TexMobject(r"\vec{x} \cdot \vec{y} = x_1y_1+x_2y_2")
        tons = TextMobject("Entonces").move_to(textprodint)
        ida = TexMobject(r"\vec{x} \perp \vec{y} \Rightarrow \vec{x} \cdot \vec{y} = 0").scale(1.2)

        self.play(Write(textprodint), Write(prodint))
        self.wait(5)
        self.play(Transform(textprodint, tons), Transform(prodint, ida))
        self.wait(6)

        masymas = TextMobject("Veamos otro aspecto geom\\'{e}trico del producto interno.").shift(UP)
        regre = TextMobject("Regresemos al tri\\'{a}ngulo antes visto.")
        self.play(Transform(textprodint, masymas), Transform(prodint, regre))
        self.wait(5)

        self.play(FadeOut(textprodint), FadeOut(prodint))

        # FadeOut Todo
        vecesp = Vector(direction=3 * UP).shift(1 * RIGHT)
        vecesp_label = TexMobject(r'\vec{x}-\lambda\vec{y}').next_to(vecesp, RIGHT)
        ylambd = Vector(direction=3 * RIGHT).shift(2 * LEFT).set_color(YELLOW)
        ylambd_label = TexMobject(r"\lambda\vec{y}").next_to(ylambd).shift(2 * LEFT + 0.5 * DOWN)
        vecx = Vector(direction=np.array([3, 3, 0]), color=BLUE).shift(2 * LEFT)
        vecx_label = TexMobject(r"\vec{x}").next_to(vecx, LEFT).shift(RIGHT)
        vecy = Vector(direction=np.array([5, 0, 0]), color=GREEN).shift(2 * LEFT)
        vecy_label = TexMobject(r"\vec{y}").next_to(vecy).shift(0.5 * DOWN)

        self.play(GrowArrow(vecx), GrowArrow(vecesp), GrowArrow(vecy))
        self.play(Write(vecx_label), Write(vecesp_label), Write(vecy_label))

        arco = ArcBetweenPoints(np.array([1, 0, 0]), np.array([0.7, 0.7, 0])).shift(2 * LEFT)
        arco_label = TexMobject(r"\theta").next_to(arco, RIGHT)
        angulis = TexMobject(r"\text{Consideremos el \'{a}ngulo entre}\ \vec{x}\ \text{y}\ \vec{y}").shift(2 * DOWN)
        utilizando = TextMobject("Utilizando identidades trigonom\\'{e}tricas, sabemos que").move_to(angulis)
        coseno = TexMobject(r"\cos\theta = \frac{\Vert \lambda\vec{y}\Vert}{\Vert \vec{x}\Vert}").move_to(angulis)
        demo = TexMobject(r"\text{...se puede demostrar que independientemente del signo de}\ \lambda...").scale(
            0.8).move_to(angulis).shift(DOWN)

        self.play(GrowArrow(arco))
        self.play(GrowArrow(ylambd))
        self.play(Write(arco_label), Write(ylambd_label), Write(angulis))
        self.wait(3)
        self.play(Transform(angulis, utilizando))
        self.wait(3)
        self.play(Transform(angulis, coseno), FadeOut(vecy), FadeOut(vecy_label))
        self.wait(4)
        self.play(Write(demo))
        self.wait(4)

        cos2 = TexMobject(r"\cos\theta = \lambda \frac{\Vert \vec{y}\Vert}{\Vert \vec{x}\Vert}").move_to(angulis)

        self.play(FadeOut(angulis))
        self.play(Write(cos2))
        self.wait(5)
        self.play(FadeOut(vecx), FadeOut(vecx_label), FadeOut(vecesp), FadeOut(vecesp_label), FadeOut(ylambd_label),
                  FadeOut(ylambd), FadeOut(demo), FadeOut(arco), FadeOut(arco_label))
        self.play(
            cos2.shift, UP * 5,
            run_time=1,
            path_arc=0
        )

        lambda_d = TexMobject(
            r"\text{Se dedujo anteriormente que}\  \lambda =\frac{\vec{x} \cdot \vec{y}}{\Vert \vec{y} \Vert^2}")
        lambda_dd = TexMobject(r"\text{Sustituyendo lo anterior...}")
        cos3 = TexMobject(r"\cos\theta = \frac{\vec{x}\cdot\vec{y}}{\Vert \vec{x} \Vert\Vert \vec{y} \Vert}").shift(
            2 * DOWN)

        self.play(Write(lambda_d))
        self.wait(6)
        self.play(Transform(lambda_d, lambda_dd), Write(cos3))
        self.wait(7)

        yasi = TextMobject("Y as\\'{i}..").shift(2 * UP)
        thetatex = TexMobject(
            r"\theta = \arccos(\frac{\vec{x}\cdot\vec{y}}{\Vert \vec{x} \Vert\Vert \vec{y} \Vert}),\ \theta \in [0,\pi]").scale(
            1.2)

        self.play(FadeOut(cos2), Transform(lambda_d, yasi), FadeOut(cos3))
        self.play(Write(thetatex))
        self.wait(8
                  )
        # thetatex2 = TexMobject(r"\theta = \arccos(\frac{\vec{x}\cdot\vec{y}}{\Vert \vec{x} \Vert\Vert \vec{y} \Vert})")
        siahora = TexMobject(r"\text{Si ahora}\ \vec{x} \cdot \vec{y}=0 ").shift(3 * UP)
        regreso = TexMobject(r" \theta = \arccos(0) = \pi").shift(1.5 * UP)
        esdecir = TexMobject(r"\vec{x} \cdot \vec{y} = 0 \Rightarrow \vec{x} \perp \vec{y}").scale(1.5)

        self.play(Transform(lambda_d, siahora), Transform(thetatex, regreso), Write(esdecir))
        self.wait(4)

        enresumen = TextMobject("En resumen, vimos dos caracter\\'{i}sticas del producto interno").shift(2.5 * UP)

        sii = TexMobject(r"1)\ \vec{x} \cdot \vec{y} = 0 \Leftrightarrow \vec{x} \perp \vec{y}").shift(UP).scale(1.2)
        thetaa = TexMobject(
            r"2)\ \theta = \arccos(\frac{\vec{x}\cdot\vec{y}}{\Vert \vec{x} \Vert\Vert \vec{y} \Vert}),\ \theta \in [0,\pi]").scale(
            1).shift(DOWN)

        esun = TextMobject("¡Este producto es m\\'{a}s que s\\'{o}lo una f\\'{o}rmula!").shift(2.5 * DOWN)
        self.play(Transform(lambda_d, enresumen), FadeOut(thetatex), FadeOut(esdecir))
        self.play(Write(sii))
        self.wait(5)
        self.play(Write(thetaa))
        self.play(Write(esun))

        self.wait(8)

        self.play(FadeOut(lambda_d), FadeOut(sii), FadeOut(thetaa), FadeOut(esun))
        self.wait()
