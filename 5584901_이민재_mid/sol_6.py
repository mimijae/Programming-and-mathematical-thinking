# 문제 6. 다음 두 딕셔너리(math_mid, math_final)는 한 학급 학생들의 각각 중간, 기말
# 수학시험 결과를 나타낸다. 이 결과를 바탕으로 각 학생의 석차(순위)를 계산하고
# 출력하는 프로그램을 작성하시오.
# math_mid = { 'A':77, 'B':95, 'C':85, 'D':70, 'E':85 }
# math_final = { 'A':85, 'B':85, 'C':90, 'D':90, 'E':93 }
# 프로그램 실행결과:
# A의 석차는 4등입니다.
# B의 석차는 1등입니다.
# C의 석차는 3등입니다.
# D의 석차는 5등입니다.
# E의 석차는 2등입니다.

def dict_sort(d):
    return dict(sorted(d.items(), key=lambda x: x[1], reverse=True))

def dict_sort2(d):
    return dict(sorted(d.items(), key=lambda x: x[0], reverse=False))

math_mid = { 'A':77, 'B':95, 'C':85, 'D':70, 'E':85 }
math_final = { 'A':85, 'B':85, 'C':90, 'D':90, 'E':93 }

result =  { 'A':0, 'B':0, 'C':0, 'D':0, 'E':0 }

grade = { 'A':0, 'B':0, 'C':0, 'D':0, 'E':0 }


for student in math_mid:
    result[student] = math_mid[student] + math_final[student]

result2 = dict_sort(result)

print(f"2번{result2}")

sum=1
for i in result2:
    result2[i] = sum
    sum +=1


print(f"순서{result2}")

result2 = dict_sort2(result2)

for i in result2:
    print(f"{i}의 석차는 {result2[i]}등입니다")


