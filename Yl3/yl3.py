import pygame

# kle robert raisk mul on nii pohhui sellest ja ma hakkasin jooma,
# niiet mine putsi, kui sina jood siis mina võin ka juua by vova, Franco toakaaslane

# ekraani seaded
W = 640
H = 480
screen = pygame.display.set_mode([W, H])
pygame.display.set_caption("yl3_pilt")

screen.fill([154, 255, 155])


def ruudud(varv, suurus, paksus=1, rida=0.1, veerg=0.1):
    x = y = ix = iy = 0  # seab vajalikud muutujad nulli
    while y <= H and iy != rida:
        # kui muutuja y on väiksem või võrdne ekraani kõrgusega ja iy ei ole võrdne ridade arvuga
        while x <= W and ix != veerg:
            # kui muutuja x on väiksem või võrdne ekraani laiusega ja ix ei ole võrdne veergude arvuga
            pygame.draw.rect(screen, varv, [x, y, suurus, suurus], paksus)  # joonistab antud parameetritega ruudu
            x += suurus - paksus  # liidab x väärtusele ruudu suuruse ja ruudu paksuse vahe
            ix += 1  # Liidab Indikaator x väärtusele arvu 1
            pygame.display.flip()  # uuendab ekraani
        x = ix = 0  # seab vajalikud muutujad nulli
        y += suurus - paksus  # liidab y väärtusele ruudu suuruse ja ruudu paksuse vahe
        iy += 1  # Liidab Indikaator y väärtusele arvu 1
        pygame.display.flip()  # uuendab ekraani


#
# Kompaktsem versioon, kuid palju raskem komenteerida
#

"""
def ruudud(varv, suurus, paksus=1, rida=0.1, veerg=0.1):
    x = y = ix = iy = 0
    while y <= H and iy != rida:
        while x <= W and ix != veerg:
            pygame.draw.rect(screen, varv, [x, y, suurus, suurus], paksus)
            x, ix = (x + (suurus - paksus)), (ix + 1)
        x, ix, y, iy = 0, 0, (y + (suurus - paksus)), (iy + 1)
"""

while True:

    ruudud([255, 0, 0], 20, 2)

    pygame.display.flip()
    for event in pygame.event.get():
        # Otsib kas on mingi "Event" toimunud
        if event.type == pygame.QUIT:
            # Kui sündmus võrdub lahkumine
            pygame.quit()
            quit()
            # Lahkub programmist ja peatab kõik mis programmis toimub
