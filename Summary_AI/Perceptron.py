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



        self.wait()