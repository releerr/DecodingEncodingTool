from Crypto.Util.number import *
import random
import hashlib
import os

# yes = 2669175714787937 << 12
# c = [140, 96, 112, 178, 38, 180, 158, 240, 179, 202, 251, 138, 188, 185, 23, 67, 163, 22, 150, 18, 143, 212, 93, 87,
#      209, 139, 92, 252, 55, 137, 6, 231, 105, 12, 65, 59, 223, 25, 179, 101, 19, 215]
#
#
# def rand(rng):
#     return rng - random.randrange(rng)
#
#
# for i in range(1<<12):
#     key = long_to_bytes(yes + i)
#     flag = []
#     random.seed(int(hashlib.md5(key).hexdigest(), 16))
#     for j in range(len(c)):
#         rand(256)
#         xor = c[j] ^ rand(256)
#         flag.append(xor)
#     if all(ch < 256 for ch in flag):
#         flag = bytes(flag)
#         # print(flag)
#         if (flag.startswith(b'flag')):
#             print(bytes_to_long(key))
#             print(flag)


for i in range(1<<5):
    print(i)