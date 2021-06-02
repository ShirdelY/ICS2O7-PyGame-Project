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
game_background = 
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
x_shape1 = 600
y_shape1 = 400
direction1_x = 1
direction1_y = 2
direction2_x = 3
direction2_y = 1
direction3_x = 7
direction3_y = 4
direction4_x = 2
direction4_y = 2
direction5_x = 1
direction5_y = 1

#functions
def button(txt, w, h, x, y, colora, colori, action):
  mousepos = pygame.mouse.get_pos() #current position of mouse
  click = pygame.mouse.get_pressed() #state of mouse button
  #check if mouse is on button
  global green
  global red
  global blue
  global white
  global black
  global quiz_score
  if x+w > mousepos[0] > x and y+h > mousepos[1] > y:
    pygame.draw.rect(gameDisplay, colora ,(x,y,w,h))
    #check left click state
    if click[0] == 1:
      if action == "game":
        playgame()
      if action == "tutorial":
        tutorial1()
      if action == "quiz":
        quiz1()
      if action == "results":
        display_result()
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
      if action == "goto_quiz2":
        quiz2()
      if action == "goto_quiz3":
        quiz3()
      if action == "goto_quiz4":
        quiz4()
      if action == "goto_quiz5":
        quiz5()
      if action == "question1":
        if txt == "(y + 15)(y - 15)":
          quiz_score += 1
          print(quiz_score)
          quiz1_exit()
        else:
          quiz1_exit()
      if action == "question2": 
        if txt == "(13 + b⁴)(13 - b⁴)":
          quiz_score += 1
          print(quiz_score)
          quiz2_exit()
        else:
          quiz2_exit()
      if action == "question3":
        if txt == "(9a + 4)²":
          quiz_score += 1
          print(quiz_score)
          quiz3_exit()
        else:
          quiz3_exit()
      if action == "question4":
        if txt == "(20x² - 16)²":
          quiz_score += 1
          print(quiz_score)
          quiz4_exit()
        else:
          quiz4_exit()
      if action == "question5":
        if txt == "(3p - 18)(p + 2)":
          quiz_score += 1
          print(quiz_score)
          quiz5_exit()
        else:
          quiz5_exit()
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
  global quiz_score
  quiz_score = 0 
  while question1:
    for event in pygame.event.get():
      print(event)
      if event.type == pygame.QUIT:
        pygame.quit()
        exit() 
    #create background
    gameDisplay.blit(quiz_background, (0, 0))
    #create buttons
    displaytext("Factor: 225 - y²", white, bigfont, 200, 350)
    button("(15 - y)²", 150, 150, 100, 600, grey, black, "question1")
    button("(y + 15)²", 150, 150, 300, 600, grey, black, "question1")
    button("(y + 15)(y + 15)", 150, 150, 500, 600, grey, black, "question1")
    button("(y + 15)(y - 15)", 150, 150, 700, 600, grey, black, "question1")
    button("Next", 300, 150, 900, 600, grey, black, "dummy")
    pygame.display.update()
    clock.tick(60)

def quiz1_exit():
  print("quiz1_exit")
  question1_exit = True
  while question1_exit:
    for event in pygame.event.get():
      print(event)
      if event.type == pygame.QUIT:
        pygame.quit()
        exit() 
    displaytext("Factor: 225 - y²", white, bigfont, 200, 350)
    button("(15 - y)²", 150, 150, 100, 600, red, red, "dummy")
    button("(y + 15)²", 150, 150, 300, 600, red, red, "dummy")
    button("(y + 15)(y + 15)", 150, 150, 500, 600, red, red, "dummy")
    button("(y + 15)(y - 15)", 150, 150, 700, 600, green, green, "dummy")
    button("Next", 300, 150, 900, 600, grey, black, "goto_quiz2")
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
    #create background
    gameDisplay.blit(quiz_background, (0, 0))
    #create buttons
    displaytext("Factor: 169 - b⁸", white, bigfont, 200, 350)
    button("(13 - b²)²", 150, 150, 100, 600, grey, black, "question2")
    button("(13 + b⁴)(13 - b⁴)", 150, 150, 300, 600, grey, black, "question2")
    button("(13 + b⁴)(13 + b⁴)", 150, 150, 500, 600, grey, black, "question2")
    button("(13 - b⁴)(13 - b⁴)", 150, 150, 700, 600, grey, black, "question2")
    button("Next", 300, 150, 900, 600, grey, black, "dummy")
    pygame.display.update()
    clock.tick(60)

