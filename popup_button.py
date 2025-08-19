import pygame

pygame.init()

# Screen setup
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Pygame Popup Example")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Popup class
class Popup:
    def __init__(self, text, rect):
        self.text = text
        self.rect = pygame.Rect(rect)
        self.font = pygame.font.Font(None, 36)
        self.visible = False

    def draw(self, surface):
        if self.visible:
            pygame.draw.rect(surface, WHITE, self.rect)
            pygame.draw.rect(surface, BLACK, self.rect, 2)
            text_surface = self.font.render(self.text, True, BLACK)
            surface.blit(text_surface, (self.rect.x + 10, self.rect.y + 10))

    def toggle(self):
        self.visible = not self.visible

# Create popup
popup = Popup("Hello, this is a popup!", (200, 150, 200, 100))

# Main loop
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_i:
            popup.toggle()

    popup.draw(screen)
    pygame.display.flip()

pygame.quit()
