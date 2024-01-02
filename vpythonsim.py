from vpython import *

scene.width = 600
scene.height = 400

# Define bounding box dimensions and position
box_width = 8
box_height = 6
box_pos = vector(0, 0, 0)

# Create bounding box walls
wall_left = box(pos=box_pos + vector(-box_width/2, box_height/2, 0),
                size=vector(box_width, 0.1, 0.1), color=color.gray(0.7))
wall_right = box(pos=box_pos + vector(box_width/2, box_height/2, 0),
                size=vector(box_width, 0.1, 0.1), color=color.gray(0.7))
wall_top = box(pos=box_pos + vector(0, box_height, 0),
                size=vector(0.1, box_height, box_width), color=color.gray(0.7))
wall_bottom = box(pos=box_pos + vector(0, 0, 0),
                size=vector(0.1, box_height, box_width), color=color.gray(0.7))

balls = []

# Create and position the ball
ball = sphere(pos=box_pos + vector(2, 4, 2), radius=1, color=color.red)
ball.velocity = vector(3, 1, -2)  # Initial velocity

def create_ball(pos):
    ball = sphere(pos=pos, radius=0.5, color=vector(random(), random(), random()))
    ball.velocity = vector(random() * 5 - 2.5, 0, random() * 5 - 2.5)  # Random initial velocity
    balls.append(ball)

scene.bind("click", create_ball)  # Bind ball creation to mouse clicks

dt = 0.01  # Time step

while True:
    rate(60)

    for ball in balls:
            ball.pos += ball.velocity * dt
            ball.velocity.y -= 9.8 * dt  # Apply gravity
            # Update ball position
            ball.pos += ball.velocity * dt

    # Check for collisions with walls
    if ball.pos.x + ball.radius >= box_pos.x + box_width/2:
        ball.velocity.x = -ball.velocity.x * 0.8
    elif ball.pos.x - ball.radius <= box_pos.x - box_width/2:
        ball.velocity.x = -ball.velocity.x * 0.8
    if ball.pos.y + ball.radius >= box_pos.y + box_height/2:
        ball.velocity.y = -ball.velocity.y * 0.8
    elif ball.pos.y - ball.radius <= box_pos.y - box_height/2:
        ball.velocity.y = -ball.velocity.y * 0.8

    # Keep ball within box boundaries
    ball.pos.x = max(box_pos.x - box_width/2 + ball.radius, min(box_pos.x + box_width/2 - ball.radius, ball.pos.x))
    ball.pos.y = max(box_pos.y - box_height/2 + ball.radius, min(box_pos.y + box_height/2 - ball.radius, ball.pos.y))

    # Apply gravity
    ball.velocity.y -= 9.8 * dt

