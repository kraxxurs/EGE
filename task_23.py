# def fn(cur, end):
#     if cur == end:
#         return 1
#     if cur < end or cur == 7:
#         return 0
#     if cur > end:
#         return(fn(cur-1, end) + fn(cur-4, end) + fn(cur//3, end))
    
# print(fn(19, 13) * fn(13, 2))
# answer: 68


# №8679
# def fn(cur, end):
#     if cur == end:
#         return 1
#     if cur > end:
#         return 0
#     if cur < end:
#         return(fn(cur+2, end) + fn(cur+5, end) + fn(cur*2, end))

# A = fn(7, 23) * fn(23, 85)
# B = fn(7, 45) * fn(45, 85)
# AB = fn(7, 23) * fn(23, 45) * fn(45, 85)
# print(A + B - AB)
# answer: 4 320 993


# №8829
# def fn(cur, end):
#     if cur == end:
#         return 1
#     if cur > end or cur == 18 or cur == 30:
#         return 0
#     if cur < end:
#         return(fn(cur+2, end) + fn(cur+3, end) + fn(cur*2, end))

# A = fn(5, 15) * fn(15, 55)
# B = fn(5, 20) * fn(20, 55)
# AB = fn(5, 15) * fn(15, 20) * fn(20, 55)
# print(A + B - AB)
# answer: 142 955


# №7213
def fn(cur, end, step, find_60):
    if cur == end:
        return find_60
    if cur > end or (cur % 10 == 3) or cur > end + 5:
        return 0
    k = 0
    if cur == 60:
        find_60 = 1
    k = fn(cur+7, end, 0, find_60) + fn(cur*2, end, 0, find_60)
    if step != 1:
        k += fn(cur-1, end, 1, find_60) + fn(cur-5, end, 1, find_60)
    return k
print(fn(9, 84, 0, 0))
# answer: 498 396