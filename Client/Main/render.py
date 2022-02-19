
import json
import pygame

class Render:
    listok = []
    @classmethod
    def init(cls, read_file):
        with open(read_file, "r") as read_file2:
            cls.data = json.load(read_file2)

    @classmethod
    def rects(cls, map_name):
        for i in cls.data[map_name]:
            cls.listok.append(pygame.Rect(i))

    @classmethod
    def render(cls, map_name, window, color):
        for i in cls.listok:
            pygame.draw.rect(window, color, i)

    @classmethod
    def intersection(cls, rect):
        for i in cls.listok:
            if rect.colliderect(i):
                return True
        return False

    @classmethod
    def render_name(cls):
        return [i for i in cls.data]
