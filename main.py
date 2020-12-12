import pygame

MAIN_COLOR = (0, 200, 150)
SIZE_OF_BLOCK = 25
BACK_COLOR = (150, 200, 150)
WHITE = (255, 255, 255)
BLUE = (0, 0, 200)
GREE = (100, 150, 255)
SNAKE_COLOR = (50, 200, 50)
MARGIN = 1
MAIN_MARGIN = 70
COUNT_OF_BLOCKS = 25

size = [SIZE_OF_BLOCK * COUNT_OF_BLOCKS + 2 * SIZE_OF_BLOCK + MARGIN * COUNT_OF_BLOCKS,
        SIZE_OF_BLOCK * COUNT_OF_BLOCKS + 2 * SIZE_OF_BLOCK + MARGIN * COUNT_OF_BLOCKS + MAIN_MARGIN]
print(size)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Snake')

def draw_blocks(color, column, raw):
    pygame.draw.rect(screen, color, [SIZE_OF_BLOCK + column * SIZE_OF_BLOCK + MARGIN * (column + 1),
                                     MAIN_MARGIN + SIZE_OF_BLOCK + raw * SIZE_OF_BLOCK + MARGIN * (raw + 1),
                                     SIZE_OF_BLOCK, SIZE_OF_BLOCK])

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill(BACK_COLOR)
    pygame.draw.rect(screen, MAIN_COLOR, [0, 0, size[0], MAIN_MARGIN])

    for raw in range(COUNT_OF_BLOCKS):
        for column in range(COUNT_OF_BLOCKS):
            if (raw + column) % 2 == 0:
                color = BLUE
            else:
                color = GREE

            draw_blocks(color, column, raw)

    draw_blocks(SNAKE_COLOR, 0, 0)

    pygame.display.flip()
