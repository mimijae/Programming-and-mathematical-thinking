# 슈팅게임
import pygame
import os
import sys
import random
from time import sleep

# 게임 스크린 크기
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 640

# 색 정의
BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
YELLOW = (250, 250, 50)
RED = (250, 50, 50)

# 전역 변수
FPS = 60

# 전투기 객체
class Fighter(pygame.sprite.Sprite):  
    # 전투기 클래스: 플레이어의 기체를 나타내며, 위치, 이동 및 충돌을 처리
    def __init__(self):
        # 부모 클래스(Sprite)의 초기화 메서드 호출
        super(Fighter, self).__init__()
        # 전투기 이미지 불러오기
        self.image = pygame.image.load(resource_path('assets/fighter.png'))
        # 전투기 이미지의 위치와 크기를 정의하는 rect 객체 생성
        self.rect = self.image.get_rect()
        # 전투기의 초기 위치 및 이동 속도 설정
        self.reset()

    # 전투기 초기화 메서드
    def reset(self):
        # 전투기를 화면 하단 중앙에 배치
        self.rect.x = int(SCREEN_WIDTH / 2)  # 화면 너비의 중앙 X 좌표
        self.rect.y = SCREEN_HEIGHT - self.rect.height  # 화면 하단 Y 좌표
        self.dx = 0  # 수평 이동 속도 초기화
        self.dy = 0  # 수직 이동 속도 초기화

    # 전투기 위치 업데이트 메서드
    def update(self):
        # 전투기의 위치를 이동 속도에 따라 업데이트
        self.rect.x += self.dx  # X축 이동
        self.rect.y += self.dy  # Y축 이동

        # 화면 경계 밖으로 나가지 않도록 처리
        if self.rect.x < 0 or self.rect.x + self.rect.width > SCREEN_WIDTH:
            self.rect.x -= self.dx  # 경계를 벗어나면 이동 취소
        if self.rect.y < 0 or self.rect.y + self.rect.height > SCREEN_HEIGHT:
            self.rect.y -= self.dy  # 경계를 벗어나면 이동 취소

    # 전투기를 화면에 그리는 메서드
    def draw(self, screen):
        # 전투기 이미지를 현재 위치(rect)에 그리기
        screen.blit(self.image, self.rect)

    # 전투기 충돌 체크 메서드
    def collide(self, sprites):
        # 다른 스프라이트 그룹과 충돌이 있는지 검사
        for sprite in sprites:
            if pygame.sprite.collide_rect(self, sprite):  # rect를 기준으로 충돌 검사
                return sprite  # 충돌한 스프라이트 반환


# 미사일 객체
class Missile(pygame.sprite.Sprite):  
    # 미사일 클래스: 플레이어가 발사하는 탄환을 나타냄
    def __init__(self, xpos, ypos, speed):
        # 부모 클래스(Sprite)의 초기화 메서드 호출
        super(Missile, self).__init__()
        # 미사일 이미지 불러오기
        self.image = pygame.image.load(resource_path('assets/missile.png'))
        # 미사일의 위치와 크기를 정의하는 rect 객체 생성
        self.rect = self.image.get_rect()
        self.rect.x = xpos  # 미사일의 초기 X 좌표
        self.rect.y = ypos  # 미사일의 초기 Y 좌표
        self.speed = speed  # 미사일 이동 속도 설정

    # 미사일 발사 메서드 (사운드 재생 용도, 현재는 비활성화)
    def launch(self):
        pass  # 실제 발사 소리 재생은 주석 처리됨
        # self.sound.play()  # 미사일 발사 소리 재생

    # 미사일 위치 업데이트 메서드
    def update(self):
        # 미사일은 Y축 위쪽으로 이동 (속도만큼 감소)
        self.rect.y -= self.speed  
        # 미사일이 화면 위쪽 경계를 벗어나면 삭제
        if self.rect.y + self.rect.height < 0:
            self.kill()  # 스프라이트 그룹에서 미사일 제거

    # 미사일 충돌 체크 메서드
    def collide(self, sprites):
        # 다른 스프라이트 그룹과 충돌이 있는지 검사
        for sprite in sprites:
            if pygame.sprite.collide_rect(self, sprite):  # rect를 기준으로 충돌 검사
                return sprite  # 충돌한 스프라이트 반환


