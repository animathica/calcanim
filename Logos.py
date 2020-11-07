from manimlib.imports import *
class escudo(Scene):
    def construct(self):
        A = SVGMobject(r'C:\manim\manim-master\manim-master\assets\svg_images\escudo_f_c')
        B = SVGMobject(r'C:\manim\manim-master\manim-master\assets\svg_images\escudo_unam')
        A.set_fill(opacity = 0)\
         .set_stroke(WHITE,0.65)\
         .scale(2)\
         .move_to(np.array([-3,0,0]))
        B.set_fill(opacity = 0)\
         .set_stroke(WHITE,0.65)\
         .scale(2)\
         .move_to(np.array([3,0,0]))
        self.play(ShowCreation(A), ShowCreation(B), run_time = 10)
        self.wait()
        self.play(FadeOut(A), FadeOut(B) )
        C = SVGMobject(r'C:\manim\manim-master\manim-master\assets\svg_images\escudo_insta').set_fill(opacity = 0.4)\
         .set_stroke(WHITE,0.65)\
         .scale(1)\
         .move_to(np.array([-3,2.5,0]))
        D = SVGMobject(r'C:\manim\manim-master\manim-master\assets\svg_images\escudo_fb').set_fill(opacity = 0.4)\
         .set_stroke(WHITE,0.65)\
         .scale(1)\
         .move_to(np.array([-3,-2.5,0]))
        E = SVGMobject(r'C:\manim\manim-master\manim-master\assets\svg_images\escudo_github').set_fill(opacity = 0.4)\
         .set_stroke(WHITE,0.65)\
         .scale(1)\
         .move_to(np.array([-3,0,0]))
        self.play(Write(C),Write(D),Write(E), run_time = 5)
        self.wait()