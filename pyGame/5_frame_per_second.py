import pygame

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game") # 게임 이름

# FPS
clock = pygame.time.Clock()

# 배경 이미지 불러오기
background = pygame.image.load("C:\\Users\\y0010\\Desktop\\pythonWorkspace\\pyGame\\background.png")

# 스프라이트(캐릭터) 불러오기
character = pygame.image.load("C:\\Users\\y0010\\Desktop\\pythonWorkspace\\pyGame\\character.png")
character_size = character.get_rect().size # 이미지의 크기를 구해옴

character_width = character_size[0] # 캐릭터의 가로 크기
character_height = character_size[1] # 캐릭터의 세로 크기

character_x_pos = (screen_width /2) - (character_width /2) # 화면 가로의 절반 크기에 해당하는 곳에 캐릭터 위치
character_y_pos = screen_height - character_height # 화면 세로 크기 가장 아래에 해당하는 곳에 위치

# 이동할 좌표
to_x = 0
to_y = 0

# 이동 속도
character_speed = 0.5

# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    dt = clock.tick(10) # 게임화면의 초당 프레임 수를 설정

# 캐릭터가 1초 동안 100 만큼 이동을 해야함
# 10 fps : 1초 동안 10번 동작 -> 한번에 10만큼 이동해야 100만큼 이동
# 20 fps : 1초 동안 20번 동작 -> 한번에 5만큼 이동해야 100만큼 이동

    for event in pygame.event.get(): # 어떤 이벤트가 발생했는지 확인
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하면
            running = False

        if event.type == pygame.KEYDOWN: #키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT: # 캐릭터를 왼쪽으로
                to_x -= character_speed 
            elif event.key == pygame.K_RIGHT: # 캐릭터를 오른쪽으로
                to_x += character_speed
            elif event.key == pygame.K_UP: # 캐릭터를 위로
                to_y -= character_speed
            elif event.key == pygame.K_DOWN: # 캐릭터를 아래로
                to_y += character_speed
        
        if event.type == pygame.KEYUP: # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
    
    # fps 값이 변한다고 해서 게임 속도가 바뀌어서는 안된다
    character_x_pos += to_x * dt #character_speed * fps 값 -> fps 값의 변화와 관계 없이 캐릭터 이동
    character_y_pos += to_y * dt
    
    # 시간 = 거리/속력
    # 시간 = 1초, 거리 = character_speed , 속력 = fps
    # 속력(fps)은 가변하는데, 시간당 거리는 일정하게 유지하고 싶다.
    # 따라서 애초에 거리 값 계산에 속력을 넣어서(to_x * dt), 
    # 속력(dt)에 몇이 가변하든 상쇄되어 사라지게 만든다. 


    # 가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height


    
    screen.blit(background, (0, 0)) # 배경 그리기

    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기

    pygame.display.update() # 게임화면을 다시 그리기


# pygame 종료
pygame.quit()
