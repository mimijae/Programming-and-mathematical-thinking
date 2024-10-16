# 문제 4. 주어진 양의 정수 n에 대해 다음 연산을 수행하는 함수를 완성하시오.
# 1 + 1/2 + 1/4 + 1/8 + ... + 1/2^n
# def my_sum(n):
# ... # 생략된 부분
# print(my_sum(5))

def my_sum(n):
    result = 0
    for i in range(n + 1):
        result += 1 / (2 ** i)
    return result

print(my_sum(5))
