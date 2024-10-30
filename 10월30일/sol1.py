import pygame
import os

# 게임 윈도우 크기
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 320

# 색 정의
LAND = (160, 120, 40)

# Pygame 초기화
pygame.init()

# 윈도우 제목
pygame.display.set_caption("Image")

# 윈도우 생성
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# 게임 화면 업데이트 속도
clock = pygame.time.Clock()

# 그림이 들어 있는 assets 폴더 경로 설정
current_path = os.path.dirname(__file__)
assets_path = os.path.join(current_path, 'assets')

# 배경 이미지 로드
background_image = pygame.image.load(os.path.join(assets_path, 'terrain.png'))

# 이미지 로드
mushroom_image_1 = pygame.image.load(os.path.join(assets_path, 'mushroom1.png'))
mushroom_image_2 = pygame.image.load(os.path.join(assets_path, 'mushroom2.png'))
mushroom_image_3 = pygame.image.load(os.path.join(assets_path, 'mushroom3.png'))
fish_image = pygame.image.load(os.path.join(assets_path, 'fish.png'))

# 게임 종료 전까지 반복
done = False
# 게임 반복 구간
while not done:
    # 이벤트 반복 구간
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    # 화면 삭제 구간
    screen.fill(LAND)
    # 배경 이미지 그리기
    screen.blit(background_image, background_image.get_rect())
    # 버섯 이미지 새로운 위치에 그리기
    screen.blit(mushroom_image_1, [150, 100])  # 위치 변경
    screen.blit(mushroom_image_2, [350, 120])  # 위치 변경
    screen.blit(mushroom_image_3, [500, 160])  # 위치 변경
    # fish 이미지 그리기
    screen.blit(fish_image, [500, 40])  # 새로운 이미지 추가
    # 화면 업데이트
    pygame.display.flip()
    # 초당 60 프레임으로 업데이트
    clock.tick(60)

# 게임 종료
pygame.quit()
