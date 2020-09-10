# Para versiones anteriores de manim
#from big_ol_pile_of_manim_imports import * 

# Para versiones mas recientes de manim
from manimlib.imports import *

#### Todo lo necesario para la parte de los 3 cuerpos en este script ####

#m_1 = float(input('Dame la masa 1, te recomeindo uses 1/10000 \n'))
#m_2 = float(input('Dame la masa 2, te recomeindo uses 2 \n'))
#m_3 = float(input('Dame la masa 3, te recomeindo uses 11/100 \n'))
m_1 = 1/10000
m_2 = 2
m_3 =11/100
G = 100

#posiblemente despues necesite los radios de los objetos.

#posiciones iniciales:
p_0_1 = np.array((35,0,0))
p_0_2 = np.array((0,0,0))
p_0_3 = np.array((25,0,0))
#velocidades iniciales:
v_0_1 = np.array((0,3,0))
#v_0_2 = np.array((0,10,0))
v_0_3 = np.array((0,2,0))
#momentos iniciales:
m_0_1 = m_1*v_0_1
m_0_3 = m_3*v_0_3
m_0_2 = -(m_0_1+m_0_3)
#lista posiciones:
Posiciones_t = [[],[],[]]
Posiciones_l = [[],[],[]]

t=0
dt=1.5

while t<400:
    r12 = p_0_2 - p_0_1
    r13 = p_0_3 - p_0_1
    r23 = p_0_3 - p_0_2
    
    r12_unit = (1/(np.linalg.norm(r12)))*r12
    r13_unit = (1/(np.linalg.norm(r13)))*r13
    r23_unit = (1/(np.linalg.norm(r23)))*r23
    
    ##calculando fuerza:
    c12 = (G*m_1*m_2)/((np.linalg.norm(r12))**2)
    c13 = (G*m_1*m_3)/((np.linalg.norm(r13))**2)
    c23 = (G*m_2*m_3)/((np.linalg.norm(r23))**2)
    
    F12 = c12*r12_unit
    F13 = c13*r13_unit
    F21 = -F12
    F23 = c23*r23_unit
    F31 = -F13
    F32 = -F23
    
    ##cambiando el momento: p_0 + f*dt:
    m_0_1 = m_0_1 + dt*(F12 + F13)
    m_0_2 = m_0_2 + dt*(F21 + F23)
    m_0_3 = m_0_3 + dt*(F31 + F32)
    
    ##nueva poscición:
    p_0_1 = p_0_1 + (dt/m_1)*m_0_1
    p_0_2 = p_0_2 + (dt/m_2)*m_0_2
    p_0_3 = p_0_3 + (dt/m_3)*m_0_3
    
    ##anexa la posición:
    Posiciones_t[0].append(tuple(p_0_1))
    Posiciones_t[1].append(tuple(p_0_2))
    Posiciones_t[2].append(tuple(p_0_3))
    
    Posiciones_l[0].append(p_0_1)
    Posiciones_l[1].append(p_0_2)
    Posiciones_l[2].append(p_0_3)
    
    #nuevo tiempo:
    t = t+dt

X_1 = [i[0]/50 for i in Posiciones_l[0]]
Y_1 = [i[1]/50 for i in Posiciones_l[0]]
Z_1 = [i[2]/50 for i in Posiciones_l[0]]

X_2 = [i[0]/50 for i in Posiciones_l[1]]
Y_2 = [i[1]/50 for i in Posiciones_l[1]]
Z_2 = [i[2]/50 for i in Posiciones_l[1]]

X_3 = [i[0]/50 for i in Posiciones_l[2]]
Y_3 = [i[1]/50 for i in Posiciones_l[2]]
Z_3 = [i[2]/50 for i in Posiciones_l[2]]

