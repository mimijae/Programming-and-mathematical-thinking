### 문제 1: 1부터 100까지의 소수 찾기
# ```
# 1,100 을 입력하여 1부터 100 사이의 소수를 출력하는 프로그램을 작성하시오.

# 출력:
# 2, 3, 5, 7, 11, 13, 17, ..., 97
# ```

prime = []
for n in range(2,100):
    is_prime=True
    for i in range(2,n):
        if(n%i==0):
            is_prime=False
            break
    if is_prime:
        prime.append(n)

# 결과 출력
print("1부터 100까지의 수 중 소수:", ", ".join(map(str, prime)))


# //====================================================================================================================================//

### 문제 2: 가위바위보 게임
# ```
# 사용자와 컴퓨터가 가위, 바위, 보 게임을 진행하는 프로그램을 작성하시오.
# 컴퓨터는 무작위로 가위, 바위, 보 중 하나를 선택합니다.
# 사용자는 가위, 바위, 보 중 하나를 입력하여 승패를 확인할 수 있습니다.
# 게임은 무승부일 수도 있고, 사용자 또는 컴퓨터가 이길 수도 있습니다.

# 예시 실행:
# 가위, 바위, 보 중 하나를 선택하시오: 가위
# 사용자: 가위, 컴퓨터: 바위
# 컴퓨터가 이겼습니다.
# ```

# **풀이:**
import random

def play_rps():
    options = ["가위", "바위", "보"]
    computer_choice = random.choice(options)
    user_choice = input("가위, 바위, 보 중 하나를 선택하시오: ")

    print(f"사용자: {user_choice}, 컴퓨터: {computer_choice}")

    if user_choice == computer_choice:
        print("무승부입니다.")
    elif (user_choice == "가위" and computer_choice == "보") or \
        (user_choice == "바위" and computer_choice == "가위") or \
        (user_choice == "보" and computer_choice == "바위"):
        print("사용자가 이겼습니다!")
    else:
        print("컴퓨터가 이겼습니다.")

play_rps()

# ### 설명:
# 1. `options` 리스트에는 가위, 바위, 보가 저장되어 있습니다.
# 2. `random.choice(options)`를 사용하여 컴퓨터의 선택을 무작위로 결정합니다.
# 3. 사용자의 입력을 받아, 컴퓨터의 선택과 비교하여 결과를 판단합니다:
#    - 사용자의 선택과 컴퓨터의 선택이 같으면 무승부.
#    - 사용자가 이길 조건을 체크하여 결과를 출력.
#    - 나머지 경우는 컴퓨터가 이긴 것으로 처리합니다.



# //====================================================================================================================================//

# 시각 차이 계산하기
# 두 개의 시각(24시간 형식)을 입력받아, 두 시각 사이의 시간 차이를 계산하는 프로그램을 작성하시오.
# 예를 들어 14:30과 18:45를 입력받으면:

# >>> python my_sol5.py
# 두 시각의 차이는 4시간 15분입니다.


# def time_difference(start, end):
#     start_h, start_m = map(int, start.split(":"))
#     end_h, end_m = map(int, end.split(":"))

#     start_minutes = start_h * 60 + start_m
#     end_minutes = end_h * 60 + end_m

#     diff_minutes = end_minutes - start_minutes
#     if diff_minutes < 0:
#         diff_minutes += 24 * 60  # 만약 종료 시간이 시작 시간보다 빠르면 하루를 더함

#     hours = diff_minutes // 60
#     minutes = diff_minutes % 60

#     return hours, minutes

# start_time = input("시작 시각을 입력하시오 (HH:MM): ")
# end_time = input("종료 시각을 입력하시오 (HH:MM): ")

# h, m = time_difference(start_time, end_time)
# print(f"두 시각의 차이는 {h}시간 {m}분입니다.")



# //====================================================================================================================================//

### 문제 3: 도형 문제들 모임

