# 사용자로부터 숫자를 입력받아 다음과 같이 출력하는 프로그램을 작성하시오.

# 숫자를 입력하시오> 29082144
# 0 = 1, 1 = 1, 2 = 2, 4 = 2, 8 = 1, 9 = 1

number = input("숫자를 입력하시오> ")

count_dict = {}

for digit in number:
    if digit in count_dict:
        count_dict[digit] += 1
    else:
        count_dict[digit] = 1

for digit, count in sorted(count_dict.items()):
    print(f"{digit} = {count}")






