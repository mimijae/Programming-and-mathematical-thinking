# 문제1의 리스트(my_list1)에 포함된 정수 중 최솟값과 최대값을 구하는 프로그램을
# 작성하시오. (단, min, max 함수 사용 불가)
# >>> python my_sol2.py
# 최솟값은 21, 최댓값은 99

my_list1 = [21, 39, 17, 47, 52, 91, 99, 42]

MAX = my_list1[0]
MIN = my_list1[0]

for i in range(0,len(my_list1)):
    if(MAX <my_list1[i]):
        MAX = my_list1[i]
    if(MIN>my_list1[i]):
        MIN = my_list1[i]
        
print(f"최솟값은 {MIN}, 최댓값은 {MAX}")
