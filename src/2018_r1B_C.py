
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
    M = int(raw_input())
    R = []
    for i in xrange(M):
        R.append(map(lambda x:x-1, map(int, raw_input().split(' '))))
    G = map(int, raw_input().split(' '))
    return [M, R, G]


def format_output(res):
    return str(res)


def proc_func(func_input):
    M, R, G = func_input

    RM = {}
    for i, r in enumerate(R):
        if r[0] != 0 and r[1] != 0 and r[0] != i and r[1] != i:
            RM[i] = r
    if 0 not in RM:
        return str(G[0])
    print RM

    def try_1g_lead():
        G[RM[0][0]] -= 1
        G[RM[0][1]] -= 1
        while True:
            if min(G) < -M:
                return False
            lack = -1
            for i, g in enumerate(G):
                if g < 0:
                    lack = i
                    break
            if lack == -1:
                return True
            if lack not in RM:
                return False
            G[RM[lack][0]] -= 1
            G[RM[lack][1]] -= 1
            G[lack] += 1

    while try_1g_lead():
        G[0] += 1
    return G[0]



    return ''


def test(func_input, expected, res):
    return

single_case = True

if single_case:
    # func_input = [3, [[1,2], [0,2], [0,1]], [5,2,3]]
    # func_input =
    func_input = [4, [[2,3], [1,2], [1,2], [1,2]], [0,1,1,0]]
    res = proc_func(func_input)
    print func_input, res
    test(func_input, '', res)
else:
    run_proc(proc_func, fetch_input, format_output)

