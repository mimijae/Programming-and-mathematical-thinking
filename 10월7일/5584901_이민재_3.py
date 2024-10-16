# 문제 3. 아래와 같이 나눗셈을 수행하고 몫과 나머지를 반환하는 함수 divrem를 완성하시오.
# def divrem(a, b):
# ... # 생략된 부분
# d, r = divrem(7,4)
# print(f’몫 = {d}, 나머지 = {r}’)

def divrem(a, b):
    return a // b, a % b

d, r = divrem(7, 4)
print(f'몫 = {d}, 나머지 = {r}')
