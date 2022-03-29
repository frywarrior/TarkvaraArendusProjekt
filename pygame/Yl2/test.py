import pygame
import sys

screen=pygame.display.set_mode([640,480])
pygame.display.set_caption("Harjutamine")

while True:





    for event in pygame.event.get():
    # Otsib kas on mingi "Event" toimunud
        if event.type == pygame.QUIT:
        # Kui sündmus võrdub lahkumine
            pygame.quit()
            sys.exit()
            # Lahkub programmist ja peatab kõik mis programmis toimub