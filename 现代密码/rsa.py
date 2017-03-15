#!/usr/bin/env python
#-*-coding:utf-8-*-


def fastExpMod(b, e, m):
    """
    e = e0*(2^0) + e1*(2^1) + e2*(2^2) + ... + en * (2^n)

    b^e = b^(e0*(2^0) + e1*(2^1) + e2*(2^2) + ... + en * (2^n))
        = b^(e0*(2^0)) * b^(e1*(2^1)) * b^(e2*(2^2)) * ... * b^(en*(2^n))

    b^e mod m = ((b^(e0*(2^0)) mod m) * (b^(e1*(2^1)) mod m) * (b^(e2*(2^2)) mod m) * ... * (b^(en*(2^n)) mod m) mod m
    """
    result = 1
    while e != 0:
        if (e & 1) == 1:
            # ei = 1, then mul
            result = (result * b) % m
        e >>= 1
        # b, b^2, b^4, b^8, ... , b^(2^n)
        b = (b * b) % m
    return result


def computeD(fn, e):
    (x, y, r) = extendedGCD(fn, e)
    # y maybe < 0, so convert it
    if y < 0:
        return fn + y
    return y


def extendedGCD(a, b):
    # a*xi + b*yi = ri
    if b == 0:
        return (1, 0, a)
    # a*x1 + b*y1 = a
    x1 = 1
    y1 = 0
    # a*x2 + b*y2 = b
    x2 = 0
    y2 = 1
    while b != 0:
        q = a / b
        #ri = r(i-2) % r(i-1)
        r = a % b
        a = b
        b = r
        #xi = x(i-2) - q*x(i-1)
        x = x1 - q * x2
        x1 = x2
        x2 = x
        #yi = y(i-2) - q*y(i-1)
        y = y1 - q * y2
        y1 = y2
        y2 = y
    return(x1, y1, a)


def decryption(C, d, n):
    # RSA M = C^d mod n
    return fastExpMod(C, d, n)


p = int(raw_input('请输入p：'))
q = int(raw_input('请输入q：'))
n = p * q
fn = (p - 1) * (q - 1)
e = int(raw_input('请输入e：'))
d = computeD(fn, e)
C = int(raw_input('输入16进制密文：'), 16)
M = decryption(C, d, n)
flag = str(hex(M))[2:-1]
print 'd=', d
print flag