def quiz2_exit():
  print("quiz2_exit")
  question2_exit = True
  while question2_exit:
    for event in pygame.event.get():
      print(event)
      if event.type == pygame.QUIT:
        pygame.quit()
        exit()
    #create buttons
    displaytext("Factor: 169 - b⁸", white, bigfont, 200, 350)
    button("(13 - b²)²", 150, 150, 100, 600, red, red, "dummy")
    button("(13 + b⁴)(13 - b⁴)", 150, 150, 300, 600, green, green, "dummy")
    button("(13 + b⁴)(13 + b⁴)", 150, 150, 500, 600, red, red, "dummy")
    button("(13 - b⁴)(13 - b⁴)", 150, 150, 700, 600, red, red, "dummy")
    button("Next", 300, 150, 900, 600, grey, black, "goto_quiz3")
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
    button("Next", 300, 150, 900, 600, grey, black, "dummy")
    pygame.display.update()
    clock.tick(60)

def quiz3_exit():
  print("quiz3_exit")
  question3_exit = True
  while question3_exit:
    for event in pygame.event.get():
      print(event)
      if event.type == pygame.QUIT:
        pygame.quit()
        exit()
    #create buttons
    displaytext("Factor: 81a² + 72a + 16", white, bigfont, 200, 350)
    button("(9a + 4)²", 150, 150, 100, 600, green, green, "dummy")
    button("(9a - 4)²", 150, 150, 300, 600, red, red, "dummy")
    button("(9a + 4)(9a - 4)", 150, 150, 500, 600, red, red, "dummy")
    button("(9a + 4)(9a - 4)", 150, 150, 700, 600, red, red, "dummy")
    button("Next", 300, 150, 900, 600, grey, black, "goto_quiz4")
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
    button("Next", 300, 150, 900, 600, grey, black, "dummy")
    pygame.display.update()
    clock.tick(60)

def quiz4_exit():
  print("quiz4_exit")
  question4_exit = True
  while question4_exit:
    for event in pygame.event.get():
      print(event)
      if event.type == pygame.QUIT:
        pygame.quit()
        exit()
    #create buttons
    displaytext("Factor: 400x⁴ - 640x² + 256", white, bigfont, 200, 350)
    button("(20x² + 16)²(20x² + 16)²", 150, 150, 100, 600, red, red, "dummy")
    button("(20x² + 16)²", 150, 150, 300, 600, red, red, "dummy")
    button("(20x² - 16)(20x² + 16)²", 150, 150, 500, 600, red, red, "dummy")
    button("(20x² - 16)²", 150, 150, 700, 600, green, green, "dummy")
    button("Next", 300, 150, 900, 600, grey, black, "goto_quiz5")
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
    button("Finish", 300, 150, 900, 600, grey, black, "dummy")
    pygame.display.update()
    clock.tick(60)

def quiz5_exit():
  print("quiz5_exit")
  question5_exit = True
  while question5_exit:
    for event in pygame.event.get():
      print(event)
      if event.type == pygame.QUIT:
        pygame.quit()
        exit()
    #create buttons
    displaytext("Fully Factor: 3p² - 12p - 36", white, bigfont, 200, 350)
    button("(3p - 18)(p - 2)", 150, 150, 100, 600, red, red, "dummy")
    button("(3p - 18)²", 150, 150, 300, 600, red, red, "dummy")
    button("(3p - 18)(p + 2)", 150, 150, 500, 600, green, green, "dummy")
    button("(3p + 18)²", 150, 150, 700, 600, red, red, "dummy")
    button("Finish", 300, 150, 900, 600, grey, black, "main menu")
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

def display_result():
  global quiz_score
  resultprint = "Your score is: " + str(quiz_score)
  result_screen = True
  while result_screen:
    for event in pygame.event.get():
      print(event)
      if event.type == pygame.QUIT:
        pygame.quit()
        exit()
    gameDisplay.fill(white)   
    displaytext(resultprint, black, bigfont, 600, 400)
    button("Return", 100, 50, 1100, 750, black, grey, "main menu")
    pygame.display.update()
    clock.tick(60)

def playgame():
  global direction1_x
  global direction1_y
  global x_shape1
  global y_shape1
  playing_game = True
  while playing_game:
    for event in pygame.event.get():
      print(event)
      if event.type == pygame.QUIT:
        pygame.quit()
        exit()
      mousepos = pygame.mouse.get_pos() #current position of mouse
      click = pygame.mouse.get_pressed() #state of mouse button
      x_shape1 += direction1_x #update the x position of the shape
      y_shape1 += direction1_y #update the y position of the shape
      #draw the shape
      gameDisplay.fill(white)
      pygame.draw.rect ((0, 255, 0), (x_shape1, y_shape1, 40, 40)) #need surface first argument
      display.update()
      clock.tick(60)



titlescreen()