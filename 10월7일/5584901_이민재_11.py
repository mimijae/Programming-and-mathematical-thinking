import math

def stand(x):
    mean = sum(x) / len(x)  # 평균 (mean) 계산 
    variance = sum((i - mean) ** 2 for i in x) / len(x) # 분산 (variance) 계산
    std_dev = math.sqrt(variance) # 표준편차
    
    return [(i - mean) / std_dev for i in x] # 각 값에 대해 표준화된 값 계산

a = [1, 2, 3, 4, 5]
print(stand(a))
