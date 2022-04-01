import pygame
# impordib mooduli pygame
import sys
# impordib mooduli sys
# import math

screen = pygame.display.set_mode([300, 300])
#
pygame.display.set_caption("Lumemees")

# Paneb display nime lumemeheks

x = 150
y = 150
s = 30


"""
def move(degrees, offset):
    rads = math.radians(degrees)
    x = math.cos(rads) * offset
    y = math.sin(rads) * offset
    return x, y
"""
def circle():
    return pygame.draw.circle(screen, [255, 255, 255], [x, y], s, 0)

while True:
    screen.fill([0, 191, 255])
    # Täidab ekraani sinisega

    a = circle()
    pygame.transform.rotate(a,10)

    pygame.display.update()

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        # Otsib kas on mingi "Event" toimunud
        if keys[pygame.K_w]:
            y -= 5
        if keys[pygame.K_s]:
            y += 5
        if keys[pygame.K_a]:
            x -= 5
        if keys[pygame.K_d]:
            x += 5

        if event.type == pygame.QUIT:
            # Kui sündmus võrdub lahkumine
            pygame.quit()
            sys.exit()

            # Lahkub programmist ja peatab kõik mis programmis toimub
