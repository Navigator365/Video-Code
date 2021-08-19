from manim import *

class OpeningQuote(Scene):
    def construct(self):
        openingQuote = Tex(r'$ ``There~goes~the~man~that~writt~a~book~that~neither~he~nor~anybody~else~understands.”$',
                           tex_template=TexFontTemplates.zapf_chancery).scale(0.8)
        subtext = Tex(
            r'$-Cambridge~student,~soon~after~the~publication~of~Isacc~Newton\textquotesingle s~\emph{Principia}$').scale(0.6).move_to([1.5, -1, 0])
        calcTex = Tex(r'$\int_{a}^{b} x^2 \,dx$').scale(3)
        crossLine1 = Line([-3, -3, 0], [3, 3, 0])
        crossLine2 = Line([-3, 3, 0], [3, -3, 0])
        self.play(Write(openingQuote), run_time=6)
        self.play(Write(subtext), run_time=4)
        self.wait(9)
        self.play(Uncreate(openingQuote), Uncreate(subtext), run_time=2)
        self.wait(1)
        self.play(Write(calcTex))
        self.play(Create(VGroup(crossLine1, crossLine2)))
        self.wait(1)


class EllipseDrawing(Scene):
    def construct(self):
        dotA = Dot([-3, 0, 0], radius=0.08)
        dotB = Dot([3, 0, 0], radius=0.08)
        dotE = Dot([0, 3, 0], radius=0.08)
        dotALabel = Tex(r'$A$').move_to([-3, -0.5, 0])
        dotBLabel = Tex(r'$B$').move_to([3, -0.5, 0])
        dotELabel = Tex(r'$E$').move_to([0, 3.5, 0])
        movingLine1 = Line([-3, 0, 0], [0, 3, 0])
        movingLine2 = Line([3, 0, 0], [0, 3, 0])
        ellipse1 = Ellipse(width=9, height=6, color=WHITE)

        self.wait(1)
        self.play(Create(dotA), Create(dotB), Create(dotE),
                  Write(VGroup(dotALabel, dotBLabel, dotELabel)))
        self.wait(2)
        self.play(Create(VGroup(movingLine1, movingLine2)))
        self.play(Create(ellipse1), run_time=2)
        self.wait(2)
        self.play(Uncreate(ellipse1))
        self.play(Uncreate(dotA), Uncreate(dotB), Uncreate(dotE))
        self.play(Uncreate(VGroup(movingLine1, movingLine2)))

        ellipse2 = Ellipse(width=8, height=7, color=WHITE)
        dotA = Dot([-2, 0, 0], radius=0.08)
        dotB = Dot([2, 0, 0], radius=0.08)
        dotE = Dot([0, 3.5, 0], radius=0.08)
        movingLine1 = Line([-2, 0, 0], [0, 3.5, 0])
        movingLine2 = Line([2, 0, 0], [0, 3.5, 0])

        self.play(Create(dotA), Create(dotB), Create(dotE), ApplyMethod(dotALabel.move_to, [-2, -0.5, 0]), ApplyMethod(dotBLabel.move_to, [2, -0.5, 0]),
                  ApplyMethod(dotELabel.move_to, [0, 3.8, 0]))
        self.play(Create(VGroup(movingLine1, movingLine2)))
        self.play(Create(ellipse2), run_time=2)
        self.wait(2)
        self.play(Uncreate(ellipse2))
        self.play(Uncreate(dotA), Uncreate(dotB), Uncreate(dotE))
        self.play(Uncreate(VGroup(movingLine1, movingLine2)))

        ellipse3 = Ellipse(width=8, height=2, color=WHITE)
        dotA = Dot([-2, 0, 0], radius=0.08)
        dotB = Dot([2, 0, 0], radius=0.08)
        dotE = Dot([0, 1, 0], radius=0.08)
        movingLine1 = Line([-2, 0, 0], [0, 1, 0])
        movingLine2 = Line([2, 0, 0], [0, 1, 0])

        self.play(Create(dotA), Create(dotB), Create(dotE), ApplyMethod(dotALabel.move_to, [-2, -0.5, 0]), ApplyMethod(dotBLabel.move_to, [2, -0.5, 0]),
                  ApplyMethod(dotELabel.move_to, [0, 1.5, 0]))
        self.play(Create(VGroup(movingLine1, movingLine2)))
        self.play(Create(ellipse3))
        self.wait(2)


