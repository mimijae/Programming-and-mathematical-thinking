# 문제 2. 사용자로부터 세 숫자를 입력받아 가장 큰 수와 가장 작은 수를 출력하는 프로그램
# 을 작성하시오.

# 실행예시:
# 세 숫자를 입력하세요> 21 44 8
# 가장 큰 수 = 44, 가장 작은 수 = 8

a=list(map(int, input().split()))

result1 = a[0]
result2 = a[0]

for s in a:
    if(result1 < s):
        result1=s
    if(result2 > s):
        result2=s

print(f"가장 큰 수 = {result1}, 가장 작은 수 = {result2}")