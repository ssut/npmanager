"""
command utils for npmanager
"""
import os
import sys
import subprocess

def which(program):
    """
    Check if command exists on linux enviornments

    This code written as suggested by http://stackoverflow.com/a/377028
    Update: change is_exe function to lambda function
            fix unused variable warning as pointed out by pylint
    """
    is_exe = lambda fpath: os.path.isfile(fpath) and os.access(fpath, os.X_OK)

    fpath, _ = os.path.split(program)
    if fpath:
        if is_exe(program):
            return program
    else:
        for path in os.environ['PATH'].split(os.pathsep):
            path = path.strip('"')
            exe_file = os.path.join(path, program)
            if is_exe(exe_file):
                return exe_file

    return None

def termsize():
    """
    Determine current terminal size

    This code written as suggested by http://stackoverflow.com/a/25730885
    """
    width, height = 60, 0
    with open('/dev/tty') as tty:
        size = subprocess.check_output(['stty', 'size'], stdin=tty).split()
        height, width = map(int, size)
    return (width, height, )

def lsb_release():
    """
    Get Linux Standard Base (LSB) information
    """
    data = subprocess.check_output(['lsb_release', '-a']).split()
    _os, codename = data[2].lower(), data[-1].lower()
    return (_os, codename, )

def update_aptitude():
    """
    Update apt-cache
    """
    cmd = 'apt-get update'
    ret = subprocess.call(cmd, shell=True, stdout=sys.stdout, stderr=sys.stderr)
    return ret

