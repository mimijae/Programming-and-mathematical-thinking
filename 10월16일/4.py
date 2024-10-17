# 4. pygame 라이브러리를 이용해 가로, 세로 각각 720, 480 크기의 빈 윈도우를 띄우는
# 프로그램을 작성하시오.

import pygame

# pygame 초기화
pygame.init()

# 창 크기 설정 (가로 720, 세로 480)
screen = pygame.display.set_mode((720, 480))

# 창 제목 설정
pygame.display.set_caption("Empty Window")

# 윈도우를 유지하기 위한 반복문
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 창을 닫는 이벤트 처리
            running = False

# pygame 종료
pygame.quit()
