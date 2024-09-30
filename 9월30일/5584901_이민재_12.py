# 문제 12. 사용자로부터 숫자를 입력받아 모든 약수를 출력하는 프로그램을 작성하시오.

# 숫자를 입력하시오> 36
# 1, 2, 3, 4, 6, 9, 12, 18, 36

num = int(input("숫자를 입력하시오> "))

# 약수를 저장할 리스트
divisors = []

for i in range(1, num + 1):
    if num % i == 0:
        divisors.append(i)

print(", ".join(map(str, divisors)))
