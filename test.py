# -*-coding:utf-8 -*-
def inttobinary(n):
    hexNum = 8*8
    bit = []
    for i in range(hexNum):
        b = n >> i
        c, d = divmod(b,2)
        bit.append(str(d))
    return "".join(bit[::-1])


if __name__ == "__main__":
    n = 80
    print("输出为："+ inttobinary(n))
