import math
from manim import *

DEFAULT_FONT = "Noto Serif CJK SC"
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
        desc = Text("分类\nClassification", font=DEFAULT_FONT).shift(DOWN+LEFT)
        self.play(Write(desc))
        self.wait(0.5)

        # or binary classification
        descN = Text("二分类\nBinary Classification", font=DEFAULT_FONT).shift(DOWN+2*LEFT)
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
        desc2 = Text("第 1 个向量的第 1 个维度", font=DEFAULT_FONT).shift(2 * LEFT + 2 * DOWN)
        self.play(Create(framebox1))
        self.play(Write(descN), Write(desc2))
        self.wait()

        # x_2
        self.play(FadeOut(descN), FadeOut(desc2))
        self.play(ReplacementTransform(framebox1, framebox2))
        descN = MathTex(r"x_2^{(1)}").shift(2 * LEFT + DOWN)
        desc2 = Text("第 1 个向量的第 2 个维度", font=DEFAULT_FONT).shift(2 * LEFT + 2 * DOWN)
        self.play(Write(descN), Write(desc2))
        self.wait(0.5)
        self.play(FadeOut(descN), FadeOut(desc2))
        self.play(FadeOut(framebox2), FadeOut(desc))
        self.wait(0.5)

        # color
        self.play(Flash(dots[0], color=BLUE))
        self.wait()
        desc = Text("标签\nLabel", font=DEFAULT_FONT).shift(LEFT + DOWN)
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
            line = ax.plot(lambda x: -(a1T.get_value() * x + bT.get_value()) / a2T.get_value(), color=BLUE)
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
            arr = Arrow(ORIGIN, ax2.c2p(a1T.get_value(), a2T.get_value(), 0), buff=0, color=BLUE)
            return arr
        arr = always_redraw(get_arrow)
        tip = MathTex(f"({a1.get_value()}, {a2.get_value()})").next_to(arr.get_end(), RIGHT)
        
        self.play(Create(arr), a1L.animate.set_color(BLUE), a2L.animate.set_color(BLUE),
                  a1.animate.set_color(BLUE), a2.animate.set_color(BLUE))
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

        vec_exp = MathTex(r"\vec{w}", color=BLUE).shift(2.5 * UP + RIGHT * 2.5) 
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
        self.play(FadeOut(area1), FadeOut(area2), FadeOut(desc2))
        self.wait()

        sample = Dot(ax2.c2p(2, 1, 0), color=YELLOW)
        self.play(Create(sample))
        self.wait(0.5)
        
        arrow_tip = MathTex(r"y = -1 < 0, \hat{y} > 0").next_to(sample, RIGHT)
        self.play(FadeIn(area1), Write(arrow_tip))
        self.wait(0.5)
        self.play(FadeOut(area1))
        self.wait()

        self.play(a1T.animate.set_value(-2), a2T.animate.set_value(1))
        self.wait(0.5)

        self.play(a1T.animate.set_value(2), a2T.animate.set_value(3))
        self.wait()

        arrow = Arrow(ORIGIN, ax2.c2p(2, 1, 0), buff=0, color=GREEN)
        self.play(Create(arrow))
        self.wait()

        arr_value = MathTex(r"\vec{w}", color=BLUE).next_to(arr, RIGHT).shift(UP)
        arr_op = MathTex("-").next_to(arr_value, RIGHT)
        arrow_value = MathTex(r"\vec{x}", color=GREEN).next_to(arr_op, RIGHT)
        self.play(Write(arrow_value), Write(arr_op), Write(arr_value))
        self.wait()

        fin_arr_value = MathTex(r"\vec{w}'", color=BLUE_A).next_to(arr_op, UP)
        self.play(*[FadeOut(item) for item in [arrow_value, arr_op, arr_value]], Write(fin_arr_value))
        self.wait()

        self.play(a1T.animate.set_value(0), a2T.animate.set_value(2), fin_arr_value.animate.move_to(ax2.c2p(1,2,0)))
        self.wait()

        self.play(bT.animate.set_value(bT.get_value() - 1), FadeOut(fin_arr_value))
        self.wait()

        def get_area():
            return ax2.get_area(ax, [-10, 10], color=BLUE, bounded_graph=ax2.plot(lambda _:8))
        area = always_redraw(get_area)

        self.play(FadeIn(area))
        self.play(a1T.animate.set_value(a1T.get_value() - 2), a2T.animate.set_value(a2T.get_value() - 1))
        self.play(bT.animate.set_value(bT.get_value() - 1))
        self.wait()

        self.play(FadeOut(area))
        self.play(FadeOut(arrow_tip), sample.animate.set_color(BLUE), Flash(sample, color=BLUE))

        self.play(a1T.animate.set_value(a1T.get_value() + 2), a2T.animate.set_value(a2T.get_value() + 1))
        self.play(bT.animate.set_value(bT.get_value() + 1))
        self.wait()

        cond1 = Text("如果预测与实际相同，不做动作", font=DEFAULT_FONT, font_size=30).shift(4 * LEFT + 3.5 * UP)
        cond2 = Text("如果预测与实际不同，调整参数", font=DEFAULT_FONT, font_size=30).next_to(cond1, DOWN)
        self.play(AnimationGroup(Write(cond1), Write(cond2), lag_ratio=0.5))
        self.wait()

        method1 = MathTex(r"\hat{y} > 0, y < 0 \;\Rightarrow\; ", 
                          r"\vec{w}' = \vec{w} - \vec{x}", 
                          r" \\ ", 
                          r"b'=b - 1", font_size=37).next_to(cond2, DOWN)
        def get_area():
            return ax2.get_area(ax, [-10, 10], color=BLUE, bounded_graph=ax2.plot(lambda _:8))
        area = always_redraw(get_area)
        self.play(Write(method1), sample.animate.set_color(YELLOW), Flash(sample, color=YELLOW), FadeIn(area))
        self.wait()
        self.play(a1T.animate.set_value(a1T.get_value() - 2), a2T.animate.set_value(a2T.get_value() - 1), 
                  Indicate(method1[1]))
        self.wait()
        self.play(bT.animate.set_value(bT.get_value() - 1), 
                  Indicate(method1[3]))
        self.wait()
        self.play(FadeOut(area))

        method2 = MathTex(r"\hat{y} < 0, y > 0 \;\Rightarrow\; ", 
                          r"\vec{w}' = \vec{w} + \vec{x}", 
                          r" \\ ", 
                          r"b'=b + 1", font_size=37).next_to(method1, DOWN)
        def get_area():
            return ax2.get_area(ax, [-10, 10], color=YELLOW, bounded_graph=ax2.plot(lambda _:-8))
        area = always_redraw(get_area)
        self.play(Write(method2), sample.animate.set_color(BLUE), Flash(sample, color=BLUE), FadeIn(area))
        self.wait()
        self.play(a1T.animate.set_value(a1T.get_value() + 2), a2T.animate.set_value(a2T.get_value() + 1), 
                  Indicate(method2[1]))
        self.wait()
        self.play(bT.animate.set_value(bT.get_value() + 1), 
                  Indicate(method2[3]))
        self.wait()
        self.play(FadeOut(area))


        self.wait()



