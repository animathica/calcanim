from manimlib.imports import *

############################################
#### NORMA EUCLIDIANA Y SUS PROPIEDADES ####
############################################

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