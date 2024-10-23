# 그래프 그리는 코드를 활용하여 주어진 수학함수(f(x))의 그래프를 그리시오.
# import matplotlib.pyplot as plt
# x = [1, 2, 3, 4, 5]
# y = [1**2, 2**2, 3**2, 4**2, 5**2]
# plt.figure()
# plt.plot(x, y)
# plt.show()
# 𝑓 𝑥 =
# 3𝑥 − 1
# 𝑥2 + 1

import matplotlib.pyplot as plt

# x 값 설정
x = [1, 2, 3, 4, 5]

# f(x) 값 계산 (주어진 수식에 따라 계산)
y = [(3 * i - 1) / (i**2 + 1) for i in x]

# 그래프 그리기
plt.figure()
plt.plot(x, y)
plt.title("Graph of f(x) = (3x - 1) / (x^2 + 1)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.show()