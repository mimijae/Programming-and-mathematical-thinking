# 하나의 문자와 숫자를 입력하면 아래와 같이 출력하는 프로그램을 작성하시오.
# def print_char(c, n):
# ... # 생략된 부분
# print_char('+', 4)
# 실행결과:


#    +
#   ++
#  +++
# ++++

def print_char(c, n):
    for i in range(0, n):
        print((" "*(n-i-1)+c*(i+1)))

print_char('+', 4)



# +
# + +
# + + +
# + + + +

def print_char(c, n):
    for i in range(0, n):
        print((c*(i+1)+" "*(n-i-1)))

print_char('+', 4)