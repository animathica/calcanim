from manimlib.imports import *

##############################################################################
################# Tipos de Curvas: simples y simples cerradas ################
##############################################################################

# Anexado 13/12/2021.

class TiposCurvas(MovingCameraScene):
    
    def curva1(self, t):
            return [t, t, 0]
    
    def curva2(self, t):
        return [np.sin(t), np.sin(t), 0]
    
    def curva3(self, t):
        return [np.cos(t), np.sin(t), 0]
    
    def construct(self):

        self.camera_frame.set_width(20) #entre mas grande mas pequeña la imagen

        # Textos de la animación.
        title = TextMobject('''Tipos de Curvas: simples \n
                                 simples cerradas''').scale(2)
        
        text1 = TextMobject('''Consideremos $C$ una curva en $\\mathbb{R}^n$ y $\\gamma(t):I\\subseteq\\mathbb{R}\\to\\mathbb{R}^n$\n su parametrización, $I$ es un intervalo.''').move_to(UP)
                            
        text2 = TextMobject("Decimos que $C$ y $\\gamma$ son simples si $\\gamma$ es inyectiva.").next_to(text1, 3*DOWN)
        
        text3 = TextMobject("Considera $\\gamma(t)=(t,t)$ con $t\\in[0,1]$, entonces $\\gamma$ es\n simple y su imagen $C$ es una curva simple.").move_to(3*UP)
                            
        text4_1 = TextMobject("Ahora considera $\\rho(t)=(sen(t),sen(t))$\n con $t\\in[0,\\pi]$, entonces $\\rho$ no es simple.").move_to(3*UP)
                            
        text4_2 = TextMobject("Observa que $Im(\\gamma)=Im(\\rho)=C$ ¿$C$ es simple o no?").move_to(3*DOWN)
                            
        text5 = TextMobject("Como una misma curva puede tener más de una \n parametrización, decimos que $C$ es simple si tiene\n alguna parametrización simple, o sea, inyectiva.")
        
        text6 = TextMobject("Decimos que $\\gamma:[a,b]\\subseteq\\mathbb{R}\\rightarrow\\mathbb{R}^n$ parametriza\n una curva simple cerrada $C$ si esta función es\n inyectiva en $[a,b)$ y $f(a)=f(b)$.")
                                                                                 
        text7 = TextMobject("Visualmente, esto significa que la curva no tiene\n intersecciones con ella misma más que en los extremos.").move_to(3*UP)
        
        gamma_curva3 = TextMobject("$\\gamma(t)=(cos(t),sen(t))$ con $t\\in[0,2\\pi]$").move_to(2.5*DOWN)
        
        gamma_curva3.scale(0.8)
        
        text8 = TextMobject("Intuitivamente esto es que sus extremos estén unidos\n para formar un \"lazo\". No olvides que $\\gamma$ es continua.").move_to(3*UP)
       
        text3.bg = SurroundingRectangle(text3, color = WHITE, fill_color = BLACK, fill_opacity = 1)
        gpo_3 = VGroup(text3.bg, text3)
        
        text4_1.bg = SurroundingRectangle(text4_1, color = WHITE, fill_color = BLACK, fill_opacity = 1)
        gpo_4_1 = VGroup(text4_1.bg, text4_1)
        
        text4_2.bg = SurroundingRectangle(text4_2, color = WHITE, fill_color = BLACK, fill_opacity = 1)
        gpo_4_2 = VGroup(text4_2.bg, text4_2)
        
        text7.bg = SurroundingRectangle(text7, color = WHITE, fill_color = BLACK, fill_opacity = 1)
        gpo_7 = VGroup(text7.bg, text7)
        
        text8.bg = SurroundingRectangle(text8, color = WHITE, fill_color = BLACK, fill_opacity = 1)
        gpo_8 = VGroup(text8.bg, text8)
        
        ejes = Axes(x_min = -2.5,
                    x_max = 2.5,
                    y_min = -2,
                    y_max = 2,
                    axis_config={"tick_frequency": 1})
        
        curva1 = ParametricFunction(self.curva1, t_min = 0, t_max = 1, color = GREEN)
        curva2_1 = ParametricFunction(self.curva2, t_min = 0, t_max = np.pi/2, color = RED)
        curva2_2 = ParametricFunction(self.curva2, t_min = np.pi/2, t_max = np.pi, color = RED)
        curva3 = ParametricFunction(self.curva3, t_min = 0, t_max = 2*np.pi, color = TEAL)
        
        # Escena
        self.play(Write(title))
        self.wait(3)
        self.play(FadeOut(title))
        
        self.play(Write(text1))
        self.wait(6)
        self.play(Write(text2))
        self.wait(3)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        self.play(Write(gpo_3))
        self.play(ShowCreation(ejes))
        self.play(ShowCreation(curva1))
        self.wait(7)
        self.play(FadeOut(gpo_3), FadeOut(curva1))
        self.play(Write(gpo_4_1))
        self.wait(3)
        self.play(ShowCreation(curva2_1))
        self.play(FadeOut(curva2_1), ShowCreation(curva2_2))
        self.wait(2)
        self.play(Write(gpo_4_2))
        self.wait(4)
        self.play(*[FadeOut(mob)for mob in self.mobjects])
        
        self.play(Write(text5))
        self.wait(8)
        self.play(FadeOut(text5))
        self.play(Write(text6))
        self.wait(9)
        self.play(FadeOut(text6))
        
        self.play(Write(gpo_7))
        self.wait(3)
        self.play(ShowCreation(ejes))
        self.play(Write(gamma_curva3))
        self.play(ShowCreation(curva3))
        self.wait(3)
        self.play(FadeOut(gpo_7))
        self.play(Write(gpo_8))
        self.wait(3)
        self.play(FadeOut(gpo_8,run_time=2))
        self.play(FadeOut(curva3),FadeOut(ejes))
        self.play(FadeOut(gamma_curva3))
        
