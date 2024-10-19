# def add_list(list_0, list_1):
# ... # 생략된 부분
# list_0 = [2, 3, 4]
# list_1 = [1, -1, 2]
# list_2 = add_list(list_0, list_1)
# print(list_2)


list_0 = [2, 3, 4]
list_1 = [1, -1, 2]

list_2=[]

def add_list(list_0, list_1):
    for i in range(0, len(list_0)):
        list_2.append(list_0[i] + list_1[i])
    return list_2


list_2 = add_list(list_0, list_1)



print(list_2)