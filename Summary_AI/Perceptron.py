from manim import *

class PreProc(Scene):
    def construct(self):
        # if there's a coord
        dot = Dot(ORIGIN)
        numberplane = NumberPlane()
        self.play(Create(numberplane, run_time=3, lag_ratio=0.1), Create(dot))
        self.wait()

        # and there some dots with different colors
        data = [[1, 1, 1], [2, 2, 1], [3, 3,-1], [4, 2,-1], [4, 3,-1]]
        dots = [Dot(single, color=BLUE if single[2] == 1 else YELLOW) for single in data]
        self.play(*[Create(dot) for dot in dots])
        self.wait()

        # we should separate them
        line = Line((-4, 4, 0), (7, -7, 0))
        self.play(Create(line))
        self.wait()

        # we can easily find the solution
        # line.move_to(Dot((3, 2, 0)))
        self.play(line.animate.move_to(Dot((3, 2, 0))))
        self.wait()

        # this is classification
        self.play(Flash(line))
        self.play(FocusOn((1.5, 1.5, 0), color=BLUE))
        self.play(FocusOn((3.5, 2.5, 0), color=YELLOW))
        desc = Text("分类\nClassification").shift(DOWN+LEFT)
        self.play(Write(desc))
        self.wait(0.5)

        # or binary classification
        descN = Text("二分类\nBinary Classification").shift(DOWN+2*LEFT)
        self.play(ReplacementTransform(desc, descN))
        self.wait()

        # back to the original
        self.play(FadeOut(line), FadeOut(descN))
        self.wait()

        # we can use vector to describe each line
        arrow = Arrow(ORIGIN, [1, 1, 0], buff=0, color=BLUE)
        self.play(Create(arrow))
        desc = MathTex(r"\vec{x}^{(1)} = (", r"1", r",", r"1", r")").shift(2 * LEFT + UP)
        self.play(Write(desc))
        self.wait()

        # x_1

        framebox1 = SurroundingRectangle(desc[1], buff = .1)
        framebox2 = SurroundingRectangle(desc[3], buff = .1)
        descN = MathTex(r"x_1^{(1)}").shift(2 * LEFT + DOWN)
        desc2 = Text("第 1 个向量的第 1 个维度", font="Simsun").shift(2 * LEFT + 2 * DOWN)
        self.play(Create(framebox1))
        self.play(Write(descN), Write(desc2))
        self.wait()

        # x_2
        self.play(FadeOut(descN), FadeOut(desc2))
        self.play(ReplacementTransform(framebox1, framebox2))
        descN = MathTex(r"x_2^{(1)}").shift(2 * LEFT + DOWN)
        desc2 = Text("第 1 个向量的第 2 个维度", font="Simsun").shift(2 * LEFT + 2 * DOWN)
        self.play(Write(descN), Write(desc2))
        self.wait(0.5)
        self.play(FadeOut(descN), FadeOut(desc2))
        self.play(FadeOut(framebox2), FadeOut(desc))
        self.wait(0.5)

        # color
        self.play(Flash(dots[0], color=BLUE))
        self.wait()
        desc = Text("标签\nLabel", font="Simsun").shift(LEFT + DOWN)
        self.play(Write(desc))
        self.wait(0.5)
        descN = MathTex(r"y^{(1)} = \text{BLUE}").shift(2 * LEFT + DOWN)
        self.play(ReplacementTransform(desc, descN))
        self.wait()
        desc = MathTex(r"y^{(1)} = 1").shift(2 * LEFT + 2 * DOWN)
        self.play(Write(desc))
        self.wait()
        arrow2 = Arrow(ORIGIN, [3, 3, 0], buff=0, color=YELLOW)
        self.play(ReplacementTransform(arrow, arrow2))
        desc2 = MathTex(r"y^{(3)} = -1").shift(2 * RIGHT + 2 * DOWN)
        self.play(Write(desc2))
        self.wait()
        arrow = Arrow(ORIGIN, [1, 1, 0], buff=0, color=BLUE)
        self.play(ReplacementTransform(arrow2, arrow), FadeOut(descN), FadeOut(desc), FadeOut(desc2))
        self.wait(0.5)

        # 3 elements
        desc = MathTex(r"\{", "x_1^{(i)}", ",", "x_2^{(i)}", ",", "y^{(i)}", "\}").shift(DOWN + 2 * LEFT)
        self.play(Write(desc))
        self.wait(0.5)
        framebox1 = SurroundingRectangle(desc[1], buff = .1)
        framebox2 = SurroundingRectangle(desc[3], buff = .1)
        framebox3 = SurroundingRectangle(desc[5], buff = .1)
        self.play(Create(framebox1))
        self.wait(0.5)
        self.play(ReplacementTransform(framebox1, framebox2))
        self.wait(0.5)
        self.play(ReplacementTransform(framebox2, framebox3))
        self.wait()
        self.play(FadeOut(framebox3))
        desc2 = MathTex(r"\left\{\left\{x_1^{(i)}, x_2^{(i)}, y^{(i)} \right\}\right\}, ",
                        r"x_j^{(i)} \in \mathbb{R}, y^{(i)} \in \{-1, 1\}").shift(2 * DOWN)
        self.play(Write(desc2))
        self.wait()
        self.play(FadeOut(desc2), FadeOut(desc))



        self.wait()

