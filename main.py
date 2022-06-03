import pygame
import math

pygame.init()
# Open a window on the screen
screen_width = 1100
screen_height = 755
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("path gen")
surface = pygame.image.load('background.png').convert()
clock = pygame.time.Clock()


def calculate_distance(x1, y1, x2, y2):
    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return dist


def timecheck(points):
    loop = 0
    time = 0
    # 715 / 144 = ppi
    for item in points:
        try:
            time += math.sqrt(((points[1][0] - points[0][0]) ** 2) + ((points[1][1] - points[0][1]) ** 2))
        except:
            pass
    return time


def main():
    points = []

    while True:
        screen.blit(surface, (0, 0))

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.MOUSEBUTTONUP:
                m_pos = pygame.mouse.get_pos()
                if int(m_pos[0]) <= 755:
                    points.append(m_pos)
                    print(points)

        x = 0
        for blob in points:
            pygame.draw.circle(screen, [255, 125, 0], blob, 10)
            try:
                if len(points) >= 2:
                    pygame.draw.line(screen, [0, 255, 255], points[x], points[x + 1], 3)
                    x += 1
            except:
                pass

        print(timecheck(points))
        pygame.display.update()
        clock.tick(30)


main()
