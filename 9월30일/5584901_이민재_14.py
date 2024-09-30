# 문제 14. 다음 주어진 리스트(my_list_0)에 대하여 홀수에는 3을 곱하고 짝수에는 5를
# 곱하여 새로운 리스트(my_list_1)를 생성하고 출력하는 프로그램을 작성하시오.

# my_list_0 = [3, 11, 4, 8, 2, 12, 5]
# ... # 생략된 부분
# print(my_list_1)
# 실행결과:
# [9, 33, 20, 40, 10, 60, 15]

my_list_0 = [3, 11, 4, 8, 2, 12, 5]

my_list_1 = []

for num in my_list_0:
    if num % 2 != 0:
        my_list_1.append(num * 3)
    else:
        my_list_1.append(num * 5)

print(my_list_1)
