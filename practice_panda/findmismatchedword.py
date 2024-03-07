# find uncommon word from string
# for example str1 ="Hello my name is adam. i am software developer"
# str2 = "Hello my name is neha. i am software engineer"
# result =["adam","neha","developer","engineer"]

def find_uncommon(A,B):
    list1 = A.split()
    list2 = B.split()
    result =[]
    for i in list1:
        if i not in list2:
            result.append(i)
    for i in list2:
        if i not in list1:
            result.append(i)

    print(list1)
    print(list2)
    res = list(set(result))
    return res



# from collections import Counter
 
 
# def UncommonWords(A, B):
#     A = A.split()
#     B = B.split()
#     frequency_arr1 = Counter(A)
#     frequency_arr2 = Counter(B)
#     result = []
#     print(frequency_arr1)
#     print(frequency_arr2)
#     for key in frequency_arr1:
#         if key not in frequency_arr2:
#             result.append(key)
#     for key in frequency_arr2:
#         if key not in frequency_arr1:
#             result.append(key)
 
#     return result


str1 ="Hello my name is adam. i am software developer  developer"
str2 ="Hello my name is neha. i am software engineer"
result = find_uncommon(str1,str2)
print(result)