from manim import *

# manim -pql '.\gravitational slingshot.py' -qh Scene1 

# F = gm1m2/r^2 scene
class Scene1(Scene):
  def construct(self):
    mg = MathTex(r"F=mg", font_size=96)
    #fm = MathTex(r"F = G\frac{m_1m_2}{r^2}", font_size=96)
    fm = MathTex(r"F =", r"G", r"{m_1", r"m_2", r"\over", r"r^2}", font_size=96)

    circm1 = Circle(color=BLUE, fill_opacity=0.7).scale(0.5).shift(2*LEFT)
    circm2 = Circle(color=GREEN, fill_opacity=0.7).scale(0.5).shift(2*RIGHT)
    m1 = MathTex(r"m_1", font_size=96).scale(0.5).next_to(circm1, UP)
    m2 = MathTex(r"m_2", font_size=96).scale(0.5).next_to(circm2, UP)
    liner = Line(circm1.get_center(), circm2.get_center()).set_color(ORANGE)
    r = MathTex(r"r", font_size=96).scale(0.5).next_to(liner, DOWN)

    G = MathTex(r"G = 6.67\times10^{-11}\,\mathrm{m}^3\cdot\mathrm{kg}^{-1}\cdot\mathrm{s}^{-2}", font_size=int(96/2)).shift(2*DOWN)

    cross = Cross(fm[1:])

    self.play(
      Write(mg)
    )
    self.wait(4)
    self.play(
      Create(cross)
    )
    self.wait(2)
    self.play(
      Uncreate(cross),
    )
    self.play(
      ReplacementTransform(mg, fm)
    )
    self.wait(3)
    self.play(
      fm.animate.scale(0.5).shift(2*UP),
      GrowFromCenter(circm1),
      GrowFromCenter(circm2),
    )

    framebox1 = SurroundingRectangle(fm[2])
    framebox2 = SurroundingRectangle(fm[3])
    framebox3 = SurroundingRectangle(fm[5])
    framebox4 = SurroundingRectangle(fm[1])

    self.play(
      Create(m1),
      Create(framebox1),
      run_time=0.5
    )
    self.wait(0.5)
    self.play(
      Create(m2),
      ReplacementTransform(framebox1, framebox2),
      run_time=0.5
    )
    self.wait(0.5)
    self.play(
      Create(liner),
      run_time=0.5
    )
    self.play(
      Create(r),
      ReplacementTransform(framebox2, framebox3)
    )
    self.wait(1)
    self.play(
      ReplacementTransform(framebox3, framebox4),
      Create(G)
    )
    self.wait(2)

