
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

    N, L = map(int, raw_input().split(' '))
    C = map(int, raw_input().split(' '))
    return [N, L, C]


def format_output(res):
    return str(res)


def proc_func(func_input):
    N, L, C = func_input
    rem = []
    for i in xrange(N):
        rem.append(int(round(100.*i/N) - 100*i//N))

    dist = [0]*N
    t = -1
    for i in xrange(N-1, -1, -1):
        if rem[i] == 1:
            t = 0
        elif t >= 0:
            t += 1
        dist[i] = t
    fill = []
    for c in C:
        fill.append([c, dist[c]])
    fill.sort(key=lambda x: x[1])
    z = dist[0]
    X = N - sum(C)
    for i in xrange(len(fill)):
        if fill[i][1] >= 0 and fill[i][1] <= X:
            fill[i][0] += fill[i][1]
            X -= fill[i][1]
    total = 0
    if X >= z:
        t = int(round(z*100. / N))
        total += t * (X // z)
        rest = X % z
    else:
        rest = X
    total += int(round(rest*100. / N))
    for i in xrange(len(fill)):
        total += int(round(fill[i][0]*100. / N))


    return str(total)


def test(func_input, expected, res):
    return

single_case = True

if single_case:
    # func_input = [9, 8, [1,1,1,1,1,1,1,1]]
    # func_input = [6, 2, [3,1]]
    func_input = [1000, 5, [36,36,36,36,36]]
    res = proc_func(func_input)
    print func_input, res
    test(func_input, '', res)
else:
    run_proc(proc_func, fetch_input, format_output)

