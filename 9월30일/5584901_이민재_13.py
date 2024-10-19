# 문제 13. 다음 두 딕셔너리(eng_1, eng_2)는 한 학급 학생들의 중간 기말 영어시험 점수를
# 나타낸다. 가장 크게 성적이 향상된 학생을 찾는 프로그램을 작성하시오.

# eng_1 = { ‘A’ : 80, ‘B’ : 85, ‘C’ : 90, ‘D’ : 75, ‘E’ : 83 }
# eng_2 = { ‘A’ : 85, ‘B’ : 80, ‘C’ : 87, ‘D’ : 85, ‘E’ : 90 }
# 실행결과:
# ‘D’ 학생이 가장 크게 성적이 향상됨

eng_1 = { 'A' : 80, 'B' : 85, 'C' : 90, 'D' : 75, 'E' : 83 }
eng_2 = { 'A' : 85, 'B' : 80, 'C' : 87, 'D' : 85, 'E' : 90 }

# max_improvement = 0
# top_student = ''

# for student in eng_1:
#     improvement = eng_2[student] - eng_1[student]
#     if improvement > max_improvement:
#         max_improvement = improvement
#         top_student = student

# # 결과 출력
# print(f"‘{top_student}’ 학생이 가장 크게 성적이 향상됨")

max = 0
student = ''

for s in eng_1:
    im = eng_2[s] - eng_1[s]
    if(im > max):
        max = im
        student = s

print(f"{student} {max}")
