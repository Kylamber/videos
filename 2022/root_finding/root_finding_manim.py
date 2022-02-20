from manim import *

# manim -pql '.\root finding manim.py' -qh Scene1 

class Scene1(Scene):
  def construct(self):
    bisection1 = Code(
      "codes/1bisection.py",
      background="window",
      font="Monospace",
      language="python"
    )

    self.play(
      Create(bisection1),
      run_time=2
    )
    self.wait(2)
    self.play(
      Uncreate(bisection1)
    )
    self.wait(1)

    bisection2 = Code(
      "codes/2bisection.py",
      background="window",
      font="Monospace",
      language="python"
    )

    self.play(
      Create(bisection2),
      run_time=2
    )
    self.wait(2)
    self.play(
      Uncreate(bisection2)
    )
    self.wait(1)

    rf = Code(
      "codes/3rf.py",
      background="window",
      font="Monospace",
      language="python"
    )

    self.play(
      Create(rf),
      run_time=2
    )
    self.wait(2)
    self.play(
      Uncreate(rf)
    )
    self.wait(1)

    bisecvrf1 = Code(
      "codes/4bisecvrf.py",
      background="window",
      font="Monospace",
      language="python"
    )

    self.play(
      Create(bisecvrf1),
      run_time=2
    )
    self.wait(2)
    self.play(
      Uncreate(bisecvrf1)
    )
    self.wait(1)

    bisecvrf2 = Code(
      "codes/5bisecvrf.py",
      background="window",
      font="Monospace",
      language="python"
    )

    self.play(
      Create(bisecvrf2),
      run_time=2
    )
    self.wait(2)
    self.play(
      Uncreate(bisecvrf2)
    )
    self.wait(1)

    newton1 = Code(
      "codes/6newton.py",
      background="window",
      font="Monospace",
      language="python"
    )

    self.play(
      Create(newton1),
      run_time=2
    )
    self.wait(2)
    self.play(
      Uncreate(newton1)
    )
    self.wait(1)

    newton2 = Code(
      "codes/7newton.py",
      background="window",
      font="Monospace",
      language="python"
    )

    self.play(
      Create(newton2),
      run_time=2
    )
    self.wait(2)
    self.play(
      Uncreate(newton2)
    )
    self.wait(1)

    secant = Code(
      "codes/8secant.py",
      background="window",
      font="Monospace",
      language="python"
    )

    self.play(
      Create(secant),
      run_time=2
    )
    self.wait(2)
    self.play(
      Uncreate(secant)
    )
    self.wait(1)
