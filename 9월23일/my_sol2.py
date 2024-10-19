# 2. 300,000초(sec)를 일, 시간, 분, 초 단위로 계산하는 프로그램(my_sol2.py)을 작성하시오.
# >>> python my_sol2.py
# 300,000초는 3일 11시간 20분 0초입니다.

sec = 300000

d = sec//(60*60*24)
sec %= (24*3600)
h = sec // 3600
sec %= 3600
m = sec // 60
sec %= 60

print(f"300,000초는 {d}일 {h}시간 {m}분 {sec}초 입니다.")


# 문제 5: 시각 차이 계산하기
# 두 개의 시각(24시간 형식)을 입력받아, 두 시각 사이의 시간 차이를 계산하는 프로그램을 작성하시오.
# 예를 들어 14:30과 18:45를 입력받으면:

# >>> python my_sol5.py
# 두 시각의 차이는 4시간 15분입니다.


# def time_difference(start, end):
#     start_h, start_m = map(int, start.split(":"))
#     end_h, end_m = map(int, end.split(":"))

#     start_minutes = start_h * 60 + start_m
#     end_minutes = end_h * 60 + end_m

#     diff_minutes = end_minutes - start_minutes
#     if diff_minutes < 0:
#         diff_minutes += 24 * 60  # 만약 종료 시간이 시작 시간보다 빠르면 하루를 더함

#     hours = diff_minutes // 60
#     minutes = diff_minutes % 60

#     return hours, minutes

# start_time = input("시작 시각을 입력하시오 (HH:MM): ")
# end_time = input("종료 시각을 입력하시오 (HH:MM): ")

# h, m = time_difference(start_time, end_time)
# print(f"두 시각의 차이는 {h}시간 {m}분입니다.")
