# Импорт необходимых модулей
import pygame
import sys
import os

# Импорт класса Maze из модуля maze
from maze import Maze

# Импорт класса Player из модуля player
from player import Player


# Шаг для перемещения объектов на экране
step = 40

# Уровни игры, каждый уровень представлен списком строк,
# где каждый символ обозначает элемент лабиринта
LEVELS = [
    [
        "###############",
        "#   #      #   ",
        "#   #  #   #  #",
        "# # #  # ###  #",
        "# #          ##",
        "#    ######   #",
        "###############"
    ],
    [
        "###############",
        "#   #      #  #",
        "# # # # #  #  #",
        "# # # # #      ",
        "# # #       ###",
        "#     #####   #",
        "###############"
    ],
    [
        "###############",
        "#   #  #   #   ",
        "#   #  #   #  #",
        "# # #  # ###  #",
        "# # #        ##",
        "#     ######  #",
        "###############"
    ],
    [
        "###############",
        "#   #  #       ",
        "#   #  #   #  #",
        "# # # # ## #  #",
        "# #          ##",
        "#    ######   #",
        "###############"
    ],
    [
        "###############",
        "#   #      #  #",
        "#   #  #   #  #",
        "#   #  # ###  #",
        "## #         ##",
        "#     ######   ",
        "###############"
    ],
    [
        "###############",
        "#   #      #   ",
        "#   #  #      #",
        "# # #  # ###  #",
        "# # #  # ### ##",
        "#     ######  #",
        "###############"
    ]
]


# Функция для загрузки изображения
def load_image(name, colorkey=None):
    fullname = os.path.join('sprites', name)
    print(fullname)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


# Инициализация Pygame
pygame.init()

# Кадры в секунду
fps = 15

# Размеры экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


# Создание окна
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Плиточный лабиринт")

# Размеры спрайтов игрока
wh = (40, 70)

# Загрузка изображений для анимации движения игрока
player_images_right = [pygame.transform.scale(load_image("spr_r1.png", -1), wh),
                       pygame.transform.scale(load_image("spr_r2.png", -1), wh),
                       pygame.transform.scale(load_image("spr_r1.png", -1), wh),
                       pygame.transform.scale(load_image("spr_r3.png", -1), wh)]
player_images_left = [pygame.transform.scale(load_image("spr_l1.png", -1), wh),
                      pygame.transform.scale(load_image("spr_l2.png", -1), wh),
                      pygame.transform.scale(load_image("spr_l1.png", -1), wh),
                      pygame.transform.scale(load_image("spr_l3.png", -1), wh)]
player_images_back = [pygame.transform.scale(load_image("spr_f1.png", -1), wh),
                      pygame.transform.scale(load_image("spr_f2.png", -1), wh),
                      pygame.transform.scale(load_image("spr_f1.png", -1), wh),
                      pygame.transform.scale(load_image("spr_f3.png", -1), wh)]
player_images_forward = [pygame.transform.scale(load_image("spr_n1.png", -1), wh),
                      pygame.transform.scale(load_image("spr_n2.png", -1), wh),
                      pygame.transform.scale(load_image("spr_n1.png", -1), wh),
                      pygame.transform.scale(load_image("spr_n3.png", -1), wh)]

# Загрузка фонового изображения
fon = pygame.transform.scale(load_image('fon1.jpg'), (SCREEN_WIDTH, SCREEN_HEIGHT))

# Функция для создания кнопок
def draw_button(screen, color, x, y, width, height, text, text_color):
    pygame.draw.rect(screen, color, (x, y, width, height))
    font = pygame.font.SysFont(None, 30)
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x + width / 2, y + height / 2)
    screen.blit(text_surface, text_rect)

