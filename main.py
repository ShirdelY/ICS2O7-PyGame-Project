#***********************************************
#
# Program Author: Shirdel Yan, Sihan Zeng
# Revision Date: 26/5/2021
# Program Name: Polyvasion
# Description: ICS2O7 Pygame Project
#
#***********************************************

#import libraries
import pygame
import random
import time

#initialize pygame
pygame.init()
clock = pygame.time.Clock()

#define colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
grey = (69, 69, 69)

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
mainmenu_background = pygame.image.load("Assets/darkblue_background.png")
mainmenu_background = pygame.transform.scale(mainmenu_background, size)
quiz_background = pygame.image.load("Assets/classroom_background.png")
quiz_background = pygame.transform.scale(quiz_background, size)

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
        quiz()
      if action == "results":
        print("results")
      if action == "exit":
        pygame.quit()
        exit()
      if action == "main menu":
        main_menu()
      #quiz options
      if action == "question1":
        if txt == "(x+5)(x+6)":
          global green
          global quiz_score
          pygame.draw.rect(gameDisplay, green,(x,y,w,h))
          quiz_score += 1
          print("le poo au chocolat")
          pygame.display.flip()
        
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
    displaytext("Polyvasion", white, bigfont, 400, 300)
    displaytext("Shirdel Yan, Sihan Zeng", white, smallfont, 850, 750)
    button("Main Menu", 300, 100, 0, 0, grey, black, "main menu")
    pygame.display.update()
    clock.tick(60)

#def main menu
def main_menu():
  main_menu = True 
  while main_menu:
    for event in pygame.event.get():
      print(event)
      if event.type == pygame.QUIT:
        pygame.quit()
        exit()
    
    #create screen
    gameDisplay.blit(mainmenu_background, (0, 0))
    
    #create buttons
    button("Play", 150, 50, 0, 0, grey, black, "game")
    button("Tutorial", 150, 50, 0, 50, grey, black, "tutorial")
    button("Quiz", 150, 50, 0, 100, grey, black, "quiz")
    button("Results", 150, 50, 0, 150, grey, black, "results")
    button("Exit", 150, 50, 0, 200, grey, black, "exit")
    pygame.display.flip()
    clock.tick(60)

#quiz functions
def quiz(): 
  question1 = True
  question2 = True
  question3 = True
  question4 = True
  question5 = True
  while question1:
    for event in pygame.event.get():
      print(event)
      if event.type == pygame.QUIT:
        pygame.quit()
        exit() 
      quiz_score = 0
    mousepos = pygame.mouse.get_pos() #current position of mouse
    click = pygame.mouse.get_pressed() #state of mouse button
    #create background
    gameDisplay.blit(quiz_background, (0, 0))
    displaytext("Fully factor: x² + 11x + 30", black, bigfont, 0, 0)
    button("(x+5)(x+6)", 150, 150, 100, 100, grey, black, "question1")
    button("(x+6)(x+6)", 150, 150, 300, 100, grey, black, "question1")
    button("(x+5)(x+5)", 150, 150, 500, 100, grey, black, "question1")
    button("(x+5)(y+6)", 150, 150, 700, 100, grey, black, "question1")
    if click[0] == 1:
      break
    pygame.display.update()
    clock.tick(60)
  while question1:
    for event in pygame.event.get():
      print(event)
      if event.type == pygame.QUIT:
        pygame.quit()
        exit() 
      quiz_score = 0
    mousepos = pygame.mouse.get_pos() #current position of mouse
    click = pygame.mouse.get_pressed() #state of mouse button
    #create background
    gameDisplay.blit(quiz_background, (0, 0))
    displaytext("Fully factor: x² + 11x + 30", black, bigfont, 0, 0)
    button("(x+5)(x+6)", 150, 150, 100, 100, grey, black, "question2")
    button("(x+6)(x+6)", 150, 150, 300, 100, grey, black, "question2")
    button("(x+5)(x+5)", 150, 150, 500, 100, grey, black, "question2")
    button("(x+5)(y+6)", 150, 150, 700, 100, grey, black, "question2")
    if click[0] == 1:
      break
    pygame.display.update()
    clock.tick(60)
  while question1:
    for event in pygame.event.get():
      print(event)
      if event.type == pygame.QUIT:
        pygame.quit()
        exit() 
      quiz_score = 0
    mousepos = pygame.mouse.get_pos() #current position of mouse
    click = pygame.mouse.get_pressed() #state of mouse button
    #create background
    gameDisplay.blit(quiz_background, (0, 0))
    displaytext("Fully factor: x² + 11x + 30", black, bigfont, 0, 0)
    button("(x+5)(x+6)", 150, 150, 100, 100, grey, black, "question3")
    button("(x+6)(x+6)", 150, 150, 300, 100, grey, black, "question3")
    button("(x+5)(x+5)", 150, 150, 500, 100, grey, black, "question3")
    button("(x+5)(y+6)", 150, 150, 700, 100, grey, black, "question3")
    if click[0] == 1:
      break
    pygame.display.update()
    clock.tick(60)
  while question1:
    for event in pygame.event.get():
      print(event)
      if event.type == pygame.QUIT:
        pygame.quit()
        exit() 
      quiz_score = 0
    mousepos = pygame.mouse.get_pos() #current position of mouse
    click = pygame.mouse.get_pressed() #state of mouse button
    #create background
    gameDisplay.blit(quiz_background, (0, 0))
    displaytext("Fully factor: x² + 11x + 30", black, bigfont, 0, 0)
    button("(x+5)(x+6)", 150, 150, 100, 100, grey, black, "question4")
    button("(x+6)(x+6)", 150, 150, 300, 100, grey, black, "question4")
    button("(x+5)(x+5)", 150, 150, 500, 100, grey, black, "question4")
    button("(x+5)(y+6)", 150, 150, 700, 100, grey, black, "question4")
    if click[0] == 1:
      break
    pygame.display.update()
    clock.tick(60)
  while question1:
    for event in pygame.event.get():
      print(event)
      if event.type == pygame.QUIT:
        pygame.quit()
        exit() 
      quiz_score = 0
    mousepos = pygame.mouse.get_pos() #current position of mouse
    click = pygame.mouse.get_pressed() #state of mouse button
    #create background
    gameDisplay.blit(quiz_background, (0, 0))
    displaytext("Fully factor: x² + 11x + 30", black, bigfont, 0, 0)
    button("(x+5)(x+6)", 150, 150, 100, 100, grey, black, "question5")
    button("(x+6)(x+6)", 150, 150, 300, 100, grey, black, "question5")
    button("(x+5)(x+5)", 150, 150, 500, 100, grey, black, "question5")
    button("(x+5)(y+6)", 150, 150, 700, 100, grey, black, "question5")
    if click[0] == 1:
      break
    pygame.display.update()
    clock.tick(60)

titlescreen()