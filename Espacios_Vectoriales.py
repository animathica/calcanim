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
