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
from pygame import mixer
import time
from datetime import date

#initialize pygame
pygame.init()
mixer.init()
clock = pygame.time.Clock()

#define colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
grey = (69, 69, 69)
pink = (255, 77, 190)
purple = (153, 51, 255)
yellow = (255, 255, 51)
cyan = (0, 255, 255)
orange = (255, 128, 0)

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
gametutorial_background = pygame.image.load("Assets/gametutorial.png")
gametutorial_background = pygame.transform.scale(gametutorial_background, size)
level1completion_background = pygame.image.load("Assets/level1completion.png")
level1completion_background = pygame.transform.scale(level1completion_background, size)
level2completion_background = pygame.image.load("Assets/level2completion.png")
level2completion_background = pygame.transform.scale(level2completion_background, size)
level3completion_background = pygame.image.load("Assets/level3completion.png")
level3completion_background = pygame.transform.scale(level3completion_background, size)
level4completion_background = pygame.image.load("Assets/level4completion.png")
level4completion_background = pygame.transform.scale(level4completion_background, size)
level5completion_background = pygame.image.load("Assets/level5completion.png")
level5completion_background = pygame.transform.scale(level5completion_background, size)
level6completion_background = pygame.image.load("Assets/level6completion.png")
level6completion_background = pygame.transform.scale(level6completion_background, size)
level7completion_background = pygame.image.load("Assets/level7completion.png")
level7completion_background = pygame.transform.scale(level7completion_background, size)
goldencirclewarning_background = pygame.image.load("Assets/goldencirclewarning.png")
goldencirclewarning_background = pygame.transform.scale(goldencirclewarning_background, size)
level8completion_background = pygame.image.load("Assets/level8completion.png")
level8completion_background = pygame.transform.scale(level8completion_background, size)
level9completion_background = pygame.image.load("Assets/level9completion.png")
level9completion_background = pygame.transform.scale(level9completion_background, size)
level10completion_background = pygame.image.load("Assets/level10completion.png")
level10completion_background = pygame.transform.scale(level10completion_background, size)
quiz_background = pygame.image.load("Assets/classroom_background.png")
quiz_background = pygame.transform.scale(quiz_background, size)
results_background = titlescreen_background
tutorial1_background = pygame.image.load("Assets/factoringlesson1.png")
tutorial1_background = pygame.transform.scale(tutorial1_background, size)
tutorial2_background = pygame.image.load("Assets/factoringlesson2.png")
tutorial2_background = pygame.transform.scale(tutorial2_background, size)

#initialize the fonts
bigfont = pygame.font.SysFont("arial",50)
smallfont = pygame.font.SysFont("arial",15)

#declare variables
previous_mouse_state = 1
quiz_score = 0
game_score = 0
today = str(date.today())
highscore = 0

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
      #check what action the button executes
      if action == "game":
        teachgame()
      if action == "mute":
        mixer.music.pause()
      if action == "startmusic":
        mixer.music.unpause()
      if action == "startgame":
        playlevel1()
      if action == "startlevel2":
        playlevel2()
      if action == "startlevel3":
        playlevel3()
      if action == "startlevel4":
        playlevel4()
      if action == "startlevel5":
        playlevel5()
      if action == "startlevel6":
        playlevel6()
      if action == "showgoldencircle":
        pygame.time.delay(100)
        showgoldencircle()
      if action == "startlevel7":
        playlevel7()
      if action == "startlevel8":
        playlevel8()
      if action == "startlevel9":
        playlevel9()
      if action == "startlevel10":
        playlevel10()
      if action == "endgame":
        pygame.time.delay(100)
        displayfinalscore()
      if action == "return":
        main_menu()
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
        pygame.time.delay(100)
        main_menu()
      if action == "continue_tutorial":
        tutorial2()
      if action == "finish_tutorial":
        pygame.time.delay(100)
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
      if action == "credits":
        pygame.time.delay(100)
        credits()
      else:
        quiz5_exit()
  else:
    #make the rectangle for the button
    pygame.draw.rect(gameDisplay, colori ,(x,y,w,h))
  #display the text
  textSurf, textRect = text_objects(txt, smallfont)
  textRect.center = ((x + (w/2)), (y + (h/2)))
  gameDisplay.blit(textSurf, textRect)

#display text function
def displaytext(text, color, z, x, y):
  text = z.render(text, True, color)
  gameDisplay.blit(text, (x, y))

#text objects function
def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

#title loop
def titlescreen():
  titlescr = True 
  while titlescr:
    #check if pygame is quitting
    for event in pygame.event.get():
      print(event)
      if event.type == pygame.QUIT:
        pygame.quit()
        exit()
    #display the title background
    gameDisplay.blit(titlescreen_background, (0,0))
    #show text
    displaytext("Polyvasion", yellow, bigfont, 500, 100)
    displaytext("Shirdel Yan, Sihan Zeng", purple, smallfont, 550, 750)
    displaytext(today, red, smallfont, 587.5, 250)
    displaytext("ICS2O7, Ms. Xie", blue, smallfont, 575, 200)
    #make main menu button
    button("Main Menu", 300, 100, 475, 400, grey, black, "main menu")
    pygame.display.update()
    clock.tick(60)

#def main menu
def main_menu():
  main_menu = True
  playing_music = True
  mixer.music.load("Assets/gamemusic.wav")
  mixer.music.set_volume(0.4)
  mixer.music.play(-1)
  while main_menu:
    #check if pygame is quitting
    for event in pygame.event.get():
      print(event)
      if event.type == pygame.QUIT:
        pygame.quit()
        exit()
    #create screen
    gameDisplay.blit(mainmenu_background, (0, 0))
    #create buttons
    button("Play", 300, 100, 450, 50, grey, black, "game")
    button("Tutorial", 300, 100, 450, 200, grey, black, "tutorial")
    button("Quiz", 300, 100, 450, 350, grey, black, "quiz")
    button("Results", 300, 100, 450, 500, grey, black, "results")
    button("Exit", 300, 100, 450, 650, grey, black, "exit")
    button("Mute", 50, 50, 0, 0, grey, black, "mute")
    button("Start Music", 100, 50, 1100, 0, grey, black, "startmusic")
    button("Credits", 150, 50, 1050, 750, grey, black, "credits")
    pygame.display.flip()
    clock.tick(60)

#quiz functions
def quiz1(): 
  question1 = True
  #import variables
  global quiz_score
  #reset quiz score to prevent point farming
  quiz_score = 0 
  while question1:
    #check if pygame is quitting
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
    #make placeholder next question button
    button("Next", 300, 150, 900, 600, grey, black, "dummy")
    pygame.display.update()
    clock.tick(60)

def quiz1_exit():
  #trouble shooting thing
  print("quiz1_exit")
  question1_exit = True
  while question1_exit:
    #check if pygame is quitting
    for event in pygame.event.get():
      print(event)
      if event.type == pygame.QUIT:
        pygame.quit()
        exit() 
    #display the question
    displaytext("Factor: 225 - y²", white, bigfont, 200, 350)
    #show dummy buttons in place of the quiz buttons
    button("(15 - y)²", 150, 150, 100, 600, red, red, "dummy")
    button("(y + 15)²", 150, 150, 300, 600, red, red, "dummy")
    button("(y + 15)(y + 15)", 150, 150, 500, 600, red, red, "dummy")
    button("(y + 15)(y - 15)", 150, 150, 700, 600, green, green, "dummy")
    #make functional next questions button
    button("Next", 300, 150, 900, 600, grey, black, "goto_quiz2")
    pygame.display.update()
    clock.tick(60)

def quiz2(): 
  question2 = True
  while question2:
    #check if pygame is quitting
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
    #make placeholder next question button
    button("Next", 300, 150, 900, 600, grey, black, "dummy")
    pygame.display.update()
    clock.tick(60)

def quiz2_exit():
  print("quiz2_exit")
  question2_exit = True
  while question2_exit:
    #check if pygame is quitting
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
    #make functional next question button
    button("Next", 300, 150, 900, 600, grey, black, "goto_quiz3")
    pygame.display.update()
    clock.tick(60)

def quiz3(): 
  question3 = True
  while question3:
    #check if pygame is quitting
    for event in pygame.event.get():
      print(event)
      if event.type == pygame.QUIT:
        pygame.quit()
        exit() 
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
    #make fucntional next question button
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
    #create background
    gameDisplay.blit(quiz_background, (0, 0))
    #create buttons
    displaytext("Factor: 400x⁴ - 640x² + 256", white, bigfont, 200, 350)
    button("(20x² + 16)²(20x² + 16)²", 150, 150, 100, 600, grey, black, "question4")
    button("(20x² + 16)²", 150, 150, 300, 600, grey, black, "question4")
    button("(20x² - 16)(20x² + 16)²", 150, 150, 500, 600, grey, black, "question4")
    button("(20x² - 16)²", 150, 150, 700, 600, grey, black, "question4")
    #create placeholder next question button
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
    #create functional next question button
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
    #create background
    gameDisplay.blit(quiz_background, (0, 0))
    #create buttons
    displaytext("Fully Factor: 3p² - 12p - 36", white, bigfont, 200, 350)
    button("(3p - 18)(p - 2)", 150, 150, 100, 600, grey, black, "question5")
    button("(3p - 18)²", 150, 150, 300, 600, grey, black, "question5")
    button("(3p - 18)(p + 2)", 150, 150, 500, 600, grey, black, "question5")
    button("(3p + 18)²", 150, 150, 700, 600, grey, black, "question5")
    #create place holder main menu button
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
    #make functional main menu button
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
      #create tutorial document
      gameDisplay.blit(tutorial2_background, (0, 0))
      #create continue function
      button("Finish", 100, 50, 1100, 750, black, grey, "finish_tutorial")
      pygame.display.update()
      clock.tick(60)

#result function
def display_result():
  #get quiz score
  global quiz_score
  #calculate the percentage and process the message
  percentage_score = float((quiz_score/5)*100)
  message0 = "Please return to the lesson to learn about factoring"
  message1 = "Please return to the lesson to learn more about factoring"
  message2 = "Not bad, but please try to reinforce your knowledge about factoring"
  message3 = "Good job, you could consider retaking the quiz again"
  message4 = "Amazing job!"
  message5 = "Perfect score! You are an extraordinary learner!"
  #make the string
  result_screen = True
  while result_screen:
    for event in pygame.event.get():
      print(event)
      if event.type == pygame.QUIT:
        pygame.quit()
        exit()
        #make background white
    gameDisplay.blit(results_background, (0, 0))  
    #show the score
    displaytext("Total Score: " + str(quiz_score), white, bigfont, 450, 150)
    displaytext("You got " + str(percentage_score) + "%", white, bigfont, 450, 300)
    #display the message depending on the score
    if quiz_score == 0:
      displaytext(message0, white, smallfont, 437.5, 450)
    elif quiz_score == 1:
      displaytext(message1, white, smallfont, 437.5, 450)
    elif quiz_score == 2:
      displaytext(message2, white, smallfont, 400, 450)
    elif quiz_score == 3:
      displaytext(message3, white, smallfont, 437.5, 450)
    elif quiz_score == 4:
      displaytext(message4, white, smallfont, 562.5, 450)
    else:
      displaytext(message5, white, smallfont, 462.5, 450)

    #make the main menu button
    button("Return", 100, 50, 1100, 750, black, grey, "main menu")
    pygame.display.update()
    clock.tick(60)

#credits fucntion
def credits():
  showingcredits = True 
  while showingcredits:
    for event in pygame.event.get():
      print(event)
      if event.type == pygame.QUIT:
        pygame.quit()
        exit()
    pygame.draw.rect(gameDisplay, grey, (0, 0, 1200, 80))
    displaytext("-Progammers-", black, bigfont, 462.5, 200)
    displaytext("Shirdel Yan", black, bigfont, 462.5, 300)
    displaytext("Sihan Zeng", black, bigfont, 462.5, 400)  
    displaytext("-Music Used-", black, bigfont, 462.5, 400)  
    displaytext("Menu Screen by Jonny Easton", black, bigfont, 462.5, 400)  
    button("Return", 100, 50, 1100, 750, black, grey, "main menu")

#game tutorial function
def teachgame():
  global game_music
  teaching_game = True
  playing_music = True
  while teaching_game:
    for event in pygame.event.get():
      print(event)
      if event.type == pygame.QUIT:
        pygame.quit()
        exit()
    #display the game tutorial
    gameDisplay.blit(gametutorial_background, (0, 0))
    #make the start button
    button("Start", 100, 50, 1100, 750, black, grey, "startgame")
    pygame.display.update()
    clock.tick(60)
   
