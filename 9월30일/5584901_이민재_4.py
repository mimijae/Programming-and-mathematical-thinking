# 문제 4. 다음 리스트 my_list_0로부터 새로운 리스트 my_list_1과 my_list_2를 구성하고 출력
# 하는 프로그램을 작성하시오.

# my_list_0 = [20, 15, 37, 22, 8, 9, 49, 52, 34]
# ... # 생략된 부분
# print(my_list_1)
# print(my_list_2)
# 실행결과:
# [20, 22, 8, 52, 34]
# [15, 37, 9, 49]

my_list_0 = [20, 15, 37, 22, 8, 9, 49, 52, 34]

my_list_1=[]
my_list_2=[]

for i in my_list_0:
    if(i%2==0):
        my_list_1.append(i)
    else:
        my_list_2.append(i)

print(my_list_1)
print(my_list_2)
