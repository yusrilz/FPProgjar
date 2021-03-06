from ctypes import Union
from types import FunctionType
import pygame

NoneType = type(None)

class Button:
    def __init__(self, surface: 'pygame.Surface', x: 'int', y: 'int', width: 'int', height: 'int', text: 'str') -> None:
        self.__surface = surface
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height
        self.__color = (255, 0, 0)
        self.__font_color = (255, 255, 255)
        self.__text = text
        self.__rect = pygame.Rect(
            self.__x, self.__y, self.__width, self.__height)
        self.__font = pygame.font.SysFont('Times New Roman', 50)
        self.__click_handler: 'Union[FunctionType, NoneType]' = None

    def draw(self):
        text = self.__font.render(self.__text, True, self.__font_color)
        textRect = text.get_rect()
        textRect.center = self.__rect.center
        self.__surface.blit(text, textRect)
        pygame.draw.rect(self.__surface, self.__color, self.__rect,  2)

    def handle_event(self, events: 'list[pygame.event.Event]'):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.__handle_click(event)

    def __handle_click(self, event: 'pygame.event.Event'):
        (click_x, click_y) = event.pos
        if click_x < self.__x or click_x > (self.__x + self.__width) or click_y < self.__y or click_y > (self.__y + self.__height) or type(self.__click_handler) == NoneType:
            return
        self.__click_handler()

    def set_click_handler(self, handler: 'FunctionType'):
        self.__click_handler = handler

class Grid:
    def __init__(self, surface: 'pygame.Surface', startx: 'int', starty: 'int', endx: 'int', endy: 'int', width: 'int') -> None:
        self.__surface = surface
        self.__startx = startx
        self.__starty = starty
        self.__endx = endx
        self.__endy = endy
        self.__width = width
        self.__color = (255,0,0)

    def draw(self):
        pygame.draw.line(self.__surface,self.__color,(self.__startx,self.__starty),(self.__endx,self.__endy),self.__width)

    