#play game function
def playlevel1():
  #import and declare variables
  global grey
  global blue
  global x
  global y
  colour1 = blue
  global game_score
  global red
  global white
  game_score = 0
  #set playing game state
  playing_game1 = True
  #generate starting coordinates for shapes
  x_shape1 = random.randint(50,1150)
  y_shape1 = random.randint(50,750)
  x_shape2 = random.randint(0,1100)
  y_shape2 = random.randint(0,750)
  #generate velocities for shapes
  direction1_x = random.randint(1, 5)
  direction1_y = random.randint(1, 5)
  direction2_x = random.randint(1, 7)
  direction2_y = random.randint(1, 7)
  #game loop
  while playing_game1:
    #check if pygame is exiting
    for event in pygame.event.get():
      print(event)
      if event.type == pygame.QUIT:
        pygame.quit()
        exit()
    #get mouse position
    mousepos = pygame.mouse.get_pos() #current position of mouse
    #update coordinates for shapes
    x_shape1 += direction1_x #update the x position of shape 1
    y_shape1 += direction1_y #update the y position of shape 1
    x_shape2 += direction2_x #update the x position of shape 2
    y_shape2 += direction2_y #update the y position of shape 2
    #check if shapes are at the boundaries of the viewport and make them bounce
    if x_shape1 >= 1150 or x_shape1 <= 50:
      direction1_x *= -1
    if y_shape1 >= 750 or y_shape1 <= 50:
      direction1_y *= -1
    if x_shape2 >= 1100 or x_shape2 <= 0:
      direction2_x *= -1
    if y_shape2 >= 750 or y_shape2 <= 0:
      direction2_y *= -1
    #draw the shape
    pygame.draw.rect(gameDisplay, grey, (0, 0, x, y))
    pygame.draw.circle(gameDisplay, colour1, (x_shape1, y_shape1), 50)
    pygame.draw.rect(gameDisplay, red, (x_shape2, y_shape2, 100, 50))
    #check if all shapes have been clicked
    if colour1 == white:
      displaytext(("Score: " + str(game_score)), blue, bigfont, 0, 0)
      pygame.display.update()
      pygame.time.delay(1000)
      finishlevel1()
    #check if the shape has been clicked on
    if mousepos[0] > x_shape1 - 50 and mousepos[0] < x_shape1 + 50 and mousepos[1] > y_shape1 - 50 and mousepos[1] < y_shape1 + 50:
      #check if mouse button has just gone down so that it doesnt deduct points every cycle
      if event.type == pygame.MOUSEBUTTONDOWN:
        #make sure the shape hasnt already been clicked
        if colour1 != white:
          colour1 = white
          #slow down shape
          direction1_x = 0.5
          direction1_y = 0.5
          pygame.display.update()
          game_score += 1
    #check if the shape has been clicked on
    if mousepos[0] > x_shape2 - 50 and mousepos[0] < x_shape2 + 50 and mousepos[1] > y_shape2 - 50 and mousepos[1] < y_shape2 + 50:
      #check if mouse button has just gone down so that it doesnt deduct points every cycle
      if event.type == pygame.MOUSEBUTTONDOWN:
        #make sure it doesnt put out a negative score
        if game_score >= 3:
          game_score -= 3
        else:
          game_score = 0
    #display the score
    displaytext(("Score: " + str(game_score)), blue, bigfont, 0, 0)
    pygame.display.update()
    clock.tick(60)

def finishlevel1():
  finish1 = True
  while finish1:
    #see if pygame is quitting
    for event in pygame.event.get():
      print(event)
      if event.type == pygame.QUIT:
        pygame.quit()
        exit()
    #show completion screen
    gameDisplay.blit(level1completion_background, (0, 0))
    #make continue button
    button("Continue", 100, 50, 1100, 750, black, grey, "startlevel2")
    pygame.display.update()
    clock.tick(60)

def playlevel2():
  #import and declare variables
  global grey
  global blue
  global green
  global x
  global y
  colour1 = blue
  colour2 = green
  global game_score
  global red
  global white
  #set playing game state
  playing_game2 = True
  #generate starting coordinates for shapes
  x_shape1 = random.randint(50,1150)
  y_shape1 = random.randint(50,750)
  x_shape2 = random.randint(0,1100)
  y_shape2 = random.randint(0,750)
  x_shape3 = random.randint(50, 1150)
  y_shape3 = random.randint(50, 750)
  #generate velocities for shapes
  direction1_x = random.randint(1, 5)
  direction1_y = random.randint(1, 5)
  direction2_x = random.randint(1, 7)
  direction2_y = random.randint(1, 7)
  direction3_x = random.randint(1, 7)
  direction3_y = random.randint(1, 3)
  while playing_game2:
    for event in pygame.event.get():
      print(event)
      if event.type == pygame.QUIT:
        pygame.quit()
        exit()
        #check if all shapes have been clicked on
    if colour1 == white and colour2 == white:
      displaytext(("Score: " + str(game_score)), blue, bigfont, 0, 0)
      pygame.draw.circle(gameDisplay, white, (x_shape1, y_shape1), 50)
      pygame.draw.circle(gameDisplay, white, (x_shape3, y_shape3), 50)
      pygame.display.update()
      pygame.time.delay(1000)
      finishlevel2()
    mousepos = pygame.mouse.get_pos() #current position of mouse
    x_shape1 += direction1_x #update the x position of shape 1
    y_shape1 += direction1_y #update the y position of shape 1
    x_shape2 += direction2_x #update the x position of shape 2
    y_shape2 += direction2_y #update the y position of shape 2
    x_shape3 += direction3_x #update the x position of shape 3
    y_shape3 += direction3_y #update the y position of shape 3
    #make the shapes bounce
    if x_shape1 >= 1150 or x_shape1 <= 50:
      direction1_x *= -1
    if y_shape1 >= 750 or y_shape1 <= 50:
      direction1_y *= -1
    if x_shape2 >= 1100 or x_shape2 <= 0:
      direction2_x *= -1
    if y_shape2 >= 750 or y_shape2 <= 0:
      direction2_y *= -1
    if x_shape3 >= 1150 or x_shape3 <= 50:
      direction3_x *= -1
    if y_shape3 >= 750 or y_shape3 <= 50:
      direction3_y *= -1
    #draw the shape
    pygame.draw.rect(gameDisplay, grey, (0, 0, x, y))
    pygame.draw.circle(gameDisplay, colour1, (x_shape1, y_shape1), 50)
    pygame.draw.rect(gameDisplay, red, (x_shape2, y_shape2, 100, 50))
    pygame.draw.circle(gameDisplay, colour2, (x_shape3, y_shape3), 50)
    #check if the shape has been clicked on
    if mousepos[0] > x_shape1 - 50 and mousepos[0] < x_shape1 + 50 and mousepos[1] > y_shape1 - 50 and mousepos[1] < y_shape1 + 50:
      if event.type == pygame.MOUSEBUTTONDOWN:
        #make sure the shape hasnt been clicked on previously
        if colour1 != white:
          colour1 = white
          direction1_x = 0.5
          direction1_y = 0.5
          game_score += 1
          pygame.display.update()
    if mousepos[0] > x_shape2 - 50 and mousepos[0] < x_shape2 + 50 and mousepos[1] > y_shape2 - 50 and mousepos[1] < y_shape2 + 50:
      if event.type == pygame.MOUSEBUTTONDOWN:
        if game_score >= 3:
          game_score -= 3
        else:
          game_score = 0
    if mousepos[0] > x_shape3 - 50 and mousepos[0] < x_shape3 + 50 and mousepos[1] > y_shape3 - 50 and mousepos[1] < y_shape3 + 50:
      if event.type == pygame.MOUSEBUTTONDOWN:
        #make suire the shape hasnt already been clicked on
        if colour2 != white:
          #slow down the shape and make it turn white
          colour2 = white
          direction3_x = 0.5
          direction3_y = 0.5
          game_score += 3
          pygame.display.update()
    #show the score
    displaytext(("Score: " + str(game_score)), blue, bigfont, 0, 0)
    pygame.display.update()
    clock.tick(60)

def finishlevel2():
  finish2 = True
  while finish2:
    for event in pygame.event.get():
      print(event)
      if event.type == pygame.QUIT:
        pygame.quit()
        exit()
    #show teh level completion background
    gameDisplay.blit(level2completion_background, (0, 0))
    #make next level button
    button("Continue", 100, 50, 1100, 750, black, grey, "startlevel3")
    pygame.display.update()
    clock.tick(60)
    
def playlevel3():
  #import and declare variables
  global grey
  global blue
  global green
  global x
  global y
  global pink
  colour1 = blue
  colour2 = green
  colour3 = pink
  global game_score
  global red
  global white
  playing_game3 = True
  #make starting positions for shapes
  x_shape1 = random.randint(50,1150)
  y_shape1 = random.randint(50,750)
  x_shape2 = random.randint(0,1100)
  y_shape2 = random.randint(0,750)
  x_shape3 = random.randint(50, 1150)
  y_shape3 = random.randint(50, 750)
  x_shape4 = random.randint(0,1100)
  y_shape4 = random.randint(0,750)
  x_shape5 = random.randint(50, 1150)
  y_shape5 = random.randint(50,750)
  #generate shape velocities
  direction1_x = random.randint(1, 5)
  direction1_y = random.randint(1, 5)
  direction2_x = random.randint(1, 7)
  direction2_y = random.randint(1, 7)
  direction3_x = random.randint(1, 7)
  direction3_y = random.randint(1, 3)
  direction4_x = random.randint(1, 9)
  direction4_y = random.randint(1, 9)
  direction5_x = random.randint(5, 13)
  direction5_y = random.randint(5, 13)
  while playing_game3:
    for event in pygame.event.get():
      print(event)
      if event.type == pygame.QUIT:
        pygame.quit()
        exit()
    #check if all shapes havent been clicked
    if colour1 == white and colour2 == white and colour3 == white:
      displaytext(("Score: " + str(game_score)), blue, bigfont, 0, 0)
      pygame.draw.circle(gameDisplay, white, (x_shape1, y_shape1), 50)
      pygame.draw.circle(gameDisplay, white, (x_shape3, y_shape3), 50)
      pygame.draw.circle(gameDisplay, white, (x_shape5, y_shape5), 50)
      pygame.display.update()
      pygame.time.delay(1000)
      finishlevel3()
    mousepos = pygame.mouse.get_pos() #current position of mouse
    x_shape1 += direction1_x #update the x position of shape 1
    y_shape1 += direction1_y #update the y position of shape 1
    x_shape2 += direction2_x #update the x position of shape 2
    y_shape2 += direction2_y #update the y position of shape 2
    x_shape3 += direction3_x #update the x position of shape 3
    y_shape3 += direction3_y #update the y position of shape 3
    x_shape4 += direction4_x #update the x position of shape 4
    y_shape4 += direction4_y #update the y position of shape 4
    x_shape5 += direction5_x #update the x position of shape 5
    y_shape5 += direction5_y #update the y position of shape 5
    #make the shapes bounce
    if x_shape1 >= 1150 or x_shape1 <= 50:
      direction1_x *= -1
    if y_shape1 >= 750 or y_shape1 <= 50:
      direction1_y *= -1
    if x_shape2 >= 1100 or x_shape2 <= 0:
      direction2_x *= -1
    if y_shape2 >= 750 or y_shape2 <= 0:
      direction2_y *= -1
    if x_shape3 >= 1150 or x_shape3 <= 50:
      direction3_x *= -1
    if y_shape3 >= 750 or y_shape3 <= 50:
      direction3_y *= -1
    if x_shape4 >= 1100 or x_shape4 <= 0:
      direction4_x *= -1
    if y_shape4 >= 750 or y_shape4 <= 0:
      direction4_y *= -1
    if x_shape5 >= 1150 or x_shape5 <= 50:
      direction5_x *= -1
    if y_shape5 >= 750 or y_shape5 <= 50:
      direction5_y *= -1
    #draw the shape
    pygame.draw.rect(gameDisplay, grey, (0, 0, x, y))
    pygame.draw.circle(gameDisplay, colour1, (x_shape1, y_shape1), 50)
    pygame.draw.rect(gameDisplay, red, (x_shape2, y_shape2, 100, 50))
    pygame.draw.circle(gameDisplay, colour2, (x_shape3, y_shape3), 50)
    pygame.draw.rect(gameDisplay, red, (x_shape4, y_shape4, 100, 50))
    pygame.draw.circle(gameDisplay, colour3, (x_shape5, y_shape5), 50)
    #check if the shape has been clicked on
    if mousepos[0] > x_shape1 - 50 and mousepos[0] < x_shape1 + 50 and mousepos[1] > y_shape1 - 50 and mousepos[1] < y_shape1 + 50:
      if event.type == pygame.MOUSEBUTTONDOWN:
        #make sure shape hasnt been previously clicked on
        if colour1 != white:
          colour1 = white
          #slow down teh shape
          direction1_x = 0.5
          direction1_y = 0.5
          game_score += 1
          pygame.display.update()
    if mousepos[0] > x_shape2 - 50 and mousepos[0] < x_shape2 + 50 and mousepos[1] > y_shape2 - 50 and mousepos[1] < y_shape2 + 50:
      #make sure the mouse button ws pressed down recentl;y to avoid deducting points on every cycle rapidly
      if event.type == pygame.MOUSEBUTTONDOWN:
        if game_score >= 3:
          game_score -= 3
        else:
          game_score = 0
    if mousepos[0] > x_shape4 - 50 and mousepos[0] < x_shape4 + 50 and mousepos[1] > y_shape4 - 50 and mousepos[1] < y_shape4 + 50:
      if event.type == pygame.MOUSEBUTTONDOWN:
        #make sure the score doesnt become negative
        if game_score >= 3:
          game_score -= 3
        else:
          game_score = 0
    if mousepos[0] > x_shape3 - 50 and mousepos[0] < x_shape3 + 50 and mousepos[1] > y_shape3 - 50 and mousepos[1] < y_shape3 + 50:
      if event.type == pygame.MOUSEBUTTONDOWN:
        #make sure shape hasnt been previously clicked on
        if colour2 != white:
          colour2 = white
          direction3_x = 0.5
          direction3_y = 0.5
          game_score += 3
          pygame.display.update()
    if mousepos[0] > x_shape5 - 50 and mousepos[0] < x_shape5 + 50 and mousepos[1] > y_shape5 - 50 and mousepos[1] < y_shape5 + 50:
      if event.type == pygame.MOUSEBUTTONDOWN:
        #make sure shape hasnt been previously clicked on
        if colour3 != white:
          colour3 = white
          #slow down shape
          direction5_x = 0.5
          direction5_y = 0.5
          game_score += 10
          pygame.display.update()
    #display score
    displaytext(("Score: " + str(game_score)), blue, bigfont, 0, 0)
    pygame.display.update()
    clock.tick(60)

