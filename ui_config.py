import pygame

display_dimensions = (-1, -1)
screen : pygame.Surface = -1
bg_col = pygame.Color("white")
clock = pygame.time.Clock()

#List of the available menus
menus = []
#index of current menu being shown
current_menu_index = -1
next_menu_index = -1

#If true display current menu (if something on screen changes)
redraw_stuff = True

exit_loop = False
clicking = False
key_pressed = None

select_rect_col = pygame.Color("red")