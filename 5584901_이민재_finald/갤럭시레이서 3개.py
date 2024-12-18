import pygame
import sys
import math
import random
from pygame.locals import *
import os

# 색상 정의 (R, G, B)
BLACK = (0, 0, 0)          # 배경색
SILVER = (192, 208, 224)   # 게임 타이틀, 점수 표시용
RED = (255, 0, 0)          # 게임 오버 텍스트 색상
CYAN = (0, 224, 255)       # 새로운 기록 알림 색상

# 파일 경로 설정
current_path = os.path.dirname(__file__)  # 현재 파일 경로 가져오기
assets_path = os.path.join(current_path, 'assets/image_gl')  # 이미지가 저장된 폴더 경로 설정

# 이미지 로딩 (게임에 필요한 모든 이미지 불러오기)
img_galaxy = pygame.image.load(os.path.join(assets_path, "galaxy.png"))  # 배경 이미지
img_sship = [  # 플레이어 기체 이미지 (기본, 왼쪽 이동, 오른쪽 이동, 엔진 불꽃)
    pygame.image.load(os.path.join(assets_path, "starship.png")),
    pygame.image.load(os.path.join(assets_path, "starship_l.png")),
    pygame.image.load(os.path.join(assets_path, "starship_r.png")),
    pygame.image.load(os.path.join(assets_path, "starship_burner.png"))
]
img_weapon = pygame.image.load(os.path.join(assets_path, "bullet.png"))  # 미사일 이미지
img_shield = pygame.image.load(os.path.join(assets_path, "shield.png"))  # 실드 이미지

# 적 기체 이미지 (일반 기체부터 보스까지)
img_enemy = [
    pygame.image.load(os.path.join(assets_path, "enemy0.png")),
    pygame.image.load(os.path.join(assets_path, "enemy1.png")),
    pygame.image.load(os.path.join(assets_path, "enemy2.png")),
    pygame.image.load(os.path.join(assets_path, "enemy3.png")),
    pygame.image.load(os.path.join(assets_path, "enemy4.png")),
    pygame.image.load(os.path.join(assets_path, "enemy_boss.png")),
    pygame.image.load(os.path.join(assets_path, "enemy_boss_f.png"))
]

# 폭발 이미지 (연속적인 프레임으로 폭발 효과 표현)
img_explode = [
    None,
    pygame.image.load(os.path.join(assets_path, "explosion1.png")),
    pygame.image.load(os.path.join(assets_path, "explosion2.png")),
    pygame.image.load(os.path.join(assets_path, "explosion3.png")),
    pygame.image.load(os.path.join(assets_path, "explosion4.png")),
    pygame.image.load(os.path.join(assets_path, "explosion5.png"))
]

# 타이틀 화면 이미지 (배경과 로고)
img_title = [
    pygame.image.load(os.path.join(assets_path, "nebula.png")),  # 타이틀 배경
    pygame.image.load(os.path.join(assets_path, "logo.png"))     # 게임 로고
]

# 사운드 효과 변수 초기화 (현재 비활성화)
se_barrage, se_damage, se_explosion, se_shot = None, None, None, None

# 게임 변수 초기화
idx = 0  # 게임 상태 인덱스 (0: 타이틀, 1: 게임 진행, 2: 게임 오버 등)
tmr = 0  # 타이머 변수 (시간 카운트)
score = 0  # 현재 점수
hisco = 10000  # 최고 점수
new_record = False  # 새로운 기록 여부
bg_y = 0  # 배경 이미지 Y축 스크롤 위치

# 플레이어 기체 상태 변수
ss_x = 0  # 플레이어 X좌표
ss_y = 0  # 플레이어 Y좌표
ss_d = 0  # 플레이어 방향 (0: 기본, 1: 왼쪽, 2: 오른쪽)
ss_shield = 0  # 실드 게이지
ss_muteki = 0  # 무적 시간
key_spc = 0  # 스페이스바 입력 상태
key_z = 0  # Z키 입력 상태

