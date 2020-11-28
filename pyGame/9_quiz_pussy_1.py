import pygame
import random
#####################################################################
# 기본 초기화 (반드시 해야하는 것들)
pygame.init() 

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("똥 피하기") # 게임 이름

# FPS
clock = pygame.time.Clock()
#####################################################################

# 1. 사용자 게임 초기화 ( 배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)

# 배경이미지 불러오기
background = pygame.image.load("C:/Users/y0010/Desktop/pythonWorkspace/pyGame/background.png")

# 캐릭터 만들기
character = pygame.image.load("C:/Users/y0010/Desktop/pythonWorkspace/pyGame/character.png")
character_size = character.get_rect().size
character_weidth = character_size[0] #가로
character_height = character_size[1] #세로
character_x_pos = (screen_width /2) - (character_weidth /2)
character_y_pos = screen_height - character_height

# 똥
pussy = pygame.image.load("C:/Users/y0010/Desktop/pythonWorkspace/pyGame/enemy.png")
pussy_size = pussy.get_rect().size
pussy_weidth = pussy_size[0] #가로
pussy_height = pussy_size[1] #세로
pussy_x_pos = random.randint(0,screen_width-pussy_weidth)
pussy_y_pos = 0

pussy = pygame.image.load("C:/Users/y0010/Desktop/pythonWorkspace/pyGame/enemy.png")

# 캐릭터 이동 속도
character_speed = 1
to_x = 0
to_y = 0

pussy_speed = 1

running = True # 게임이 진행중인가?
while running:
    dt = clock.tick(30) # 게임화면의 초당 프레임 수를 설정

    # 2. 이벤트 처리(키보드, 마우스)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_LEFT:
                to_x -= character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                to_x = 0



    # 3. 게임 캐릭터 위치 정의
    character_x_pos += to_x * dt 
    
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_weidth:
        character_x_pos = screen_width - character_weidth
    
     # 똥 떨어짐
    pussy_y_pos += pussy_speed * dt
    if pussy_y_pos > screen_height:
        pussy_y_pos = 0
        pussy_x_pos = random.randint(0,screen_width-pussy_weidth)
   

    # 4. 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    pussy_rect = pussy.get_rect()
    pussy_rect.left = pussy_x_pos
    pussy_rect.top = pussy_y_pos

    if character_rect.colliderect(pussy_rect):
        print("충돌했어요")
        running = False

    # 5. 화면에 그리기(blit)

    screen.blit(background, (0,0))
    screen.blit(character, (character_x_pos,character_y_pos))
    screen.blit(pussy, (pussy_x_pos,pussy_y_pos))

    pygame.display.update() 

pygame.time.delay(2000)

# pygame 종료
pygame.quit()
