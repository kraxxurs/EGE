import ipaddress

# task 1
# ip_net = ipaddress.ip_network("172.95.116.174/255.255.192.0", 0)
# print(ip_net[1])
# print(172+95+64+1)


# task 2
# ip_net = ipaddress.ip_network("98.81.154.195/255.252.0.0", 0)
# print(ip_net[-2])


# task 3
# for mask in range(33):
#     ip_net1 = ipaddress.ip_network(f"113.188.14.51/{mask}", 0)
#     ip_net2 = ipaddress.ip_network(f"113.188.6.86/{mask}", 0)
#     if ip_net1 == ip_net2:
#         print(ip_net1)
# net1 = ipaddress.ip_network(f"113.188.14.51/20", 0)
# count = 0
# for ip in net1:
#     if f"{ip:b}".count("1") == 17:
#         count += 1
# print(count)


# task 4
for mask in range(33):
    ip_net = ipaddress.ip_network(f"132.118.34.161/{mask}", 0)
    count = 0
    for ip in ip_net:
        if f"{ip:b}".count("1") == 13:
            count += 1
    if count == 35:
        print(f"{mask:b}".count("0"))
print("end")