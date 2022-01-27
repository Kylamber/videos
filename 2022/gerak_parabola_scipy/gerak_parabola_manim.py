from manim import *

# manim -pql '.\gerak_parabola_manim.py' -qh Scene1 

class Scene1(Scene):
  def construct(self):
    imports = Code(
      "codes/imports.py",
      background="window",
      font="Monospace",
      language="python"
    )

    self.play(
      Create(imports),
      run_time=2
    )
    self.wait(2)
    self.play(
      Uncreate(imports)
    )
    self.wait(1)
    
    diff1 = Code(
      "codes/diff1.py",
      background="window",
      font="Monospace",
      language="python"
    )

    self.play(
      Create(diff1),
      run_time=2
    )
    self.wait(2)
    self.play(
      Uncreate(diff1)
    )
    self.wait(1)

    solve1 = Code(
      "codes/solve1.py",
      background="window",
      font="Monospace",
      language="python"
    )

    self.play(
      Create(solve1),
      run_time=2
    )
    self.wait(2)
    self.play(
      Uncreate(solve1)
    )
    self.wait(1)

    diff2 = Code(
      "codes/diff2.py",
      background="window",
      font="Monospace",
      language="python"
    )

    self.play(
      Create(diff2),
      run_time=2
    )
    self.wait(2)
    self.play(
      Uncreate(diff2)
    )
    self.wait(1)

    solve2 = Code(
      "codes/solve2.py",
      background="window",
      font="Monospace",
      language="python"
    )

    self.play(
      Create(solve2),
      run_time=2
    )
    self.wait(2)
    self.play(
      Uncreate(solve2)
    )
    self.wait(1)
