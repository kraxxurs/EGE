# TASK 1: Для какого наиб. натурал. числа А выражение тождетвенно истинно при любых х

# def Del(n, m):
#     return (n % m == 0)

# for A in range(1, 10_000):
#     A_podoshel = True
#     for x in range(1, 10_000):
#         if ((not Del(x, A)) <= (not Del(x, 18)) or (not Del(x, 42))) == 0:
#             A_podoshel = False
#             break
#     if A_podoshel == True:
#         print(A)
# answer: 126


# TASK 2: Для какого наим. натурал. числа А выражение тождетвенно истинно при любых х

# for A in range(1, 1_000):
#     for x in range(1, 1_000):
#         if not ((x & 34 != 0) <= ((x & 41 == 0) <= (x & A != 0))):
#             break
#     else:
#         print(A)
# answer: 2


# TASK 3: Для какого наим. натурал. числа А выражение тождетвенно истинно при любых полож. х и у

# for A in range(1, 1000):      # 1-ЫЙ СПОСОБ
#     A_podoshel = True
#     for x in range(1, 1000):
#         for y in range(1, 1000):
#             if not (((y + 5*x != 31) or (A > x - 2)) and (A < y + 37)):
#                 A_podoshel = False
#                 break
#         if A_podoshel == False:
#             break
#     if A_podoshel:
#         print(A)

# for A in range(1, 1000):      # 2-ОЙ СПОСОБ
#     for x in range(1, 1000):
#         for y in range(1, 1000):
#             if not (((y + 5*x != 31) or (A > x - 2)) and (A < y + 37)):
#                 break
#         if not (((y + 5*x != 31) or (A > x - 2)) and (A < y + 37)):
#             break
#     else:
#         print(A)
#         break

# for A in range(1, 1000):      # 3-ИЙ СПОСОБ
#     if all((((y + 5*x != 31) or (A > x - 2)) and (A < y + 37)) 
#            for x in range(1, 1000) for y in range (1, 1000)):
#         print(A)
#         break

# answer: 5


# TASK 4: Какую наим. длину может принимать отрезок А, чтобы формула была тождествена при любых х?

# R = list(range(12, 31+1))
# Q = list(range(6, 15+1))
# P = list(range(17, 23+1))
# A = []
# for x in range(1, 100):
#     if not (((x in A) or (x in P)) or ((x in Q) <= (x in R))):
#         A.append(x)
# print(A, 11+1-6)
# answer: 6


# TASK 5: Какую наим. длину может принимать отрезок А, чтобы формула была тождествена при любых х?

# Q = list(range(8, 17+1))
# P = list(range(3, 11+1))
# A = list(range(1, 100))
# for x in range(1, 100):
#     if not (((x in A) <= (x in P)) or (x in Q)):
#         A.remove(x)
# print(A, 17-13)
# answer: 14


# TASK 6: Для какого наиб. натурал. числа А выражение тождетвенно истинно при любых х

def Del(n, m):
    return (n % m == 0)

for A in range(1, 1000):
    for x in range(1, 1000):
        if not (((x + 40 < A) or (x + A < 40)) <= (Del(x, A))):
            break
    else:
        print(A)