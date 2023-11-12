from manimlib.imports import *

###################################
#### OPERACIONES CON VECTORES #####
###################################

######Hint para crear la animación
###Primero crea una clase con el nombre de animación.
###Luego necesitas crear una "construcción" (función) para que manim ejecute el objeto animación
###Luego tendrás que definir vectores...
###No solo ellos, tambien sus propiedades como en las animaciones anteriores
###Finalmente dile a la computadora cómo deben ser realizadas las animaciones con "self.play[...etc.]"

######¿Qué conclusiones geométricas puedes obtener de ésta animación?


#### Operaciones con vectores representados por flechas ####


# Puedes modificar estos parámetros para probar diferentes vectores y escalares #

a = np.array([1, 1, 0])
b = np.array([-2, 1, 0])
c = -1.5

#### considera que el plano es [-7,7]x[-4,4] ####

text_pos = np.array([-4, 2.6, 0])


class Opera(Scene):
    def construct(self):
        plano = NumberPlane()

        vec1 = Vector(direction=a, color=RED)
        vec1_name = TexMobject("a")
        vec1_name.next_to(vec1.get_corner(RIGHT + UP), RIGHT)
        vec2 = Vector(direction=b, color=GOLD_E)
        vec2_name = TexMobject("b")
        vec2_name.next_to(vec2.get_corner(LEFT + UP), LEFT)

        #### Suma ####

        vecsum = Vector(direction=a + b, color=GREEN_SCREEN)
        vecsum_name = TexMobject("a+b").set_color(GREEN_SCREEN)
        vecsum_name.next_to(vecsum, LEFT)
        suma1 = TextMobject("Podemos ver la suma de dos")
        suma2 = TextMobject("vectores con flechas")
        suma2.next_to(suma1, DOWN)
        suma = VGroup(suma1, suma2)
        suma.scale(0.75)

        suma.bg = SurroundingRectangle(suma, color=WHITE, fill_color=BLACK,
                                         fill_opacity=1)
        Group11 = VGroup(suma.bg, suma)
        #### Multiplicar por escalar ####
        vecesc = Vector(direction=c * a, color=RED)
        vecesc_name = TexMobject(str(c) + "a")
        vecesc_name.next_to(vecesc, DOWN)
        esc1 = TextMobject("Tambi\\'{e}n podemos multiplicar")
        esc2 = TextMobject("vectores por un escalar del campo")
        esc2.next_to(esc1, DOWN)
        esc = VGroup(esc1, esc2)
        esc.scale(0.75)
        valor = TexMobject(r"\text{En este caso el escalar es}" + str(c))
        valor.scale(0.75)
        valor.move_to(text_pos)

        esc.bg = SurroundingRectangle(esc, color=WHITE, fill_color=BLACK,
                                       fill_opacity=1)
        Group12 = VGroup(esc.bg, esc)

        valor.bg = SurroundingRectangle(valor, color=WHITE, fill_color=BLACK,
                                      fill_opacity=1)
        Group13 = VGroup(valor.bg, valor)
        #### Desafíos ####
        ejem = TextMobject("Puedes modificar los vectores y el escalar para probar tus propios ejemplos,").scale(0.75)
        ejem2 = TextMobject("encontrar\\'{a}s m\\'{a}s informaci\\'{o}n en el c\\'{o}digo de este video.").scale(0.75)
        ejem2.next_to(ejem, DOWN)

        #Animación
        #Animación suma
        self.play(FadeIn(Group11))
        self.play(ApplyMethod(Group11.move_to, text_pos))
        self.play(ShowCreation(plano))
        self.play(ShowCreation(vec1), ShowCreation(vec2), Write(vec1_name), Write(vec2_name))
        self.wait()
        self.play(ApplyMethod(vec2.move_to, a + b / 2), ApplyMethod(vec2_name.move_to, a + b / 2))
        self.wait()
        self.play(ShowCreation(vecsum), Write(vecsum_name))
        self.wait()
        self.play(FadeOut(vec1), FadeOut(vec2), FadeOut(vecsum), FadeOut(plano), FadeOut(Group11), FadeOut(vec1_name),
                  FadeOut(vec2_name), FadeOut(vecsum_name))
        #Animación escalar
        self.play(Write(Group12))
        self.play(ApplyMethod(Group12.move_to, text_pos))
        self.play(ShowCreation(plano))
        self.play(ShowCreation(vec1), Write(vec1_name))
        self.wait()
        self.play(ReplacementTransform(Group12, Group13))
        self.play(ReplacementTransform(vec1, vecesc), ReplacementTransform(vec1_name, vecesc_name))
        self.wait(2)
        self.play(FadeOut(plano), FadeOut(vecesc_name), FadeOut(Group13), FadeOut(vecesc))
        #Animación desafíos     
        self.play(Write(ejem), Write(ejem2))
        self.wait(3)
        self.play(FadeOut(ejem), FadeOut(ejem2))