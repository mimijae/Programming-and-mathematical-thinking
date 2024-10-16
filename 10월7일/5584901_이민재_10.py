# 다음 수식을 이용해 원하는 갯수의 수열을 생성하는 프로그램을 작성하시오.
# 𝑎𝑘+1 = 2𝑎𝑘 + 1, 𝑘 = 0, 1, 2, … , 𝑛
# def ak(a0, n):
# ... # 생략된 부분
# print(ak(1, 10))

def ak(a0, n):
    result = [a0]
    for i in range(n):
        a_next = 2 * result[-1] + 1
        result.append(a_next)
    return result

print(ak(1, 10))
