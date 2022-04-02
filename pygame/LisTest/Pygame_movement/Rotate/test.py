import pygame
import math

x = 150
y = 0
"""
def rotate_triangle(center, scale, mouse_pos):
    vMouse = pygame.math.Vector2(mouse_pos)
    vCenter = pygame.math.Vector2(center)
    angle = pygame.math.Vector2().angle_to(vMouse - vCenter)

    # points = [(-0.5, -0.866), (-0.5, 0.866), (2.0, 0.0)]
    points = [(-0.5, -0.5), (-0.5, 0.5), (0.5, 0.5), (0.5, -0.5)]
    rotated_point = [pygame.math.Vector2(p).rotate(angle) for p in points]

    triangle_points = [(vCenter + p * scale) for p in rotated_point]
    return triangle_points
"""

loc = (150, 150)


def rotate_polygon(center, scale, mouse_pos):
    dx = mouse_pos[0] - center[0]
    # print(f"dx.{dx}")
    dy = mouse_pos[1] - center[1]
    # print(f"dy.{dy}")
    le = math.sqrt(dx * dx + dy * dy)
    dx, dy = (dx * scale / le, dy * scale / le) if le > 0 else (1, 0)

    pts = [(1, 0.5), (2, 0.5), (2, -0.5), (1, -0.5)]
    pts = [(center[0] + p[0] * dx + p[1] * dy, center[1] + p[0] * dy - p[1] * dx) for p in pts]
    return pts


disp = pygame.display.set_mode((300, 300))

run = True
while run:
    keys = pygame.key.get_pressed()
    mouse_position = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if keys[pygame.K_m]:
            loc = mouse_position

    points = rotate_polygon(loc, 10, mouse_position)

    pygame.Surface.fill(disp, (255, 255, 255))
    pygame.draw.circle(disp, (0, 0, 0), loc, 15)
    pygame.draw.polygon(disp, (150, 150, 150), points)
    pygame.display.update()