def finishlevel3():
  finish3 = True
  while finish3:
    for event in pygame.event.get():
      print(event)
      if event.type == pygame.QUIT:
        pygame.quit()
        exit()
    #show finish screen
    gameDisplay.blit(level3completion_background, (0, 0))
    #make next level button
    button("Continue", 100, 50, 1100, 750, black, grey, "startlevel4")
    pygame.display.update()
    clock.tick(60)

def playlevel4():
  #import and declare variables
  global grey
  global blue
  global green
  global x
  global y
  global pink
  colour1 = blue
  colour2 = green
  colour3 = pink
  global game_score
  global red
  global white
  playing_game4 = True
  #generate starting positions
  x_shape1 = random.randint(50,1150)
  y_shape1 = random.randint(50,750)
  x_shape2 = random.randint(0,1100)
  y_shape2 = random.randint(0,750)
  x_shape3 = random.randint(50, 1150)
  y_shape3 = random.randint(50, 750)
  x_shape4 = random.randint(0,1100)
  y_shape4 = random.randint(0,750)
  x_shape5 = random.randint(50, 1150)
  y_shape5 = random.randint(50,750)
  x_shape6 = random.randint(0,1100)
  y_shape6 = random.randint(0,750)
  x_shape7 = random.randint(0,1100)
  y_shape7 = random.randint(0,750)
  #generate velocities
  direction1_x = random.randint(1, 5)
  direction1_y = random.randint(1, 5)
  direction2_x = random.randint(1, 7)
  direction2_y = random.randint(1, 7)
  direction3_x = random.randint(1, 7)
  direction3_y = random.randint(1, 3)
  direction4_x = random.randint(1, 9)
  direction4_y = random.randint(1, 9)
  direction5_x = random.randint(5, 13)
  direction5_y = random.randint(5, 13)
  direction6_x = random.randint(1, 11)
  direction6_y = random.randint(1, 11)
  direction7_x = random.randint(1, 11)
  direction7_y = random.randint(1, 11)
  while playing_game4:
    for event in pygame.event.get():
      print(event)
      if event.type == pygame.QUIT:
        pygame.quit()
        exit()
    #make sure all shapes have been clicked before exiting
    if colour1 == white and colour2 == white and colour3 == white:
      displaytext(("Score: " + str(game_score)), blue, bigfont, 0, 0)
      pygame.draw.circle(gameDisplay, white, (x_shape1, y_shape1), 50)
      pygame.draw.circle(gameDisplay, white, (x_shape3, y_shape3), 50)
      pygame.draw.circle(gameDisplay, white, (x_shape5, y_shape5), 50)
      pygame.display.update()
      pygame.time.delay(1000)
      finishlevel4()
    mousepos = pygame.mouse.get_pos() #current position of mouse
    x_shape1 += direction1_x #update the x position of shape 1
    y_shape1 += direction1_y #update the y position of shape 1
    x_shape2 += direction2_x #update the x position of shape 2
    y_shape2 += direction2_y #update the y position of shape 2
    x_shape3 += direction3_x #update the x position of shape 3
    y_shape3 += direction3_y #update the y position of shape 3
    x_shape4 += direction4_x #update the x position of shape 4
    y_shape4 += direction4_y #update the y position of shape 4
    x_shape5 += direction5_x #update the x position of shape 5
    y_shape5 += direction5_y #update the y position of shape 5
    x_shape6 += direction6_x #update the x position of shape 6
    y_shape6 += direction6_y #update the y position of shape 6
    x_shape7 += direction7_x #update the x position of shape 7
    y_shape7 += direction7_y #update the y position of shape 7
    #make the shapes bounce
    if x_shape1 >= 1150 or x_shape1 <= 50:
      direction1_x *= -1
    if y_shape1 >= 750 or y_shape1 <= 50:
      direction1_y *= -1
    if x_shape2 >= 1100 or x_shape2 <= 0:
      direction2_x *= -1
    if y_shape2 >= 750 or y_shape2 <= 0:
      direction2_y *= -1
    if x_shape3 >= 1150 or x_shape3 <= 50:
      direction3_x *= -1
    if y_shape3 >= 750 or y_shape3 <= 50:
      direction3_y *= -1
    if x_shape4 >= 1100 or x_shape4 <= 0:
      direction4_x *= -1
    if y_shape4 >= 750 or y_shape4 <= 0:
      direction4_y *= -1
    if x_shape5 >= 1150 or x_shape5 <= 50:
      direction5_x *= -1
    if y_shape5 >= 750 or y_shape5 <= 50:
      direction5_y *= -1
    if x_shape6 >= 1100 or x_shape6 <= 0:
      direction6_x *= -1 
    if y_shape6 >= 750 or y_shape6 <= 0:
      direction6_y *= -1
    if x_shape7 >= 1100 or x_shape7 <= 0:
      direction7_x *= -1 
    if y_shape7 >= 750 or y_shape7 <= 0:
      direction7_y *= -1  
    #draw the shapes
    pygame.draw.rect(gameDisplay, grey, (0, 0, x, y))
    pygame.draw.circle(gameDisplay, colour1, (x_shape1, y_shape1), 50)
    pygame.draw.rect(gameDisplay, red, (x_shape2, y_shape2, 100, 50))
    pygame.draw.circle(gameDisplay, colour2, (x_shape3, y_shape3), 50)
    pygame.draw.rect(gameDisplay, red, (x_shape4, y_shape4, 100, 50))
    pygame.draw.circle(gameDisplay, colour3, (x_shape5, y_shape5), 50)
    pygame.draw.rect(gameDisplay, red, (x_shape6, y_shape6, 100, 50))
    pygame.draw.rect(gameDisplay, red, (x_shape7, y_shape7, 100, 50))
    #check if the shape has been clicked on
    if mousepos[0] > x_shape1 - 50 and mousepos[0] < x_shape1 + 50 and mousepos[1] > y_shape1 - 50 and mousepos[1] < y_shape1 + 50:
      if event.type == pygame.MOUSEBUTTONDOWN:
        if colour1 != white:
          #turn the shape white and slow it down
          colour1 = white
          direction1_x = 0.5
          direction1_y = 0.5
          game_score += 1
          pygame.display.update()
    if mousepos[0] > x_shape2 - 50 and mousepos[0] < x_shape2 + 50 and mousepos[1] > y_shape2 - 50 and mousepos[1] < y_shape2 + 50:
      #make sure mouse click is recetn
      if event.type == pygame.MOUSEBUTTONDOWN:
        if game_score >= 3:
          game_score -= 3
        else:
          game_score = 0
    if mousepos[0] > x_shape4 - 50 and mousepos[0] < x_shape4 + 50 and mousepos[1] > y_shape4 - 50 and mousepos[1] < y_shape4 + 50:
      if event.type == pygame.MOUSEBUTTONDOWN:
        #make sure game score doesnt become negative
        if game_score >= 3:
          game_score -= 3
        else:
          game_score = 0
    if mousepos[0] > x_shape3 - 50 and mousepos[0] < x_shape3 + 50 and mousepos[1] > y_shape3 - 50 and mousepos[1] < y_shape3 + 50:
      if event.type == pygame.MOUSEBUTTONDOWN:
        #make sure shape hasnt already been clicked on
        if colour2 != white:
          colour2 = white
          direction3_x = 0.5
          direction3_y = 0.5
          game_score += 3
          pygame.display.update()
    if mousepos[0] > x_shape5 - 50 and mousepos[0] < x_shape5 + 50 and mousepos[1] > y_shape5 - 50 and mousepos[1] < y_shape5 + 50:
      if event.type == pygame.MOUSEBUTTONDOWN:
        #make sure shape hasnt already been clicked on
        if colour3 != white:
          #turn the shape white and slow it down
          colour3 = white
          direction5_x = 0.5
          direction5_y = 0.5
          game_score += 10
          pygame.display.update()
    if mousepos[0] > x_shape6 - 50 and mousepos[0] < x_shape6 + 50 and mousepos[1] > y_shape6 - 50 and mousepos[1] < y_shape6 + 50:
      if event.type == pygame.MOUSEBUTTONDOWN:
        #make sure game score doesnt become negative
        if game_score >= 3:
          game_score -= 3
        else:
          game_score = 0
    if mousepos[0] > x_shape7 - 50 and mousepos[0] < x_shape7 + 50 and mousepos[1] > y_shape7 - 50 and mousepos[1] < y_shape7 + 50:
      if event.type == pygame.MOUSEBUTTONDOWN:
        #make sure game score doesnt become negative
        if game_score >= 3:
          game_score -= 3
        else:
          game_score = 0
    #display score
    displaytext(("Score: " + str(game_score)), blue, bigfont, 0, 0)
    pygame.display.update()
    clock.tick(60)

def finishlevel4():
  finish4 = True
  while finish4:
    for event in pygame.event.get():
      print(event)
      if event.type == pygame.QUIT:
        pygame.quit()
        exit()
    #display completyion screen
    gameDisplay.blit(level4completion_background, (0, 0))
    #make continue button
    button("Continue", 100, 50, 1100, 750, black, grey, "startlevel5")
    pygame.display.update()
    clock.tick(60)    