class KeplerRules(Scene):
    def construct(self):
        rule1 = Tex(
            r'$1.~Planets~orbit~in~ellipses~(like~we~just~drew)$').shift(UP)
        rule2 = Tex(r'$2.~Planets~travel~equal~areas~in~equal~times$')
        rule3 = Tex(r'$3.~T^2~is~proprotional~to~r^3$').shift(DOWN)

        self.play(Write(rule1))
        self.wait(3)
        self.play(Write(rule2))
        self.wait(4)
        self.play(Write(rule3))
        self.wait(10)


class UniversalGravitation(Scene):
    def construct(self):
        equationTex = Tex(r'$F_G = G\frac{M_1M_2}{r^2}$').shift(2 * UP)
        definitionTex1 = Tex(
            r'$G = Gravitational~constant~(Newton~didn\textquotesingle t~know~what~this~value~was)$').shift(UP).scale(0.8)
        definitionTex2 = Tex(r'$M_1M_2 = Masses~of~the~two~objects$')
        definitionTex3 = Tex(
            r'$r^2 = Distance~between~their~centers$').shift(DOWN)

        self.play(Write(equationTex))
        self.play(Write(definitionTex1))
        self.play(Write(definitionTex2))
        self.play(Write(definitionTex3))
        self.wait(4)


class GamePlan(Scene):
    def construct(self):
        basicGravity = Tex(r'$Basic~gravity: d = \frac{1}{2}gt^2$').shift(UP)
        universalGravity = Tex(
            r'$(i.e~gravity~not~just~when~objects~are~falling~straight~down)$')
        gamePlan1 = Tex(r'$Game~Plan:~$').shift(2 * UP)
        gamePlan2 = Tex(
            r'$1.~Some~force~keeps~planets~in~orbit:~maybe~gravity?$').shift(UP)
        gamePlan3 = Tex(
            r'$2.~A~planet\textquotesingle s~acceleration~keeps~it~in~orbit-gravity~is~related~to~acceleration$').scale(0.8)
        gamePlan4 = Tex(r'$3.~Find~acceleration,~find~gravity$').shift(DOWN)

        self.play(Write(basicGravity))
        self.play(Write(universalGravity))
        self.wait(1)
        self.play(Uncreate(VGroup(basicGravity, universalGravity)), run_time=4)
        self.play(Write(gamePlan1))
        self.wait(2)
        self.play(Write(gamePlan2))
        self.wait(5)
        self.play(Write(gamePlan3))
        self.wait(5)
        self.play(Write(gamePlan4))
        self.wait(5)


class NewtonMath(Scene):
    def construct(self):

        problemTex = Tex(
            r'$Ellipses~are~tricky,~and~circles~are~easy$').shift(3*UP)
        orbit = Ellipse(width=7, height=4, color=WHITE)
        circularOrbit = Circle(radius=3.5, color=WHITE)
        O = Dot([0, 0, 0], radius=0.08)
        radiusLine = Line([0, 0, 0], [3.03, 1.75, 0])
        OLabel = Tex(r'$O$').move_to([0, -0.5, 0])
        radiusLabel = Tex(r'$r$').move_to([1.1, 1, 0])
        vLabel = Tex(r'v').move_to([2.8, 2.5, 0])

        flatRadiusLine = Line([0, 0, 0], [3.5, 0, 0])
        flatRadiusLineLabel = Tex(r'$r$').move_to([1.25, 0.2, 0])
        P = Dot([3.5, 0, 0], radius=0.08)
        PLabel = Tex(r'$P$').move_to([3.8, 0, 0])

        travelLine = Line([3.5, 0, 0], [3.5, 2, 0])
        travelLineLabel = Tex(r'vt').move_to([3.8, 0.8, 0])
        R = Dot([3.5, 2, 0], radius=0.08)
        RLabel = Tex(r'$R$').move_to([3.8, 2, 0])

        Q = Dot([3.03, 1.75, 0], radius=0.08)
        QLabel = Tex(r'$Q$').move_to([2.5, 1.75, 0])

        ORLine = Line([0, 0, 0], [3.5, 2, 0])

        smallTravelLine = Line([3.5, 0, 0], [3.5, 1, 0])
        smallTravelLineLabel = Tex(r'vt').move_to([3.8, 0.5, 0])
        smallR = Dot([3.5, 1, 0], radius=0.08)
        smallRLabel = Tex(r'$R$').move_to([3.8, 1, 0])

        smallQ = Dot([3.35, 0.95, 0], radius=0.08)
        smallQLabel = Tex(r'$Q$').move_to([2.9, 1.2, 0])

        smallORLine = Line([0, 0, 0], [3.5, 1, 0])

        elbow = Elbow(width=0.3, angle=PI/2).move_to([3.3, 0.2, 0])

        self.play(Create(orbit))
        self.wait(4)
        self.play(Write(problemTex))
        self.wait(2)
        self.play(Uncreate(problemTex))
        self.play(ReplacementTransform(orbit, circularOrbit))
        self.wait(16)
        self.play(Create(O), Create(radiusLine), Write(
            VGroup(OLabel, radiusLabel, vLabel)))
        self.wait(8)
        self.play(Create(flatRadiusLine), Write(
            flatRadiusLineLabel), Create(P), Write(PLabel))
        self.wait(8)
        self.play(Create(travelLine), Write(
            travelLineLabel), Create(R), Write(RLabel))
        self.play(Create(Q), Write(QLabel))
        self.wait(8)
        self.play(Create(ORLine))
        self.wait(8)

        flatRadiusLineLabel = Tex(r'$r$').move_to([1.25, -0.2, 0])

        self.play(ReplacementTransform(travelLine, smallTravelLine), ReplacementTransform(travelLineLabel, smallTravelLineLabel),
                  ReplacementTransform(R, smallR), ReplacementTransform(
                      RLabel, smallRLabel), ReplacementTransform(Q, smallQ),
                  ReplacementTransform(QLabel, smallQLabel), ReplacementTransform(ORLine, smallORLine), Uncreate(radiusLine), Uncreate(radiusLabel), Write(flatRadiusLineLabel))
        self.wait(40)
        self.play(Create(elbow))


