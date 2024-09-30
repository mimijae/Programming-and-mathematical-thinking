# 문제 3. 영어 대문자 O를 이용해 다음과 같이 출력하는 프로그램을 작성하시오.
# OOOOOOOOO
#  OOOOOOO
#   OOOOO
#    OOO
#     O

n = 9

for i in range(5):
    print(" " * i + "O" * (n - 2 * i))