ss_x_list = [400, 480, 560]  # 비행기 3개 나란히 배치 (X 좌표)
ss_y_list = [600, 600, 600]  # Y 좌표는 동일

# 미사일 변수 (최대 개수 설정 및 초기화)
MISSILE_MAX = 200  # 미사일 최대 개수
msl_no = 0  # 현재 미사일 인덱스
msl_f = [False] * MISSILE_MAX  # 미사일 활성화 여부
msl_x = [0] * MISSILE_MAX  # 미사일 X좌표
msl_y = [0] * MISSILE_MAX  # 미사일 Y좌표
msl_a = [0] * MISSILE_MAX  # 미사일 각도

# 적 기체 변수 (최대 개수 설정 및 초기화)
ENEMY_MAX = 100  # 적 기체 최대 개수
emy_no = 0  # 현재 적 기체 인덱스
emy_f = [False] * ENEMY_MAX  # 적 기체 활성화 여부
emy_x = [0] * ENEMY_MAX  # 적 기체 X좌표
emy_y = [0] * ENEMY_MAX  # 적 기체 Y좌표
emy_a = [0] * ENEMY_MAX  # 적 기체 이동 각도
emy_type = [0] * ENEMY_MAX  # 적 기체 종류
emy_speed = [0] * ENEMY_MAX  # 적 기체 속도
emy_shield = [0] * ENEMY_MAX  # 적 기체 체력
emy_count = [0] * ENEMY_MAX  # 적 기체 추가 데이터 (카운터)

# 적 기체 종류 정의
EMY_BULLET = 0  # 적 미사일
EMY_ZAKO = 1    # 일반 적 기체
EMY_BOSS = 5    # 보스 기체

# 화면 경계선 설정 (적 기체 이동 제한)
LINE_T = -80   # 상단 경계
LINE_B = 800   # 하단 경계
LINE_L = -80   # 왼쪽 경계
LINE_R = 1040  # 오른쪽 경계

# 폭발 효과 변수 (최대 개수 설정 및 초기화)
EFFECT_MAX = 100  # 폭발 효과 최대 개수
eff_no = 0  # 현재 폭발 인덱스
eff_p = [0] * EFFECT_MAX  # 폭발 프레임 단계
eff_x = [0] * EFFECT_MAX  # 폭발 X좌표
eff_y = [0] * EFFECT_MAX  # 폭발 Y좌표

def get_dis(x1, y1, x2, y2):  # 두 점 사이 거리 계산
    return ((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))

def draw_text(scrn, txt, x, y, siz, col):  # 입체적인 문자 표시
    fnt = pygame.font.Font(None, siz)  # 지정된 크기의 기본 폰트 생성
    cr = int(col[0] / 2)  # 색상(R) 값을 어둡게 조정 (입체감 효과)
    cg = int(col[1] / 2)  # 색상(G) 값을 어둡게 조정
    cb = int(col[2] / 2)  # 색상(B) 값을 어둡게 조정
    sur = fnt.render(txt, True, (cr, cg, cb))  # 어두운 색상으로 텍스트 렌더링
    x = x - sur.get_width() / 2  # 텍스트 중앙 정렬 (X축 기준)
    y = y - sur.get_height() / 2  # 텍스트 중앙 정렬 (Y축 기준)
    scrn.blit(sur, [x + 1, y + 1])  # 어두운 그림자 효과를 아래에 출력
    cr = col[0] + 128  # 색상(R) 값 밝게 조정 (최대 255)
    if cr > 255: cr = 255
    cg = col[1] + 128  # 색상(G) 값 밝게 조정
    if cg > 255: cg = 255
    cb = col[2] + 128  # 색상(B) 값 밝게 조정
    if cb > 255: cb = 255
    sur = fnt.render(txt, True, (cr, cg, cb))  # 밝은 색상으로 텍스트 렌더링
    scrn.blit(sur, [x - 1, y - 1])  # 밝은 효과를 위쪽에 출력
    sur = fnt.render(txt, True, col)  # 원래 색상으로 텍스트 렌더링
    scrn.blit(sur, [x, y])  # 최종 텍스트 출력 (가운데)

