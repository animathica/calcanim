from manimlib.imports import *

########################################
#### BASES DE ESPACIOS VECTORIALES #####
########################################

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