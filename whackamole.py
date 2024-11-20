import pygame,sys
import random



def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        grid_size = 15
        cell_widht = 640/grid_size
        cell_height = 512/grid_size
        x,y = 0,0
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    a, b = event.pos
                    row = b // cell_height
                    col = a // cell_widht
                    print(row, col)
                    if row == y and col == x:
                        x, y = (random.randrange(0, 15), random.randrange(0, 15))
                        screen.blit(mole_image, mole_image.get_rect(topleft=(x, y)))
                        print(x, y)
            screen.fill("light green")

            for i in range(16):
                pygame.draw.line(
                    screen,  # where?
                    (245, 152, 66),  # color of the line
                    (0, i * 512 / 15),
                    (640, i * 512 / 15),
                )
            # vertival lines
            for i in range(16):
                pygame.draw.line(
                    screen,
                    (245, 152, 66),
                    (i*640 / 15, 0),
                    (i*640 / 15, 640),
                )
            x_quadrant =  x * cell_widht + cell_widht // 2 - mole_image.get_width() // 2
            y_quadrant =y * cell_height + cell_height // 2 - mole_image.get_height() // 2
            screen.blit(mole_image, mole_image.get_rect(topleft=(x_quadrant, y_quadrant)))
            pygame.display.flip()
            clock.tick(60)
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     a, b = event.pos
            #     row = b//(512//15)
            #     col = a//(640//15)
            #     print(row, col)
            #     print(random.randrange(0,15),random.randrange(0,15))
            #     if row == y and col == x:
            #         screen.blit(mole_image, mole_image.get_rect(random.randrange(0,15),random.randrange(0,15)))


    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