class NewtonPy(Scene):
    def construct(self):
        pythagoreanTheorem = Tex(
            r'$r^2 + (vt)^2 = (QR+r)^2$').move_to([0, 1, 0])
        expandedPy = Tex(
            r'$r^2 + v^2t^2 = QR^2+2QRr + r^2$').move_to([0, 0, 0])
        simp3Py = Tex(r'$v^2t^2=QR^2 + 2QRr$').move_to([0, 0, 0])
        addSimPy = Tex(r'$v^2t^2  \approx 2QRr$').move_to([0, -1, 0])
        simp4Py = Tex(
            r'$\frac{v^2t^2}{2r} = QR = \frac{1}{2}\frac{v^2}{r}t^2$').move_to([0, -1, 0])
        simp5Py = Tex(r'$g = \frac{v^2}{r}$').move_to([0, -2, 0])

        self.play(Write(pythagoreanTheorem))
        self.wait(4)
        self.play(Write(expandedPy))
        self.wait(6)
        self.play(ReplacementTransform(expandedPy, simp3Py))
        self.wait(9)
        self.play(Write(addSimPy))
        self.wait(3)
        self.play(ReplacementTransform(addSimPy, simp4Py))
        self.wait(13)
        self.play(Write(simp5Py))
        self.wait(6)


class FinalKepler(Scene):
    def construct(self):
        rule3 = Tex(r'$3.~T^2~is~proprotional~to~r^3$').move_to([0, 1, 0])
        distance = Tex(r'$d=rT$')
        periodDefinition = Tex(
            r'$T=\frac{distance}{velocity} = \frac{circumfrence}{v}=\frac{2 \pi r}{v}$').move_to([0, -1, 0])
        per2 = Tex(r'$T^2=\frac{2r^2}{v^2}~proportional~to~r^3$').move_to(
            [0, 2, 0])
        per3 = Tex(r'$v^2~proportional~to~\frac{1}{r},~\frac{v^2}{r}~proportional~to~\frac{1}{r^2}$').move_to(
            [0, 1, 0])
        note = Tex(r'$Note:~We~can~ignore~constants~since~we\textquotesingle re~looking~for~proportionality$').move_to(
            [0, 0, 0]).scale(0.8)
        final = Tex(r'$g~proportional~to~\frac{1}{r^2}$').move_to([0, -1, 0])

        self.play(Write(rule3), run_time=3)
        self.wait(8)
        self.play(Write(distance))
        self.play(Write(periodDefinition))
        self.wait(8)
        self.play(Uncreate(VGroup(rule3, distance, periodDefinition)))
        self.play(Write(periodDefinition))
        self.play(Write(per2))
        self.play(Write(note))
        self.wait(2)
        self.play(Write(per3))
        self.wait(10)
        self.play(Write(final))
        self.wait(10)


class Ending(Scene):
    def construct(self):
        congrats = Tex(r'$You~did~it!$').scale(3)
        limit = Tex(r'$\lim_{x \to 0}$')
        ending = Tex(r'$You~just~did~calculus!$').scale(2.5)

        self.play(Write(congrats))
        self.wait(5)
        self.play(Uncreate(congrats))
        self.play(Write(limit))
        self.wait(23)
        self.play(Uncreate(limit))
        self.play(Write(ending))
        self.wait(11)
