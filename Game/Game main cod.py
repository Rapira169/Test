import pygame
pygame.init()
clock = pygame.time.Clock()
x = 894 #= int(input("введите разрешение"))
y = 894 #= int(input("x"))
k = x/y
screen = (x, y)

# color = bool(input("словом? если нет нажмите любую кнопку и enter"))  #выбор RGB пока не работает
# if color == True:
#     color = str(input("RGB"))
# else:
#     color = str(input("цвет"))
color = "Red"

window = pygame.display.set_mode((screen))
bg = pygame.image.load("bg.png").convert() #фон
# window.blit(bg, (0, 0)) #отрисовка фона, не обязательно, протсо пример
#переменные player
p_x = x / 2 - x / 60
p_y = y * 0.8
psize_x = x / 30
psize_y = y / 30 * k
#обьекты:
speed_x = 0
speed_y = 0



run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

#движение куба
    def kub(k_x, k_y, ksize_x, ksize_y, speed_x, speed_y):
        k_x += speed_x
        k_y += speed_y
        kub = pygame.draw.rect(window, "CYAN", pygame.Rect(k_x, k_y, ksize_x, ksize_y))



    Key = pygame.key.get_pressed() #переобозначение нажатия
    # нажатия:
    if Key[pygame.K_w]: p_y-=3
    if Key[pygame.K_s]: p_y += 3
    if Key[pygame.K_a]: p_x -= 3
    if Key[pygame.K_d]: p_x += 3
    if Key[pygame.K_SPACE]:  #Jump
        if psize_x <= x / 20 and psize_y <= y / 20 * k:
            psize_x = psize_x + 1
            p_x = p_x - 0.5
            psize_y = psize_y + 1
            p_y = p_y - 0.5
    else:
        if psize_x > x / 30 and psize_y > y / 30 * k:
            psize_x = psize_x - 1
            p_x = p_x + 0.5
            psize_y = psize_y - 1
            p_y = p_y + 0.5


    window.blit(bg, (0, 0))   #обновление экрана
    #все отрисовки:
    player = pygame.draw.rect(window, color, pygame.Rect(p_x, p_y, psize_x, psize_y))
    kub(100, 200, 100, 20, 20, 20)#отрисовка куба


    pygame.display.flip() #!!!
    clock.tick(60)