def move_starship(scrn, key):  # 플레이어 기체 이동
    global idx, tmr, ss_x_list, ss_y_list, ss_d, ss_shield, ss_muteki, key_spc, key_z

    ss_d = 0  # 기체 방향 초기화
    for i in range(3):  # 비행기 3대 각각 이동 처리
        if key[K_UP] == 1:
            ss_y_list[i] -= 20
            if ss_y_list[i] < 80:
                ss_y_list[i] = 80
        if key[K_DOWN] == 1:
            ss_y_list[i] += 20
            if ss_y_list[i] > 640:
                ss_y_list[i] = 640
        if key[K_LEFT] == 1:
            ss_d = 1
            ss_x_list[i] -= 20
            if ss_x_list[i] < 40 + (i * 40):  # 비행기 간격 유지
                ss_x_list[i] = 40 + (i * 40)
        if key[K_RIGHT] == 1:
            ss_d = 2
            ss_x_list[i] += 20
            if ss_x_list[i] > 920 - (2 - i) * 40:  # 비행기 간격 유지
                ss_x_list[i] = 920 - (2 - i) * 40

        scrn.blit(img_sship[ss_d], [ss_x_list[i] - 37, ss_y_list[i] - 48])  # 비행기 출력

    # 미사일 발사 처리
    key_spc = (key_spc + 1) * key[K_SPACE]
    if key_spc % 5 == 1:
        for i in range(3):  # 비행기마다 미사일 발사
            set_missile(0, ss_x_list[i], ss_y_list[i])
    
    key_z = (key_z + 1) * key[K_z]  # Z키를 누르면 특수 미사일 발사
    if key_z == 1 and ss_shield > 10:  # 실드가 충분할 때만 특수 미사일 사용
        set_missile(10, ss_x_list[1], ss_y_list[1])  # 특수 미사일 발사
        ss_shield = ss_shield - 10  # 실드 감소
        # se_barrage.play()  # 특수 발사 효과음

    # 비행기 3개에서 필살기
    # key_z = (key_z + 1) * key[K_z]  # Z키를 누르면 특수 미사일 발사
    # if key_z == 1 and ss_shield > 10:  # 실드가 충분할 때만 특수 미사일 사용
    #     for i in range(3):  # 비행기마다 미사일 발사
    #         set_missile(10, ss_x_list[i], ss_y_list[i])  # 특수 미사일 발사
    #         ss_shield = ss_shield - 10  # 실드 감소
    #         # se_barrage.play()  # 특수 발사 효과음

    # 충돌 검사 및 실드 감소 (한번만 체크)
    if ss_muteki == 0:  # 무적 상태가 아닐 때만 충돌 체크
        for j in range(ENEMY_MAX):  # 모든 적 기체 확인
            if emy_f[j] == True:
                w = img_enemy[emy_type[j]].get_width()
                h = img_enemy[emy_type[j]].get_height()
                r = int((w + h) / 4 + 37)  # 충돌 범위
                # 비행기 3대 중 중앙 좌표(ss_x_list[1]) 기준 충돌 검사
                if get_dis(emy_x[j], emy_y[j], ss_x_list[1], ss_y_list[1]) < r * r:
                    set_effect(ss_x_list[1], ss_y_list[1])  # 폭발 효과 출력
                    ss_shield -= 10  # 실드 감소
                    ss_muteki = 60  # 전체 무적 시간 설정
                    if ss_shield <= 0:
                        idx = 2  # 게임 오버
                        tmr = 0
                    return  # 충돌이 감지되면 더 이상 검사하지 않음

    # 무적 상태 처리
    if ss_muteki > 0:
        ss_muteki -= 1




