'''
PICASSO PROJECT
---------------
Your job is to make a cool picture.
You must use multiple colors.
You must have a coherent picture. No abstract art with random shapes.
You must use multiple types of graphic functions (e.g. circles, rectangles, lines, etc.)
Somewhere you must include a WHILE or FOR loop to create a repeating pattern.
Do not just redraw the same thing in the same location 10 times. 
You can contain multiple drawing commands in a loop, so you can draw multiple train cars for example.
Please use comments and blank lines to make it easy to follow your program. 
If you have 5 lines that draw a robot, group them together with blank lines above and below. 
Then add a comment at the top telling the reader what you are drawing.
IN THE WINDOW TITLE PLEASE PUT YOUR NAME.
When you are finished Pull Request your file to your instructor.
'''
import arcade

arcade.open_window(500, 400, "Picasso Project")
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()

arcade.draw_rectangle_filled(250, 200, 300, 250, arcade.color.BROWN_NOSE) #head

arcade.draw_circle_filled(200, 250, 30, arcade.color.BLACK) #eyes
arcade.draw_circle_filled(300, 250, 30, arcade.color.WHITE)
arcade.draw_circle_filled(200, 250, 10, arcade.color.PALATINATE_BLUE) #pupils
arcade.draw_circle_filled(300, 250, 10, arcade.color.ORCHID_PINK)


arcade.draw_arc_filled(250, 175, 50, 25, arcade.color.ORANGE, 90, 180) #beak/nose

arcade.draw_arc_filled(250, 145, 75, 45, arcade.color.YELLOW, 180, 360) #mouth

arcade.draw_text("What's up!?", 195, 40, arcade.color.BLUE_YONDER, 20)

for x_offset in range(5, 302, 15):      #hair
    arcade.draw_line(102+x_offset, 300, 102+x_offset, 335, arcade.color.PAKISTAN_GREEN, 4)












arcade.finish_render()
arcade.run()

