# 문제 1. 사용자로부터 두 숫자를 입력받아 합, 차, 곱, 몫, 나머지를 출력하는 프로그램을
# 작성하시오.

# 실행예시:
# 두 숫자를 입력하세요> 23 4
# 합 = 27, 차 = 19, 곱 = 92, 몫 = 5, 나머지 = 3

n, k = map(int, input().split())

print(f"합 = {n+k}, 차 = {n-k}, 곱 = {n*k}, 몫 = {n//k}, 나머지 = {n%k}")