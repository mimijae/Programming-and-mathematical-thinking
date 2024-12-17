import pygame
import os
import sys
import random

# 현재 파일의 경로와 assets 폴더 경로 설정
# __file__은 현재 실행되는 파일의 경로를 반환하고, assets 폴더를 상대 경로로 설정
current_path = os.path.dirname(__file__)
assets_path = os.path.join(current_path, 'assets')

# 게임 스크린 크기 설정
SCREEN_WIDTH = 480  # 화면의 가로 크기
SCREEN_HEIGHT = 640  # 화면의 세로 크기

# 색 정의 (RGB 값)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (20, 60, 120)
ORANGE = (250, 170, 70)
RED = (250, 0, 0)

# 게임의 FPS 설정 (프레임 속도)
FPS = 60

# 공 객체 정의
class Ball:
    def __init__(self, bounce_sound=None):
        # 공의 초기 위치와 크기 설정
        self.rect = pygame.Rect(int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2), 12, 12)
        self.bounce_sound = bounce_sound  # 공이 튕길 때 나는 소리
        self.dx = random.choice([-6, 6])  # x축 이동 속도 (양수 또는 음수 랜덤)
        self.dy = 5 # y축 이동 속도 (아래 방향으로 고정)

    # 공의 움직임 업데이트
    def update(self):
        self.rect.x += self.dx  # x축 이동
        self.rect.y += self.dy  # y축 이동

        # 화면 왼쪽 벽에 닿았을 때
        if self.rect.left < 0:
            self.dx *= -1  # 이동 방향 반전
            self.rect.left = 0
            if self.bounce_sound:
                self.bounce_sound.play()
        # 화면 오른쪽 벽에 닿았을 때
        elif self.rect.right > SCREEN_WIDTH:
            self.dx *= -1  # 이동 방향 반전
            self.rect.right = SCREEN_WIDTH 
            if self.bounce_sound:
                self.bounce_sound.play()

    # 공의 위치 초기화 (리셋)
    def reset(self, x, y):
        self.rect.x = x
        self.rect.y = y
        self.dx = random.choice([-8, -6, 6, 8])  # x축 속도 새로 설정
        self.dy = 5  # y축 속도 고정

    # 공 그리기
    def draw(self, screen):
        pygame.draw.rect(screen, ORANGE, self.rect)

# 플레이어 객체 정의
class Player:
    def __init__(self, ping_sound=None):
        # 플레이어의 초기 위치와 크기 설정
        self.rect = pygame.Rect(int(SCREEN_WIDTH / 2), SCREEN_HEIGHT - 40, 50, 15)
        self.ping_sound = ping_sound  # 공과 충돌 시 소리
        self.dx = 0  # 이동 속도 초기화

    # 플레이어와 공의 상호작용 및 이동
    def update(self, ball):
        # 화면 왼쪽 끝에서 멈춤
        if self.rect.left <= 0 and self.dx < 0:
            self.dx = 0
        # 화면 오른쪽 끝에서 멈춤
        elif self.rect.right >= SCREEN_WIDTH and self.dx > 0:
            self.dx = 0

        # 공과 충돌 시
        if self.rect.colliderect(ball.rect):
            ball.dx = random.randint(-15, 15)  # 공의 x축 속도 랜덤 변경
            ball.dy *= -1  # y축 속도 반전
            ball.rect.bottom = self.rect.top # 플레이어와 공이 맞았을때 공 시작 위치 조정
            if self.ping_sound:
                self.ping_sound.play()
        # 플레이어 이동
        self.rect.x += self.dx

    # 플레이어 그리기
    def draw(self, screen):
        pygame.draw.rect(screen, RED, self.rect)

# 적 객체 정의
class Enemy:
    def __init__(self, pong_sound=None):
        # 적의 초기 위치와 크기 설정
        self.rect = pygame.Rect(int(SCREEN_WIDTH / 2), 25, 50, 15)
        self.pong_sound = pong_sound  # 공과 충돌 시 소리

    # 적의 공 추적 및 움직임
    def update(self, ball):
        # 적이 공을 추적 (x축 이동)
        if self.rect.centerx > ball.rect.centerx:
            diff = self.rect.centerx - ball.rect.centerx
            self.rect.x -= 4 if diff > 4 else diff
        elif self.rect.centerx < ball.rect.centerx:
            diff = ball.rect.centerx - self.rect.centerx
            self.rect.x += 4 if diff > 4 else diff

        # 공과 충돌 시
        if self.rect.colliderect(ball.rect):
            ball.dy *= -1  # y축 속도 반전
            ball.rect.top = self.rect.bottom  # 공 위치 조정
            if self.pong_sound:
                self.pong_sound.play()

    # 적 그리기
    def draw(self, screen):
        pygame.draw.rect(screen, BLACK, self.rect)

# 게임 객체 정의
class Game:
    def __init__(self):
        # 사운드 및 폰트 파일 경로 설정
        bounce_path = os.path.join(assets_path, "bounce.wav")
        ping_path = os.path.join(assets_path, "ping.wav")
        pong_path = os.path.join(assets_path, "pong.wav")
        font_path = os.path.join(assets_path, "NanumGothicCoding-Bold.ttf")

        # 사운드 및 폰트 로드
        bounce_sound = pygame.mixer.Sound(bounce_path)
        ping_sound = pygame.mixer.Sound(ping_path)
        pong_sound = pygame.mixer.Sound(pong_path)

        self.font = pygame.font.Font(font_path, 50)
        self.ball = Ball(bounce_sound)
        self.player = Player(ping_sound)
        self.enemy = Enemy(pong_sound)
        self.player_score = 0
        self.enemy_score = 0

    # 키보드 이벤트 처리
    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.dx -= 15
                elif event.key == pygame.K_RIGHT:
                    self.player.dx += 15
            elif event.type == pygame.KEYUP:
                if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                    self.player.dx = 0
        return False

    # 게임 로직 실행
    def run_logic(self):
        self.ball.update()
        self.player.update(self.ball)
        self.enemy.update(self.ball)

        # 점수 계산
        if self.ball.rect.y < 0:
            self.player_score += 1
            self.ball.reset(self.player.rect.centerx, self.player.rect.centery)
        elif self.ball.rect.y > SCREEN_HEIGHT:
            self.enemy_score += 1
            self.ball.reset(self.enemy.rect.centerx, self.enemy.rect.centery)

    # 화면에 메시지 표시
    def display_message(self, screen, message, color):
        label = self.font.render(message, True, color)
        screen.blit(label, ((SCREEN_WIDTH - label.get_width()) // 2, SCREEN_HEIGHT // 2))
        pygame.display.update()

    # 화면 갱신
    def display_frame(self, screen):
        screen.fill(BLUE)
        if self.player_score == 10:
            self.display_message(screen, "You Win!", WHITE)
        elif self.enemy_score == 10:
            self.display_message(screen, "Enemy Wins!", WHITE)
        else:
            self.ball.draw(screen)
            self.player.draw(screen)
            self.enemy.draw(screen)
            pygame.draw.line(screen, WHITE, (0, SCREEN_HEIGHT // 2), (SCREEN_WIDTH, SCREEN_HEIGHT // 2))

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("PingPong Game")
    clock = pygame.time.Clock()
    game = Game()
    done = False

    while not done:
        done = game.process_events()
        game.run_logic()
        game.display_frame(screen)
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()

if __name__ == "__main__":
    main()
