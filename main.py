import pygame
import sys
import random
import pygame_menu
from pygame import mixer

pygame.init()

back_image = pygame.image.load("picture.jpg")

mixer.music.load("515946__mrthenoronha__detective-game-theme-loop.wav")
mixer.music.play(-1)

SIZE_OF_BLOCK = 20
BACK_COLOR = (150, 150, 150)
MAIN_COLOR = (255, 255, 255)
WHITE = (255, 255, 255)
BLUE = (204, 255, 204)
BLACK = (50, 50, 50)
RED = (200, 50, 50)
SNAKE_COLOR = (50, 150, 50)
MARGIN = 1
INTENT_MARGIN = 70
COUNT_OF_BLOCKS = 20

size = [SIZE_OF_BLOCK * COUNT_OF_BLOCKS + 2 * SIZE_OF_BLOCK + MARGIN * COUNT_OF_BLOCKS,
        SIZE_OF_BLOCK * COUNT_OF_BLOCKS + 2 * SIZE_OF_BLOCK + MARGIN * COUNT_OF_BLOCKS + INTENT_MARGIN]

print(size)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Snake')
timer = pygame.time.Clock()
my_font = pygame.font.SysFont('Comic Sans MS', 35)


class SnakeBlocks:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def is_inside(self):
        return 0 <= self.x < SIZE_OF_BLOCK and 0 <= self.y < SIZE_OF_BLOCK

    def __eq__(self, other):
        return isinstance(other, SnakeBlocks) and self.x == other.x and self.y == other.y


def draw_blocks(color, raw, column):
    pygame.draw.rect(screen, color, [SIZE_OF_BLOCK + column * SIZE_OF_BLOCK + MARGIN * (column + 1),
                                     INTENT_MARGIN + SIZE_OF_BLOCK + raw * SIZE_OF_BLOCK + MARGIN * (raw + 1),
                                     SIZE_OF_BLOCK,
                                     SIZE_OF_BLOCK])


def start():

    def random_empty_block():
        x, y = random.randint(0, COUNT_OF_BLOCKS - 1), random.randint(0, COUNT_OF_BLOCKS - 1)
        empty_block = SnakeBlocks(x, y)
        while empty_block in snake_blocks:
            empty_block.x = random.randint(0, COUNT_OF_BLOCKS - 1)
            empty_block.y = random.randint(0, COUNT_OF_BLOCKS - 1)
        return empty_block

    snake_blocks = [SnakeBlocks(13, 12), SnakeBlocks(12, 12), SnakeBlocks(11, 12)]
    apple = random_empty_block()
    stones = random_empty_block()
    d_raw = 0
    d_col = 1
    total = 0
    speed = 1
    running, PAUSE = 0, 1
    state = running

    def pause():
        paused = True
        global d_col
        global d_raw
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print('Exit')
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        quit()
                    elif event.key == pygame.K_RETURN:
                        paused = False
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('Exit')
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_UP and d_col != 0:
                    d_raw = -1
                    d_col = 0
                elif event.key == pygame.K_DOWN and d_col != 0:
                    d_raw = 1
                    d_col = 0
                elif event.key == pygame.K_LEFT and d_raw != 0:
                    d_raw = 0
                    d_col = -1
                elif event.key == pygame.K_RIGHT and d_raw != 0:
                    d_raw = 0
                    d_col = 1
                elif event.key == pygame.K_ESCAPE:
                    pause()

        screen.fill(BACK_COLOR)
        pygame.draw.rect(screen, MAIN_COLOR, [0, 0, size[0], INTENT_MARGIN])

        text_total = my_font.render(f"Total: {total}", False, BLACK)
        text_speed = my_font.render(f"Speed: {speed}", False, BLACK)
        screen.blit(text_total, (SIZE_OF_BLOCK, SIZE_OF_BLOCK))
        screen.blit(text_speed, (SIZE_OF_BLOCK + 250, SIZE_OF_BLOCK))

        for raw in range(COUNT_OF_BLOCKS):
            for column in range(COUNT_OF_BLOCKS):
                if (raw + column) % 2 == 0:
                    color = WHITE
                else:
                    color = BLUE

                draw_blocks(color, column, raw)

        snake_head = snake_blocks[-1]
        if not snake_head.is_inside():
            print('You have crashed')
            break

        draw_blocks(BLACK, stones.x, stones.y)
        draw_blocks(RED, apple.x, apple.y)
        for block in snake_blocks:
            draw_blocks(SNAKE_COLOR, block.x, block.y)

        if stones == snake_head:
            print('You encountered a stone')
            break

        if apple == snake_head:
            total += 1
            speed = total // 5 + 1
            snake_blocks.append(apple)
            apple = random_empty_block()

        new_head = SnakeBlocks(snake_head.x + d_raw, snake_head.y + d_col)
        if new_head in snake_blocks:
            print('You have crashed yourself')
            break

        snake_blocks.append(new_head)
        snake_blocks.pop(0)

        pygame.display.flip()
        timer.tick(5 + speed)


menu = pygame_menu.Menu(220, 300, 'Welcome',
                        theme=pygame_menu.themes.THEME_GREEN)

menu.add_text_input('Name: ', default='')
menu.add_button('Play', start)
menu.add_button("Exit", pygame_menu.events.EXIT)


while True:

    screen.blit(back_image, (0, 0))

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()
    if menu.is_enabled():
        menu.update(events)
        menu.draw(screen)

    pygame.display.update()
