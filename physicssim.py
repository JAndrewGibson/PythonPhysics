import pygame
import sys

# Constants for screen dimensions
WIDTH, HEIGHT = 800, 600

# Constants for colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Particle class representing objects in the physics simulation
class Particle:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.velocity_x = 0
        self.velocity_y = 0
        self.acceleration_y = 0.5  # Gravity-like acceleration
        self.is_dragging = False
        self.drag_offset_x = 0
        self.drag_offset_y = 0

    def update(self):
        self.velocity_y += self.acceleration_y
        self.y += self.velocity_y

        # Collision with ground (simple ground plane at y = HEIGHT)
        if self.y + self.radius >= HEIGHT:
            self.y = HEIGHT - self.radius
            self.velocity_y *= -0.8  # Bounce with some energy loss

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Simple Physics Engine")
    clock = pygame.time.Clock()

    particles = []  # List to hold Particle objects

    # Create a particle
    particle = Particle(100, 100, 20, RED)
    particles.append(particle)

    prev_mouse_pos = (0, 0)

    while True:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if the mouse click happened within the particle
                mouse_x, mouse_y = pygame.mouse.get_pos()
                for particle in particles:
                    distance = ((particle.x - mouse_x) ** 2 + (particle.y - mouse_y) ** 2) ** 0.5
                    if distance <= particle.radius:
                        particle.is_dragging = True
                        particle.drag_offset_x = particle.x - mouse_x
                        particle.drag_offset_y = particle.y - mouse_y
                        prev_mouse_pos = pygame.mouse.get_pos()
            elif event.type == pygame.MOUSEBUTTONUP:
                for particle in particles:
                    particle.is_dragging = False
                    current_mouse_pos = pygame.mouse.get_pos()
                    particle.velocity_x = current_mouse_pos[0] - prev_mouse_pos[0]
                    particle.velocity_y = current_mouse_pos[1] - prev_mouse_pos[1]

        for particle in particles:
            if particle.is_dragging:
                particle.x, particle.y = pygame.mouse.get_pos()
                particle.x += particle.drag_offset_x
                particle.y += particle.drag_offset_y
            particle.update()
            particle.draw(screen)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
