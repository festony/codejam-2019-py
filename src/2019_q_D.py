
import sys
import time
import inspect
import os.path as path
import os
import shutil
import math
import fractions
import zipfile


# map(int, raw_input().split(' '))

def run_proc(proc_func):
    T = int(raw_input())
    for i in range(T):
        proc_func()


in_template0 = ''.join(['00000000000000001111111111111111']*32)
in_template1 = ''.join(['0000000011111111']*64)
in_template2 = ''.join(['00001111']*128)
in_template3 = ''.join(['0011']*256)
in_template4 = ''.join(['01']*512)


def get_01_count(o):
    c0 = 0
    c1 = 0
    for c in o:
        if c == '0':
            c0 += 1
        else:
            c1 += 1
    return c0, c1


cache = {}


def find_b(expected, good_bits, sout):
    k = (expected, good_bits, sout)
    if k in cache:
        return cache[k]
    T = good_bits
    r = []
    if T == expected:
        cache[k] = []
        return cache[k]
    if expected == 1:
        cache[k] = [0]
        return cache[k]
    first_half, second_half = get_01_count(sout[0])
    if first_half < expected / 2:
        f_sout = []
        for i in range(1, len(sout)):
            f_sout.append(sout[i][:first_half])
        r += find_b(expected / 2, first_half, tuple(f_sout))
    if second_half < expected / 2:
        s_sout = []
        for i in range(1, len(sout)):
            s_sout.append(sout[i][first_half:])
        s_r = find_b(expected / 2, second_half, tuple(s_sout))
        for b in s_r:
            r.append(expected / 2 + b)
    cache[k] = r
    return cache[k]


def proc_func():
    # interactive
    N, B, F = map(int, raw_input().split(' '))
    in0 = in_template0[:N]
    print in0
    sys.stdout.flush()
    out0 = raw_input()

    if N <= 8:
        out1 = out0[:]
    else:
        in1 = in_template1[:N]
        print in1
        sys.stdout.flush()
        out1 = raw_input()

    if N <= 4:
        out2 = out1
    else:
        in2 = in_template2[:N]
        print in2
        sys.stdout.flush()
        out2 = raw_input()

    if N <= 2:
        out3 = out2
    else:
        in3 = in_template3[:N]
        print in3
        sys.stdout.flush()
        out3 = raw_input()

    in4 = in_template4[:N]
    print in4
    sys.stdout.flush()
    out4 = raw_input()

    if N % 16 != 0:
        newN = int(math.ceil(N / 16.)) * 16
        out0 += in_template0[N:newN]
        out1 += in_template1[N:newN]
        out2 += in_template2[N:newN]
        out3 += in_template3[N:newN]
        out4 += in_template4[N:newN]
        N = newN

    return_16blocks = []
    curr = '0'
    for i, c in enumerate(out0):
        if c != curr:
            return_16blocks.append(i)
            curr = c
    return_16blocks.append(len(out0))

    # print return_16blocks
    offsets = []
    x = 0
    for y in return_16blocks:
        offsets.append(x)
        x += 16
    # print offsets

    B = []
    starti = 0
    for i, endi in enumerate(return_16blocks):
        sub_out1 = out1[starti:endi]
        sub_out2 = out2[starti:endi]
        sub_out3 = out3[starti:endi]
        sub_out4 = out4[starti:endi]

        bs = find_b(16, endi - starti, (sub_out1, sub_out2, sub_out3, sub_out4))
        for b in bs:
            B.append(offsets[i] + b)

        starti = endi

    print ' '.join(map(str, B))
    sys.stdout.flush()
    raw_input()
    return

run_proc(proc_func)
# print ''
# sys.stdout.flush()
# print ''
# sys.stdout.flush()
exit(0)


# print find_b(8, 5, ['00111', '01001', '11010'])