# F = gm1m2/rnorm^2 rhat vector scene
class Scene2(Scene):
  def construct(self):
    axes = Axes(x_range=[-3, 3, 1], x_length=5, y_range=[-3, 3, 1], y_length=5)
    axes.add_coordinates()

    fm = MathTex(r"\vec{F} =", r"G", r"{m_1", r"m_2", r"\over", r"||\vec{r}||^2}", r"\hat{r}", font_size=48).shift(3*LEFT)
    r_norm = MathTex(r"||r||", r"= \sqrt{x^2+y^2}", font_size=48)
    r_hat = MathTex(r"\hat{r} = {\vec{r} \over", r"||r||", r"}", font_size=48)

    self.play(
      Create(axes),
      run_time=2
    )
    self.play(
      axes.animate.shift(3*RIGHT)
    )

    def arrow_updater(mobj):
      mobj.put_start_and_end_on(dot2.get_center(), dot.get_center())

    def r_vec_updater(mobj):
      mobj.next_to(arrow, 0.25*RIGHT)

    dot = Dot(axes.coords_to_point(2, 2)).set_color(BLUE)
    dot2 = Dot(axes.coords_to_point(0, 0)).set_color(RED)
    arrow = Arrow(axes.coords_to_point(0, 0), axes.coords_to_point(2, 2), stroke_width=2, buff=0, max_tip_length_to_length_ratio=0.1)

    r_vec = MathTex(r"\vec{r}", font_size=48).next_to(arrow)

    axes_group = VGroup(axes, arrow, dot, dot2, r_vec)
    # textx = DecimalNumber(0, font_size=48).next_to(dot, RIGHT)
    # comma = Text(",", font_size=48).next_to(textx, RIGHT)
    # texty = DecimalNumber(0, font_size=48).next_to(comma, RIGHT)

    # # Just use matrix...
    # def textx_updater(mobj):
    #   val = np.around(axes.point_to_coords(dot.get_center()), decimals=2)
    #   mobj.set_value(val[0])
    #   mobj.next_to(dot, RIGHT)

    # def texty_updater(mobj):
    #   val = np.around(axes.point_to_coords(dot.get_center()), decimals=2)
    #   mobj.set_value(val[1])
    #   mobj.next_to(dot, 3*RIGHT)
    
    # textx.add_updater(textx_updater)   
    # comma.add_updater(lambda mobj: mobj.next_to(dot, 2*RIGHT))   
    # texty.add_updater(texty_updater)   

    self.play(
      Create(fm)
    )
    self.play(
      Create(dot), 
      Create(dot2),
    )
    arrow.add_updater(arrow_updater)
    r_vec.add_updater(r_vec_updater)
    self.play(
      Create(arrow),
      Create(r_vec)
    )
    self.play(
      dot.animate.shift(LEFT)
    )
    self.play(
      dot.animate.shift(DOWN)
    )
    self.play(
      dot.animate.shift(RIGHT)
    )
    self.play(
      dot.animate.shift(UP)
    )
    self.wait(2)

    self.play(
      FadeOut(axes_group, shift=RIGHT),
      fm.animate.shift(3*RIGHT, 2*UP)
    )

    framebox_r_norm = SurroundingRectangle(fm[5])
    framebox_r_hat = SurroundingRectangle(fm[6])

    formula_group = VGroup(framebox_r_hat, r_hat, fm)

    self.play(
      Create(r_norm),
      Create(framebox_r_norm)
    )
    self.wait(2)

    self.play(
      TransformMatchingTex(r_norm, r_hat),
      ReplacementTransform(framebox_r_norm, framebox_r_hat)
    )
    self.wait(2)

    self.play(
      FadeOut(formula_group)
    )
    self.wait(1)

    numberline = NumberLine(
      x_range=[-5, 5],
      length=10,
      include_numbers=True
    )

    dot3 = Dot(numberline.number_to_point(4), radius=0.1).set_color(RED)

    def arrow_dir_rhat(mobj):
      dot_point = numberline.point_to_number(dot3.get_center())
      if dot_point == 0:
        dot_point = 0.01  
      mobj.put_start_and_end_on(
        numberline.number_to_point(0), 
        numberline.number_to_point(dot_point/abs(dot_point))
      )
      mobj.set_stroke_width_from_length()
    
    def arrow_dir_r(mobj):
      if np.all(numberline.number_to_point(0) - dot3.get_center() == 0):
        mobj.put_start_and_end_on(numberline.number_to_point(0), dot3.get_center() - [-0.01, 0, 0])
      else:
        mobj.put_start_and_end_on(numberline.number_to_point(0), dot3.get_center())
    
    r_hat_symb = MathTex(r"\hat{r}", font_size=48).shift(UP)
    r_vec_symb = MathTex(r"\hat{r}", r"\times ||\vec{r}||", font_size=48).shift(UP)

    arrow_rhat = Arrow(numberline.number_to_point(0), numberline.number_to_point(1), stroke_width=5,  buff=0).set_color(BLUE)
    arrow_rhat.add_updater(arrow_dir_rhat)

    self.play(
      Create(numberline),
      Create(dot3)
    )
    self.play(
      Create(arrow_rhat),
      Create(r_hat_symb)
    )

    self.play(
      dot3.animate.move_to(numberline.number_to_point(-4))
    )
    self.play(
      dot3.animate.move_to(numberline.number_to_point(2))
    )

    arrow_r = Arrow(numberline.number_to_point(0), dot3.get_center(), stroke_width=5, buff=0).set_color(BLUE)
    arrow_r.add_updater(arrow_dir_r)
    self.play(
      TransformMatchingTex(r_hat_symb, r_vec_symb),
      ReplacementTransform(arrow_rhat, arrow_r)
    )
    self.play(
      dot3.animate.move_to(numberline.number_to_point(-2))
    )
    self.play(
      dot3.animate.move_to(numberline.number_to_point(4))
    )
    self.wait(2)