def set_missile(typ, x, y):  # 미사일 설정 함수
    global msl_no
    if typ == 0:  # 3발 미사일 발사
        for offset in [-20, 0, 20]:  # X좌표를 약간 조정하여 미사일을 3발 발사
            msl_f[msl_no] = True
            msl_x[msl_no] = x + offset
            msl_y[msl_no] = y - 50
            msl_a[msl_no] = 270  # 미사일 위로 발사
            msl_no = (msl_no + 1) % MISSILE_MAX  # 미사일 번호 순환

    elif typ == 10:  # 탄막 모드 (확산형 미사일 발사)
        for a in range(160, 390, 10):  # 160도에서 380도까지 10도 간격으로 확산 발사
            msl_f[msl_no] = True
            msl_x[msl_no] = x  # 미사일 X좌표를 기체 중앙으로 설정
            msl_y[msl_no] = y - 50  # 미사일 Y좌표를 기체보다 위로 설정
            msl_a[msl_no] = a  # 각도에 따라 미사일 방향 설정
            msl_no = (msl_no + 1) % MISSILE_MAX  # 미사일 번호 순환


def move_missile(scrn):  # 탄환 이동
    for i in range(MISSILE_MAX):  # 모든 미사일 검사 (최대 미사일 개수까지 반복)
        if msl_f[i] == True:  # 해당 미사일이 활성화된 경우만 처리
            # 미사일의 위치를 발사 각도에 따라 이동 (속도 36)
            msl_x[i] = msl_x[i] + 36 * math.cos(math.radians(msl_a[i]))  
            msl_y[i] = msl_y[i] + 36 * math.sin(math.radians(msl_a[i]))
            
            # 미사일 이미지를 회전 및 크기 조정 후 화면에 출력
            img_rz = pygame.transform.rotozoom(img_weapon, -90 - msl_a[i], 1.0)
            scrn.blit(img_rz, [msl_x[i] - img_rz.get_width() / 2, msl_y[i] - img_rz.get_height() / 2])
            
            # 화면 밖으로 벗어난 미사일은 비활성화
            if msl_y[i] < 0 or msl_x[i] < 0 or msl_x[i] > 960:  # 위쪽, 왼쪽, 오른쪽 화면 경계 체크
                msl_f[i] = False  # 미사일 비활성화

