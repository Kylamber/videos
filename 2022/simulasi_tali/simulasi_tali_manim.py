from manim import *

# manim -pql '.\root finding manim.py' -qh Scene1 

class Scene1(Scene):
  def construct(self):
    variabel1 = Code(
      "codes/1variabel.py",
      background="window",
      font="Monospace",
      language="python"
    )

    self.play(
      Create(variabel1),
      run_time=2
    )
    self.wait(2)
    self.play(
      Uncreate(variabel1)
    )
    self.wait(1)

    diff4beban2 = Code(
      "codes/2diff4beban.py",
      background="window",
      font="Monospace",
      language="python"
    )

    self.play(
      Create(diff4beban2),
      run_time=2
    )
    self.wait(2)
    self.play(
      Uncreate(diff4beban2)
    )
    self.wait(1)

    diffnbeban3 = Code(
      "codes/3diffnbeban.py",
      background="window",
      font="Monospace",
      language="python"
    )

    self.play(
      Create(diffnbeban3),
      run_time=2
    )
    self.wait(2)
    self.play(
      Uncreate(diffnbeban3)
    )
    self.wait(1)

    solve4 = Code(
      "codes/4solve.py",
      background="window",
      font="Monospace",
      language="python"
    )

    self.play(
      Create(solve4),
      run_time=2
    )
    self.wait(2)
    self.play(
      Uncreate(solve4)
    )
    self.wait(1)

    solve5 = Code(
      "codes/5solve2.py",
      background="window",
      font="Monospace",
      language="python"
    )

    self.play(
      Create(solve5),
      run_time=2
    )
    self.wait(2)
    self.play(
      Uncreate(solve5)
    )
    self.wait(1)

    animasi6 = Code(
      "codes/6animasi.py",
      background="window",
      font="Monospace",
      language="python"
    )

    self.play(
      Create(animasi6),
      run_time=2
    )
    self.wait(2)
    self.play(
      Uncreate(animasi6)
    )
    self.wait(1)
