from manimlib.imports import *

##grid para animaciones de definicion y definicion de limite

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

#define la sucesión para usar definicion_sucesiones y definicion de limite:
n_sup = 150
cjto_pts_sucesion = []

for i in range(1,n_sup):
    x = 1/(0.2*i)
    y = 1/(0.2*i)
    cjto_pts_sucesion.append((x,y,0))

n_sup_1 = 30
cjto_pts_sucesion_1 = []
for i in range(1,n_sup_1):
    x_1 = (np.exp(i/20))*(np.cos(0.7*i))
    y_1 = (np.exp(i/20))*(np.sin(0.7*i))
    cjto_pts_sucesion_1.append((x_1,y_1,0))

###################################
#### DEFINICIÓN DE SUCESIONES #####
###################################
    
class Definicion_Sucesiones(Scene):
    def construct(self):

        ##texto:
        t_1 = TextMobject(''' \\textquestiondown Recuerdas la definici\\'{o}n de sucesiones en $\\mathbb{R}?$ ''')
        t_2 = TextMobject('''Una sucesi\\'{o}n es una funci\\'{o}n de: \n
                            $\\mathbb{N}\\rightarrow\\mathbb{R}$ ''')
        t_3 = TextMobject('''Nota que es distinto hablar del conjunto \n
                            que contiene a todos los \n
                            elementos de dicha sucesi\\'{o}n:\n
                            $\{ x_n \}$, \n
                            donde $x_n = s(n)$ y \n
                            donde $s$ es la funci\\'{o}n.''')
        t_4 = TextMobject(''' \\textexclamdown Bueno! Pues es an\\'{a}logo para \n
                            sucesiones de $\\mathbb{R}^n$. ''')
        t_5 = TextMobject('''Recuerda que un vector en $\\mathbb{R}^n$, \n
                            se ve de la siguiente forma: \n
                            $(x_1,x_2,\\dots,x_n)$, donde $x_i\\in \\mathbb{R}$, \n
                            para cualquier $i\\in \{ 1,\\dots, n \}$''')
        t_6 = TextMobject('''Por lo que para definir una sucesi\\'{o}n \n
                            en $\\mathbb{R}^n$  \n
                            basta definir una sucesi\\'{o}n para \n
                            cada entrada vectorial, es decir: \n
                            $\\vec{s}: \\mathbb{N}\\rightarrow \\mathbb{R}^n$ ''')
        t_7 = TextMobject('''O sea que: \n
                            $\\vec{s}(n) = (s_1(n),s_2(n),\\dots, s_n(n))$ \n
                            Donde $s_i$ es una sucesi\\'{o}n en $\\mathbb{R}$.''')
        t_8 = TextMobject('''Por ejemplo en $\\mathbb{R}^2$, tomemos: \n
                            $\\vec{s}(n) = ((e^{-n})\\cos(n),(e^{-n})\\sin(n))$''')
        t_9 = TextMobject('''Pintemos las parejas de la sucesi\\'{o}n en el plano:''')



        ##mas
        grid = NumberPlane()
        Elementos = [Dot(point=i).set_color(RED_E) for i in cjto_pts_sucesion_1]
        Elementos_Y = [Dot(point=i).set_color(YELLOW_E) for i in cjto_pts_sucesion_1]

        Elementos_t = [TexMobject('\\vec{s}_{%i}' % i).next_to(Elementos[i], 0.08*DOWN).set_color(YELLOW_E) for i in range(0, n_sup_1 - 1)]

        Elementos_g = VGroup(*Elementos)
        Elementos_g_Y = VGroup(*Elementos_Y)
        Elementos_t_g = VGroup(*Elementos_t)



        ##animación:
        self.play(Write(t_1))
        self.wait(2.2)
        self.play(ReplacementTransform(t_1, t_2))
        self.wait(4.3)
        self.play(ReplacementTransform(t_2, t_3))
        self.wait(11.5)
        self.play(ReplacementTransform(t_3, t_4))
        self.wait(6)
        self.play(ReplacementTransform(t_4, t_5))
        self.wait(13)
        self.play(ReplacementTransform(t_5, t_6))
        self.wait(13)
        self.play(ReplacementTransform(t_6, t_7))
        self.wait(10)
        self.play(ReplacementTransform(t_7, t_8))
        self.wait(12)
        self.play(ReplacementTransform(t_8, t_9))
        self.wait(4)
        self.play(ReplacementTransform(t_9, grid))
        self.wait()
        self.play(Write(Elementos_g),
                  Write(Elementos_t_g), run_time=6.35)
        self.wait()
        self.play(FadeOut(Elementos_t_g), ReplacementTransform(Elementos_g, Elementos_g_Y))
        self.wait(3.5)
        self.play(FadeOut(grid),FadeOut(Elementos_g_Y))
        
        