# Главная функция меню
def main_menu():

    # Флаг для отображения главного меню
    show_menu = True

    # Флаг для отображения главного меню
    clock = pygame.time.Clock()

    # Индекс текущего уровня
    current_level_index = 0

    # Создание объекта лабиринта
    maze = Maze(LEVELS[current_level_index], step)

    # Получение свободного места для размещения игрока
    x, y = maze.get_free_place()

    # Создание объекта игрока
    player = Player(x, y, step, [player_images_left, player_images_right, player_images_forward, player_images_back])
    
    while True:

        # Если нужно отобразить главное меню
        if show_menu:

            # Отображение фонового изображения на экране
            screen.blit(fon, (0, 0))
            
            # Отрисовка кнопок
            draw_button(screen, GRAY, 300, 200, 200, 50, "Играть", BLACK)
            draw_button(screen, GRAY, 300, 300, 200, 50, "Выйти", BLACK)

            # Обновление экрана
            pygame.display.flip()

            # Обработка событий
            for event in pygame.event.get():

                # Обработка события выхода из игры
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Обработка события нажатия кнопки мыши
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()

                    # Проверка клика на кнопки
                    if 300 <= mouse_pos[0] <= 500 and 200 <= mouse_pos[1] <= 250:

                        # Действия при нажатии на кнопку "Играть"
                        print("Игра начнется")
                        show_menu = False
                    elif 300 <= mouse_pos[0] <= 500 and 300 <= mouse_pos[1] <= 350:

                        # Действия при нажатии на кнопку "Выйти"
                        pygame.quit()
                        sys.exit()

        # Если все уровни пройдены
        elif current_level_index >= len(LEVELS):

            # Отображение фонового изображения на экране
            screen.blit(fon, (0, 0))
            
            # Отрисовка кнопки
            draw_button(screen, GRAY, 100, 300, 500, 50, "Вы победили! Выходим в главное меню", BLACK)

            # Обновление экрана
            pygame.display.flip()

            for event in pygame.event.get():

                # Обработка события выхода из игры
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Обработка события нажатия кнопки мыши
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()

                    # Проверка клика на кнопки
                    if 100 <= mouse_pos[0] <= 600 and 300 <= mouse_pos[1] <= 350:

                        # Действия при нажатии на кнопку "Играть"
                        print("Игра начнется")
                        show_menu = True
        else:

            # Если игра запущена
            # Отображение фонового изображения на экране
            screen.blit(fon, (0, 0))
            try:

                # Получение состояния клавиш
                keys = pygame.key.get_pressed()

                # Движение влево
                if keys[pygame.K_LEFT]:
                    player.move(-1, 0, maze)

                # Движение вправо
                if keys[pygame.K_RIGHT]:
                    player.move(1, 0, maze)
                
                # Движение вверх
                if keys[pygame.K_UP]:
                    player.move(0, -1, maze)
                
                # Движение вниз
                if keys[pygame.K_DOWN]:
                    player.move(0, 1, maze)
            
            # Обработка исключений
            except Exception as e:

                # Переход на следующий уровень
                current_level_index += 1
                print('новый урвень')

                # Если все уровни пройдены
                if current_level_index >= len(LEVELS):
                    continue

                # Создание нового объекта лабиринта
                maze = Maze(LEVELS[current_level_index], step)

                # Получение свободного места для размещения игрока
                x, y = maze.get_free_place()

                # Создание нового объекта игрока
                player = Player(x, y, step, [player_images_left, player_images_right, player_images_forward, player_images_back])

            # Отображение лабиринта на экране
            maze.draw(screen)

            # Отображение игрока на экране
            player.draw(screen)

            # Отображение кнопки "В главное меню"
            draw_button(screen, WHITE, 0, 0, 200, 50, "В главное меню", BLACK)

            # Обновление экрана
            pygame.display.flip()

            for event in pygame.event.get():

                # Обработка события выхода из игры
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Обработка события нажатия кнопки мыши
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if 0 <= mouse_pos[0] <= 200 and 0 <= mouse_pos[1] <= 50:
                        # Действия при нажатии на кнопку "Выйти"
                        # Переход в главное меню
                        show_menu = True
        # Управление частотой обновления экрана
        clock.tick(fps)

# Запуск главного меню
main_menu()
