# 문제 11. 사용자로부터 5개의 수를 입력받아 오름 차순으로 정렬하는 프로그램을 작성하
# 시오.

# 5개의 수를 입력하시오> 39 43 23 82 66
# 23 39 43 66 82

numbers = list(map(int, input("5개의 숫자를 입력하시오> ").split()))

for i in range(0, len(numbers)-1):
    for j in range(0, len(numbers)-1-i):
        if(numbers[j+1] < numbers[j]):
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
        
print(numbers)








# 1.
# 정렬된 정수 배열에서 중복된 요소를 제거하고, 중복을 제거한 배열의 길이를 반환하시오.

# 입력:
# nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

# 출력:
# 5 (중복이 제거된 배열: [0, 1, 2, 3, 4])

# def remove_duplicates(nums):
#     if not nums:
#         return 0
    
#     index = 0
#     for i in range(1, len(nums)):
#         if nums[i] != nums[index]:
#             index += 1
#             nums[index] = nums[i]
#     return index + 1

# nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
# length = remove_duplicates(nums)
# print(length)


#2.
# 정수 배열이 주어졌을 때, 특정 구간의 합을 빠르게 계산할 수 있는 프로그램을 작성하시오.

# 입력:
# nums = [1, 2, 3, 4, 5]
# 쿼리: (1, 3) => 배열의 인덱스 1부터 3까지의 합

# 출력:
# 9 (2 + 3 + 4)


# def prefix_sum(nums):
#     prefix = [0] * (len(nums) + 1)

#     for i in range(len(nums)):
#         prefix[i + 1] = prefix[i] + nums[i]

#     return prefix

# def range_sum(prefix, left, right):
#     return prefix[right + 1] - prefix[left]

# nums = [1, 2, 3, 4, 5]
# prefix = prefix_sum(nums)
# print(range_sum(prefix, 1, 3))

