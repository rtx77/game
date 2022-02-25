import pygame
import json
from PyQt5.QtWidgets import QApplication
from Windowidjet import Example
import Windowidjet
import sys
import os.path

pygame.init()
dis = pygame.display.set_mode((1000, 600))
# dis.fill("white")

pygame.display.set_caption('Map generator')

GREEN = (0, 255, 0)

Windowidjet.map_name = '.'

if not os.path.exists("file.txt"):
    with open('file.txt', 'a') as fw:
        fw.write("{\x22.\x22:[[]]")
else:
    with open("file.txt", 'rb+') as filehandle:
        filehandle.seek(-1, os.SEEK_END)
        filehandle.truncate()

class Rect:
    rect_coordinate_list = []
    def __init__(self, position):
        self.__position = position

    def helpf(self, second_position):
        coords = (self.__position[0], self.__position[1],
                                      second_position[0] - self.__position[0],
                                      second_position[1] - self.__position[1])
        pygame.draw.rect(dis, GREEN, coords)
        self.rect_coordinate_list.append(coords)

    def draw(self, second_position):
        if self.__position[0] > second_position[0] and self.__position[1] < second_position[1]:
            k = self.__position[0]
            self.__position[0] = second_position[0]
            second_position[0] = k
        if self.__position[0] < second_position[0] and self.__position[1] > second_position[1]:
            k = self.__position[1]
            self.__position[1] = second_position[1]
            second_position[1] = k
        if self.__position[0] > second_position[0] and self.__position[1] > second_position[1]:
            k = self.__position
            self.__position = second_position
            second_position = k
        self.helpf(second_position)

switch = False
game_over = False
dop_window = True
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and dop_window:
            dop_window = False
            app = QApplication(sys.argv)
            ex = Example()
            app.exec_()
            del app

        if event.type == pygame.KEYUP:
            with open('file.txt', 'a') as fw:
                fw.write(",\x22" + Windowidjet.map_name + "\x22:")
                json.dump(Rect.rect_coordinate_list, fw)

        if event.type == pygame.QUIT:
            with open('file.txt', 'a') as fw:
                fw.write("}")
            game_over = True
        if event.type == pygame.MOUSEBUTTONUP:
            print(event.pos)
            if switch:
                rect.draw(list(event.pos))
            else:
                firstclick_mouse_position = pygame.mouse.get_pos()
                rect = Rect(list(firstclick_mouse_position))
            switch = not switch
    pygame.display.update()
pygame.quit()
quit()