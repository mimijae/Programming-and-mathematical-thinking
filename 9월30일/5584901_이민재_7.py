# 영어 대문자 O를 이용해 다음과 같이 출력하는 프로그램을 작성하시오.
# OO       OO
#  OO     OO
#   OO   OO
#    OO OO
#     OOO

n = 5
spaces_between = 7
for i in range(n):
    if i < n - 1:
        print(' ' * i + 'OO' + ' ' * (spaces_between - 2 * i) + 'OO')
    else:
        print(' ' * i + 'OOO')













# 문제: 별 피라미드 출력
#     *
#    ***
#   *****
#  *******
# *********

# def star_pyramid(n):
#     for i in range(1, n + 1):
#         # 공백과 별을 조합하여 출력
#         print(' ' * (n - i) + '*' * (2 * i - 1))

# # 사용자로부터 층 수를 입력받아 출력
# layers = int(input("피라미드의 층 수를 입력하시오> "))
# star_pyramid(layers)




# 문제 1: 숫자 피라미드 출력
# 숫자와 숫자의 개수를 입력 받아 아래와 같은 피라미드를 출력하는 프로그램을 작성하시오.
# 예를 들어 숫자 1과 5를 입력하면:

#     1
#    121
#   12321
#  1234321
# 123454321

# def number_pyramid(n):
#     for i in range(1, n+1):
#         # 왼쪽 공백, 숫자 오름차순, 숫자 내림차순 출력
#         print(" " * (n - i) + "".join(str(j) for j in range(1, i + 1)) + "".join(str(j) for j in range(i - 1, 0, -1)))

# number_pyramid(5)




# 문제 2: 별 패턴 다이아몬드

# 정수를 입력받아 아래와 같은 다이아몬드 모양을 출력하는 프로그램을 작성하시오.

#   *
#  ***
# *****
#  ***
#   *

# def diamond(n):
#     for i in range(n):
#         print(" " * (n - i - 1) + "*" * (2 * i + 1))
#     for i in range(n - 2, -1, -1):
#         print(" " * (n - i - 1) + "*" * (2 * i + 1))

# diamond(3)


# 문제 3: 테두리 사각형
# 정사각형의 크기를 입력 받아 아래와 같이 테두리만 출력하는 프로그램을 작성하시오.

# *****
# *   *
# *   *
# *   *
# *****
# def border_square(size):
#     for i in range(size):
#         if i == 0 or i == size - 1:
#             print("*" * size)
#         else:
#             print("*" + " " * (size - 2) + "*")

# border_square(5)


# 문제 4: 좌우 대칭 숫자 삼각형
# 정수를 입력 받아 아래와 같은 좌우 대칭 숫자 삼각형을 출력하는 프로그램을 작성하시오.

# 1
# 22
# 333
# 4444
# 55555

# def symmetric_triangle(n):
#     for i in range(1, n + 1):
#         print(str(i) * i)

# symmetric_triangle(5)


# 문제 6: 홀수 마름모 출력
# 홀수를 입력 받아 아래와 같은 마름모를 출력하는 프로그램을 작성하시오.

# 예:
#   *
#  ***
# *****
#  ***
#   *

# def odd_diamond(n):
#     half = n // 2
#     for i in range(half + 1):
#         print(" " * (half - i) + "*" * (2 * i + 1))
#     for i in range(half - 1, -1, -1):
#         print(" " * (half - i) + "*" * (2 * i + 1))

# odd_diamond(5)


# 문제 5: 피보나치 수열 패턴 출력
# 정수를 입력 받아 해당 길이까지의 피보나치 수열을 한 줄에 출력하는 프로그램을 작성하시오.

# 예:
# 1 1 2 3 5 8 13 21 ...

# def fibonacci_sequence(n):
#     a, b = 1, 1
#     result = []
#     for _ in range(n):
#         result.append(str(a))
#         a, b = b, a + b
#     print(" ".join(result))

# fibonacci_sequence(10)
