from manim import *


class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set color and transparency

        square = Square()  # create a square
        square.rotate(PI / 4)  # rotate a certain amount

        self.play(Create(square))  # animate the creation of the square
        self.play(Transform(square, circle))  # interpolate the square into the circle
        self.play(FadeOut(square))  # fade out animation

class SquareAndCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency

        square = Square()  # create a square
        square.set_fill(BLUE, opacity=0.5)  # set the color and transparency

        square.next_to(circle, RIGHT, buff=0.5)  # set the position
        self.play(Create(circle), Create(square))  # show the shapes on screen

        self.play(Transform(square, circle))
        # self.play(Transform(circle, square))

class AnimatedSquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        square = Square()  # create a square

        self.play(Create(square))  # show the square on screen
        self.play(square.animate.rotate(PI / 4))  # rotate the square
        self.play(Transform(square, circle))  # transform the square into a circle
        self.play(
            square.animate.set_fill(PINK, opacity=0.5)
        )  # color the circle on screen

class DifferentRotations(Scene):
    def construct(self):
        left_square = Square(color=BLUE, fill_opacity=0.7).shift(2 * LEFT)
        right_square = Square(color=GREEN, fill_opacity=0.7).shift(2 * RIGHT)
        self.play(
            left_square.animate.rotate(PI), Rotate(right_square, angle=PI), run_time=2
        )
        self.wait()

class TwoTransforms(Scene):
    def transform(self):
        a = Circle()
        b = Square()
        c = Triangle()
        self.play(Transform(a, b))
        self.play(Transform(a, c))
        self.play(FadeOut(a))

    def replacement_transform(self):
        a = Circle()
        b = Square()
        c = Triangle()
        self.play(ReplacementTransform(a, b))
        self.play(ReplacementTransform(b, c))
        self.play(FadeOut(c))

    def construct(self):
        self.transform()
        self.wait(0.5)  # wait for 0.5 seconds
        self.replacement_transform()

class TextRender(Scene):
    def construct(self):
        text = Text("Hello, World!")
        self.play(Create(text))
        self.wait(0.5)
        formula = Text(r"\frac{1}{2} \int_{-\infty}^{\infty} x^2 dx").shift(DOWN)
        self.play(ReplacementTransform(text, formula))
        self.wait(0.5)
        self.play(FadeOut(formula))

class LinearTransformationSceneExample(LinearTransformationScene):
    def __init__(self, **kwargs):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=False,
            leave_ghost_vectors=True,
            **kwargs
        )

    def construct(self):
        matrix = [[1, 1], [0, -1]]
        self.apply_matrix(matrix)
        self.wait()

class VectorTest(VectorScene):
    def construct(self):
        ax = Axes((-5,5,1), (-5,5,1))
        self.add(ax)
        self.wait(0.5)
        self.add_vector([1, 1])
        self.wait(0.5)
        self.add_vector([1, 6])
        self.wait(0.5)
        axn = Axes((0,10,1), (0,10,1))
        self.play(ReplacementTransform(ax, axn))
        # self.show_ghost_movement((1,1))
        # self.play(self.camera.frame.animate.move_to(s))