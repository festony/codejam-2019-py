'''
CodeJam Python Lib for Festony, By Festony

Created on 2012-12-12

@author: festony
'''

import time
import inspect
import os.path as path
import os
import shutil
import math
import fractions

import properties
import zipfile

from properties import *

__all__ = [ \
    'run_proc', \
    'accumulate', \
    'get_full', \
    'get_perm', \
    'get_comb', \
    'gen_prime', \
    'get_prime_list', \
    'int2bin', \
    'bin2int', \
    'gcd', \
    'nCk', \
    'nCkMod', \
    'testOnLine', \
    'get_yh_triangle', \
    'calc_tri_point', \
    'calc_distance_2_p_2', \
    'calc_distance_p_2', \
    ]

print_details = True


def print_detailed_info(info):
    if print_details:
        print info


def check_input(working_folder, file_name, func):
    in_path = path.join(working_folder, file_name + '.in')
    out_path = path.join(working_folder, file_name + '.out')

    r = [in_path, out_path, working_folder]

    if file_name.find('test') >= 0:
        return r

    full_source_path = inspect.getsourcefile(func)
    source_file_name = os.path.split(full_source_path)[-1][:-3]
    first_separator_index = source_file_name.find('_')
    if first_separator_index < 0:
        return r

    in_year_str = source_file_name[:first_separator_index]
    in_year = -1
    try:
        in_year = int(in_year_str)
    except ValueError:
        return r
    if in_year < 2007 or in_year > 2020:
        return r

    source_file_name = source_file_name[first_separator_index + 1:]
    first_separator_index = source_file_name.find('_')
    if first_separator_index < 0:
        return r

    in_round = source_file_name[:first_separator_index]
    source_file_name = source_file_name[first_separator_index + 1:]
    question = source_file_name[0]

    if len(source_file_name) > 1 and source_file_name[1] != '_':
        return r
    if not question.isalpha() or question != question.upper():
        return r

    moved_in_folder = path.join(working_folder, in_year_str, in_round)

    # todo: refine this branch checking here.
    if not os.path.isdir(moved_in_folder):
        os.makedirs(moved_in_folder)
    new_in_path = path.join(moved_in_folder, file_name + '.in')
    new_out_path = path.join(moved_in_folder, file_name + '.out')
    new_r = [new_in_path, new_out_path, moved_in_folder]
    if os.path.isfile(new_in_path):
        return new_r
    if os.path.isfile(in_path):
        shutil.move(in_path, new_in_path)
        return new_r
    return r


def run_proc(func, input_dividing_func, working_folder=default_working_folder, file_name=default_file_name):
    '''Run the function multiple times for cases.
    
    Process time for each run / all runs are tracked.
    1) need to provide the function to process each case, the function
    should take a list as raw func_input;
    2) an input_dividing_func should be provided to break func_input lines into func_input lists
    for each case.
    '''
    # in_path = working_folder + file_name + '.in'
    # out_path = working_folder + file_name + '.out'
    in_path, out_path, working_folder = check_input(working_folder, file_name, func)
    inputfile = open(in_path, 'r')
    raw_input_str = inputfile.read()
    inputfile.close()
    input_lines = map(lambda x: x.rstrip('\r\n'), raw_input_str.split('\n'))
    inputs = input_dividing_func(input_lines)
    r = ''
    case_total_num = len(inputs)
    print_detailed_info('{0} cases in total.'.format(case_total_num))
    start_time_overall = time.clock()

    for i, func_input in enumerate(inputs):
        case_num = i + 1
        print_detailed_info('Case {0}:'.format(case_num))
        start_time_single_case = time.clock()
        r += 'Case #%d: %s\n' % (case_num, str(func(func_input)))
        print_detailed_info("Process time: %g sec(s)" % \
                            (time.clock() - start_time_single_case,))
        print_detailed_info("Overall process time till now: %g sec(s)" % \
                            (time.clock() - start_time_overall,))

    end_time_overall = time.clock()
    print(r)
    print("Overall process time: %g sec(s)" % \
          (end_time_overall - start_time_overall,))
    inputfile = open(out_path, 'w')
    inputfile.write(r)
    inputfile.close()

    if not ('practice' in file_name or 'test' in file_name):
        cjlibfile = inspect.getsourcefile(run_proc)
        propfile = inspect.getsourcefile(properties)
        funcfile = inspect.getsourcefile(func)
        codezip = zipfile.ZipFile(working_folder + file_name + '-code.zip', 'w')
        codezip.write(cjlibfile, os.path.split(cjlibfile)[1])
        codezip.write(propfile, os.path.split(propfile)[1])
        codezip.write(funcfile, os.path.split(funcfile)[1])
        codezip.close()

    return r