###################################
#### SUCESIONES ACOTADAS    #####
###################################

class Sucesiones_Acotadas(Scene):
    def construct(self):
        plano = NumberPlane()
        title = TextMobject('''Sucesiones acotadas''')
        text1 = TextMobject('''Considera la siguiente sucesión''').shift(UP)

        self.play(Write(title))
        self.wait()
        self.play(ReplacementTransform(title,text1))

        ejem1 = TexMobject(r"X_n=\left(3e^{-n/30}\cos\left(\frac{n}{5}\right),3e^{-n/30}\sin\left(\frac{n}{5}\right)\right)").next_to(text1,DOWN)
        
        self.play(Write(ejem1))
        self.wait()
        self.play(FadeOut(text1),FadeOut(ejem1))

        suce1 = []
        for n in range(1,151):
            x_n = Dot(point=np.array([3*np.exp(-n/30)*np.cos(n/5),3*np.exp(-n/30)*np.sin(n/5),0]),color=ORANGE)
            suce1.append(x_n)
        sucesion1 = VGroup(*suce1)

        self.play(ShowCreation(plano),run_time=0.5)
        self.play(Write(sucesion1),run_time=10)
        self.wait()
        self.play(FadeOut(plano),FadeOut(sucesion1),run_time=0.5)

        text2 = TextMobject('''Piensa en lo que representaría geométricamente \n
                                que una sucesión fuera acotada''')
        text3 = TextMobject('''Considera una bola de radio $M=3$ centrada en el origen''')
        bola = Circle(radius=3,color=RED)

        self.play(Write(text2))
        self.wait()
        self.play(ReplacementTransform(text2,text3))
        self.wait(3)
        self.play(FadeOut(text3))
        self.play(ShowCreation(plano),run_time=0.5)
        self.play(FadeIn(bola),Write(sucesion1))
        self.wait()

        text4 = TextMobject('''Puedes ver que se cumple \n
                            $\\{X_n\\}\\subset B_{M}(\\bar{0})$''',color=BLACK).scale(0.6)
        text4.bg = SurroundingRectangle(text4,color=RED,fill_color=WHITE,fill_opacity=1)
        text4.group = VGroup(text4.bg,text4).move_to(np.array([-4.5,3,0]))

        self.play(FadeIn(text4.group))
        self.wait(4)
        self.play(FadeOut(plano),FadeOut(sucesion1),FadeOut(bola),FadeOut(text4.group))

        text5 = TextMobject('''Y justo con esto es como se define sucesión acotada''')
        text6 = TextMobject('''Decimos que $\\{X_n\\}$ es acotoda si existe $M\\in\\mathbb{R}^+$ \n
                            tal que $\\{X_n\\}\\subset B_{M}(\\bar{0})$''')
        text7 = TextMobject('''Intenta demostrar que la sucesión $X_n=(n,n)$ NO es acotada\n
                                usando la definición anterior (su negación)''')

        self.play(Write(text5))
        self.wait()
        self.play(ReplacementTransform(text5,text6))
        self.wait(5)
        self.play(ReplacementTransform(text6,text7))
        self.wait(5)
        self.play(FadeOut(text7))