def bring_enemy():  # 적 기체 등장
    # 시간에 따라 적 기체를 등장시키는 함수
    sec = tmr / 30  # tmr(타이머)를 30으로 나누어 초 단위로 변환
    if 0 < sec and sec < 25:  # 시작 후 0~25초 동안
        if tmr % 15 == 0:  # 15프레임마다 실행
            # 적 기체 1번 등장 (화면 상단에서 아래로 이동)
            set_enemy(random.randint(20, 940), LINE_T, 90, EMY_ZAKO, 8, 1)  

    if 30 < sec and sec < 55:  # 30~55초 동안
        if tmr % 10 == 0:  # 10프레임마다 실행
            # 적 기체 2번 등장
            set_enemy(random.randint(20, 940), LINE_T, 90, EMY_ZAKO + 1, 12, 1)  

    if 60 < sec and sec < 85:  # 60~85초 동안
        if tmr % 15 == 0:  # 15프레임마다 실행
            # 적 기체 3번 등장 (랜덤 각도로 이동)
            set_enemy(random.randint(100, 860), LINE_T, random.randint(60, 120), EMY_ZAKO + 2, 6, 3)

    if 90 < sec and sec < 115:  # 90~115초 동안
        if tmr % 20 == 0:  # 20프레임마다 실행
            # 적 기체 4번 등장
            set_enemy(random.randint(100, 860), LINE_T, 90, EMY_ZAKO + 3, 12, 2)

    if 120 < sec and sec < 145:  # 120~145초 동안 두 종류의 적 등장
        if tmr % 20 == 0:
            # 적 기체 1번과 3번 동시에 등장
            set_enemy(random.randint(20, 940), LINE_T, 90, EMY_ZAKO, 8, 1)
            set_enemy(random.randint(100, 860), LINE_T, random.randint(60, 120), EMY_ZAKO + 2, 6, 3)

    if 150 < sec and sec < 175:  # 150~175초 동안 두 방향에서 등장
        if tmr % 20 == 0:
            # 아래에서 위로 이동하는 적 1번
            set_enemy(random.randint(20, 940), LINE_B, 270, EMY_ZAKO, 8, 1)
            # 위에서 랜덤 각도로 이동하는 적 2번
            set_enemy(random.randint(20, 940), LINE_T, random.randint(70, 110), EMY_ZAKO + 1, 12, 1)

    if 180 < sec and sec < 205:  # 180~205초 동안 두 종류의 적 등장
        if tmr % 20 == 0:
            # 적 기체 3번과 4번 등장
            set_enemy(random.randint(100, 860), LINE_T, random.randint(60, 120), EMY_ZAKO + 2, 6, 3)
            set_enemy(random.randint(100, 860), LINE_T, 90, EMY_ZAKO + 3, 12, 2)

    if 210 < sec and sec < 235:  # 210~235초 동안 양쪽에서 등장
        if tmr % 20 == 0:
            # 왼쪽에서 오른쪽으로 이동하는 적 1번
            set_enemy(LINE_L, random.randint(40, 680), 0, EMY_ZAKO, 12, 1)
            # 오른쪽에서 왼쪽으로 이동하는 적 2번
            set_enemy(LINE_R, random.randint(40, 680), 180, EMY_ZAKO + 1, 18, 1)

    if 240 < sec and sec < 265:  # 240~265초 동안 총공격
        if tmr % 30 == 0:
            # 다양한 종류의 적 기체 등장
            set_enemy(random.randint(20, 940), LINE_T, 90, EMY_ZAKO, 8, 1)
            set_enemy(random.randint(20, 940), LINE_T, 90, EMY_ZAKO + 1, 12, 1)
            set_enemy(random.randint(100, 860), LINE_T, random.randint(60, 120), EMY_ZAKO + 2, 6, 3)
            set_enemy(random.randint(100, 860), LINE_T, 90, EMY_ZAKO + 3, 12, 2)

    if tmr == 30 * 270:  # 270초에 보스 등장
        # 보스는 화면 중앙 상단에서 등장
        set_enemy(480, -210, 90, EMY_BOSS, 4, 200)

def set_enemy(x, y, a, ty, sp, sh):  
    # 적 기체를 설정하는 함수
    global emy_no  # 적 기체 인덱스를 전역 변수로 사용
    while True:
        if emy_f[emy_no] == False:  # 비활성화된 슬롯을 찾으면 설정
            emy_f[emy_no] = True  # 적 기체 활성화
            emy_x[emy_no] = x  # X좌표 설정
            emy_y[emy_no] = y  # Y좌표 설정
            emy_a[emy_no] = a  # 이동 각도 설정
            emy_type[emy_no] = ty  # 적 기체 유형 설정
            emy_speed[emy_no] = sp  # 이동 속도 설정
            emy_shield[emy_no] = sh  # 체력 설정
            emy_count[emy_no] = 0  # 추가 카운터 초기화
            break  # 설정 완료 후 반복 종료
        # 다음 인덱스로 이동 (순환 구조)
        emy_no = (emy_no + 1) % ENEMY_MAX  

