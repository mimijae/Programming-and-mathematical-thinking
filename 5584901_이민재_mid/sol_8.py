# 문제 8. 다음은 pygame을 이용해 빈 윈도우를 출력하는 프로그램의 일부이다. 생략된
# 부분을 채워 프로그램을 완성하시오.

import pygame
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
pygame.init()
pygame.display.set_caption("Pygame")
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
done = False


# 윈도우를 유지하기 위한 반복문
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 창을 닫는 이벤트 처리
            running = False
            
            
pygame.quit()