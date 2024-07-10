import pygame

pygame.init()

width = 900
height = 700
fbs = 60

# colours
white = (255, 255, 255)  # rgb
black = (0, 0, 0)
red = (255, 0, 0)
green = (80, 175, 90)
blue = (60, 160, 200)

cols = 10
rows = 10

wind = pygame.display.set_mode((width, height))
pygame.display.set_caption("Breakout Game")
clock = pygame.time.Clock()


# paddle class
class Paddle():
    def __init__(self):
        self.width = int(width / cols)
        self.height = 20
        self.x = int(width / 2) - int(self.width / 2)
        self.y = height - 30
        self.speed = 10
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw_paddle(self):
        pygame.draw.rect(wind, white, self.rect)

    def move_paddle(self):
        key = pygame.key.get_pressed()
        # left move
        if key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        # right move
        if key[pygame.K_RIGHT] and self.rect.right < width:
            self.rect.x += self.speed


# Ball class
class Ball():
    def __init__(self, x, y):
        self.radius = 10
        self.x = x - self.radius
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, self.radius * 2, self.radius * 2)
        self.dx = 3
        self.dy = -3
        self.game_status = 0

    def draw_ball(self):
        pygame.draw.circle(wind, blue, (self.rect.x, self.rect.y), self.radius)

    def move_ball(self):
        # wall collision
        if self.rect.right > width or self.rect.left < 0:
            self.dx *= -1
        if self.rect.top < 0:
            self.dy *= -1
        if self.rect.bottom > height:
            self.game_status = -1
        # paddle collision
        if self.rect.colliderect(paddle) and self.dy > 0:
            self.dy *= -1
        # brick collision
        row_num = 0
        all_done = True
        for row in brick_walls.bricks:
            col_num = 0
            for br in row:
                if self.rect.colliderect(br):
                    if abs(self.rect.bottom - br.top) < 5 and self.dy > 0:
                        self.dy *= -1
                    if abs(self.rect.top - br.bottom) < 5 and self.dy < 0:
                        self.dy *= -1
                    if abs(self.rect.left - br.right) < 5 and self.dy < 0:
                        self.dx *= -1
                    if abs(self.rect.right - br.left) < 5 and self.dy > 0:
                        self.dx *= -1
                    brick_walls.bricks[row_num][col_num] = (0, 0, 0, 0)
                if brick_walls.bricks[row_num][col_num] != (0, 0, 0, 0):
                    all_done = False
                col_num += 1
            row_num += 1
        if all_done:
            self.game_status = 1

        self.rect.x += self.dx
        self.rect.y += self.dy
        return self.game_status


# Bricks class
class Bricks():
    def __init__(self):
        self.width = int(width / cols)
        self.height = 30

    def create_bricks(self):
        self.bricks = []
        for row in range(rows):
            row_bricks = []
            for col in range(cols):
                x_brick = col * self.width
                y_brick = row * self.height
                br = pygame.Rect(x_brick, y_brick, self.width, self.height)
                row_bricks.append(br)
            self.bricks.append(row_bricks)

    def draw_bricks(self):
        for row in self.bricks:
            for br in row:
                pygame.draw.rect(wind, green, br)
                pygame.draw.rect(wind, black, br, 2)


paddle = Paddle()
ball = Ball(paddle.x + int(paddle.width / 2), paddle.y - 10)
brick_walls = Bricks()
brick_walls.create_bricks()

run = True
while run:
    clock.tick(fbs)
    wind.fill(black)
    paddle.draw_paddle()
    paddle.move_paddle()
    ball.draw_ball()
    brick_walls.draw_bricks()
    game_status = ball.move_ball()
    if game_status == -1:
        wind.fill(black)
        font = pygame.font.SysFont(None, 50)
        text = font.render("GAME OVER BUDDY!", True, red)
        text_react = text.get_rect(center=(width / 2, height / 2))
        wind.blit(text, text_react)

    if game_status == 1:
        wind.fill(black)
        font = pygame.font.SysFont(None, 50)
        text = font.render("YOU WON BUDDY!", True, green)
        text_react = text.get_rect(center=(width / 2, height / 2))
        wind.blit(text, text_react)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()