class Perc(Scene):
    def construct(self):
        odot = Dot(ORIGIN)
        numberplane = NumberPlane()

        data = [[1, 1, 1], [2, 2, 1], [3, 3,-1], [4, 2,-1], [4, 3,-1]]
        dots = [Dot(single, color=BLUE if single[2] == 1 else YELLOW) for single in data]
        self.play(Create(numberplane, run_time=3, lag_ratio=0.02), Create(odot))
        self.play(*[Create(dot) for dot in dots], lag_ratio=0.2)
        self.wait()

        line = Line((-4, 4, 0), (7, -7, 0))
        exp = MathTex(r"y = -x").shift(2 * LEFT + DOWN)
        self.play(Create(line), Write(exp))
        self.wait()

        exp2 = MathTex(r"0 = (-1, -1) \cdot \vec{x}").shift(4 * LEFT + DOWN)
        self.play(ReplacementTransform(exp, exp2))
        self.wait()

        t = ValueTracker(0)
        tloss = ValueTracker(0.4)
        tlossTip = Text("Training Loss:", font=DEFAULT_FONT).shift(4 * LEFT + 0.5 * UP)
        tlossLable = DecimalNumber(
            0.4,
            show_ellipsis=False,
            num_decimal_places=2,
            include_sign=False
        ).next_to(tlossTip, RIGHT)
        tlable = DecimalNumber(
            0,
            show_ellipsis=False,
            num_decimal_places=1,
            include_sign=True,
        ).next_to(exp2, RIGHT)
        self.play(Write(tlable), Write(tlossTip), Write(tlossLable))
        self.wait(0.5)

        line.add_updater(lambda l:l.put_start_and_end_on(
            (-4, 4 + t.get_value(), 0), (7, -7 + t.get_value(), 0)))
        tlossLable.add_updater(lambda l:l.set_value(tloss.get_value()))
        tlable.add_updater(lambda l:l.set_value(t.get_value()))
        self.play(t.animate.set_value(3), tloss.animate.set_value(0.2))
        self.wait(0.5)

        self.play(t.animate.set_value(5), tloss.animate.set_value(0.0))
        self.wait()

        line.clear_updaters()
        tlossLable.clear_updaters()

        exp = MathTex(r"0 = (-1, 0) \cdot \vec{x}").shift(4 * LEFT + DOWN)

        self.play(ReplacementTransform(exp2, exp), t.animate.set_value(2.5),
                  line.animate.put_start_and_end_on((2.5, 4, 0), (2.5, -4, 0)))
        t.clear_updaters()
        self.wait()
        
        self.play(FadeOut(tlable), FadeOut(tlossTip), FadeOut(tlossLable), FadeOut(exp), FadeOut(line))
        self.wait()

        table0 = Table(
            [[str(single[0]), str(single[1])] for single in data],
            row_labels=[Text(f"{i + 1}") for i in range(len(data))],
            col_labels=[MathTex("x_1^{(i)}"), MathTex("x_2^{(i)}")],
            top_left_entry=MathTex("i"),
        ).shift(3 * LEFT)

        self.play(Write(table0))
        self.wait()

        mean = MathTex(r"\text{Mean:} \mu_{x_1} = 2.8 \\ \mu_{x_2} = 2.2").shift(3 * RIGHT + DOWN)
        std = MathTex(r"\text{Std:} \sigma_{x_1} = 1.2 \\ \sigma_{x_2} = 0.7").shift(3 * RIGHT + 3 * DOWN)

        self.play(Write(mean), Write(std))
        self.wait()

        exp = MathTex(r"x' = \frac{x - \mu}{\sigma}").shift(3 * LEFT + 2 * UP)
        self.play(FadeOut(table0), Write(exp))
        self.wait()

        exp2 = MathTex(r"x'_{1} = \frac{x_{1} - 2.8}{1.2} \\ x'_{2} = \frac{x_{2} - 2.2}{0.7}").shift(3 * LEFT + 2 * UP) \
            .next_to(exp, DOWN)
        self.play(Write(exp2))
        self.wait()

        dataN = [[(single[0] - 2.8) / 1.2, (single[1] - 2.2) / 0.7, single[2]] for single in data]
        dotsN = [Dot(single, color=BLUE if single[2] == 1 else YELLOW) for single in dataN]
        self.play(*[ReplacementTransform(dots[i], dotsN[i]) for i in range(len(dots))],
                  FadeOut(mean), FadeOut(std), FadeOut(exp2), exp.animate.move_to(3 * UP).set_color(RED),)
        self.wait()

        desc = Text("归一化: “Z-score 标准化”方法", font=DEFAULT_FONT, color=RED).shift(2 * UP)
        self.play(Write(desc))
        self.wait()

