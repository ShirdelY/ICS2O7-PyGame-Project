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
tutorial1_background = pygame.image.load("Assets/factoringlesson1.png")
tutorial1_background = pygame.transform.scale(tutorial1_background, size)
tutorial2_background = pygame.image.load("Assets/factoringlesson2.png")
tutorial2_background = pygame.transform.scale(tutorial2_background, size)

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
  global green
  global quiz_score
  if x+w > mousepos[0] > x and y+h > mousepos[1] > y:
    pygame.draw.rect(gameDisplay, colora ,(x,y,w,h))
    #check left click state
    if click[0] == 1:
      if action == "game":
        print("game")
      if action == "tutorial":
        tutorial1()
      if action == "quiz":
        quiz1()
      if action == "results":
        print("results")
      if action == "exit":
        pygame.quit()
        exit()
      if action == "main menu":
        main_menu()
      if action == "continue_tutorial":
        tutorial2()
      if action == "finish_tutorial":
        main_menu()
      #quiz options
      if action == "question1":
        if txt == "(x+5)(x+6)":
          pygame.draw.rect(gameDisplay, green,(x,y,w,h))
          quiz_score += 1
          pygame.display.update()
          quiz2()
        else:
          pygame.draw.rect(gameDisplay, red,(x,y,w,h))
          pygame.display.update()
          quiz2()
      if action == "question2":
        if txt == "(13 + b⁴)(13 - b⁴)":
          pygame.draw.rect(gameDisplay, green,(x,y,w,h))
          quiz_score += 1
          pygame.display.update()
          quiz3()
        else:
          pygame.draw.rect(gameDisplay, red,(x,y,w,h))
          pygame.display.update()
          quiz3()
      if action == "question3":
        if txt == "(9a + 4)²":
          pygame.draw.rect(gameDisplay, green,(x,y,w,h))
          quiz_score += 1
          pygame.display.update()
          quiz4()
        else:
          pygame.draw.rect(gameDisplay, red,(x,y,w,h))
          pygame.display.update()
          quiz4()
      if action == "question4":
        if txt == "(20x² - 16)²":
          pygame.draw.rect(gameDisplay, green,(x,y,w,h))
          quiz_score += 1
          pygame.display.update()
          quiz5()
        else:
          pygame.draw.rect(gameDisplay, red,(x,y,w,h))
          pygame.display.update()
          quiz5()
      if action == "question5":
        if txt == "(3p - 18)(p + 2)":
          pygame.draw.rect(gameDisplay, green,(x,y,w,h))
          quiz_score += 1
          pygame.display.update()
          main_menu()
        else:
          pygame.draw.rect(gameDisplay, red,(x,y,w,h))
          pygame.display.update()
          main_menu()
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
def quiz1(): 
  question1 = True
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
    #create buttons
    displaytext("Factor: 225 - y²", white, bigfont, 200, 350)
    button("(15 - y)²", 150, 150, 100, 600, grey, black, "question1")
    button("(y + 15)²", 150, 150, 300, 600, grey, black, "question1")
    button("(y + 15)(y + 15)", 150, 150, 500, 600, grey, black, "question1")
    button("(y + 15)(y - 15)", 150, 150, 700, 600, grey, black, "question1")
    pygame.display.update()
    clock.tick(60)
def quiz2(): 
  question2 = True
  while question2:
    for event in pygame.event.get():
      print(event)
      if event.type == pygame.QUIT:
        pygame.quit()
        exit() 
    mousepos = pygame.mouse.get_pos() #current position of mouse
    click = pygame.mouse.get_pressed() #state of mouse button
    #create background
    gameDisplay.blit(quiz_background, (0, 0))
    #create buttons
    displaytext(" Factor: 169 - b⁸", white, bigfont, 200, 350)
    button("(13 - b²)²", 150, 150, 100, 600, grey, black, "question2")
    button("(13 + b⁴)(13 - b⁴)", 150, 150, 300, 600, grey, black, "question2")
    button("(13 + b⁴)(13 + b⁴)", 150, 150, 500, 600, grey, black, "question2")
    button("(13 - b⁴)(13 - b⁴)", 150, 150, 700, 600, grey, black, "question2")
    pygame.display.update()
    clock.tick(60)