class ALine(Scene):
    def construct(self):
        a1 = DecimalNumber(
            2,
            show_ellipsis=False,
            num_decimal_places=1,
            include_sign=True,
        ).shift(3 * UP + RIGHT * 3) 
        a1L = MathTex(r"a_1", "=").next_to(a1, LEFT)
        a1T = ValueTracker(2)
        a1.add_updater(lambda l:l.set_value(a1T.get_value()))

        a2 = DecimalNumber(
            3,
            show_ellipsis=False,
            num_decimal_places=1,
            include_sign=True,
        ).shift(2 * UP + RIGHT * 3)
        a2L = MathTex(r"a_2", "=").next_to(a2, LEFT)
        a2T = ValueTracker(3)
        a2.add_updater(lambda l:l.set_value(a2T.get_value()))

        b = DecimalNumber(
            1,
            show_ellipsis=False,
            num_decimal_places=1,
            include_sign=True,
        ).shift(1 * UP + RIGHT * 3)
        bL = MathTex(r"b", "=").next_to(b, LEFT)
        bT = ValueTracker(1)
        b.add_updater(lambda l:l.set_value(bT.get_value()))
        # ax = Axes(
        #     x_range=[-5, 5],
        #     y_range=[-5, 5],
        #     tips=True
        # )

        # a1 x + a2 y + b = 0
        # line = ax.plot(lambda x: -(a1 * x + b) / a2)
        # self.add(ax, line)

        def get_line():
            ax = Axes(
                x_range=[-10, 10],
                y_range=[-5, 5],
                tips=True
            )
            line = ax.plot(lambda x: -(a1.get_value() * x + bT.get_value()) / a2.get_value(), color=BLUE)
            return line
        
        ax = always_redraw(get_line)
        self.wait(0.5)
        
        ax2 = Axes(
                x_range=[-10, 10],
                y_range=[-5, 5],
                tips=True
            )
        self.play(Create(ax2))
        desc2 = MathTex("a_1", "x", " + ", "a_2", "y", " + ", "b", " = 0").shift(UP * 3 + LEFT * 3)
        self.play(Write(desc2))
        self.wait()
        self.play(Write(a1L), Write(a2L), Write(bL))
        self.play(Write(a1), Write(a2), Write(b))
        self.wait()
        self.play(Create(ax))
        self.wait()
        self.play(bT.animate.set_value(3), run_time=1)
        self.wait(0.5)
        self.play(a1T.animate.set_value(4), run_time=1)
        self.wait(0.5)
        self.play(a2T.animate.set_value(-1), run_time=1)
        self.wait()
        
        def get_arrow():
            arr = Arrow(ORIGIN, ax2.c2p(a1.get_value(), a2.get_value(), 0), buff=0, color=YELLOW)
            return arr
        arr = always_redraw(get_arrow)
        tip = MathTex(f"({a1.get_value()}, {a2.get_value()})").next_to(arr.get_end(), RIGHT)
        
        self.play(Create(arr), a1L.animate.set_color(YELLOW), a2L.animate.set_color(YELLOW),
                  a1.animate.set_color(YELLOW), a2.animate.set_color(YELLOW))
        self.wait(0.5)
        self.play(Write(tip))
        self.wait(0.5)
        self.play(FadeOut(tip))
        self.wait()
        self.play(bT.animate.set_value(1), run_time=1)
        self.wait(0.5)
        self.play(a1T.animate.set_value(2), run_time=1)
        self.wait(0.5)
        self.play(a2T.animate.set_value(3), run_time=1)
        self.wait()

        vec_exp = MathTex(r"\vec{w}", color=YELLOW).shift(2.5 * UP + RIGHT * 2.5) 
        self.play(FadeOut(a1L), FadeOut(a1), FadeOut(a2L), FadeOut(a2), Write(vec_exp))
        self.wait(0.5)
        exp = MathTex(r"0", "=", r"\vec{w}", r"\cdot", r"\vec{x}", "+", "b") \
            .shift(LEFT * 3 + DOWN * 3)
        # self.play(Write(exp))
        self.play(Write(exp), Transform(vec_exp, exp[2]), Transform(bL[0], exp[6]))
        self.play(FadeOut(bL), FadeOut(b))
        self.wait()
        self.play(Indicate(exp))
        self.play(Indicate(desc2))
        self.wait()

        t = ValueTracker(0)
        initial_point = [ax2.c2p(t.get_value(),
                                 -(a1.get_value() * (t.get_value()) 
                                   + bT.get_value()) / a2.get_value())]
        dot = Dot(point=initial_point, color=GREEN)

        dot.add_updater(lambda d:d.move_to(
            ax2.c2p(t.get_value(), -(a1.get_value() * (t.get_value()) 
                                   + bT.get_value()) / a2.get_value())))
        
        self.play(Create(dot))
        self.wait(0.5)
        self.play(t.animate.set_value(2))
        self.wait()
        self.play(t.animate.set_value(-2))
        self.wait()
        self.play(t.animate.set_value(1))
        self.wait()

        dot.clear_updaters()
        dot.add_updater(lambda d:d.move_to(
            ax2.c2p(t.get_value(), -(a1.get_value() * 1
                                   + bT.get_value()) / a2.get_value())))
        
        tip_exp = MathTex(r"\vec{w} \cdot \vec{x} + b =").next_to(dot, RIGHT)
        tip_exp.add_updater(lambda l:l.next_to(dot, RIGHT))
        tip = DecimalNumber(
            1,
            show_ellipsis=False,
            num_decimal_places=1,
            include_sign=True,
        ).next_to(tip_exp, RIGHT, 2.8)
        currentY = -(a1.get_value() * 1 + bT.get_value()) / a2.get_value()
        tip.add_updater(lambda l:l.set_value(a1.get_value() * t.get_value() + a2.get_value() * currentY + b.get_value())
            .next_to(dot, RIGHT, 2.8))

        self.play(Write(tip_exp), Write(tip))
        self.wait()
        self.play(t.animate.set_value(3))
        self.wait()
        self.play(t.animate.set_value(-1))
        self.wait()
        self.play(t.animate.set_value(1))
        self.wait()

        area1 = ax2.get_area(ax, [-10, 10], color=BLUE, bounded_graph=ax2.plot(lambda _:8))
        self.play(FadeIn(area1), t.animate.set_value(3))
        self.wait()
        area2 = ax2.get_area(ax, [-10, 10], color=YELLOW, bounded_graph=ax2.plot(lambda _:-8))
        self.play(FadeOut(area1), FadeIn(area2), t.animate.set_value(-1))
        self.wait()
        self.play(FadeOut(area2), FadeOut(dot), FadeOut(tip), FadeOut(tip_exp))

        exp2 = MathTex(r"\hat{y}", r" = \vec{w} \cdot \vec{x} + b") \
            .shift(LEFT * 3 + DOWN * 3)
        self.wait(0.5)
        self.play(Indicate(exp[0]))
        self.wait(0.5)
        self.play(ReplacementTransform(exp[0], exp2[0]))
        self.wait()
        self.play(FadeIn(area1), FadeIn(area2))
        self.wait()
        self.play(FadeOut(area1), FadeOut(area2))