# 문제 3. 영어 대문자 O를 이용해 다음과 같이 출력하는 프로그램을 작성하시오.
# OOOOOOOOO
#  OOOOOOO
#   OOOOO
#    OOO
#     O

n = 9

for i in range(5):
    print(" " * i + "O" * (n - 2 * i))


# //====================================================================================================================================//


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


# //====================================================================================================================================//


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


# //====================================================================================================================================//


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


# //====================================================================================================================================//


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



# //====================================================================================================================================//


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



# //====================================================================================================================================//


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


# //====================================================================================================================================//


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



# //====================================================================================================================================//


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


# //====================================================================================================================================//


# 정렬된 정수 배열에서 중복된 요소를 제거하고, 중복을 제거한 배열의 길이를 반환하시오.

# 입력:
# nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

# 출력:
# 5 (중복이 제거된 배열: [0, 1, 2, 3, 4])

# def remove_duplicates(nums):
#     if not nums:
#         return 0
    
#     index = 0
#     for i in range(1, len(nums)):
#         if nums[i] != nums[index]:
#             index += 1
#             nums[index] = nums[i]
#     return index + 1

# nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
# length = remove_duplicates(nums)
# print(length)


# # //====================================================================================================================================//


# 문제 5: 단어 개수 세기
# 사용자로부터 문장을 입력받아, 문장에 포함된 단어의 개수를 출력하는 프로그램을 작성하시오.

# 입력 예시:
# 문장을 입력하시오: This is a simple sentence.

# 출력 예시:
# 단어 개수: 5

# def count_words(sentence):
#     words = sentence.split()
#     return len(words)

# sentence = input("문장을 입력하시오: ")
# print(f"단어 개수: {count_words(sentence)}")



# //====================================================================================================================================//


# 문제: 윤년인지 판별하기

# 사용자로부터 연도를 입력받아, 해당 연도가 윤년인지 아닌지를 출력하는 프로그램을 작성하시오.

# 윤년의 조건:
# 1. 연도가 4로 나누어떨어지지만, 100으로 나누어떨어지지 않는 경우는 윤년이다.
# 2. 또는 연도가 400으로 나누어떨어지면 윤년이다.

# 입력 예시:
# 연도를 입력하시오: 2024

# 출력 예시:
# 2024년은 윤년입니다.

# 입력 예시:
# 연도를 입력하시오: 1900

# 출력 예시:
# 1900년은 윤년이 아닙니다.

# def is_leap_year(year):
#     # 4로 나누어 떨어지면서 100으로는 나누어 떨어지지 않거나, 400으로 나누어 떨어지면 윤년
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         return True
#     else:
#         return False

# # 사용자로부터 연도 입력받기
# year = int(input("연도를 입력하시오: "))

# # 윤년 여부 확인 및 출력
# if is_leap_year(year):
#     print(f"{year}년은 윤년입니다.")
# else:
#     print(f"{year}년은 윤년이 아닙니다.")


# //====================================================================================================================================//

# 돈 구하는 문제

# def currency_breakdown(amount):
#     # 화폐 단위를 큰 순서대로 리스트에 저장
#     denominations = [50000, 10000, 1000, 500, 100, 50, 10, 1]
#     counts = []  # 각 화폐 단위의 개수를 저장할 리스트

#     # 각 화폐 단위로 나누어 몇 개가 필요한지 계산
#     for denomination in denominations:
#         count = amount // denomination
#         counts.append(count)
#         amount %= denomination

#     # 결과 출력
#     print(f"오만원권: {counts[0]}개")
#     print(f"만원권: {counts[1]}개")
#     print(f"천원권: {counts[2]}개")
#     print(f"500원 동전: {counts[3]}개")
#     print(f"100원 동전: {counts[4]}개")
#     print(f"50원 동전: {counts[5]}개")
#     print(f"10원 동전: {counts[6]}개")
#     print(f"1원 동전: {counts[7]}개")

# # 사용자로부터 금액 입력받기
# amount = int(input("금액을 입력하시오: "))
# currency_breakdown(amount)