# acceleration differential
class Scene3(Scene):
  def construct(self):
    fma = MathTex(r"\vec{F}", r"=", r"m", r"\vec{a}", font_size=48)
    magm1m2 = MathTex(r"m", 
                      r"\vec{a}", 
                      r"=", 
                      r"G", r"{"
                      r"m_1", 
                      r"m_2", r"\over",
                      r"||\vec{r}||^2", r"}",
                      r"\hat{r}", font_size=48)
    m1agm1m2 = MathTex(r"m_1", 
                      r"\vec{a}", 
                      r"=", 
                      r"G", r"{"
                      r"m_1", 
                      r"m_2", r"\over",
                      r"||\vec{r}||^2", r"}",
                      r"\hat{r}", font_size=48)
    agm2 = MathTex(r"\vec{a}", 
                    r"=", 
                    r"G", r"{",
                    r"m_2", r"\over",
                    r"||\vec{r}||^2", r"}",
                    r"\hat{r}", font_size=48)

    self.play(
      Create(fma)
    )
    self.wait(2)
    self.play(
      TransformMatchingTex(fma, magm1m2)
    )
    self.wait(2)
    self.play(
      TransformMatchingTex(magm1m2, m1agm1m2)
    )
    self.wait(2)
    self.play(
      TransformMatchingTex(m1agm1m2, agm2)
    )
    self.wait(2)
    self.play(
      FadeOut(agm2)
    )

# the codes
class Scene4(Scene):
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
    acceleration = Code(
      "codes/acceleration.py",
      background="window",
      font="Monospace",
      language="python"
    )

    self.play(
      Create(acceleration),
      run_time=2
    )
    self.wait(2)
    self.play(
      Uncreate(acceleration)
    )

    diff_earth = Code(
      "codes/diff_earth.py",
      background="window",
      font="Monospace",
      language="python"
    )

    self.play(
      Create(diff_earth),
      run_time=2
    )
    self.wait(2)
    self.play(
      Uncreate(diff_earth)
    )

    solve_ivp_earth = Code(
      "codes/solve_ivp_earth.py",
      background="window",
      font="Monospace",
      language="python"
    )

    self.play(
      Create(solve_ivp_earth),
      run_time=2
    )
    self.wait(2)
    self.play(
      Uncreate(solve_ivp_earth)
    )

    diff_jup_1 = Code(
      "codes/diff_jup_1.py",
      background="window",
      font="Monospace",
      language="python",
      font_size=16
    )

    self.play(
      Create(diff_jup_1),
      run_time=2
    )
    self.wait(2)
    self.play(
      Uncreate(diff_jup_1)
    )

    solve_ivp_jup_1 = Code(
      "codes/solve_ivp_jup_1.py",
      background="window",
      font="Monospace",
      language="python"
    )

    self.play(
      Create(solve_ivp_jup_1),
      run_time=2
    )
    self.wait(2)
    self.play(
      Uncreate(solve_ivp_jup_1)
    )

    diff_jup_2 = Code(
      "codes/diff_jup_2.py",
      background="window",
      font="Monospace",
      language="python",
      font_size=16
    )

    self.play(
      Create(diff_jup_2),
      run_time=2
    )
    self.wait(2)
    self.play(
      Uncreate(diff_jup_2)
    )

    solve_ivp_jup_2 = Code(
      "codes/solve_ivp_jup_2.py",
      background="window",
      font="Monospace",
      language="python"
    )

    self.play(
      Create(solve_ivp_jup_2),
      run_time=2
    )
    self.wait(2)
    self.play(
      Uncreate(solve_ivp_jup_2)
    )

    solve_ivp_jup_3 = Code(
      "codes/solve_ivp_jup_3.py",
      background="window",
      font="Monospace",
      language="python"
    )

    self.play(
      Create(solve_ivp_jup_3),
      run_time=2
    )
    self.wait(2)
    self.play(
      Uncreate(solve_ivp_jup_3)
    )

    solve_ivp_jup_4 = Code(
      "codes/solve_ivp_jup_4.py",
      background="window",
      font="Monospace",
      language="python"
    )

    self.play(
      Create(solve_ivp_jup_4),
      run_time=2
    )
    self.wait(2)
    self.play(
      Uncreate(solve_ivp_jup_4)
    )

    solve_ivp_earth_2 = Code(
      "codes/solve_ivp_earth_2.py",
      background="window",
      font="Monospace",
      language="python"
    )

    self.play(
      Create(solve_ivp_earth_2),
      run_time=2
    )
    self.wait(2)
    self.play(
      Uncreate(solve_ivp_earth_2)
    )

