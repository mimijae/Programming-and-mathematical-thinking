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