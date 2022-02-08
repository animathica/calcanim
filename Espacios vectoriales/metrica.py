from manimlib.imports import *

##################################
#### MÉTRICA Y SUS PROPIEDADES #####
##################################

### Puntos para propiedad de simetría, PUEDES CAMBIARLOS ###
posa = np.array([4, 0, 0])
posb = np.array([-4, 0, 0])
distab = round(np.linalg.norm(posa - posb), 3)
distba = round(np.linalg.norm(posb - posa), 3)

### Definición de los puntos para la desigualdad del tríangulo, PUEDES CAMBIARLOS ###
posx = np.array([3, 2, 0])
posy = np.array([-2, -1, 0])
posz = np.array([-2, 1, 0])
### Distancias Desig. del triángulo - NO CAMBIAR ###
dxy = round(np.linalg.norm(posx - posy), 3)
dxz = round(np.linalg.norm(posx - posz), 3)
dzy = round(np.linalg.norm(posz - posy), 3)

class Metrica(Scene):
    def construct(self):
        dist = TextMobject("La m\\'{e}trica es un concepto relacionado con la distancia").scale(1)
        aux1 = TexMobject(r"\text{Auxiliados del concepto de norma, definimos la distancia}").to_edge(UP).shift(DOWN)
        aux2 = TexMobject(r"\text{entre dos vectores}\ \vec{x},\ \vec{y}\ \text{como}:").next_to(aux1, DOWN)
        aux = VGroup(aux1, aux2)

        defdist = TexMobject(r"d(\vec{x},\vec{y}):=\Vert \vec{x} - \vec{y}\Vert").scale(1.2)
        tprops1 = TextMobject("Una distancia se conoce como \"m\\'{e}trica\"")
        tprops2 = TextMobject(" si satisface las siguientes propiedades:").next_to(tprops1, DOWN)
        tprops = VGroup(tprops1, tprops2)

        self.play(Write(dist))
        self.wait(1.5)
        self.play(FadeOut(dist))
        self.play(Write(aux))
        self.wait(3.3)
        self.play(ReplacementTransform(aux, defdist))
        self.wait(4.8)
        self.play(FadeOut(defdist))
        self.play(Write(tprops))
        self.wait(2.7)
        self.play(FadeOut(tprops))

        # PROPIEDAD 1: DEFINIDO SEMI-POSITIVO##
        distprop1 = TexMobject(
            r"d(\vec{x},\vec{y}) \geq 0\  \text{y}\ d(\vec{x},\vec{y}) = 0 \Leftrightarrow \vec{x} = \vec{y}").shift(
            3 * DOWN)
        xdot = Dot((2, 1, 0), color=RED, radius=0.12)
        xdot_label = TexMobject(r"\vec{x}").next_to(xdot, RIGHT)
        gxdot = VGroup(xdot, xdot_label)
        ydot = Dot((-2, -1, 0), color=BLUE, radius=0.12)
        ydot_label = TexMobject(r"\vec{y}").next_to(ydot, LEFT)
        gydot = VGroup(ydot, ydot_label)
        arrow1 = DoubleArrow(xdot.get_center(), ydot.get_center())
        arrow1_label = TexMobject(r"d(\vec{x},\vec{y})").next_to(arrow1.get_center(), DOWN + RIGHT)
        dmayor = TexMobject(r"d(\vec{x},\vec{y})> 0").shift(3 * UP)
        garrow1 = VGroup(arrow1, arrow1_label)
        cerodot = Dot((0, 0, 0), color=PURPLE, radius=0.12)
        cerodot_label = TexMobject(r"\vec{x}=\vec{y}").next_to(cerodot, DOWN)
        gcerodot = VGroup(cerodot, cerodot_label)
        ceroarrow = DoubleArrow((0, 0, 0), (0, 0, 0))
        dcero = TexMobject(r"d(\vec{x},\vec{y}) = 0").shift(3 * UP)

        self.play(Write(distprop1))
        self.wait(4.5)
        self.play(ShowCreation(gxdot), ShowCreation(gydot))
        self.wait(1)
        self.play(GrowArrow(arrow1), Write(dmayor))
        self.wait(1.8)
        self.play(ReplacementTransform(gxdot, gcerodot), ReplacementTransform(ydot, cerodot),
                  Transform(arrow1, ceroarrow),
                  FadeOut(ydot_label), ReplacementTransform(dmayor, dcero), runtime=2.3)
        self.wait()
        self.play(FadeOut(gcerodot), FadeOut(dcero))
        self.play(distprop1.shift, 3 * UP)
        self.wait(1.65)
        self.play(FadeOut(distprop1))

        ### PROPIEDAD 2: SIMETRÍA ###
        distprop2 = TexMobject(r"d(\vec{x},\vec{y}) = d(\vec{y},\vec{x})").shift(3 * DOWN)
        adot = Dot(posa, color=RED, radius=0.12)
        adot_label = TexMobject(r"\vec{x}").next_to(adot, DOWN)
        gadot = VGroup(adot, adot_label)
        bdot = Dot(posb, color=BLUE, radius=0.12)
        bdot_label = TexMobject(r"\vec{y}").next_to(bdot, DOWN)
        gbdot = VGroup(bdot, bdot_label)

        ab_arrow = Arrow(adot.get_center(), bdot.get_center())
        ab_arrow_lb = TexMobject(r"d(\vec{x},\vec{y}) = " + str(distab)).next_to(ab_arrow, 3 * UP)
        ba_arrow = Arrow(bdot.get_center(), adot.get_center())
        ba_arrow_lb = TexMobject(r"d(\vec{y},\vec{x})= " + str(distba)).move_to(ab_arrow_lb)

        self.play(Write(distprop2))
        self.wait(1.3)
        self.play(ShowCreation(gadot), ShowCreation(gbdot), runtime=1.35)
        self.play(GrowArrow(ab_arrow), Write(ab_arrow_lb))
        self.wait(2)
        self.play(ReplacementTransform(ab_arrow, ba_arrow), Transform(ab_arrow_lb, ba_arrow_lb))
        self.wait(2)
        self.play(FadeOut(gadot), FadeOut(gbdot), FadeOut(ba_arrow), FadeOut(ab_arrow_lb))
        self.play(distprop2.shift, 3 * UP, runtime=1)
        self.wait(2)
        self.play(FadeOut(distprop2))

        ### PROPIEDAD 3: DESIG DEL TRIÁNGULO ###
        TRI = TextMobject("Ahora, la desigualdad del tri\\'{a}ngulo")
        distprop3 = TexMobject(r"d(\vec{x},\vec{y}) \leq d(\vec{x},\vec{z})+d(\vec{z},\vec{y})").shift(3 * DOWN)
        newxdot = Dot(posx, color=RED, radius=0.12)
        newxdot_label = TexMobject(r"\vec{x}").next_to(newxdot, DOWN)
        gnewxdot = VGroup(newxdot, newxdot_label)
        newydot = Dot(posy, color=BLUE, radius=0.12)
        newydot_label = TexMobject(r"\vec{y}").next_to(newydot, DOWN)
        gnewydot = VGroup(newydot, newydot_label)
        zdot = Dot(posz, color=YELLOW, radius=0.12)
        zdot_label = TexMobject(r"\vec{z}").next_to(zdot, UP)
        gzdot = VGroup(zdot, zdot_label)


        narrow1 = DoubleArrow(newxdot.get_center(), newydot.get_center(), stroke_width=4)
        narrow1_label = TexMobject(r"d(\vec{x},\vec{y})").next_to(narrow1.get_center(), DOWN + RIGHT)
        arrow2 = DoubleArrow(newxdot.get_center(), zdot.get_center(), stroke_width=4)
        arrow2_label = TexMobject(r"d(\vec{x},\vec{z})").next_to(arrow2.get_center(), UP)
        garrow2 = VGroup(arrow2, arrow2_label)
        arrow3 = DoubleArrow(newydot.get_center(), zdot.get_center(), stroke_width=4)
        arrow3_label = TexMobject(r"d(\vec{z},\vec{y})").next_to(arrow3.get_center(), 2 * LEFT)
        garrow3 = VGroup(arrow3, arrow3_label)

        tdxz = DoubleArrow((0, 0, 0), (dxz, 0, 0), color=RED).shift(2.5 * LEFT + UP)
        tdzy = DoubleArrow((0, 0, 0), (dzy, 0, 0), color=BLUE).shift(2.5 * LEFT + UP + (dxz * 0.9, 0, 0))
        tdxy = DoubleArrow((0, 0, 0), (dxy, 0, 0), color=YELLOW).shift(2.5 * LEFT)
        brace1 = Brace(tdxz, UP)
        brace2 = Brace(tdzy, UP)
        bracesum = Brace(tdxy, DOWN)
        ldxz = TexMobject(r"d(\vec{x},\vec{z})").next_to(brace1.get_center(), UP)
        ldzy = TexMobject(r"d(\vec{z},\vec{y})").next_to(brace2.get_center(), UP)
        ldxy = TexMobject(r"d(\vec{x},\vec{y})").next_to(bracesum.get_center(), DOWN)
        braces = VGroup(brace1, brace2, bracesum)
        dists = VGroup(ldxz, ldzy, ldxy)
        laigualdad = TextMobject("(La igualdad se da si y s\\'{o}lo si los tres puntos son colineales)").shift(DOWN).scale(0.8)
        i_1 = TextMobject("Este concepto te\\'{o}rico nos permite")
        i_2 = TextMobject("definir m\\'{e}tricas en espacios m\\'{a}s abstractos").next_to(i_1, DOWN)
        revisa = TextMobject("Edita el c\\'{o}digo para visualizar con m\\'{a}s vectores")

        Group= VGroup(i_1, i_2)

        self.play(Write(TRI), runtime = 1.2)
        self.play(FadeOut(TRI))
        self.play(Write(distprop3))
        self.wait(3.7)
        self.play(ShowCreation(gnewxdot), ShowCreation(gnewydot), ShowCreation(gzdot))
        self.wait()
        self.play(GrowArrow(arrow2), GrowArrow(arrow3))
        self.play(Write(arrow2_label), Write(arrow3_label))
        self.wait()
        self.play(GrowArrow(narrow1))
        self.play(Write(narrow1_label))
        self.wait()

        arrow2.set_color(RED)
        arrow3.set_color(BLUE)
        narrow1.set_color(YELLOW)

        self.wait(2)

        self.play(FadeOut(gnewxdot), FadeOut(gnewydot), FadeOut(gzdot))
        self.play(FadeOut(narrow1_label), FadeOut(arrow2_label), FadeOut(arrow3_label))
        self.play(ReplacementTransform(narrow1, tdxy), ReplacementTransform(arrow2, tdxz),
                  ReplacementTransform(arrow3, tdzy))
        self.play(ShowCreation(braces), ShowCreation(dists))
        self.wait(5)
        self.play(FadeOut(dists), FadeOut(braces), FadeOut(tdxy), FadeOut(tdxz), FadeOut(tdzy))
        self.play(distprop3.shift, 3 * UP, runtime=1)
        self.play(Write(laigualdad))
        self.wait(4)
        self.play(FadeOut(laigualdad), FadeOut(distprop3))
        self.wait()
        self.play(Write(Group))
        self.wait(2)
        self.play(ReplacementTransform(Group, revisa))
        self.wait()