posiciones_1 = [(i,j,k) for i,j,k in zip(X_1, Y_1, Z_1)]
posiciones_2 = [(i,j,k) for i,j,k in zip(X_2, Y_2, Z_2)]
posiciones_3 = [(i,j,k) for i,j,k in zip(X_3, Y_3, Z_3)]


#### Previo para los campos vectoriales ####

#Escalares para campo tipo Lotka-Volterra
a,b,c,d= 5,4,6,13
# Campo vectorial tipo Lotka-Volterra
def get_lotvol_x(point):
    x,y = point[0:2]
    return a*(x+5)-b*(x+5)*(y+3.5)
def get_lotvol_y(point):
    x,y = point[0:2]
    return c*(x+5)*(y+3.5)-d*(y+3.5) 
def lotkavolt(point):
    return (get_lotvol_x(point)*RIGHT+get_lotvol_y(point)*UP)*0.1  

# Campo vectorial rotacional
def curlfunc(point):
    x,y=point[:2]
    return (-y*RIGHT+x*UP)


# Reto: Construye tu propio campo vectorial

# Campo vectorial retosducido por el estudiante
#def micampo(point):
#    x,y=point[:2]
#    return alto*RIGHT+otracosa*UP


#### Parte de curvas ('orbitas) ####

class intro(Scene):
    def construct(self):
        
        ##### El problema de los 3 cuerpos ###
        planetintro = TextMobject("Consideremos tres planetas en \\'{o}rbita").to_edge(UP)
        estrella = Dot()
        planeta = Dot()
        satelite = Dot()

        estrella.set_color(YELLOW)\
                .move_to((X_1[0],Y_1[0],Z_1[0]))
        planeta.set_color(RED)\
               .move_to((X_2[0],Y_2[0],Z_2[0]))
        satelite.set_color(BLUE)\
                .move_to((X_3[0],Y_3[0],Z_3[0]))

        self.play( Write(estrella), Write(planeta), Write(satelite), Write(planetintro))

        E = []
        P = []
        S = []

        for i,j,k in zip(posiciones_1, posiciones_2, posiciones_3):
            self.remove(estrella, planeta, satelite)
            
            estrella_sig = Dot()
            estrella_sig_aux = Dot(radius = 0.01)
            planeta_sig = Dot()
            planeta_sig_aux = Dot(radius = 0.01)
            satelite_sig = Dot()
            satelite_sig_aux = Dot(radius = 0.01)

            estrella_sig.move_to(i)\
                        .set_color(RED)
            estrella_sig_aux.move_to(i)
            planeta_sig.move_to(j)\
                       .set_color(YELLOW)
            planeta_sig_aux.move_to(j)
            satelite_sig.move_to(k)\
                        .set_color(BLUE)
            satelite_sig_aux.move_to(k)

            E.append(estrella_sig_aux)
            P.append(planeta_sig_aux)
            S.append(satelite_sig_aux)

            self.add(estrella_sig_aux, planeta_sig_aux, satelite_sig_aux, estrella_sig, planeta_sig, satelite_sig)
            self.wait(0.1)
            
            estrella = estrella_sig 
            planeta = planeta_sig
            satelite = satelite_sig

        intr = TextMobject(
            "Vale la pena pensar"
            )
        intr2 = TextMobject(
            "en las siguientes preguntas:"
            )
        intr2.next_to(intr, DOWN, buff = 0.5)
        intro = VGroup(intr, intr2)
        intro.move_to((0,2.5,0))

        preg1_1 = TextMobject(
            "¿El movimiento de uno de los cuerpos puede verse con"
            )
        preg1_2 = TexMobject(
            r"\text{funciones de } \mathbb{R} \text{ a } \mathbb{R}?"
	    )
        preg1_2.next_to(preg1_1, DOWN, buff = 0.5)
        preg1 = VGroup(preg1_1,preg1_2)
        preg1.move_to((0,2.5,0))

        preg5_1 = TextMobject("¿Qu\\'{e} tipo de función podemos utilizar para describir la")
        preg5_2 = TextMobject("posici\\'{o}n de un planeta en cada momento?")
        preg5_2.next_to(preg5_1,DOWN)
        preg5 = VGroup(preg5_1,preg5_2)
        preg5.move_to((0,2.5,0))

        preg6 = TextMobject("¿Cu\\'{a}l es el dominio y qu\\'{e} representa su variable?")
        preg6.move_to((0,2.5,0))

        preg7 = TextMobject("¿Cu\\'{a}l es su contradominio y qu\\'{e} representan sus elementos?")
        preg7.move_to((0,2.5,0))

        preg2_1 = TextMobject(
		"¿C\\'{o}mo se relaciona esa funci\\'{o}n con"
		)
        preg2_2 = TextMobject(
		"la trayectoria del planeta?"
		)
        preg2_1.next_to(preg2_2, UP, buff = 0.5)
        preg2 = VGroup(preg2_1,preg2_2)
        preg2.move_to((0,2.5,0))

        preg4_1 = TextMobject(
            "Y para ver el movimiento de los tres con una sola funci\\'{o}n,"
            )
        preg4_2 = TextMobject(
            "¿qu\\'{e} dominio y codominio tendr\\'{i}a?"
	    )
        preg4_2.next_to(preg4_1, DOWN, buff = 0.5)
        preg4 = VGroup(preg4_1,preg4_2)
        preg4.move_to((0,2.5,0))

        preg3_1 = TextMobject(
		"Imagina la gr\\'{a}fica de una"
		)
        preg3_2 = TexMobject(
		r"\text{funci\'{o}n } f:\mathbb{R} \to \mathbb{R}^2."
		)
        preg3_2.next_to(preg3_1,DOWN)
        preg3 = VGroup(preg3_1,preg3_2)
        preg3.move_to((0,2.5,0))

        self.play(FadeOut(planetintro))
        self.play(Write(intro))
        self.wait(2)
        self.play(ReplacementTransform(intro,preg1))
        self.wait(3)

        self.play(ReplacementTransform(preg1,preg5))
        self.wait(3)
        
        self.play(ReplacementTransform(preg5,preg6))
        self.wait(2)

        self.play(ReplacementTransform(preg6,preg7))
        self.wait(2)

        self.play(ReplacementTransform(preg7,preg2))
        self.wait(2)

        self.play(ReplacementTransform(preg2,preg4))
        self.wait(3)

        self.play(ReplacementTransform(preg4,preg3))
        self.wait(2)
        self.play(FadeOut(preg3))
        self.remove(estrella,planeta,satelite,estrella_sig_aux,planeta_sig_aux,satelite_sig_aux)
        for i in E:
            self.remove(i)
        for j in P:
            self.remove(j)
        for k in S:
            self.remove(k)
        
        #### Se crea un ejemplo para introducir las flechas a utilizar más adelante ####
        ### Parte de "transici'on"###
        conex = TextMobject("Imaginemos ahora una \\'{o}rbita circular:")
        conex.to_edge(UP)
        planeta.move_to(np.array([2,0,0]))
        self.play(Write(conex))
        self.add(planeta)

        t=0
        dt=0.2
        P2=[]
        while t<20:
            self.remove(planeta)

            planeta_sig = Dot()
            planeta_sig_aux = Dot(radius = 0.01)

            planeta_sig.move_to(np.array([2*np.cos(t),2*np.sin(t),0]))
            planeta_sig.set_color(RED)
            planeta_sig_aux.move_to(np.array([2*np.cos(t),2*np.sin(t),0]))

            P2.append(planeta_sig_aux)

            self.add(planeta_sig_aux,planeta_sig)
            self.wait(0.1)
            
            planeta = planeta_sig

            t=t+dt
        preg_vel1 = TextMobject("¿Qu\\'{e} tipo de funci\\'{o}n necesitamos para conocer")
        preg_vel2 = TextMobject("la velocidad del planeta en cada posici\\'{o}n?")
        preg_vel2.next_to(preg_vel1,DOWN)
        preg_vel = VGroup(preg_vel1,preg_vel2)
        preg_vel.to_edge(UP)
        expl1 = TextMobject("Pensemos en la velocidad como una flecha.")
        expl1.to_edge(UP)
        expl2 = TextMobject("As\\'{i}, a cada punto de la \\'{o}rbita le corresponde una flecha.")
        expl2.to_edge(UP)

        self.play(ReplacementTransform(conex,preg_vel))
        self.wait(2)
        self.play(ReplacementTransform(preg_vel,expl1))
        self.wait()
        self.play(ReplacementTransform(expl1,expl2))
        self.remove(planeta)
        for i in P2:
            self.remove(i)

        t=0
        dt=0.2
        P2=[]
        planeta_vel = Vector(direction=np.array([-2*np.sin(t),2*np.cos(t),0]))
        while t<20:
            self.remove(planeta,planeta_vel)

            planeta_sig = Dot()
            planeta_sig_aux = Dot(radius = 0.01)
            planeta_vel_sig = Vector(direction=np.array([-2*np.sin(t),2*np.cos(t),0]))

            planeta_sig.move_to(np.array([2*np.cos(t),2*np.sin(t),0]))
            planeta_sig.set_color(RED)
            planeta_vel_sig.move_to(np.array([2*np.cos(t)-np.sin(t),2*np.sin(t)+np.cos(t),0]))
            planeta_sig_aux.move_to(np.array([2*np.cos(t),2*np.sin(t),0]))

            P2.append(planeta_sig_aux)

            self.add(planeta_sig_aux,planeta_sig,planeta_vel_sig)
            self.wait(0.1)
            
            planeta = planeta_sig
            planeta_vel = planeta_vel_sig

            t=t+dt
        self.remove(planeta,planeta_vel)
        for i in P2:
            self.remove(i)
        self.wait()
        self.play(FadeOut(expl2))

        #### Parte de campos vectoriales ####

        title = TextMobject("Como cada flecha se puede representar con un par ordenado,")
        title2 = TextMobject("esto nos hace pensar en funciones del plano en el plano.")
        title2.next_to(title,DOWN)
        transform_title = TextMobject("Estas funciones suelen verse as\\'{i}:").scale(1.5)
        efe = TexMobject("F(x,y)=(f_x(x,y),f_y(x,y))").scale(1.3)
        curl = TexMobject("F(x,y)=(-y,x)").scale(1.3)
        efe.scale(1.5)     
        # Se crea el campo vectorial con la función CurlFunc
        vector_field_curl = VectorField(curlfunc, x_min=-5,x_max=5,y_min=-3,y_max=2.6)       
        ltkvolt = TexMobject(
            "F(x,y)=(\\alpha x-\\beta xy, \\gamma xy - \\delta y), \ \\alpha,\\beta,\\gamma,\\delta \\in \mathbb{R}^+ "
        )
        ltkvolt.scale(1)
        ltkvolt.shift(3.5*UP)
        # Se crea el campo vectorial con el campo tipo Lotka-Volterra
        vector_field_LV = VectorField(lotkavolt, x_min=-5,x_max=5,y_min=-3.5,y_max=2.5)

        
        self.play(
            Write(title),
            Write(title2)
        )
        self.wait(2)
        self.play(
            Transform(title, transform_title),
            FadeOutAndShiftDown(title2)
            )
        self.wait()
        self.play(
            FadeOut(title)
            )
        self.play(
            Write(efe)
        )
        self.play(
            ReplacementTransform(efe,curl)
        )
        self.wait()
        self.play(
                curl.shift, UP*3.58,
                run_time=1,
                path_arc=0
        )
        # Dibujamos el campo vectorial "curl" de forma gradual
        self.play(*[GrowArrow(vec) for vec in vector_field_curl])
        self.wait()
        self.play(
            ReplacementTransform(curl,ltkvolt),
            ReplacementTransform(vector_field_curl,vector_field_LV) # Cambiamos por el campo LV
            )
        self.wait(1.5)

        self.play(
            FadeOut(ltkvolt),
            FadeOut(vector_field_LV)
            ) 
        self.wait()

        # RETO: Revisa el código anterior para dibujar tu propio campo vectorial
        # según el campo vectorial que se definió en la introducción
        
        ### Sección de Preguntas campos vectoriales###
        retos = TextMobject("Pensemos ahora en las siguientes preguntas:").scale(1.3)
        preg1_1 = TextMobject(
            "¿Cual es el dominio y contradominio"
            )
        preg1_2 = TextMobject(
            "de las funciones que acabamos de ver?"
            )
        preg1_1.next_to(preg1_2,UP)
        preg1 = VGroup(preg1_1,preg1_2)

        preg2_1 = TextMobject(
            "Trata de imaginar funciones con dominio/contradominio"
            )
        preg2_2 = TexMobject(
            r"\text{en } \mathbb{R}^3 \text{ y en } \mathbb{R}^4."
            )
        preg2_2.next_to(preg2_1,DOWN)
        preg2 = VGroup(preg2_1,preg2_2)
        extra = TextMobject(
            "Intenta dibujar las siguientes funciones:"
            )
        extra.move_to(np.array([0,2,0]))
        campo1 = TexMobject(
            r"F_1(x,y)=(0,-g)\ g\in\mathbb{R}^{+}"
            )
        campo1.next_to(extra,DOWN)
        campo2 = TexMobject(
            r"F_2(x,y)=(B,-g)\ B\in\mathbb{R},g\in\mathbb{R}^{+}"
            )
        campo2.next_to(campo1,DOWN)
        campo3 = TexMobject(
            r"F_3(x,y)=(x,x)"
            )
        campo3.next_to(campo2,DOWN)
        gropuo = VGroup(campo1,campo2,campo3)
        masretos = TextMobject(
            "Encuentra m\\'{a}s retos en el c\\'{o}digo de este video."
        ).shift(2*DOWN)
        
        self.play(Write(retos))
        self.wait()
        self.play(ReplacementTransform(retos,preg1))
        self.wait()
        self.play(ApplyMethod(preg1.to_edge,UP))

        self.play(Write(preg2))
        self.wait()
        self.play(ApplyMethod(preg2.to_edge,DOWN))
        self.play(FadeOut(preg1),FadeOut(preg2))

        self.play(Write(extra))
        self.play(Write(campo1))
        self.wait()
        self.play(Write(campo2))
        self.wait()
        self.play(Write(campo3))
        self.wait()
        self.play(Write(masretos))
        self.wait() 
        self.remove(extra,campo1,campo2,campo3,masretos)

        #### Autores y créditos ####

        autor1 = TextMobject("Bruno Ram\\'{i}rez")
        autor1.scale(0.8)
        contact1 = TextMobject("GitHub: @brunormzg")
        contact1.scale(0.6)
        contact1.next_to(autor1,DOWN)
        aut1 = VGroup(autor1,contact1)

        autor2 = TextMobject("Donaldo Mora")
        autor2.scale(0.8)
        autor2.next_to(contact1,DOWN)
        contact2 = TextMobject("Instagram: donal\\_mora")
        contact2.scale(0.6)
        contact2.next_to(autor2,DOWN)
        aut2 = VGroup(autor2,contact2)

        autor3 = TextMobject("Rodrigo Moreno")
        autor3.scale(0.8)
        autor3.next_to(contact2,DOWN)
        contact3 = TextMobject("Instagram: \\_nosoyro")
        contact3.scale(0.6)
        contact3.next_to(autor3,DOWN)
        aut3 = VGroup(autor3,contact3)

        self.play(Write(aut1),Write(aut2),Write(aut3))