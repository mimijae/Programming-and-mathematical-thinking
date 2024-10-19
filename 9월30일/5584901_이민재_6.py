# 문제 6. 사용자로부터 5개의 숫자를 입력받아 평균과 분산을 출력하는 프로그램을 작성
# # 하시오.

# 5개의 숫자를 입력하시오> 3 9 13 22 1
# 평균 = 9.6
# 분산 = 70.8

numbers = list(map(int, input("5개의 숫자를 입력하시오> ").split()))

mean = sum(numbers) / len(numbers)

variance = sum((x - mean) ** 2 for x in numbers) / (len(numbers))

print(f"평균 = {mean:.2f}")
print(f"분산 = {variance:.2f}")