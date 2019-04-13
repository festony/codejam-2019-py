
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
    return [int(line)]


def format_output(res):
    return str(res)


def proc_func(func_input):
    N = func_input[0]
    strN = str(N)
    strA = []
    strB = []
    for d in strN:
        if d == '4':
            strA.append('3')
            strB.append('1')
        else:
            strA.append(d)
            if strB:
                strB.append('0')

    if not strB:
        strB.append('0')
    return ''.join(strA) + ' ' + ''.join(strB)


def test(func_input, expected, res):
    return

single_case = False

if single_case:
    func_input = ['4']
    res = proc_func(func_input)
    print func_input, res
    test(func_input, '', res)
else:
    run_proc(proc_func, fetch_input, format_output)

