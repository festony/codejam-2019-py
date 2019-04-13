
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

def run_proc(proc_func, fetch_input, format_output):
    T = int(raw_input())
    all_r = ''
    for i in range(T):
        func_input = fetch_input()
        res = proc_func(func_input)
        r = format_output(res)
        all_r += 'Case #{}: {}\n'.format(i + 1, r)
    print all_r
    sys.stdout.flush()


def fetch_input():
    line = raw_input()
    N, L = map(int, line.split(' '))
    line = raw_input()
    C = map(int, line.split(' '))
    return [N, L, C]


def format_output(res):
    return str(res)


def proc_func(func_input):
    N, L, C = func_input

    i = 0
    while C[i] == C[i+1]:
        i += 1

    p1 = fractions.gcd(C[i], C[i+1])
    p0 = C[i] / p1
    p = [p0, p1]
    j = i-1
    while j >= 0:
        p.insert(0, C[j] / p[0])
        j -= 1
    j = i+1
    while j < len(C):
        p.append(C[j] / p[-1])
        j += 1

    sp = set(p)
    slp = sorted(list(sp))
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ'
    dec_m = dict()
    for i in range(len(slp)):
        dec_m[slp[i]] = alpha[i]
    r = ''
    for n in p:
        r += dec_m[n]
    return r


def test(func_input, expected, res):
    return

single_case = False

if single_case:
    func_input = [3571082522473766674484304975778527401895200115726120795842576355509746402614775567, 109365877189563187326603635520127561735031361824126205462909387312835060326083471734588324314134746753917003016771380861541]
    res = proc_func(func_input)
    print func_input, res
    test(func_input, '', res)
else:
    run_proc(proc_func, fetch_input, format_output)