def playlevel5():
  #import and declare variables
  global grey
  global blue
  global green
  global x
  global y
  global pink
  global purple
  colour1 = blue
  colour2 = green
  colour3 = pink
  colour4 = purple
  global game_score
  global red
  global white
  playing_game5 = True
  #generate starting positions
  x_shape1 = random.randint(50,1150)
  y_shape1 = random.randint(50,750)
  x_shape2 = random.randint(0,1100)
  y_shape2 = random.randint(0,750)
  x_shape3 = random.randint(50, 1150)
  y_shape3 = random.randint(50, 750)
  x_shape4 = random.randint(0,1100)
  y_shape4 = random.randint(0,750)
  x_shape5 = random.randint(50, 1150)
  y_shape5 = random.randint(50,750)
  x_shape6 = random.randint(0,1100)
  y_shape6 = random.randint(0,750)
  x_shape7 = random.randint(0,1100)
  y_shape7 = random.randint(0,750)
  x_shape8 = random.randint(50,1150)
  y_shape8 = random.randint(50,750)
  #generate velocities
  direction1_x = random.randint(1, 5)
  direction1_y = random.randint(1, 5)
  direction2_x = random.randint(1, 7)
  direction2_y = random.randint(1, 7)
  direction3_x = random.randint(1, 7)
  direction3_y = random.randint(1, 3)
  direction4_x = random.randint(1, 9)
  direction4_y = random.randint(1, 9)
  direction5_x = random.randint(5, 13)
  direction5_y = random.randint(5, 13)
  direction6_x = random.randint(1, 11)
  direction6_y = random.randint(1, 11)
  direction7_x = random.randint(1, 11)
  direction7_y = random.randint(1, 11)
  direction8_x = random.randint(1, 3)
  direction8_y = random.randint(1, 3)
  #game loop
  while playing_game5:
    for event in pygame.event.get():
      print(event)
      if event.type == pygame.QUIT:
        pygame.quit()
        exit()
    #check if all shapes haev been clicked on
    if colour1 == white and colour2 == white and colour3 == white and colour4 == white:
      displaytext(("Score: " + str(game_score)), blue, bigfont, 0, 0)
      pygame.draw.circle(gameDisplay, white, (x_shape1, y_shape1), 50)
      pygame.draw.circle(gameDisplay, white, (x_shape3, y_shape3), 50)
      pygame.draw.circle(gameDisplay, white, (x_shape5, y_shape5), 50)
      pygame.draw.circle(gameDisplay, white, (x_shape8, y_shape8), 50)
      pygame.display.update()
      pygame.time.delay(1000)
      finishlevel5()
    mousepos = pygame.mouse.get_pos() #current position of mouse
    x_shape1 += direction1_x #update the x position of shape 1
    y_shape1 += direction1_y #update the y position of shape 1
    x_shape2 += direction2_x #update the x position of shape 2
    y_shape2 += direction2_y #update the y position of shape 2
    x_shape3 += direction3_x #update the x position of shape 3
    y_shape3 += direction3_y #update the y position of shape 3
    x_shape4 += direction4_x #update the x position of shape 4
    y_shape4 += direction4_y #update the y position of shape 4
    x_shape5 += direction5_x #update the x position of shape 5
    y_shape5 += direction5_y #update the y position of shape 5
    x_shape6 += direction6_x #update the x position of shape 6
    y_shape6 += direction6_y #update the y position of shape 6
    x_shape7 += direction7_x #update the x position of shape 7
    y_shape7 += direction7_y #update the y position of shape 7
    x_shape8 += direction8_x #update the x position of shape 8
    y_shape8 += direction8_y #update the y position of shape 8
    #make shapes bounce
    if x_shape1 >= 1150 or x_shape1 <= 50:
      direction1_x *= -1
    if y_shape1 >= 750 or y_shape1 <= 50:
      direction1_y *= -1
    if x_shape2 >= 1100 or x_shape2 <= 0:
      direction2_x *= -1
    if y_shape2 >= 750 or y_shape2 <= 0:
      direction2_y *= -1
    if x_shape3 >= 1150 or x_shape3 <= 50:
      direction3_x *= -1
    if y_shape3 >= 750 or y_shape3 <= 50:
      direction3_y *= -1
    if x_shape4 >= 1100 or x_shape4 <= 0:
      direction4_x *= -1
    if y_shape4 >= 750 or y_shape4 <= 0:
      direction4_y *= -1
    if x_shape5 >= 1150 or x_shape5 <= 50:
      direction5_x *= -1
    if y_shape5 >= 750 or y_shape5 <= 50:
      direction5_y *= -1
    if x_shape6 >= 1100 or x_shape6 <= 0:
      direction6_x *= -1 
    if y_shape6 >= 750 or y_shape6 <= 0:
      direction6_y *= -1
    if x_shape7 >= 1100 or x_shape7 <= 0:
      direction7_x *= -1 
    if y_shape7 >= 750 or y_shape7 <= 0:
      direction7_y *= -1  
    if x_shape8 >= 1150 or x_shape8 <= 50:
      direction8_x *= -1
    if y_shape8 >= 750 or y_shape8 <= 50:
      direction8_y *= -1
    #draw the shape
    pygame.draw.rect(gameDisplay, grey, (0, 0, x, y))
    pygame.draw.circle(gameDisplay, colour1, (x_shape1, y_shape1), 50)
    pygame.draw.rect(gameDisplay, red, (x_shape2, y_shape2, 100, 50))
    pygame.draw.circle(gameDisplay, colour2, (x_shape3, y_shape3), 50)
    pygame.draw.rect(gameDisplay, red, (x_shape4, y_shape4, 100, 50))
    pygame.draw.circle(gameDisplay, colour3, (x_shape5, y_shape5), 50)
    pygame.draw.rect(gameDisplay, red, (x_shape6, y_shape6, 100, 50))
    pygame.draw.rect(gameDisplay, red, (x_shape7, y_shape7, 100, 50))
    pygame.draw.circle(gameDisplay, colour4, (x_shape8, y_shape8), 50)
    #check if the shape has been clicked on
    if mousepos[0] > x_shape1 - 50 and mousepos[0] < x_shape1 + 50 and mousepos[1] > y_shape1 - 50 and mousepos[1] < y_shape1 + 50:
      if event.type == pygame.MOUSEBUTTONDOWN:
        #make sure shape hasnt alreadt been clicked on
        if colour1 != white:
          #make shape white and slow it down
          colour1 = white
          direction1_x = 0.5
          direction1_y = 0.5
          game_score += 1
          pygame.display.update()
    if mousepos[0] > x_shape2 - 50 and mousepos[0] < x_shape2 + 50 and mousepos[1] > y_shape2 - 50 and mousepos[1] < y_shape2 + 50:
      if event.type == pygame.MOUSEBUTTONDOWN:
        #check if game score is above 3 to prevent negative scores
        if game_score >= 3:
          game_score -= 3
        else:
          game_score = 0
    if mousepos[0] > x_shape4 - 50 and mousepos[0] < x_shape4 + 50 and mousepos[1] > y_shape4 - 50 and mousepos[1] < y_shape4 + 50:
      if event.type == pygame.MOUSEBUTTONDOWN:
        #make sure score doesnt go negative
        if game_score >= 3:
          game_score -= 3
        else:
          game_score = 0
    if mousepos[0] > x_shape3 - 50 and mousepos[0] < x_shape3 + 50 and mousepos[1] > y_shape3 - 50 and mousepos[1] < y_shape3 + 50:
      if event.type == pygame.MOUSEBUTTONDOWN:
        #make sure shape hasnt been previously clicked on
        if colour2 != white:
          #make shape white and slow it down
          colour2 = white
          direction3_x = 0.5
          direction3_y = 0.5
          game_score += 3
          pygame.display.update()
    if mousepos[0] > x_shape5 - 50 and mousepos[0] < x_shape5 + 50 and mousepos[1] > y_shape5 - 50 and mousepos[1] < y_shape5 + 50:
      if event.type == pygame.MOUSEBUTTONDOWN:
        if colour3 != white:
          #make shape white and slow it down
          colour3 = white
          direction5_x = 0.5
          direction5_y = 0.5
          game_score += 10
          pygame.display.update()
    if mousepos[0] > x_shape6 - 50 and mousepos[0] < x_shape6 + 50 and mousepos[1] > y_shape6 - 50 and mousepos[1] < y_shape6 + 50:
      if event.type == pygame.MOUSEBUTTONDOWN:
        #make sure score doesnt become negative
        if game_score >= 3:
          game_score -= 3
        else:
          game_score = 0
    if mousepos[0] > x_shape7 - 50 and mousepos[0] < x_shape7 + 50 and mousepos[1] > y_shape7 - 50 and mousepos[1] < y_shape7 + 50:
      if event.type == pygame.MOUSEBUTTONDOWN:
        #make sure score doesnt become negative
        if game_score >= 3:
          game_score -= 3
        else:
          game_score = 0
    if mousepos[0] > x_shape8 - 50 and mousepos[0] < x_shape8 + 50 and mousepos[1] > y_shape8 - 50 and mousepos[1] < y_shape8 + 50:
      if event.type == pygame.MOUSEBUTTONDOWN:
        if colour4 != white:
          #slow down shape and turn it white
          colour4 = white
          direction8_x = 0.5
          direction8_y = 0.5
          game_score += 2
    #display score
    displaytext(("Score: " + str(game_score)), blue, bigfont, 0, 0)
    pygame.display.update()
    clock.tick(60)

def finishlevel5():
  finish5 = True
  while finish5:
    for event in pygame.event.get():
      print(event)
      if event.type == pygame.QUIT:
        pygame.quit()
        exit()
    #create background
    gameDisplay.blit(level5completion_background, (0, 0))
    #make next level button
    button("Continue", 100, 50, 1100, 750, black, grey, "startlevel6")
    pygame.display.update()
    clock.tick(60)  

def playlevel6():
  #import and declare variables
  global grey
  global blue
  global green
  global x
  global y
  global pink
  global purple
  colour1 = blue
  colour2 = green
  colour3 = pink
  colour4 = purple
  global game_score
  global red
  global white
  playing_game6 = True
  #generate starting positions
  x_shape1 = random.randint(50,1150)
  y_shape1 = random.randint(50,750)
  x_shape2 = random.randint(0,1100)
  y_shape2 = random.randint(0,750)
  x_shape3 = random.randint(50, 1150)
  y_shape3 = random.randint(50, 750)
  x_shape4 = random.randint(0,1100)
  y_shape4 = random.randint(0,750)
  x_shape5 = random.randint(50, 1150)
  y_shape5 = random.randint(50,750)
  x_shape6 = random.randint(0,1100)
  y_shape6 = random.randint(0,750)
  x_shape7 = random.randint(0,1100)
  y_shape7 = random.randint(0,750)
  x_shape8 = random.randint(50,1150)
  y_shape8 = random.randint(50,750)
  x_shape9 = random.randint(0,1100)
  y_shape9 = random.randint(0,750)
  #generae shape velocities
  direction1_x = random.randint(1, 5)
  direction1_y = random.randint(1, 5)
  direction2_x = random.randint(1, 7)
  direction2_y = random.randint(1, 7)
  direction3_x = random.randint(1, 7)
  direction3_y = random.randint(1, 3)
  direction4_x = random.randint(1, 9)
  direction4_y = random.randint(1, 9)
  direction5_x = random.randint(5, 13)
  direction5_y = random.randint(5, 13)
  direction6_x = random.randint(1, 11)
  direction6_y = random.randint(1, 11)
  direction7_x = random.randint(1, 11)
  direction7_y = random.randint(1, 11)
  direction8_x = random.randint(1, 3)
  direction8_y = random.randint(1, 3)
  direction9_x = random.randint(1, 13)
  direction9_y = random.randint(1, 13)
  #game loop
  while playing_game6:
    for event in pygame.event.get():
      print(event)
      if event.type == pygame.QUIT:
        pygame.quit()
        exit()
    #check if all shapes have been clicked on
    if colour1 == white and colour2 == white and colour3 == white and colour4 == white:
      displaytext(("Score: " + str(game_score)), blue, bigfont, 0, 0)
      pygame.draw.circle(gameDisplay, white, (x_shape1, y_shape1), 50)
      pygame.draw.circle(gameDisplay, white, (x_shape3, y_shape3), 50)
      pygame.draw.circle(gameDisplay, white, (x_shape5, y_shape5), 50)
      pygame.draw.circle(gameDisplay, white, (x_shape8, y_shape8), 50)
      pygame.display.update()
      pygame.time.delay(1000)
      finishlevel6()
    mousepos = pygame.mouse.get_pos() #current position of mouse
    x_shape1 += direction1_x #update the x position of shape 1
    y_shape1 += direction1_y #update the y position of shape 1
    x_shape2 += direction2_x #update the x position of shape 2
    y_shape2 += direction2_y #update the y position of shape 2
    x_shape3 += direction3_x #update the x position of shape 3
    y_shape3 += direction3_y #update the y position of shape 3
    x_shape4 += direction4_x #update the x position of shape 4
    y_shape4 += direction4_y #update the y position of shape 4
    x_shape5 += direction5_x #update the x position of shape 5
    y_shape5 += direction5_y #update the y position of shape 5
    x_shape6 += direction6_x #update the x position of shape 6
    y_shape6 += direction6_y #update the y position of shape 6
    x_shape7 += direction7_x #update the x position of shape 7
    y_shape7 += direction7_y #update the y position of shape 7
    x_shape8 += direction8_x #update the x position of shape 8
    y_shape8 += direction8_y #update the y position of shape 8
    x_shape9 += direction9_x #update the x position of shape 9
    y_shape9 += direction9_y #update the y position of shape 9
    #make the shapes bounce
    if x_shape1 >= 1150 or x_shape1 <= 50:
      direction1_x *= -1
    if y_shape1 >= 750 or y_shape1 <= 50:
      direction1_y *= -1
    if x_shape2 >= 1100 or x_shape2 <= 0:
      direction2_x *= -1
    if y_shape2 >= 750 or y_shape2 <= 0:
      direction2_y *= -1
    if x_shape3 >= 1150 or x_shape3 <= 50:
      direction3_x *= -1
    if y_shape3 >= 750 or y_shape3 <= 50:
      direction3_y *= -1
    if x_shape4 >= 1100 or x_shape4 <= 0:
      direction4_x *= -1
    if y_shape4 >= 750 or y_shape4 <= 0:
      direction4_y *= -1
    if x_shape5 >= 1150 or x_shape5 <= 50:
      direction5_x *= -1
    if y_shape5 >= 750 or y_shape5 <= 50:
      direction5_y *= -1
    if x_shape6 >= 1100 or x_shape6 <= 0:
      direction6_x *= -1 
    if y_shape6 >= 750 or y_shape6 <= 0:
      direction6_y *= -1
    if x_shape7 >= 1100 or x_shape7 <= 0:
      direction7_x *= -1 
    if y_shape7 >= 750 or y_shape7 <= 0:
      direction7_y *= -1  
    if x_shape8 >= 1150 or x_shape8 <= 50:
      direction8_x *= -1
    if y_shape8 >= 750 or y_shape8 <= 50:
      direction8_y *= -1
    if x_shape9 >= 1100 or x_shape9 <= 0:
      direction9_x *= -1
    if y_shape9 >= 750 or y_shape9 <= 0:
      direction9_y *= -1
    #draw the shapes
    pygame.draw.rect(gameDisplay, grey, (0, 0, x, y))
    pygame.draw.circle(gameDisplay, colour1, (x_shape1, y_shape1), 50)
    pygame.draw.rect(gameDisplay, red, (x_shape2, y_shape2, 100, 50))
    pygame.draw.circle(gameDisplay, colour2, (x_shape3, y_shape3), 50)
    pygame.draw.rect(gameDisplay, red, (x_shape4, y_shape4, 100, 50))
    pygame.draw.circle(gameDisplay, colour3, (x_shape5, y_shape5), 50)
    pygame.draw.rect(gameDisplay, red, (x_shape6, y_shape6, 100, 50))
    pygame.draw.rect(gameDisplay, red, (x_shape7, y_shape7, 100, 50))
    pygame.draw.circle(gameDisplay, colour4, (x_shape8, y_shape8), 50)
    pygame.draw.rect(gameDisplay, red, (x_shape9, y_shape9, 100, 50))
    #check if the shape has been clicked on
    if mousepos[0] > x_shape1 - 50 and mousepos[0] < x_shape1 + 50 and mousepos[1] > y_shape1 - 50 and mousepos[1] < y_shape1 + 50:
      if event.type == pygame.MOUSEBUTTONDOWN:
        #check if shape has already been clicked on
        if colour1 != white:
          #make shape whtie and slow it down
          colour1 = white
          direction1_x = 0.5
          direction1_y = 0.5
          game_score += 1
          pygame.display.update()
    if mousepos[0] > x_shape2 - 50 and mousepos[0] < x_shape2 + 50 and mousepos[1] > y_shape2 - 50 and mousepos[1] < y_shape2 + 50:
      if event.type == pygame.MOUSEBUTTONDOWN:
        #make sure score doesnt become negative
        if game_score >= 3:
          game_score -= 3
        else:
          game_score = 0
    if mousepos[0] > x_shape4 - 50 and mousepos[0] < x_shape4 + 50 and mousepos[1] > y_shape4 - 50 and mousepos[1] < y_shape4 + 50:
      if event.type == pygame.MOUSEBUTTONDOWN:
        #make sure score doesnt become negative
        if game_score >= 3:
          game_score -= 3
        else:
          game_score = 0
    if mousepos[0] > x_shape3 - 50 and mousepos[0] < x_shape3 + 50 and mousepos[1] > y_shape3 - 50 and mousepos[1] < y_shape3 + 50:
      if event.type == pygame.MOUSEBUTTONDOWN:
        #check if shape has already been clicked on
        if colour2 != white:
          #turn shape white and slow it down
          colour2 = white
          direction3_x = 0.5
          direction3_y = 0.5
          game_score += 3
          pygame.display.update()
    if mousepos[0] > x_shape5 - 50 and mousepos[0] < x_shape5 + 50 and mousepos[1] > y_shape5 - 50 and mousepos[1] < y_shape5 + 50:
      if event.type == pygame.MOUSEBUTTONDOWN:
        #check if shape has already been clicked on
        if colour3 != white:
          #turn shape white and slow it down
          colour3 = white
          direction5_x = 0.5
          direction5_y = 0.5
          game_score += 10
          pygame.display.update()
    if mousepos[0] > x_shape6 - 50 and mousepos[0] < x_shape6 + 50 and mousepos[1] > y_shape6 - 50 and mousepos[1] < y_shape6 + 50:
      if event.type == pygame.MOUSEBUTTONDOWN:
        #make sure game score doesn t become negative
        if game_score >= 3:
          game_score -= 3
        else:
          game_score = 0
    if mousepos[0] > x_shape7 - 50 and mousepos[0] < x_shape7 + 50 and mousepos[1] > y_shape7 - 50 and mousepos[1] < y_shape7 + 50:
      if event.type == pygame.MOUSEBUTTONDOWN:
        #make sure game score doesnt become negative
        if game_score >= 3:
          game_score -= 3
        else:
          game_score = 0
    if mousepos[0] > x_shape8 - 50 and mousepos[0] < x_shape8 + 50 and mousepos[1] > y_shape8 - 50 and mousepos[1] < y_shape8 + 50:
      if event.type == pygame.MOUSEBUTTONDOWN:
        #check if shape has already been clicked on
        if colour4 != white:
          #turn shape white and slow it down
          colour4 = white
          direction8_x = 0.5
          direction8_y = 0.5
          game_score += 2
    if mousepos[0] > x_shape9 - 50 and mousepos[0] < x_shape9 + 50 and mousepos[1] > y_shape9 - 50 and mousepos[1] < y_shape9 + 50:
      if event.type == pygame.MOUSEBUTTONDOWN:
        #make sure game score doesnt become negative
        if game_score >= 3:
          game_score -= 3
        else:
          game_score = 0
    #display score
    displaytext(("Score: " + str(game_score)), blue, bigfont, 0, 0)
    pygame.display.update()
    clock.tick(60)