def quiz3(): 
  question3 = True
  while question3:
    for event in pygame.event.get():
      print(event)
      if event.type == pygame.QUIT:
        pygame.quit()
        exit() 
    mousepos = pygame.mouse.get_pos() #current position of mouse
    click = pygame.mouse.get_pressed() #state of mouse button
    #create background
    gameDisplay.blit(quiz_background, (0, 0))
    #create buttons
    displaytext("Factor: 81a² + 72a + 16", white, bigfont, 200, 350)
    button("(9a + 4)²", 150, 150, 100, 600, grey, black, "question3")
    button("(9a - 4)²", 150, 150, 300, 600, grey, black, "question3")
    button("(9a + 4)(9a - 4)", 150, 150, 500, 600, grey, black, "question3")
    button("(9a + 4)(9a - 4)", 150, 150, 700, 600, grey, black, "question3")
    pygame.display.update()
    clock.tick(60)
def quiz4(): 
  question4 = True
  while question4:
    for event in pygame.event.get():
      print(event)
      if event.type == pygame.QUIT:
        pygame.quit()
        exit() 
    mousepos = pygame.mouse.get_pos() #current position of mouse
    click = pygame.mouse.get_pressed() #state of mouse button
    #create background
    gameDisplay.blit(quiz_background, (0, 0))
    #create buttons
    displaytext("Factor: 400x⁴ - 640x² + 256", white, bigfont, 200, 350)
    button("(20x² + 16)²(20x² + 16)²", 150, 150, 100, 600, grey, black, "question4")
    button("(20x² + 16)²", 150, 150, 300, 600, grey, black, "question4")
    button("(20x² - 16)(20x² + 16)²", 150, 150, 500, 600, grey, black, "question4")
    button("(20x² - 16)²", 150, 150, 700, 600, grey, black, "question4")
    pygame.display.update()
    clock.tick(60)
def quiz5(): 
  question5 = True
  while question5:
    for event in pygame.event.get():
      print(event)
      if event.type == pygame.QUIT:
        pygame.quit()
        exit() 
    mousepos = pygame.mouse.get_pos() #current position of mouse
    click = pygame.mouse.get_pressed() #state of mouse button
    #create background
    gameDisplay.blit(quiz_background, (0, 0))
    #create buttons
    displaytext("Fully Factor: 3p² - 12p - 36", white, bigfont, 200, 350)
    button("(3p - 18)(p - 2)", 150, 150, 100, 600, grey, black, "question5")
    button("(3p - 18)²", 150, 150, 300, 600, grey, black, "question5")
    button("(3p - 18)(p + 2)", 150, 150, 500, 600, grey, black, "question5")
    button("(3p + 18)²", 150, 150, 700, 600, grey, black, "question5")
    pygame.display.update()
    clock.tick(60)

#def tutorial
def tutorial1():
  page1 = True
  while page1:
    for event in pygame.event.get():
      print(event)
      if event.type == pygame.QUIT:
        pygame.quit()
        exit()
      mousepos = pygame.mouse.get_pos() #current position of mouse
      click = pygame.mouse.get_pressed() #state of mouse button
      #create tutorial document
      gameDisplay.blit(tutorial1_background, (0, 0))
      #create continue button
      button("Continue", 100, 50, 1100, 750, black, grey, "continue_tutorial")
      pygame.display.flip()
      clock.tick(60)
#page 2 tutorial function
def tutorial2():
  page2 = True
  while page2:
    for event in pygame.event.get():
      print(event)
      if event.type == pygame.QUIT:
        pygame.quit()
        exit()
      mousepos = pygame.mouse.get_pos() #current position of mouse
      click = pygame.mouse.get_pressed() #state of mouse button
      #create tutorial document
      gameDisplay.blit(tutorial2_background, (0, 0))
      #create continue function
      button("Finish", 100, 50, 1100, 750, black, grey, "finish_tutorial")
      pygame.display.update()
      clock.tick(60)
titlescreen()