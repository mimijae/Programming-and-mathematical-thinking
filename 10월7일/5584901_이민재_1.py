# 다음과 같이 각각 덧셈, 뺄셈, 곱셈, 나눗셈을 수행하는 함수 add, subtract, multiply,
# divide를 완성하시오.
#
# 덧셈 함수
def add(a, b):
    return a + b  # a와 b의 합을 반환

# 뺄셈 함수
def subtract(a, b):
    return a - b  # a에서 b를 뺀 값을 반환

# 곱셈 함수
def multiply(a, b):
    return a * b  # a와 b의 곱을 반환

# 나눗셈 함수
def divide(a, b):
    return a / b  # a를 b로 나눈 값을 반환

# 함수들을 테스트
print(add(7, 4))        # 7 + 4 = 11
print(subtract(7, 4))   # 7 - 4 = 3
print(multiply(7, 4))   # 7 * 4 = 28
print(divide(7, 4))     # 7 / 4 = 1.75
