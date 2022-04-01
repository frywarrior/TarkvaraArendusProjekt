import pygame #Impordib pygame mooduli
pygame.init()

screen=pygame.display.set_mode([300,750]) # määrab akna resolutsiooni
pygame.display.set_caption("Foor") # Määrab akna nime

# Teeb tausta mustaks
screen.fill([0, 0, 0])
# Joonistab hallid ääred
pygame.draw.rect(screen, [80, 80, 80], [100, 15, 100, 270], 2)
# Joonistab punase ringi
pygame.draw.circle(screen, [255, 0, 0], [150,64], 40, 100)
# Joonistab kollase ringi
pygame.draw.circle(screen, [255, 255, 0], [150,150], 40, 100)
# Joonistab rohelise ringi
pygame.draw.circle(screen, [0, 255, 0], [150,235], 40, 100)

pygame.draw.line(screen, [80,80,80], [150,285], [150,600], 9)
pygame.draw.polygon(screen, [80, 80, 80], [[100,600],[200,600],[250,700],[50,700]], 2)
pygame.draw.polygon(screen, [0, 0, 255], [[99,601],[201,601],[218,633],[81,633]], 0)
pygame.draw.polygon(screen, [255, 255, 255], [[69,667],[233,667],[249,699],[51,699]], 0)










pygame.display.flip()

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if running == False:
      pygame.quit()