def move_enemy(scrn):  # 적 기체 이동
    global idx, tmr, score, hisco, new_record, ss_shield
    for i in range(ENEMY_MAX):  # 모든 적 기체 처리
        if emy_f[i] == True:  # 활성화된 적만 이동
            ang = -90 - emy_a[i]  # 적 기체의 기본 회전 각도 설정
            png = emy_type[i]  # 적 기체의 이미지 타입 설정
            if emy_type[i] < EMY_BOSS:  # 일반 적 기체 이동 처리
                emy_x[i] += emy_speed[i] * math.cos(math.radians(emy_a[i]))  # 각도에 따라 X좌표 이동
                emy_y[i] += emy_speed[i] * math.sin(math.radians(emy_a[i]))  # 각도에 따라 Y좌표 이동
                if emy_type[i] == 4:  # 진행 방향을 변경하는 특수 적
                    emy_count[i] += 1  # 이동 카운트 증가
                    ang = emy_count[i] * 10  # 회전 각도 변경
                    if emy_y[i] > 240 and emy_a[i] == 90:  # 특정 조건에서 방향 전환
                        emy_a[i] = random.choice([50, 70, 110, 130])  # 새로운 이동 각도 설정
                        set_enemy(emy_x[i], emy_y[i], 90, EMY_BULLET, 6, 0)  # 적 탄환 발사
                # 화면 경계를 벗어난 적 비활성화
                if emy_x[i] < LINE_L or emy_x[i] > LINE_R or emy_y[i] < LINE_T or emy_y[i] > LINE_B:
                    emy_f[i] = False
            else:  # 보스 기체 이동 처리
                if emy_count[i] == 0:  # 보스 초기 이동 (아래로 이동)
                    emy_y[i] += 2
                    if emy_y[i] >= 200:  # 특정 위치에 도달하면 상태 변경
                        emy_count[i] = 1
                elif emy_count[i] == 1:  # 보스가 왼쪽으로 이동
                    emy_x[i] -= emy_speed[i]
                    if emy_x[i] < 200:  # 특정 위치에서 탄환 발사 후 방향 전환
                        for j in range(0, 10):  # 탄환 여러 개 발사
                            set_enemy(emy_x[i], emy_y[i] + 80, j * 20, EMY_BULLET, 6, 0)
                        emy_count[i] = 2
                else:  # 보스가 오른쪽으로 이동
                    emy_x[i] += emy_speed[i]
                    if emy_x[i] > 760:  # 특정 위치에서 탄환 발사 후 방향 전환
                        for j in range(0, 10):  # 탄환 여러 개 발사
                            set_enemy(emy_x[i], emy_y[i] + 80, j * 20, EMY_BULLET, 6, 0)
                        emy_count[i] = 1
                if emy_shield[i] < 100 and tmr % 30 == 0:  # 보스가 체력이 낮을 때 주기적으로 탄환 발사
                    set_enemy(emy_x[i], emy_y[i] + 80, random.randint(60, 120), EMY_BULLET, 6, 0)

            if emy_type[i] != EMY_BULLET:  # 적과 플레이어의 미사일 충돌 검사
                w = img_enemy[emy_type[i]].get_width()  # 적 이미지의 너비
                h = img_enemy[emy_type[i]].get_height()  # 적 이미지의 높이
                r = int((w + h) / 4) + 12  # 충돌 반경 설정
                er = int((w + h) / 4)  # 효과 범위 설정
                for n in range(MISSILE_MAX):  # 모든 미사일과 충돌 체크
                    if msl_f[n] == True and get_dis(emy_x[i], emy_y[i], msl_x[n], msl_y[n]) < r * r:
                        msl_f[n] = False  # 충돌한 미사일 비활성화
                        set_effect(emy_x[i] + random.randint(-er, er), emy_y[i] + random.randint(-er, er))  # 폭발 효과
                        if emy_type[i] == EMY_BOSS:  # 보스 기체는 깜빡임 효과 처리
                            png = emy_type[i] + 1
                        emy_shield[i] -= 1  # 적 체력 감소
                        score += 100  # 점수 증가
                        if score > hisco:  # 최고 점수 갱신 확인
                            hisco = score
                            new_record = True
                        if emy_shield[i] == 0:  # 적 체력이 0이면 제거
                            emy_f[i] = False
                            if ss_shield < 100:  # 플레이어 실드 회복
                                ss_shield += 1
                            if emy_type[i] == EMY_BOSS and idx == 1:  # 보스 격추 시 게임 클리어
                                idx = 3
                                tmr = 0
                                for j in range(10):  # 폭발 효과 출력
                                    set_effect(emy_x[i] + random.randint(-er, er), emy_y[i] + random.randint(-er, er))
                                # se_explosion.play()  # 폭발 효과음 재생

            # 적 기체 이미지 회전 및 화면에 출력
            img_rz = pygame.transform.rotozoom(img_enemy[png], ang, 1.0)
            scrn.blit(img_rz, [emy_x[i] - img_rz.get_width() / 2, emy_y[i] - img_rz.get_height() / 2])

