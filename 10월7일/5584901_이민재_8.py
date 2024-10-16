# def add_list(list_0, list_1):
# ... # 생략된 부분
# list_0 = [2, 3, 4]
# list_1 = [1, -1, 2]
# list_2 = add_list(list_0, list_1)
# print(list_2)


def add_list(list_0, list_1):
    result = []
    for i in range(len(list_0)):
        result.append(list_0[i] + list_1[i])
    return result

list_0 = [2, 3, 4]
list_1 = [1, -1, 2]
list_2 = add_list(list_0, list_1)
print(list_2)
