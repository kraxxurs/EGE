# TASK 1: Определите, что вернет данная функция, если в нее передать n = 5?

# def F(n):
#     if n == 1:
#         return 3
#     if n > 1:
#         return (7 * F(n - 1) - n + 4)
# print(F(5))
# answer: 7937


# TASK 2: Определите, что вернет данная функция, если в нее передать n = 10?

# def F(n):
#     if n == 0:
#         return 0
#     if n >= 1:
#         return (F(n - 1) + n)
# print(F(10))
# answer: 55


# TASK 3: Определите, что вернет данная функция, если в нее передать n = 15?

# def F(n):
#     if n == 1:
#         return 2
#     if n >= 2:
#         if n % 2 == 0:
#             return (F(n - 1))
#         else:
#             return (3 * F(n - 2) - 2 * n + 5) 
# print(F(15))
# answer: 1_109


# TASK 4: Найдите кол-во n из диапазона [1; 220], при которых F(n) кратно 3?

# def F(n):
#     if n <= 3:
#         return n
#     if n > 3:
#         if n % 2 == 0:
#             return (n + 5 * F(n - 4))
#         else:
#             return (2 * n + F(n - 4)) 
# cnt = 0
# for n in range(1, 221):
#     if F(n) % 3 == 0:
#         cnt += 1
# print(cnt)
# answer: 73


# TASK 5: Запишите целую часть значения F(20) / G(15)?

# def F(n):
#     if n == 1:
#         return 1 
#     if n >= 2:
#         return (F(n - 1) + G(n - 1) + n * 2)
# def G(n):
#     if n == 1:
#         return 1
#     if n >= 2:
#         return (F(n - 1) + G(n - 1) * 4)
# print (F(20) // G(15))
# answer: 446


# TASK 6: Чему равно выражение?

# import sys      # 1-ЫЙ СПОСОБ
# sys.setrecursionlimit(3000)
# def F(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return (n * F(n - 1))
# print((3 * F(2025) + F(2024)) // F(2023))

# F = [0] * 3000      # 2-ОЙ СПОСОБ
# for n in range(1, 3000):
#     if n == 1:
#         F[n] = 1
#     if n > 1:
#         F[n] = n * F[n - 1] 
# print((3 * F[2025] + F[2024]) // F[2023])

# answer: 12_297_824


# TASK 7: Чему равно выражение?

# F = [0] * 3000
# for n in range(1, 3000):
#     if n == 1:
#         F[n] = 1
#     if n > 1:
#         F[n] = n * F[n - 1]
# print(F[2025] // F[2023])
# answer: 4_098_600


# TASK 8: Чему равно выражение?
# def F(n):
#     if n > 2025:
#         return n
#     if n <= 2025:
#         return ((n + 1) * F(n + 1))
# print(F(2015) // F(2020))

F = [0] * 3000
for n in range(3000 -1, 1, -1):
    if n > 2025:
        F[n] = n
    if n <= 2025:
        F[n] = ((n + 1) * F[n + 1])
print(F[2015] // F[2020])

answer: 33_466_113_241_908_480