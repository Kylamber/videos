from manim import *

# manim -pql '.\gravitational slingshot.py' -qh Scene1 

class Scene1(Scene):
  def construct(self):
    imports = Code(
      "codes/import.py",
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
    
    figure = Code(
      "codes/figure.py",
      background="window",
      font="Monospace",
      language="python"
    )

    self.play(
      Create(figure),
      run_time=2
    )
    self.wait(2)
    self.play(
      Uncreate(figure)
    )
    self.wait(1)

    limit = Code(
      "codes/limit.py",
      background="window",
      font="Monospace",
      language="python"
    )

    self.play(
      Create(limit),
      run_time=2
    )
    self.wait(2)
    self.play(
      Uncreate(limit)
    )
    self.wait(1)

    plots = Code(
      "codes/plots.py",
      background="window",
      font="Monospace",
      language="python"
    )

    self.play(
      Create(plots),
      run_time=2
    )
    self.wait(2)
    self.play(
      Uncreate(plots)
    )
    self.wait(1)

    foriinrange = Code(
      "codes/foriinrange.py",
      background="window",
      font="Monospace",
      language="python"
    )

    self.play(
      Create(foriinrange),
      run_time=2
    )
    self.wait(2)
    self.play(
      Uncreate(foriinrange)
    )
    self.wait(1)

    animate = Code(
      "codes/animate.py",
      background="window",
      font="Monospace",
      language="python"
    )

    self.play(
      Create(animate),
      run_time=2
    )
    self.wait(2)
    self.play(
      Uncreate(animate)
    )
    self.wait(1)

    funcanim = Code(
      "codes/funcanim.py",
      background="window",
      font="Monospace",
      language="python"
    )

    self.play(
      Create(funcanim),
      run_time=2
    )
    self.wait(2)
    self.play(
      Uncreate(funcanim)
    )
    self.wait(1)

    display1 = Code(
      "codes/display1.py",
      background="window",
      font="Monospace",
      language="python"
    )

    self.play(
      Create(display1),
      run_time=2
    )
    self.wait(2)
    self.play(
      Uncreate(display1)
    )
    self.wait(1)

    display2 = Code(
      "codes/display2.py",
      background="window",
      font="Monospace",
      language="python"
    )

    self.play(
      Create(display2),
      run_time=2
    )
    self.wait(2)
    self.play(
      Uncreate(display2)
    )
    self.wait(1)

    saveanim = Code(
      "codes/saveanim.py",
      background="window",
      font="Monospace",
      language="python"
    )

    self.play(
      Create(saveanim),
      run_time=2
    )
    self.wait(2)
    self.play(
      Uncreate(saveanim)
    )
    self.wait(1)

    gerakparabola = Code(
      "codes/gerakparabola.py",
      background="window",
      font="Monospace",
      language="python"
    )

    self.play(
      Create(gerakparabola),
      run_time=2
    )
    self.wait(2)
    self.play(
      Uncreate(gerakparabola)
    )
    self.wait(1)

