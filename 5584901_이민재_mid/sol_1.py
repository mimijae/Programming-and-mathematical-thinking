# 문제 1. 사용자로부터 이름과 태어난 년도를 각각 입력받아 나이를 계산하고 다음과 같이
# 출력하는 프로그램을 작성하시오

import datetime
# 이름 입력> 김계명
# 태어난 연도 입력> 2001
# 김계명씨는 23살입니다.

name = input()

year = int(input())

result = 2024 - year

print(f"{name}씨는 {result}살입니다.")