def finishlevel6():
  finish6 = True
  while finish6:
    for event in pygame.event.get():
      print(event)
      if event.type == pygame.QUIT:
        pygame.quit()
        exit()
    #make background
    gameDisplay.blit(level6completion_background, (0, 0))
    #make button
    button("Continue", 100, 50, 1100, 750, black, grey, "showgoldencircle")
    pygame.display.update()
    clock.tick(60) 

#golden circle warning
def showgoldencircle():
  showinggoldencircle = True
  while showinggoldencircle:
    for event in pygame.event.get():
      print(event)
      if event.type == pygame.QUIT:
        pygame.quit()
        exit()
    #make background
    gameDisplay.blit(goldencirclewarning_background, (0, 0))\
    #create button
    button("Continue", 100, 50, 1100, 750, black, grey, "startlevel7")
    pygame.display.update()
    clock.tick(60) 

def playlevel7():
  #import and declare variables
  global grey
  global blue
  global green
  global x
  global y
  global pink
  global purple
  global yellow
  colour1 = blue
  colour2 = green
  colour3 = pink
  colour4 = purple
  colour5 = yellow
  global game_score
  global red
  global white
  playing_game7 = True
  #generate starting positions
  x_shape1 = random.randint(50,1150)
  y_shape1 = random.randint(50,750)
  x_shape2 = random.randint(0,1100)
  y_shape2 = random.randint(0,750)
  x_shape3 = random.randint(50, 1150)
  y_shape3 = random.randint(50, 750)
  x_shape4 = random.randint(0,1100)
  y_shape4 = random.randint(0,750)
  x_shape5 = random.randint(50, 1150)
  y_shape5 = random.randint(50,750)
  x_shape6 = random.randint(0,1100)
  y_shape6 = random.randint(0,750)
  x_shape7 = random.randint(0,1100)
  y_shape7 = random.randint(0,750)
  x_shape8 = random.randint(50,1150)
  y_shape8 = random.randint(50,750)
  x_shape9 = random.randint(0,1100)
  y_shape9 = random.randint(0,750)
  x_shape10 = random.randint(50,1150)
  y_shape10 = random.randint(50,750)
  #generate velocities
  direction1_x = random.randint(1, 5)
  direction1_y = random.randint(1, 5)
  direction2_x = random.randint(1, 7)
  direction2_y = random.randint(1, 7)
  direction3_x = random.randint(1, 7)
  direction3_y = random.randint(1, 3)
  direction4_x = random.randint(1, 9)
  direction4_y = random.randint(1, 9)
  direction5_x = random.randint(5, 13)
  direction5_y = random.randint(5, 13)
  direction6_x = random.randint(1, 11)
  direction6_y = random.randint(1, 11)
  direction7_x = random.randint(1, 11)
  direction7_y = random.randint(1, 11)
  direction8_x = random.randint(1, 3)
  direction8_y = random.randint(1, 3)
  direction9_x = random.randint(1, 13)
  direction9_y = random.randint(1, 13)
  direction10_x = random.randint(18, 25)
  direction10_y = random.randint(18, 25)
  #game level1completion_background
  while playing_game7:
    for event in pygame.event.get():
      print(event)
      if event.type == pygame.QUIT:
        pygame.quit()
        exit()
    #check if all shapes have been clicked
    if colour1 == white and colour2 == white and colour3 == white and colour4 == white:
      displaytext(("Score: " + str(game_score)), blue, bigfont, 0, 0)
      pygame.draw.circle(gameDisplay, white, (x_shape1, y_shape1), 50)
      pygame.draw.circle(gameDisplay, white, (x_shape3, y_shape3), 50)
      pygame.draw.circle(gameDisplay, white, (x_shape5, y_shape5), 50)
      pygame.draw.circle(gameDisplay, white, (x_shape8, y_shape8), 50)
      pygame.display.update()
      pygame.time.delay(1000)
      finishlevel7()
    mousepos = pygame.mouse.get_pos() #current position of mouse
    x_shape1 += direction1_x #update the x position of shape 1
    y_shape1 += direction1_y #update the y position of shape 1
    x_shape2 += direction2_x #update the x position of shape 2
    y_shape2 += direction2_y #update the y position of shape 2
    x_shape3 += direction3_x #update the x position of shape 3
    y_shape3 += direction3_y #update the y position of shape 3
    x_shape4 += direction4_x #update the x position of shape 4
    y_shape4 += direction4_y #update the y position of shape 4
    x_shape5 += direction5_x #update the x position of shape 5
    y_shape5 += direction5_y #update the y position of shape 5
    x_shape6 += direction6_x #update the x position of shape 6
    y_shape6 += direction6_y #update the y position of shape 6
    x_shape7 += direction7_x #update the x position of shape 7
    y_shape7 += direction7_y #update the y position of shape 7
    x_shape8 += direction8_x #update the x position of shape 8
    y_shape8 += direction8_y #update the y position of shape 8
    x_shape9 += direction9_x #update the x position of shape 9
    y_shape9 += direction9_y #update the y position of shape 9
    x_shape10 += direction10_x #update the x position of shape 10
    y_shape10 += direction10_y #update the y position of shape 10
    #make shapes bounce
    if x_shape1 >= 1150 or x_shape1 <= 50:
      direction1_x *= -1
    if y_shape1 >= 750 or y_shape1 <= 50:
      direction1_y *= -1
    if x_shape2 >= 1100 or x_shape2 <= 0:
      direction2_x *= -1
    if y_shape2 >= 750 or y_shape2 <= 0:
      direction2_y *= -1
    if x_shape3 >= 1150 or x_shape3 <= 50:
      direction3_x *= -1
    if y_shape3 >= 750 or y_shape3 <= 50:
      direction3_y *= -1
    if x_shape4 >= 1100 or x_shape4 <= 0:
      direction4_x *= -1
    if y_shape4 >= 750 or y_shape4 <= 0:
      direction4_y *= -1
    if x_shape5 >= 1150 or x_shape5 <= 50:
      direction5_x *= -1
    if y_shape5 >= 750 or y_shape5 <= 50:
      direction5_y *= -1
    if x_shape6 >= 1100 or x_shape6 <= 0:
      direction6_x *= -1 
    if y_shape6 >= 750 or y_shape6 <= 0:
      direction6_y *= -1
    if x_shape7 >= 1100 or x_shape7 <= 0:
      direction7_x *= -1 
    if y_shape7 >= 750 or y_shape7 <= 0:
      direction7_y *= -1  
    if x_shape8 >= 1150 or x_shape8 <= 50:
      direction8_x *= -1
    if y_shape8 >= 750 or y_shape8 <= 50:
      direction8_y *= -1
    if x_shape9 >= 1100 or x_shape9 <= 0:
      direction9_x *= -1
    if y_shape9 >= 750 or y_shape9 <= 0:
      direction9_y *= -1
    if x_shape10 >= 1150 or x_shape10 <= 50:
      direction10_x *= -1
    if y_shape10 >= 750 or y_shape10 <= 50:
      direction10_y *= -1
    #draw the shapes
    pygame.draw.rect(gameDisplay, grey, (0, 0, x, y))
    pygame.draw.circle(gameDisplay, colour1, (x_shape1, y_shape1), 50)
    pygame.draw.rect(gameDisplay, red, (x_shape2, y_shape2, 100, 50))
    pygame.draw.circle(gameDisplay, colour2, (x_shape3, y_shape3), 50)
    pygame.draw.rect(gameDisplay, red, (x_shape4, y_shape4, 100, 50))
    pygame.draw.circle(gameDisplay, colour3, (x_shape5, y_shape5), 50)
    pygame.draw.rect(gameDisplay, red, (x_shape6, y_shape6, 100, 50))
    pygame.draw.rect(gameDisplay, red, (x_shape7, y_shape7, 100, 50))
    pygame.draw.circle(gameDisplay, colour4, (x_shape8, y_shape8), 50)
    pygame.draw.rect(gameDisplay, red, (x_shape9, y_shape9, 100, 50))
    pygame.draw.circle(gameDisplay, colour5, (x_shape10, y_shape10), 50)
    #check if the shape has been clicked on
    if mousepos[0] > x_shape1 - 50 and mousepos[0] < x_shape1 + 50 and mousepos[1] > y_shape1 - 50 and mousepos[1] < y_shape1 + 50:
      if event.type == pygame.MOUSEBUTTONDOWN:
        #check if shape has already been clicked
        if colour1 != white:
          #turn shape white and slow it down
          colour1 = white
          direction1_x = 0.5
          direction1_y = 0.5
          game_score += 1
          pygame.display.update()
    if mousepos[0] > x_shape2 - 50 and mousepos[0] < x_shape2 + 50 and mousepos[1] > y_shape2 - 50 and mousepos[1] < y_shape2 + 50:
      if event.type == pygame.MOUSEBUTTONDOWN:
        #make sure game score doesnt become negative
        if game_score >= 3:
          game_score -= 3
        else:
          game_score = 0
    if mousepos[0] > x_shape4 - 50 and mousepos[0] < x_shape4 + 50 and mousepos[1] > y_shape4 - 50 and mousepos[1] < y_shape4 + 50:
      if event.type == pygame.MOUSEBUTTONDOWN:
        #make sure game score doesnt become negative
        if game_score >= 3:
          game_score -= 3
        else:
          game_score = 0
    if mousepos[0] > x_shape3 - 50 and mousepos[0] < x_shape3 + 50 and mousepos[1] > y_shape3 - 50 and mousepos[1] < y_shape3 + 50:
      if event.type == pygame.MOUSEBUTTONDOWN:  
        #check if shape has already been clicked on
        if colour2 != white:
          #turn shpae white and slow it down
          colour2 = white
          direction3_x = 0.5
          direction3_y = 0.5
          game_score += 3
          pygame.display.update()
    if mousepos[0] > x_shape5 - 50 and mousepos[0] < x_shape5 + 50 and mousepos[1] > y_shape5 - 50 and mousepos[1] < y_shape5 + 50:
      if event.type == pygame.MOUSEBUTTONDOWN:
        #check if shape has been clicked on
        if colour3 != white:
          #turn white and slow down
          colour3 = white
          direction5_x = 0.5
          direction5_y = 0.5
          game_score += 10
          pygame.display.update()
    if mousepos[0] > x_shape6 - 50 and mousepos[0] < x_shape6 + 50 and mousepos[1] > y_shape6 - 50 and mousepos[1] < y_shape6 + 50:
      if event.type == pygame.MOUSEBUTTONDOWN:
        #make sure that game score doesnt become negatibve
        if game_score >= 3:
          game_score -= 3
        else:
          game_score = 0
    if mousepos[0] > x_shape7 - 50 and mousepos[0] < x_shape7 + 50 and mousepos[1] > y_shape7 - 50 and mousepos[1] < y_shape7 + 50:
      if event.type == pygame.MOUSEBUTTONDOWN:
        #make sure game score doesnt become negative
        if game_score >= 3:
          game_score -= 3
        else:
          game_score = 0
    if mousepos[0] > x_shape8 - 50 and mousepos[0] < x_shape8 + 50 and mousepos[1] > y_shape8 - 50 and mousepos[1] < y_shape8 + 50:
      if event.type == pygame.MOUSEBUTTONDOWN:
        #check if shape has already been clicked on
        if colour4 != white:
          #turn white and slow down
          colour4 = white
          direction8_x = 0.5
          direction8_y = 0.5
          game_score += 2
    if mousepos[0] > x_shape9 - 50 and mousepos[0] < x_shape9 + 50 and mousepos[1] > y_shape9 - 50 and mousepos[1] < y_shape9 + 50:
      if event.type == pygame.MOUSEBUTTONDOWN:
        #make sure game score deosnt become negative
        if game_score >= 3:
          game_score -= 3
        else:
          game_score = 0
    if mousepos[0] > x_shape10 - 50 and mousepos[0] < x_shape10 + 50 and mousepos[1] > y_shape10 - 50 and mousepos[1] < y_shape10 + 50:
      if event.type == pygame.MOUSEBUTTONDOWN:
        #check if shape has already been clicked on
        if colour5 != white:
          #turn white and slow down
          colour5 = white
          direction10_x = 0.5
          direction10_y = 0.5
          game_score += 25
          pygame.display.update()
    #show score
    displaytext(("Score: " + str(game_score)), blue, bigfont, 0, 0)
    pygame.display.update()
    clock.tick(60)

