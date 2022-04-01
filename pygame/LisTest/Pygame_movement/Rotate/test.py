import pygame


x = 150
y = 0
def rotate_triangle(center, scale, mouse_pos):
    vMouse = pygame.math.Vector2(mouse_pos)
    vCenter = pygame.math.Vector2(center)
    angle = pygame.math.Vector2().angle_to(vMouse - vCenter)

    # points = [(-0.5, -0.866), (-0.5, 0.866), (2.0, 0.0)]
    points = [(-0.5, -0.5), (-0.5, 0.5), (0.5, 0.5), (0.5, -0.5)]
    rotated_point = [pygame.math.Vector2(p).rotate(angle) for p in points]

    triangle_points = [(vCenter + p * scale) for p in rotated_point]
    return triangle_points


disp = pygame.display.set_mode((300, 300))


run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    mouse_position = pygame.mouse.get_pos()
    points = rotate_triangle((150, 150), 10, mouse_position)

    pygame.Surface.fill(disp, (255, 255, 255))
    pygame.draw.polygon(disp, (0, 0, 0), points)
    pygame.display.update()
