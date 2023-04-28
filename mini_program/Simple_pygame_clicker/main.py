import pygame

pygame.init()

WIDTH_WINDOW = (400)
HEIGHT_WINDOW = (400)
TITLE_WINDOW = 'WINDOW'
BACKGROUND_COLOR = (119, 128, 253)
TEXT_COLOR = (255, 255, 255)
count = 0
font = pygame.font.SysFont('Arial', 50)

screen = pygame.display.set_mode([WIDTH_WINDOW, HEIGHT_WINDOW])
pygame.display.set_caption(TITLE_WINDOW)

Close_Window = False

while not Close_Window:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Close_Window = True

    screen.fill(color=BACKGROUND_COLOR)

    key_press = pygame.key.get_pressed()

    if key_press[pygame.K_UP]:
        count += 1

    if key_press[pygame.K_DOWN]:
        count -= 1
        if count == 0:
            Close_Window = True

    clicker_text = font.render(str(count), True, TEXT_COLOR)
    screen.blit(clicker_text, (WIDTH_WINDOW // 2, HEIGHT_WINDOW // 2))
    pygame.display.update()
