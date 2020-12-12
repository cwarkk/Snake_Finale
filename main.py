import pygame
import sys
import random
pygame.init()

SIZE_OF_BLOCK = 25
BACK_COLOR = (150, 200, 150)
MAIN_COLOR = (0, 200, 150)
WHITE = (255, 255, 255)
BLUE = (0, 0, 200)
GREE = (100, 150, 255)
RED = (200, 0, 0)
SNAKE_COLOR = (50, 200, 50)
MARGIN = 1
MAIN_MARGIN = 70
COUNT_OF_BLOCKS = 25

size = [SIZE_OF_BLOCK * COUNT_OF_BLOCKS + 2 * SIZE_OF_BLOCK + MARGIN * COUNT_OF_BLOCKS,
        SIZE_OF_BLOCK * COUNT_OF_BLOCKS + 2 * SIZE_OF_BLOCK + MARGIN * COUNT_OF_BLOCKS + MAIN_MARGIN]
print(size)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Snake')
timer = pygame.time.Clock()
courier = pygame.font.SysFont('courier', 45)


class SnakeBlocks:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def is_inside(self):
        return 0 <= self.x < SIZE_OF_BLOCK and 0 <= self.y < SIZE_OF_BLOCK

    def __eq__(self, other):
        return isinstance(other, SnakeBlocks) and self.x == other.x and self.y == other.y


def random_empty_block():
    x = random.randint(0, COUNT_OF_BLOCKS -1)
    y = random.randint(0, COUNT_OF_BLOCKS -1)
    empty_block = SnakeBlocks(x, y)
    while empty_block in snake_blocks:
        empty_block.x = random.randint(0, COUNT_OF_BLOCKS -1)
        empty_block.y = random.randint(0, COUNT_OF_BLOCKS -1)
    return empty_block


def draw_blocks(color, column, raw):
    pygame.draw.rect(screen, color, [SIZE_OF_BLOCK + column * SIZE_OF_BLOCK + MARGIN * (column + 1),
                                     MAIN_MARGIN + SIZE_OF_BLOCK + raw * SIZE_OF_BLOCK + MARGIN * (raw + 1),
                                     SIZE_OF_BLOCK,
                                     SIZE_OF_BLOCK])


snake_blocks = [SnakeBlocks(13, 12), SnakeBlocks(12, 12), SnakeBlocks(11, 12)]
apple = random_empty_block()
d_raw = 0
d_col = 1
total = 0

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('Exit')
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and d_col != 0:
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

    screen.fill(BACK_COLOR)
    pygame.draw.rect(screen, MAIN_COLOR, [0, 0, size[0], MAIN_MARGIN])

    text_total = courier.render(f"Total: {total}", 0 , GREE)
    screen.blit(text_total, (SIZE_OF_BLOCK, SIZE_OF_BLOCK))

    for raw in range(COUNT_OF_BLOCKS):
        for column in range(COUNT_OF_BLOCKS):
            if (raw + column) % 2 == 0:
                color = BLUE
            else:
                color = GREE

            draw_blocks(color, column, raw)

    snake_head = snake_blocks[-1]
    if not snake_head.is_inside():
        print('You have crashed')
        pygame.quit()
        sys.exit()

    draw_blocks(RED, apple.x, apple.y)
    for block in snake_blocks:
        draw_blocks(SNAKE_COLOR, block.x, block.y)

    if apple == snake_head:
        total += 1
        snake_blocks.append(apple)
        apple = random_empty_block()

    new_head = SnakeBlocks(snake_head.x + d_raw, snake_head.y + d_col)
    snake_blocks.append(new_head)
    snake_blocks.pop(0)

    pygame.display.flip()
    timer.tick(4)
