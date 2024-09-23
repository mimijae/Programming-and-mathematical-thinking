# 다음 리스트(my_list)에 포함된 수의 합계와 평균을 계산하는 프로그램(my_sol1.py)을
# 작성하시오.
# >>> python my_sol1.py
# 합계 = 440
# 평균 = 88.0
# my_list = [80, 90, 75, 95, 100]

my_list = [80, 90, 75, 95, 100]

sum1 = sum(my_list)
print(f"합계: {sum1}")

average = sum(my_list)/len(my_list)
print(f"평균: {average}")

