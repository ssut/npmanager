"""
command utils for npmanager
"""
import os

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

