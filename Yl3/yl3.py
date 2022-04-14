import pygame

# kle robert raisk mul on nii pohhui sellest ja ma hakkasin jooma,
# niiet mine putsi sina jood nii et mina võin ka juua by vova, Franco toakaaslane

# ekraani seaded
W = 640
H = 480
screen = pygame.display.set_mode([W, H])
pygame.display.set_caption("yl3_pilt")

# a = int(input("Kui suured ruudud?: "))

screen.fill([154, 255, 155])


def ruudud(varv, suurus, rida=0.1, veerg=0.1, paksus=1):
    x = 0
    y = 0
    ix = 0
    iy = 0
    while y <= H and iy != rida:
        while x <= W and ix != veerg:
            pygame.draw.rect(screen, varv, [x, y, suurus, suurus], paksus)
            x += suurus - paksus
            ix += 1
            pygame.display.flip()
        x = 0
        ix = 0
        y += suurus - paksus
        iy += 1
        pygame.display.flip()


while True:

    ruudud([255, 0, 0], 40, 3, 3, 1)

    pygame.display.flip()
    for event in pygame.event.get():
        # Otsib kas on mingi "Event" toimunud
        if event.type == pygame.QUIT:
            # Kui sündmus võrdub lahkumine
            pygame.quit()
            quit()
            # Lahkub programmist ja peatab kõik mis programmis toimub
