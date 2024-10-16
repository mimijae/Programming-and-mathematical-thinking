# 13. 입력한 두 수의 최대공약수를 계산하고 반환하는 함수를 작성하시오.
# def gcd(num1, num2):
# ... # 생략된 부분
# print(gcd(36, 24))


def gcd(num1, num2):
    # 두 수 중 작은 값까지만 반복
    min_num = min(num1, num2)
    gcd_value = 1  # 기본적으로 1은 모든 수의 공통 약수
    for i in range(1, min_num + 1):
        if num1 % i == 0 and num2 % i == 0:
            gcd_value = i  # 공통 약수 업데이트
    return gcd_value

print(gcd(36, 24))
