# 2. time 모듈을 이용하여 아래 반복문이 몇 초 동안 실행되는지 출력하는 프로그램을
# 작성하시오.
# for n in range(1000000):
# print('n = ', n)

import time

# 시작 시간 기록
start_time = time.time()

# 반복문 실행
for n in range(1000000):
    print('n = ', n)

# 종료 시간 기록
end_time = time.time()

# 실행 시간 계산 및 출력
execution_time = end_time - start_time
print(f'반복문 실행 시간: {execution_time} 초')
