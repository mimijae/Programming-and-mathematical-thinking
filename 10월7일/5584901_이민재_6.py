# 문제 6. 임의의 갯수의 숫자를 입력하면 최댓값과 최솟값을 반환하는 함수를 완성하시오.
# def minmax(*num):
# ... # 생략된 부분
# a, b = minmax(3, 5, 11, -1, 9, 7)
# print(a, b)

def minmax(*num):
    min_value = num[0]
    max_value = num[0]
    
    for n in num:
        if n < min_value:
            min_value = n
        if n > max_value:
            max_value = n
            
    return min_value, max_value

a, b = minmax(3, 5, 11, -1, 9, 7)
print(a, b)