def finishlevel7():
  finish7 = True
  while finish7:
    for event in pygame.event.get():
      print(event)
      if event.type == pygame.QUIT:
        pygame.quit()
        exit()
    #make background
    gameDisplay.blit(level7completion_background, (0, 0))
    #back button
    button("Continue", 100, 50, 1100, 750, black, grey, "startlevel8")
    pygame.display.update()
    clock.tick(60) 

def playlevel8():
  #import and declare variables
  global grey
  global blue
  global green
  global x
  global y
  global pink
  global purple
  global yellow
  global cyan
  colour1 = blue
  colour2 = green
  colour3 = pink
  colour4 = purple
  colour5 = yellow
  colour6 = cyan
  global game_score
  global red
  global white
  playing_game8 = True
  #generate startign positions
  x_shape1 = random.randint(50,1150)
  y_shape1 = random.randint(50,750)
  x_shape2 = random.randint(0,1100)
  y_shape2 = random.randint(0,750)
  x_shape3 = random.randint(50, 1150)
  y_shape3 = random.randint(50, 750)
  x_shape4 = random.randint(0,1100)
  y_shape4 = random.randint(0,750)
  x_shape5 = random.randint(50, 1150)
  y_shape5 = random.randint(50,750)
  x_shape6 = random.randint(0,1100)
  y_shape6 = random.randint(0,750)
  x_shape7 = random.randint(0,1100)
  y_shape7 = random.randint(0,750)
  x_shape8 = random.randint(50,1150)
  y_shape8 = random.randint(50,750)
  x_shape9 = random.randint(0,1100)
  y_shape9 = random.randint(0,750)
  x_shape10 = random.randint(50,1150)
  y_shape10 = random.randint(50,750)
  x_shape11 = random.randint(50,1150)
  y_shape11 = random.randint(50,750)
  #generate velocities
  direction1_x = random.randint(1, 5)
  direction1_y = random.randint(1, 5)
  direction2_x = random.randint(1, 7)
  direction2_y = random.randint(1, 7)
  direction3_x = random.randint(1, 7)
  direction3_y = random.randint(1, 3)
  direction4_x = random.randint(1, 9)
  direction4_y = random.randint(1, 9)
  direction5_x = random.randint(5, 13)
  direction5_y = random.randint(5, 13)
  direction6_x = random.randint(1, 11)
  direction6_y = random.randint(1, 11)
  direction7_x = random.randint(1, 11)
  direction7_y = random.randint(1, 11)
  direction8_x = random.randint(1, 3)
  direction8_y = random.randint(1, 3)
  direction9_x = random.randint(1, 13)
  direction9_y = random.randint(1, 13)
  direction10_x = random.randint(18, 25)
  direction10_y = random.randint(18, 25)
  direction11_x = random.randint(1, 7)
  direction11_y = random.randint(1, 7)
  #game loop
  while playing_game8:
    for event in pygame.event.get():
      print(event)
      if event.type == pygame.QUIT:
        pygame.quit()
        exit()
    #check if all shapes have been clicked
    if colour1 == white and colour2 == white and colour3 == white and colour4 == white and colour6 == white:
      displaytext(("Score: " + str(game_score)), blue, bigfont, 0, 0)
      pygame.draw.circle(gameDisplay, white, (x_shape1, y_shape1), 50)
      pygame.draw.circle(gameDisplay, white, (x_shape3, y_shape3), 50)
      pygame.draw.circle(gameDisplay, white, (x_shape5, y_shape5), 50)
      pygame.draw.circle(gameDisplay, white, (x_shape8, y_shape8), 50)
      pygame.draw.circle(gameDisplay, white, (x_shape11, y_shape11), 50)
      pygame.display.update()
      pygame.time.delay(1000)
      finishlevel8()
    mousepos = pygame.mouse.get_pos() #current position of mouse
    x_shape1 += direction1_x #update the x position of shape 1
    y_shape1 += direction1_y #update the y position of shape 1
    x_shape2 += direction2_x #update the x position of shape 2
    y_shape2 += direction2_y #update the y position of shape 2
    x_shape3 += direction3_x #update the x position of shape 3
    y_shape3 += direction3_y #update the y position of shape 3
    x_shape4 += direction4_x #update the x position of shape 4
    y_shape4 += direction4_y #update the y position of shape 4
    x_shape5 += direction5_x #update the x position of shape 5
    y_shape5 += direction5_y #update the y position of shape 5
    x_shape6 += direction6_x #update the x position of shape 6
    y_shape6 += direction6_y #update the y position of shape 6
    x_shape7 += direction7_x #update the x position of shape 7
    y_shape7 += direction7_y #update the y position of shape 7
    x_shape8 += direction8_x #update the x position of shape 8
    y_shape8 += direction8_y #update the y position of shape 8
    x_shape9 += direction9_x #update the x position of shape 9
    y_shape9 += direction9_y #update the y position of shape 9
    x_shape10 += direction10_x #update the x position of shape 10
    y_shape10 += direction10_y #update the y position of shape 10
    x_shape11 += direction11_x #update the x position of shape 10
    y_shape11 += direction11_y #update the y position of shape 10
    #make shapes bounce
    if x_shape1 >= 1150 or x_shape1 <= 50:
      direction1_x *= -1
    if y_shape1 >= 750 or y_shape1 <= 50:
      direction1_y *= -1
    if x_shape2 >= 1100 or x_shape2 <= 0:
      direction2_x *= -1
    if y_shape2 >= 750 or y_shape2 <= 0:
      direction2_y *= -1
    if x_shape3 >= 1150 or x_shape3 <= 50:
      direction3_x *= -1
    if y_shape3 >= 750 or y_shape3 <= 50:
      direction3_y *= -1
    if x_shape4 >= 1100 or x_shape4 <= 0:
      direction4_x *= -1
    if y_shape4 >= 750 or y_shape4 <= 0:
      direction4_y *= -1
    if x_shape5 >= 1150 or x_shape5 <= 50:
      direction5_x *= -1
    if y_shape5 >= 750 or y_shape5 <= 50:
      direction5_y *= -1
    if x_shape6 >= 1100 or x_shape6 <= 0:
      direction6_x *= -1 
    if y_shape6 >= 750 or y_shape6 <= 0:
      direction6_y *= -1
    if x_shape7 >= 1100 or x_shape7 <= 0:
      direction7_x *= -1 
    if y_shape7 >= 750 or y_shape7 <= 0:
      direction7_y *= -1  
    if x_shape8 >= 1150 or x_shape8 <= 50:
      direction8_x *= -1
    if y_shape8 >= 750 or y_shape8 <= 50:
      direction8_y *= -1
    if x_shape9 >= 1100 or x_shape9 <= 0:
      direction9_x *= -1
    if y_shape9 >= 750 or y_shape9 <= 0:
      direction9_y *= -1
    if x_shape10 >= 1150 or x_shape10 <= 50:
      direction10_x *= -1
    if y_shape10 >= 750 or y_shape10 <= 50:
      direction10_y *= -1
    if x_shape11 >= 1150 or x_shape11 <= 50:
      direction11_x *= -1
    if y_shape11 >= 750 or y_shape11 <= 50:
      direction11_y *= -1
    #draw the shape
    pygame.draw.rect(gameDisplay, grey, (0, 0, x, y))
    pygame.draw.circle(gameDisplay, colour1, (x_shape1, y_shape1), 50)
    pygame.draw.rect(gameDisplay, red, (x_shape2, y_shape2, 100, 50))
    pygame.draw.circle(gameDisplay, colour2, (x_shape3, y_shape3), 50)
    pygame.draw.rect(gameDisplay, red, (x_shape4, y_shape4, 100, 50))
    pygame.draw.circle(gameDisplay, colour3, (x_shape5, y_shape5), 50)
    pygame.draw.rect(gameDisplay, red, (x_shape6, y_shape6, 100, 50))
    pygame.draw.rect(gameDisplay, red, (x_shape7, y_shape7, 100, 50))
    pygame.draw.circle(gameDisplay, colour4, (x_shape8, y_shape8), 50)
    pygame.draw.rect(gameDisplay, red, (x_shape9, y_shape9, 100, 50))
    pygame.draw.circle(gameDisplay, colour5, (x_shape10, y_shape10), 50)
    pygame.draw.circle(gameDisplay, colour6, (x_shape11, y_shape11), 50)
    #check if the shape has been clicked on
    if mousepos[0] > x_shape1 - 50 and mousepos[0] < x_shape1 + 50 and mousepos[1] > y_shape1 - 50 and mousepos[1] < y_shape1 + 50:
      if event.type == pygame.MOUSEBUTTONDOWN:
        #check if shape has been clicked
        if colour1 != white:
          #turn white and slow down
          colour1 = white
          direction1_x = 0.5
          direction1_y = 0.5
          game_score += 1
          pygame.display.update()
    if mousepos[0] > x_shape2 - 50 and mousepos[0] < x_shape2 + 50 and mousepos[1] > y_shape2 - 50 and mousepos[1] < y_shape2 + 50:
      if event.type == pygame.MOUSEBUTTONDOWN:
        #make sure game score doesnt become negative
        if game_score >= 3:
          game_score -= 3
        else:
          game_score = 0
    if mousepos[0] > x_shape4 - 50 and mousepos[0] < x_shape4 + 50 and mousepos[1] > y_shape4 - 50 and mousepos[1] < y_shape4 + 50:
      if event.type == pygame.MOUSEBUTTONDOWN:
        #make sure game score doesnt ecome negative
        if game_score >= 3:
          game_score -= 3
        else:
          game_score = 0
    if mousepos[0] > x_shape3 - 50 and mousepos[0] < x_shape3 + 50 and mousepos[1] > y_shape3 - 50 and mousepos[1] < y_shape3 + 50:
      if event.type == pygame.MOUSEBUTTONDOWN:
        #check if shape has been clicked on
        if colour2 != white:
          #turn whtie and slow down
          colour2 = white
          direction3_x = 0.5
          direction3_y = 0.5
          game_score += 3
          pygame.display.update()
    if mousepos[0] > x_shape5 - 50 and mousepos[0] < x_shape5 + 50 and mousepos[1] > y_shape5 - 50 and mousepos[1] < y_shape5 + 50:
      if event.type == pygame.MOUSEBUTTONDOWN:
        #check if shape has been clicked on
        if colour3 != white:
          #turn white and slow down
          colour3 = white
          direction5_x = 0.5
          direction5_y = 0.5
          game_score += 10
          pygame.display.update()
    if mousepos[0] > x_shape6 - 50 and mousepos[0] < x_shape6 + 50 and mousepos[1] > y_shape6 - 50 and mousepos[1] < y_shape6 + 50:
      if event.type == pygame.MOUSEBUTTONDOWN:
        #make sure game score doent become negative
        if game_score >= 3:
          game_score -= 3
        else:
          game_score = 0
    if mousepos[0] > x_shape7 - 50 and mousepos[0] < x_shape7 + 50 and mousepos[1] > y_shape7 - 50 and mousepos[1] < y_shape7 + 50:
      if event.type == pygame.MOUSEBUTTONDOWN:
        #maek sure game score doesnt become negative
        if game_score >= 3:
          game_score -= 3
        else:
          game_score = 0
    if mousepos[0] > x_shape8 - 50 and mousepos[0] < x_shape8 + 50 and mousepos[1] > y_shape8 - 50 and mousepos[1] < y_shape8 + 50:
      if event.type == pygame.MOUSEBUTTONDOWN:
        #check if shape has been clicked on
        if colour4 != white:
          #turn white and slow down
          colour4 = white
          direction8_x = 0.5
          direction8_y = 0.5
          game_score += 2
    if mousepos[0] > x_shape9 - 50 and mousepos[0] < x_shape9 + 50 and mousepos[1] > y_shape9 - 50 and mousepos[1] < y_shape9 + 50:
      if event.type == pygame.MOUSEBUTTONDOWN:
        #make sure game score doesnt become negative
        if game_score >= 3:
          game_score -= 3
        else:
          game_score = 0
    if mousepos[0] > x_shape10 - 50 and mousepos[0] < x_shape10 + 50 and mousepos[1] > y_shape10 - 50 and mousepos[1] < y_shape10 + 50:
      if event.type == pygame.MOUSEBUTTONDOWN:
        #make sure shape hasnt already been clicked
        if colour5 != white:
          colour5 = white
          direction10_x = 0.5
          direction10_y = 0.5
          game_score += 25
          pygame.display.update()
    if mousepos[0] > x_shape11 - 50 and mousepos[0] < x_shape11 + 50 and mousepos[1] > y_shape11 - 50 and mousepos[1] < y_shape11 + 50:
      if event.type == pygame.MOUSEBUTTONDOWN:
        #make sure shape hasnt already been clicked
        if colour6 != white:
          colour6 = white
          direction11_x = 0.5
          direction11_y = 0.5
          game_score += 3
    #show current score
    displaytext(("Score: " + str(game_score)), blue, bigfont, 0, 0)
    pygame.display.update()
    clock.tick(60)

