# 문제 2. 문제1에서 작성한 함수들을 활용해 다음 연산을 수행하는 프로그램을 작성하시오.
# (23 + 12) / (8 - 13) * 11

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

result = multiply(divide(add(23, 12), subtract(8, 13)), 11)
print(result)
