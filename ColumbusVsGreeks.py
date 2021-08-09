from manim import *


class FancyMath(Scene):
    def construct(self):
        fancyMath = MathTex(r"MATH").scale(8)

        self.play(Write(fancyMath))


class StickAndShadow(Scene):
    def construct(self):
        rotation_center = LEFT

        triangle1 = Line([-1.2, -1.2, 0], [-1.2, 3.6, 0])
        triangle2 = Line([-1.2, 3.6, 0], [2.4, -1.2, 0])
        triangle3 = Line([-1.2, -1.2, 0], [2.4, -1.2, 0])
        shadow = Tex(r"$shadow$").move_to([0.6, -1.6, 0])
        stick = Tex(r"$stick$").move_to([-1.7, 1.2, 0]).rotate(PI/2)

        angle = Angle(triangle1, triangle2, radius=0.5,
                      quadrant=(-1, 1), other_angle=False)
        theta = MathTex(r"\theta").move_to(
            Angle(
                triangle1, triangle2, radius=0.8, other_angle=False
            ).point_from_proportion(0.92)
        )
        thetaDescription = MathTex(r"\theta = angle~of~the~shadow").scale(
            0.8).move_to([0.6, -2.5, 0])
        trigFormula = MathTex(
            r"tan(\theta) &= \frac{opposite}{adjacent} = \frac{shadow}{stick}").move_to([1, 1, 1]).shift(1.5 * UP)
        inverseTrigFormula = MathTex(
            r"tan^{-1}(\theta) &= tan^{-1}\left(\frac{shadow}{stick}\right) = \theta").move_to([1, 1, 1])
        trigAnswer = MathTex(r"\theta \approx 7.2 = \frac{360}{50}").move_to(
            [0.6, -1.2, 1]).shift(UP)

        self.play(Create(VGroup(triangle1, triangle2, triangle3)), run_time=2)
        self.play(Create(angle), Write(theta))
        self.play(Write(VGroup(shadow, stick, thetaDescription)), run_time=3)
        self.wait(1)
        self.play(ApplyMethod(VGroup(triangle1, triangle2, triangle3, angle,
                                     theta, shadow, stick, thetaDescription).shift, 4*LEFT), run_time=2)
        self.play(Write(trigFormula), run_time=6)
        self.wait(5)
        self.play(Write(inverseTrigFormula), run_time=6)
        self.wait(22)
        self.play(Write(trigAnswer), run_time=2)
        self.wait(3)


class EroMath(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()

        circle = Circle(radius=4, color=WHITE)
        verticalLine = Line([0, 0, 0], [0, 4.8, 0])
        hypotenuseLine = Line([0, 0, 0], [-1, 3.7, 0])
        alexandriaLine = Line([-1, 4.8, 0], [-1, 2.7, 0])
        trackingPoint = Point([0, 2, 0])

        angle = Angle(verticalLine, hypotenuseLine, radius=0.5,
                      quadrant=(1, 1), other_angle=False)
        angleTransversal = Angle(
            alexandriaLine, hypotenuseLine, radius=0.5, quadrant=(1, -1), other_angle=False)
        theta = MathTex(r"\theta").move_to(
            Angle(
                verticalLine, hypotenuseLine, radius=1.5, other_angle=False
            ).scale(0.1)
        )
        theta2 = MathTex(r"\theta").move_to([-0.9, 2.5, 0])

        syeneLabel = MathTex(r"Syene").move_to([0.4, 2.4, 0]).scale(0.5)
        alexandriaLabel = MathTex(r"Alexandria").move_to(
            [-1.2, 1.8, 0]).scale(0.5)
        sun = MathTex(r"Sun").move_to([-1.3, 3.8, 0]).scale(0.5)
        stick = MathTex(r"Stick").move_to([-0.6, 3.4, 0]).scale(0.5)

        distanceLabel = MathTex(r"d").move_to([-0.5, 3.1, 0]).scale(0.6)

        self.play(Create(circle))
        self.play(Create(VGroup(alexandriaLine, verticalLine)))
        self.play(self.camera.frame.animate.scale(0.5).move_to(trackingPoint))
        self.play(ApplyMethod(circle.shift, DOWN))
        self.play(Create(hypotenuseLine))
        self.play(Write(VGroup(syeneLabel, alexandriaLabel, sun, stick)), run_time=2)
        self.wait(10)
        self.play(Create(angleTransversal), Write(theta2))
        self.play(Create(angle), Write(theta))
        self.wait(10)
        self.play(Write(distanceLabel))
        self.wait(2)


class EroFormula(Scene):
    def construct(self):
        variableText = MathTex(r"C = circumfrence").shift(3.5*UP)
        formulaText = MathTex(
            r"\frac{1}{50} &= \frac{d}{C} \\ C &= 50d").shift(2 * UP)
        radiusText = MathTex(r"r = \frac{C}{2\pi}")
        formulaPercentText = MathTex(
            r"\approx 99.6\%~correct").move_to([3, 1.35, 0])
        radiusPercentText = MathTex(
            r"\approx 99.9\%~correct").move_to([2.8, 0, 0])

        self.play(Write(variableText))
        self.wait(1)
        self.play(Write(formulaText), run_time=5)
        self.wait(10)
        self.play(Write(radiusText))
        self.wait(4)
        self.play(Write(radiusPercentText))
        self.wait(6)
        self.play(Write(formulaPercentText))
        self.wait(3)


class Conclusion(Scene):
    def construct(self):
        conclusionText = MathTex(
            r"Math + History = Victory").scale(2).shift(UP)

        self.play(Write(conclusionText), run_time=5)
        self.wait(4)
