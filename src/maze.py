import pygame
import random


class Maze:
    def __init__(self, level_data, step):

        # Инициализация лабиринта с уровнем данных и размером шага клетки
        self.step = step
        self.level_data = level_data

        # Цвет стен
        self.wall_color = (255, 0, 0)

        # Цвет пола
        self.floor_color = (0, 255, 0)

        # Отступ для отображения лабиринта на экране
        self.otstup = 160

    def draw(self, screen):

        # Метод для отрисовки лабиринта на экране
        for y, row in enumerate(self.level_data):
            for x, tile in enumerate(row):

                # Если клетка - стена, рисуем стену
                if tile == '#':
                    pygame.draw.rect(screen, self.wall_color, (x * self.step + self.step, y * self.step + self.otstup, self.otstup , self.step))
                
                # Если клетка - пустое пространство, рисуем пол
                elif tile == ' ':
                    pygame.draw.rect(screen, self.floor_color, (x * self.step + self.step, y * self.step + self.otstup, self.otstup, self.step))

    def test_place(self, x, y):

        # Метод для проверки, можно ли переместиться в указанную клетку (x, y)
        # Возвращает True, если клетка доступна (не стена), иначе False
        i_x = (x - self.step) // self.step
        i_y = (y - self.otstup) // self.step
        return self.level_data[i_y][i_x] != '#'

    def get_free_place(self):

        # Метод для получения случайной свободной клетки в лабиринте
        cods = []
        for y, row in enumerate(self.level_data):
            for x, tile in enumerate(row):
                if tile != '#':
                    cods.append((x, y))
        x, y = random.choice(cods)
        return (x * self.step + self.step, y * self.step + self.otstup)