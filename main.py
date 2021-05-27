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
x = 1200
y = 800
size = (x, y)
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
def button(txt, w, h, x, y, colora, colori, action):
  mousepos = pygame.mouse.get_pos() #current position of mouse
  click = pygame.mouse.get_pressed() #state of mouse button
  #check if mouse is on button
  if x+w > mousepos[0] > x and y+h > mousepos[1] > y:
    pygame.draw.rect(gameDisplay, colora ,(x,y,w,h))
    #check left click state
    if click[0] == 1:
      if action == "game":
        print("game")
      if action == "tutorial":
        print("tutorial")
      if action == "quiz":
        print("quiz")
      if action == "results":
        print("results")
      if action == "exit":
        pygame.quit()
        exit()
  else:
    pygame.draw.rect(gameDisplay, colori ,(x,y,w,h))
    #displaytext(txt, white, bigfont,(x+w/2), (y+h/2))
    textSurf, textRect = text_objects(txt, smallfont)
    textRect.center = ( (x + (w/2)), (y + (h/2)))
    gameDisplay.blit(textSurf, textRect)

def displaytext(text, color, z, x, y):
  text = z.render(text, True, color)
  gameDisplay.blit(text, (x, y))

def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

button("pee", 200, 600, 0, 0, white, black, "game")
#title loop
def titlescreen():
  titlescr = True 
  while titlescr:
    for event in pygame.event.get():
      print(event)
      if event.type == pygame.QUIT:
        pygame.quit()
        exit()
    gameDisplay.fill(white)
    gameDisplay.blit(titlescreen_background, (0,0))
    displaytext("Polyvasion", white, bigfont, 350, 500)
    displaytext("Shirdel Yan, Sihan Zeng", white, smallfont, 1000, 750)
    button("Play", 300, 100, 0, 0, white, black, "quiz")
    pygame.display.update()
titlescreen()