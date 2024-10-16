# 문제 5. 숫자를 포함한 리스트를 입력하면 최댓값과 최솟값을 반환하는 함수를 완성하시오.
# def minmax(num_list):
# ... # 생략된 부분
# my_list = [3, 5, 11, -1, 9, 7]
# a, b = minmax(my_list)
# print(a, b)

def minmax(num_list):
    min_value = num_list[0]
    max_value = num_list[0]
    
    for num in num_list:
        if num < min_value:
            min_value = num
        if num > max_value:
            max_value = num
            
    return min_value, max_value

my_list = [3, 5, 11, -1, 9, 7]
a, b = minmax(my_list)
print(a, b)
