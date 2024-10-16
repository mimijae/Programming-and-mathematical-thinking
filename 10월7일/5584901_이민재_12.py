# 문제 12. 문자열로 된 두 수를 입력받아 덧셈한 결과를 반환하는 프로그램을 작성하시오.
# def add(num1, num2):
# ... # 생략된 부분
# print(add('123', '12'))

def add(num1, num2):
    return str(int(num1) + int(num2))

print(add('123', '12'))
