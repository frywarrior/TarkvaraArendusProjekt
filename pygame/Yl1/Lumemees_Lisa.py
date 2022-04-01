import pygame
# impordib mooduli pygame
import sys
# impordib mooduli sys
import time as t

i = 0
u = 20
screen = pygame.display.set_mode([300, 300])
#
pygame.display.set_caption("Lumemees")


# Paneb display nime lumemeheks

def pilv(x, y):
    pygame.draw.circle(screen, [255, 255, 255], [x, y], 15, 0)
    pygame.draw.circle(screen, [255, 255, 255], [x + 15, y], 16, 0)
    pygame.draw.circle(screen, [255, 255, 255], [x + 30, y], 15, 0)


while True:
    screen.fill([0, 191, 255])
    # Täidab ekraani sinisega

    pygame.draw.circle(screen, [255, 255, 26], [300, 0], 50, 0)
    pygame.draw.circle(screen, [255, 255, 77], [300, 0], 40, 0)
    # Päike

    if u < 330:
        pilv(u, 50)
        pilv(u + 50, 15)
        pilv(u - 50, 75)
        u += 10
    else:
        u = -70
    # Pilv

    pygame.draw.circle(screen, [255, 255, 255], [150, 85], 30, 0)
    # pygame.draw.circle(screen, värv, tsentri_pos, raadius, joone_paksus)
    pygame.draw.circle(screen, [0, 0, 0], [160, 80], 5, 0)
    # pygame.draw.circle(screen, värv, tsentri_pos, raadius, joone_paksus)
    pygame.draw.circle(screen, [0, 0, 0], [140, 80], 5, 0)
    # pygame.draw.circle(screen, värv, tsentri_pos, raadius, joone_paksus)
    pygame.draw.polygon(screen, [230, 115, 0], [[145, 90], [150, 105], [155, 90]])

    # pygame.draw.polygon(screen, värv, tsentri_pos, raadius, joone_paksus)
    pygame.draw.circle(screen, [255, 255, 255], [150, 150], 40, 0)
    # pygame.draw.circle(screen, värv, tsentri_pos, raadius, joone_paksus)
    pygame.draw.circle(screen, [255, 255, 255], [150, 235], 50, 0)
    # pygame.draw.circle(screen, värv, tsentri_pos, raadius, joone_paksus)

    i += 1
    pygame.draw.circle(screen, [230, 230, 230], [300, 450], 200, 0)
    pygame.draw.circle(screen, [230, 230, 230], [100, 450], 195, 0)
    pygame.draw.circle(screen, [230, 230, 230], [200, 350], 85, 0)
    pygame.draw.circle(screen, [230, 230, 230], [0, 450], 190, 0)
    # Lumi

    if i != 2:
        pygame.draw.line(screen, [102, 51, 0], [50, 190], [200, 190], 2)
        pygame.draw.polygon(screen, [255, 179, 102], [[200, 190], [230, 180], [230, 200]])
        # Hari

        pygame.draw.line(screen, [153, 102, 51], [190, 150], [175, 190], 2)
        pygame.draw.line(screen, [153, 102, 51], [175, 190], [175, 200], 2)
        pygame.draw.line(screen, [153, 102, 51], [175, 190], [170, 200], 2)
        pygame.draw.line(screen, [153, 102, 51], [175, 190], [180, 200], 2)
        # parem käsi

        pygame.draw.line(screen, [153, 102, 51], [110, 150], [75, 190], 2)
        pygame.draw.line(screen, [153, 102, 51], [75, 190], [75, 200], 2)
        pygame.draw.line(screen, [153, 102, 51], [75, 190], [70, 200], 2)
        pygame.draw.line(screen, [153, 102, 51], [75, 190], [80, 200], 2)
        # vasak käsi

    else:
        i = 0
        pygame.draw.line(screen, [102, 51, 0], [100, 190], [250, 190], 2)
        pygame.draw.polygon(screen, [255, 179, 102], [[250, 190], [280, 180], [280, 200]])
        # Hari

        pygame.draw.line(screen, [153, 102, 51], [190, 150], [225, 190], 2)
        pygame.draw.line(screen, [153, 102, 51], [225, 190], [225, 200], 2)
        pygame.draw.line(screen, [153, 102, 51], [225, 190], [220, 200], 2)
        pygame.draw.line(screen, [153, 102, 51], [225, 190], [230, 200], 2)
        # parem käsi

        pygame.draw.line(screen, [153, 102, 51], [110, 150], [125, 190], 2)
        pygame.draw.line(screen, [153, 102, 51], [125, 190], [125, 200], 2)
        pygame.draw.line(screen, [153, 102, 51], [125, 190], [120, 200], 2)
        pygame.draw.line(screen, [153, 102, 51], [125, 190], [130, 200], 2)
        # vasak käsi

    pygame.draw.polygon(screen, [50, 50, 50],
                        [[125, 70], [175, 70], [175, 60], [165, 60], [165, 30], [135, 30], [135, 60], [125, 60]], 0)
    pygame.draw.polygon(screen, [255, 255, 255], [[135, 60], [165, 60], [165, 55], [135, 55]], 0)
    pygame.draw.circle(screen, [200, 0, 0], [165, 55], 5, 0)
    pygame.draw.circle(screen, [255, 0, 0], [165, 55], 3, 0)
    # müts

    pygame.draw.circle(screen, [0, 0, 0], [150, 130], 5, 0)
    pygame.draw.circle(screen, [0, 0, 0], [150, 150], 5, 0)
    pygame.draw.circle(screen, [0, 0, 0], [150, 170], 5, 0)
    # nööbid

    pygame.display.update()
    # Uuendab akent viimaste muudatustega

    for event in pygame.event.get():
        # Otsib kas on mingi "Event" toimunud
        if event.type == pygame.QUIT:
            # Kui sündmus võrdub lahkumine
            pygame.quit()
            sys.exit()
            # Lahkub programmist ja peatab kõik mis programmis toimub
    t.sleep(0.3)
    # ootab 0.3 sekundit enne kui loop jälle algab
