#coding=utf8
"""_print(a, b, c)
_print_err(a, b, c)
"""

import sys
import os
import codecs
import datetime
import logging


def _str(val, encoding):
    "convert object to string."
    if isinstance(val, unicode):
        return val.encode(encoding)
    return str(val)

def _unicode(val, encoding):
    if isinstance(val, str):
        return val.decode(encoding)
    return unicode(val)


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
            
def logprint(logname, category, level=logging.DEBUG, max_bytes=1024*10124*100,
             backup_count=0, to_stdout=True, base_dir='.'):
    """category could be 'category', also 'category/subcategory. It's part of\
 path."""
    path = os.path.join(base_dir, category, logname+'.log')

    # Initialize logger
    logger = logging.getLogger(logname)
    frt = logging.Formatter('%(message)s')
    hdr = None
    if path:
        hdr = logging.handlers.RotatingFileHandler(path, 'a', max_bytes,
                                                   backup_count, 'utf-8')
        hdr.setFormatter(frt)
        logger.addHandler(hdr)
    if to_stdout:
        hdr = logging.StreamHandler(sys.stdout)
        hdr.setFormatter(frt)
        logger.addHandler(hdr)
    logger.setLevel(level)
    
    def _wraper(*args):
        if not args:
            return
        encoding = 'utf8' if os.name == 'posix' else 'gbk'
        args = [_unicode(a, encoding) for a in args]
        f_back = None
        try:
            raise Exception
        except:
            f_back = sys.exc_traceback.tb_frame.f_back
        f_name = f_back.f_code.co_name
        filename = os.path.basename(f_back.f_code.co_filename)
        m_name = os.path.splitext(filename)[0]
        prefix = (u'[%s.%s]' % (m_name, f_name)).ljust(20, ' ')
        logger.info(u' '.join([u'[%s]'%unicode(datetime.datetime.now()), prefix,
                               ' '.join(args)]))
    return _wraper, logger
            

class BCOLORS:
    "Terminal color control."
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