def set_effect(x, y):  # 폭발 효과 설정
    global eff_no
    eff_p[eff_no] = 1  # 효과 활성화
    eff_x[eff_no] = x  # 폭발 효과 X좌표
    eff_y[eff_no] = y  # 폭발 효과 Y좌표
    eff_no = (eff_no + 1) % EFFECT_MAX  # 효과 인덱스 순환 처리

def draw_effect(scrn):  # 폭발 연출 함수
    for i in range(EFFECT_MAX):  # 최대 폭발 효과 개수만큼 반복
        if eff_p[i] > 0:  # 폭발 효과가 활성화된 경우만 처리
            scrn.blit(img_explode[eff_p[i]], [eff_x[i] - 48, eff_y[i] - 48])  # 폭발 이미지를 화면에 출력
            eff_p[i] = eff_p[i] + 1  # 프레임 진행 (다음 폭발 이미지로 이동)
            if eff_p[i] == 6:  # 폭발 효과가 끝났으면 초기화
                eff_p[i] = 0  # 폭발 효과 비활성화

def main():  # 메인 루프 함수
    global idx, tmr, score, new_record, bg_y, ss_x, ss_y, ss_d, ss_shield, ss_muteki
    global se_barrage, se_damage, se_explosion, se_shot  # 전역 변수 선언

    pygame.init()  # Pygame 초기화
    pygame.display.set_caption("Galaxy Lancer")  # 게임 창 제목 설정
    screen = pygame.display.set_mode((960, 720))  # 게임 화면 크기 설정
    clock = pygame.time.Clock()  # 프레임 관리를 위한 Clock 객체 생성

    while True:
        tmr = tmr + 1  # 타이머 증가 (게임 진행 시간)
        for event in pygame.event.get():  # 이벤트 처리
            if event.type == QUIT:  # 창을 닫을 경우 종료
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:  # 키보드 입력 이벤트 처리
                if event.key == K_F1:  # F1 키: 전체 화면 전환
                    screen = pygame.display.set_mode((960, 720), FULLSCREEN)
                if event.key == K_F2 or event.key == K_ESCAPE:  # F2 또는 ESC 키: 창 모드 전환
                    screen = pygame.display.set_mode((960, 720))

        # 배경 스크롤 처리
        bg_y = (bg_y + 16) % 720  # 배경 y 좌표를 이동시켜 스크롤 효과
        screen.blit(img_galaxy, [0, bg_y - 720])  # 배경 이미지 위쪽 부분 출력
        screen.blit(img_galaxy, [0, bg_y])  # 배경 이미지 아래쪽 부분 출력

        key = pygame.key.get_pressed()  # 키 입력 상태 확인

        if idx == 0:  # 타이틀 화면
            img_rz = pygame.transform.rotozoom(img_title[0], -tmr % 360, 1.0)  # 타이틀 이미지 회전 효과
            screen.blit(img_rz, [480 - img_rz.get_width() / 2, 280 - img_rz.get_height() / 2])
            screen.blit(img_title[1], [70, 160])  # 서브 타이틀 출력
            draw_text(screen, "Press [SPACE] to start!", 480, 600, 50, SILVER)  # 시작 안내 메시지 출력
            if key[K_SPACE] == 1:  # 스페이스 키 입력 시 게임 시작
                idx = 1  # 게임 상태를 "플레이 중"으로 전환
                tmr = 0  # 타이머 초기화
                score = 0  # 점수 초기화
                new_record = False  # 새 기록 여부 초기화
                ss_x = 480  # 플레이어 기체 x 좌표 초기화
                ss_y = 600  # 플레이어 기체 y 좌표 초기화
                ss_d = 0  # 플레이어 상태 초기화
                ss_shield = 100  # 실드 초기화
                ss_muteki = 0  # 무적 시간 초기화
                for i in range(ENEMY_MAX):  # 모든 적 비활성화
                    emy_f[i] = False
                for i in range(MISSILE_MAX):  # 모든 미사일 비활성화
                    msl_f[i] = False

        if idx == 1:  # 게임 플레이 중
            move_starship(screen, key)  # 플레이어 기체 이동 처리
            move_missile(screen)  # 미사일 이동 처리
            bring_enemy()  # 적 등장 설정
            move_enemy(screen)  # 적 이동 처리

        if idx == 2:  # 게임 오버 상태
            move_missile(screen)  # 미사일 이동 처리
            move_enemy(screen)  # 적 이동 처리
            if tmr <= 90:  # 폭발 연출 (90프레임 동안)
                if tmr % 5 == 0:  # 5프레임마다 폭발 효과 생성
                    set_effect(ss_x + random.randint(-60, 60), ss_y + random.randint(-60, 60))
            if tmr > 120:  # 120프레임 이후 게임 오버 메시지 표시
                draw_text(screen, "GAME OVER", 480, 300, 80, RED)
                if new_record == True:  # 새 기록인 경우 표시
                    draw_text(screen, "NEW RECORD " + str(hisco), 480, 400, 60, CYAN)
            if tmr == 400:  # 400프레임 후 타이틀 화면으로 돌아감
                idx = 0
                tmr = 0

        if idx == 3:  # 게임 클리어 상태
            move_starship(screen, key)  # 플레이어 기체 이동 처리
            move_missile(screen)  # 미사일 이동 처리
            if tmr < 30 and tmr % 2 == 0:  # 클리어 연출 (빨간색 깜빡임)
                pygame.draw.rect(screen, (192, 0, 0), [0, 0, 960, 720])
            if tmr > 120:  # 120프레임 이후 게임 클리어 메시지 표시
                draw_text(screen, "GAME CLEAR", 480, 300, 80, SILVER)
                if new_record == True:  # 새 기록인 경우 표시
                    draw_text(screen, "NEW RECORD " + str(hisco), 480, 400, 60, CYAN)
            if tmr == 400:  # 400프레임 후 타이틀 화면으로 돌아감
                idx = 0
                tmr = 0

        draw_effect(screen)  # 폭발 연출 처리
        draw_text(screen, "SCORE " + str(score), 200, 30, 50, SILVER)  # 현재 점수 표시
        draw_text(screen, "HISCORE " + str(hisco), 760, 30, 50, CYAN)  # 최고 점수 표시
        if idx != 0:  # 플레이어 실드 상태 표시
            screen.blit(img_shield, [40, 680])  # 실드 아이콘 출력
            pygame.draw.rect(screen, (64, 32, 32), [40 + ss_shield * 4, 680, (100 - ss_shield) * 4, 12])  # 실드 게이지 표시

        pygame.display.update()  # 화면 업데이트
        clock.tick(30)  # 프레임 속도 설정 (30FPS)

if __name__ == '__main__':
    main()


