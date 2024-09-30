# 문제 10. 1부터 50까지의 수 중에서 소수(prime number)를 찾아 출력하는 프로그램을 작성
# 하시오. 

# 1부터 50까지의 수 중 소수: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

primes = []
for num in range(1, 51):
    if is_prime(num):
        primes.append(num)

# 결과 출력
print("1부터 50까지의 수 중 소수:", ", ".join(map(str, primes)))
