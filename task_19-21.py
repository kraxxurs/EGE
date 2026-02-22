# TASK 1

# def g(s, step, end):
#     if s >= 129:
#         return step in end
#     if step >= max(end):
#         return False
#     moves = [g(s + 1, step + 1, end), g(s * 2, step + 1, end)]
#     if ((step + 1) % 2) == (end[0] % 2):
#         return any(moves)
#     else:
#         return all(moves)

# print("19 answer:", [s for s in range(1, 129) if g(s, 0, [2])])
# print("20 answer:", [s for s in range(1, 129) if g(s, 0, [3])])
# print("21 answer:", min([s for s in range(1, 129) if g(s, 0, [2, 4]) and not g(s, 0, [2])]))


# TASK 2

# def g(s, step, end):
#     if s <= 30:
#         return step in end
#     if step >= max(end):
#         return False
#     moves = [g(s - 3, step + 1, end), g(s - 5, step + 1, end), g(s // 4, step + 1, end)]
#     if ((step + 1) % 2) == (end[0] % 2):
#         return any(moves)
#     else:
#         return all(moves)

# print("19 answer:", [s for s in range(31, 1000) if g(s, 0, [2])])
# print("20 answer:", [s for s in range(31, 1000) if g(s, 0, [3])])
# print("21 answer:", min([s for s in range(31, 1000) if g(s, 0, [2, 4]) and not g(s, 0, [2])]))