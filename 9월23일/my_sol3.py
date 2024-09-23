# 3. 다음 리스트(my_list2)에 포함된 정수 중에서 3 또는 7의 배수를 출력하는 프로그램
# (my_sol3.py)을 작성하시오.
# my_list2 = [21, 39, 17, 47, 52, 91, 99, 42]

# >>> python my_sol3.py
# 3 또는 7의 배수는 21, 39, 91, 99, 42 입니다.


my_list2 = [21, 39, 17, 47, 52, 91, 99, 42]
result = []
for r in my_list2:
    if(r%3==0 or r%7==0):
        result.append(r)

print(f"3 또는 7의 배수는 {result} 입니다")