# commonly used functions

def accumulate(l):
    r = l[:]
    for i in range(1, len(r)):
        r[i] += r[i - 1]
    return r


def get_full(k):
    r = []
    k1 = 0
    for i in range(k):
        if r == []:
            for j in range(k):
                r.append([j])
        else:
            l = len(r)
            for j in range(l):
                temp = r.pop(0)
                for j1 in range(k):
                    temp2 = temp + [j1]
                    r.append(temp2)
    return r


def get_perm(k, n):
    if k == 0:
        return []
    r = []
    if k == 1:
        for i in range(n):
            r.append([i])
        return r
    r1 = get_perm(k - 1, n)
    r = []
    for p in r1:
        for j in range(max(p) + 1, n):
            for i in range(k):
                temp = p[:]
                temp.insert(i, j)
                r.append(temp)
    return r


def get_comb(k, n):
    '''
    get k items out of total n
    '''
    if k == 0:
        return []
    r = []
    if k == 1:
        for i in range(n):
            r.append([i])
        return r
    r1 = get_comb(k - 1, n)
    for sr in r1:
        for i in range(sr[-1] + 1, n):
            if i not in sr:
                temp = sr[:]
                temp.append(i)
                r.append(temp)
    return r


def is_dividable(n, prime_list):
    for p in prime_list:
        if n % p == 0:
            return True
    return False


def gen_prime(n):
    r = [2]
    i = 3
    while i <= n:
        if not is_dividable(i, r):
            r.append(i)
        i += 2
    return r


def get_prime_list():
    f = open('../resources/prime_list.txt', 'r')
    prime_list = eval(f.read())
    f.close()
    return prime_list


def int2bin(n, N=None):
    bn = bin(n)[2:]
    if N == None or N <= len(bn):
        return map(int, list(bn))
    else:
        return map(int, list(bn.zfill(N)))


def bin2int(bn):
    return int(''.join(map(str, list(bn))), 2)


def gcd(N):
    if N == []:
        return 0
    n = N[:]
    while len(n) > 1:
        p = n[-2:]
        n = n[:-2]
        n.append(fractions.gcd(p[0], p[1]))
    return n[0]


def nCk(n, k):
    return int(reduce(lambda x, y: x * y, (fractions.Fraction(n - i, i + 1) for i in range(k)), 1))


def nCkMod(n, k, m):
    return (int(reduce(lambda x, y: (x * y) % m, (fractions.Fraction(n - i, i + 1) for i in range(k)), 1))) % m


def testOnLine(A, B, P, threshold=None):
    r = ((B[0] - A[0]) * (P[1] - A[1]) - (B[1] - A[1]) * (P[0] - A[0]))
    if threshold == None:
        threshold = 0
    if r > threshold:
        return 1
    elif r < threshold * -1:
        return -1
    return 0


def get_yh_triangle(maxn):
    fname = '../resources/yanghui_triangle_{}.txt'.format(maxn)
    f = open(fname, 'r')
    yh_tri = eval(f.read())
    f.close()
    return yh_tri


