# 3. random 모듈을 이용해-1 <= x <= 1, -1 <= y <= 1 를 만족하는 10개의 (x, y) 좌표를 출력하는
# 프로그램을 작성하시오.


import random

# 좌표 생성 및 출력
for _ in range(10):
    x = random.uniform(-1, 1)  # -1 <= x <= 1 범위의 난수 생성
    y = random.uniform(-1, 1)  # -1 <= y <= 1 범위의 난수 생성
    print(f'({x}, {y})')

# 좌표 생성 및 출력
for _ in range(10):
    x = random.random() * 2 - 1  # -1 <= x <= 1 범위의 난수 생성
    y = random.random() * 2 - 1  # -1 <= y <= 1 범위의 난수 생성
    print(f'({x}, {y})')
