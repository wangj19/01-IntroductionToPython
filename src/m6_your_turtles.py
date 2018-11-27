"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Jiadi Wang
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################
import rosegraphics as rg
window = rg.TurtleWindow()
blueone = rg.SimpleTurtle('turtle')
blueone.pen = rg.Pen('midnight blue', 10)
blueone.speed = 10
radius = 120
for k in range(7):

    blueone.draw_circle(radius)
    blueone.pen_up()
    blueone.right(90)
    blueone.forward(20)
    blueone.left(90)
    blueone.pen_down()
    radius = radius - 8

blueone.draw_circle(radius=200)

redone = rg.SimpleTurtle('turtle')
redone.pen = rg.Pen('red',8)
redone.speed = 10
redone.right(90)
redone.forward(180)
redone.left(90)
redone.draw_circle(220)

window.close_on_mouse_click()
########################################################################
# DONE: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
