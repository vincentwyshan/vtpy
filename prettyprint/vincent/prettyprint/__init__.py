#coding=utf8
"""_print(a, b, c)
_print_err(a, b, c)
"""

import sys
import os
import datetime


def _str(val, encoding):
    "convert object to string."
    if isinstance(val, unicode):
        return val.encode(encoding)
    return str(val)

def _print(*args):
    "print regular..."
    if not args:
        return
    encoding = 'utf8' if os.name == 'posix' else 'gbk'
    args = [_str(a, encoding) for a in args]
    f_back = None
    try:
        raise Exception
    except:
        f_back = sys.exc_traceback.tb_frame.f_back
    f_name = f_back.f_code.co_name
    filename = os.path.basename(f_back.f_code.co_filename)
    m_name = os.path.splitext(filename)[0]
    prefix = ('[%s.%s]'%(m_name, f_name)).ljust(20, ' ')
    print '[%s]' % str(datetime.datetime.now()), prefix, ' '.join(args)

def _print_err(*args):
    "print error..."
    if not args:
        return
    encoding = 'utf8' if os.name == 'posix' else 'gbk'
    args = [_str(a, encoding) for a in args]
    f_back = None
    try:
        raise Exception
    except:
        f_back = sys.exc_traceback.tb_frame.f_back
    f_name = f_back.f_code.co_name
    filename = os.path.basename(f_back.f_code.co_filename)
    m_name = os.path.splitext(filename)[0]
    prefix = ('[%s.%s]' % (m_name, f_name)).ljust(20, ' ')
    print BCOLORS.FAIL + '[%s]' % str(datetime.datetime.now()), prefix, \
            ' '.join(args) + BCOLORS.ENDC

class BCOLORS:
    "Terminal color control."
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

