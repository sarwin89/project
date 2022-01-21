from manim import *

class BraceAnnotation(Scene):
    def construct(self):
        dot1 = Dot([-2, -2, -2])
        dot2 = Dot([2, 2, 2])
        line = Arrow(dot1.get_center(), dot2.get_center()).set_color(ORANGE)

        d1t = Text('[-2, -2, -2]').next_to(dot1, LEFT)
        d2t = Text('[2, 2, 2]').next_to(dot2, RIGHT)
        
        b1 = Brace(line)
        b1text = b1.get_text("Horizontal distance")

        b2 = Brace(line, direction=line.copy().rotate(PI / 2).get_unit_vector())
        b2text = b2.get_tex("x_1-x_2")
        
        b3 = Brace(line, direction=line.copy().rotate(-PI / 4).get_unit_vector())
        b3text = b3.get_text("Vertical distance")

        """numberplane = NumberPlane().set_color(DARK_BLUE)
        self.add(d1t, d2t, line, dot1, dot2, b1, b2, b3, b1text, b2text, b3text)"""

        self.play(FadeIn(dot1, dot2))
        self.play(Write(d1t), Write(d2t))
        self.wait()

        self.play(Create(line))
        self.play(FadeIn(b1, b2, b3))
        self.play(Write(b2text))
        self.play(Write(b1text), Write(b3text))