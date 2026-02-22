# №8750

# def to_3(n):
#     n3 = ""
#     while n > 0:
#         n3 += str(n % 3)
#         n //= 3
#     return(n3[::-1])

# all = []
# for n in range(1, 1000):
#     n3 = to_3(n)
#     if n % 3 != 0:
#         n3 = "1" + n3 + n3[-3:]
#     else:
#         res = 0
#         for i in range(len(n3)):
#             res += int(n3[i])
#         n3 += str(to_3(res*8))
#     n3 = int(n3, 3)
#     all.append(n3)
# all.sort()
# print(all)
# answer: 1205


# №8749

# def to_3(n):
#     n3 = ""
#     while n > 0:
#         n3 += str(n % 3)
#         n //= 3
#     return(n3[::-1])

# all = []
# for n in range(1, 1000):
#     n3 = to_3(n)
#     if n % 3 == 0:
#         n3 = n3 + n3[-2:] + "0"
#     else:
#         res = 0
#         for i in range(len(n3)):
#             res += int(n3[i])
#         n3 += str(to_3(res*4))
#     n3 = int(n3, 3)
#     all.append(n3)
# all.sort()
# print(all)
# answer: 448


# №8561

# def to_3(n):
#     n3 = ""
#     while n > 0:
#         n3 += str(n % 3)
#         n //= 3
#     return(n3[::-1])

# r = 0
# res = []
# for n in range(1, 1000):
#     n3 = to_3(n)
#     if n % 3 == 0:
#         n3 = "1" + n3 + "21"
#     else:
#         n3 += str(to_3(5*(n % 3)))
#     r = int(n3, 3)
#     if r <= 1130 and n % 2 != 0:
#         res.append(n)

# print(res)
# answer: 121


# №8559

# r = 0
# res = []
# for n in range(1, 1000):
#     n2 = str(bin(n))[2:]
#     if n % 7 == 0:
#         n2 += "01"
#     else:
#         n2 += str(bin(n // 7))[2:]
#     r = int(n2, 2)
#     if r <= 1300 and n % 2 != 0:
#         res.append(n)
# print(res)
# answer: 315


# №8557

# def to_3(n):
#     n3 = ""
#     while n > 0:
#         n3 += str(n % 3)
#         n //= 3 
#     return (n3[::-1])

# all_n = []
# for n in range(1, 1000):
#     n3 = to_3(n)
#     if n % 3 == 0:
#         n3 += n3[-2:]
#     else:
#         res = 0
#         for i in range(len(n3)):
#             res += int(n3[i])
#         n3 += to_3(res*3)
#     r = int(n3, 3)
#     if r % 2 != 0 and r > 208:
#         all_n.append(r)
# all_n.sort()
# print(all_n)
# answer: 243


# №8217

# all_n = {}
# for n in range(1, 1000):
#     n8 = str(oct(n)[2:])
#     if n8[0] == "5":
#         help_str = ""
#         for i in range(len(n8)):
#             if n8[i] == "2":
#                 help_str += "1"
#             elif n8[i] == "1":
#                 help_str += "2"
#             else:
#                 help_str += n8[i]
#         n8 = help_str
#         n8 = "11" + n8
#     else:
#         n8 += "10"
#         n8 = "2" + n8[1:-1] + "0"
#     r = int(n8, 8)
#     if r < 1354:
#         all_n[n] = r
# print(all_n)
# answer: 61

# №8216

# all_nr = {}
# def to_4(n):
#     n4 = ""
#     while n > 0:
#         n4 += str(n % 4)
#         n //= 4
#     return str(n4[::-1])

# for n in range(1, 1000):
#     n4 = to_4(n)
#     if n4[0] == "3":
#         help_str = ""
#         for i in n4:
#             if i == "1":
#                 help_str += "3"
#             elif i == "3":
#                 help_str += "1"
#             else:
#                 help_str += i
#         n4 = help_str + "21"
#     else:
#         n4 += "11"
#         n4 = "2" + n4[1:-1] + "1"
#     r = int(n4, 4)
#     if r < 598:
#         all_nr[n] = r
# print(all_nr)
# ancwer: 63