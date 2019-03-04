"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Jonah Egertson.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

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


import rosegraphics as rg

window = rg.TurtleWindow()


smoke = rg.SimpleTurtle()
smoke.pen = rg.Pen('gray',15)

angle = 75
i = 16

for k in range(i):
    smoke.left(angle)
    smoke.forward(35)
    angle=angle/(i/(1-i))

mtn = rg.SimpleTurtle()
mtn.pen = rg.Pen('brown',15)

mtn.right(135)

for k in range(i):
    mtn.forward(30)
    mtn.left(45/(i/8-i))


mtn2 = rg.SimpleTurtle()
mtn2.pen = rg.Pen('brown',15)

mtn2.right(45)

for k in range(i):
    mtn2.forward(30)
    mtn2.right(45/(i/8-i))

mtn2.left(173.6)
mtn2.forward(880)

window.close_on_mouse_click()