# 문제 5. dict_sort()는 입력한 딕셔너리를 key에 따라 내림차순으로 정렬하는 함수이다.
# value에 따라 내림차순으로 정렬하도록 dict_sort() 함수를 수정하시오.
# def dict_sort(d):
# return dict(sorted(d.items(), key=lambda x: x[0], reverse=True))
# dict_1 = { 'car':200, 'house':500, 'watch':50, 'boat':300, 'land':600 }
# dict_2 = dict_sort(dict_1)
# print(dict_2)
# 즉, 아래와 같은 결과가 나오도록 dict_sort() 함수를 수정해야 함
# {'land': 600, 'house': 500, 'boat': 300, 'car': 200, 'watch': 50}

def dict_sort(d):
    return dict(sorted(d.items(), key=lambda x: x[1], reverse=True))

dict_1 = { 'car':200, 'house':500, 'watch':50, 'boat':300, 'land':600 }
dict_2 = dict_sort(dict_1)
print(dict_2)