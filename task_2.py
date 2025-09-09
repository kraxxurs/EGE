# ПРИМЕР №1
# w ∧ ¬((x -> y) -> (y ≡ z))

# for x in [0, 1]:
#     for y in [0, 1]:
#         for z in [0, 1]:
#             for w in [0, 1]:
#                 if (w and not((x <= y) <= (y == z))) == True:
#                     print(x, y, z, w)


# ПРИМЕР №2
# ¬(x → y) ∨ (z ≡ w) ∨ z

# for x in [0, 1]:
#     for y in [0, 1]:
#         for z in [0, 1]:
#             for w in [0, 1]:
#                 if (not(x <= y) or (z == w) or z) == False:
#                     print (x, y, z, w)


# ПРИМЕР №3 (7912)
# ¬((¬x ˅ y) ∧ ¬w) ˅ ¬(z ∧ ¬(y ∧ w))

# from itertools import product, permutations
# print (list(product("ABC", repeat = 2))) - с повторами
# print(list(permutations("ABC", 2))) - без повторов

# def F (x, y, z, w):
#     return not ((not x or y) and not w) or not (z and not (y and w))

# for p in product([0, 1], repeat = 7):
#     table = [(0, p[0], p[1], 1),
#              (p[2], 1, p[3], p[4]),
#              (1, 0, p[5], p[6])]
    
#     if(len(table) == len(set(table))):
#         for vars in permutations("xywz", 4):
#             if [F(**dict(zip(vars, row))) for row in table] == [0, 0, 0]:
#                 print(vars)


# ПРИМЕР №4 (6616)
# F1 = (x → y) ∨ (¬w  ≡ z), F2 = (x → y) ≡ (w ∧ ¬z)

from itertools import product, permutations

def F1 (x, y, z, w):
    return (x <= y) or ((not w)  == z)

def F2 (x, y, z, w):
    return (x <= y) == (w and not z)

for p in product([0, 1], repeat = 7):
    table = [(p[0], p[1], p[2], 0),
             (p[3], p[4], 0, 0),
             (p[5], 0, 0, 0)]
    
    if(len(table) == len(set(table))):
        for vars in permutations("zwyx", 4):
            r1 = [F1(**dict(zip(vars, row))) for row in table]
            r2 = [F2(**dict(zip(vars, row))) for row in table]
            if (r1[0] == r2[0] and r1[1] == r2[1] and r1[2] == r2[2]):
                print(vars)