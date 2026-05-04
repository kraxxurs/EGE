from itertools import product, permutations

# №8142 

# count = 0
# for number in permutations("0123456789", 4):
#     if number[0] != "0":
#         for i in range(3):
#             if int(number[i])%2 == 0 and int(number[i+1])%2 == 0:
#                 break
#             if int(number[i])%2 != 0 and int(number[i+1])%2 != 0:
#                 break
#         else: # если цикл завершился логически, и не было прерываний
#             count += 1
# print(count)


# №8141

# count = 0
# for i, number in enumerate(product("АБДЕОП", repeat=6), start=1):
#     if number[0] == "О" and len(set(number)) == 6:
#         if i % 2 == 0:
#             count = i

# print(count)


from itertools import permutations, product
count = []
res = []
chet = "02468"
nechet = "1357"
for i, number in enumerate(product("012345678", repeat = 6), start = 1):
    if number[0] != "0" and number[0] not in nechet:
        if number[5] == "2" or number[5] == "3":
            continue
        if number.count("1") < 2:
            continue
        else: 
            count.append(i)
            res.append(number)
print(res)
#print(count)
print(len(count))