# know position of triangle's 2 points, and the distances from these 2 points to the 3rd point
# calc the position of this 3rd point
def calc_tri_point(p1, p2, r1, r2, sigma=0.00000000001):
    x1 = p1[0]
    y1 = p1[1]
    x2 = p2[0] - x1
    y2 = p2[1] - y1

    if x2 != 0:
        a = 1 + float(y2 * y2) / (x2 * x2)
        b = y2 * (r2 * r2 - r1 * r1 - x2 * x2 - y2 * y2) / float(x2 * x2)
        c = (r1 * r1 - r2 * r2 + x2 * x2 + y2 * y2) * (r1 * r1 - r2 * r2 + x2 * x2 + y2 * y2) / float(
            4 * x2 * x2) - r1 * r1

        delta = b * b - 4 * a * c
        if delta < sigma * -1:
            return []
        if delta >= sigma * -1 and delta <= sigma:
            y3 = -1 * b / (2 * a)
            x3 = (2 * y2 * y3 + r2 * r2 - r1 * r1 - x2 * x2 - y2 * y2) / float(-2 * x2)
            return [[x3 + x1, y3 + y1]]
        y3 = (-1 * b + math.sqrt(delta)) / (2 * a)
        x3 = (2 * y2 * y3 + r2 * r2 - r1 * r1 - x2 * x2 - y2 * y2) / float(-2 * x2)
        p3_1 = [x1 + x3, y1 + y3]
        y3 = (-1 * b - math.sqrt(delta)) / (2 * a)
        x3 = (2 * y2 * y3 + r2 * r2 - r1 * r1 - x2 * x2 - y2 * y2) / float(-2 * x2)
        p3_2 = [x1 + x3, y1 + y3]
        return [p3_1, p3_2]
    else:
        y3 = (r1 * r1 - r2 * r2 + y2 * y2) / float(2 * y2)
        delta = -1 * (y3 * y3 - r1 * r1)
        if delta < sigma * -1:
            return []
        if delta >= sigma * -1 and delta <= sigma:
            return [[x1, y3 + y1]]
        x3 = math.sqrt(delta)
        return [[x1 + x3, y1 + y3], [x1 - x3, y1 + y3]]


def calc_tri_signed_area_2(p0, p1, p2):
    return p0[0] * p1[1] + p1[0] * p2[1] + p2[0] * p0[1] - p0[0] * p2[1] - p2[0] * p1[1] - p1[0] * p0[1]


def calc_distance_2_p_2(p0, p1):
    return (p0[0] - p1[0]) * (p0[0] - p1[0]) + (p0[1] - p1[1]) * (p0[1] - p1[1])


def calc_distance_p_2(p0, p1):
    return math.sqrt(calc_distance_2_p_2(p0, p1))


# todo:
# calc point inside triangle
# calc distance of 2 points
# calc if a point is on left side of a line formed by 2 points, or right
# get all cuts of separating a group of points into 2 groups by a line



# Test
if __name__ == '__main__':
    def test_process_func(func_input):
        print 'func_input:', func_input
        return 0


    # Set test case input file
    f = open(default_working_folder + default_file_name + '.in', 'r')
    old_content = f.read()
    f.close()
    f = open(default_working_folder + default_file_name + '.in', 'w')
    f.write('''4
5
Yeehaw
NSM
Dont Ask
B9
Googol
10
Yeehaw
Yeehaw
Googol
B9
Googol
NSM
B9
NSM
Dont Ask
Googol
5
Yeehaw
NSM
Dont Ask
B9
Googol
7
Googol
Dont Ask
NSM
NSM
Yeehaw
Yeehaw
Googol
4
Zol
Zolz
Zollz
Zolzz
0
0
3
'AZ'
'BZ'
'CZ'
''')
    f.close()


    def test_input_dividing_func(input_lines):
        total_case = int(input_lines.pop(0))
        case_inputs = []
        for i in range(total_case):
            engine_num = int(input_lines.pop(0))
            engines = input_lines[:engine_num]
            del input_lines[:engine_num]
            query_num = int(input_lines.pop(0))
            queries = input_lines[:query_num]
            del input_lines[:query_num]
            case_inputs.append([engines, queries])
        return case_inputs


    run_proc(test_process_func, test_input_dividing_func)

    # restore file used in test case back to its original content.
    f = open(default_working_folder + default_file_name + '.in', 'w')
    f.write(old_content)
    f.close()
