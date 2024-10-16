#  입력한 두 수의 최소공배수를 계산하고 반환하는 함수를 작성하시오.
# def lcm(num1, num2):
# ... # 생략된 부분
# print(lcm(36, 24))

def gcd(num1, num2):
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1

def lcm(num1, num2):
    return (num1 * num2) // gcd(num1, num2)

print(lcm(36, 24))
