from manimlib.imports import *

#########################################################
#### PROPIEDAD DISTRIBUTIVA EN UN ESPACIO VECTORIAL #####
#########################################################

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