'''
FLAG PROJECT
---------------
Make your flag 260 pixels tall
Use the scaling image on the website to determine other dimensions
The hexadecimal colors for the official flag are red:#BF0A30 and blue:#002868
Title the window, "The Stars and Stripes"
I used a draw_text command and used 20 pt. asterisks for the stars.
We will have a competition to see who can make this flag in the least lines of code.
The record is 16! You will have to use some loops to achieve this.
'''

import arcade

#Height of flag 260 pixels, Fly of flag 494 pixels?
#Red = (191, 10, 48)
#Blue = (0, 40, 104)

arcade.open_window(500, 500, "American Flag")
arcade.set_background_color(arcade.color.WHITE)

arcade.start_render()

for x_offset in range(0, 250, 40):          #Stripes
    arcade.draw_rectangle_filled(250, 20+x_offset, 20, 494, (191, 10, 48), 90)

arcade.draw_rectangle_filled(94, 200, 182, 140, (0, 40, 104))   #Union
#

for x_offset in range(90, 220, 28):
    arcade.draw_text("*   *   *   *   *   *", 10, 40+x_offset, arcade.color.BLACK, 20)
    arcade.draw_text("*   *   *   *   *", 10, 40+x_offset, arcade.color.BLACK, 20)
arcade.finish_render()

arcade.run()



