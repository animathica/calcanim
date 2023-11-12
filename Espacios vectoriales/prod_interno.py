from manimlib.imports import *

#######################################
#### PRODUCTO INTERNO DE VECTORES #####
#######################################

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