def finishlevel8():
  finish8 = True
  while finish8:
    for event in pygame.event.get():
      print(event)
      if event.type == pygame.QUIT:
        pygame.quit()
        exit()
    #maek background
    gameDisplay.blit(level8completion_background, (0, 0))
    #make button
    button("Continue", 100, 50, 1100, 750, black, grey, "startlevel9")
    pygame.display.update()
    clock.tick(60) 

def playlevel9():
  #import and declare variables
  global grey
  global blue
  global green
  global x
  global y
  global pink
  global purple
  global yellow
  global cyan
  global orange
  colour1 = blue
  colour2 = green
  colour3 = pink
  colour4 = purple
  colour5 = yellow
  colour6 = cyan
  colour7 = orange
  global game_score
  global red
  global white
  playing_game9 = True
  #generate starting positions
  x_shape1 = random.randint(50,1150)
  y_shape1 = random.randint(50,750)
  x_shape2 = random.randint(0,1100)
  y_shape2 = random.randint(0,750)
  x_shape3 = random.randint(50, 1150)
  y_shape3 = random.randint(50, 750)
  x_shape4 = random.randint(0,1100)
  y_shape4 = random.randint(0,750)
  x_shape5 = random.randint(50, 1150)
  y_shape5 = random.randint(50,750)
  x_shape6 = random.randint(0,1100)
  y_shape6 = random.randint(0,750)
  x_shape7 = random.randint(0,1100)
  y_shape7 = random.randint(0,750)
  x_shape8 = random.randint(50,1150)
  y_shape8 = random.randint(50,750)
  x_shape9 = random.randint(0,1100)
  y_shape9 = random.randint(0,750)
  x_shape10 = random.randint(50,1150)
  y_shape10 = random.randint(50,750)
  x_shape11 = random.randint(50,1150)
  y_shape11 = random.randint(50,750)
  x_shape12 = random.randint(50,1150)
  y_shape12 = random.randint(50,750)
  #generate velocities
  direction1_x = random.randint(1, 5)
  direction1_y = random.randint(1, 5)
  direction2_x = random.randint(1, 7)
  direction2_y = random.randint(1, 7)
  direction3_x = random.randint(1, 7)
  direction3_y = random.randint(1, 3)
  direction4_x = random.randint(1, 9)
  direction4_y = random.randint(1, 9)
  direction5_x = random.randint(5, 13)
  direction5_y = random.randint(5, 13)
  direction6_x = random.randint(1, 11)
  direction6_y = random.randint(1, 11)
  direction7_x = random.randint(1, 11)
  direction7_y = random.randint(1, 11)
  direction8_x = random.randint(1, 3)
  direction8_y = random.randint(1, 3)
  direction9_x = random.randint(1, 13)
  direction9_y = random.randint(1, 13)
  direction10_x = random.randint(18, 25)
  direction10_y = random.randint(18, 25)
  direction11_x = random.randint(1, 7)
  direction11_y = random.randint(1, 7)
  direction12_x = random.randint(1, 7)
  direction12_y = random.randint(1, 7)
  #game loop
  while playing_game9:
    for event in pygame.event.get():
      print(event)
      if event.type == pygame.QUIT:
        pygame.quit()
        exit()
    #check if all shapes are clicked
    if colour1 == white and colour2 == white and colour3 == white and colour4 == white and colour6 == white and colour7 == white:
      displaytext(("Score: " + str(game_score)), blue, bigfont, 0, 0)
      pygame.draw.circle(gameDisplay, white, (x_shape1, y_shape1), 50)
      pygame.draw.circle(gameDisplay, white, (x_shape3, y_shape3), 50)
      pygame.draw.circle(gameDisplay, white, (x_shape5, y_shape5), 50)
      pygame.draw.circle(gameDisplay, white, (x_shape8, y_shape8), 50)
      pygame.draw.circle(gameDisplay, white, (x_shape11, y_shape11), 50)
      pygame.draw.circle(gameDisplay, white, (x_shape12, y_shape12), 50)
      pygame.display.update()
      pygame.time.delay(1000)
      finishlevel9()
    mousepos = pygame.mouse.get_pos() #current position of mouse
    x_shape1 += direction1_x #update the x position of shape 1
    y_shape1 += direction1_y #update the y position of shape 1
    x_shape2 += direction2_x #update the x position of shape 2
    y_shape2 += direction2_y #update the y position of shape 2
    x_shape3 += direction3_x #update the x position of shape 3
    y_shape3 += direction3_y #update the y position of shape 3
    x_shape4 += direction4_x #update the x position of shape 4
    y_shape4 += direction4_y #update the y position of shape 4
    x_shape5 += direction5_x #update the x position of shape 5
    y_shape5 += direction5_y #update the y position of shape 5
    x_shape6 += direction6_x #update the x position of shape 6
    y_shape6 += direction6_y #update the y position of shape 6
    x_shape7 += direction7_x #update the x position of shape 7
    y_shape7 += direction7_y #update the y position of shape 7
    x_shape8 += direction8_x #update the x position of shape 8
    y_shape8 += direction8_y #update the y position of shape 8
    x_shape9 += direction9_x #update the x position of shape 9
    y_shape9 += direction9_y #update the y position of shape 9
    x_shape10 += direction10_x #update the x position of shape 10
    y_shape10 += direction10_y #update the y position of shape 10
    x_shape11 += direction11_x #update the x position of shape 10
    y_shape11 += direction11_y #update the y position of shape 10
    x_shape12 += direction12_x #update the x position of shape 10
    y_shape12 += direction12_y #update the y position of shape 10
    #make shapes bounce
    if x_shape1 >= 1150 or x_shape1 <= 50:
      direction1_x *= -1
    if y_shape1 >= 750 or y_shape1 <= 50:
      direction1_y *= -1
    if x_shape2 >= 1100 or x_shape2 <= 0:
      direction2_x *= -1
    if y_shape2 >= 750 or y_shape2 <= 0:
      direction2_y *= -1
    if x_shape3 >= 1150 or x_shape3 <= 50:
      direction3_x *= -1
    if y_shape3 >= 750 or y_shape3 <= 50:
      direction3_y *= -1
    if x_shape4 >= 1100 or x_shape4 <= 0:
      direction4_x *= -1
    if y_shape4 >= 750 or y_shape4 <= 0:
      direction4_y *= -1
    if x_shape5 >= 1150 or x_shape5 <= 50:
      direction5_x *= -1
    if y_shape5 >= 750 or y_shape5 <= 50:
      direction5_y *= -1
    if x_shape6 >= 1100 or x_shape6 <= 0:
      direction6_x *= -1 
    if y_shape6 >= 750 or y_shape6 <= 0:
      direction6_y *= -1
    if x_shape7 >= 1100 or x_shape7 <= 0:
      direction7_x *= -1 
    if y_shape7 >= 750 or y_shape7 <= 0:
      direction7_y *= -1  
    if x_shape8 >= 1150 or x_shape8 <= 50:
      direction8_x *= -1
    if y_shape8 >= 750 or y_shape8 <= 50:
      direction8_y *= -1
    if x_shape9 >= 1100 or x_shape9 <= 0:
      direction9_x *= -1
    if y_shape9 >= 750 or y_shape9 <= 0:
      direction9_y *= -1
    if x_shape10 >= 1150 or x_shape10 <= 50:
      direction10_x *= -1
    if y_shape10 >= 750 or y_shape10 <= 50:
      direction10_y *= -1
    if x_shape11 >= 1150 or x_shape11 <= 50:
      direction11_x *= -1
    if y_shape11 >= 750 or y_shape11 <= 50:
      direction11_y *= -1
    if x_shape12 >= 1150 or x_shape12 <= 50:
      direction12_x *= -1
    if y_shape12 >= 750 or y_shape12 <= 50:
      direction12_y *= -1
    #draw the shape
    pygame.draw.rect(gameDisplay, grey, (0, 0, x, y))
    pygame.draw.circle(gameDisplay, colour1, (x_shape1, y_shape1), 50)
    pygame.draw.rect(gameDisplay, red, (x_shape2, y_shape2, 100, 50))
    pygame.draw.circle(gameDisplay, colour2, (x_shape3, y_shape3), 50)
    pygame.draw.rect(gameDisplay, red, (x_shape4, y_shape4, 100, 50))
    pygame.draw.circle(gameDisplay, colour3, (x_shape5, y_shape5), 50)
    pygame.draw.rect(gameDisplay, red, (x_shape6, y_shape6, 100, 50))
    pygame.draw.rect(gameDisplay, red, (x_shape7, y_shape7, 100, 50))
    pygame.draw.circle(gameDisplay, colour4, (x_shape8, y_shape8), 50)
    pygame.draw.rect(gameDisplay, red, (x_shape9, y_shape9, 100, 50))
    pygame.draw.circle(gameDisplay, colour5, (x_shape10, y_shape10), 50)
    pygame.draw.circle(gameDisplay, colour6, (x_shape11, y_shape11), 50)
    pygame.draw.circle(gameDisplay, colour7, (x_shape12, y_shape12), 50)
    #check if the shape has been clicked on
    if mousepos[0] > x_shape1 - 50 and mousepos[0] < x_shape1 + 50 and mousepos[1] > y_shape1 - 50 and mousepos[1] < y_shape1 + 50:
      if event.type == pygame.MOUSEBUTTONDOWN:
        #make sure shape hasnt already been clicked
        if colour1 != white:
          colour1 = white
          direction1_x = 0.5
          direction1_y = 0.5
          game_score += 1
          pygame.display.update()
    if mousepos[0] > x_shape2 - 50 and mousepos[0] < x_shape2 + 50 and mousepos[1] > y_shape2 - 50 and mousepos[1] < y_shape2 + 50:
      if event.type == pygame.MOUSEBUTTONDOWN:
        #check to maek sure gme score doesnt become negative
        if game_score >= 3:
          game_score -= 3
        else:
          game_score = 0
    if mousepos[0] > x_shape4 - 50 and mousepos[0] < x_shape4 + 50 and mousepos[1] > y_shape4 - 50 and mousepos[1] < y_shape4 + 50:
      if event.type == pygame.MOUSEBUTTONDOWN:
        #make sure game score doesnt become negative
        if game_score >= 3:
          game_score -= 3
        else:
          game_score = 0
    if mousepos[0] > x_shape3 - 50 and mousepos[0] < x_shape3 + 50 and mousepos[1] > y_shape3 - 50 and mousepos[1] < y_shape3 + 50:
      if event.type == pygame.MOUSEBUTTONDOWN:
        if colour2 != white:
          #maek sure shape hasnt already been clicked
          colour2 = white
          direction3_x = 0.5
          direction3_y = 0.5
          game_score += 3
          pygame.display.update()
    if mousepos[0] > x_shape5 - 50 and mousepos[0] < x_shape5 + 50 and mousepos[1] > y_shape5 - 50 and mousepos[1] < y_shape5 + 50:
      if event.type == pygame.MOUSEBUTTONDOWN:
        if colour3 != white:
          #maek sure shape hasnt already been clicked
          colour3 = white
          direction5_x = 0.5
          direction5_y = 0.5
          game_score += 10
          pygame.display.update()
    if mousepos[0] > x_shape6 - 50 and mousepos[0] < x_shape6 + 50 and mousepos[1] > y_shape6 - 50 and mousepos[1] < y_shape6 + 50:
      if event.type == pygame.MOUSEBUTTONDOWN:
        #maek sure game score doesnt become negative
        if game_score >= 3:
          game_score -= 3
        else:
          game_score = 0
    if mousepos[0] > x_shape7 - 50 and mousepos[0] < x_shape7 + 50 and mousepos[1] > y_shape7 - 50 and mousepos[1] < y_shape7 + 50:
      if event.type == pygame.MOUSEBUTTONDOWN:
        #make sure game score deosnt becom negative
        if game_score >= 3:
          game_score -= 3
        else:
          game_score = 0
    if mousepos[0] > x_shape8 - 50 and mousepos[0] < x_shape8 + 50 and mousepos[1] > y_shape8 - 50 and mousepos[1] < y_shape8 + 50:
      if event.type == pygame.MOUSEBUTTONDOWN:
        if colour4 != white:
          #maek sure shape hasnt already been clicked
          colour4 = white
          direction8_x = 0.5
          direction8_y = 0.5
          game_score += 2
    if mousepos[0] > x_shape9 - 50 and mousepos[0] < x_shape9 + 50 and mousepos[1] > y_shape9 - 50 and mousepos[1] < y_shape9 + 50:
      if event.type == pygame.MOUSEBUTTONDOWN:
        #make sure gamescore doesnt become negative
        if game_score >= 3:
          game_score -= 3
        else:
          game_score = 0
    if mousepos[0] > x_shape10 - 50 and mousepos[0] < x_shape10 + 50 and mousepos[1] > y_shape10 - 50 and mousepos[1] < y_shape10 + 50:
      if event.type == pygame.MOUSEBUTTONDOWN:
        if colour5 != white:
          #maek sure shape hasnt already been clicked
          colour5 = white
          direction10_x = 0.5
          direction10_y = 0.5
          game_score += 25
          pygame.display.update()
    if mousepos[0] > x_shape11 - 50 and mousepos[0] < x_shape11 + 50 and mousepos[1] > y_shape11 - 50 and mousepos[1] < y_shape11 + 50:
      if event.type == pygame.MOUSEBUTTONDOWN:
        if colour6 != white:
          #maek sure shape hasnt already been clicked
          colour6 = white
          direction11_x = 0.5
          direction11_y = 0.5
          game_score += 3
    if mousepos[0] > x_shape12 - 50 and mousepos[0] < x_shape12 + 50 and mousepos[1] > y_shape12 - 50 and mousepos[1] < y_shape12 + 50:
      if event.type == pygame.MOUSEBUTTONDOWN:
        if colour7 != white:
          #maek sure shape hasnt already been clicked
          colour7 = white
          direction12_x = 0.5
          direction12_y = 0.5
          game_score += 3
          pygame.display.update()
    #show score
    displaytext(("Score: " + str(game_score)), blue, bigfont, 0, 0)
    pygame.display.update()
    clock.tick(60)