# 암석 객체
class Rock(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos, speed):
        super(Rock, self).__init__()  # 부모 클래스(Sprite)의 초기화 메서드 호출
        rock_images_path = resource_path('assets/rock')  # 암석 이미지들이 저장된 디렉토리 경로 설정
        image_file_list = os.listdir(rock_images_path)  # 해당 디렉토리에 있는 파일 목록 가져오기
        
        # 파일 목록에서 ".png" 확장자만 필터링하여 전체 경로 리스트 생성
        self.image_path_list = [os.path.join(rock_images_path, file)
                                for file in image_file_list if file.endswith(".png")]
        
        # 필터링된 이미지 파일 중 하나를 랜덤으로 선택
        choice_rock_path = random.choice(self.image_path_list)
        
        # 선택된 이미지 파일을 불러와서 rock 객체의 이미지로 설정
        self.image = pygame.image.load(choice_rock_path)
        
        # 이미지의 사각형(rect) 객체를 가져와 위치 및 충돌 영역 정의
        self.rect = self.image.get_rect()
        self.rect.x = xpos  # x 좌표 설정
        self.rect.y = ypos  # y 좌표 설정
        self.speed = speed  # 암석이 화면에서 움직일 속도 설정

    # 암석 업데이트 (이동 동작)
    def update(self):
        self.rect.y += self.speed  # 암석을 아래쪽으로 이동시킴 (속도에 따라 y 좌표 증가)

    # 암석이 화면을 벗어났는지 확인
    def out_of_screen(self):
        if self.rect.y > SCREEN_HEIGHT:  # 암석의 y 좌표가 화면 높이보다 커지면 화면을 벗어남
            return True  # 화면을 벗어났음을 알림


# 게임 객체
# 게임 객체
class Game():
    def __init__(self):
        # 메뉴 및 배경 이미지 로드
        self.menu_image = pygame.image.load(resource_path('assets/background.png'))  # 메뉴 화면 배경 이미지
        self.background_image = pygame.image.load(resource_path('assets/background.png'))  # 게임 화면 배경 이미지
        self.explosion_image = pygame.image.load(resource_path('assets/explosion.png'))  # 폭발 이미지
        self.default_font = pygame.font.Font(resource_path('assets/NanumGothic.ttf'), 28)  # 기본 폰트 (크기 28)
        self.font_60 = pygame.font.Font(resource_path('assets/NanumGothic.ttf'), 60)  # 큰 텍스트용 폰트 (크기 60)
        self.font_30 = pygame.font.Font(resource_path('assets/NanumGothic.ttf'), 30)  # 중간 텍스트용 폰트 (크기 30)

        self.fighter = Fighter()  # 플레이어 캐릭터 객체
        self.missiles = pygame.sprite.Group()  # 미사일 객체 그룹
        self.rocks = pygame.sprite.Group()  # 운석 객체 그룹

        self.occur_prob = 40  # 운석 생성 확률 (낮을수록 자주 생성됨)
        self.shot_count = 0  # 파괴된 운석 수
        self.count_missed = 0  # 놓친 운석 수

        # 게임 메뉴 상태 (True일 경우 메뉴 화면 출력)
        self.menu_on = True

    # 게임 이벤트 처리 및 조작
    def process_events(self):
        for event in pygame.event.get():  # 발생한 모든 이벤트 가져오기
            if event.type == pygame.QUIT:  # 게임 종료 이벤트
                return True
            if self.menu_on:  # 메뉴 화면일 때 이벤트 처리
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:  # 스페이스 바 누를 경우 게임 시작
                    self.shot_count = 0  # 파괴된 운석 수 초기화
                    self.count_missed = 0  # 놓친 운석 수 초기화
                    self.menu_on = False  # 메뉴 화면 종료
            else:  # 게임 화면일 때 이벤트 처리
                if event.type == pygame.KEYDOWN:  # 키가 눌렸을 때 처리
                    if event.key == pygame.K_LEFT:  # 좌측 이동
                        self.fighter.dx -= 15
                    elif event.key == pygame.K_RIGHT:  # 우측 이동
                        self.fighter.dx += 15
                    elif event.key == pygame.K_UP:  # 위쪽 이동
                        self.fighter.dy -= 15
                    elif event.key == pygame.K_DOWN:  # 아래쪽 이동
                        self.fighter.dy += 15
                    elif event.key == pygame.K_SPACE:  # 미사일 발사
                        # 미사일 3개를 생성하고 발사
                        missile1 = Missile(self.fighter.rect.centerx-6, self.fighter.rect.y, 10)
                        missile2 = Missile(self.fighter.rect.centerx, self.fighter.rect.y, 10)
                        missile3 = Missile(self.fighter.rect.centerx+6, self.fighter.rect.y, 10)
                        missile1.launch()
                        missile2.launch()
                        missile3.launch()
                        self.missiles.add(missile1, missile2, missile3)  # 미사일 그룹에 추가
                elif event.type == pygame.KEYUP:  # 키를 뗄 때 이동 멈춤
                    if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                        self.fighter.dx = 0
                    elif event.key in (pygame.K_UP, pygame.K_DOWN):
                        self.fighter.dy = 0
        return False

    # 게임 로직 수행
    def run_logic(self, screen):
        occur_of_rocks = 4 + int(self.shot_count / 300)  # 운석 개수는 점수에 비례해 증가
        min_rock_speed = 4 + int(self.shot_count / 200)  # 최소 운석 속도
        max_rock_speed = 4 + int(self.shot_count / 100)  # 최대 운석 속도

        if random.randint(1, self.occur_prob) == 1:  # 확률적으로 운석 생성
            for i in range(occur_of_rocks):
                speed = random.randint(min_rock_speed, max_rock_speed)
                rock = Rock(random.randint(0, SCREEN_WIDTH - 30), 0, speed)  # 랜덤 위치와 속도
                self.rocks.add(rock)  # 운석 그룹에 추가

        for missile in self.missiles:  # 미사일과 운석 충돌 검사
            rock = missile.collide(self.rocks)
            if rock:
                self.occur_explosion(screen, rock.rect.x, rock.rect.y)  # 폭발 효과
                self.shot_count += 1  # 점수 증가
                missile.kill()  # 미사일 제거
                rock.kill()  # 운석 제거

        for rock in self.rocks:  # 운석이 화면을 벗어났는지 검사
            if rock.out_of_screen():
                rock.kill()
                self.count_missed += 1  # 놓친 운석 수 증가

        # 플레이어와 운석 충돌 또는 3번 이상 놓친 경우 게임 오버
        if self.fighter.collide(self.rocks) or self.count_missed >= 3:
            self.occur_explosion(screen, self.fighter.rect.x, self.fighter.rect.y)
            self.rocks.empty()  # 모든 운석 제거
            self.fighter.reset()  # 플레이어 위치 초기화
            self.menu_on = True  # 메뉴 화면으로 전환
            sleep(1)

    # 텍스트 출력
    def draw_text(self, screen, text, font, x, y, color):
        text_obj = font.render(text, True, color)  # 텍스트 렌더링
        text_rect = text_obj.get_rect(center=(x, y))  # 텍스트 위치 설정
        screen.blit(text_obj, text_rect)  # 화면에 출력

    # 폭발 효과 출력
    def occur_explosion(self, screen, x, y):
        explosion_rect = self.explosion_image.get_rect(topleft=(x, y))  # 폭발 이미지 위치 설정
        screen.blit(self.explosion_image, explosion_rect)  # 폭발 이미지 출력
        pygame.display.update()  # 화면 갱신

    # 게임 메뉴 출력
    def display_menu(self, screen):
        screen.blit(self.menu_image, [0, 0])  # 메뉴 배경 이미지 출력
        draw_x = int(SCREEN_WIDTH / 2)
        draw_y = int(SCREEN_HEIGHT / 4)
        self.draw_text(screen, 'Save the Earth!', self.font_60, draw_x, draw_y, YELLOW)
        self.draw_text(screen, 'Press the space bar', self.font_30, draw_x, draw_y + 200, WHITE)
        self.draw_text(screen, 'to start the game.', self.font_30, draw_x, draw_y + 250, WHITE)

    # 게임 화면 출력
    def display_frame(self, screen):
        screen.blit(self.background_image, self.background_image.get_rect())  # 배경 이미지 출력
        self.draw_text(screen, 'Destroyed: {}'.format(self.shot_count), self.default_font, 100, 20, YELLOW)
        self.draw_text(screen, 'Missed: {}'.format(self.count_missed), self.default_font, 400, 20, RED)
        self.rocks.update()  # 운석 상태 업데이트
        self.rocks.draw(screen)  # 운석 화면에 출력
        self.missiles.update()  # 미사일 상태 업데이트
        self.missiles.draw(screen)  # 미사일 화면에 출력
        self.fighter.update()  # 플레이어 상태 업데이트
        self.fighter.draw(screen)  # 플레이어 화면에 출력



