from pygame import *
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed 
        if keys_pressed[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed 
        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed 
        if keys_pressed[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed 
class Enemy(GameSprite):
    def update(self):
        if self.rect.x <= 470:
            self.direction = "right"
        if self.rect.x >= win_width - 85:
            self.direction = "left"
        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed 
class Wall(sprite.Sprite):
    def __init__(self, color_1,color_2,color_3,wall_width,wall_height,x,y):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.image.fill((color_1, color_2, color_3))
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
win_width = 700
win_height = 500
clock=time.Clock()
FPS = 0
window = display.set_mode(
    (win_width, win_height)
)
    display.update()
    clock.tick(FPS)
display.set_caption('Maze')
hero = Player('hero.png',5 ,win_height-80,4)
monster = Enemy('cyborg.png',win_width-80,270 ,2)
final = GameSprite('treasure.png',win_width-120 ,win_height-80 ,0)
wall_1 = Wall(108,108,108,10,300,110,120)
wall_2 = Wall(108,108,108,455,10,110,20)
wall_3 = Wall(108,108,108,345,10,210,100)
wall_4 = Wall(108,108,108,10,150,555,330)
wall_5 = Wall(108,108,108,10,150,555,100)
wall_6 = Wall(108,108,108,350,10,120,320)
wall_7 = Wall(108,108,108,10,130,465,200)
wall_8 = Wall(108,108,108,10,130,340,100)
wall_9 = Wall(108,108,108,10,130,210,200)
wall_10 = Wall(108,108,108,10,100,110,20)
background = transform.scale(
    image.load("background.jpg"),
    (win_width, win_height)
)
font.init()
font = font.Font(None, 70)
win = font.render('YOU WIN!', True, (255, 215, 0))
lose = font.render('YOU LOSE!', True, (180, 0, 0))
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
money =mixer.Sound('money.ogg')
kick =mixer.Sound('kick.ogg')
finish = False
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background,(0, 0) )
        hero.update()
        hero.reset()
        monster.update()
        monster.reset()
        final.reset()
        wall_1.draw_wall()
        wall_2.draw_wall()
        wall_3.draw_wall()
        wall_4.draw_wall()
        wall_5.draw_wall()
        wall_6.draw_wall()
        wall_7.draw_wall()
        wall_7.draw_wall()
        wall_8.draw_wall()
        wall_9.draw_wall()
        wall_10.draw_wall()
        if sprite.collide_rect(hero, monster) or sprite.collide_rect(hero, wall_1) or sprite.collide_rect(hero, wall_2) or sprite.collide_rect(hero, wall_3) or sprite.collide_rect(hero, wall_4) or sprite.collide_rect(hero, wall_5) or sprite.collide_rect(hero, wall_6) or sprite.collide_rect(hero, wall_7) or sprite.collide_rect(hero, wall_8) or sprite.collide_rect(hero, wall_9):
            finish = True
            window.blit(lose, (200, 200))
            kick.play()
        if sprite.collide_rect(hero, final):
            finish = True
            window.blit(win, (200, 200))           
            money.play()
    display.update()
    clock.tick(FPS)