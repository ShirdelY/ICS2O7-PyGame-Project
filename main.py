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
icon = pygame.image.load("angrycircle.png")
pygame.display.set_icon(icon)

#initialize the backgrounds
titlescreen_background = pygame.











#fonts
bigfont = pygame.font.SysFont("arial",50)
smallfont = pygame.font.SysFont("arial",15)