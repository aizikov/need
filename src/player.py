import pygame


class Player:
    def __init__(self, x, y, step, images):

        # Шаг, на который перемещается игрок за один раз
        self.step = step

        # Координата x игрока на экране
        self.x = x

        # Координата y игрока на экране
        self.y = y

        # Список изображений для анимации игрока
        self.images = images

        # Индекс текущего изображения игрока в списке
        self.image_index = 0

        # Индекс направления движения игрока
        self.image_direction_index = 0

        # Текущее изображение игрока
        self.image = self.images[self.image_direction_index][self.image_index]

        # Прямоугольник, описывающий область изображения игрока на экране
        self.rect = self.image.get_rect(center=(x, y))

    def move(self, dx, dy, maze):

        # Проверка, возможно ли переместить игрока в новую позицию
        if maze.test_place(self.x + dx * self.step, self.y + dy * self.step):

            # Если перемещение возможно, обновляем координаты игрока
            self.x += dx * self.step
            self.y += dy * self.step

            # Обновляем положение прямоугольника
            self.rect.x = self.x

            # Корректируем положение прямоугольника для визуального выравнивания
            self.rect.y = self.y - (70 - self.step)

            # Обновляем изображение игрока в соответствии с направлением
            self.update_image(dx, dy)

    def update_image(self, dx, dy):

        # Определяем индекс направления движения игрока и обновляем изображение
        if dx > 0:

            # Персонаж идет вправо
            self.image_direction_index = 1
        elif dx < 0:

            # Персонаж идет влево
            self.image_direction_index = 0
        elif dy < 0:

            # Персонаж идет вверх
            self.image_direction_index = 2
        elif dy > 0:

            # Персонаж идет вниз
            self.image_direction_index = 3
        
        # Обновляем индекс изображения для анимации
        self.image_index = (self.image_index + 1) % len(self.images[self.image_direction_index])

        # Получаем текущее изображение для анимации
        self.image = self.images[self.image_direction_index][self.image_index]

    def draw(self, screen):

        # Отображаем изображение игрока на экране
        screen.blit(self.image, self.rect)