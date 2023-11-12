from manimlib.imports import *

###################################
#### SUCESIONES DE CAUCHY     #####
###################################

#Definimos un Dot con métodos específicos para la escena de Suc. de Cauchy
class ACustomDot(SmallDot):
    def custom_method(self, color):
        self.set_color(color)
        self.scale(5)
        self.scale(3/5)
        return self
    def inverse_method(self):
        self.set_color(GREY)
        self.scale(1/3)
        return self

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


class SucesionDeCauchy(MovingCameraScene, Scene):
    # Necesario para que funcione la herencia doble
    def setup(self):
        Scene.setup(self)
        MovingCameraScene.setup(self)
    def construct(self):
        # Primero guardamos el estado original de la cámara
        self.camera_frame.save_state()
        plano = NumberPlane()
        titu = TextMobject("Sucesiones de Cauchy")
        bas1 = TextMobject("Revisemos la definición de una sucesión de Cauchy")
        bas2 = TextMobject("de forma geométrica.").set_color(YELLOW).next_to(bas1,DOWN)
        bas = VGroup(bas1,bas2)
        675
        suc = TexMobject(r"\text{Sea}\ \{x_n\}\ \text{una sucesión}").shift(3*LEFT+UP)
        xn = TexMobject(r"\{x_n\}=\{\frac{1}{n},\frac{1}{n}\}").shift(4*RIGHT+UP)
        # Definición en puntos de la sucesión 
        points = []
        for n in range(1,1500):
            points.append(ACustomDot(point=np.array([10/n, 10/(n), 0.0]), color = GREY).scale(1.2))
        group = VGroup(*points)

        #Definición de los puntos pequeños
        smolpoints = []
        for n in range(1,1500):
            smolpoints.append(ACustomDot(point=np.array([10/n, 10/(n), 0.0]),color = GREY).scale(0.1))
        group2 = VGroup(*smolpoints)
        
        circ_text = TexMobject(r"\text{Consideremos un círculo de diámetro}\ \varepsilon").scale(0.1).shift(0.62*UP)

        circulo1 = Circle(radius = 0.3).move_to(points[50])

        amarillo_t1 = TextMobject("A partir de cierto punto, llamémosle").move_to(circ_text).scale(0.11)
        amarillo_t2 = TexMobject(r"\vec{x}_N").scale(0.09).next_to(amarillo_t1).set_color(YELLOW).shift(0.22*LEFT)
        amarillo = VGroup(amarillo_t1,amarillo_t2)

        posteriores_t1 = TextMobject("cualesquiera dos términos posteriores").move_to(circ_text).scale(0.10).shift(0.1*LEFT)
        posteriores_t2 = TexMobject(r"\vec{x}_k, \vec{x}_l").scale(0.1).next_to(posteriores_t1).set_color(BLUE).shift(0.22*LEFT)
        posteriores_t3 = TexMobject(r"\text{distan entre sí menos que}\ \varepsilon").scale(0.1).next_to(posteriores_t1,0.15*DOWN)
        posteriores = VGroup(posteriores_t1,posteriores_t2,posteriores_t3)

        mates_1 = TexMobject(r"\text{Esto es:}\ \forall\ k,l > N, d(\vec{x}_k,\vec{x}_l)<\varepsilon").move_to(circ_text).scale(0.10).shift(0.1*LEFT)
        mates_2 = TexMobject(r" ").scale(0.08).next_to(posteriores_t1,0.15*DOWN).shift(0.22*LEFT)
        mates = VGroup(mates_1,mates_2)

        sipodemos_1 = TexMobject(r"\text{Si podemos hacer esto tomando}\ \varepsilon>0").move_to(circ_text).scale(0.10)
        sipodemos_2 = TextMobject("tan pequeño como queramos...").scale(0.1).next_to(sipodemos_1,0.15*DOWN)
        sipodemos = VGroup(sipodemos_1, sipodemos_2)

        #Definición de los puntos MAS pequeños
        smolerpoints = []
        for n in range(1,1500):
            smolerpoints.append(ACustomDot(point=np.array([10/n, 10/(n), 0.0]),color = GREY).scale(0.001))
        group3 = VGroup(*smolpoints)

        circulo2 = Circle(radius = 0.147).move_to(points[100])
        circulos = VGroup(circulo1,circulo2)
        entonces = TextMobject("¡Entonces tenemos una sucesión de Cauchy!").scale(0.05).shift(0.3*UP)

        defform1 = TexMobject(r"\text{Sea}\ \{\vec{x}_n\}\ \text{una sucesión, decimos que es de Cauchy si:}").shift(3*UP)
        defform2 = TexMobject(r"\text{para todo}\ \varepsilon>0").set_color(RED).shift(2*UP+2*LEFT)
        defform3 = TexMobject(r"\text{existe}\ N \in \mathbb{N}").set_color(YELLOW).next_to(defform2,RIGHT)
        defform4 = TexMobject(r"\text{tal que si}\ k,l > N, \Rightarrow d(\vec{x}_k,\vec{x}_l)<\varepsilon").set_color(BLUE).shift(UP)

        #Secuencia de la animación: Suc. de Cauchy
        self.play(Write(titu))
        self.wait()
        self.play(FadeOutAndShift(titu)) 
        self.play(Write(bas))
        self.wait()
        self.play(FadeOut(bas))
        self.add(plano)
        self.play(ShowCreation(plano, runtime = 1))
        self.play(Write(suc))
        self.play(ShowIncreasingSubsets(group, run_time=2.0), Write(xn))
        self.wait(2)
        # Zoom de la cámara
        self.play(FadeOut(suc), FadeOut(xn))
        self.play(
            # Establecemos tamaño refiriendo a un objeto
            self.camera_frame.set_width,bas2.get_width()*0.4,
            # Movemos la cámara a un objeto
            self.camera_frame.move_to,points[40],
            ReplacementTransform(group, group2))
        ###
        self.wait()
        self.play(Write(circ_text))
        self.wait()
        self.play(ShowCreation(circulo1))
        self.wait(2)
        self.play(FadeOut(circ_text))
        self.play(Write(amarillo))
        self.play(ApplyMethod(points[23].custom_method, YELLOW))
        self.wait(2)
        self.play(FadeOut(amarillo))
        self.play(Write(posteriores))
        self.play(ApplyMethod(points[24].custom_method, BLUE), ApplyMethod(points[50].custom_method, BLUE))
        self.wait(2)
        self.play(ApplyMethod(points[100].custom_method, BLUE), ApplyMethod(points[50].inverse_method))
        self.wait(2)
        self.play(ApplyMethod(points[500].custom_method, BLUE), ApplyMethod(points[100].inverse_method))
        self.wait(2)
        self.play(ApplyMethod(points[1498].custom_method, BLUE), ApplyMethod(points[500].inverse_method))
        self.wait(2)
        self.play(ReplacementTransform(posteriores,mates))
        self.wait(9)
        self.play(FadeOut(mates))
        self.play(Write(sipodemos),ApplyMethod(points[1498].inverse_method),ApplyMethod(points[24].inverse_method), ApplyMethod(points[23].inverse_method))
        self.wait()
        self.play(FadeOut(sipodemos))
        # Segundo zoom de la cámara
        self.play(
            # Nuevo ancho
            self.camera_frame.set_width,bas2.get_width()*0.2,
            # Nueva posición
            self.camera_frame.move_to,points[80],
            ReplacementTransform(group, group3))
        ###
        self.wait()
        self.play(ShowCreation(circulo2))
        self.wait()
        self.play(ApplyMethod(points[48].custom_method, YELLOW))
        self.wait()
        self.play(ApplyMethod(points[49].custom_method, BLUE), ApplyMethod(points[60].custom_method,BLUE))
        self.wait(2)
        self.play(ApplyMethod(points[100].custom_method, BLUE), ApplyMethod(points[60].inverse_method))
        self.wait()
        self.play(Write(entonces))
        self.wait()
        self.play(FadeOut(circulos),FadeOut(group3),FadeOut(entonces),ApplyMethod(points[100].custom_method, BLACK),
        ApplyMethod(points[48].custom_method, BLACK),ApplyMethod(points[49].custom_method, BLACK),
        ApplyMethod(points[60].custom_method, BLACK),FadeOut(plano))
        # Regresamos a la posición de cámara original
        self.play(Restore(self.camera_frame))
        self.wait()
        self.play(Write(defform1))
        self.play(Write(defform2))
        self.wait(5)
        self.play(Write(defform3))
        self.wait(3)
        self.play(Write(defform4))
        self.wait(7)
        self.play(FadeOut(defform1), FadeOut(defform2), FadeOut(defform3), FadeOut(defform4))