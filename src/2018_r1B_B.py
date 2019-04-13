
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
    S = int(raw_input())
    M = []
    N = []
    for i in xrange(S):
        D, A, B = map(int, raw_input().split(' '))
        M.append(D+A)
        N.append(D-B)

    return [S, M, N]


def format_output(res):
    return str(res)


def proc_func(func_input):
    S, M, N = func_input
    # brute force
    if S == 1:
        return '1 1'
    possibleMN = set([])
    for i in xrange(1, S):
        possibleMN.add(tuple([M[i-1], N[i]]))
        possibleMN.add(tuple([M[i], N[i-1]]))
    validSets = set([])
    for mn in possibleMN:
        m, n = mn
        isValid = False
        start = 0
        for i in range(S):
            if M[i] == m or N[i] == n:
                if not isValid:
                    isValid = True
                    start = i
            else:
                if isValid:
                    isValid = False
                    validSets.add((start, i))
        if isValid:
            validSets.add((start, S))
    lens = {}
    for s in validSets:
        l = s[1] - s[0]
        if l not in lens:
            lens[l] = 1
        else:
            lens[l] += 1

    maxl = max(lens.keys())
    maxlv = lens[maxl]

    return '{} {}'.format(maxl, maxlv)


def test(func_input, expected, res):
    return

single_case = False

if single_case:
    func_input = [5, [9,9,18,22,22], [-10, -5, -7, -1, -1]]
    res = proc_func(func_input)
    print func_input, res
    test(func_input, '', res)
else:
    run_proc(proc_func, fetch_input, format_output)

