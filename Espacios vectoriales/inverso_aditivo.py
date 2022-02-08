from manimlib.imports import *

#######################################
#### INVERSO ADITIVO DE UN VECTOR #####
#######################################

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