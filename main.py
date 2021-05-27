#***********************************************
#
# Program Author: Shirdel Yan, Sihan Zeng
# Revision Date: 26/5/2021
# Program Name: Pygame Project
# Description:Pygame Project
#
#***********************************************

#import libraries
import pygame
import random
import time

#initialize pygame
pygame.init()

#define colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

#create the screen
size = (1200, 800)
gameDisplay = pygame.display.set_mode(size)

#initialize the title and icon
pygame.display.set_caption("Polyvasion")
icon = pygame.image.load("Assets/angrycircle.png")
pygame.display.set_icon(icon)

#initialize the backgrounds
titlescreen_background = pygame.image.load("Assets/blue_polygons_background.png")
titlescreen_background = pygame.transform.scale(titlescreen_background, size)

#initialize the fonts
bigfont = pygame.font.SysFont("arial",50)
smallfont = pygame.font.SysFont("arial",15)

#declare variables
quiz_score = 0



#functions
def button(txt, w, h, x, y, color1, color2, function, textsize):
  mousepos = pygame.mouse.get_pos() #current position of mouse
  click = pygame.mouse.get_pressed() #state of mouse button

def displaytext(text, color, x, y):
  text = bigfont.render(text, True, color)
  gameDisplay.blit(text, (x, y))

#title loop
def titlescreen():
  titlescr = True
  x = 0
  y = 0    
  while titlescr:
    for event in pygame.event.get():
      print(event)
      if event.type == pygame.QUIT:
        pygame.quit()
        exit()
    gameDisplay.fill(white)
    gameDisplay.blit(titlescreen_background, (0,0))
    displaytext("Polyvasion", white, 600, 500)
    displaytext("Shirdel Yan, Sihan Zeng", white, 1000, 600)
    pygame.display.update()
titlescreen()