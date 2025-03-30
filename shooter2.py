from pygame import*
import pygame
import random


# Ініціалізація Pygame
pygame.init()

# Розміри екрану
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background = transform.scale(image.load("images.jpg"),
                             (SCREEN_WIDTH, SCREEN_HEIGHT))

# Завантаження зображень
player_image = pygame.image.load("ship.jpg")  # Заміни на шлях до свого зображення
enemy_image = pygame.image.load("enemy.png")    # Заміни на шлях до зображення ворога
bullet_image = pygame.image.load("ball.png")  # Заміни на шлях до зображення кулі
  # Заміни на шлях до зображення фону
bullets = sprite.Group()
# Швидкість гри
clock = pygame.time.Clock()

# Клас для гравця
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(player_image, (50, 50))  # Масштабуємо зображення
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50)
        self.speed = 5
    
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)

        bullets.add(bullet)

# Клас для кулі
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.transform.scale(bullet_image, (5, 10))  # Масштабуємо зображення кулі
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 7

    def update(self):
        self.rect.y -= self.speed
        if self.rect.bottom < 0:
            self.kill()

# Клас для ворога
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(enemy_image, (50, 50))  # Масштабуємо зображення ворога
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - 50)
        self.rect.y = random.randint(-100, -40)
        self.speed = random.randint(2, 5)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.x = random.randint(0, SCREEN_WIDTH - 50)
            self.rect.y = random.randint(-100, -40)

# Головна функція гри
def game_loop():
    # Створюємо групи спрайтів
    player = Player()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)
    
    bullets = pygame.sprite.Group()
    
    enemies = pygame.sprite.Group()
    for i in range(5):
        enemy = Enemy()
        all_sprites.add(enemy)
        enemies.add(enemy)

running = True
while running:
    clock.tick(60)  # Обмежуємо кадри до 60 в секунду
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

        # Оновлення всіх спрайтів


        # Перевірка на зіткнення кулі з ворогами
        for bullet in bullets:
            hit_enemies = pygame.sprite.spritecollide(bullet, enemies, True)
            for enemy in hit_enemies:
                bullet.kill()

        # Заповнення екрану фоном
        screen.blit(background, (0, 0))  # Малюємо фон на весь екран
        
        # Малюємо всі спрайти
        all_sprites.draw(screen)
        
        # Оновлення екрану
        pygame.display.flip()

    pygame.quit()

# Запуск гри
game_loop()