# This scene is between the import code and the accel code.
class Scene5(Scene):
  def construct(self):
    axes = Axes(
      x_range=[-3, 3, 1], 
      x_length=5, 
      y_range=[-3, 3, 1], 
      y_length=5, 
      axis_config={"include_numbers": False})

    earth = Dot(
      axes.coords_to_point(1.5, 0),
      radius=0.15
    ).set_color(BLUE)

    sun = Dot(
      radius=0.25
    ).set_color(RED)

    orbit = Circle(radius=1.25, color=BLUE)

    self.play(
      Create(axes),
      Create(earth),
      Create(sun),
      Create(orbit)
    )

    self.play(
      MoveAlongPath(
        earth, 
        orbit,
        rate_func=linear
      ),
      run_time=5
    )

class Scene6(Scene):
  def construct(self):
    theta = ValueTracker(45)

    jupiter = Dot(color=GOLD, radius=0.15).shift(3*RIGHT)
    jupiter_copy = jupiter.copy()
    jupiter.rotate(
      theta.get_value() * DEGREES,
      about_point=ORIGIN
    )

    line = Line(ORIGIN, jupiter.get_center())
    line_ref = Line(ORIGIN, RIGHT)
    axes = Axes(
      x_range=[-3, 3, 1], 
      x_length=7, 
      y_range=[-3, 3, 1], 
      y_length=7, 
      axis_config={"include_numbers": False})

    angle = Angle(line_ref, line, radius=1, other_angle=False)
    texta = MathTex(r"\theta").move_to(Angle(
          line_ref, line, radius=1 + 3 * SMALL_BUFF, other_angle=False
        ).point_from_proportion(0.5)
    )

    r = MathTex(r"r").move_to(line).shift(0.2*(UP+LEFT))

    self.play(
      Create(axes)
    )
    self.play(
      Create(jupiter),
      Create(line),
      Create(angle),
      Create(texta),
      Create(r)
    )

    line_x = Line(
      jupiter.get_center() * [1, 1, 0],
      jupiter.get_center() * [0, 1, 0],
      color=YELLOW
    )

    line_y = Line(
      jupiter.get_center() * [1, 1, 0],
      jupiter.get_center() * [1, 0, 0],
      color=YELLOW
    )

    rx = MathTex(r"r\cos\theta", color=YELLOW).next_to(line_x, UP)
    ry = MathTex(r"r\sin\theta", color=YELLOW).next_to(line_y)

    line.add_updater(
      lambda x: x.put_start_and_end_on(
        ORIGIN,
        jupiter.get_center()
      )
    )

    line_x.add_updater(
      lambda x: x.put_start_and_end_on(
        jupiter.get_center() * [1, 1, 0],
        jupiter.get_center() * [0, 1, 0]
      )
    )

    line_y.add_updater(
      lambda x: x.put_start_and_end_on(
        jupiter.get_center() * [1, 1, 0],
        jupiter.get_center() * [1, 0, 0],
      )
    )

    r.add_updater(
      lambda x: x.move_to(line).shift(0.2*(UP+LEFT))
    )

    rx.add_updater(
      lambda x: x.next_to(line_x, UP)
    )
    
    ry.add_updater(
      lambda x: x.next_to(line_y)
    )

    jupiter.add_updater(
      lambda x: x.become(jupiter_copy.copy()).rotate(
        theta.get_value() * DEGREES, about_point=ORIGIN
      )
    )

    angle.add_updater(
      lambda x: x.become(Angle(line_ref, line, radius=1, other_angle=False))
    )

    texta.add_updater(
      lambda x: x.move_to(
        Angle(
          line_ref, line, radius=1 + 3 * SMALL_BUFF, other_angle=False
        ).point_from_proportion(0.5)
      )
    )

    self.play(
      Create(line_x),
      Create(line_y)
    )

    self.play(
      Create(rx),
      Create(ry),
      Uncreate(r)
    )

    self.wait(1)

    self.play(
      theta.animate.set_value(150)
    )

    self.play(
      theta.animate.set_value(10)
    )

    self.play(
      theta.animate.set_value(45)
    )

    self.wait(1)

    self.play(
      Uncreate(rx),
      Uncreate(ry),
      Uncreate(line_x)
    )

    #vel_point = Dot().shift(jupiter.get_center() + RIGHT)
    #vel_point.rotate((theta - 90) * DEGREES, about_point=jupiter.get_center())

    arrow = Arrow(
      jupiter.get_center(), 
      jupiter.get_center() + 2*RIGHT,
      buff=0
      #vel_point.get_center()
    )

    arrow_x = Arrow(
      jupiter.get_center(), 
      jupiter.get_center() + 2*RIGHT*np.sin(theta.get_value() * DEGREES),
      buff=0,
      color=YELLOW
    )

    arrow_y = Arrow(
      jupiter.get_center(), 
      jupiter.get_center() - 2*UP*np.cos(theta.get_value() * DEGREES),
      buff=0,
      color=YELLOW
    )

    arrow.rotate((theta.get_value() - 90) * DEGREES, about_point=jupiter.get_center())

    angle2 = Angle(line_y, arrow, radius=0.5, other_angle=False)
    alpha = MathTex(r"\theta").move_to(Angle(
          line_y, arrow, radius=0.5 + 3 * SMALL_BUFF, other_angle=False
        ).point_from_proportion(0.5)
    )

    angle2.add_updater(
      lambda x: x.become(
        Angle(line_y, arrow, radius=0.5, other_angle=False)
      )
    )

    alpha.add_updater(
      lambda x: x.move_to(
        Angle(
          line_y, arrow, radius=0.5 + 3 * SMALL_BUFF, other_angle=False
        ).point_from_proportion(0.5)
      )
    )

    arrow.add_updater(
      lambda x: x.become(
        Arrow(
          jupiter.get_center(), 
          jupiter.get_center() + 2*RIGHT,
          buff=0)
        ).rotate((theta.get_value() - 90) * DEGREES, about_point=jupiter.get_center())
    )
    
    arrow_x.add_updater(
      lambda x: x.become(
        Arrow(
          jupiter.get_center(), 
          jupiter.get_center() + 2*RIGHT*np.sin(theta.get_value() * DEGREES),
          buff=0,
          color=YELLOW
        )
      )
    )

    arrow_y.add_updater(
      lambda x: x.become(
        Arrow(
          jupiter.get_center(), 
          jupiter.get_center() - 2*UP*np.cos(theta.get_value() * DEGREES),
          buff=0,
          color=YELLOW
        )
      )
    )

    vsintheta = MathTex(r"v\sin\theta", color=YELLOW).next_to(arrow_x, UP)
    vcostheta = MathTex(r"-v\cos\theta", color=YELLOW).next_to(arrow_y, LEFT)

    vsintheta.add_updater(
      lambda x: x.next_to(arrow_x, UP)
    )

    vcostheta.add_updater(
      lambda x: x.next_to(arrow_y, LEFT)
    )



    self.play(
      Create(arrow),
      Create(angle2),
      Create(alpha),
      line_y.animate.set_color(WHITE)
    )

    self.play(
      Create(arrow_x),
      Create(arrow_y)
    )

    self.play(
      Create(vsintheta),
      Create(vcostheta)
    )

    self.play(
      theta.animate.set_value(150)
    )

    self.play(
      theta.animate.set_value(10)
    )

    self.play(
      theta.animate.set_value(45)
    )

    self.wait(1)

    self.wait(1)

class Scene7(Scene):
  def construct(self):
    animasi = Code(
      "codes/animasi.py",
      background="window",
      font="Monospace",
      language="python",
      font_size="16"
    )

    self.play(
      Create(animasi),
      run_time=2
    )
    self.wait(2)
    self.play(
      Uncreate(animasi)
    )

    plot = Code(
      "codes/plot.py",
      background="window",
      font="Monospace",
      language="python",
      font_size="16"
    )

    self.play(
      Create(plot),
      run_time=2
    )
    self.wait(2)
    self.play(
      Uncreate(plot)
    )

class Scene8(Scene):
  def construct(self):
    dvdt = MathTex(r"\vec{a} = \frac{d\vec{v}}{dt}")
    drdt = MathTex(r"\vec{v} = \frac{d\vec{r}}{dt}")

    self.play(
      Create(dvdt)
    )

    self.wait(1)

    self.play(
      Uncreate(dvdt)
    )

    self.wait(1)

    self.play(
      Create(drdt)
    )

    self.wait(1)

    self.play(
      Uncreate(drdt)
    )
