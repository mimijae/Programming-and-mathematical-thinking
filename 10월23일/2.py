import pygame

# 게임 윈도우 크기
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 700

# 색 정의
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

def main():
    # Pygame 초기화
    pygame.init()
    # 윈도우 제목
    pygame.display.set_caption("Drawing")
    # 윈도우 생성
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    # 게임 화면 업데이트 속도
    clock = pygame.time.Clock()
    # 게임 종료 전까지 반복
    done = False

    # 게임 반복 구간
    while not done:
        # Pygame이 macOS에서 잘 작동하도록 함
        pygame.event.pump()
        
        # 이벤트 반복 구간
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        
        # 화면 삭제 구간
        screen.fill(WHITE)

        # 선 그리기 
        pygame.draw.line(screen, RED, [50, 50], [500, 50], 4)
        pygame.draw.line(screen, GREEN, [50, 100], [500, 100], 4)
        pygame.draw.line(screen, BLUE, [50, 150], [500, 150], 4)

        # 사각형 그리기 
        pygame.draw.rect(screen, RED, [50, 200, 150, 150], 4) 

        # 다각형 그리기
        pygame.draw.polygon(screen, GREEN, [[350, 200], [250, 350], [450, 350]], 4)

        # 원형 그리기
        pygame.draw.circle(screen, BLUE, [150, 450], 60, 4)

        # 타원 그리기: 선 두께를 0으로 선택하면 내부를 채움
        pygame.draw.ellipse(screen, BLUE, [250, 400, 200, 100], 0)

        # 폰트 선택(폰트, 크기, 두껍게, 이탤릭)
        font = pygame.font.SysFont('FixedSys', 40, True, False)

        # 안티얼리어스를 적용하고 검은색 문자열 렌더링
        text = font.render("Hello Pygame", True, BLACK)

        # 화면에 텍스트 표시
        screen.blit(text, [200, 600])

        # 화면 업데이트
        pygame.display.flip()

        # 초당 60 프레임으로 업데이트
        clock.tick(60)
    
    # 게임 종료
    pygame.quit()

if __name__ == "__main__":
    main()
