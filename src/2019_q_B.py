
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
    line = raw_input()
    return line


def format_output(res):
    return str(res)


def proc_func(func_input):
    L = func_input
    r = ''
    m = {'E': 'S', 'S': 'E'}
    for c in L:
        r += m[c]

    return r


def test(func_input, expected, res):
    return

single_case = False

if single_case:
    func_input = 'ESSESSE'
    res = proc_func(func_input)
    print func_input, res
    test(func_input, '', res)
else:
    run_proc(proc_func, fetch_input, format_output)

