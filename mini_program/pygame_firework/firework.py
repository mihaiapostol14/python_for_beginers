import math
import random
import time

import pygame

pygame.init()
width, height = 400, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Новогодний Фейерверк')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Function to create a firework
def create_firework(x, y):
    color = random.choice(['#FF3366', '#33FF66', '#3366FF', '#FF33CC', '#FFFF33', '#FF6600', '#33FFFF'])
    firework = []
    for i in range(50):
        angle = random.uniform(0, 2 * math.pi)
        speed = random.uniform(5, 12)
        firework.append({
            'x': x,
            'y': y,
            'angle': angle,
            'length': 0,
            'speed': speed,
            'max_length': random.uniform(50, 120),
            'color': color,
            'line_width': 3,
        })
    return firework

# Update fireworks
def update_fireworks():
    global fireworks, last_firework_time
    screen.fill(BLACK)

    for firework in fireworks:
        for line in firework:
            # Increase line length over time
            if line['length'] < line['max_length']:
                line['length'] += line['speed'] * 0.1  # Increase length

            # Line end position
            x_end = line['x'] + line['length'] * math.cos(line['angle'])
            y_end = line['y'] + line['length'] * math.sin(line['angle'])

            # Draw line
            pygame.draw.line(
                screen,
                pygame.Color(line['color']),
                (int(line['x']), int(line['y'])),
                (int(x_end), int(y_end)),
                int(line['line_width'])
            )

            # Decrease line width
            line['line_width'] = max(1, line['line_width'] - 0.05)

        # Remove firework when all lines reached max length
        if all(line['length'] >= line['max_length'] for line in firework):
            fireworks.remove(firework)

    # Generate new firework every 1 second
    if time.time() - last_firework_time > 1:
        fireworks.append(create_firework(random.randint(50, 350), random.randint(50, 350)))
        last_firework_time = time.time()

# Main loop
fireworks = []
last_firework_time = time.time()

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    update_fireworks()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
