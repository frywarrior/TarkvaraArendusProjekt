import pygame

pygame.init()
#ekraani seaded
screen=pygame.display.set_mode([640,480])
pygame.display.set_caption("yl2_pilt")

main = True

while main == True:
    screen.fill([255, 255, 255])

    font = pygame.font.Font(None, 30)
    text = font.render("Tere, olen sinu nimi", True, [0, 0, 0])
    screen.blit(text, [200, 200])

    bg = pygame.image.load("yl2_pilt.jpg")
    screen.blit(bg, [0, 0])
    bg = pygame.image.load("yl2_seller.jpg")
    screen.blit(bg, [0, 0])

    pygame.display.flip()
    for event in pygame.event.get():
    # Otsib kas on mingi "Event" toimunud
        if event.type == pygame.QUIT:
        # Kui sündmus võrdub lahkumine
            pygame.quit()
            quit()
            # Lahkub programmist ja peatab kõik mis programmis toimub