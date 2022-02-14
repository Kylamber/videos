from manim import *

# manim -pql '.\gravitational slingshot.py' -qh Scene1 

class Scene1(Scene):
  def construct(self):
    bagirata = Code(
      "codes/1bagirata.py",
      background="window",
      font="Monospace",
      language="python"
    )

    self.play(
      Create(bagirata),
      run_time=2
    )
    self.wait(2)
    self.play(
      Uncreate(bagirata)
    )
    self.wait(1)
    
    luas = Code(
      "codes/2luas.py",
      background="window",
      font="Monospace",
      language="python"
    )

    self.play(
      Create(luas),
      run_time=2
    )
    self.wait(2)
    self.play(
      Uncreate(luas)
    )
    self.wait(1)

    luas1000 = Code(
      "codes/3luas1000.py",
      background="window",
      font="Monospace",
      language="python"
    )

    self.play(
      Create(luas1000),
      run_time=2
    )
    self.wait(2)
    self.play(
      Uncreate(luas1000)
    )
    self.wait(1)

    versikelebihan = Code(
      "codes/4versikelebihan.py",
      background="window",
      font="Monospace",
      language="python"
    )

    self.play(
      Create(versikelebihan),
      run_time=2
    )
    self.wait(2)
    self.play(
      Uncreate(versikelebihan)
    )
    self.wait(1)

    trapesium = Code(
      "codes/5trapesium.py",
      background="window",
      font="Monospace",
      language="python"
    )

    self.play(
      Create(trapesium),
      run_time=2
    )
    self.wait(2)
    self.play(
      Uncreate(trapesium)
    )
    self.wait(1)

    trapesium1000 = Code(
      "codes/6trapesium1000.py",
      background="window",
      font="Monospace",
      language="python"
    )

    self.play(
      Create(trapesium1000),
      run_time=2
    )
    self.wait(2)
    self.play(
      Uncreate(trapesium1000)
    )
    self.wait(1)

    simpsontex = MathTex(r"\int_a^b f(x) dx \approx \frac{b-a}{3n} \left( f(x_0) + 4 \sum_{i = 1,3,5,...}^{n-1} f(x_i) + 2 \sum_{i = 2,4,6,...}^{n-2} f(x_i) + f(x_{n})\right)", font_size=36)

    self.play(
      Create(simpsontex),
      run_time=2
    )
    self.wait(2)
    self.play(
      Uncreate(simpsontex)
    )
    self.wait(1)

    simpson = Code(
      "codes/7simpson.py",
      background="window",
      font="Monospace",
      language="python"
    )

    self.play(
      Create(simpson),
      run_time=2
    )
    self.wait(2)
    self.play(
      Uncreate(simpson)
    )
    self.wait(1)

    trapvssimp = Code(
      "codes/8trapvssimp.py",
      background="window",
      font="Monospace",
      language="python"
    )

    self.play(
      Create(trapvssimp),
      run_time=2
    )
    self.wait(2)
    self.play(
      Uncreate(trapvssimp)
    )
    self.wait(1)

    trapvssimp2 = Code(
      "codes/9trapvssimp2.py",
      background="window",
      font="Monospace",
      language="python"
    )

    self.play(
      Create(trapvssimp2),
      run_time=2
    )
    self.wait(2)
    self.play(
      Uncreate(trapvssimp2)
    )
    self.wait(1)
