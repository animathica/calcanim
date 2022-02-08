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

####################################
#### ASOCIATIVIDAD DE VECTORES #####
####################################

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