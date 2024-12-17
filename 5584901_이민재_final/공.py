import pygame

# 게임 윈도우 크기
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# 색 정의
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Pygame 초기화
pygame.init()

# 윈도우 제목
pygame.display.set_caption("Ball")

# 윈도우 생성
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# 게임 화면 업데이트 속도
clock = pygame.time.Clock()

# 녹색 공 초기 위치, 크기, 속도
ball_x = int(WINDOW_WIDTH / 2)
ball_y = int(WINDOW_HEIGHT / 2)
ball_dx = 8  # 속도를 더 빠르게
ball_dy = 8
ball_size = 60  # 크기를 더 크게

# 빨간색 공 초기 위치, 크기, 속도
red_ball_x = int(WINDOW_WIDTH / 3)
red_ball_y = int(WINDOW_HEIGHT / 3)
red_ball_dx = 30  # 빨간 공 속도
red_ball_dy = 30
red_ball_size = 50  # 빨간 공 크기

# 파란색 공 초기 위치, 크기, 속도
blue_ball_x = int(WINDOW_WIDTH / 4)
blue_ball_y = int(WINDOW_HEIGHT / 4)
blue_ball_dx = 10  # 파란 공 속도
blue_ball_dy = 10
blue_ball_size = 40  # 파란 공 크기

# 게임 종료 전까지 반복
done = False

# 게임 반복 구간
while not done:
    # 이벤트 반복 구간
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # 게임 로직 구간
    # 녹색 공 위치 변경
    ball_x += ball_dx
    ball_y += ball_dy

    # 빨간 공 위치 변경
    red_ball_x += red_ball_dx
    red_ball_y += red_ball_dy

    # 파란 공 위치 변경
    blue_ball_x += blue_ball_dx
    blue_ball_y += blue_ball_dy

    # 녹색 공이 윈도우를 벗어날 경우
    if (ball_x + ball_size) > WINDOW_WIDTH or (ball_x - ball_size) < 0:
        ball_dx *= -1
    if (ball_y + ball_size) > WINDOW_HEIGHT or (ball_y - ball_size) < 0:
        ball_dy *= -1

        # ✅✅✅✅✅✅✅✅✅✅녹색 공이 윈도우를 벗어날 경우 게임 종료✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅
    # if (ball_x - ball_size) > WINDOW_WIDTH or (ball_x + ball_size) < 0 or (ball_y - ball_size) > WINDOW_HEIGHT or (ball_y + ball_size) < 0:
    #     print("공이 화면을 벗어났습니다. 게임 종료!")
    #     done = True

    # 빨간 공이 윈도우를 벗어날 경우
    if (red_ball_x + red_ball_size) > WINDOW_WIDTH or (red_ball_x - red_ball_size) < 0:
        red_ball_dx *= -1
    if (red_ball_y + red_ball_size) > WINDOW_HEIGHT or (red_ball_y - red_ball_size) < 0:
        red_ball_dy *= -1

    # 파란 공이 윈도우를 벗어날 경우
    if (blue_ball_x + blue_ball_size) > WINDOW_WIDTH or (blue_ball_x - blue_ball_size) < 0:
        blue_ball_dx *= -1
    if (blue_ball_y + blue_ball_size) > WINDOW_HEIGHT or (blue_ball_y - blue_ball_size) < 0:
        blue_ball_dy *= -1

    # 윈도우 화면을 노란색으로 채우기
    screen.fill(YELLOW)

    # 화면 그리기 구간
    # 녹색 공 그리기
    pygame.draw.circle(screen, GREEN, [ball_x, ball_y], ball_size, 0)

    # 빨간 공 그리기
    pygame.draw.circle(screen, RED, [red_ball_x, red_ball_y], red_ball_size, 0)

    # 파란 공 그리기
    pygame.draw.circle(screen, BLUE, [blue_ball_x, blue_ball_y], blue_ball_size, 0)

    # 화면 업데이트
    pygame.display.flip()

    # 초당 60 프레임으로 업데이트
    clock.tick(60)

# 게임 종료
pygame.quit()
