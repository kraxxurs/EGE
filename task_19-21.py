# № 8080

# def fn(s, m):
#     if s <= 87:
#         return m % 2 == 0
#     if m == 0:
#         return False
#     h = [fn(s-2, m - 1), fn(s // 2, m - 1)]
#     return any(h) if m % 2 != 0 else all(h)

# print("19)", [s for s in range(88, 200) if fn(s, 2)])
# print("20)", [s for s in range(88, 200) if not fn(s, 1) and fn(s, 3)])
# print("21)", [s for s in range(88, 200) if not fn(s, 2) and fn(s, 4)])


# № 8666

def fn(s, m):
    if s >= 125:
        return m % 2 == 0
    if m == 0:
        return False
    h = [fn(s + 2, m - 1), fn(s + 4, m - 1), fn(s * 2, m - 1)]
    return any(h) if m % 2 != 0 else all(h)

print("19)", [s for s in range(1, 125) if fn(s, 2)])
print("20)", [s for s in range(1, 125) if not fn(s, 1) and fn(s, 3)])
print("21)", [s for s in range(1, 125) if not fn(s, 2) and fn(s, 4)])