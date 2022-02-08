from manimlib.imports import *

#########################################
####  TEOREMA PUENTE DE SUCESIONES  #####
#########################################

class Teo_Puente(Scene):
    def construct(self):

        plano = NumberPlane()

        title = TextMobject('''Teorema Puente''')
        title.scale(1.2)
        title.set_color(YELLOW)
        intro = TextMobject('''El teorema dice:''').shift(2 * UP)
        teo1 = TexMobject(
            r'''\text{Sea } \{X_n\}\subset\mathbb{R}^m\text{ sucesi\'{o}n. } \forall k\in\{1,...,m\} \lim_{n\to\infty}X_{n,k}=L_k''')
        teo2 = TexMobject(r'''\Longleftrightarrow \lim_{n\to\infty} X_{n}=L=(L_1,...,L_k,...,L_m)''')
        teo2.next_to(teo1, DOWN)
        teo = VGroup(teo1, teo2)
        ejemplos = TextMobject("Veamos algunos ejemplos de su aplicación")



        ## Primer ejemplo ##

        ejem1 = TexMobject(r'''X_n=\left(\frac{6}{n},0\right)''').shift(1.5 * UP)
        desc1 = TexMobject(r'''\Rightarrow X_{n,1}=\frac{6}{n}\quad X_{n,2}=0''')
        teoapl1 = TexMobject(
            r'''\lim_{n\to\infty}\frac{6}{n}=0,\ \lim_{n\to\infty}0=0\Rightarrow\lim_{n\to\infty}X_n=(0,0)''').shift(
            1.5 * DOWN)
        vis = TextMobject('''Veamos esta sucesi\\'{o}n''')
        ejem1.set_color(RED)
        ejem1.bg = SurroundingRectangle(ejem1, color=RED, fill_color=BLACK,
                                         fill_opacity=1)
        Group11 = VGroup(ejem1.bg, ejem1)



        suce1 = []
        for n in range(1, 101):
            x_n = Dot(point=np.array([6 / n, 0, 0]), radius=0.05, color=RED)
            suce1.append(x_n)
        sucesion1 = VGroup(*suce1)



        ## Segundo ejemplo ##

        ejem2 = TexMobject(r'''X_n  =\left(\frac{n}{10},\frac{1}{n}\right)''').shift(1.5 * UP)
        desc2 = TexMobject(r'''\Rightarrow X_{n,1}=\frac{n}{10}\quad X_{n,2}=\frac{1}{n}''')
        teoapl2 = TexMobject(
            r'''\nexists\lim_{n\to\infty}\frac{n}{10} \Rightarrow \nexists\lim_{n\to\infty}X_n''').shift(1.5 * DOWN)
        vis = TextMobject('''Veamos esta sucesi\\'{o}n''')
        ejem2.set_color(YELLOW_E)
        ejem2.bg = SurroundingRectangle(ejem2, color=YELLOW_E, fill_color=BLACK,
                                        fill_opacity=1)
        Group12 = VGroup(ejem2.bg, ejem2)



        suce2 = []
        for n in range(1, 101):
            x_n = Dot(point=np.array([n / 10, 1 / n, 0]), radius=0.05, color=YELLOW_E)
            suce2.append(x_n)
        sucesion2 = VGroup(*suce2)



        ## Desaf\\'{i}o ##

        desa1 = TextMobject('''Es tu turno de usar el teorema''')
        desa2 = TextMobject('''Demuestra el valor del l\\'{i}mite de la siguiente sucesi\\'{o}n. Usa \n 
                                la definici\\'{o}n e int\\'{e}ntalo despu\\'{e}s usando el teorema puente:''').shift(UP)
        desa = TexMobject(r'''X_n=\left(6\frac{(-1)^n}{n},\frac{4}{n}\right)''').shift(DOWN)
        desa.set_color(ORANGE)
        desa.bg = SurroundingRectangle(desa, color=ORANGE, fill_color=BLACK,
                                        fill_opacity=1)
        Group13 = VGroup(desa.bg, desa)



        suce5 = []
        for n in range(1, 101):
            x_n = Dot(point=np.array([6 * (-1) ** n / n, 4 / n, 0]), radius=0.05, color=ORANGE)
            suce5.append(x_n)
        sucesion5 = VGroup(*suce5)



        #animación

        self.play(Write(title))
        self.wait(2)
        self.play(ReplacementTransform(title, intro), Write(teo))
        self.wait(20)
        self.play(FadeOut(intro), FadeOut(teo))
        self.play(Write(ejemplos))
        self.wait(3.2)

        self.play(ReplacementTransform(ejemplos, ejem1))
        self.wait(2.5)
        self.play(Write(desc1))
        self.wait(7)
        self.play(Write(teoapl1))
        self.wait(10)
        self.play(ReplacementTransform(desc1, vis), FadeOut(teoapl1))
        self.wait(2)
        self.play(Transform(ejem1, Group11))
        self.play(ApplyMethod(Group11.to_edge, UP), FadeOut(vis))
        self.add_foreground_mobjects(Group11)

        self.play(ShowCreation(plano), run_time=0.5)
        self.play(Write(sucesion1), run_time=5)
        self.wait(3)
        self.play(FadeOut(Group11), FadeOut(plano), FadeOut(sucesion1))

        self.play(Write(ejem2))
        self.wait(2.5)
        self.play(Write(desc2))
        self.wait(2)
        self.play(Write(teoapl2))
        self.wait(7)
        self.play(ReplacementTransform(desc2, vis), FadeOut(teoapl2))
        self.wait(2)
        self.play(Transform(ejem2, Group12))
        self.play(ApplyMethod(Group12.to_edge, UP), FadeOut(vis))
        self.add_foreground_mobjects(Group12)

        self.play(ShowCreation(plano), run_time=0.5)
        self.play(Write(sucesion2), run_time=5)
        self.wait(3)
        self.play(FadeOut(Group12), FadeOut(plano), FadeOut(sucesion2))

        self.play(Write(desa1))
        self.wait(2.5)
        self.play(FadeOut(desa1), Write(desa2), Write(desa))
        self.wait(15)
        self.play(Transform(desa, Group13))
        self.play(FadeOut(desa2), ApplyMethod(Group13.to_edge, UP))
        self.add_foreground_mobjects(Group13)

        self.play(ShowCreation(plano), run_time=0.5)
        self.play(Write(sucesion5), run_time=5)
        self.wait(4)
        self.play(FadeOut(plano), FadeOut(sucesion5), FadeOut(Group13))