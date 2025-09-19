# ЗАДАНИЕ №4
# F=(x∨y)∧¬(y≡z)∧¬w

# for x in [0, 1]:
#     for y in [0, 1]:
#         for z in [0, 1]:
#             for w in [0, 1]:
#                 if ((x or y) and ((not(y == z))) and (not w) ) == True:
#                     print (x, y, z, w)



# ЗАДАНИЕ №5
# F = ((w→z) ≡ (x→¬y)) ∧ (x∨z)

# from itertools import product, permutations

# def F (x, y, z, w):
#     return (((w <= z) == (x <= (not y))) and (x or z))

# for p in product([0, 1], repeat = 2):
#     table = [(1, 0, 0, 1),
#              (1, 1, 1, 0),
#              (0, p[0], 0, p[1])]
    
#     if(len(table) == len(set(table))):
#         for vars in permutations("xywz", 4):
#             if [F(**dict(zip(vars, row))) for row in table] == [1, 0, 1]:
#                 print(vars)



# ЗАДАНИЕ №6
# F1 = (w ≡ x) ∧ (y → z)
# F2 = (w → x) → (y ≡ z)

from itertools import product, permutations

def F1 (x, y, z, w):
    return (w == x) and (y <= z)

def F2 (x, y, z, w):
    return (w <= x) <= (y == z)

for p in product([0, 1], repeat = 4):
    table = [(1, p[0], 1, 1),
             (p[1], 1, 0, 0),
             (p[2], 0, 0, p[3])]
    
    if(len(table) == len(set(table))):
        for vars in permutations("xywz", 4):
            r1 = [F1(**dict(zip(vars, row))) for row in table]
            r2 = [F2(**dict(zip(vars, row))) for row in table]
            if (r1[0] == 1 and r1[1] == 1 and r1[2] == 0 and r2[0] == 0 and r2[2] == 0):
                print(vars)