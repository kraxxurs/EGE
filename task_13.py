import ipaddress

# №8308

# ip_net = ipaddress.ip_network("192.168.12.207/255.192.0.0", 0)
# result = ""

# for ip in list(ip_net):
#     ip1 = f"{ip:b}"
#     #ip2 = bin(int(ip))[2:]
#     if str(ip1).count("0") == str(ip1).count("1"):
#         result = ip

# print(result)



# №7850

# for mask in range(33):
#     net1 = ipaddress.ip_network(f"126.115.78.15/{mask}", 0)
#     net2 = ipaddress.ip_network(f"126.115.84.26/{mask}", 0)

#     if net1 == net2:
#         print(net1)

# net1 = ipaddress.ip_network(f"126.115.78.15/19", 0)
# count = 0
# for ip in list(net1):
#     if f"{ip:b}".count("1") == 22:
#         count += 1

# print(count)


# №7048

# for A in range(255, -1, -1):
#     net = ipaddress.ip_network(f"159.242.{A}.223/255.255.254.0", 0)
#     for ip in list(net):
#         ip_b = f"{ip:b}"
#         left = ip_b[:16].count("0")
#         right = ip_b[16:].count("0")
#         if left >= right:
#             break
#     else:
#         print(A)
#         break