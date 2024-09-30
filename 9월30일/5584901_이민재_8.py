# 문제 8. 다음 리스트 my_list_0로부터 다음과 같이 새로운 리스트 my_list_1를 구성하고
# 출력하는 프로그램을 작성하시오.

# my_list_0 = [201, 125, 137, 222, 811]
# ... # 생략된 부분
# print(my_list_1)
# 실행결과:
# [3, 8, 11, 6, 10]

my_list_0 = [201, 125, 137, 222, 811]
my_list_1=[]

def sum_of_digits(number):
    return sum(int(s) for s in str(number))

for i in my_list_0:
    my_list_1.append(sum_of_digits(i))

print(my_list_1)