def finishlevel9():
  finish9 = True
  while finish9:
    for event in pygame.event.get():
      print(event)
      if event.type == pygame.QUIT:
        pygame.quit()
        exit()
    #make background
    gameDisplay.blit(level9completion_background, (0, 0))
    #make button
    button("Continue", 100, 50, 1100, 750, black, grey, "startlevel10")
    pygame.display.update()
    clock.tick(60)

def playlevel10():
  #import and declare variables
  global grey
  global blue
  global green
  global x
  global y
  global pink
  global purple
  global yellow
  global cyan
  global orange
  global black
  colour1 = black
  global game_score
  global red
  global white
  playing_game10 = True
  #generate starting positions
  x_shape1 = random.randint(50,1150)
  y_shape1 = random.randint(50,750)
  x_shape2 = random.randint(0,1100)
  y_shape2 = random.randint(0,750)
  x_shape3 = random.randint(0,1100)
  y_shape3 = random.randint(0,750)
  x_shape4 = random.randint(0,1100)
  y_shape4 = random.randint(0,750)
  x_shape5 = random.randint(0,1100)
  y_shape5 = random.randint(0,750)
  x_shape6 = random.randint(0,1100)
  y_shape6 = random.randint(0,750)
  x_shape7 = random.randint(0,1100)
  y_shape7 = random.randint(0,750)
  x_shape8 = random.randint(0,1100)
  y_shape8 = random.randint(0,750)
  x_shape9 = random.randint(0,1100)
  y_shape9 = random.randint(0,750)
  x_shape10 = random.randint(0,1100)
  y_shape10 = random.randint(0,750)
  x_shape11 = random.randint(0,1100)
  y_shape11 = random.randint(0,750)
  x_shape12 = random.randint(0,1100)
  y_shape12 = random.randint(0,750)
  #generate velocities
  direction1_x = 30
  direction1_y = 30
  direction2_x = 5
  direction2_y = 5
  direction3_x = 5
  direction3_y = 5
  direction4_x = 5
  direction4_y = 5
  direction5_x = 5
  direction5_y = 5
  direction6_x = 5
  direction6_y = 5
  direction7_x = 5
  direction7_y = 5
  direction8_x = 5
  direction8_y = 5
  direction9_x = 5
  direction9_y = 5
  direction10_x = 5
  direction10_y = 5
  direction11_x = 5
  direction11_y = 5
  direction12_x = 5
  direction12_y = 5
  #game loop
  while playing_game10:
    for event in pygame.event.get():
      print(event)
      if event.type == pygame.QUIT:
        pygame.quit()
        exit()
    if colour1 == white:
      displaytext(("Score: " + str(game_score)), blue, bigfont, 0, 0)
      pygame.draw.circle(gameDisplay, white, (x_shape1, y_shape1), 30)
      pygame.display.update()
      pygame.time.delay(1000)
      finishlevel10()
    mousepos = pygame.mouse.get_pos() #current position of mouse
    x_shape1 += direction1_x #update the x position of shape 1
    y_shape1 += direction1_y #update the y position of shape 1
    x_shape2 += direction2_x #update the x position of shape 2
    y_shape2 += direction2_y #update the y position of shape 2
    x_shape3 += direction3_x #update the x position of shape 3
    y_shape3 += direction3_y #update the y position of shape 3
    x_shape4 += direction4_x #update the x position of shape 4
    y_shape4 += direction4_y #update the y position of shape 4
    x_shape5 += direction5_x #update the x position of shape 5
    y_shape5 += direction5_y #update the y position of shape 5
    x_shape6 += direction6_x #update the x position of shape 6
    y_shape6 += direction6_y #update the y position of shape 6
    x_shape7 += direction7_x #update the x position of shape 7
    y_shape7 += direction7_y #update the y position of shape 7
    x_shape8 += direction8_x #update the x position of shape 8
    y_shape8 += direction8_y #update the y position of shape 8
    x_shape9 += direction9_x #update the x position of shape 9
    y_shape9 += direction9_y #update the y position of shape 9
    x_shape10 += direction10_x #update the x position of shape 10
    y_shape10 += direction10_y #update the y position of shape 10
    x_shape11 += direction11_x #update the x position of shape 10
    y_shape11 += direction11_y #update the y position of shape 10
    x_shape12 += direction12_x #update the x position of shape 10
    y_shape12 += direction12_y #update the y position of shape 10
    if x_shape1 >= 1170 or x_shape1 <= 30:
      direction1_x *= -1
    if y_shape1 >= 750 or y_shape1 <= 50:
      direction1_y *= -1
    if x_shape2 >= 1100 or x_shape2 <= 0:
      direction2_x *= -1
    if y_shape2 >= 750 or y_shape2 <= 0:
      direction2_y *= -1
    if x_shape3 >= 1100 or x_shape3 <= 0:
      direction3_x *= -1
    if y_shape3 >= 750 or y_shape3 <= 0:
      direction3_y *= -1
    if x_shape4 >= 1100 or x_shape4 <= 0:
      direction4_x *= -1
    if y_shape4 >= 750 or y_shape4 <= 0:
      direction4_y *= -1
    if x_shape5 >= 1100 or x_shape5 <= 0:
      direction5_x *= -1
    if y_shape5 >= 750 or y_shape5 <= 0:
      direction5_y *= -1
    if x_shape6 >= 1100 or x_shape6 <= 0:
      direction6_x *= -1
    if y_shape6 >= 750 or y_shape6 <= 0:
      direction6_y *= -1
    if x_shape7 >= 1100 or x_shape7 <= 0:
      direction7_x *= -1
    if y_shape7 >= 750 or y_shape7 <= 0:
      direction7_y *= -1
    if x_shape8 >= 1100 or x_shape8 <= 0:
      direction8_x *= -1
    if y_shape8 >= 750 or y_shape8 <= 0:
      direction8_y *= -1
    if x_shape9 >= 1100 or x_shape9 <= 0:
      direction9_x *= -1
    if y_shape9 >= 750 or y_shape9 <= 0:
      direction9_y *= -1
    if x_shape10 >= 1100 or x_shape10 <= 0:
      direction10_x *= -1
    if y_shape10 >= 750 or y_shape10 <= 0:
      direction10_y *= -1
    if x_shape11 >= 1100 or x_shape11 <= 0:
      direction11_x *= -1
    if y_shape11 >= 750 or y_shape11 <= 0:
      direction11_y *= -1
    if x_shape12 >= 1100 or x_shape12 <= 0:
      direction12_x *= -1
    if y_shape12 >= 750 or y_shape12 <= 0:
      direction12_y *= -1
    #draw the shape
    pygame.draw.rect(gameDisplay, grey, (0, 0, x, y))
    pygame.draw.circle(gameDisplay, colour1, (x_shape1, y_shape1), 30)
    pygame.draw.rect(gameDisplay, red, (x_shape2, y_shape2, 100, 50))
    pygame.draw.rect(gameDisplay, red, (x_shape3, y_shape3, 100, 50))
    pygame.draw.rect(gameDisplay, red, (x_shape4, y_shape4, 100, 50))
    pygame.draw.rect(gameDisplay, red, (x_shape5, y_shape5, 100, 50))
    pygame.draw.rect(gameDisplay, red, (x_shape6, y_shape6, 100, 50))
    pygame.draw.rect(gameDisplay, red, (x_shape7, y_shape7, 100, 50))
    pygame.draw.rect(gameDisplay, red, (x_shape8, y_shape8, 100, 50))
    pygame.draw.rect(gameDisplay, red, (x_shape9, y_shape9, 100, 50))
    pygame.draw.rect(gameDisplay, red, (x_shape10, y_shape10, 100, 50))
    pygame.draw.rect(gameDisplay, red, (x_shape11, y_shape11, 100, 50))
    pygame.draw.rect(gameDisplay, red, (x_shape12, y_shape12, 100, 50))
    #check if the shape has been clicked on
    if mousepos[0] > x_shape1 - 30 and mousepos[0] < x_shape1 + 30 and mousepos[1] > y_shape1 - 30 and mousepos[1] < y_shape1 + 30:
      if event.type == pygame.MOUSEBUTTONDOWN:
        if colour1 != white:
          colour1 = white
          direction1_x = 0.5
          direction1_y = 0.5
          game_score += 100
          pygame.display.update()
    if mousepos[0] > x_shape2 - 50 and mousepos[0] < x_shape2 + 50 and mousepos[1] > y_shape2 - 50 and mousepos[1] < y_shape2 + 50:
      if event.type == pygame.MOUSEBUTTONDOWN:
        if game_score >= 3:
          game_score -= 3
        else:
          game_score = 0
    if mousepos[0] > x_shape3 - 50 and mousepos[0] < x_shape3 + 50 and mousepos[1] > y_shape3 - 50 and mousepos[1] < y_shape3+ 50:
      if event.type == pygame.MOUSEBUTTONDOWN:
        if game_score >= 3:
          game_score -= 3
        else:
          game_score = 0
    if mousepos[0] > x_shape4 - 50 and mousepos[0] < x_shape4 + 50 and mousepos[1] > y_shape4 - 50 and mousepos[1] < y_shape4 + 50:
      if event.type == pygame.MOUSEBUTTONDOWN:
        if game_score >= 3:
          game_score -= 3
        else:
          game_score = 0
    if mousepos[0] > x_shape5 - 50 and mousepos[0] < x_shape5 + 50 and mousepos[1] > y_shape5 - 50 and mousepos[1] < y_shape5 + 50:
      if event.type == pygame.MOUSEBUTTONDOWN:
        if game_score >= 3:
          game_score -= 3
        else:
          game_score = 0
    if mousepos[0] > x_shape6 - 50 and mousepos[0] < x_shape6 + 50 and mousepos[1] > y_shape6 - 50 and mousepos[1] < y_shape6 + 50:
      if event.type == pygame.MOUSEBUTTONDOWN:
        if game_score >= 3:
          game_score -= 3
        else:
          game_score = 0
    if mousepos[0] > x_shape7 - 50 and mousepos[0] < x_shape7 + 50 and mousepos[1] > y_shape7 - 50 and mousepos[1] < y_shape7 + 50:
      if event.type == pygame.MOUSEBUTTONDOWN:
        if game_score >= 3:
          game_score -= 3
        else:
          game_score = 0
    if mousepos[0] > x_shape8 - 50 and mousepos[0] < x_shape8 + 50 and mousepos[1] > y_shape8 - 50 and mousepos[1] < y_shape8 + 50:
      if event.type == pygame.MOUSEBUTTONDOWN:
        if game_score >= 3:
          game_score -= 3
        else:
          game_score = 0
    if mousepos[0] > x_shape9 - 50 and mousepos[0] < x_shape9 + 50 and mousepos[1] > y_shape9 - 50 and mousepos[1] < y_shape9 + 50:
      if event.type == pygame.MOUSEBUTTONDOWN:
        if game_score >= 3:
          game_score -= 3
        else:
          game_score = 0
    if mousepos[0] > x_shape10 - 50 and mousepos[0] < x_shape10 + 50 and mousepos[1] > y_shape10 - 50 and mousepos[1] < y_shape10 + 50:
      if event.type == pygame.MOUSEBUTTONDOWN:
        if game_score >= 3:
          game_score -= 3
        else:
          game_score = 0
    if mousepos[0] > x_shape11 - 50 and mousepos[0] < x_shape11 + 50 and mousepos[1] > y_shape11 - 50 and mousepos[1] < y_shape11 + 50:
      if event.type == pygame.MOUSEBUTTONDOWN:
        if game_score >= 3:
          game_score -= 3
        else:
          game_score = 0
    if mousepos[0] > x_shape12 - 50 and mousepos[0] < x_shape12 + 50 and mousepos[1] > y_shape12 - 50 and mousepos[1] < y_shape12 + 50:
      if event.type == pygame.MOUSEBUTTONDOWN:
        if game_score >= 3:
          game_score -= 3
        else:
          game_score = 0
    displaytext(("Score: " + str(game_score)), blue, bigfont, 0, 0)
    pygame.display.update()
    clock.tick(60)

def finishlevel10():
  finish10 = True
  global highscore
  global game_score
  if game_score > highscore:
    highscore = game_score
  while finish10:
    for event in pygame.event.get():
      print(event)
      if event.type == pygame.QUIT:
        pygame.quit()
        exit()
    gameDisplay.blit(level10completion_background, (0, 0))
    button("Continue", 100, 50, 1100, 750, black, grey, "endgame")
    pygame.display.update()
    clock.tick(60) 

def displayfinalscore():
  displayingscore = True
  while displayingscore:
    for event in pygame.event.get():
      print(event)
      if event.type == pygame.QUIT:
        pygame.quit()
        exit()
    displaytext("Your final score: " + str(game_score), black, bigfont, 375, 400)
    displaytext("High Score: " + str(highscore), black, bigfont, 425, 600)
    button("Finish", 100, 50, 1100, 750, black, grey, "return")
    pygame.display.update()
    clock.tick(60) 

titlescreen()