# 게임 리소스 경로 설정 함수
def resource_path(relative_path):
    # 리소스 파일의 경로를 반환하는 함수
    try:
        # __file__ 경로를 기준으로 상대 경로를 계산
        current_path = os.path.dirname(__file__)  # 현재 파일의 디렉토리 경로
    except Exception:
        # __file__이 없을 경우 (예외 상황) 현재 작업 디렉토리 사용
        base_path = os.path.abspath(".")  # 현재 절대 경로 반환
    # 입력받은 상대 경로를 현재 경로에 합쳐서 반환
    return os.path.join(current_path, relative_path)

# 메인 함수: 게임 실행
def main():
    # Pygame 초기화
    pygame.init()
    # 게임 윈도우의 제목 설정
    pygame.display.set_caption('Shooting Game')  
    # 게임 화면 설정 (너비와 높이)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  
    # 게임 프레임 속도 관리를 위한 Clock 객체 생성
    clock = pygame.time.Clock()  
    # Game 클래스 객체 생성
    game = Game()  

    # 게임 루프 실행
    done = False  # 게임 종료 여부를 확인하는 플래그 변수
    while not done:
        # 이벤트 처리 (키 입력, 종료 등)
        done = game.process_events()  
        # 메뉴 화면 처리
        if game.menu_on:  
            game.display_menu(screen)  # 게임 메뉴를 화면에 표시
        else:
            # 게임 로직 실행 및 화면 갱신
            game.run_logic(screen)  # 게임 로직 (미사일, 충돌 등) 처리
            game.display_frame(screen)  # 게임 화면에 객체 출력

        # 화면을 업데이트하여 변경사항 표시
        pygame.display.flip()  
        # 게임 프레임 속도 유지 (FPS 설정값에 따라)
        clock.tick(FPS)  

    # 게임 종료 처리
    pygame.quit()

# 프로그램이 직접 실행될 때만 main() 함수 실행
if __name__ == "__main__":
    main()
