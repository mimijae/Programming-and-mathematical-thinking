# 문제 2. 사용자로부터 1 보다 크거나 같은 정수 하나를 입력받아 1부터 입력받은 정수까지
# 의 총합을 계산하고 출력하는 프로그램을 작성하시오.
# 실행결과:
# 1 이상의 정수 입력> 11
# 1부터 11까지의 총합은 66입니다

numbers = int(input("1 이상의 정수 입력> "))

# n=int(input())

result = 0

for n in range(1, numbers+1):
    result += n

print(f"1부터 11까지의 총합은 {result}입니다")