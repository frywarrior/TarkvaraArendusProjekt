import pygame
# impordib mooduli pygame
import sys
# impordib mooduli sys


screen = pygame.display.set_mode([300, 300])
#
pygame.display.set_caption("Lumemees")

# Paneb display nime lumemeheks

x = 150
y = 150
s = 30

while True:
    screen.fill([0, 191, 255])
    # Täidab ekraani sinisega

    pygame.draw.circle(screen, [255, 255, 255], [x, y], s, 0)

    pygame.display.update()

    for event in pygame.event.get():
        # Otsib kas on mingi "Event" toimunud
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                y -= 10
            if event.key == pygame.K_s:
                y += 10
            if event.key == pygame.K_a:
                x -= 10
            if event.key == pygame.K_d:
                x += 10
            if event.key == pygame.K_SPACE:
                s += 5
        if event.type == pygame.QUIT:
            # Kui sündmus võrdub lahkumine
            pygame.quit()
            sys.exit()
            # Lahkub programmist ja peatab kõik mis programmis toimub

