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

######################################
#### CONMUTATIVIDAD CON VECTORES #####
######################################

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