class Ntwk(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(PINK, opacity=0.5)
        self.play(Create(circle))
        self.wait(0.5)
        
        arrow = Arrow([1, 0, 0], [3, 0, 0], buff=0, color=BLUE)
        self.play(Create(arrow))
        self.wait()

        text = Text("神经元\nNeuron", font=DEFAULT_FONT).shift(4 * LEFT)
        self.play(Write(text))
        self.wait()
        self.play(FadeOut(text))

        arrow1 = Arrow([-1.29, 1.29, 0], [-0.72, 0.72, 0], buff=0, color=BLUE)
        arrow2 = Arrow([-1.29, -1.29, 0], [-0.72, -0.72, 0], buff=0, color=BLUE)
        circle1 = Circle().shift(2 * LEFT + 2 * UP).set_fill(PINK, opacity=0.5)
        circle2 = Circle().shift(2 * LEFT + 2 * DOWN).set_fill(PINK, opacity=0.5)
        self.play(Create(arrow1), Create(arrow2), Create(circle1), Create(circle2))
        self.wait()

        inputText = Text("输入层", font=DEFAULT_FONT, font_size=20).shift(2 * LEFT + 3.5 * UP)
        outputText = Text("输出层", font=DEFAULT_FONT, font_size=20).shift(3.5 * UP)
        self.play(Write(inputText), Write(outputText))

        w1 = MathTex("w_1").next_to(arrow1, RIGHT).shift(0.5 * UP   + 0.4 * LEFT)
        w2 = MathTex("w_2").next_to(arrow2, RIGHT).shift(0.5 * DOWN + 0.4 * LEFT)
        x1 = MathTex("x_1").shift(2 * LEFT + 2 * UP)
        x2 = MathTex("x_2").shift(2 * LEFT + 2 * DOWN)
        self.play(Write(w1), Write(w2), Write(x1), Write(x2))
        self.wait()

        x3 = MathTex(r"w_1 x_1 + w_2 x_2").shift(2.5 * RIGHT + 0.4 * UP)
        self.play(Write(x3))
        self.wait()

        t3 = MathTex(r"0.7 \times 1 + 0.2 \times 1").shift(3 * RIGHT + 0.4 * DOWN)
        self.play(Write(t3))
        self.wait()

        bias_exp = MathTex(r"-b").next_to(x3, RIGHT)
        bias = MathTex(r"-0.5").next_to(t3, RIGHT)
        biast = Text("偏置 Bias", font=DEFAULT_FONT, font_size=30).next_to(bias, DOWN)
        self.play(Write(bias), Write(biast), Write(bias_exp))
        self.wait()

        # GOTO ACFUN

        exp = MathTex(r"f \left( \sum w_i x_i - b \right)").shift(3 * RIGHT + 0.7 * DOWN)
        self.play(FadeOut(bias), FadeOut(biast), FadeOut(bias_exp), FadeOut(x3),
                  ReplacementTransform(t3, exp))
        self.wait()

class AcFun(Scene):
    def construct(self):
        title = Text("激活函数", font=DEFAULT_FONT).shift(3 * UP + 5 * LEFT)
        self.play(Write(title))
        self.wait()

        ax = Axes(
            x_range=[-5, 5],
            y_range=[-2, 2],
            tips=True,
            axis_config={"include_numbers": True},
            
        )
        labels = ax.get_axis_labels(
            Text("总输入", font=DEFAULT_FONT).scale(0.7), Text("输出", font=DEFAULT_FONT).scale(0.7)
        )
        self.play(Create(ax), Write(labels))
        self.wait()

        ac1 = ax.plot(lambda _: 0, [-5, 0, 1], color=RED)
        ac2 = ax.plot(lambda _: 1, [0, 5, 1], color=GREEN)
        self.play(Create(ac1), Create(ac2))
        self.wait()

        name = Text("阶跃函数", font=DEFAULT_FONT).next_to(title, DOWN)
        self.play(Write(name))
        self.wait()

        name2 = Text("Sigmoid 函数", font=DEFAULT_FONT).next_to(title, DOWN).shift(0.8 * RIGHT)
        self.play(ReplacementTransform(name, name2))
        self.wait()

        sigmoid = ax.plot(lambda x:1/(1 + math.e ** (-x)), color=YELLOW)
        self.play(Create(sigmoid))
        self.wait()

        sigmoid1 = ax.plot(lambda x:1/(1 + math.e ** (-x)), [-5, -2, 0.1], color=RED)
        sigmoid2 = ax.plot(lambda x:1/(1 + math.e ** (-x)), [2, 5, 0.1], color=GREEN)
        self.play(Create(sigmoid1), Create(sigmoid2))
        self.wait()

        self.play(FadeOut(name2), FadeOut(sigmoid), FadeOut(sigmoid1), FadeOut(sigmoid2), FadeOut(ac1), FadeOut(ac2))
        name3 = Text("ReLU 函数", font=DEFAULT_FONT).next_to(title, DOWN).shift(0.2 * RIGHT)
        relu1 = ax.plot(lambda _:0, [-5, 0, 1], color=RED)
        relu2 = ax.plot(lambda x:x, [0, 5, 1], color=GREEN)
        self.play(Write(name3), Create(relu1), Create(relu2))
        self.wait()

class LRate(Scene):
    def construct(self):
        ax = Axes(
            x_range=[-10, 10],
            y_range=[0, 1],
            tips=True,
        )
        label = ax.get_axis_labels(
            Text("参数", font=DEFAULT_FONT).scale(0.7), Text("学习效果", font=DEFAULT_FONT).scale(0.7)
        )
        func = lambda x: - (x / 12) ** 2 + 0.8
        graph = ax.plot(func, color=BLUE)
        self.play(Write(ax), Write(label))
        self.wait()
        self.play(Create(graph))
        self.wait()

        t = ValueTracker(-10)
        dot = Dot(ax.c2p(t.get_value(), func(t.get_value())), color=GREEN)
        dot.add_updater(lambda d:d.move_to(ax.c2p(t.get_value(), func(t.get_value()))))

        self.play(Create(dot))
        self.wait(.5)
        self.play(t.animate.set_value(-7), run_time=1)
        self.play(t.animate.set_value(-4), run_time=1)
        self.play(t.animate.set_value(-1), run_time=1)
        self.play(t.animate.set_value( 2), run_time=1)
        self.wait()

        lrate = ValueTracker(3)
        lrateTip = Text("学习率:", font=DEFAULT_FONT, font_size=30).shift(5 * LEFT + 3 * UP)
        lrateVal = DecimalNumber(
            3,
            show_ellipsis=False,
            num_decimal_places=1,
            # include_sign=True,
        ).next_to(lrateTip, RIGHT)
        lrateVal.add_updater(lambda l:l.set_value(lrate.get_value()))

        self.play(Write(lrateTip), Write(lrateVal), t.animate.set_value(-5))
        self.wait()

        lfunc = lambda x: 0.5 * x
        lfuncTip = Text("衰减函数:", font=DEFAULT_FONT, font_size=30).next_to(lrateTip, DOWN, aligned_edge=LEFT)
        lfuncVal = MathTex(r"f(\eta) = 0.5 \times \eta").scale(0.8).next_to(lfuncTip, RIGHT)

        self.play(Write(lfuncTip), Write(lfuncVal))
        self.wait()

        for _ in range(5):
            self.play(t.animate.set_value(t.get_value() + (1 if t.get_value() < 0 else -1) * lrate.get_value()))
            self.play(lrate.animate.set_value(lfunc(lrate.get_value())))

        self.wait()

        self.play([FadeOut(item) for item in [dot, ax, label, graph, lrateTip, lrateVal, lfuncTip, lfuncVal]])

        orig_exp = MathTex(r"\vec{w}' &= \vec{w} \pm \vec{x} \\ b' &= b \pm 1")
        self.play(Write(orig_exp))
        self.wait()

        new_exp = MathTex(r"\vec{w}' &= \vec{w} \pm \eta \vec{x} \\ b' &= b \pm \eta")
        self.play(ReplacementTransform(orig_exp, new_exp))
        self.wait()

        self.play(FadeOut(new_exp))
        self.wait()

class XOR(Scene):
    def construct(self):
        title = Text("XOR问题", font=DEFAULT_FONT).shift(3 * UP + 5 * LEFT)
        self.play(Write(title))
        self.wait()

        ax = Axes(
            x_range=[-4, 4],
            y_range=[-2, 2],
            tips=True,
            axis_config={"include_numbers": True},
        )
        labels = ax.get_axis_labels(
            Tex("Input 1").scale(0.7), Tex("Input 2").scale(0.7)
        )
        self.play(Create(ax), Write(labels))
        self.wait()

        data = [[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 0]]
        dots = [Dot(ax.c2p(*single), color=BLUE if single[2] == 1 else YELLOW) for single in data]
        self.play(*[Create(dot) for dot in dots])
        self.wait()
        
        desc = Text("线性不可分", font=DEFAULT_FONT).shift(2 * DOWN + 2 * LEFT)
        self.play(Write(desc))
        self.wait()

        self.play(FadeOut(desc))
        self.wait()

        desc = Text("多层感知机", font=DEFAULT_FONT).shift(2 * DOWN + 2 * LEFT)
        self.play(Write(desc))
        self.wait()

        self.play(FadeOut(desc))
        self.wait()

class MLP(Scene):
    def construct(self):
        cx1 = Circle(radius=0.5, color=WHITE).shift(2.5 * LEFT + UP)
        cx2 = Circle(radius=0.5, color=WHITE).shift(2.5 * LEFT + DOWN)
        ch1 = Circle(radius=0.5, color=WHITE).shift(0.5 * LEFT + UP)
        ch2 = Circle(radius=0.5, color=WHITE).shift(0.5 * LEFT + DOWN)
        co1 = Circle(radius=0.5, color=WHITE).shift(1 * RIGHT)

        self.play(Create(cx1), Create(cx2), Create(ch1), Create(ch2), Create(co1))

        arr1 = Arrow([-2, 1, 0], [-1, 1, 0], buff=0, color=BLUE)
        arr2 = Arrow([-2.14, 0.64, 0], [-0.85, -0.64, 0], buff=0, color=YELLOW_E)
        arr3 = Arrow([-2.14, -0.64, 0], [-0.85, 0.64, 0], buff=0, color=YELLOW_E)
        arr4 = Arrow([-2, -1, 0], [-1, -1, 0], buff=0, color=BLUE)
        arr5 = Arrow([-0.08, 0.72, 0], [0.58, 0.27, 0], buff=0, color=BLUE)
        arr6 = Arrow([-0.08, -0.72, 0], [0.58, -0.27, 0], buff=0, color=BLUE)
        arr7 = Arrow([1.5, 0, 0], [2.5, 0, 0], buff=0, color=WHITE)

        self.play(*[Create(arrow) for arrow in [arr1, arr2, arr3, arr4, arr5, arr6, arr7]])
        self.wait()

        arrBlue = Arrow([4, 3, 0], [5, 3, 0], buff=0, color=BLUE)
        blueTip = MathTex("w = +1").next_to(arrBlue, RIGHT)
        arrYellow = Arrow([4, 2, 0], [5, 2, 0], buff=0, color=YELLOW_E)
        yellowTip = MathTex("w = -1").next_to(arrYellow, RIGHT)
        biasTip = MathTex("b = 0.5").next_to(yellowTip, DOWN, buff=0.5 , aligned_edge=RIGHT)

        self.play(Create(arrBlue), Write(blueTip), Create(arrYellow), Write(yellowTip), Write(biasTip))
        self.wait()

        x1Val = MathTex("1").next_to(cx1, LEFT)
        x1Text = MathTex("x_1=").next_to(x1Val, LEFT)
        x2Val = MathTex("0").next_to(cx2, LEFT)
        x2Text = MathTex("x_2=").next_to(x2Val, LEFT)

        midVal  = MathTex("0", color=WHITE).move_to([-1.5, 0, 0])
        mid1Val = MathTex("1", color=WHITE).move_to([-1.5, 1, 0])

        self.play(Write(x1Val), Write(x1Text), Write(x2Val), Write(x2Text))
        self.wait()

        # input
        self.play(x1Val.animate.move_to([-2.5, 1, -1]), x2Val.animate.move_to([-2.5, -1, 0]))
        self.wait()

        # light up cx1
        self.play(x1Val.animate.set_color(BLACK), cx1.animate.set_fill(WHITE, opacity=1))
        self.wait()

        # transform to arrow
        self.play(TransformFromCopy(x1Val, mid1Val), TransformFromCopy(x2Val, midVal))
        self.wait()

        # multiply
        self.play(AnimationGroup(Indicate(mid1Val), Indicate(blueTip), lag_ratio=1))
        self.wait()
        self.play(AnimationGroup(Indicate(midVal), Indicate(yellowTip), lag_ratio=1))
        self.wait()

        # move
        self.play(mid1Val.animate.move_to([-0.5, 1, 0]), midVal.animate.move_to([-0.5, 1, 0]))
        self.wait(0.5)

        # sum
        h1Val = MathTex("1", color=WHITE).move_to([-0.5, 1, 0])
        self.play(FadeOut(mid1Val), FadeOut(midVal), FadeIn(h1Val))
        self.wait()

        # bias
        self.play(AnimationGroup(Indicate(h1Val), Indicate(biasTip), lag_ratio=1))
        self.wait(0.5)
        h1ValN = MathTex("0.5").move_to([-0.5, 1, 0])
        self.play(Transform(h1Val, h1ValN))
        self.wait()

        # light up
        self.play(ch1.animate.set_fill(WHITE, opacity=1), h1Val.animate.set_color(BLACK))
        self.wait()

        # output
        h1ValN = MathTex("1", color=BLACK).move_to([-0.5, 1, 0])
        self.play(Transform(h1Val, h1ValN))
        self.wait()

        # 2nd
        midVal  = MathTex("1", color=WHITE).move_to([-1.5, 0, 0])
        mid2Val = MathTex("0", color=WHITE).move_to([-1.5, -1, 0])
        self.play(TransformFromCopy(x1Val, midVal), TransformFromCopy(x2Val, mid2Val))
        self.play(AnimationGroup(Indicate(midVal), Indicate(yellowTip), lag_ratio=1))
        midValN = MathTex("-1", color=WHITE).move_to([-1.5, 0, 0])
        self.play(Transform(midVal, midValN))
        self.play(AnimationGroup(Indicate(mid2Val), Indicate(blueTip), lag_ratio=1))
        self.play(midVal.animate.move_to([-0.5, -1, 0]), mid2Val.animate.move_to([-0.5, -1, 0]))
        h2Val = MathTex("-1", color=WHITE).move_to([-0.5, -1, 0])
        self.play(FadeOut(midVal), FadeOut(mid2Val), FadeIn(h2Val))
        self.wait()
        
        h2ValN = MathTex("-1.5", color=WHITE).move_to([-0.5, -1, 0])
        self.play(Transform(h2Val, h2ValN))
        self.wait()

        h2ValN = MathTex("0", color=WHITE).move_to([-0.5, -1, 0])
        self.play(Transform(h2Val, h2ValN))
        self.wait()
        
        # output
        outVal = MathTex("1").move_to([1, 0, 0])
        self.play(Write(outVal))
        self.wait()

        outValN = MathTex("0.5").move_to([1, 0, 0])
        self.play(Transform(outVal, outValN))
        self.wait()

        outValN = MathTex("1", color=BLACK).move_to([1, 0, 0])
        self.play(Transform(outVal, outValN), co1.animate.set_fill(WHITE, opacity=1))
        self.wait()

        self.play(*[FadeOut(item) for item in [outVal, x1Val, x2Val, h1Val, h2Val]])
        self.wait()

        datas = [[1, 1, 0, 0, 0], [1, 0, 1, 0, 1], [0, 1, 0, 1, 1], [0, 0, 0, 0, 0]]

        for data in datas:
            
            self.play(AnimationGroup(
                cx1.animate.set_fill(WHITE if data[0] else BLACK, opacity=1),
                cx2.animate.set_fill(WHITE if data[1] else BLACK, opacity=1),
                ch1.animate.set_fill(WHITE if data[2] else BLACK, opacity=1),
                ch1.animate.set_fill(WHITE if data[3] else BLACK, opacity=1),
                co1.animate.set_fill(WHITE if data[4] else BLACK, opacity=1),
            ))
        
        self.wait()