from math import*

# TASK 1

# for k in range(1, 1000):
#     N = 10 + 52 + 963
#     i = ceil(log2(N))
#     V1 = ceil((k * i) / 2**3)
#     V2000 = V1 * 2000
#     if V2000 <= 693 * (2**10):
#         print(k)
# answer: 257


# TASK_2

# V_whole = 31 * (2**20)
# for N in range(1, 1000):
#     k = 261
#     i = ceil(log2(N))
#     V1 = ceil((k * i) / (2**3))
#     V_all = V1 * 252_500
#     if V_all > V_whole:
#         print(N)
# answer: 9


# №8774

# for k in range(1, 1000):
#     N = 10 + 26 + 4065
#     i = ceil(log2(N))
#     V1 = ceil((k * i) / (2**3))
#     V_all = V1 * 153_897
#     if V_all > 12 * (2**20):
#         print(k)
#         break
# answer: 50


# №8727

# for N in range(1, 1000):
#     k = 251
#     i = ceil(log2(N))
#     V1 = ceil((k * i) / (2**3))
#     V_all = V1 * 65_536
#     if V_all >= 8_064 * (2**10):
#         print(N)
#         break
# answer: 9


# №8727

# k = 21
# N = 52 + 10 + 25
# i = ceil(log2(N))
# V1_pw = ceil((k * i) / (2**3))
# V1_extra = 18
# V1 = V1_extra + V1_pw
# V_all = 1 * 2**20
# max_users = V_all // V1
# print(max_users)
# answer: 28339


